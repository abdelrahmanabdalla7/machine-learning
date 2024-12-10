class Library:
    def __init__(self, gameslist:list, lenders:dict, doners:dict ):
        self.gamelist = gameslist
        self.lender = lenders
        self.doners = doners

    def games(self):
        return self.gamelist
    def lend (self,name:str,gamename:str):
        if gamename in self.gamelist:
            self.gamelist.remove(gamename)
            self.lender.update({gamename:name})
            print(f"{gamename} has been lent to {name}")
        else:
            print("{gamename} is not available")

    def returnb (self, name:str, gamename:str):
        if name in self.lender.values() and gamename in self.lender.keys(): 
            self.lender.pop(gamename)
            self.gamelist.append(gamename)
            print(f"{gamename} has been returned by {name}")
        else:
            print("Please check the entry")
    
    def donate(self, doner, newgame):
        self.gamelist.append(newgame)
        self.doners.update({doner:newgame})
        print(f"{newgame} has been donated by {doner} to the liberary")
