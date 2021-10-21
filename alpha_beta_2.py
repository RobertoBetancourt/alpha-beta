from pprint import pprint
import numpy as np 
from random import randrange

def alpha_beta(node, alpha, beta):
  if(node['terminal']):
    return node['h(j)']
  
  children_ids = node['children']
  if(node['depth'] % 2 == 0):
    for child_id in children_ids:
      alpha = max(alpha, alpha_beta(graph[child_id], alpha, beta))
      if alpha >= beta:
        return beta
    return alpha
  
  else:
    for child_id in children_ids:
      beta = min(beta, alpha_beta(graph[child_id], alpha, beta))
      if alpha >= beta:
        return alpha
    return beta

def make_user_move(board, x, y):
  board[y-1][x-1] = 2

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

def check_rows(board, rival_number):
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


def get_possibilities_to_win(board, number_to_check):
  return 1

def get_function_result(board, terminal):
  if terminal:
    # Obtener las posibilidades que tengo de ganar como computadora y las que tiene el usuario
    h = get_possibilities_to_win(board, 1) - get_possibilities_to_win(board, 2)
    return h
  else:
    return None
    

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

def create_graph_of_boards(board):
  alpha = -99999999999
  beta = 99999999999

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
  children = generate_children(root, 2, False)
  for child in children:
    child_id = get_board_id(child['board'])
    root['children'].append(child_id)
    graph[child_id] = child    

    # Se generan los hijos de los hijos (llamados 'subhijos') y se agregan al grafo
    subchildren = generate_children(child, 1, True)
    for subchild in subchildren:
      subchild_id = get_board_id(subchild['board'])
      child['children'].append(subchild_id)
      graph[subchild_id] = subchild
  
  pprint(graph, compact=True)


def execute_game(board, user_starts):
  if user_starts:
    x = int(input())
    y = int(input())
    make_user_move(board, x, y)
    print(board)
  else:
    create_graph_of_boards(board)

def main():
  global graph
  graph = {}

  user_starts = randrange(2)

  # 0 empty space, 1 CPU, 2 user
  initial_board = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ])

  execute_game(initial_board, user_starts)

main()