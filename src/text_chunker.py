def split_by_newline_caps(text):
  """Splits a string by the pattern 'newline + caps lock letter'."""
  #return re.split(r'\n(?=[A-Z])', text)
  return re.findall(r"<s>(.*?)<\\s>", text, re.DOTALL)