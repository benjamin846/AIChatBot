prompt = input("> ")

def submitPrompt(prompt):
  if prompt:
    pass
  else:
    print("No prompt provided")
    submitPrompt(prompt)

submitPrompt(prompt)
