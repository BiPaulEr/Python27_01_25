noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

etudiant = list(zip(noms, scores))
print(etudiant) #[('Alice', 85), ('Bob', 92), ('Charlie', 78)]

def calculer_note_20(liste):
    liste_20 = map(lambda x : (x[0], x[1]/5), liste)
    return list(liste_20)

etudiant_20 = calculer_note_20(etudiant)
print(etudiant_20) #[('Alice', 17.0), ('Bob', 18.4), ('Charlie', 15.6)]

def filter_etudiant(liste, score):
    liste_filtre = filter(lambda x : x[1] >= score, liste)
    return list(liste_filtre)

etudiant_score_17 = filter_etudiant(etudiant_20, 17)
print(etudiant_score_17) #[('Alice', 17.0), ('Bob', 18.4)]

#[('Alice', 17.0), ('Bob', 18.4)] -> [17, 18.4]

def extraire_note(liste):
    liste_note = map(lambda x : x[1], liste)
    return list(liste_note)

def moyenne_etudiant(liste):
    notes = extraire_note(liste)
    if not notes:
        return 0
    moyenne = sum(etudiant_score_17_note) / len(etudiant_score_17_note)
    return moyenne

etudiant_score_17_note = extraire_note(etudiant_score_17)
print(etudiant_score_17_note) #[17.0, 18.4]

print(moyenne_etudiant(etudiant_score_17)) #17.7
