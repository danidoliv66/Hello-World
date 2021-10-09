def check(func):
  
  def inner(strg):
    if len(strg) > 20:
      return "You said a lot! I can't handle it."
    elif len(strg.split()) > 10:
      return "Too many words! Make a brief."
    else:
      return func(strg)
  return inner

@check()
def say(strg):
  return strg

if __name__ == '__main__':
  say(input("Do you wanna say something?\n "))
