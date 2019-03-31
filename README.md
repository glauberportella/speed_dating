Bonjour! My name is Mohit. This code works well on python 3. The core logic is developed with help from nice python libraries i.e. pandas and numpy. I use matplotlib for plotting graphs.The preprocessing code is stored in preprocess.py. The graph plotting for question 2 is in 2_1.py and 2_2.py. The code for conversion of continuous valued columns to discrete values is written in discretize.py. The split.py file has logic for splitting the data stored in data-binned.csv file to training and testing dataset in 80-20 ratio.

Finally, the naive bayes classifier algorithm is written in 5_1.py file. The main logic is in function named nbc(t_frac). In 5_2.py and 5_3.py, there is code for plotting graphs for variation of number of bins with accuracy and fraction of training data with accuracy respectively.

The detailed report can be found in CS573_HW2.pdf. The homework instructions can be found in hw2.pdf.

Kindly note that a single run of 5_1.py which contains the Naive Bayes Classifier implementation takes around 4-5 seconds. This includes calculating all model parameters i.e. the prior probabilities, the conditional probabilities for attributes given the label and the posterior probability of label. This also includes the inference step performed on the entire training and test dataset which have approximately 5000 and 1300 datapoints respectively. The primary reason for my fast inference step is the usage of pandas apply method! I would love to learn more about other efficient implementations for the Naive Bayes Algorithm. 

Happy Coding!
