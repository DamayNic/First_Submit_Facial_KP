__author__ = 'nnico'
from sklearn.linear_model import LogisticRegression

class ModeleHandler(object):
    """
    Class used to reduce the dimension of a data set.
    """

    def __init__(self, model='LogisticRegression', *args, **kwargs):
        """
        Reduce the dimension of the input data.

        :param model: Name of the model
        :return: void
        """
        if model == "LogisticRegression":
            self._model = LogisticRegression(*args, **kwargs)
        else:
            raise Exception("The model {}, is not handled".format(model))

    def fit(self, data, target, *args, **kwargs):
        """
        Fit the model to the data.

        :param data: Data set
        :paramm target: Target
        :param args: Additional parameters
        :param kwargs: Additional parameters
        :return: void
        """
        return self._model.fit(data, data, target, *args, **kwargs)

    def score(self, data, target, *args, **kwargs):
        """
        Transform a data set using the model

        :param data: Data set
        :param target: Target
        :param args: Additional parameters
        :param kwargs: Additional parameters
        :return: Void
        """
        return self._model.score(data, target, *args, **kwargs)
