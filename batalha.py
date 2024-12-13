import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self, inimigo):
        inimigo.vida = inimigo.vida - 30
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa 30 de Dano!")

class Mago(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
    def especial(self):
        self.vida = self.vida + 25
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")

class Arqueiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
    
    def especial(self,inimigos):
        for ini in inimigos:
            if ini == self:
                pass
            else:
                ini.vida = ini.vida - 15
        print(f"Legolas usa Chuva de Flechas e Causa 15 de Dano a Todos os Inimigos!")

def importar_personagens(caminho):
    with open(caminho,'r') as ficheiro:
        stats = json.load(ficheiro)

    personagens = []

    for stat in stats:
        if stat["classe"] == "Guerreiro":
            personagens.append(Guerreiro(stat["nome"],stat["vida"],stat["ataque"]))
        elif stat["classe"] == "Mago":
            personagens.append(Mago(stat["nome"],stat["vida"],stat["ataque"]))
        elif stat["classe"] == "Arqueiro":
            personagens.append(Arqueiro(stat["nome"],stat["vida"],stat["ataque"]))

    num_personagens = len(personagens)
    return personagens, num_personagens
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    pass

def ordenar_personagens_por_vida(personagens):
    personagens = (sorted(personagens, key=lambda l: l.vida))
    return personagens
    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    pass

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])