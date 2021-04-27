import abc


class AudioIOInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(
            cls,
            subclass
    ) -> bool:
        return hasattr(subclass, 'load_audio') \
               and callable(subclass.load_audio) \
               and hasattr(subclass, 'save_audio') \
               and callable(subclass.save_audio)
