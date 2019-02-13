import pandas as pd

def split_dataset(t_frac, random_state, filename):
    dating = pd.read_csv(filename)
    '''
    split dataset
    '''
    testset=dating.sample(frac=t_frac,random_state=random_state)
    trainset=dating.drop(testset.index)
    testset.to_csv("testSet.csv", index = False)
    trainset.to_csv("trainingSet.csv", index = False)


def main():
    filename = "dating-binned.csv"
    split_dataset(0.2, 47, filename)

if __name__ == '__main__':
    main()