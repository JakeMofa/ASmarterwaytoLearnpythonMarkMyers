particulars = {
  "last name": "Verdi",
  "first name": "Giuseppe",
  "profession": "composer   ",
}
  
valuest = []
def loopthrough():
  for x in particulars.values():
    valuest.append(x)
  return(f"this is the key values.: {valuest}") 
# print(f"this is the key values: {valuest}") 

  
result = loopthrough()
print(result)