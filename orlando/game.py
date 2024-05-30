import pygame as raceGame

imagemPrincipal = raceGame.image.load("./imagensOficiais/carroPrincipal.png")
imagemCarro1 = raceGame.image.load("./imagensOficiais/carroLaranja.png")
imagemCarro2 = raceGame.image.load("./imagensOficiais/carroCinza.png")
imagemFaixa = raceGame.image.load("./imagensOficiais/faixa.png")


raceGame.init()

tela = raceGame.display.set_mode((800,600), (0,0))

raceGame.display.set_caption("Jogo de Corrida da Keiske")

emExecusao = True
posicaoCarro = 0
def movimentarCarro(x:int, y:int):
    tela.blit(raceGame.transform.scale_by(imagemPrincipal,0.7), (x,y))

while emExecusao:
    for event in raceGame.event.get():
        if event.type == raceGame.QUIT:
            emExecusao = False
        if event.type == raceGame.KEYDOWN:
            if event.key == raceGame.K_LEFT:
                print("Esquerda")
                posicaoCarro = posicaoCarro - 30
            if event.key == raceGame.K_RIGHT:
                print("Direita")
                posicaoCarro = posicaoCarro + 30
                
    gerarFundoDaTela()
    movimentarCarro(posicaoCarro, 340)
    raceGame.display.update()