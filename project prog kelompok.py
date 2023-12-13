# Import modul yang dibutuhkan
import random
import time

# Definisikan konstanta
BOARD_SIZE = 100
START_POSITION = 0
WINNING_POSITION = 99

# Definisikan fungsi untuk mengacak gerakan
def roll_dice():
  """
  Mengacak gerakan dadu

  Mengembalikan:
    Gerakan dadu (1-6)
  """

  return random.randint(1, 6)

# Definisikan fungsi untuk mengecek apakah pemain menang
def is_winner(position):
  """
  Memeriksa apakah pemain menang

  Argumen:
    position: Posisi pemain

  Mengembalikan:
    True jika pemain menang, False jika tidak
  """

  return position == WINNING_POSITION

# Definisikan fungsi untuk mengecek apakah pemain jatuh ke ular atau tangga
def check_ladder_snake(position):
  """
  Memeriksa apakah pemain jatuh ke ular atau tangga

  Argumen:
    position: Posisi pemain

  Mengembalikan:
    Posisi baru pemain jika jatuh ke ular atau tangga, posisi pemain semula jika tidak
  """

  ladder_positions = [13, 24, 39, 54, 72]
  snake_positions = [11, 22, 43, 68]

  # Cek apakah pemain jatuh ke ular

  for snake_position in snake_positions:
    if position == snake_position:
      return position - snake_position

  # Cek apakah pemain jatuh ke tangga

  for ladder_position in ladder_positions:
    if position == ladder_position:
      return position + ladder_position

  return position

# Definisikan fungsi untuk memainkan satu putaran game
def play_round(player_position):
  """
  Memainkan satu putaran game

  Argumen:
    player_position: Posisi pemain

  Mengembalikan:
    Posisi baru pemain
  """

  # Mengacak gerakan dadu

  movement = roll_dice()

  # Menghitung posisi baru pemain

  new_position = player_position + movement

  # Memeriksa apakah pemain jatuh ke ular atau tangga

  new_position = check_ladder_snake(new_position)

  # Mengembalikan posisi baru pemain

  return new_position

# Definisikan fungsi untuk memainkan game
def play_game():
  """
  Memainkan game ular tangga

  Mengembalikan:
    Pemain yang menang
  """

  # Inisialisasi pemain

  player_1 = 1
  player_2 = 2

  # Mulai game

  while True:
    # Mengacak gerakan dadu untuk pemain 1

    movement = roll_dice()

    # Menghitung posisi baru pemain 1

    new_position = player_1 + movement

    # Memeriksa apakah pemain 1 menang

    if is_winner(new_position):
      return player_1

    # Mengacak gerakan dadu untuk pemain 2

    movement = roll_dice()

    # Menghitung posisi baru pemain 2

    new_position = player_2 + movement

    # Memeriksa apakah pemain 2 menang

    if is_winner(new_position):
      return player_2

    # Update posisi pemain

    player_1 = new_position
    player_2 = new_position

    # Tampilkan status game

    print("Pemain 1:", player_1)
    print("Pemain 2:", player_2)

# Mainkan game
winner = play_game()

# Tampilkan pemenang game
print("Pemenang game adalah pemain", winner)