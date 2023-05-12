from random import randint


class Repo:
    def __init__(self,file_name):
        self._file_name=file_name
        self._sentence=""
        self._used=[]
        self._read()



    def _read(self):

        with open(self._file_name, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                self._used.append(lines[i].strip("\n"))
            a = randint(0, len(lines)-1)
            self.sentence = lines[a]
            self.sentence = self.sentence.strip("\n")
        f.close()

    def _add(self, sentence):
        with open(self._file_name, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                self._used.append(lines[i].strip("\n"))
        with open(self._file_name, 'a') as f:
            if sentence!="":
                f.write('\n'+sentence)
            self._used.append(sentence)


    @property
    def used(self):
        return self._used

    @property
    def sentence(self):
        return self._sentence
    @sentence.setter
    def sentence(self,n_sentence):
        self._sentence=n_sentence

