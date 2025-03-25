import numpy as np
# Nural network var
inputVector = np.array([1.66, 1.56])
wheights1 = np.array([1.45, -0.66])
bias = np.array([0.0])

prompt = input("> ")

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def submitPrompt(prompt, inputVecters, weights, bias):
  layer1 = np.dot(inputVecters, weights) + bias
  if prompt:
    pass
  else:
    print("No prompt provided")
    submitPrompt(prompt)

submitPrompt(prompt, inputVector, weights1, bias)
