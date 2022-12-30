class CreatedInstancesCounter(object):
    c = 0
    def __init__(self):
        self.__class__.c += 1

    @classmethod
    def get_created_instances_count(cls):
        return cls.c