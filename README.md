# PromptCrafter_A-Streamlit-Powered-Few-Shot-Generative-AI-for-Social-Content-Generation
PromptCrafter is a powerful and user-friendly Generative AI web application that automatically generates LinkedIn-style social media posts using few-shot learning, structured prompt engineering, and LLM-based text generation. Designed with both practical applications and academic relevance in mind, this tool demonstrates how modern LLMs can be customized for creative content generation through a clean UI and intelligent prompt chaining. Built using Streamlit as the frontend and LangChain with Groq’s LLaMA 3.3-70 b-versatile as the backend LLM, the app allows users to select the desired topic, length, and language (English or Banglish) for the post. It then dynamically generates a well-structured LinkedIn post by sampling from a curated dataset of examples.

# Demo (Performance)
![Image](https://github.com/user-attachments/assets/a94be5a4-140c-441c-af25-aa9818572c62)

# Features
✅ Streamlit UI with left–right layout for intuitive interaction and real-time preview <br/>
✅ Few-Shot Learning powered by post filtering based on tags, length, and language <br/>
✅ Prompt Construction Pipeline using LangChain with preloaded examples <br/>
✅ Groq LLaMA 3 Integration for blazing fast LLM responses <br/>
✅ Preprocessing Module to extract metadata (tags, language, line count) from raw posts <br/>
✅ Tag Unification using an LLM to standardize tags for consistency <br/>
✅ Multilingual Output with support for English and Banglish <br/>
✅ Structured JSON Dataset for scalability and reproducibility <br/>
✅ Ideal for showcasing in AI research, LLM-powered tools, or portfolio projects <br/>

# Installation

git clone https://github.com/yourusername/linkedin-post-generator.git
cd linkedin-post-generator

Create virtual env (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

# Model Details
This project uses Groq-hosted LLaMA-3.3-70 b-versatile via the langchain_groq integration for fast and efficient generation.<br\> The LLM is guided through a few-shot prompt strategy where example posts are dynamically injected based on selected inputs like topic, length, and language.

Model Type: Generative Large Language Model (Groq LLaMA 3)

Prompt Strategy: Few-shot learning using LangChain’s PromptTemplate module

Response Parsing: Handled using JsonOutputParser for structured metadata extraction (line count, tags, etc.)

Metadata Extraction: Custom LangChain prompt to extract metadata from raw posts during preprocessing

Tag Normalization: Another LLM-based prompt pipeline to unify diverse tags into a controlled set for consistency

# Project Structure

PromptCrafter/
├── data/
│   ├── raw_post_data.json           # Raw LinkedIn posts (unprocessed)
│   └── structured_post_data.json    # Processed posts with language, tags, line count
│
├── main.py                          # Streamlit UI and frontend layout
├── few_shot.py                      # Few-shot filtering logic (based on topic, language, length)
├── post_generator.py                # Constructs final prompt and invokes LLM
├── preprocessing.py                 # Metadata extraction + tag unification from raw posts
├── LLM_helper.py                    # Groq LLaMA 3 setup via LangChain
│
├── requirements.txt                 # Project dependencies
└── README.md       

# Results & Screenshots

# Contributing
Contributions are welcome! Please open an issue or submit a pull request.


# Contact / Credits
Developed by Tahajib Jakir Khan  
📧 tahajibjakirkhan00@gmail.com 
📎 [LinkedIn](https://www.linkedin.com/in/tahajib-jakir-khan-53b30822b/)
