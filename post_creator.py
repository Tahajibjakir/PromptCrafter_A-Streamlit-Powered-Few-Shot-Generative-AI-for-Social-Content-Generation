from LLM_helper import llm
from post_examples import PostExamples

examples = PostExamples()

def map_length_to_range(length_label):
    """Convert length category to text line range."""
    mapping = {
        "Short": "1–6 lines",
        "Medium": "7–12 lines",
        "Long": "13–18 lines"
    }
    return mapping.get(length_label, "7–12 lines")

def build_prompt(length, lang, topic, num_examples=2):
    """Assemble the prompt including few-shot examples if available."""
    range_description = map_length_to_range(length)

    base = f"""Write a LinkedIn post using the details below. Do not add any introduction.

- Topic: {topic}
- Expected Length: {range_description}
- Language: {lang} 
(Note: If Banglish, mix Bangla and English, but use English script.)"""

    sample_posts = examples.fetch_examples(length, lang, topic)

    if sample_posts:
        base += "\n\nReplicate the style shown in the following sample(s):"
        for idx, sample in enumerate(sample_posts[:num_examples]):
            base += f"\n\nSample {idx + 1}:\n{sample['text']}"

    return base

def create_linkedin_post(length, lang, topic):

    prompt = build_prompt(length, lang, topic)
    output = llm.invoke(prompt)
    return output.content


if __name__ == "__main__":
    result = create_linkedin_post("Short", "Banglish", "Self Growth")
    print(result)
