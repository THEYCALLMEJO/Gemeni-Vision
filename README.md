# Gemini Vision | Gemini Vision

![Gemini Vision ](Demo.mp4)

## Overview 

This project is a Streamlit-based application that allows users to upload images and ask questions about them using the Gemini AI model. The application leverages generative AI to provide insightful responses based on the uploaded images and user queries.

## Features
- **Image Upload**: Users can upload images in various formats (PNG, JPG, WEBP).
- **Interactive Q&A**: Engage with the AI by asking questions about the uploaded image.
- **User-Friendly Design**: A simple and intuitive interface built with Streamlit.
- **Environment Variable Management**: Securely manage API keys using dotenv.

## Technologies Used
- **Python**: The primary programming language for development.
- **Streamlit**: For building the user interface.
- **Google Gemini API**: For generating responses based on images and queries.
- **dotenv**: For managing environment variables.
- **Pillow**: For image processing.

## Getting Started

### Dependencies

This code uses the following libraries:

- `streamlit`: for building the user interface.
- `google.generativeai`: for generating responses using the Gemini model.
- `python-dotenv`: for managing environment variables.
- `Pillow`: for handling image uploads and proccess it in any way

### Contributing

We welcome contributions to enhance the Gemini PicAnalyzer! Here’s how you can get involved:

#### How to Contribute
1. **Fork the Repository**: Click on the "Fork" button at the top right of this page.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/THEYCALLMEJO/Gemeni-Vision.git

### Usage

Follow these steps to set up and run the project:
1. Initially Clone the repository:
   
   git clone https://github.com/THEYCALLMEJO/Gemeni-Vision.git
   

2. Create a virtual environment:
   
   python3 -m venv my_env
   source my_env/bin/activate 
   # For Windows
   .\my_env\Scripts\activate 
   

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Run the Streamlit server:
   
   streamlit run app.py
   

5. Access the application in your browser at [http://localhost:8501](http://localhost:8501).

6. Start analyzing images with the assistant!

### Repository Structure
repository/
├── main.py                       # the code and UI integrated together live here
├── requirements.txt             # the python packages needed to run locally
├── Demo.mp4              # demo of the application
├── Readme.md
├── .gitignore

## How it Works
1. The user uploads an image using the file uploader.
2. The user enters a question related to the uploaded image.
3. The input query and image are sent to the Gemini model for processing.
4. The Gemini model generates a response based on the image and the user's question.
5. The application displays the response to the user.```