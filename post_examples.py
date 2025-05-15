import pandas as pd
import json

class PostExamples:
    def __init__(self, dataset_path="dataset/linkedin_clean_data.json"):
        """Initialize and preprocess the dataset for few-shot sampling."""
        self.dataset = None
        self.all_topics = None
        self._load_dataset(dataset_path)

    def _load_dataset(self, path):
        with open(path, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
            df = pd.json_normalize(raw_data)
            df['category'] = df['line_count'].apply(self._assign_length_label)
            self.dataset = df

            tag_lists = df['tags'].apply(list)
            self.all_topics = sorted(set(tag for tags in tag_lists for tag in tags))

    def _assign_length_label(self, lines):
        if lines < 5:
            return "Short"
        elif 5 <= lines <= 10:
            return "Medium"
        else:
            return "Long"

    def fetch_examples(self, desired_length, language, topic):
        """Return filtered posts based on length, language, and topic tag."""
        filtered = self.dataset[
            self.dataset['tags'].apply(lambda tags: topic in tags) &
            (self.dataset['language'] == language) &
            (self.dataset['category'] == desired_length)
        ]
        return filtered.to_dict(orient="records")

    def available_tags(self):
        """Return all unique topic tags from the dataset."""
        return self.all_topics


if __name__ == "__main__":
    ex = PostExamples()
    posts = ex.fetch_examples("Medium", "English", "AI")
    print(posts)
