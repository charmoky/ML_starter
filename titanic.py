from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

train_filename = "train.csv"
test_filename = "test.csv"
gender_submission = "gender_submission.csv"

def load_data(filename):
    train = pd.read_csv(filename)
    return train

train = load_data(train_filename)
gender_submission = load_data(gender_submission)


train.head()
train.describe()

gender_submission.head()
gender_sumission.describe()




