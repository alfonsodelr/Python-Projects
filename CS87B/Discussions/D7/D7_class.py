class Player:

    def __init__(self, userName, gamerTag, playerID):
        self.userName = userName
        self.gamerTag = gamerTag
        self.playerID = playerID
    
    @property
    def allInfo(self):
        return 'User Name: {}\nGamer Tag: {}\n ID: {}'.format(self.userName, self.gamerTag, self.playerID)
