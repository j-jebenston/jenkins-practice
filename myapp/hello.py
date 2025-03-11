import fire
# import fire is necessary to use fire.Fire()
def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)