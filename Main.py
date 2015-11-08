__author__ = 'nnico'
from DataHandler import DataHandler
from DImHandler import DimHandler
from ModeleHandler import ModeleHandler

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from patsy import dmatrices

from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

########################################################################################################################
# Interface for the data.
########################################################################################################################

def myprint(str):
    """
    Useless.

    Print a message with standart shape.
    """
    print "#######################################\n{}\n#######################################\n".format(str)

if __name__ == "__main__":


    myprint("Start computations")

    ####################################################################################################################
    # Get data
    ####################################################################################################################
    myprint("Load data")
    MyDataHandler = DataHandler()
    print "Loading train"
    train = MyDataHandler.get_train()

    #Pretty things up.
    column_names = {}
    for i in xrange(96*96):
        column_names[i] = 'pixel{}'.format(i)

    ####################################################################################################################
    # Split pixels:
    ####################################################################################################################
    myprint("Extract data")
    train_x = train.iloc[:800]['Image'].apply(lambda x: pd.Series([int(i) for i in x.split(' ')])).rename(columns=column_names)
    train_y = train.iloc[:800].ix[:, 0:30].fillna(0).astype(int)

    ####################################################################################################################
    # Reduce dimension
    ####################################################################################################################
    myprint("Reduce dimension")
    MyDimHandler = DimHandler(model='pca', **{'n_components': 0.80, 'whiten': True})

    train_x = MyDimHandler.fit_transform(train_x)
    ####################################################################################################################
    # Train models:
    ####################################################################################################################
    myprint("Train models")
    names = list(train.columns.values)
    models = []
    models_name = {}
    for index in xrange(30):
        model = ModeleHandler("LogisticRegression")
        models.append(model)
        models_name[names[i]] = model

    for index, model in enumerate(models):
        y = np.ravel(train_y.ix[:,index])
        model.fit(train_x, y)
        score = model.score(train_x, y)
        print "For the model {}, the score is: {}".format(names[i], score)

    ####################################################################################################################
    # Visualize some training images:
    ####################################################################################################################
    # print list(train.columns.values)
    # print list(test.columns.values)
    # MyDataHandler.visualize_train_image(index=6493, features=True)

    ####################################################################################################################
    #
    ####################################################################################################################
    myprint("Predict the score of the test data")

    print "Loading test"

    test = MyDataHandler.get_test()
    test_x = test.iloc[:800]['Image'].apply(lambda x: pd.Series([int(i) for i in x.split(' ')])).rename(columns=column_names)
    test_x = MyDimHandler.transform(test_x)

    myprint("Finished")