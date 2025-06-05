# OpenAI Poetry Chatbot

## Overview

This project is a poetry chatbot designed to test the capabilities of OpenAI's GPT-3.5 and GPT-4 models. By leveraging the OpenAI API, the chatbot generates poetic responses based on user prompts, showcasing the creative potential of advanced language models.

##  Features

- **GPT-3.5 and GPT-4 Integration**: Utilizes OpenAI's latest language models to generate poetry.
- **User-Friendly Interface**: Interactive frontend for users to input prompts and receive poetic responses.
- **Backend API**: Handles prompt processing and communicates with OpenAI's API.
- **Database Integration**: Stores user interactions and generated poems for analysis and improvement.

## Project Structure

openai_poetry_app/
├── app.py # Main application script
├── config.py # Configuration settings
├── poetry_app.sql # SQL schema for the database
├── templates/ # HTML templates for the frontend
│ └── index.html # Main interface page
├── pycache/ # Compiled Python files
└── README.md # Project documentation



##  Installation

1. **Clone the Repository**:

   git clone https://github.com/sriram7737/openai_poetry_app.git
   cd openai_poetry_app
Set Up a Virtual Environment (Optional but recommended):


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:


pip install -r requirements.txt
Configure OpenAI API Key:

Obtain your API key from OpenAI.

Set the API key as an environment variable:


export OPENAI_API_KEY='your-api-key-here'
Initialize the Database:

Set up the database using the provided poetry_app.sql schema.

## Usage
Run the Application:

python app.py
Access the Chatbot:

Open your web browser and navigate to http://localhost:5000.

Enter a prompt, and the chatbot will generate a poetic response using GPT-3.5 or GPT-4.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.
