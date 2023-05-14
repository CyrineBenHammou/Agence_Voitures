from Agence import Agence
from Transformation_données import TransformationVoiture
from Transformation_Images import TransformationImageVoiture
from Recherche_similarite import Recherche_par_similarité




if __name__ == '__main__':

    a = Agence()
    df=a.to_df()
    
    print('Choisissez une des options suivantes : \n1: Afficher la liste des voitures \n2: Manipulation des données \n3: Recherche \n0: Quitter')
    option = input('Entrez votre choix : ')


    if option == '1':
        a.afficher_voitures()

    elif option == '2':
        print('1: Ajouter une voiture \n2: Supprimer une voiture \n0: Quitter')
        option = input('Entrez votre choix : ')

        if option == '1':
            a.ajouter_voiture()

        elif option == '2':
            a.supprimer_voiture()

        elif option == '0':
            print('Quitter')

        else:
            print('Option invalide !')
    
    
    elif option == '3':
        print('1: Par saisi de données \n2: Par image \n3: Par description \n0: Quitter')
        option = input('Entrez votre choix : ')

        if option == '1':
            v = a.V_requete()
            df_ = df.append(v, ignore_index=True)
            print(df_)
            Trans_voit = TransformationVoiture()
            transformed_data = Trans_voit.transform(df_)
            Rech= Recherche_par_similarité()
            d = Rech.calcule_distance(transformed_data[-1],transformed_data[:-1])
            i= Rech.trier_distance(d)
            Rech.afficher_voiture_similaire(df,i)

        elif option == '2':
            df_i = df.iloc[:, -1]
            r=input('Donnez le schema de l''image de la voiture')
            df_i.loc[len(df_i)] = r
            
            I=[]
            Trans_img = TransformationImageVoiture()
            for row in df_i:
                I.append(Trans_img.transform(row))

            Rech= Recherche_par_similarité()
            d = Rech.calcule_distance(I[-1],I[:-1])
            i= Rech.trier_distance(d)
            Rech.afficher_voiture_similaire(df,i)


        elif option == '3':
        # do something for option 2
            pass

        elif option == '0':
            print('Quitter')

        else:
            print('Option invalide !')

       
    elif option == '0':

        print('Quitter')

    else:
        print('Option invalide !')
