CS698T PROJECT
GROUP NUMBER: 02


MEMBERS: 
* Manjyot Singh Nanra(21111038)
* Sharanya Saha(21111056)
* Shiv Kumar Yadav(21111057)
* Utkarsh Shrivastava(21111063)


CONTENTS:
The folder contains 7 files and 2 folders:
1. Files
	1.1. constants.py
	1.2. data_prep.py
	1.3. prediction.py
	1.4. roles.json
	1.5. telegramnotification3.py
	1.6. trained_knn_model.clf
	1.7. training.py
	1.8. README.txt
2. Folders
 	2.1. image dataset: The folders gets updated dynamically with the code
 	2.2 analysis: Contains the required dataset and code used for face encoding and encoding classification analysis
	
Required Packages:
* cv2
* skimage
* face_recognition
* telegram-bot
* PIL
* seaborn, keras (These packages are only required for analysis. Main code can run without it)


How to run the code:
* Smart Visitor Recognition code:
   * Make sure you are in the source directory
   * Run prediction.py file to predict the person who comes to the door.
   * Run data_prep.py to register a new person to the system.
* Analysis Code:
   * Run knn_analysis.ipynb notebook to run the code for KNN classifier.
   * Run svm_analysis.ipynb notebook to run the analysis for the SVM classifier.
   * Run encoding_analysis.ipynb notebook the get analysis on encoding method comparison.
   * Train_test.py code is to be run to make a separate testing folder. This code only needs to run one time and has already been executed so no need to run again.


For any queries, please contact Manjyot singh Nanra(manjyots21@iitk.ac.in) or Sharanya Saha(sharanya21@iitk.ac.in)
