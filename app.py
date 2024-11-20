def afficher_taches(taches):
    if len(taches) == 0:
        print("Votre liste de tâches est vide.")
    else:
        print("\nListe de tâches :")
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")
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

def gestionnaire_taches():
    taches = []
    while True:
        print("=== Gestionnaire de tâches ===")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        
        choix = input("Choisissez une option : ")
        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            supprimer_tache(taches)
        elif choix == "4":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.\n")

gestionnaire_taches()
