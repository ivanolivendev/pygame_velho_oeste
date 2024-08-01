# Target Shooting

"Target Shooting" is a 2D game developed in Python using Pygame, where the objective is to hit moving targets to score points. Choose between three difficulty levels that affect the speed of the targets.

## Necessary Files

- **Background:** `assets/imgs/bg.png`
- **Font:** `assets/fonts/PixelGameFont.ttf`
- **Target:** `assets/imgs/target.png`
- **Crosshair:** `assets/imgs/mouse.png`
- **Shot Sound:** `assets/audio/disparo.mp3`

## How to Play

1. **Game Initialization**
   - Run the main script to start the game.
   - The main screen displays three difficulty options: Easy, Medium, and Hard.
   - Click on the desired difficulty to start the game.

2. **Gameplay**
   - Move the mouse to control the crosshair.
   - Click the left mouse button to shoot.
   - With each hit, a new target will appear at a random position.
   - The game ends when the time runs out.

3. **Scoring**
   - The score is displayed in the upper left corner of the screen.
   - The remaining time is shown just below the score.

4. **Pause**
   - Press the ESC key to pause the game.
   - The current high score will be displayed on the pause screen.
   - Press ESC again to resume the game.

## Controls

- **Mouse:**
  - Move the mouse: Controls the position of the crosshair.
  - Left mouse button: Shoots.

- **Keyboard:**
  - ESC key: Pauses or resumes the game.

## Difficulty Levels

- **Easy:** Static targets.
- **Medium:** Targets move every 0.1 seconds.
- **Hard:** Targets move every 0.3 seconds.

## Classes

### Target

- **`__init__`:** Initializes the `Target` class by loading the target image, setting its scale, and positioning it randomly on the screen.
- **`set_movement_time`:** Sets the time between target movements based on the chosen difficulty.
- **`update`:** Updates the target's position each frame, reversing its direction when it hits the screen edges.

### Crosshair

- **`__init__`:** Initializes the `Crosshair` class, loading the crosshair image and the shot sound.
- **`update`:** Updates the position of the crosshair to match the mouse cursor's position.
- **`shoot`:** Plays the shot sound and checks for collisions between the crosshair and the target, increasing the score and repositioning the target if hit.

## Code Structure

- **`initialize_game()`:** Sets up and starts the game window.
- **`load_background()`:** Loads the background image and adjusts it to fit the screen size.
- **`display_score()`:** Shows the current score on the screen.
- **`display_time()`:** Shows the remaining time on the screen.
- **`display_pause_screen()`:** Displays pause instructions and the high score.
- **`draw_menu()`:** Draws the difficulty selection menu.
- **`check_button_click()`:** Checks if the player clicked on a difficulty button.

## Requirements

- Python 3.x
- Pygame

## Installation and Execution

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ivanolivendev/pygame_velho_oeste.git

2. **Enter in directory:**
   cd pygame_velho_oeste

4. **Execute the file**
   python main.py

