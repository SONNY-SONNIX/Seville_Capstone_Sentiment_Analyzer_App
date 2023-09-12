
  ## Deploying an Interactive Sentiment Analyzer with FastAPI, Docker and Transformers on Hugging Face 🩺🐳
  
 ### Introduction
 
The interactive sentiment analyzer App is a practical demonstration of applying Natural Language Processing (NLP) techniques to analyze the sentiment of movie reviews. 

In this project, we leverage FastAPI, a user-friendly interface, and Hugging Face's Transformers library, which offers pre-trained NLP models.

The goal is to create an interactive tool that allows users to input text and receive instant classification about whether the sentiment expressed in the text is positive or negative.

Sentiment analysis plays a pivotal role in understanding public opinion, customer feedback, and user sentiments in various domains, including the film industry.

By providing a user-friendly interface for sentiment analysis, this project showcases the potential for NLP applications and offers a practical solution for analyzing movie sentiments.


 # Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
| Capstone Project|The Sentiment Analysis Project| [Article] (https://medium.com/@otchie.sonny/deploying-an-interactive-sentiment-analyzer-with-gradio-and-transformers-on-hugging-face-f1025b3610a0)| [Deployed App](https://gyesibiney-sentiment-movie-review-fastapi-2.hf.space/docs) |

FastAPI

### Description 🚀📊

Building Machine Learning Applications on huggingface With FastAPI✨

Welcome to Deploying an Interactive Sentiment Analyzer with FastAPI and Transformers on Hugging Face! 

This project demonstrates how to build a movie sentiment analysis app using FastAPI and Hugging Face's Transformers library. 

Sentiment analysis, also known as opinion mining, is a natural language processing (NLP) task that involves determining the sentiment expressed in a piece of text. 

It uses a previously pre-trained hugging text classification model(roBERTa-case).
The project showcases a simple sentiment analysis app for movie reviews.
### Installation and Setup ⚙️

#### Getting Started

To run this application, follow these steps:

- Clone the Repository: Clone this repository to your local machine.


- Navigate to the Directory: Open a terminal and navigate to the cloned repository directory.


- Install Docker: Ensure that you have Docker installed on your machine. Docker documentation link : https://docs.docker.com/get-started/


- Build the Docker Image using this link https://huggingface.co/docs/hub/spaces-sdks-docker :

- Run the following command to build the Docker image:


#### Copy code

*docker build -t sepsis-prediction-app*

Run the Docker Container: Once the image is built, run the Docker container using the following command:


#### Copy code

*docker run -p 7860:7860 sepsis-prediction-app*

### Project Setup

It's important to note, we'll need to create a directory structure for our project:

sepsis_prediction_app/

├── Dockerfile

├── main.py

├── XGB.joblib

├── requirements.txt


#### Access the App: 

Open your web browser and navigate to http://localhost:7860 or https://sonny4sonnix-sepsis-prediction-app-using-fastapi-1.hf.space/docs.

You'll be greeted with a welcome message!

# Endpoints 📡

### Root Endpoint 🌐

- Endpoint: /

- Method: GET

- Description: Welcome message to the Sepsis Prediction API.

- Response: {"message": "Welcome to the Sepsis Prediction using FastAPI"}

### Prediction Endpoint 🔮

Use the /predict/docs endpoint to predict sepsis for a patient. 

Send a POST request with the following input parameters:

- prg: Plasma glucose
  
- pl: Blood Work Result-1 (mu U/ml)
  
- pr: Blood Pressure (mm Hg)
  
- sk: Blood Work Result-2 (mm)
  
- ts: Blood Work Result-3 (mu U/ml)
  
- m11: Body mass index (weight in kg/(height in m)^2)
  
- bd2: Blood Work Result-4 (mu U/ml)
  
- age: Patient's age (years)

#### Response: 

{"prediction": "Patient does not have sepsis"} or {"prediction": "Patient has sepsis"}

### Technologies Used 🛠️

- FastAPI: A modern, fast, web framework for building APIs with Python.
  
- Docker: A platform for developing, shipping, and running applications in containers.
  
- XGBoost: A machine learning library for gradient boosting.
  
### Project Structure 📂

- *main.py:* Contains the FastAPI application code and endpoint definitions.

- *XGB.joblib:* The pickled machine learning model used for sepsis prediction.

- *Dockerfile:* Specifies the Docker image configuration.

- *requirements.txt:* Lists the Python dependencies required for the app.

- *Other files and directories:* Application files and directories.


### Conclusion and Next Steps 🏁

This FastAPI application demonstrates how to predict sepsis using a machine learning model. 

Dockerization makes deployment hassle-free. Feel free to customize and extend the app for your own projects!

#### License 📜

This project is licensed under the MIT License.

#### Conclusion 🎉

Congratulations! You've successfully set up the Sepsis Prediction FastAPI application using Docker.

This app provides a simple and efficient way to predict sepsis using patient data.

#### 👥 Authors

This project is developed and maintained by:

Sonny Agorvor -Otchie feel free to reach out to me with any questions or feedback!

#### ✨ Acknowledgments

I would like to express my gratitude to The Azubi Africa team for their valuable contributions to this project.

#### 📞 Contact

For any questions, concerns, or suggestions regarding this project, please contact us at otchie.sonny@gmail.com.



 

