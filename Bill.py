from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1350x700+0+0")
		self.root.title("Billing Application")
		bg_color="cadet blue"
		title=Label(self.root,text="Billing Application",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",30,"bold"),pady=5).pack(fill=X)


		#++++++++++++++++++++++++++++++++++++variables dec area+++++++++++++++++++++++#
		#+++++++++++++++cosmectics++++++++++++
		self.soap=IntVar()
		self.fc=IntVar()
		self.fw=IntVar()
		self.spray=IntVar()
		self.gell=IntVar()
		self.comb=IntVar()

		#+++++++++++++++++++gosery+++++++++++++++
		self.milk=IntVar()
		self.cheese=IntVar()
		self.paneer=IntVar()
		self.tea=IntVar()
		self.coffe=IntVar()
		self.chips=IntVar()


		#++++++++++++++++++bevrages++++++++++++++++++

		self.coca=IntVar()
		self.Thumbs=IntVar()
		self.redb=IntVar()
		self.mons=IntVar()
		self.chass=IntVar()
		self.mazza=IntVar()

		#+++++++++++++++++++++++++++++product price++++++++++++++++++++++++

		self.cos_price=StringVar()
		self.gro_price=StringVar()
		self.cold_price=StringVar()

		self.cos_tax=StringVar()
		self.gro_tax=StringVar()
		self.cold_tax=StringVar()

		#+++++++++++++++++++++++++++++++Customer++++++++++++++++++++++++
		self.c_name=StringVar()
		self.c_phno=StringVar()

		self.bill_no=StringVar()
		x=random.randint(1000,9999)
		self.bill_no.set(str(x))
		self.search_bill=StringVar()
















		#+++++++++++++++++++++++++++++++++Customer Detail Frame+++++++++++++++++#

		f1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		f1.place(x=8,y=80,relwidth=1)	

		c_name_lbl=Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
		cname_txt=Entry(f1,width=15,bd=7,textvariable=self.c_name,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=0,column=1,pady=5,padx=10)

		c_phn_lbl=Label(f1,text="Phone No",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
		cphn_txt=Entry(f1,width=15,bd=7,textvariable=self.c_phno,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=0,column=3,pady=5,padx=10)

		c_bill_lbl=Label(f1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
		cbill_txt=Entry(f1,width=15,bd=7,textvariable=self.search_bill,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=0,column=5,pady=5,padx=10)

		
		bill_btn=Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font=("times new roman",18,"bold")).grid(row=0,column=6,padx=10,pady=10)


		#++++++++++++++++++++++++++++++++++++ITEM1++++++++++++++++++++++++++++#

		f2=LabelFrame(self.root,text="Cosemtics",bd=15,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		f2.place(x=5,y=180,width=350,height=380)


		bath_lbl=Label(f2,text="Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		bath_txt=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		face_lbl=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		face_txt=Entry(f2,width=10,textvariable=self.fc,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		facew_lbl=Label(f2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		facew_txt=Entry(f2,width=10,textvariable=self.fw,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		hairs_lbl=Label(f2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		hairs_txt=Entry(f2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		hairg_lbl=Label(f2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
		hairg_txt=Entry(f2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

		comb_lbl=Label(f2,text="Comb",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
		comb_txt=Entry(f2,width=10,textvariable=self.comb,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


		#+++++++++++++++++++++++++++++++++++ITEM2++++++++++++++++++++++++++++++++#

		f3=LabelFrame(self.root,text="Grosery",bd=15,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		f3.place(x=360,y=180,width=350,height=380)


		g1_lbl=Label(f3,text="Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		g1_txt=Entry(f3,width=10,textvariable=self.milk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		g2_lbl=Label(f3,text="Cheese",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		g2_txt=Entry(f3,width=10,textvariable=self.cheese,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		g3_lbl=Label(f3,text="Paneer",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		g3_txt=Entry(f3,width=10,textvariable=self.paneer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		g4_lbl=Label(f3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		g4_txt=Entry(f3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		g5_lbl=Label(f3,text="Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
		g5_txt=Entry(f3,width=10,textvariable=self.coffe,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

		g6_lbl=Label(f3,text="Chips",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
		g6_txt=Entry(f3,width=10,textvariable=self.chips,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


		#++++++++++++++++++++++++++++++++++++++ITEM3+++++++++++++++++++++++++++++++++#

		f4=LabelFrame(self.root,text="Bevrages",bd=15,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		f4.place(x=690,y=180,width=350,height=380)


		b1_lbl=Label(f4,text="CocaCola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		b1_txt=Entry(f4,width=10,textvariable=self.coca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		b2_lbl=Label(f4,text="Mazza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		b2_txt=Entry(f4,width=10,textvariable=self.mazza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		b3_lbl=Label(f4,text="ThumbsUP",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		b3_txt=Entry(f4,width=10,textvariable=self.Thumbs,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		b4_lbl=Label(f4,text="RedBull",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		b4_txt=Entry(f4,width=10,textvariable=self.redb,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		b5_lbl=Label(f4,text="Monster",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
		b5_txt=Entry(f4,width=10,textvariable=self.mons,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

		b6_lbl=Label(f4,text="Chass",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
		b6_txt=Entry(f4,width=10,textvariable=self.chass,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


		#+++++++++++++++++++++++++++++++++++++++++++BILL AREA+++++++++++++++++++++++++++++++#		

		f5=Frame(self.root,bd=10,relief=GROOVE)
		f5.place(x=1010,y=180,width=350,height=380)

		bill_title=Label(f5,text="Bill Area",font=("times new roman",16,"bold"),bd=7,relief=GROOVE).pack(fill=X)
		scroll_y=Scrollbar(f5,orient=VERTICAL)
		self.txtarea=Text(f5,yscrollcommand=scroll_y.set)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_y.config(command=self.txtarea.yview)
		self.txtarea.pack()



		#+++++++++++++++++++++++++++++++++++++++++++++MENU BUTTONS+++++++++++++++++++++++++++#


		f6=LabelFrame(self.root,text="Bill Menu",bd=15,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		f6.place(x=0,y=560,relwidth=1,height=140)


		m1_lbl=Label(f6,text="Total Cosemtics Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
		m1_txt=Entry(f6,width=18,textvariable=self.cos_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

		m2_lbl=Label(f6,text="Total Grosery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
		m2_txt=Entry(f6,width=18,textvariable=self.gro_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

		m3_lbl=Label(f6,text="Total Bevrages Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
		m3_txt=Entry(f6,width=18,textvariable=self.cold_price,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

		c1_lbl=Label(f6,text="Cosemtics Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
		c1_txt=Entry(f6,width=18,textvariable=self.cos_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

		c2_lbl=Label(f6,text="Grosery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
		c2_txt=Entry(f6,width=18,textvariable=self.gro_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

		c3_lbl=Label(f6,text="Bevrages Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
		c3_txt=Entry(f6,width=18,textvariable=self.cold_tax,font=("times new roman",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


		btn_F=Frame(f6,bd=7,relief=GROOVE)
		btn_F.place(x=750,width=580,height=105)

		

		total_btn=Button(btn_F,command=self.totall,text="Total",bg="cadetblue",bd=2,fg="white",pady=15,width=10,font=("times new roman",15,"bold"))
		total_btn.grid(row=0,column=0,padx=5,pady=5)

		GBill_btn=Button(btn_F,text="Generate BIll",command=self.bill_area,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font=("times new roman",15,"bold")).grid(row=0,column=1,padx=5,pady=5)

		Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=5,pady=5)

		Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font=("times new roman",15,"bold")).grid(row=0,column=3,padx=5,pady=5)
		self.welcome_bill()


	def totall(self):

		self.csp=self.soap.get()*40
		self.cfc=self.fc.get()*60
		self.cfw=self.fw.get()*70
		self.spr=self.spray.get()*200
		self.gel=self.gell.get()*20
		self.cm=self.comb.get()*10
		self.total_cos_price=float(self.csp+
								self.cfc+
								self.cfw+
								self.spr+
								self.gel+
								self.cm

								)
		self.cos_price.set("Rs. "+str(self.total_cos_price))

		self.c_tax=round((self.total_cos_price*0.05),2)

		self.cos_tax.set("Rs. "+str(self.c_tax))

		self.gr1=self.milk.get()*40
		self.gr2=self.cheese.get()*60
		self.gr3=self.paneer.get()*45
		self.gr4=self.tea.get()*200
		self.gr5=self.coffe.get()*100
		self.gr6=self.chips.get()*10
	
		self.total_gro_price=float(self.gr1+
								self.gr2+
								self.gr3+
								self.gr4+
								self.gr5+
								self.gr6

								)
		self.gro_price.set("Rs. "+str(self.total_gro_price))

		self.g_tax=round((self.total_gro_price*0.1),2)
		self.gro_tax.set("Rs. "+str(self.g_tax))


		self.br1=self.coca.get()*40
		self.br2=self.Thumbs.get()*25
		self.br3=self.redb.get()*110
		self.br4=self.mons.get()*90
		self.br5=self.chass.get()*10
		self.br6=self.mazza.get()*20


		self.total_bev_price=float(self.br1+
								self.br2+
								self.br3+
								self.br4+
								self.br5+
								self.br6

								)
		self.cold_price.set("Rs. "+str(self.total_bev_price))
		self.cold_taxx=round((self.total_bev_price*0.15),2)
		self.cold_tax.set("Rs. "+str(self.cold_taxx))

		self.Total_bill=float(self.total_cos_price + self.total_gro_price +
		 						self.total_bev_price + self.c_tax + self.g_tax
		 						+ self.cold_taxx )


	def welcome_bill(self):
		self.txtarea.delete('1.0',END)
		self.txtarea.insert(END,"\t Welcome XYZ BILLING")
		self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
		self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
		self.txtarea.insert(END,f"\n Phone Number : {self.c_phno.get()}")
		self.txtarea.insert(END,"\n======================================")
		self.txtarea.insert(END,"\n Products \t\t QNTY \t\t Price")
		self.txtarea.insert(END,"\n======================================")
	def bill_area(self):
		if self.c_name.get()=="" or self.c_phno.get()=="":
			messagebox.showerror("Error","Customer details are must")
		elif self.cos_price.get()=="Rs. 0.0" and self.gro_price.get()=="Rs. 0.0" and self.cold_price.get()=="Rs. 0.0":
			messagebox.showerror("Error","No Products are selected")

		else:
			self.welcome_bill()
			#+++++++++++++++++COSMETICS+++++++++++++++++++++++++++++++#
			if self.soap.get()!=0:
				self.txtarea.insert(END,f"\n Bath Soap \t\t {self.soap.get()} \t\t {self.csp}")

			if self.fc.get()!=0:
				self.txtarea.insert(END,f"\n Face Cream \t\t {self.fc.get()} \t\t {self.cfc}")

			if self.fw.get()!=0:
				self.txtarea.insert(END,f"\n Face Wash \t\t {self.fw.get()} \t\t {self.cfw}")

			if self.spray.get()!=0:
				self.txtarea.insert(END,f"\n Spray \t\t {self.spray.get()} \t\t {self.spr}")

			if self.gell.get()!=0:
				self.txtarea.insert(END,f"\n Hair Gell \t\t {self.gell.get()} \t\t {self.gel}")

			if self.comb.get()!=0:
				self.txtarea.insert(END,f"\n Comb \t\t {self.comb.get()} \t\t {self.cm}")

			if self.milk.get()!=0:
				self.txtarea.insert(END,f"\n Milk \t\t {self.milk.get()} \t\t {self.gr1}")

			if self.cheese.get()!=0:
				self.txtarea.insert(END,f"\n Cheese \t\t {self.cheese.get()} \t\t {self.gr2}")

			if self.paneer.get()!=0:
				self.txtarea.insert(END,f"\n Paneer \t\t {self.paneer.get()} \t\t {self.gr3}")

			if self.tea.get()!=0:
				self.txtarea.insert(END,f"\n TEA \t\t {self.tea.get()} \t\t {self.gr4}")

			if self.coffe.get()!=0:
				self.txtarea.insert(END,f"\n Coffee \t\t {self.coffe.get()} \t\t {self.gr5}")

			if self.chips.get()!=0:
				self.txtarea.insert(END,f"\n Chips \t\t {self.chips.get()} \t\t {self.gr6}")

			if self.coca.get()!=0:
				self.txtarea.insert(END,f"\n CocaCola \t\t {self.coca.get()} \t\t {self.br1}")

			if self.Thumbs.get()!=0:
				self.txtarea.insert(END,f"\n ThumbsUP \t\t {self.Thumbs.get()} \t\t {self.br2}")

			if self.redb.get()!=0:
				self.txtarea.insert(END,f"\n RedBull \t\t {self.redb.get()} \t\t {self.br3}")
			if self.mons.get()!=0:
				self.txtarea.insert(END,f"\n Monster \t\t {self.mons.get()} \t\t {self.br4}")
			if self.chass.get()!=0:
				self.txtarea.insert(END,f"\n Chass \t\t {self.chass.get()} \t\t {self.br5}")
			if self.mazza.get()!=0:
				self.txtarea.insert(END,f"\n Mazza \t\t {self.mazza.get()} \t\t {self.br6}")



			self.txtarea.insert(END,"\n* * * * * * * * * * * * * * * * * * * ")

			if self.cos_tax.get()!="Rs. 0.0":

				self.txtarea.insert(END,f"\n Cosemtics Tax \t\t\t {self.cos_tax.get()}")
			
			if self.gro_tax.get()!="Rs. 0.0":

				self.txtarea.insert(END,f"\n Grosery Tax \t\t\t {self.gro_tax.get()}")
			
			if self.cold_tax.get()!="Rs. 0.0":

				self.txtarea.insert(END,f"\n Bevrages Tax \t\t\t {self.cold_tax.get()}")

			self.txtarea.insert(END,f"\n Total Bill \t\t\t Rs. {self.Total_bill}")
			self.txtarea.insert(END,"\n* * * * * * * * * * * * * * * * * * *  ")
			self.save_bill()




	def save_bill(self):
		op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
		if op>0:

			self.bill_data=self.txtarea.get('1.0',END)
			f1=open("cbill/"+str(self.bill_no.get())+ ".txt","w")
			f1.write(self.bill_data)
			f1.close()
			messagebox.showinfo("Saved",f"Bill no. {self.bill_no.get()} Saved Sucessfully")
		else:
			return
	def find_bill(self):
		present="no"
		for i in os.listdir("cbill/"):
			if i.split('.')[0]==self.search_bill.get():
				f1=open(f"cbill/{i}","r")
				self.txtarea.delete('1.0',END)
				for d in f1:
					self.txtarea.insert(END,d)
				f1.close()
				present="yes"

		if present=="no":
			messagebox.showerror("Invalid","Invalid Bill No")

	def clear_data(self):
		op=messagebox.askyesno("CLear","Do you want to clear data?")
		if op>0:
		
			self.soap.set(0)
			self.fc.set(0)
			self.fw.set(0)
			self.spray.set(0)
			self.gell.set(0)
			self.comb.set(0)

			#+++++++++++++++++++gosery+++++++++++++++
			self.milk.set(0)
			self.cheese.set(0)
			self.paneer.set(0)
			self.tea.set(0)
			self.coffe.set(0)
			self.chips.set(0)


			#++++++++++++++++++bevrages++++++++++++++++++

			self.coca.set(0)
			self.Thumbs.set(0)
			self.redb.set(0)
			self.mons.set(0)
			self.chass.set(0)
			self.mazza.set(0)

			#+++++++++++++++++++++++++++++product price++++++++++++++++++++++++

			self.cos_price.set("")
			self.gro_price.set("")
			self.cold_price.set("")

			self.cos_tax.set("")
			self.gro_tax.set("")
			self.cold_tax.set("")

			#+++++++++++++++++++++++++++++++Customer++++++++++++++++++++++++
			self.c_name.set("")
			self.c_phno.set("")

			self.bill_no.set("")
			x=random.randint(1000,9999)
			self.bill_no.set(str(x))
			self.search_bill.set("")
			self.welcome_bill()

	def Exit_app(self):
		op=messagebox.askyesno("Exit","Do you want to exit?")
		if op>0:
			self.root.destroy()






root=Tk()
obj=Bill_App(root)
root.mainloop()