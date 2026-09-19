import shutil
from pathlib import Path
import logging
from threading import Thread
import sys

class Threading():                              #Класс потоку
    def __init__(self,directory,dist):
        self.directory=directory
        self.dist=dist
    def __call__(self):
        analis(self.directory, self.dist)

def copying(file:Path, folder_in_dist:Path):            #Функція, яка переміщає файл у потрібну папку
    try: 
        shutil.copy(str(file), folder_in_dist)
    except FileNotFoundError :
        logging.debug("Директорію куди потрібно перенести файли не знайдено")

def analis(directory, dist):
    print(sys.argv)                           #Функція яка аналізує папки і файли
    for file in directory.iterdir():
        if file.is_dir():                               #Якщо це папка - створюємо потік який при старті починає для себе функцію analis
            t=Threading(file, dist)
            thread = Thread(target=t)
            thread.start()
                
        else:                                           #Якщо це файл - взнаємо його розширенння і прибираємо крапку.
            sufix=str(file.suffix).replace(".","")
            new_folder=dist/sufix
            new_folder.mkdir(exist_ok=True)             #Якщо папки немає для вказаних розширень - створюємо
            copying(file, dist/sufix)




if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    directory=Path(sys.argv[1])
    if len(sys.argv)>2:
        dist=Path(sys.argv[2])
    else:    
        dist=Path("dist")
        dist.mkdir()
    if directory.is_dir():          
        analis(directory, dist)     
    else:
        logging.debug("Це не директорія або неправильний шлях")     
    