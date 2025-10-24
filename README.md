# MNIST digit recognition using Convolutional Neural Networks

This project explores digit recognition using Convolutional Neural Networks (CNNs) with the MNIST dataset. 
It involves building and training models in TensorFlow/Keras to classify handwritten digits.
It also includes a simple app (`main.py`) where you can handwrite a digit and see real time predictions from the saved model.

## Project Overview
- **Datasets:** MNIST digits. Source: https://www.kaggle.com/datasets/hojjatk/mnist-dataset?resource=download  
- **Model:** CNN.  
- **Techniques:** Data Augmentation, Dropout, Early Stopping, LRS, Batch Normalization  
- **Goal:** Classify handwritten digits into one of 10 categories i.e. 0-9.  

## Project Structure

📂 digit-recognition-MNIST  <br>
│<br>
├── 📂 model/mnist_model.keras&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #Saved model <br> 
├── main.py <br>
├── character-reader.ipynb&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main script  
├── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Project Dependencies  
└── .gitignore 

---

## Installation and Setup

1. Set the destination folder <br>
Create or navigate to the folder where you want this project to be located:

2. Clone the repository:
    ```bash
    git clone https://github.com/P-Alakara/digit-recognition-MNIST.git
    ```

3. Navigate to the newly created folder.
   ```bash
    cd digit-recognition-MNIST
    ```
   
5. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # venv\Scripts\activate (for windows systems)
    ```

6. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
 7. Run the app
    ```bash
    python main.py
    ```
        
---

