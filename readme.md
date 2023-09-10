  ## Deploying an Interactive Sentiment Analyzer with Gradio and Transformers on Hugging Face
  
 ### Introduction
 
The Movie Sentiment Analysis App is a practical demonstration of applying Natural Language Processing (NLP) techniques to analyze the sentiment of movie reviews. 

In this project, we leverage Gradio, a user-friendly interface, and Hugging Face's Transformers library, which offers pre-trained NLP models.

The goal is to create an interactive tool that allows users to input movie reviews and receive instant predictions about whether the sentiment expressed in the review is positive, negative, or neutral.

Sentiment analysis plays a pivotal role in understanding public opinion, customer feedback, and user sentiments in various domains, including the film industry.

By providing a user-friendly interface for sentiment analysis, this project showcases the potential for NLP applications and offers a 
practical solution for analyzing movie sentiments.

# Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
| Capstone Project|The Sentiment Analysis Project| [Article]()| [Deployed App]() |

Gradio_App

Building Machine Learning Applications on huggingface With Gradio ✨


## 📖 Table of Contents

+ Description

+ Dataset Overview

+ Project Setup

+ Building the Sentiment Analysis App

+ Running the App

+ Project Structure

+  License

+ Resources

+ Conclusion

  ##  Description 🚀📊

Welcome to Deploying an Interactive Sentiment Analyzer with Gradio and Transformers on Hugging Face! 

This project demonstrates how to build a movie sentiment analysis app using Gradio and Hugging Face's Transformers library. 

Sentiment analysis, also known as opinion mining, is a natural language processing (NLP) task that involves determining the sentiment expressed in a piece of text. 

It uses a previously pre-trained hugging text classification model(roBERTa-case).
The project showcases a simple sentiment analysis app for movie reviews.

### Dataset Overview 

The dataset used for this project contains movie reviews along with binary sentiment polarity labels. 

It serves as a benchmark for sentiment classification, with labels indicating whether the sentiment is positive or negative. 

Neutral sentiment is also considered as a class.

## Installation and Setup ⚙️🔧 

To get started, follow these installation steps:

# set up the environment on Windows by running the following code.

Make sure you have Python installed on your system.

- Clone this repository to your local machine.
  
  git clone <repository-url>

  - Navigate to the project directory.

  cd <project-directory>

- Set up a virtual environment (optional but recommended).

python -m venv myenv

- Activate the virtual environment.

### On Windows:

- myenv\Scripts\activate

  ### On macOS and Linux:

- source myenv/bin/activate

  

### Install the required packages.

- pip install -r requirements.txt

   ### The Two commands are of the same structure

1. Activate the python environment 

2. Upgrade pip to its current version 

3. Install the requirements located in requirements.txt: You should be at the root of your env

## 🚀 Usage

### To see how the app works, follow these instructions: 

1. After setting up environment, activating the environment, and installing requirements, type

gradio run <python_script> # in the terminal

This will open the App in your browser

### Project Setup
Before running the app, make sure you have installed the required 
dependencies listed in the requirements.txt file:

* transformers

* gradio

* torch

### You can install these dependencies using pip:

 pip install -r requirements.txt

### Building the Sentiment Analysis App

The app is built using Gradio and Hugging Face's Transformers library. 

The Python script app.py contains the app logic. 

Here's an overview of the key steps:

1. Load a pre-trained sentiment analysis model from Hugging Face's model hub using AutoModelForSequenceClassification and AutoTokenizer. Replace model_name with the name of the model you want to use.

2. Define a function get_sentiment that takes the input text (movie review) and returns the predicted sentiment label (positive, negative, or neutral).

3. Create a Gradio interface using gr.Interface. Specify that the function expects text input and produces text output.

 4. Launch the Gradio interface with iface.launch(inline=True).





