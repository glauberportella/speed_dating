import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

participant_cols = ['attractive_important', 'sincere_important', 'intelligence_important', 'funny_important', 'ambition_important', 'shared_interests_important']    

def get_print_participant_mean(dataframe):
    mean_scores = []
    for i in range(0,6):
        participant_mean = dataframe[participant_cols[i]].sum()/len(dataframe[participant_cols[i]])
        # print ('Mean of ', participant_cols[i], ':', round(participant_mean, 2))
        mean_scores.append(participant_mean)
    return mean_scores

def main():

    dating = pd.read_csv('dating.csv')

    dating_female = dating[dating['gender'] == 0]
    dating_male = dating[dating['gender'] == 1]
    female_mean_scores = get_print_participant_mean(dating_female)
    male_mean_scores = get_print_participant_mean(dating_male)

    ind = np.arange(6)
    width = 0.35
    # plt.figure(figsize=(10,10))
    plt.gcf().subplots_adjust(bottom=0.45)
    p1 = plt.bar(ind, female_mean_scores, width,color = 'pink')
    p2 = plt.bar(ind+width, male_mean_scores, width, color = 'blue')
    plt.ylabel('Mean Scores')
    plt.title('Preference scores of participants by gender')
    plt.xticks(ind+width/2, (participant_cols[0], participant_cols[1], participant_cols[2], 
                     participant_cols[3], participant_cols[4], participant_cols[5]), rotation=70)
    plt.yticks(np.arange(0,0.5,0.05))
    plt.legend((p1[0], p2[0]), ('Female', 'Male'))
    plt.savefig('gender_barplot')
    # plt.show()
    

if __name__ == '__main__':
    main()