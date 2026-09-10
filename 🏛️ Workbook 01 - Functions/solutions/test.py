def is_palindrome(s: str) -> str:
  rvsd_str = ''
  for char in reversed(s):
    rvsd_str += char
  return s == rvsd_str
print(is_palindrome('madam'))