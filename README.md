# Tiro ao Alvo

"Tiro ao Alvo" é um jogo 2D desenvolvido em Python com Pygame, onde o objetivo é acertar alvos móveis para marcar pontos. Escolha entre três níveis de dificuldade que afetam a velocidade dos alvos.

## Arquivos Necessários

- **Plano de fundo:** `assets/imgs/bg.png`
- **Fonte:** `assets/fonts/PixelGameFont.ttf`
- **Alvo:** `assets/imgs/target.png`
- **Mira:** `assets/imgs/mouse.png`
- **Disparo:** `assets/audio/disparo.mp3`

## Como Jogar

1. **Inicialização do Jogo**
   - Execute o script principal para iniciar o jogo.
   - A tela principal exibe três opções de dificuldade: Fácil, Médio e Difícil.
   - Clique na dificuldade desejada para começar o jogo.

2. **Jogabilidade**
   - Mova o mouse para controlar a mira.
   - Clique com o botão esquerdo do mouse para disparar.
   - A cada acerto, um novo alvo aparecerá em uma posição aleatória.
   - O jogo termina quando o tempo se esgota.

3. **Pontuação**
   - A pontuação é exibida no canto superior esquerdo da tela.
   - O tempo restante é exibido logo abaixo da pontuação.

4. **Pausa**
   - Pressione a tecla ESC para pausar o jogo.
   - Na tela de pausa, o recorde atual será exibido.
   - Pressione ESC novamente para retomar o jogo.

## Controles

- **Mouse:**
  - Mover o mouse: Controla a posição da mira.
  - Botão esquerdo do mouse: Dispara.

- **Teclado:**
  - Tecla ESC: Pausa ou retoma o jogo.

## Dificuldades

- **Fácil:** Alvos estáticos.
- **Médio:** Alvos se movem a cada 0.1 segundo.
- **Difícil:** Alvos se movem a cada 0.3 segundo.

## Classes

### Alvo

- **`__init__`:** Inicializa a classe `Alvo` carregando a imagem do alvo, definindo sua escala e posição aleatória na tela.
- **`definir_tempo_movimento`:** Define o tempo entre movimentos dos alvos com base na dificuldade escolhida.
- **`update`:** Atualiza a posição do alvo a cada frame, invertendo sua direção ao atingir as bordas da tela.

### Mira

- **`__init__`:** Inicializa a classe `Mira`, carregando a imagem da mira e o som do disparo.
- **`update`:** Atualiza a posição da mira para coincidir com a posição do cursor do mouse.
- **`shoot`:** Executa o som do disparo e verifica colisões entre a mira e o alvo, incrementando a pontuação e reposicionando o alvo se atingido.

## Estrutura do Código

- **`inicializa_jogo()`:** Configura e inicia a janela do jogo.
- **`carrega_fundo()`:** Carrega a imagem de fundo e a ajusta ao tamanho da tela.
- **`exibe_pontuacao()`:** Mostra a pontuação atual na tela.
- **`exibe_tempo()`:** Mostra o tempo restante na tela.
- **`exibe_tela_pausa()`:** Exibe as instruções de pausa e o recorde.
- **`desenha_menu()`:** Desenha o menu de seleção de dificuldade.
- **`verifica_clique_botao()`:** Verifica se o jogador clicou em um botão de dificuldade.

## Requisitos

- Python 3.x
- Pygame

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/tiro-ao-alvo.git
