import random

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tts = ALProxy('ALTextToSpeech')
        self.tts.setLanguage('Czech')
        try:
            self.speech = ALProxy("ALSpeechRecognition")
            self.speech.setLanguage('Czech')
        except:
            self.logger.info('Running on virtual robot')
            self.speech = None
        
    def get_answer(self, reactions):
        if self.speech is None:
            return (random.choice(reactions.keys()))
        else:
            self.speech.setVocabulary(reactions.keys(), False)
            self.speech.subscribe("Test_ASR")
            self.logger.info('Speech recognition engine started')
            time.sleep(20)
            self.speech.unsubscribe("Test_ASR")

    def onInput_onStart(self):
        self.tts.say("Ahoj, jak se máš?")
        reactions = {
            'dobře':  'to je super!',
            'špatně': 'doufám, že to brzo bude lepší',
            'nevím': 'tak to určitě nebude tak zlé',
        }
        answer = self.get_answer(reactions)
        react = reactions.get(answer)
        self.logger.info('answer={}, react={}'.format(answer, react))
        self.tts.say(react)
        self.onStopped()

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
