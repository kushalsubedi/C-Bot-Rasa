from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData


import nltk
from nltk.classify import NaiveBayesClassifier
import os

import typing
from typing import Any, Optional, Text, Dict

FOOD_ITEM_NER_FILE_NAME = "fooditemNer.pkl"

class FoodItemNer(Components):
    provides = ["entities"]
    requires = ['token']
    default = {}
    language_list = ["en"]
    print("initialised the class")

    def __init__(self,component_config = None):
        super(FoodItemNer, self).__init__(component_config)

    def train(self, training_data, cfg,**kwargs):
        with open('fooddata.txt','r') as f:
            labels = f.read().splitlines()
            training_data = training_data.training_examples
            tokens = [list(map(lambda x: x.text, t.get('tokens'))) for t in training_data]
            processed_tokens = [self.preprocessing(t) for t in tokens]
            labeled_data = [(t, x) for t,x in zip(processed_tokens, labels)]
            self.clf = NaiveBayesClassifier.train(labeled_data)

    def conver_to_rasa(self,value,confidence):
        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "food_item",
                  "extractor": "food_item_extractor"}

        return entity
    
    def preprocessing(self, tokens):
        return ({word: True for word in tokens})
    

    def process(self,message,**kwargs):
        if not self.clf:
            # component is either not trained or didn't
            # receive enough training data
            entity = None
        else:
            tokens = [t.text for t in message.get("tokens")]
            tb = self.preprocessing(tokens)
            pred = self.clf.prob_classify(tb)

            food_item = pred.max()
            confidence = pred.prob(food_item)

            entity = self.convert_to_rasa(food_item, confidence)

            message.set("entities", [entity], add_to_output=True)


    def persist(self, file_name, model_dir):
        """Persist this model into the passed directory."""
        classifier_file = os.path.join(model_dir, FOOD_ITEM_NER_FILE_NAME)
        utils.json_pickle(classifier_file, self)
        return {"classifier_file": FOOD_ITEM_NER_FILE_NAME}

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir=None,
             model_metadata=None,
             cached_component=None,
             **kwargs):
        file_name = meta.get("classifier_file")
        classifier_file = os.path.join(model_dir, file_name)
        return utils.json_unpickle(classifier_file)
    
    