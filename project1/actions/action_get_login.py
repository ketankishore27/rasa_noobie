from typing import Any, Text, Dict, List
import getpass
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractLoginDetail(Action):

    def name(self) -> Text:
        return "action_get_login_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        login_name = getpass.getuser()
        dispatcher.utter_message(text=f"Hi {login_name}, How can i help you?")

        return []
