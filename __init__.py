from mycroft.skills.core import FallbackSkill


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

    def shutdown(self):
        """
            Remove this skill from list of fallback skills.
        """
        self.remove_fallback(self.handle_fallback)
        super(MeaningFallback, self).shutdown()


def create_skill():
    return MeaningFallback()
