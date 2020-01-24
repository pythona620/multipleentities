from mycroft import MycroftSkill, intent_file_handler

class TomatoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_intent_file('what.is.intent', self.handle_what_is) #register the intentes
        self.register_intent_file('your.friend.intent', self.handle_do_you_like) #register the intentes

    def handle_what_is(self, message): #get the intent
        self.speak('A tomato is a big red thing') #

    def handle_do_you_like(self, message):
        tomato_type = message.data.get('condition')  #get the specific keword into type
        tomato = message.data.get('temp')
        if tomato_type is not None:
            self.speak("your friend is going " + tomato_type +  tomato ) #print specific keword
        else:
            self.speak('you are not given any specific word!') #print if specific keword is not given


    def stop(self):
        pass

def create_skill():
    return TomatoSkill()
