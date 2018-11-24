from mycroft.skills.core import FallbackSkill
import requests
from pygame import mixer
import random
import time

class MeaningFallback(FallbackSkill):
    """
        A Fallback skill to answer the question about the
        meaning of life, the universe and everything.
    """
    def __init__(self):
        super(MeaningFallback, self).__init__(name='Meaning Fallback')

    def initialize(self):
        """
            Registers the fallback skill
        """
        self.register_fallback(self.handle_fallback, 1)
        # Any other initialize code goes here

    def handle_fallback(self, message):
        print("fart")
        #api_url = "http://furby-control.synyx.coffee:3872/cmd/action"
        #requests.post(api_url, data='{"params":{"input":7,"index":2,"subindex":0,"specific":0}}')
        time.sleep(1)
        fart = "./fart-0%d.mp3" % (random.randint(1, 8))
        mixer.init()
        mixer.music.load(fart)
        mixer.music.play()
        player = vlc.MediaPlayer(fart)
        player.play()

    def shutdown(self):
        """
            Remove this skill from list of fallback skills.
        """
        self.remove_fallback(self.handle_fallback)
        super(MeaningFallback, self).shutdown()


def create_skill():
    return MeaningFallback()
