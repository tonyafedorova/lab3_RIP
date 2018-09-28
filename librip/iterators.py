# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.lst = items
        self.index = 0
        self.pre = 0
        if kwargs.__len__() == 0:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs

    def __next__(self):
        if self.index == (len(self.lst)):
            raise StopIteration
        else:
            if self.index == 0:
                self.index = self.index + 1
                return self.lst[self.pre]
            else:
                if self.ignore_case is False:
                    if self.lst[self.pre] != self.lst[self.index]:
                        self.pre = self.index
                        self.index = self.index + 1
                        return self.lst[self.pre]
                    else:
                        self.pre = self.index
                        self.index = self.index + 1
                        return self.__next__()
                else:
                    if self.lst[self.pre].lower() != self.lst[self.index].lower():
                        self.pre = self.index
                        self.index = self.index + 1
                        return self.lst[self.pre]
                    else:
                        self.pre = self.index
                        self.index = self.index + 1
                        return self.__next__()

    def __iter__(self):
        return self
