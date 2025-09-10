from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class AskOrderDetail(Action):

    def name(self) -> Text:        
        return "action_ask_order_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"What would you like to order?")

        return []

class ExtractOrderDetail(Action):

    def name(self) -> Text:        
        return "action_extract_order_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values("food"), None)

        if food_entity:
            dispatcher.utter_message(text=f"You just selected {food_entity}, Do you Confirm?")

        return []
    

