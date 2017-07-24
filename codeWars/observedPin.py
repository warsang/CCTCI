import copy

class stack(object):
    
    def __init__(self,values = []):
        self.values = values
    
    def pop(self):
        value = self.values[-1]
        self.values = self.values[:-1]
        return value
    
    def push(self, newValue):
        self.values.append(newValue)
        

def get_pins(observed):
  '''TODO: This is your job, detective!'''
  hash_table = {'1':['1','2','4'],'2':['1','2','3','5'],'3':['2','3','6'],'4':['1','4','5','7'],'5':['2','4','5','6','8']
  ,'6':['3','5','6','9'],'7':['4','7','8'],'8':['5','7','8','9','0'],'9':['6','8','9'],'0':['0','8']}
  result1 = stack([])
  result2 = stack([])
  for element in observed:
      result1.push(element)
  for element in observed:
      length1 = len(hash_table[element])
      if len(result1.values) == 0:
          empty_stack = result1
          to_empty = result2
      elif len(result2.values) == 0:
          empty_stack = result2
          to_empty = result1
      while len(to_empty.values) != 0:
          tab = to_empty.pop()
          for i in hash_table[element]:
              temp = copy.copy(tab)
              temp += i
              empty_stack.push(temp)
  if len(result1.values) != 0:
    for i,j in enumerate(result1.values):
        result1.values[i] = j[1:]
    return list(set(result1.values))
  else:
    for i,j in enumerate(result2.values):
        result2.values[i] = j[1:]
    return list(set(result2.values))

'''expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]
'''
print(get_pins('8'))
print(get_pins('11'))
