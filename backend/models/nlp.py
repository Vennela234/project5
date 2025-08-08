from transformers import pipeline

qa_pipeline = pipeline("question-answering")
summarizer = pipeline("summarization", model="t5-small")

def get_answer(context, question):
    return qa_pipeline({"context": context, "question": question})

def summarize_text(text):
    return summarizer(text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]
