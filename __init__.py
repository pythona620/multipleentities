from mycroft import MycroftSkill, intent_file_handler

class TomatoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_intent_file('where.are.intent', self.handle_where_are) #register the intentes
        self.register_intent_file('i.am.intent', self.handle_i_am) #register the intentes

    def handle_what_is(self, message): #get the intent
        self.speak('your friend is going') 

    def handle_do_you_like(self, message):
        going_from = message.data.get('type1')  #get the specific keword into type
        going = message.data.get('type2') 
        if tomato_type is not None:
            self.speak("Well, your specific keyword is " + "going_from" + "going" + " in your word.") #print specific keword
        else:
            self.speak('you are not given any specific word!') #print if specific keword is not given


    def stop(self):
        pass

def create_skill():
    return TomatoSkill()
