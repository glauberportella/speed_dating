import pandas as pd
import numpy as np

partner_cols = ['pref_o_attractive','pref_o_sincere','pref_o_intelligence','pref_o_funny','pref_o_ambitious','pref_o_shared_interests']
participant_cols = ['attractive_important', 'sincere_important', 'intelligence_important', 'funny_important', 'ambition_important', 'shared_interests_important'] 
non_binned_cols = ['gender', 'race', 'race_o', 'samerace', 'field', 'decision']   

def get_binned_column(dataframe, column, num_bins, bin_range):
    dataframe[column] = pd.cut(dataframe[column], bin_range, include_lowest = True,
                               labels = np.arange(num_bins), retbins = False)
    return dataframe[column]

def do_discretize(num_bins):
    dating = pd.read_csv("dating.csv")
    '''
    clean data for columns gaming and reading
    '''
    column = 'gaming'
    range_highest = 10
    dating.loc[dating[column] > range_highest,column] = range_highest
    dating.loc[dating['reading'] > range_highest,'reading'] = range_highest

    age_cols = ['age', 'age_o']
    for column in dating:
        if column not in non_binned_cols:
            bin_range = np.arange(0,10.00000001,(10-0)/num_bins)
            '''
            Change bin range if needed
            '''
            if column in age_cols:
                bin_range = np.arange(18,58.00001,(58-18.0)/num_bins)
    #             print ("bin range for age ", column)
            elif column in partner_cols or column in participant_cols:
                bin_range = np.arange(0,1.000001,(1.0)/num_bins)
    #             print ("different bin range ", column)
            elif column == 'interests_correlate':
                bin_range = np.arange(-1,1.000001,(1+1.0)/num_bins)
    #             print ("interest column", column)
            
            '''
            get binned column
            '''
            # print ("for column ", column, "num of bins ", num_bins, " len of bin range ", bin_range)
            dating[column] = get_binned_column(dating, column, num_bins, bin_range)


    dating.to_csv("dating-binned.csv", index = False)
    return dating

def main():
    num_bins = 5
    dating = do_discretize(num_bins)
    for column in dating:
        if column not in non_binned_cols:
            count = dating[column].value_counts(sort=False)
            print (column, ": ", count.tolist())

if __name__ == '__main__':
    main()