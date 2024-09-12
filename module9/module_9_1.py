def apply_all_func(int_list, *functions):

  results = {}
  for func in functions:
    results[func.__name__] = func(int_list)
  return results

