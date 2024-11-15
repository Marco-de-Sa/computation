name, nameNew = ["Ann", "Mary", "Jane", "Sue"], []
nameNew = [f"{name[i]} {name[j]}" for i in range(len(name)) for j in range(len(name)) if name[i]!=name[j]]
# for i in range(len(name)):
#     for j in range(len(name)):
#         if name[i]!=name[j]:
#             nameNew.append(f"{name[i]} {name[j]}")
print(nameNew)