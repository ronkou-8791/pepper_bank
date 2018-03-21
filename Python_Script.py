class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box

        x = 10
        y = 0

        #y = 2
        try:
            self.logger.info(x/y)
        except:
            self.logger.info("Error!")
        else:
            self.logger.info("Success!")
        finally:
            self.logger.info("Completed!")




    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
