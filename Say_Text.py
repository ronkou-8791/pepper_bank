import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)
        self.tts = ALProxy('ALTextToSpeech')
        self.ttsStop = ALProxy('ALTextToSpeech', True) #Create another proxy as wait is blocking if audioout is remote

    def onLoad(self):
        self.bIsRunning = False
        self.ids = []

    def onUnload(self):
        for id in self.ids:
            try:
                self.ttsStop.stop(id)
            except:
                pass
        while( self.bIsRunning ):
            time.sleep( 0.2 )

    def onInput_onStart(self, p):
        self.bIsRunning = True
        human = self.getParameter("text1").split(";")
        pepper= self.getParameter("text2").split(";")

        try:
            sentence = "\RSPD="+ str( self.getParameter("Speed (%)") ) + "\ "
            sentence += "\VCT="+ str( self.getParameter("Voice shaping (%)") ) + "\ "
            for i in range(len(human)):
                if p == human[i]:
                    sentence +=pepper[i]

            sentence +=  "\RST\ "
            id = self.tts.post.say(str(sentence))
            self.ids.append(id)
            self.tts.wait(id, 0)
        finally:
            try:
                self.ids.remove(id)
            except:
                pass
            if( self.ids == [] ):
                self.onStopped() # activate output of the box
                self.bIsRunning = False

    def onInput_onStop(self):
        self.onUnload()
