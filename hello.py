def check(func):
  
  def inner(strg):
    if len(strg) > 60:
      strg =  "You said a lot! I can't handle it."
    elif len(strg.split()) > 10:
      strg = "Too many words! Make a brief."
    return func(strg)

  return inner

@check
def say(strg):
  return 'You said: ' + strg

if __name__ == '__main__':
  sentence = say(input("Do you wanna say something?\n "))
  print(sentence)
