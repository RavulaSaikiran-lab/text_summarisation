#text summarisation tool

#pip install transformers torch

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
int=("enter the text")
text = """
In the age of time travel, tourism exploded for the rich.
Meet an ancestor, kill a relative, spare a dictator, all now possible.
No-one thought about the pathogens hitching a lift backwards. Time to fester, to develop resistance—to rule.
In the age of time travel, pandemics slaughtered the poor.
"""

summary = summarizer(text, max_length=150, min_length=50, do_sample=True)
summarizer('text',max_length=30)
print(summary[0]["summary_text"])
