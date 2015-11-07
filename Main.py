__author__ = 'nnico'
from Data import DataHandler


########################################################################################################################
# Interface for the data.
########################################################################################################################
MyDataHandler = DataHandler()



if __name__ == "__main__":

    print "hello world"

    train_data = MyDataHandler.get_train()
    test_data = MyDataHandler.get_test()

    print test_data.hist()

    print "Im done!"