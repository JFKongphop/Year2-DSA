def check_special_characters(input_string):
  special_characters = ['(', ')', '{', '}', '[', ']']
  
  for char in input_string:
    if char in special_characters:
      return True
  
  return False

def custom_remove(input_string, pattern):
  result = ""
  i = 0
  while i < len(input_string):
    if input_string[i:i+len(pattern)] == pattern:
      i += len(pattern)
    else:
      result += input_string[i]
      i += 1
  return result

def is_balanced(word: str) -> None:
  dict = {
    'a': '',
    'b': '',
    'c': ''
  }

  new_word = ''
  for i in word:
    if (check_special_characters(i)):
      new_word += i

  for i in new_word:
    if i == '(' or i == ')':
      dict['a'] += i

    if i == '[' or i == ']':
      dict['b'] += i

    if i == '{' or i == '}':
      dict['c'] += i

  while True:
    if (len(dict['a']) > 1 or len(dict['a']) > 1 or len(dict['a']) > 1):
      if 'a' == 'a' in dict:
        dict['a'] = custom_remove(dict['a'], '()') 
      if 'b' == 'b' in dict:
        dict['b'] = custom_remove(dict['b'], '[]') 
      if 'c' == 'c' in dict:
        dict['c'] = custom_remove(dict['c'], '{' + '}')
    else: break

  all_values_empty = all(len(value) == 0 for value in dict.values())
  return all_values_empty
       
print(is_balanced('([])[]()'))
print(is_balanced('()(()){([()])}'))
print(is_balanced('[(5+x)-(y+z)]'))
print(is_balanced('((()(()){([()])}))'))

class Empty(Exception):
  """ Error attempting to access an element from an empty container. """
  pass

class ArrayStack:
  def __init__(self):
    """ Create an empty stack. """
    self._data = []   # Initiate a nonpublic list instance
  
  def __len__(self):
    """ Return the number of elements in the stack. """
    return len(self._data)
  
  def is_empty(self):
    """ Return True if the stack is empty. """
    return len(self._data) == 0
  
  def push(self, element):
    """ Add an element to the top of the stack. """
    self._data.append(element) # new item stored at end of list
  
  def top(self):
    """ Return (but do not remove) the element at the top of the stack.
    Raise an exception if the stack is empty. """
    if self.is_empty():
      print('Stack is empty')
      raise Empty('Stack is empty') # Calling subclass Empty
    return self._data[-1] # the last item in the list

  def pop(self):
    """ Remove and return the element from the top of the stack.
    Raise an exception if the stack is empty. """
    if self.is_empty():
      print('Stack is empty')
      raise Exception('Stack is empty') # Alternate way to call subclass Empty
    return self._data.pop() # remove last item from the list
  
  def pop_all(self):
    while (len(self._data) != 0):
      self._data.pop()
    pass
  
  def printStack(self):
    print(str(self._data)
          .replace('[', '')
          .replace(']', '')
          .replace(',', '')
    )    
    pass


def is_balanced(value):
    """ Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    count = 0
    i = 0

    while i < len(value):
        if count < 0:
            return False
        if value[i] in lefty:
            S.push(value[i])
            count += 1
        elif value[i] in righty:
            if S.is_empty():
                return False
            if value[i] == ")" and S.top() == "(":
                S.pop()
                count -= 1
            elif value[i] == "]" and S.top() == "[":
                S.pop()
                count -= 1
            elif value[i] == "}" and S.top() == "{":
                S.pop()
                count -= 1
            else:
                return False
        i += 1

    return count == 0

is_balanced('({)}')
