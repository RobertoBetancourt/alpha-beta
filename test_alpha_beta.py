from alpha_beta import check_rows, check_columns, check_diagonals, alpha_beta, check_if_winning_column, check_if_winning_row, check_if_winning_diagonal, check_if_game_is_over

def test_check_rows():
  original_board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
  ]

  rival_number = 1
  my_moves_from_fn = check_rows(board=original_board, rival_number=rival_number)
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
  my_moves_from_fn = check_columns(board=original_board, rival_number=rival_number)
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
  my_moves_from_fn = check_diagonals(board=original_board, rival_number=rival_number)
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
  my_moves_from_fn = check_diagonals(board=original_board, rival_number=rival_number)
  expected_my_moves = 2

  assert(my_moves_from_fn == expected_my_moves)


def test_alpha_beta():
  graph = {
    '1': {
      'depth': 0,
      'children': ['2', '3'],
      'h(j)': None,
      'terminal': False
    },
    '2': {
      'depth': 1,
      'children': ['4', '5'],
      'h(j)': None,
      'terminal': False
    },
    '3': {
      'depth': 1,
      'children': ['6', '7'],
      'h(j)': None,
      'terminal': False
    },
    '4': {
      'depth': 2,
      'children': [],
      'h(j)': 6,
      'terminal': True
    },
    '5': {
      'depth': 2,
      'children': [],
      'h(j)': 3,
      'terminal': True
    },
    '6': {
      'depth': 2,
      'children': [],
      'h(j)': 5,
      'terminal': True
    },
    '7': {
      'depth': 2,
      'children': [],
      'h(j)': 10,
      'terminal': True
    }
  }

  root = {
    'depth': 0,
    'children': ['2', '3'],
    'h(j)': None,
    'terminal': False
  }

  alpha = -99999999999
  beta = 99999999999

  result = alpha_beta(root, alpha, beta, graph)

  assert(5 == result['h(j)'])


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
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
  ]

  result_from_fn = check_if_game_is_over(board=original_board)
  expected_result = False

  assert(result_from_fn == expected_result)


def test_check_if_game_is_over_when_it_is():
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