from pprint import pprint
import numpy as np 
from random import randrange

def make_user_move(board):
  valid_movement = False
  while not valid_movement:
    try:
      print('Introduce coordenada x')
      x = int(input())
      print('Introduce coordenada y')
      y = int(input())

      if board[y-1][x-1] == 0:
        board[y-1][x-1] = 2
        valid_movement = True
      else:
        print('Movimiento no valido, intenta de nuevo')

    except Exception:
      print('Movimiento no valido, intenta de nuevo')
    
def get_board_id(board):
  id = ''
  for i in range(5):
    for j in range(5):
      if i == 4 and j == 4:
        id += str(board[i][j])
      else:
        id += str(board[i][j]) + '-'
  return id

def print_formatted_board(board, formatted_board_symbols):
  for i in range(5):
    for j in range(5):
      print(' ',formatted_board_symbols[board[i][j]], end = '')
    print('\n')

# Funciones para validar victoria
def check_if_winning_row(board, number_to_check):  
  i = 0
  win = True
  while i < 5:
    j = 0
    while j < 5 and win:
      if board[i][j] != number_to_check:
        win = False
      j += 1
    
    if win:
      return True
    i += 1
    win = True

  return False

def check_if_winning_column(board, number_to_check):
  i = 0
  j = 0
  found_winning_movement = False
  valid_column = True
  
  while i < 5 and not found_winning_movement:
    while j < 5 and valid_column:
      if board[j][i] != number_to_check:
        valid_column = False
        continue

      if j == 4 and board[j][i] == number_to_check:
        found_winning_movement = True

      j +=1

    valid_column = True  
    i += 1
    j = 0 
  

  return found_winning_movement

def check_if_winning_diagonal(board, number_to_check):
  i = 0
  found_winning_movement = False
  valid_diagonal = True
  
  while i < 5 and not found_winning_movement and valid_diagonal:
    if board[i][i] != number_to_check:
      valid_diagonal = False
      continue

    if i == 4 and board[i][i] == number_to_check:
      found_winning_movement = True
    
    i += 1

  if found_winning_movement: 
    return found_winning_movement
  
  anti_i = 4
  i = 0
  found_winning_movement = False
  valid_diagonal = True

  while i < 5 and not found_winning_movement and valid_diagonal:
    if board[i][anti_i] != number_to_check:
      valid_diagonal= False
      continue

    if i == 4 and board[i][anti_i] == number_to_check:
      found_winning_movement = True

    i += 1
    anti_i -= 1

  
  return found_winning_movement

def validate_win(board, current_turn):
  return check_if_winning_row(board, current_turn) or check_if_winning_column(board, current_turn) or check_if_winning_diagonal(board, current_turn)

# Funciones para validar lugares disponibles para potencial victoria
def check_free_rows_to_win(board, rival_number):
  valid_movements = 0 
  currently_valid = True
  for i in range(5):
    for j in range(5):
      if board[i][j] == rival_number:
        currently_valid = False
        break

    if currently_valid:
      valid_movements += 1

    currently_valid = True  

  return valid_movements

def check_free_columns_to_win(board, rival_number):
  valid_movements = 0 
  currently_valid = True
  for i in range(5):
    for j in range(5):
      if board[j][i] == rival_number:
        currently_valid = False
        break

    if currently_valid:
      valid_movements += 1

    currently_valid = True   
  
  return valid_movements
  
def check_free_diagonals_to_win(board, rival_number):
  valid_movements = 0
  currently_valid = True
  for i in range(5):
    if board[i][i] == rival_number:
        currently_valid = False
        break

  if currently_valid:
    valid_movements += 1

  currently_valid = True
  anti_i = 4
  i = 0

  while currently_valid and i < 5:
    if board[i][anti_i] == rival_number:
      currently_valid = False
      continue

    i += 1
    anti_i -= 1

  if currently_valid:
    valid_movements += 1

  return valid_movements

def get_possibilities_to_win(board, number_to_check):
  rival_number = 2 if number_to_check == 1 else 1
  return check_free_rows_to_win(board=board, rival_number=rival_number) + check_free_columns_to_win(board=board, rival_number=rival_number) + check_free_diagonals_to_win(board=board, rival_number=rival_number)

def get_function_result(board):
  # Obtener las posibilidades que tengo de ganar como computadora y las que tiene el usuario
  cpu_possibilities = get_possibilities_to_win(board, 1)
  user_possibilites = get_possibilities_to_win(board, 2)
  return cpu_possibilities - user_possibilites

# Función que verifica si todos los espacios del tablero están llenos
def check_if_game_is_over(board):
  for row in board:
    if 0 in row:
      return False
  return True       

