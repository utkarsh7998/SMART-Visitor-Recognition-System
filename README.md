## CONTENTS:<br>
The folder contains 7 files and 2 folders: <br>
### 1. Files <br>
	1.1. constants.py <br>
	1.2. data_prep.py <br>
	1.3. prediction.py <br>
	1.4. roles.json <br>
	1.5. telegramnotification3.py <br>
	1.6. trained_knn_model.clf <br>
	1.7. training.py <br>
	1.8. README.txt <br>
2. Folders <br>
 	2.1. image dataset: The folders gets updated dynamically with the code <br>
 	2.2 analysis: Contains the required dataset and code used for face encoding and encoding classification analysis <br>
	
Required Packages: <br>
* cv2 <br>
* skimage <br>
* face_recognition <br>
* telegram-bot <br>
* PIL <br>
* seaborn, keras (These packages are only required for analysis. Main code can run without it) <br>


# How to run the code: <br>
### * Smart Visitor Recognition code: <br>
   * Make sure you are in the source directory <br>
   * Run prediction.py file to predict the person who comes to the door. <br>
   * Run data_prep.py to register a new person to the system.<br>
   
### * Analysis Code: <br>
   * Run knn_analysis.ipynb notebook to run the code for KNN classifier. <br>
   * Run svm_analysis.ipynb notebook to run the analysis for the SVM classifier. <br>
   * Run encoding_analysis.ipynb notebook the get analysis on encoding method comparison. <br>
   * Train_test.py code is to be run to make a separate testing folder. This code only needs to run one time and has already been executed so no need to run again. <br>
