__author__ = 'nnico'
from Singleton import Singleton
import pandas as pd

########################################################################################################################
# Path to the folders:
########################################################################################################################
LOOK_UP_TABLE = "/home/nnico/PycharmProjects/First_Submit_Facial_KP/Data/IdLookupTable.csv"
SUBMISSION = "/home/nnico/PycharmProjects/First_Submit_Facial_KP/Data/SampleSubmission.csv"
TEST_DATA = "/home/nnico/PycharmProjects/First_Submit_Facial_KP/Data/test.csv"
TRAIN_DATA = "/home/nnico/PycharmProjects/First_Submit_Facial_KP/Data/training.csv"

########################################################################################################################
# Interface to load the data
########################################################################################################################
class DataHandler(object):

    __metaclass__ = Singleton

    def __init__(self, test=TEST_DATA, train=TRAIN_DATA, look_up=LOOK_UP_TABLE, sub=SUBMISSION):
        """
        This class is used to deal with the data.

        The parameters are used to define the input files.

        :param test: Location of the test data
        :param train: Location of the train data
        :param look_up: Look up table
        :param sub:  Submission sample.

        :type test: String
        :type train: String
        :type look_up: String
        :type sub: String

        :return: void.
        """
        self.test = test
        self.train = train
        self.lookup = look_up
        self.sub = sub
        self._train = None
        self._test = None

    def get_test(self):
        """
        Get the test data.

        If the test data have never been loaded, load them using the proper function.

        :return: Test data
        """
        if self._test is None:
            self.load_data(test=True, train=False)
        return self._test

    def get_train(self):
        """
        Get the train data.

        If the train data have never been loaded, load them using the proper function.

        :return: train data
        """
        if self._train is None:
            self.load_data(test=False, train=True)
        return self._train

    def load_data(self, test=True, train=True):
        """
        Load the data.

        :param test:  Whether or not to load the test data
        :rtype test: bool
        :param train: Whether or not to load the train data
        :rtype train: bool.
        :return: Void
        """
        if test:
            self._test  = pd.read_csv(self.test)
        if train:
            self._train = pd.read_csv(self.train)




