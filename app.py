import gradio as gr 
import transformers as pipeline 
from transformers import AutoTokenizer,AutoModelForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_name = "Sonny4Sonnix/Roberta-capstone_2"  # Replace with the name of the pre-trained model you want to use
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

sentiment = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)









iface = gr.Interface(fn=get_sentiment,title="Sentimental Analysis", inputs="text",outputs="text")
iface.launch(inline=True)
