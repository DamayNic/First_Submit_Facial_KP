__author__ = 'nnico'
from Data import DataHandler
import pandas as pd
import matplotlib.pyplot as plt

########################################################################################################################
# Interface for the data.
########################################################################################################################
MyDataHandler = DataHandler()



if __name__ == "__main__":

    print "hello world"
    ####################################################################################################################
    # Get data
    ####################################################################################################################
    train = MyDataHandler.get_train()
    test = MyDataHandler.get_test()

    ####################################################################################################################
    # Visualize some training images:
    ####################################################################################################################
    print list(train.columns.values)
    print list(test.columns.values)

    MyDataHandler.visualize_train_image(index=0, features=True)
    MyDataHandler.visualize_train_image(index=1, features=True)
    MyDataHandler.visualize_train_image(index=2, features=True)
    # print "Analyse data type: {}\n".format(train.dtypes)
    # print "Analyse data info: {}".format(train.info())
    # print "Describe data: {}".format(train.describe())

    ####################################################################################################################
    # Visualize Train data:
    ####################################################################################################################
    # print test.values
    # imgplot = plt.imshow(test.values)
    # plt.show()

    print "Im done!"