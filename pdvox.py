class Tracker:
    def __init__(self):
        self.__raw_instr = []
        self.__raw_pattern = []
    def add_instr(self, instr: str):
        self.__raw_instr.append(instr)
    def add_pattern(self, pattern: list)
        self.__raw_pattern.append(pattern)
    def __eval(self):
        for pattern in self.__raw_pattern:
            instr = 0
            freq = 1
            length = 1
            vel = 1
            for n, line in enumerate(pattern):
                if n == 0:
                    freq = line[0]
                    length = line[1]
                    vel = line[2]
                    continue
                freq *= line[1]
                length *= line[2]
                vel *= line[3]
                    

