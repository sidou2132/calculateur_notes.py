# Applique les concepts de L1 - Université de Toulouse

def calculer_moyenne_ponderee(liste_notes, liste_coeffs):
    """
    Calcule la moyenne en fonction des coefficients.
    Notions : Boucles, Listes, Calculs arithmétiques.
    """
    somme_points = 0
    somme_coeffs = 0
    
    # On parcourt les deux listes en même temps
    for i in range(len(liste_notes)):
        somme_points += liste_notes[i] * liste_coeffs[i]
        somme_coeffs += liste_coeffs[i]
    
    if somme_coeffs == 0:
        return 0
        
    return somme_points / somme_coeffs

def verifier_validation(moyenne):
    """Vérifie si le semestre est validé ou non."""
    if moyenne >= 10:
        return "Semestre validé BG :)"
    else:
        return "Semestre non validé :(  "

if __name__ == "__main__":
    # Exemple avec mes matières 
    matieres = ["MathCalc", "MathBase", "Info", "Science Num"]
    notes = [17, 16, 19, 13]
    coefficients = [4, 4, 6, 2] # Exemple de coeffs

    moyenne_finale = calculer_moyenne_ponderee(notes, coefficients)

    print(f"--- Relevé de Notes (Simulé) ---")
    for j in range(len(matieres)):
        print(f"{matieres[j]} : {notes[j]}/20 (coeff {coefficients[j]})")
    
    print("-" * 30)
    print(f"Moyenne Générale : {moyenne_finale:.2f}/20")
    print(verifier_validation(moyenne_finale))