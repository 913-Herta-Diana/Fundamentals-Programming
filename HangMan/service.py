

class Player:
    def __init__(self, repository):
        self._repository=repository
        self._loser=""
        self._winner=''

    @property
    def winner (self):
        return  self._winner
    @property
    def loser(self):
        return self._loser

    def sentence_validity(self,sentence):
        words=sentence.split(" ")
        if len(words)<1:
            raise Exception("Can't play with an empty sentence!")
        for word in words:
            if len(word)<3:
                raise Exception("Words need at least 3 letters!")
        already_used=self._repository.used
        if sentence in already_used:
             raise Exception("Choose a new sentence!")



    def _add_sentence(self,sentence):
        self.sentence_validity(sentence)
        self._repository._add(sentence)

    def _format_hangman(self):

        sentence=self._repository.sentence
        self._loser=''
        self._winner=''
        words=sentence.split(' ')
        visible=[]
        visible.append(words[0])

        for word in words:
            if word[0] not in visible or word[-1] not in visible:
                visible.append(word[0])
                visible.append(word[-1])
        new_string=""
        for word in words:
            for i in range(len(word)):
                if word[i] in visible:
                    new_string+=word[i]
                else:
                    new_string+='_'
            new_string+=" "
        new_string.strip()
        self._winner=new_string
        return self._winner

    def _user_plays(self,ch):
        format=self._winner.split(" ")
        sentence=self._repository.sentence.split(" ")
        new_string=""
        visible=[]

        ok=False
        index=0
        for word in format:
            for i in range(len(word)):
                if word[i]!="_":
                    visible.append(word[i])

        for word in sentence:
            if ch in word and ch not in visible:
                ok=True
        if ok==True:
            for i in range(len(format)):
                for j in range(len(format[i])):
                    if sentence[i][j]==ch:
                        new_string+=ch
                    else:
                        new_string+=format[i][j]
                new_string+=" "
            self._winner=new_string
        else:
            self._loser=self.complete_hangman(self._loser)

        message=self.check_winner(self._winner,self._loser)

        if message=="Winner!" or message=="Loser!":
            return f"{self._winner} -> {self._loser}\n {message}"
        else:
            return f"{self._winner} -> {self._loser}"

    def complete_hangman(self,string):

        if string=="":
            string+='h'
        elif string=='h':
            string+='a'
        elif string=='ha':
            string+='n'
        elif string=="han":
            string+='g'
        elif string=="hang":
            string+='m'
        elif string=="hangm":
            string+="a"
        elif string=="hangma":
            string+='n'
        return string

    def check_winner(self, win, loose):
        message=""
        sentence=self._repository.sentence
        if win==sentence:
            message="Winner!"
        elif loose=="hangman":
            message="Loser!"

        return message

    def _lost(self):

        message = "You lost ma' friend"
        return message

    def _won(self):
        message = "Good job! You won!"
        return message






