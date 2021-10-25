from alpha_beta import check_free_rows_to_win, check_free_columns_to_win, check_free_diagonals_to_win, alpha_beta, check_if_winning_column, check_if_winning_row, check_if_winning_diagonal, check_if_game_is_over, get_board_id, node_is_terminal
import numpy as np 

def test_check_rows():
  original_board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  rival_number = 1
  my_moves_from_fn = check_free_rows_to_win(board=original_board, rival_number=rival_number)
  expected_my_moves = 4

  assert(my_moves_from_fn == expected_my_moves)


def test_check_columns():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  rival_number = 1
  my_moves_from_fn = check_free_columns_to_win(board=original_board, rival_number=rival_number)
  expected_my_moves = 4

  assert(my_moves_from_fn == expected_my_moves)


def test_check_diagonals():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  rival_number = 1
  my_moves_from_fn = check_free_diagonals_to_win(board=original_board, rival_number=rival_number)
  expected_my_moves = 1

  assert(my_moves_from_fn == expected_my_moves)


def test_check_diagonals_complex():
  original_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  rival_number = 1
  my_moves_from_fn = check_free_diagonals_to_win(board=original_board, rival_number=rival_number)
  expected_my_moves = 2

  assert(my_moves_from_fn == expected_my_moves)

def test_alpha_beta():
  graph = {}

  root = {
    'depth': 0,
    'children': [],
    'h(j)': None,
    'terminal': False,
    'board': np.array([
        [2, 2, 2, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [2, 1, 2, 1, 2],
        [2, 2, 0, 0, 0]      
      ])
  }
  alpha = -999999999
  beta = 999999999

  root_id = get_board_id(root['board'])
  graph[root_id] = root

  result = alpha_beta(root, alpha, beta, graph)

  found = False
  current_node = None
  i = 0

  while not found and i < len(root['children']):
    current_node = graph[root['children'][i]]
    if root['h(j)'] == current_node['h(j)']:
      found = True
    
    i += 1

  assert(0 == result['h(j)'])


def test_check_if_winning_column():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_column(board=original_board, number_to_check=number_to_check)
  expected_result = True

  assert(result_from_fn == expected_result)

def test_check_if_not_winning_column():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_column(board=original_board, number_to_check=number_to_check)
  expected_result = False

  assert(result_from_fn == expected_result)

def test_check_if_winning_row():
  original_board = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_row(board=original_board, number_to_check=number_to_check)
  expected_result = True

  assert(result_from_fn == expected_result)

def test_check_if_not_winning_row():
  original_board = [
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_row(board=original_board, number_to_check=number_to_check)
  expected_result = False

  assert(result_from_fn == expected_result)


def test_check_if_winning_diagonal():
  original_board = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_diagonal(board=original_board, number_to_check=number_to_check)
  expected_result = True

  assert(result_from_fn == expected_result)

def test_check_if_winning_inverse_diagonal():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_diagonal(board=original_board, number_to_check=number_to_check)
  expected_result = True

  assert(result_from_fn == expected_result)

def test_check_if_not_winning_diagonal():
  original_board = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_diagonal(board=original_board, number_to_check=number_to_check)
  expected_result = False

  assert(result_from_fn == expected_result)

def test_check_if_not_winning_inverse_diagonal():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
  ]

  number_to_check = 1
  result_from_fn = check_if_winning_diagonal(board=original_board, number_to_check=number_to_check)
  expected_result = False

  assert(result_from_fn == expected_result)

def test_check_if_game_is_over():
  original_board = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
  ]

  result_from_fn = check_if_game_is_over(board=original_board)
  expected_result = True

  assert(result_from_fn == expected_result)

def test_check_if_game_is_not_over():
  original_board = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
  ]

  result_from_fn = check_if_game_is_over(board=original_board)
  expected_result = False

  assert(result_from_fn == expected_result)

def test_check_if_node_is_terminal():
  node = {
    'depth': 1,
    'board': [
      [0, 0, 1, 0, 0],
      [0, 2, 1, 0, 2],
      [2, 0, 1, 0, 0],
      [0, 0, 1, 2, 0],
      [0, 0, 1, 0, 0]
    ],
    'h(j)': None
  }

  result = node_is_terminal(node)

  assert(node['h(j)'] == 999999999)
  assert(result == True)

def test_check_if_node_is_not_terminal():
  node = {
    'depth': 1,
    'board': [
      [0, 0, 1, 0, 0],
      [0, 2, 1, 0, 2],
      [2, 0, 0, 0, 0],
      [0, 0, 1, 2, 0],
      [0, 0, 1, 0, 0]
    ],
    'h(j)': None
  }

  result = node_is_terminal(node)
  assert(result == False)