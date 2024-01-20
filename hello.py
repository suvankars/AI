from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I've been waiting for this course whole life")

print(res)
