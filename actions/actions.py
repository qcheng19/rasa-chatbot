import re
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa.shared.core.slots import Slot

import sqlite3
con = sqlite3.connect('rasa.db')

class UsernameVerification(Action):
    def name(self) -> Text:
        return "action_determine_new_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("username")
        print(name)
        if sql_fetch(con, name, 'user'):
            dispatcher.utter_message(text="You don't have to pay extra.")
        else:
            insert_name(con, name)
            dispatcher.utter_message(text=f"Will register you as a new user, please pay extra fee!")
        return []

class AskCarName(Action):
    def name(self) -> Text:
        return "action_ask_car_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=fetch_all_car(con) + "You can choose one of them")
        return []

class GetCarName(Action):
    def name(self) -> Text:
        return "get_car_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("md")
        name = tracker.get_slot("car_name")
        print(name)
        if rent_sql_fetch(con, name):
            sql_update(con, name, 'usage', 0)
            dispatcher.utter_message(text=f"You rented a car!")
        else:
            dispatcher.utter_message(text=f"The input is invalid")
        return []

class after_feedback_form(FormValidationAction):
    def name(self) -> Text:
        return "car_feedback_form"

    def run(self, slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker) -> List[Dict[Text, Any]]:
        if sql_fetch(con, slot_value.lower(), 'vehicle'):
            dispatcher.utter_message(text=f"The input is invalid")
            return {"car_name": None}
        else:
            sql_update(con, slot_value.lower(), "vehicleStatus", slot_value())
            dispatcher.utter_message(text=f"yi shou dao ni dui {slot_value.lower()} de fan kui")
        return []

class car_break_form(FormValidationAction):
    def name(self) -> Text:
        return "car_break_form"

    def run(self, slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker) -> List[Dict[Text, Any]]:
        if sql_fetch(con, slot_value.lower(), 'vehicle'):
            dispatcher.utter_message(text=f"The input is invalid")
            return {"car_name": None}
        else:
            sql_update(con, slot_value.lower(), "vehiclePosition", slot_value())
            dispatcher.utter_message(text=f"wo men hui jin kuai gan qu, qing nai xin deng dai!")
        return []

def sql_fetch(con, name, tablename):
    cursorObj = con.cursor()
    if tablename=='vehicle':
        cursorObj.execute('SELECT vehicleName FROM vehicle')
    else:
        cursorObj.execute('SELECT name FROM user')
    for back_name in cursorObj.fetchall():
        if back_name[0] == name:
            return True
    return False

def rent_sql_fetch(con, name):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT vehicleName FROM vehicle WHERE usage = 1')
    for back_name in cursorObj.fetchall():
        if back_name[0] == name:
            return True
    return False

def sql_update(con,car_name, line_name, value):
    cursorObj = con.cursor()
    if(line_name == 'vehicleStatus'):
        sql = "UPDATE vehicle SET vehicleStatus=? where vehicleName = ?"
    elif line_name == 'usage':
        sql = "UPDATE vehicle SET usage=? where vehicleName = ?"
    else:
        sql = "UPDATE vehicle SET vehiclePosition=? where vehicleName = ?"
    cursorObj.execute(sql,(value, car_name,))
    con.commit()

def insert_name(con,name):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO user(name) VALUES(?)', (name,))   
    con.commit()

def fetch_all_car(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT vehicleName FROM vehicle WHERE usage = 1")
    back_name = cursorObj.fetchall()
    s = ""
    for row in back_name:
        s = s + row[0] + "\n"
    return s
