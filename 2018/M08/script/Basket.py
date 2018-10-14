class Basket:
  def __init__(self, contents=[]):
    self.contents22 = contents[:]

  def add(self, element):
    self.contents22.append(element)

  def __str__(self):
    result = ""
    for element in self.contents22:
      result = result + ":" + repr(element)
    return "Contains:" + result

b = Basket(['apple','orange'])
b.add("lemon")
print b
