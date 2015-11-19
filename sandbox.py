
import os
import fonction_en_vrac

fonction_en_vrac.afficher_flottant(3.9999999999)
fonction_en_vrac.afficher_flottant(1.5)
fonction_en_vrac.afficher(1,2,'test',sep=" \\ ",end=" c'est fini")

inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraises", 76),("prunes", 51),]
print(fonction_en_vrac.tri(inventaire))

os.system("pause")