"""
Module pour gérer une liste de tâches (To-Do List).
"""

def afficher_taches(taches):
    """
    Affiche la liste des tâches avec leurs indices.
    """
    if len(taches) == 0:
        print("Votre liste de tâches est vide.")
    else:
        print("\nListe de tâches :")
        for i, tache in enumerate(taches, start=1):  # Indexation à partir de 1
            print(f"{i}. {tache}")
    print()

def ajouter_tache(taches):
    """
    Ajoute une nouvelle tâche à la liste.
    """
    nouvelle_tache = input("Entrez la nouvelle tâche : ")
    taches.append(nouvelle_tache)
    print(f"Tâche ajoutée : {nouvelle_tache}\n")

def supprimer_tache(taches):
    """
    Supprime une tâche de la liste en fonction de son index.
    """
    afficher_taches(taches)
    if len(taches) == 0:
        print("Aucune tâche à supprimer.\n")
        return

    index = input("Entrez le numéro de la tâche à supprimer : ")
    if index.isdigit():
        index = int(index)
        if 1 <= index <= len(taches):
            tache_supprimee = taches[index - 1]
            del taches[index - 1]
            print(f"Tâche supprimée : {tache_supprimee}\n")
        else:
            print("Numéro invalide. Veuillez entrer un numéro valide.\n")
    else:
        print("Entrée invalide. Veuillez entrer un numéro.\n")

def ajouter_tache_test(nouvelle_tache):
    """
    Ajoute une nouvelle tâche à une liste dans un contexte de test unitaire.
    Retourne une chaîne pour valider les entrées.
    """
    taches = []
    if nouvelle_tache.isdigit():
        return "facho"
    taches.append(nouvelle_tache)
    return "c'est good mon gars"
