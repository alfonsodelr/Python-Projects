def cipher(original_string):
#ord of the first letter of the string to cipher each letter including the first letter. 
  key = ord(original_string[0])
  length = len(original_string)
  new_string=""
  for i in range(0,length-1,1):
    new_string += chr(ord(original_string[i])+key)
  return new_string