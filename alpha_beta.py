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

def check_rows(board, rival_number):
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
  
def check_if_winning_row(board, number_to_check):  
  i = 0
  # j = 0
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

def check_columns(board, rival_number):
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


def check_if_winning_column(board, number_to_check: int) -> bool:
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
  


def check_diagonals(board, rival_number):
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

def check_if_winning_diagonal(board, number_to_check: int) -> bool:
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

def get_possibilities_to_win(board, number_to_check):
  rival_number = 2 if number_to_check == 1 else 1

  return check_rows(board=board, rival_number=rival_number) + check_columns(board=board, rival_number=rival_number) + check_diagonals(board=board, rival_number=rival_number)

def get_function_result(board, terminal):
  if terminal:
    # Obtener las posibilidades que tengo de ganar como computadora y las que tiene el usuario
    h = get_possibilities_to_win(board, 1) - get_possibilities_to_win(board, 2)
    return h
  else:
    return None

def check_if_game_is_over(board):
  for row in board:
    if 0 in row:
      return False

  return True       

def generate_children(parent, team, terminal):
  child_boards = []
  parent_id = get_board_id(parent['board'])

  for i in range(5):
    for j in range(5):
      new_child = np.copy(parent['board'])
      if new_child[i][j] == 0:
        new_child[i][j] = team
        child_boards.append({
          'board': new_child,
          'depth': parent['depth'] + 1,
          'parent': parent_id,
          'children': [],
          'terminal': terminal,
          'h(j)': get_function_result(new_child, terminal)
        }) 
  return child_boards

def alpha_beta(node, alpha, beta, graph):
  if(node['terminal']):
    # print('terminal', node)
    return node
  
  children_ids = node['children']
  if(node['depth'] % 2 == 0):
    for child_id in children_ids:
      child_node = alpha_beta(graph[child_id], alpha, beta, graph)
      # print(child_node)
      alpha = max(alpha, child_node['h(j)'])
      if alpha >= beta:
        node['h(j)'] = beta
        return node
    node['h(j)'] = alpha     
    return node 
  
  else:
    for child_id in children_ids:
      child_node = alpha_beta(graph[child_id], alpha, beta, graph)
      # print(child_node)
      beta = min(beta, child_node['h(j)'])
      if alpha >= beta:
        node['h(j)'] = alpha
        return node
    node['h(j)'] = beta    
    return node

def create_graph_of_boards(board):
  graph = {}

  # Se genera el id de la raíz y se forma el nodo
  root_id = get_board_id(board)
  root = {
    # 'id':  root_id,
    'board': board,
    'depth': 0,
    'parent': None,
    'children': [],
    'terminal': False,
    'h(j)': None
  }

  # El nodo se agrega al grafo
  graph[root_id] = root

  # Se generan los hijos de la raíz y se agregan al grafo
  children = generate_children(root, 1, False)
  for child in children:
    child_id = get_board_id(child['board'])
    root['children'].append(child_id)
    graph[child_id] = child    

    # Se generan los hijos de los hijos (llamados 'subhijos') y se agregan al grafo
    subchildren = generate_children(child, 2, True)
    for subchild in subchildren:
      subchild_id = get_board_id(subchild['board'])
      child['children'].append(subchild_id)
      graph[subchild_id] = subchild
  
  # pprint(graph, compact=True)

  return [root, graph]
  

def run_algorithm(board):
  [root, graph] = create_graph_of_boards(board)

  alpha = -99999999999
  beta = 99999999999
  # print(graph)
  # print('===============================================')
  # pprint(root)
  root = alpha_beta(root, alpha, beta, graph)

  found = False
  current_node = None
  i = 0

  while not found and i < len(root['children']):
    current_node = graph[root['children'][i]]
    if root['h(j)'] == current_node['h(j)']:
      found = True
    
    i += 1
    

  # print(current_node)
  return current_node['board']



def execute_game(current_turn):
  # if alguien gano o se acabo el juego, terminar ciclo
  board = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ])

  victory = False
  game_over = False
  while not victory and not game_over:
    if current_turn == 2:
      print('Turno del usuario')
      make_user_move(board)
      print(board)
      # Mandar a llamar a la función para validar victoria
      victory = validate_win(board, current_turn)
      if victory:
        print('Felicidades, el usuario gano')
      else:
        current_turn = 1
    else:
      print('Turno de la computadora')
      board = run_algorithm(board)
      print(board)
      # Mandar a llamar a la función para validar victoria
      victory = validate_win(board, current_turn)
      if victory:
        print('GG, perdiste')
      else:
        current_turn = 2
    
    game_over = check_if_game_is_over(board)
    if game_over:
      print('Fin del juego')

def main():
  # global graph
  # graph = {}

  user_starts = randrange(1, 3)

  # 0 empty space, 1 CPU, 2 user
  

  execute_game(user_starts)

main()