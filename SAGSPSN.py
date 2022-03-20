from tkinter import*
from fractions import Fraction
import webbrowser

def calculo():
	m=tkvarpM.get()
	r=tkvarpR.get()
	#validado o raio
	if r == "1/4":
		r=0.25
	elif r == "1/2":
		r=0.5
	elif r == "1" or r=="2" or r=="3" or r=="4":
		r=int(r)
	else:
		r=1

	if m == "1/4":
		m=0.25
	elif m == "1/2":
		m=0.5
	else:
		m=int(m)
		
	g=m/(r**2)
	
	if 1/36==g:
		g="1/36"
	
	elif 1/18==g:
		g="1/18"
	
	elif 1/9==g:
		g="1/9"
	
	elif 2/9==g:
		g="2/9"
	
	elif 1/3==g:
		g="1/3"
	
	elif 4/9==g:
		g="4/9"
	
	else:
		g=str(Fraction(g))
	
	Respeso["text"]=g
	Resgravidade["text"]=g
	
def validarPlaneta(value):
	T=tkvarpR.get()
	 
	global Planeta
	apagarResultado(value)
	canvas.delete(Planeta)
	
	if T=="1/4":
		Planeta=canvas.create_image(390,350, image=imagPlaneta1)

	elif T=="1/2":
		Planeta=canvas.create_image(390,350, image=imagPlaneta2)

	elif T=="1":
		Planeta=canvas.create_image(390,350, image=imagPlaneta3)

	elif T=="2":
		Planeta=canvas.create_image(390,350, image=imagPlaneta4)
	
	elif T=="3":
		Planeta=canvas.create_image(390,350, image=imagPlaneta5)
	
	else:
		Planeta.set(390,350, image=imagPlaneta6)
		
		
def apagarResultado (value):
	Respeso["text"]="?"
	Resgravidade["text"]="?"

	
def mostrarCreditos():
	canvasCred = Canvas(janela,  bd=0, highlightthickness=0, width=1370, height=710)
	canvasCred.place(rely=0, relx=0,relwidth=1, relheight=1)
	Creditos= canvasCred.create_image(685,350, image=ImagCred)
	voltar=Button(janela, text="VOLTAR>", font="Arial",bd=0,bg="red",command=lambda:[canvasCred.destroy(), voltar.destroy()])
	voltar.place(rely=0.955, relx=0.937, relwidth=0.06, relheight=0.04)
	
janela=Tk()
janela.title("Simulador de Aceleração Gravitacional na Superfície de Planetas ou Satélites Naturais")
janela.iconbitmap('imagem\icone.ico')
janela.geometry("1366x700")
janela.state("zoomed")
 
canvas = Canvas(janela,  bd=0, highlightthickness=0, width=1370, height=710)
canvas.place(rely=0, relx=0,relwidth=1, relheight=1)

imag=PhotoImage(file="fundo.png")
fundo = canvas.create_image(685,350, image=imag)
imagPlaneta1=PhotoImage(file="imagem\planeta1.png")
imagPlaneta2=PhotoImage(file="imagem\planeta2.png")
imagPlaneta3=PhotoImage(file="imagem\planeta3.png")
imagPlaneta4=PhotoImage(file="imagem\planeta4.png")
imagPlaneta5=PhotoImage(file="imagem\planeta5.png")
imagPlaneta6=PhotoImage(file="imagem\planeta6.png")
ImagIFRS=PhotoImage(file="imagem\IFRS.png")
ImagCred=PhotoImage(file="imagem\Créditos.png")
Planeta=canvas.create_image(390,350, image=imagPlaneta3)

preencherM=["1/4", "1/2", "1", "2", "3", "4"]
preencherR=["1/4", "1/2", "1", "2", "3", "4"]

tkvarpM=StringVar(janela)
tkvarpM.set(preencherM[2])

tkvarpR=StringVar(janela)
tkvarpR.set(preencherR[2])

OMMassa=OptionMenu(janela, tkvarpM,*preencherM, command=apagarResultado)
OMMassa.config(font="Arial20")
OMMassa.place(rely=0.44, relx=0.654,relwidth=0.111, relheight=0.05)

OMRaio=OptionMenu(janela, tkvarpR,*preencherR, command=validarPlaneta)
OMRaio.place(rely=0.512, relx=0.654,relwidth=0.111, relheight=0.05)
OMRaio.config(font="Arial20")

calcular=Button(janela, text="CALCULAR", font="Arial20", command=calculo).place(rely=0.585, relx=0.654,relwidth=0.275, relheight=0.05)
Creduitos=Button(janela, text="CRÉDITOS", font="Arial",bd=0,bg="#0D2FA8",command=mostrarCreditos).place(rely=0.955, relx=0.937, relwidth=0.06, relheight=0.04)
BotãoIF=Button(janela, bd=0, imag=ImagIFRS, command=lambda:webbrowser.open('https://ifrs.edu.br/rolante/')).place(rely=0.004, relx=0.9153, relwidth=0.083, relheight=0.245)

Resgravidade=Label(janela, text="?", font="Arial20", bd=1, relief="solid")
Resgravidade.place(rely=0.658, relx=0.654,relwidth=0.111, relheight=0.049)

Respeso=Label(janela, text="?", font="Arial20", bd=1, relief="solid")
Respeso.place(rely=0.729, relx=0.654,relwidth=0.111, relheight=0.049)


label1=Label(janela, text="X MASSA DA TERRA",font="Arial20", bd=1, relief="solid").place(rely=0.44, relx=0.774,relwidth=0.155, relheight=0.049)

label1=Label(janela, text="X RAIO DA TERRA",font="Arial20", bd=1, relief="solid").place(rely=0.512, relx=0.774,relwidth=0.155, relheight=0.049)

label3=Label(janela, text="X ACELERAÇÃO NA TERRA",font="Arial20", bd=1, relief="solid").place(rely=0.658, relx=0.774,relwidth=0.155, relheight=0.049)

label4=Label(janela, text="X PESO NA TERRA",font="Arial20", bd=1, relief="solid" ).place(rely=0.729, relx=0.774,relwidth=0.155, relheight=0.049)

janela.mainloop()
