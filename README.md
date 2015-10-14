# leap_facial_detection
Scripts for Kaggle facial detection competition.

#technical goal
The goal of this project is to predict the location of 31 face key points (eg: left_eye_center, right_eye_center, etc.) based on the grayscale image only, using neural networks. This is why the X variable (the features) contains the "image" column, while y contains the target variables (the 31 face key points).

# Easy install
Log in to EC2 AWS, and clone the github repo with:

git clone NAME_OF_REPO

Then, simply run the 2 bash scripts to setup:

- source installCUDA1.sh
- source installCUDA2.sh

This should setup all the python packages on the machine. Then, follow README_setupAWS.md to download the datasets onto the machine in "~/data/", and run the python script output.py which should produce a kaggle.csv file in "neural_network/". This is the file you need to submit to kaggle.
