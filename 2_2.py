import numpy as np
import pandas as pd

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
mpl.rcParams['figure.figsize'] = (7,7)


def get_success_rate(dataframe, attribute, value):
    dating_attribute_value = dataframe[dataframe[attribute] == value]
    dating_success = dating_attribute_value[dating_attribute_value['decision'] == 1]
    return len(dating_success)*1.0/len(dating_attribute_value)

def get_distinct_values_rating_partner(dataframe, attribute):
    # print (dataframe[attribute].nunique()) 
    return (dataframe[attribute].unique())

def main():

    dating = pd.read_csv('dating.csv')

    rating_partner_participant = ['attractive_partner','sincere_partner','intelligence_parter', 
                             'funny_partner', 'ambition_partner', 'shared_interests_partner']
    unique_values = []
    for i in range(0,6):
        unique_values.append(get_distinct_values_rating_partner(dating, rating_partner_participant[i]))

    success_rates_all_attributes = []
    for i in range(6):
        success_rate_attribute = []
        for value in unique_values[i]:
            success_rate_attribute.append(get_success_rate(dating, rating_partner_participant[i], value))
        success_rates_all_attributes.append(success_rate_attribute)

    for i in range(6):
        area = np.pi*3
        plt.figure(figsize=(8,8))
        plt.scatter(unique_values[i], success_rates_all_attributes[i], s=area)

        plt.title('Scatter Plot for Partners who Perform Well on ' + rating_partner_participant[i])
        plt.xlabel('Attribute Value for ' + rating_partner_participant[i])
        plt.ylabel('Success Rate')

        plt.xticks(np.arange(0,11,1))
        plt.yticks(np.arange(0,1.1,0.1))
        plt.savefig('scatter_plot_' + rating_partner_participant[i])
        # plt.show()

if __name__ == '__main__':
    main()