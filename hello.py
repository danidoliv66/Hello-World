def check(func):
  
  def inner(str):
    if len(str) > 20:
      return "You said a lot! I can't handle it."
    elif len(str.split()) > 10:
      return "Too many words! Make a brief."
    else:
      return func(str)
  return inner

@check()
def say(str):
  return str

if __name__ == '__main__':
  say(input("Do you wanna say something?\n "))
