# add (adiciona), update (atualiza), clear, discard
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_diference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5,6}

print(type(s1))


for v in s1:
    print(v)


s2 = set()

s2.add(1)
s2.add((1,2,3,'Luiz'))
s2.discard(1)
s2.update('python')




print(s2)