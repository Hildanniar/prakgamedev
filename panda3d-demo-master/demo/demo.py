from panda3d.core import * #library
from direct.showbase.ShowBase import ShowBase #import direct.showbase.ShowBase

class Mygame(ShowBase): #membuat class bernama Mygame
    def __init__(self): #mengaktifkan properti class
        super().__init__() #mengembalikan atribut dan metode dari super objek (induk) suatu kelas

        #muat model dan barang di sini
        vanilla = self.loader.loadModel("vanilla.egg") #memanggil gambar
        vanilla.setPos(0, 10, 0) #mencari posisi sebuah karakter atau sebuah string di dalam string lainnya
        vanilla.setScale(0.2, 0.2, 0.2) #mengatur ukuran gambar
        vanilla.reparentTo(self.render) 

#Main Loop
game = Mygame()
game.run()