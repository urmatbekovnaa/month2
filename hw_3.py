class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__cpu

    @memory.setter
    def memory(self, value):
        pass

    def  make_computations(self):
        print(f'')
