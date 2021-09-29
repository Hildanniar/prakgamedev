# prakgamedev
2.	Langkah selanjutnya adalah, identifikasi pada bagian manakah implementasi AI pada program game tersebut. Jelaskan ! 
    ini merupakan implementasi AI pada program, karena membuat gerakan/control dari papan pingpongnya dengan perintah Key UP dan Key DOWN
    
    class Opponent(Block): #ini adalah bagian opponent AI/Artificial Intelegence
	def __init__(self,path,x_pos,y_pos,speed): #membuat fungsi init yang mengambil posisi dari self,path,x_pos,y_pos,speed
		super().__init__(path,x_pos,y_pos) 
		self.speed = speed #membuat properti speed

	def update(self,ball_group):                       
		if self.rect.top < ball_group.sprite.rect.y: #jika paddle yang berada di posisi atas maka posisi bola akan memantulkan lawan arah 
			self.rect.y += self.speed #akan bertambah kecepatannya 
		if self.rect.bottom > ball_group.sprite.rect.y: #jika paddle yang berada di posisi bawah maka posisi bola akan memantul ke atas atau lawan arah
			self.rect.y -= self.speed
		self.constrain() 

	def constrain(self): #sebagai fungsi pembatas permainan
		if self.rect.top <= 0: self.rect.top = 0 #ketika musuh berada disisi atas 
		if self.rect.bottom >= screen_height: self.rect.bottom = screen_height #ketika musuh berada di sisi bawah dan tidak lebih sama dengan ukuran layar atau self.rect.bottom = screen_height

4.	Jelaskan bagaimana alur AI yang digunakan pada program tersebut ! 
    mengatur gerak bola dan paddle pada program game pingpong
