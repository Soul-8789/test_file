# Django Project Setup Guide

This guide provides detailed instructions on how to set up, run, and manage this Django project on your local system.

## Prerequisites

Ensure the following are installed on your system:
- Python (>= 3.8)
- pip (Python package manager)
- virtualenv (optional but recommended)
- Git

## Getting Started

Follow these steps to get the project running locally.

### 1. Clone the Repository

git clone <repository_url>
cd <project_directory>

### create a virtual environment 
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


## install the requirements.txt 
pip install -r requirements.txt


## then run this two command 
python manage.py makemigrations
python manage.py migrate


### this are the api we can you for our testing file
*** add the authorization token while run the file in postman ****
![api file](https://github.com/user-attachments/assets/c581f0cf-cd35-4dff-9e93-ede87269a4ec)
