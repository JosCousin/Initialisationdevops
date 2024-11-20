def afficher_taches(taches):
    if len(taches) == 0:
        print("Votre liste de tâches est vide.")
    else:
        print("\nListe de tâches :")
        for i in enumerate(len(taches)):
            print(i, taches[i])
    print()

def ajouter_tache(taches):
    nouvelle_tache = input("Entrez la nouvelle tâche : ")
    taches.append(nouvelle_tache)
    print(f"Tâche ajoutée : {nouvelle_tache}\n")

def supprimer_tache(taches):
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

def ajouter_tache(nouvelle_tache):
    taches=[]
    if nouvelle_tache.isdigit():
        return "facho"
    else:
        taches.append(nouvelle_tache)
        return "c'est good mon gars"
        

