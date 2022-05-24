class Scoreboard:
    def __init__(self):
        self.__scoreboard={}
        self.FillTheScoreboard()
    def FillTheScoreboard(self):
        file = open("scores.txt","r")
        content=file.read()
        file.close()
        list_content=content.split(" ")
        i=0
        while i <len(list_content):
            self.__scoreboard[list_content[i]]=list_content[i+1]
            i+=2
    def Display(self):
        for key in self.__scoreboard:
            print(key+" : "+self.__scoreboard[key])
    def Save(self):
        pass