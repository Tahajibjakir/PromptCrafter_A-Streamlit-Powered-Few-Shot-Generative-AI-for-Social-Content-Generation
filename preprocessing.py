import json
from LLM_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def enrich_and_save_posts(raw_path, output_path=None):
    with open(raw_path, encoding='utf-8') as f:
        raw_posts = json.load(f)

    processed_posts = []
    for entry in raw_posts:
        try:
            metadata = extract_post_info(entry['text'])
            combined = {**entry, **metadata}
            processed_posts.append(combined)
        except Exception as e:
            continue  # optionally log error here

    tag_map = unify_tags_across_posts(processed_posts)
    for post in processed_posts:
        post['tags'] = [tag_map.get(tag, tag) for tag in post['tags']]

    with open(output_path, 'w', encoding='utf-8', errors='ignore') as out:
        json.dump(processed_posts, out, indent=4, ensure_ascii=False)


def extract_post_info(text):
    clean_text = text.encode('utf-8', 'ignore').decode('utf-8')
    prompt = """
    You're analyzing a LinkedIn post. Extract and return the following in a JSON:
    - Total number of lines (line_count)
    - Language (English or Banglish — Banglish means a mix of Bengali and English, written in English script)
    - Up to two tags describing the topic of the post

    Return a valid JSON with exactly these keys: line_count, language, tags.
    Here's the post:
    {post}
    """
    prompt_template = PromptTemplate.from_template(prompt)
    chain = prompt_template | llm
    response = chain.invoke({"post": clean_text})

    try:
        return JsonOutputParser().parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse metadata from post.")


def unify_tags_across_posts(posts):
    all_tags = set(tag for post in posts for tag in post['tags'])
    tag_string = ', '.join(all_tags)

    unification_prompt = """
    Given a list of topic tags, group and rename them under unified categories. Examples:
    - "Jobseekers", "Job Hunting" → "Job Search"
    - "Motivation", "Inspiration" → "Motivation"
    - "Scam Alert", "Job Scam" → "Scams"

    Use title case (e.g., "Job Search"). Return a JSON map of original → unified tags.

    Tags:
    {tags}
    """
    prompt_template = PromptTemplate.from_template(unification_prompt)
    chain = prompt_template | llm
    response = chain.invoke({"tags": tag_string})

    try:
        return JsonOutputParser().parse(response.content)
    except OutputParserException:
        raise OutputParserException("Tag unification failed.")


if __name__ == "__main__":
    enrich_and_save_posts("dataset/linkedin_raw_data.json", "dataset/linkedin_clean_data.json")
