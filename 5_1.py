import pandas as pd

training_file = "trainingSet.csv"
test_file = "testSet.csv"

count_dict_yes = {}
count_dict_no = {}
prior_probability_dict = {}

def inference_row(row):
    correct = 0
    prob_dec_1 = 1
    prob_dec_0 = 1
    for column in count_dict_yes:
        if column != 'decision':
#                 prob_dec_1 += np.log(get_probability(column, row[column], 1))
#                 prob_dec_0 += np.log(get_probability(column, row[column], 0))
                '''
                dont take logs
                '''
                prob_dec_1 *= get_probability(column, row[column], 1)
                prob_dec_0 *= get_probability(column, row[column], 0)
    '''
    multiply by prior probabilities
    '''
#     prob_dec_1 += np.log(prior_probability_dict[1])
#     prob_dec_0 += np.log(prior_probability_dict[0])
    # dont take logs
    prob_dec_1 *= prior_probability_dict[1]
    prob_dec_0 *= prior_probability_dict[0]
    
    predicted_value = 0
    true_value = row['decision']
    if prob_dec_1 > prob_dec_0:
        predicted_value = 1
    if predicted_value == true_value:
        correct = 1
    return correct

def inference(dataset):  
    dataset['correct_prediction'] = dataset.apply(inference_row, axis=1)
    correct_prediction_dict = dataset['correct_prediction'].value_counts().to_dict()
    return correct_prediction_dict

def get_probability(attribute, value, decision):
    if decision == 1:
        value_count = 0
        if value in count_dict_yes[attribute]:
            value_count = count_dict_yes[attribute][value]
        return (value_count+1.0)/(count_dict_yes['decision'][1]+len(count_dict_yes[attribute]))
    elif decision == 0:
        value_count = 0
        if value in count_dict_no[attribute]:
            value_count = count_dict_no[attribute][value]
        return (value_count+1.0)/(count_dict_no['decision'][0]+len(count_dict_no[attribute]))

def nbc(t_frac):
    trainset = pd.read_csv(training_file)
    trainset=trainset.sample(frac=t_frac,random_state=47)
    testset = pd.read_csv(test_file)
    
    for column in trainset:
        count_dict_yes[column] = trainset[trainset['decision'] == 1][column].value_counts(sort=False).to_dict()
        count_dict_no[column] = trainset[trainset['decision'] == 0][column].value_counts(sort=False).to_dict()
        # print ('for column', column, 'bin count for decision 1 are', 
        #        count_dict_yes[column])
        # print ('for column', column, 'bin count for decision 0 are',
        #        count_dict_no[column])


    prior_probability_dict[1]= count_dict_yes['decision'][1]/(count_dict_no['decision'][0]+count_dict_yes['decision'][1])
    prior_probability_dict[0] = count_dict_no['decision'][0]/(count_dict_no['decision'][0]+count_dict_yes['decision'][1])

    correct_predictions_train = inference(trainset)
    correct_predictions_test = inference(testset)
    accuracy_test = correct_predictions_test[1]/(correct_predictions_test[1] + correct_predictions_test[0])
    accuracy_train = correct_predictions_train[1]/(correct_predictions_train[1] + correct_predictions_train[0])
    print ("Training Accuracy:", round(accuracy_train,2))
    print ("Testing Accuracy:", round(accuracy_test,2))

    return accuracy_train, accuracy_test


def main():
    t_frac = 1
    accuracy_train, accuracy_test = nbc(t_frac)

if __name__ == '__main__':
    main()