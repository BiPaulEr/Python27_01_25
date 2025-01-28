equipe_a = {'Alice', 'Charles', 'Diane', 'Fabien'} #front_end
equipe_b = {'Bernard', 'Diane', 'Eloise', 'Fabien'} #back_end

#intersection
print("intersection")
print(equipe_a & equipe_b)

#union
print("union")
print(equipe_a | equipe_b)

#xor
print("unqiue dans chaque equipe")
print(equipe_a ^ equipe_b)

#xor
print("unqiue dans chaque equipe")
print((equipe_a | equipe_b) - (equipe_a & equipe_b))