from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from actions.utils.load_lookup import load_lookup_table
class AskPhoneAction (Action):
    def name (self)->Text:
        return "action_ask_phone"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone = tracker.get_slot("phone")
        print("phone:", phone)
        if phone is not None:
          
          dispatcher.utter_message(text=f"Your phone number is {phone}") 
          print ("HEllo!")
        else:
            dispatcher.utter_message(text="Please provide your phone number.")
        return []
    
class ActionGetItemPrice(Action):
    def name(self)-> Text:
        print ("Called")
        return "action_get_item_price"
    lookup_table = load_lookup_table("actions/Foods.csv")
    print (lookup_table)
    def run (self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any])->List[Dict[Text,Any]]:
        print ("Foods")
        item = tracker.get_slot("Food")
        item = item.lower().strip()
        print (item)

       
        if item is not None:
            if item in self.lookup_table:
                price = self.lookup_table[item]
                print (price)
                dispatcher.utter_message(text=f"The price of {item} is {price}")
            else:
                dispatcher.utter_message(text=f"Sorry, we do not have the price of {item}")
        else:
            dispatcher.utter_message(text="Please provide the item name.")
        return []


