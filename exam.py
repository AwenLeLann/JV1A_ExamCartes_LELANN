class Carte:
    def __init__(self,mana, nom, description):
        self.__c_mana = mana
        self.__nom = nom
        self.__desc = description

    def getCout(self):
        return self.__c_mana

class Mage:
    def __init__(self, nom, pv, t_mana, actuel, main, defausse, zone):
        self.__nom = nom
        self.__pv = pv
        self.__total = t_mana
        self.__actuel = actuel
        self.__main = []
        self.__defausse = []
        self.__zone = []

    def getNom(self):
        return self.__nom

    def getPv(self):
        return self.__pv

    def getTmana(self):
        return self.__total

    def getMana(self):
        return self.__mana
   
    def defausser(self):
    
    def affichedefausse(self):

    def affichemain(self):

    def jouer(self, ):
        if(self.getMana > self.getMana):
            self.defausser
        else:
            print("mana insuffisant")    

    def recup_mana(self, a_mana):
        self.__a_mana += 1


    def attaque(self, creature, carte):


class Cristal(Carte):
    def __init__(self, mana, nom, description,valeur):
        super().__init__(mana, nom, description)
        self.__valeur = valeur

    def jeu(self, mana, t_mana):
        if self.getMana >= self.getCout :
            

class Creature(Carte):
    def __init__(self, nom, mana, description, pvs, scoreAtk):
        super().__init__(mana, nom, description)
        self.__pvs = pvs
        self.__atk = scoreAtk

    def getPvs(self):
        return self.__pvs
     

class Blast(Carte):
    def __innit__(self, mana, nom, description, valeur):
        super().__innit__(mana, nom, description)
        self.__init__valeur = valeur

joueur = Mage("joueur",10 , 10, 10)

creature = Creature("Chat",10,"un chat", 10, 10)
creature2 = Creature("Poule",10,"une poule", 10, 10)
creature3 = Creature("Chèvre",10,"une chèvre", 10, 10)

cristal = Cristal(5)
blast = Blast(6)