# Función que genera los hijos de un nodo
def generate_children(parent, current_turn, terminal):
  child_boards = []
  parent_id = get_board_id(parent['board'])

  # Variable de control para búsqueda tabú
  child_ids = []
  for i in range(5):
    for j in range(5):
      new_child = np.copy(parent['board'])
      if new_child[i][j] == 0:
        new_child[i][j] = current_turn
        current_id = get_board_id(new_child)

        # Búsqueda tabú: se busca si un nodo "hermano" tiene el mismo id
        # Si no es el caso, se proced a agregar el nodo actual a la lista de nodos hijos
        if not current_id in child_ids:
          child_ids.append(current_id)
          child_boards.append({
            'board': new_child,
            'depth': parent['depth'] + 1,
            'parent': parent_id,
            'children': [],
            'terminal': terminal,
            'h(j)': None
          })
  return child_boards

# Función que determina si un nodo es terminal, y si es el caso, le da un valor de h(j)
def node_is_terminal(node):
  # Se asigna el turno actual con base en la profundidad del nodo actual
  current_turn = 2 if node['depth'] % 2 == 0 else 1

  # Si el nodo actual ya representa una victoria, se asume que es terminal, sin importar su profundidad
  if validate_win(node['board'], current_turn):
    if current_turn == 2:
      node['h(j)'] = -999999999
    else:
      node['h(j)'] = 999999999
    return True

  # Si el nodo tiene la profundidad máxima, se obtienen las posibilidades de ganar
  if node['depth'] == 2:
    node['h(j)'] = get_function_result(node['board'])
    return True

  return False

# Función que obtiene si el siguiente turno es del usuario o de la CPU
def get_next_turn(node):
  next_turn = 1 if node['depth'] % 2 == 0 else 2
  return next_turn

# Función que asocia el nodo padre con sus hijos y añade los nodos hijos al grafo
def add_children_to_graph(parent, children, graph):
  for child in children:
    child_id = get_board_id(child['board'])
    parent['children'].append(child_id)
    graph[child_id] = child

# Función que se encarga de la lógica del algoritmo alpha-beta
def alpha_beta(node, alpha, beta, graph):
  # Si el nodo es terminal, regresa el nodo
  if(node_is_terminal(node)):
    return node
  
  # Si el nodo no es terminal, se generan sus hijos, se agregan al grafo y a su padre
  children = generate_children(node, get_next_turn(node), node['depth'] == 1)
  add_children_to_graph(node, children, graph)
  children_ids = node['children']

  # Caso MAX
  if(node['depth'] % 2 == 0):
    for child_id in children_ids:
      child_node = alpha_beta(graph[child_id], alpha, beta, graph)
      alpha = max(alpha, child_node['h(j)'])
      if alpha >= beta:
        node['h(j)'] = beta
        return node
    node['h(j)'] = alpha     
    return node 
  
  # Caso MIN
  else:
    for child_id in children_ids:
      child_node = alpha_beta(graph[child_id], alpha, beta, graph)
      beta = min(beta, child_node['h(j)'])
      if alpha >= beta:
        node['h(j)'] = alpha
        return node
    node['h(j)'] = beta    
    return node

def run_algorithm(board):
  # Se inicializa el grafo
  graph = {}

  # Se genera el nodo raíz
  root = {
    'board': board,
    'depth': 0,
    'parent': None,
    'children': [],
    'terminal': False,
    'h(j)': None
  }

  alpha = -999999999
  beta = 999999999
  root = alpha_beta(root, alpha, beta, graph)

  found = False
  current_node = None
  index = 0
  while not found and index < len(root['children']):
    current_id = root['children'][index]
    current_node = graph[current_id]
    if root['h(j)'] == current_node['h(j)']:
      found = True
    index += 1
    
  return current_node['board']

def execute_game(current_turn, formatted_board_symbols):
  # Inicio de tablero (vacío)
  board = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ])

  # Si alguien ganó o se acabó el juego, terminar ciclo
  victory = False
  game_over = False
  while not victory and not game_over:
    if current_turn == 2:
      print('\nTurno del usuario:')
      make_user_move(board)
      # Mandar a llamar a la función para validar victoria
      victory = validate_win(board, current_turn)
      if victory:
        print('Felicidades, el usuario gano')
      else:
        current_turn = 1
    else:
      print('\nTurno de la computadora:')
      board = run_algorithm(board)
      # Mandar a llamar a la función para validar victoria
      victory = validate_win(board, current_turn)
      if victory:
        print('Perdiste, victoria de la computadora')
      else:
        current_turn = 2
    
    print_formatted_board(board, formatted_board_symbols)
    game_over = check_if_game_is_over(board)
    if game_over:
      print('Fin del juego, empate')

def main():
  # 0 empty space, 1 CPU, 2 user
  first_turn = randrange(1, 3)

  if(first_turn == 1):
    formatted_board_symbols = { 0: '-', 1: 'X', 2: 'O' }
  else:
    formatted_board_symbols = { 0: '-', 1: 'O', 2: 'X' }

  print('Inicia el juego:')
  execute_game(first_turn, formatted_board_symbols)

# main()