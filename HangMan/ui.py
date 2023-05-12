
class UI:
    def __init__(self,repository,service):
        self._service=service
    @staticmethod
    def display_menu():
        display = "Loading Hangman...\n"
        display += "1. Add sentence\n"
        display += "2. Start game\n"
        display += "0. Exit game\n"
        print(display)


    def add_sentence(self):
        sentence=input("Insert a sentence: ")
        self._service._add_sentence(sentence)

    def play(self):
        while True:
            ch=input("Select a letter:")
            etalon=self._service._user_plays(ch)
            print(etalon)
            if etalon=="Loser!" or etalon=="Winner!":
                break






    def start(self):
        commands=['1','2','0']
        while True:
            try:
                self.display_menu()
                command=input("Choose your option: ")
                while command not in commands:
                    command=input("Not an option, try 1,2, or 0\n")
                if command=='0':
                    break
                elif command=='1':

                    self.add_sentence()
                    print("Sentence added successfully!")

                elif command=='2':

                    sent=self._service._format_hangman()
                    print(sent)
                    self.play()

            except Exception as e:
                print(e)
            except KeyError as e:
                print(e)









