
class Planet:
    " En klasse for å beskrive en planet"
    def __init__(self,navn:str,solavstand:float,radius:float,antallRinger=0) -> None:

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius
        self.antallRinger=antallRinger

jorden = Planet( "Jorden", 152, 6371)

def visInfo(self):
    print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")

jorden.visInfo()
print(jorden.navn)
print(jorden.antallRinger)
# Oppgave 1: 
# Lag et objekt for Mars, Jupiter og Jorda, der du lagrer informasjon om navn, solavstand og radius. Lagre disse objektene i egne variabler

# Hva skjer om du skriver print(Jorda)?
# Hva skjer om du skriver print(Jorda.navn)?
# Prøv å skriv ut de andre attributtene til klassen


# OBS: pass på rekkefølgen i argumentene til konstruktøren.



