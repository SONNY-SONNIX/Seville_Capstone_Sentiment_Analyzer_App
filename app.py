import gradio as gr 
import transformers as pipeline 
from transformers import AutoTokenizer,AutoModelForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_name = "Sonny4Sonnix/Roberta-capstone_2"  # Replace with the name of the pre-trained model you want to use
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

sentiment = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def get_sentiment(input_text):
    result = sentiment(input_text)
    sentiment_label = result[0]['label']
    sentiment_score = result[0]['score']
    
    if sentiment_label == 'LABEL_1':
        sentiment_label = "positive"
    elif sentiment_label == 'LABEL_0':
        sentiment_label = "neutral"
    else:
        sentiment_label = "negative"
    
    return f"Sentiment: {sentiment_label.capitalize()}, Score: {sentiment_score:.2f}"


iface = gr.Interface(fn=get_sentiment,title="Sentimental Analysis", inputs="text",outputs="text")
iface.launch(inline=True)
