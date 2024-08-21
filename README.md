# Development-of-a-Network-Anomaly-Detection-System-for-Enhanced-Cybersecurity
**OVERVIEW:** This project aims to detect Distributed Denial of Service (DDoS) attacks using machine learning models, specifically RandomForest. The project includes steps for data preprocessing, feature engineering, model training, and deployment.

**PROJECT CONTENTS:**
├── cicddos2019_dataset.csv # Raw dataset

├── cleaned_dataset.csv # Cleaned dataset used for model training

├── final_model.pkl # Trained Random Forest model

├── final_model.txt # Model description

├── features.txt # List of features used in the model

├── scaler.pkl # Scaler used to standardize the features

├── Code.ipynb # Jupyter Notebook with all code (preprocessing,
training, prediction)

├── README.pdf # This file

**INSTALLATION AND SETUP:**
Prerequisites:
--Python 3.7 or higher
--Jupyter Notebook
--pip (Python package installer)
INSTALLATION:
1. Unzip the project folder.
2. Navigate to the project directory:
cd ddos_detection
3. Create a virtual environment (optional but recommended):
   python -m venv venv 
4. Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS/Linux::
source venv/bin/activate

5. Install the required dependencies by running the following command:
pip install -r requirements.txt
Run the Python app:
python app.py

6. The Flask app will run on http://127.0.0.1:5000/ . You can now test the API using
Postman.

Postman Steps
1. Open Postman:
Download and install Postman if you haven't already:
https://www.postman.com/downloads/

3. Create a New Request:
Click on "New" in the top left corner and select "Request".

4. Set Request Type:
Change the request type to POST .
Enter the URL:
In the request URL field, enter: http://127.0.0.1:5000/predict

5. Set the Request Body:
Click on the "Body" tab.
Select "raw" and choose "JSON" from the dropdown menu.
Paste the following example JSON data (modify as needed): (Open Postman_commands.json for commands)
