"""
-----------------------------------
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@date: 17.7.2020
-----------------------------------
"""
import numpy as np

from abc import ABC, abstractmethod
from keras.models import Sequential


class BaseModel(ABC):
    def __init__(self,dataset):
        
        # Training and testing dataset
        self._dataset = dataset

        # Neural network
        self._model = Sequential()

		# Training time.
        self._train_time = 0

    @abstractmethod    
    def compile_model(self):
        """
		Configures the NeuralNetwork model.
		:param none
		:return none
		"""

    @abstractmethod
    def fit_model(self):
        """
        Trains the NeuralNetwork model.
        :param none
        :return none
        """

    @abstractmethod
    def evaluate_model(self):
        """
        Evaluates the NeuralNetwork model.
        :param none
        :return none
        """

    def save_model(self, model_path):
        """
        Saves the NeuralNetwork model to disk in h5 format.
        :param none
        :return none
        """

        if( self._model is None ):
        	raise Exception("NeuralNetwork model not configured and trained !")
		
        self._model.save(model_path)
        print("NeuralNetwork model saved at path: ", model_path, "\n")

        return
    
    def load_model(self, load_model):
        """
        Loads the saved model from the disk.
        :param none
        :return none
        :raises NotImplementedError: Implement this method.
        """

        if( self._model is None ):
        	raise Exception("NeuralNetwork model not configured and trained !")
		
        self._model.load_weights( load_model )
        print("NeuralNetwork model loaded from the path: ", load_model, "\n")

        return


    

