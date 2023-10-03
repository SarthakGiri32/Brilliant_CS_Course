sentence = "a breakfast for billy the bee is an early egg"

# sentence = sentence.replace("e", "a")
sentence = sentence.replace("e", "@")
print("Step 1:", sentence)
# sentence = sentence.replace("a", "b")
sentence = sentence.replace("a", "e")
print("Step 2:", sentence)
sentence = sentence.replace("@", "a")
print("Step 3:", sentence)
# sentence = sentence.replace("b", "e")

print(sentence)
