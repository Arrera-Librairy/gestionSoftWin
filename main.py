from gestionSoftWindows import*


def main():
    gestionSoft = gestionSoftWindows("C:/")
    gestionSoft.setEmplacementSoft()
    gestionSoft.setName("test")
    gestionSoft.saveSoftware()
    #gestionSoft.supprSoft("test")
    print(gestionSoft.getName())

if __name__ == "__main__":
    main()