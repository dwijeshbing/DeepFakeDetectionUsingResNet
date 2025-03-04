# DeepFake Detection Using ResNet

## Overview
DeepFake Detection Using ResNet is a machine learning project that leverages deep learning to detect deepfake videos. The system consists of a Django web application integrated with a ResNet-based model for classification.

## Prerequisites
- Python 3.x
- Django
- PyTorch
- Virtual Environment (venv)
- Required dependencies (listed in `requirements.txt`)

## Repository Structure
```
DeepFakeDetectionUsingResNet/
    ├── Django_Application/
    ├── Model_Creation/
```

## Setup Instructions

### Step 1: Accessing the Code Repository
Clone the repository to your local system:
```sh
git clone <repository_url>
```

### Step 2: Setting Up the Virtual Environment
Before running the project, create and activate a Python virtual environment:

**Creating a Virtual Environment:**
```sh
python -m venv myenv
```

**Activating the Virtual Environment:**
- On Windows (CMD):
  ```sh
  myenv\Scripts\activate
  ```
- On Mac/Linux:
  ```sh
  source myenv/bin/activate
  ```
For further details, refer to the official Python documentation on virtual environments.

### Step 3: Navigating to the Django Application Directory
```sh
cd DeepFakeDetectionUsingResNet/Django_Application
```

### Step 4: Installing Required Dependencies
Install all required packages using:
```sh
pip install -r requirements.txt
```

### Step 5: Preparing the Dataset
Place your dataset files in the `DataSetPreparation/` directory before proceeding.

### Step 6: Data Preprocessing
Navigate to the `Model_Creation/` folder and open `preprocessing.ipynb`. Modify file paths as necessary and execute all notebook cells to preprocess the dataset.

### Step 7: Model Training
Once preprocessing is complete, open `Model_and_training.ipynb` to train the deepfake detection model. Adjust hyperparameters such as:
- Number of epochs
- Learning rate

Run the notebook until training is completed.

### Step 8: Saving the Trained Model
After training, save the model in `.pt` format for later use:
```sh
model.save("model.pt")
```

### Step 9: Deploying the Model in Django
Copy the saved `.pt` model file into the following directory:
```
DeepFakeDetectionUsingResNet/Django_Application/models/
```
This allows the Django application to use the trained model for predictions.

### Step 10: Starting the Django Server
Run the following command inside the `Django_Application/` directory:
```sh
python manage.py runserver
```

### Step 11: Verifying Successful Setup
Upon successful execution, the server will start, and you should see an output similar to:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 12: Using the Web Application
- Open the provided server URL in a web browser.
- Upload a video to analyze.
- The system will classify the video as real or deepfake with confidence scores.

## License
This project is open-source and available for modifications and contributions.

