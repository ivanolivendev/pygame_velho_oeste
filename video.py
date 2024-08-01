import pygame
import random
import sys

# Configurações do jogo
LARGURA = 1280
ALTURA = 720
FPS = 60
TIMER_INICIAL = 600  # 600 frames = 10 segundos

# Caminhos dos arquivos
ARQUIVOS = {
    'bg': 'assets/imgs/bg.png',
    'fonte': 'assets/fonts/PixelGameFont.ttf',
    'alvo': 'assets/imgs/target.png',
    'mira': 'assets/imgs/mouse.png',
    'disparo': 'assets/audio/disparo.mp3'
}

# Variáveis do jogo
pontos = 0
recorde = 0
timer = TIMER_INICIAL
game_paused = True
finalizar = False
dificuldade = None  # Dificuldade padrão

class Alvo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(ARQUIVOS['alvo']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.ultimo_movimento = pygame.time.get_ticks()
        self.tempo_movimento = self.definir_tempo_movimento()
        self.direcao_x = 1  # Direção inicial em x
        self.direcao_y = 1  # Direção inicial em y

    def definir_tempo_movimento(self):
        if dificuldade == 'Médio':
            return 100  # 0.1 segundo em milissegundos
        elif dificuldade == 'Difícil':
            return 300  # 0.3 segundos em milissegundos
        else:
            return 0

    def update(self):
        if dificuldade in ['Médio', 'Difícil']:
            agora = pygame.time.get_ticks()
            if agora - self.ultimo_movimento > self.tempo_movimento:
                self.rect.x += self.direcao_x * 10  # Movimento em x
                self.rect.y += self.direcao_y * 10  # Movimento em y
                self.ultimo_movimento = agora

                # Verifica se o alvo atinge as bordas da tela e inverte a direção
                if self.rect.left <= 0 or self.rect.right >= LARGURA:
                    self.direcao_x *= -1
                if self.rect.top <= 0 or self.rect.bottom >= ALTURA:
                    self.direcao_y *= -1

class Mira(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ARQUIVOS['mira']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound(ARQUIVOS['disparo'])

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self, alvo):
        global pontos
        self.sound.play()

        if self.rect.colliderect(alvo.rect):
            pontos += 1
            alvo.rect.x = random.randrange(0, LARGURA - alvo.rect.width)
            alvo.rect.y = random.randrange(0, ALTURA - alvo.rect.height)

def inicializa_jogo():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Tiro ao Alvo')
    return screen

def carrega_fundo():
    bg = pygame.image.load(ARQUIVOS['bg']).convert()
    return pygame.transform.scale(bg, (LARGURA, ALTURA))

def exibe_pontuacao(screen, font):
    score_text = font.render(f' Pontos: {pontos} ', True, (0, 0, 0))
    screen.blit(score_text, (50, 50))

def exibe_tempo(screen, font):
    tempo_text = font.render(f'Tempo: {timer / 60:.1f} s', True, (0, 0, 0))
    screen.blit(tempo_text, (50, 100))

def exibe_tela_pausa(screen, font):
    pause_text = font.render("PRESSIONE ESC PARA PAUSAR", True, (255, 255, 255))
    recorde_text = font.render(f"RECORDE: {recorde} ", True, (255, 255, 255))

    pause_rect = pause_text.get_rect(center=(LARGURA / 2, ALTURA / 2))
    recorde_rect = recorde_text.get_rect(center=(LARGURA / 2, ALTURA / 2 - 50))

    screen.blit(pause_text, pause_rect)
    screen.blit(recorde_text, recorde_rect)

def desenha_menu(screen, font):
    pygame.draw.rect(screen, (150, 150, 150), (0, 0, LARGURA, 50))
    opcoes = ["Fácil", "Médio", "Difícil"]
    for i, opcao in enumerate(opcoes):
        text_surface = font.render(opcao, True, (255, 255, 255))
        screen.blit(text_surface, (50 + i * 200, 10))

def verifica_clique_botao(mouse_pos):
    global dificuldade, game_paused
    if 50 < mouse_pos[0] < 150 and 10 < mouse_pos[1] < 40:
        dificuldade = 'Fácil'
        game_paused = False
        return True
    elif 250 < mouse_pos[0] < 350 and 10 < mouse_pos[1] < 40:
        dificuldade = 'Médio'
        game_paused = False
        return True
    elif 450 < mouse_pos[0] < 550 and 10 < mouse_pos[1] < 40:
        dificuldade = 'Difícil'
        game_paused = False
        return True
    return False

def main():
    global timer, pontos, recorde, game_paused, finalizar, dificuldade

    screen = inicializa_jogo()
    bg = carrega_fundo()
    clock = pygame.time.Clock()
    font = pygame.font.Font(ARQUIVOS['fonte'], 30)

    alvo = Alvo(random.randrange(0, LARGURA), random.randrange(0, ALTURA))
    grupo_de_alvos = pygame.sprite.Group(alvo)

    mira = Mira()
    mira_group = pygame.sprite.Group(mira)

    while not finalizar:
        screen.blit(bg, (0, 0))
        desenha_menu(screen, font)

        if not game_paused:
            pygame.mouse.set_visible(False)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    finalizar = True
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    game_paused = not game_paused
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mira.shoot(alvo)

            grupo_de_alvos.update()
            grupo_de_alvos.draw(screen)
            mira_group.draw(screen)
            mira_group.update()

            exibe_pontuacao(screen, font)
            exibe_tempo(screen, font)

            timer -= 1
            if timer < 0:
                timer = TIMER_INICIAL
                if pontos > recorde:
                    recorde = pontos
                pontos = 0
                game_paused = True

        else:
            pygame.mouse.set_visible(True)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    finalizar = True
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    game_paused = not game_paused
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    verifica_clique_botao(pygame.mouse.get_pos())

            exibe_tela_pausa(screen, font)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
