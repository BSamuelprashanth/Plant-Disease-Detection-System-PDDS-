# Plant Disease Detection System (PDDS)

## Introduction
The Plant Disease Detection System is a machine learning-based application that helps identify plant diseases using image processing and deep learning techniques. The system can classify plant leaves into different categories including Healthy, Powdery, Rust, and Invalid conditions.

## Project Structure
```
├── app.py                 # Flask web application
├── Model_Training.ipynb   # Jupyter notebook for model training
├── model.h5              # Trained model file
├── Dataset/              # Contains all image data
│   ├── Train/           # Training dataset
│   ├── Test/            # Testing dataset
│   └── Validation/      # Validation dataset
├── static/              # Static files for web interface
│   ├── css/            # CSS stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
├── templates/           # HTML templates
└── uploads/            # Directory for uploaded images
```

## Dataset Structure
The dataset is organized into three main directories:
1. **Train**: Contains training images categorized into:
   - Healthy
   - Invalid
   - Powdery
   - Rust

2. **Test**: Contains test images with the same categories
3. **Validation**: Contains validation images with the same categories

## Requirements
- Python 3.x
- TensorFlow
- Flask
- OpenCV
- NumPy
- Other dependencies (requirements.txt)

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sri-Galaxy/PDDS.git
   cd PDDS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup Gemini API key in app.py
    ```bash
    client = genai.Client(api_key="YOU_API_KEY")
    ```

## Usage
1. **Training the Model**:
   - Open `Model_Training.ipynb` in Jupyter Notebook
   - Run all cells to train the model
   - The trained model will be saved as `model.h5`

2. **Running the Web Application**:
   ```bash
   python app.py
   ```
   The application will start on `http://localhost:5000`

## Features
- Upload plant leaf images for disease detection
- Real-time classification
- Web-based user interface
- Support for multiple disease categories
- High accuracy disease detection

## Technologies Used
- Python
- TensorFlow/Keras
- Flask
- Bootstrap
- HTML/CSS/JavaScript
- jQuery

## Project Output
The system classifies plant leaves into four categories:
1. Healthy - Normal plant leaves
2. Powdery - Leaves affected by powdery mildew
3. Rust - Leaves affected by rust disease
4. Invalid - Unidentifiable or invalid images
