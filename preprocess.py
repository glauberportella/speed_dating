import pandas as pd


global_encoder_by_field = {}
count_quotes = 0
count_lowercase = 0


def remove_quotes(column):
    global count_quotes
    count = column.str.count("\'.*\'").sum()
#     print (count)
    if count_quotes != count:
        count_quotes += count
    return column.str.strip('\'')

def convert_lowercase(column):
    global count_lowercase
    count_lowercase = len(column)- column.str.islower().sum()
#     print (count_lowercase)
    return column.str.lower()

def get_encoding(column):
    column = column.astype('category')
    encoding = {}
    for i, category in enumerate(column.cat.categories):
        encoding[category] = i
    global_encoder_by_field[column.name] = encoding
    return column.cat.codes

def main():
    dating = pd.read_csv('dating-full.csv')
    dating = dating.head(6500)
    
    dating[['race','race_o','field']] = dating[['race','race_o','field']].apply(remove_quotes)
    dating[['field']] = dating[['field']].apply(convert_lowercase)

    print ('Quotes removed from', count_quotes, 'cells')
    print('Standardized', count_lowercase , 'cells to lower case.')

    dating[['race','race_o','gender','field']] = dating[['race','race_o','gender','field']].apply(get_encoding)

    print ('Value assigned for male in column gender:', global_encoder_by_field['gender']['male'])
    print ('Value assigned for European/Caucasian-American in column race:', global_encoder_by_field['race']['European/Caucasian-American'])
    print ('Value assigned for Latino/Hispanic American in column race o:', global_encoder_by_field['race_o']['Latino/Hispanic American'])
    print ('Value assigned for law in column field:', global_encoder_by_field['field']['law'])

    partner_cols = ['pref_o_attractive','pref_o_sincere','pref_o_intelligence','pref_o_funny','pref_o_ambitious','pref_o_shared_interests']
    participant_cols = ['attractive_important', 'sincere_important', 'intelligence_important', 'funny_important', 'ambition_important', 'shared_interests_important']  

    total_partner = 0
    total_participant = 0 

    for i in range (0,6):
        total_partner += dating[partner_cols[i]]
        total_participant += dating[participant_cols[i]] 

    for i in range(0,6):
        dating[partner_cols[i]]/=total_partner
        dating[participant_cols[i]]/=total_participant

    for i in range(0,6):
        participant_mean = dating[participant_cols[i]].sum()/len(dating[participant_cols[i]])
        print ('Mean of ', participant_cols[i], ':', round(participant_mean, 2))
    for i in range(0,6): 
        partner_mean = dating[partner_cols[i]].sum()/len(dating[partner_cols[i]])
        print ('Mean of ', partner_cols[i], ':', round(partner_mean, 2))

    dating.to_csv('dating.csv', index = False)



if __name__ == '__main__':
    main()