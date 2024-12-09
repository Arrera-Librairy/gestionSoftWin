import shutil
import os
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import messagebox

class gestionSoftWindows :
    def __init__(self,emplacement:str):
        self.__emplacement = emplacement
    
    def setEmplacementSoft(self)->str:
        messagebox.showinfo("Information","Choisir un le dossier ou enregistrer les logiciel")
        self.__emplacement = filedialog.askdirectory()
        return self.__emplacement

    def setName(self,name:str)->bool:
        if not name :
            return False
        else :
            self.name = name
            return True
    
    def saveSoftware(self)->bool:
        self.racourcieSoft =os.path.abspath(self.__emplacement+"/"+self.name+".lnk")
        emplacement = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk")])
        if emplacement:
            shutil.copyfile(emplacement,self.racourcieSoft)
            return True
        else :
            return False
    
    def supprSoft(self,name)->bool:
        sortie = os.remove(self.__emplacement+"/"+name+".lnk")
        if (sortie==OSError):
            return False 
        else :
            return True
    
    def getName(self)-> str:
        return str(self.name)  