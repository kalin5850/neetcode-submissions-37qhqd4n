class MinStack:

    def __init__(self):
        self.__stack: list[int] = []
        self.__min: list[int] = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if len(self.__min) == 0:
            self.__min.append(val)
        elif val <= self.__min[-1]:
            self.__min.append(val)

    def pop(self) -> None:
        num = self.__stack.pop()
        if num == self.__min[-1]:
            self.__min.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min[-1]
