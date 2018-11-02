import random
import tkinter
import math

class Blackjack():
	def __init__(self, master):
	
		#Menu
		glavniMenu = tkinter.Menu(master)
		master.config(menu = glavniMenu)
		
		menuBJ = tkinter.Menu(glavniMenu)
		glavniMenu.add_cascade(label = 'Blackjack', menu=menuBJ)
		menuBJ.add_cascade(label = 'New Game', command = self.newGame)
		menuBJ.add_cascade(label = 'Quit', command = master.destroy)
		
		#zeleno platno (igralna povrsina)
		self.platno = tkinter.Canvas(master, width = 700, height = 480, bg = 'green')
		self.platno.grid(row = 0, column = 0)
		
		#Crte
		self.pokoncaCrta = self.platno.create_line(500, 0, 500, 600, width = 4)
		self.lezecaCrta = self.platno.create_line(0, 410, 500, 410, width = 4)
		
		
		#####Spremenljivke
		self.sezKart = ['karte/1.gif', 'karte/2.gif', 'karte/3.gif', 'karte/4.gif', 'karte/5.gif',
		'karte/6.gif', 'karte/7.gif', 'karte/8.gif', 'karte/9.gif', 'karte/10.gif',
		'karte/11.gif', 'karte/12.gif', 'karte/13.gif', 'karte/4.gif', 'karte/15.gif',
		'karte/16.gif', 'karte/17.gif', 'karte/18.gif', 'karte/19.gif', 'karte/20.gif',
		'karte/21.gif', 'karte/22.gif', 'karte/23.gif', 'karte/24.gif', 'karte/25.gif',
		'karte/26.gif', 'karte/27.gif', 'karte/28.gif', 'karte/29.gif', 'karte/30.gif',
		'karte/31.gif', 'karte/32.gif', 'karte/33.gif', 'karte/34.gif', 'karte/35.gif',
		'karte/36.gif', 'karte/37.gif', 'karte/38.gif', 'karte/39.gif', 'karte/40.gif',
		'karte/41.gif', 'karte/42.gif', 'karte/43.gif', 'karte/44.gif', 'karte/45.gif',
		'karte/46.gif', 'karte/47.gif', 'karte/48.gif', 'karte/49.gif', 'karte/50.gif',
		'karte/51.gif', 'karte/52.gif']
		
		self.credit = 1000 #toliko dobimo na zacetku
		self.vsotaStave = 0 #trenutna stava
		
		self.scorePlayer = 0 #tocke igralca
		self.scoreDealer = 0 #tocke dealerja
		
		#seznam igralcevih kart
		self.indexIgralceveKarte = 0 #katero karto damo na platno, dve karti dobimo ob inic. izbiramo tretjo
		self.sezKartIgralec = ['','',''] #dejanska imena kart za sklicevanje
		self.sezKartIgralecPlatno = ['','',''] #da bodo karte vidne na zaslonu
		
		  #Pozicja (x,y) za igralceve karte
		self.pX = 260
		self.pY = 350
		
		
		
		#seznam dealerjevih kart
		self.indexDealerjeveKarte = 0 #katero karto damo na platno, dve karti dobimo ob inic. izbiramo tretjo
		self.sezKartDealer = ['','',''] #dejanska imena kart za sklicevanje
		self.sezKartDealerPlatno = ['','',''] #da bodo karte vidne na zaslonu
		
			#Pozicja (x,y) za dealerjeve karte
		self.dX = 260
		self.dY = 120
		
		#####
		
		
		#####Napisi
		
		#Zgolj napis kje so igralceve karte
		self.napisIgralec = tkinter.Label(text = 'Player:', bg = 'green', fg = 'blue', font = ('Helvetica', 18, 'bold'))
		self.napisIgralecNaPlatnu = self.platno.create_window(55, 280, window = self.napisIgralec)
		
		#Zgolj napis kje do Dealerjeve karte
		self.napisDealer = tkinter.Label(text = 'Dealer:', bg = 'green', fg = 'red', font = ('Helvetica', 18, 'bold'))
		self.napisDealerNaPlatnu = self.platno.create_window(55, 50, window = self.napisDealer)
		
		#Zgolj napis, da je pod tem napisom igralcevo financno stanje
		self.napisCredit = tkinter.Label(text = 'Credit:', bg = 'green', font = ('Helvetica', 23, 'bold'))
		self.napisCreditNaPlatnu = self.platno.create_window(600, 40, window = self.napisCredit)
		
		#Zgolj napis, da je pod tem napisom igralceva trenutna stava
		self.napisCurrentBet = tkinter.Label(text = 'Current Bet:', bg = 'green', font = ('Helvetica', 23, 'bold'))
		self.napisCurrentBetNaPlatnu = self.platno.create_window(600, 250, window = self.napisCurrentBet)
		
		#Dejanski napis, ki prikazuje igralcevo financno stanje
		self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
		self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
		
		#Dejanski napis, ki prikazuje igralcevo trenutno stavo
		self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
		self.vsotaStaveNapisPlatno = self.platno.create_window(610, 295, window = self.vsotaStaveNapis)
		
		##Tukaj so napisi za navodila igralcu
		
		self.pWin = tkinter.Label(text = 'Player Wins!', bg = 'green', font = ('Helvetica', 24, 'bold'))
		self.pBlackjack = tkinter.Label(text = 'Blackjack! Player Wins!', bg = 'green', font = ('Helvetica', 21, 'bold'))
		self.pBust = tkinter.Label(text = 'Player Busts!', bg = 'green', fg = 'red', font = ('Helvetica', 21, 'bold'))
		
		self.dWin = tkinter.Label(text = 'Delaer Wins!', bg = 'green', fg = 'red', font = ('Helvetica', 23, 'bold'))
		self.dBlackjack = tkinter.Label(text = 'Dealer hits Blackjack! You Lose!', bg = 'green', font = ('Helvetica', 25, 'bold'))
		self.dBust = tkinter.Label(text = 'Dealer Busts! Player Wins!', bg = 'green', font = ('Helvetica', 25, 'bold'))
		self.draw = tkinter.Label(text = 'It is a Draw!', bg = 'green', font = ('Helvetica', 23, 'bold'))
		
		self.hitORstand = tkinter.Label(text = 'Hit or Stand', bg = 'green', font = ('Helvetica', 23, 'bold'))
		self.maxReached = tkinter.Label(text = 'Maximum of 5 cards reached!', bg = 'green', fg = 'red', font = ('Helvetica', 15, 'bold'))
		self.placeBet = tkinter.Label(text = 'Place your bet and decide wether to Hit or Stand', bg = 'green', font = ('Helvetica', 11, 'bold'))
		self.emptyBank = tkinter.Label(text = 'Player ran out of money. Please choose new game.', bg = 'green', font = ('Helvetica', 8, 'bold'))
		#####
		
		#####Gumbi
		self.gumbHit = tkinter.Button(master, text = 'HIT', command = self.hit, state = 'disabled')
		self.gumbHitNaPlatnu = self.platno.create_window(30, 450, window = self.gumbHit)
		
		
		self.gumbStand = tkinter.Button(master, text = 'STAND', command = self.stand, state = 'disabled')
		self.gumbStandNaPlatnu = self.platno.create_window(90, 450, window = self.gumbStand)
		
		self.gumbNaprej = tkinter.Button(master, text = 'Next Round', command = self.naslednjaRoka)
		#To bos se potreboval
		self.gumbNaprejNaPlatnu = ''
		
		self.gumb10 = tkinter.Button(master, text = '$10', command = self.dodaj10)
		self.gumb10NaPlatnu = self.platno.create_window(300, 450, window = self.gumb10)
		
		self.gumb20 = tkinter.Button(master, text = '$20', command = self.dodaj20)
		self.gumb20NaPlatnu = self.platno.create_window(360, 450, window = self.gumb20)
		
		self.gumb50 = tkinter.Button(master, text = '$50', command = self.dodaj50)
		self.gumb50NaPlatnu = self.platno.create_window(420, 450, window = self.gumb50)
		#####
		
		#Prva vrstica
		#self.SlikaNaPlatnu11 = self.platno.create_image(60, 120, image = self.karta1)
		#self.SlikaNaPlatnu12 = self.platno.create_image(160, 120, image = self.karta1)
		#self.SlikaNaPlatnu13 = self.platno.create_image(260, 120, image = self.karta1)
		#self.SlikaNaPlatnu14 = self.platno.create_image(360, 120, image = self.karta1)
		#self.SlikaNaPlatnu15 = self.platno.create_image(460, 120, image = self.karta1)
		
		#Druga vrstica
		#self.SlikaNaPlatnu21 = self.platno.create_image(60, 350, image = self.karta2)
		#self.SlikaNaPlatnu22 = self.platno.create_image(160, 350, image = self.karta2)
		#self.SlikaNaPlatnu23 = self.platno.create_image(260, 350, image = self.karta2)
		#self.SlikaNaPlatnu24 = self.platno.create_image(360, 350, image = self.karta2)
		#self.SlikaNaPlatnu25 = self.platno.create_image(460, 350, image = self.karta2)
	
		#Tukaj inicializiramo igro...
		random.shuffle(self.sezKart)#premesamo kup kart
		
		##Najprej inicializiramo igralca
		self.prvaKartaPlayer = self.sezKart.pop() #izberemo prvo karto igralcu
		self.vrednost = self.vrednostKarte(self.prvaKartaPlayer) # dolocimo vrednost prve karte
		self.scorePlayer += self.vrednost
		self.prvaKartaPlayer = tkinter.PhotoImage(file = self.prvaKartaPlayer) #Playing with fire
		self.prvaKartaPlayerNaPlatnu = self.platno.create_image(60, 350, image = self.prvaKartaPlayer)
		
		self.drugaKartaPlayer = self.sezKart.pop() #izberemo drugo karto igralcu
		self.vrednost = self.vrednostKarte(self.drugaKartaPlayer) # dolocimo vrednost druge karte
		#ce dobimo se enega asa bi presegli 21, torej se as steje kot 1
		if self.vrednost == 11 and self.scorePlayer > 10:
			self.vrednost = 1
		self.scorePlayer += self.vrednost
		self.drugaKartaPlayer = tkinter.PhotoImage(file = self.drugaKartaPlayer) #Playing with fire
		self.drugaKartaPlayerNaPlatnu = self.platno.create_image(160, 350, image = self.drugaKartaPlayer)
		##
		
		##Potem inicializiramo dealerja
		self.prvaKartaDealer = self.sezKart.pop() #izberemo prvo karto dealerju
		self.vrednost = self.vrednostKarte(self.prvaKartaDealer) # dolocimo vrednost prve karte
		self.scoreDealer += self.vrednost
		self.prvaKartaDealer = tkinter.PhotoImage(file = self.prvaKartaDealer) #Playing with fire
		self.prvaKartaDealerNaPlatnu = self.platno.create_image(60, 120, image = self.prvaKartaDealer)
		
		self.drugaKartaDealer = self.sezKart.pop() #izberemo drugo karto dealerju
		self.vrednost = self.vrednostKarte(self.drugaKartaDealer) # dolocimo vrednost druge karte
		#ce dobimo se enega asa bi presegli 21, torej se as steje kot 1
		if self.vrednost == 11 and self.scoreDealer > 10:
			self.vrednost = 1 
		self.scoreDealer += self.vrednost
		self.drugaKartaDealer = tkinter.PhotoImage(file = self.drugaKartaDealer) #Playing with fire
		self.drugaKartaDealerNaPlatnu = self.platno.create_image(160, 120, image = self.drugaKartaDealer)
		
		#Po pravilih je druga karta dealerja zakrita
		self.zakritaKarta = tkinter.PhotoImage(file = 'karte/back.gif')
		self.zakritaKartaNaPlatnu = self.platno.create_image(160, 120, image = self.zakritaKarta)
		##
		
		#Na platno postavimo navodila, kaj naj igralec stori
		self.navodilaPlatno = self.platno.create_window(270, 230, window = self.placeBet)
	
		
		
	def vrednostKarte(self, karta):
		if karta == 'karte/1.gif' or karta == 'karte/2.gif' or karta == 'karte/3.gif' or karta == 'karte/4.gif':
			return 11
		if karta == 'karte/5.gif' or karta == 'karte/6.gif' or karta == 'karte/7.gif' or karta == 'karte/8.gif' or karta == 'karte/9.gif' or karta == 'karte/10.gif' or karta == 'karte/11.gif' or karta == 'karte/12.gif' or karta == 'karte/13.gif' or karta == 'karte/14.gif' or karta == 'karte/15.gif' or karta == 'karte/16.gif' or karta == 'karte/17.gif' or karta == 'karte/18.gif' or karta == 'karte/19.gif' or karta == 'karte/20.gif':
			return 10
		if karta == 'karte/21.gif' or karta == 'karte/22.gif' or karta == 'karte/23.gif' or karta == 'karte/24.gif':
			return 9
		if karta == 'karte/25.gif' or karta == 'karte/26.gif' or karta == 'karte/27.gif' or karta == 'karte/28.gif':
			return 8
		if karta == 'karte/29.gif' or karta == 'karte/30.gif' or karta == 'karte/31.gif' or karta == 'karte/32.gif':
			return 7
		if karta == 'karte/33.gif' or karta == 'karte/34.gif' or karta == 'karte/35.gif' or karta == 'karte/36.gif':
			return 6
		if karta == 'karte/37.gif' or karta == 'karte/38.gif' or karta == 'karte/39.gif' or karta == 'karte/40.gif':
			return 5
		if karta == 'karte/41.gif' or karta == 'karte/42.gif' or karta == 'karte/43.gif' or karta == 'karte/44.gif':
			return 4
		if karta == 'karte/45.gif' or karta == 'karte/46.gif' or karta == 'karte/47.gif' or karta == 'karte/48.gif':
			return 3
		if karta == 'karte/49.gif' or karta == 'karte/50.gif' or karta == 'karte/51.gif' or karta == 'karte/52.gif':
			return 2
		
	
	def dodaj10(self):
		if self.credit >= 10:
			self.gumbHit.config(state = 'normal')
			self.gumbStand.config(state = 'normal')
			#stava se poveca
			self.vsotaStave += 10
			self.platno.delete(self.vsotaStaveNapisPlatno)
			self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
			#credit se zmanjsa
			self.credit -= 10
			self.platno.delete(self.creditNapisPlatno)
			self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
		else:
			pass
	
	def dodaj20(self):
		if self.credit >= 20 :
			self.gumbHit.config(state = 'normal')
			self.gumbStand.config(state = 'normal')
			#stava se poveca
			self.vsotaStave += 20
			self.platno.delete(self.vsotaStaveNapisPlatno)
			self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
			#credit se zmanjsa
			self.credit -= 20
			self.platno.delete(self.creditNapisPlatno)
			self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
		else:
			pass
			
	def dodaj50(self):
		if self.credit >= 50:
			self.gumbHit.config(state = 'normal')
			self.gumbStand.config(state = 'normal')
			#stava se poveca
			self.vsotaStave += 50
			self.platno.delete(self.vsotaStaveNapisPlatno)
			self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
			#credit se zmanjsa
			self.credit -= 50
			self.platno.delete(self.creditNapisPlatno)
			self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
		else:
			pass
			
	def hit(self):
		self.gumbStand.config(state = 'normal')
		self.gumb10.config(state = 'disabled')
		self.gumb20.config(state = 'disabled')
		self.gumb50.config(state = 'disabled')
		
		
		if self.indexIgralceveKarte >= 3: #Ne moremo imeti vec kot 5 kart
			self.platno.delete(self.navodilaPlatno)
			self.navodilaPlatno = self.platno.create_window(310, 230, window = self.maxReached)
			self.gumbHit.config(state = 'disabled')
		
		else:
			self.platno.delete(self.navodilaPlatno)
			self.navodilaPlatno = self.platno.create_window(310, 230, window = self.hitORstand)
			
			#iz premesanega kupa izberemo karto
			self.sezKartIgralec[self.indexIgralceveKarte] = self.sezKart.pop()
			#dolocimo vrednost izbrane karte
			self.vrednost = self.vrednostKarte(self.sezKartIgralec[self.indexIgralceveKarte])
			#ce smo dobili asa, ki je vreden 11 vendar bi nam bolj pasala 1 si stejemo 1
			if self.vrednost == 11 and self.scorePlayer > 10:
				self.vrednost = 1
			#povecamo skupno vsoto
			self.scorePlayer += self.vrednost
		
			#karto nalozimo, da bi jo lahko prikazali
			self.sezKartIgralec[self.indexIgralceveKarte] = tkinter.PhotoImage(file = self.sezKartIgralec[self.indexIgralceveKarte])
			#karto prikazemo na zaslonu
			self.sezKartIgralecPlatno[self.indexIgralceveKarte] = self.platno.create_image(self.pX, self.pY, image = self.sezKartIgralec[self.indexIgralceveKarte])
		
			if self.scorePlayer == 21:
				#Sporocimo igralcu kaj se je zgodilo
				self.platno.delete(self.navodilaPlatno)
				self.navodilaPlatno = self.platno.create_window(310, 230, window = self.pBlackjack)
				
				#zmagali smo torej si zasluzimo denar
				self.credit += (self.vsotaStave*2)
				self.vsotaStave = 0
				self.platno.delete(self.creditNapisPlatno)
				self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
				self.platno.delete(self.vsotaStaveNapisPlatno)
				self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
				
				self.gumbHit.config(state = 'disabled')
				self.gumbStand.config(state = 'disabled')
				self.gumb10.config(state = 'disabled')
				self.gumb20.config(state = 'disabled')
				self.gumb50.config(state = 'disabled')
				self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
				
				if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
			if self.scorePlayer > 21:
				#igralcu sporocimo, kaj se je zgodilo
				self.platno.delete(self.navodilaPlatno)
				self.navodilaPlatno = self.platno.create_window(310, 230, window = self.pBust)
				
				#izgubili smo, torej smo izgubili trenutno stavo
				self.vsotaStave = 0
				self.platno.delete(self.creditNapisPlatno)
				self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
				self.platno.delete(self.vsotaStaveNapisPlatno)
				self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
				
				self.gumbHit.config(state = 'disabled')
				self.gumbStand.config(state = 'disabled')
				self.gumb10.config(state = 'disabled')
				self.gumb20.config(state = 'disabled')
				self.gumb50.config(state = 'disabled')
				self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
				
				if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
			self.indexIgralceveKarte += 1 #s tem naredimo prostor za naslednjo karto
			self.pX += 100 #premaknemo pozicijo, da bi lahko prikazali novo karto
	
	
	def stand(self):
		#self.gumbStand.config(state = 'disabled')
		#self.gumbHit.config(state = 'normal')
		self.platno.delete(self.zakritaKartaNaPlatnu)
		while self.scoreDealer < 15:
			#iz premesanega kupa izberemo karto
			self.sezKartDealer[self.indexDealerjeveKarte] = self.sezKart.pop()
			#dolocimo vrednost izbrane karte
			self.vrednost = self.vrednostKarte(self.sezKartDealer[self.indexDealerjeveKarte])
			#spremenimo vrednost asa iz 11 v ena ce nam bolj pase
			if self.vrednost == 11 and self.scoreDealer > 10:
				self.vrednost = 1
			self.scoreDealer += self.vrednost
		
			#karto nalozimo, da bi jo lahko prikazali
			self.sezKartDealer[self.indexDealerjeveKarte] = tkinter.PhotoImage(file = self.sezKartDealer[self.indexDealerjeveKarte])
			#karto prikazemo na zaslonu
			self.sezKartDealerPlatno[self.indexDealerjeveKarte] = self.platno.create_image(self.dX, self.dY, image = self.sezKartDealer[self.indexDealerjeveKarte])
			
			self.indexDealerjeveKarte += 1 #s tem naredimo prostor za naslednjo karto
			self.dX += 100 #premaknemo pozicijo, da bi lahko prikazali novo karto
			
			if self.scoreDealer > 21:
				#Sporocimo igralcu kaj se je zgodilo
				self.platno.delete(self.navodilaPlatno)
				self.navodilaPlatno = self.platno.create_window(310, 230, window = self.dBust)
				
				#zmagali smo torej si zasluzimo denar
				self.credit += (self.vsotaStave*2)
				self.vsotaStave = 0
				self.platno.delete(self.creditNapisPlatno)
				self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
				self.platno.delete(self.vsotaStaveNapisPlatno)
				self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
				
				self.gumbHit.config(state = 'disabled')
				self.gumbStand.config(state = 'disabled')
				self.gumb10.config(state = 'disabled')
				self.gumb20.config(state = 'disabled')
				self.gumb50.config(state = 'disabled')
				self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
				
				if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
				
			elif self.scoreDealer == 21:
				#igralcu sporocimo, kaj se je zgodilo
				self.platno.delete(self.navodilaPlatno)
				self.navodilaPlatno = self.platno.create_window(310, 230, window = self.dBlackjack)
				
				#izgubili smo, torej smo izgubili trenutno stavo
				self.vsotaStave = 0
				self.platno.delete(self.creditNapisPlatno)
				self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
				self.platno.delete(self.vsotaStaveNapisPlatno)
				self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
				self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
				
				self.gumbHit.config(state = 'disabled')
				self.gumbStand.config(state = 'disabled')
				self.gumb10.config(state = 'disabled')
				self.gumb20.config(state = 'disabled')
				self.gumb50.config(state = 'disabled')
				self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
				
				if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
					
				
		self.oceniIgro()
		
	def oceniIgro(self):
		'''Metoda namenjena oceni igre, če noben ne preseže 21 oz. ga ne pogodi blackjack'''
		if self.scorePlayer > self.scoreDealer:
			#Zmaga igralec
			self.platno.delete(self.navodilaPlatno)
			self.navodilaPlatno = self.platno.create_window(310, 230, window = self.pWin)
			
			self.credit += (self.vsotaStave*2)
			
			self.vsotaStave = 0
			self.platno.delete(self.creditNapisPlatno)
			self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
			self.platno.delete(self.vsotaStaveNapisPlatno)
			self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
			self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
			if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
			
		elif self.scorePlayer == self.scoreDealer:
			#Neodloceno
			self.platno.delete(self.navodilaPlatno)
			self.navodilaPlatno = self.platno.create_window(310, 230, window = self.draw)
			
			self.credit += int(math.ceil(0.5 * self.vsotaStave))
			self.vsotaStave = 0
			self.platno.delete(self.creditNapisPlatno)
			self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
			self.platno.delete(self.vsotaStaveNapisPlatno)
			self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
			self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
			if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
		elif self.scoreDealer > self.scorePlayer and self.scoreDealer <= 21:
			#Zmaga dealer
			self.platno.delete(self.navodilaPlatno)
			self.navodilaPlatno = self.platno.create_window(310, 230, window = self.dWin)
			
			self.vsotaStave = 0
			self.platno.delete(self.creditNapisPlatno)
			self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
			
			self.platno.delete(self.vsotaStaveNapisPlatno)
			self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
			self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
			self.gumbNaprejNaPlatnu = self.platno.create_window(610, 400, window = self.gumbNaprej)
			
			if self.credit == 0:
					self.platno.delete(self.navodilaPlatno)
					self.navodilaPlatno = self.platno.create_window(270, 230, window = self.emptyBank)
					
					self.gumb10.config(state = 'disabled')
					self.gumb20.config(state = 'disabled')
					self.gumb50.config(state = 'disabled')
					self.gumbHit.config(state = 'disabled')
					self.gumbStand.config(state = 'disabled')
					
					self.platno.delete(self.gumbNaprejNaPlatnu)
			
		self.gumbHit.config(state = 'disabled')
		self.gumbStand.config(state = 'disabled')
		self.gumb10.config(state = 'disabled')
		self.gumb20.config(state = 'disabled')
		self.gumb50.config(state = 'disabled')
		
	
	def naslednjaRoka(self):
		'''Metoda se izvede ob zakljucku vsake igre. Njen glavni namen je pobrisati stvari, ki so ostale
		iz prejsnje igre iz platna, ter ponovno nastaviti nekatere spremenljivke. Npr. seznam kart mora, biti
		zopet poln, pa se premesati ga moremo. Poleg tega moramo se ponastaviti tocke igralca in 
		dealerja na 0.'''
		##Najprej pobrisemo vse kar bomo hoteli imeti na platnu na novo
		self.platno.delete(self.navodilaPlatno) #To moramo najprej, drugace bodo prekrivanja
		
		#pobrisemo dve karte ob inicializaciji
		self.platno.delete(self.prvaKartaPlayer)
		self.platno.delete(self.prvaKartaDealer)
		self.platno.delete(self.drugaKartaPlayer)
		self.platno.delete(self.drugaKartaDealer)
		
		#Ponovno nastavimo tudi tri karte, ki jih dobimo kasneje
		for i in range(0, 3):
			self.sezKartIgralec[i] = ''
			self.sezKartDealer[i] = ''
			self.sezKartIgralecPlatno[i] = ''
			self.sezKartDealerPlatno[i] = ''
		##
		
		##Ponastavimo spremenljivke
		self.sezKart = ['karte/1.gif', 'karte/2.gif', 'karte/3.gif', 'karte/4.gif', 'karte/5.gif',
		'karte/6.gif', 'karte/7.gif', 'karte/8.gif', 'karte/9.gif', 'karte/10.gif',
		'karte/11.gif', 'karte/12.gif', 'karte/13.gif', 'karte/4.gif', 'karte/15.gif',
		'karte/16.gif', 'karte/17.gif', 'karte/18.gif', 'karte/19.gif', 'karte/20.gif',
		'karte/21.gif', 'karte/22.gif', 'karte/23.gif', 'karte/24.gif', 'karte/25.gif',
		'karte/26.gif', 'karte/27.gif', 'karte/28.gif', 'karte/29.gif', 'karte/30.gif',
		'karte/31.gif', 'karte/32.gif', 'karte/33.gif', 'karte/34.gif', 'karte/35.gif',
		'karte/36.gif', 'karte/37.gif', 'karte/38.gif', 'karte/39.gif', 'karte/40.gif',
		'karte/41.gif', 'karte/42.gif', 'karte/43.gif', 'karte/44.gif', 'karte/45.gif',
		'karte/46.gif', 'karte/47.gif', 'karte/48.gif', 'karte/49.gif', 'karte/50.gif',
		'karte/51.gif', 'karte/52.gif']
		
		self.scorePlayer = 0
		self.scoreDealer = 0
		self.pX = 260
		self.dX = 260
		self.indexIgralceveKarte = 0
		self.indexDealerjeveKarte = 0
		##
		##Ponovno inicializiramo igro
		random.shuffle(self.sezKart)#premesamo kup kart
		
		##Najprej inicializiramo igralca
		self.prvaKartaPlayer = self.sezKart.pop() #izberemo prvo karto igralcu
		self.scorePlayer += self.vrednostKarte(self.prvaKartaPlayer) # dolocimo vrednost prve karte
		self.prvaKartaPlayer = tkinter.PhotoImage(file = self.prvaKartaPlayer) #Playing with fire
		self.prvaKartaPlayerNaPlatnu = self.platno.create_image(60, 350, image = self.prvaKartaPlayer)
		
		self.drugaKartaPlayer = self.sezKart.pop() #izberemo drugo karto igralcu
		self.scorePlayer += self.vrednostKarte(self.drugaKartaPlayer) # dolocimo vrednost druge karte
		self.drugaKartaPlayer = tkinter.PhotoImage(file = self.drugaKartaPlayer) #Playing with fire
		self.drugaKartaPlayerNaPlatnu = self.platno.create_image(160, 350, image = self.drugaKartaPlayer)
		##
		
		##Potem inicializiramo dealerja
		self.prvaKartaDealer = self.sezKart.pop() #izberemo prvo karto dealerju
		self.scoreDealer += self.vrednostKarte(self.prvaKartaDealer) # dolocimo vrednost prve karte
		self.prvaKartaDealer = tkinter.PhotoImage(file = self.prvaKartaDealer) #Playing with fire
		self.prvaKartaDealerNaPlatnu = self.platno.create_image(60, 120, image = self.prvaKartaDealer)
		
		self.drugaKartaDealer = self.sezKart.pop() #izberemo drugo karto dealerju
		self.scoreDealer += self.vrednostKarte(self.drugaKartaDealer) # dolocimo vrednost druge karte
		self.drugaKartaDealer = tkinter.PhotoImage(file = self.drugaKartaDealer) #Playing with fire
		self.drugaKartaDealerNaPlatnu = self.platno.create_image(160, 120, image = self.drugaKartaDealer)
		
		#Po pravilih je druga karta dealerja zakrita
		self.zakritaKarta = tkinter.PhotoImage(file = 'karte/back.gif')
		self.zakritaKartaNaPlatnu = self.platno.create_image(160, 120, image = self.zakritaKarta)
		##
		
		#Na platno postavimo navodila, kaj naj igralec stori
		self.navodilaPlatno = self.platno.create_window(270, 230, window = self.placeBet)
		
		
		#Ponastavimo se gumbe
		self.gumbHit.config(state = 'disabled')
		self.gumbStand.config(state = 'disabled')
		
		self.gumb10.config(state = 'normal')
		self.gumb20.config(state = 'normal')
		self.gumb50.config(state = 'normal')
		
		self.platno.delete(self.gumbNaprejNaPlatnu)
	
	def newGame(self):
		'''Metoda se uporablja, ko igralec ostane brez denarja. Lahko pa se kliče
		za svež začetek'''
		
		self.credit = 1000
		self.platno.delete(self.creditNapisPlatno)
		self.creditNapis = tkinter.Label(text = '$'+str(self.credit), bg = 'green', font = ('Helvetica', 27, 'bold'))
		self.creditNapisPlatno = self.platno.create_window(610, 90, window = self.creditNapis)
		
		self.vsotaStave = 0
		self.platno.delete(self.vsotaStaveNapisPlatno)
		self.vsotaStaveNapis = tkinter.Label(text = '$'+str(self.vsotaStave), bg = 'green', font = ('Helvetica', 27, 'bold'))
		self.vsotaStaveNapisPlatno = self.platno.create_window(610, 285, window = self.vsotaStaveNapis)
		
		self.naslednjaRoka()
	

if __name__ == '__main__':
	root = tkinter.Tk()
	root.title('Blackjack')
	
	app = Blackjack(root)
	root.mainloop()
