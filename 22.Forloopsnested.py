first_names = ["BlueRay ", "Upchuck ", "Lojack ","Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []

## we can take names from both lists, add them together loop them and then merge and append them
for x in first_names:
    for y in last_names:
        full_names.append(x +" "+ y)
    print(full_names)
    break