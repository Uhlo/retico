from flexx import flx
from retico_builder.modules.abstract import AbstractModule

try:
    from retico.modules.simulation import asr, dm, eot, nlg, nlu, tts

    class SimulatedASRModule(AbstractModule):

        MODULE = asr.SimulatedASRModule
        PARAMETERS = {}

        def set_content(self):
            self.gui.clear_content()
            self.gui.add_info("Simulated ASR Module")

        def update_running_info(self):
            latest_iu = self.retico_module.latest_iu()
            if latest_iu:
                self.gui.update_info("Recognized Speech:<br>%s (confidence: %.2f)" % (latest_iu.text, latest_iu.confidence))

    class SimulatedDialogueManagerModule(AbstractModule):

        MODULE = dm.SimulatedDialogueManagerModule
        PARAMETERS = {"agenda_file": "data/sct/callerfile.ini", "conv_folder": "data/sct11/audio", "agent_class": "caller", "first_utterance": False}

        def set_content(self):
            self.gui.clear_content()
            self.gui.add_info("Dialogue Manager:<br><b>%s</b>" % self.retico_module.agent_class)

        def update_running_info(self):
            latest_iu = self.retico_module.latest_iu()
            if latest_iu:
                self.gui.update_info("Intent: %s<br>Concept: %s" % (latest_iu.act, latest_iu.concepts))

    class SimulatedEoTModule(AbstractModule):

        MODULE = eot.SimulatedEoTModule
        PARAMETERS = {}

        def set_content(self):
            self.gui.clear_content()
            self.gui.add_info("Simulated EOT Module")

        def update_running_info(self):
            latest_iu = self.retico_module.latest_iu()
            if latest_iu:
                self.gui.update_info("Is Speaking: <b>%s</b><br> Probability: %.2f)" % (latest_iu.is_speaking, latest_iu.probability))

    class SimulatedNLGModule(AbstractModule):

        MODULE = nlg.SimulatedNLGModule
        PARAMETERS = {"data_directory": "data/sct11/audio", "agent_type":"caller"}

        def set_content(self):
            self.gui.clear_content()
            self.gui.add_info("Simulated NLG Module")
            self.gui.add_info("Data directory: %s" % self.retico_module.data_directory)

        def update_running_info(self):
            latest_iu = self.retico_module.latest_iu()
            if latest_iu:
                self.gui.update_info("Is Speaking: <b>%s</b><br>Text: %s)" % (latest_iu.dispatch, latest_iu.get_text()))

    class SimulatedNLUModule(AbstractModule):

        MODULE = nlu.SimulatedNLUModule
        PARAMETERS = {}

        def set_content(self):
            self.gui.clear_content()
            self.gui.add_info("Simulated NLU Module")

        def update_running_info(self):
            latest_iu = self.retico_module.latest_iu()
            if latest_iu:
                self.gui.update_info("Intent: %s<br>Concept: %s" % (latest_iu.act, latest_iu.concepts))

    class SimulatedTTSModule(AbstractModule):

        MODULE = tts.SimulatedTTSModule
        PARAMETERS = {}

        def set_content(self):
            self.gui.clear_content()
            self.gui.add_info("Simulated TTS Module")

        def update_running_info(self):
            latest_iu = self.retico_module.latest_iu()
            if latest_iu:
                self.gui.update_info("Disptaching: %s" % latest_iu.dispatch)



except ImportError:
    pass
