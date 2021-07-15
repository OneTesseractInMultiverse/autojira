from abc import ABCMeta, abstractmethod


class AbstractTemplateProvider(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def load_template_as_dict(self) -> str:
        pass
