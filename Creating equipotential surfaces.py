from tkinter import*
from math import *
import time

t=Tk()
t.geometry("1000x1000")
p=Canvas(t,width=1000,height=1000,bg='lightblue')
p.pack()
b=Button(text='построить', font='Times 15')
#b=Button(text='нарисуй',command=show)
b.place(x=-500,y=-300)
auto=Button(text='aвтозаполнение', font='Times 15')

stir=Button(text='oчистить', font='Times 15')
stir.place(x=905,y=-400, anchor='w')
        
global x11
global y11
x11=-10
y11=-10
global x22
global y22
x22=-10
y22=-10
global x33
global y33
x33=-10
y33=-10

counter=0

a=Entry()
a.place(x=-5,y=-25)
aa=Entry()
aa.place(x=-5,y=-55)
c=Entry()
c.place(x=-5,y=-85)   
aaa=Entry()
aaa.place(x=-5,y=-115)   
aaaa=Entry()
aaaa.place(x=-5,y=-145)   
cc=Entry()
cc.place(x=-5,y=-175)  
ama=Entry()
ama.place(x=-5,y=-205)   
amaa=Entry()
amaa.place(x=-5,y=-235)  
cm=Entry()
cm.place(x=-5,y=-265)
pl=Entry()
pl.place(x=-5,y=-295)
po=Entry()
po.place(x=-5,y=-295)


global one
global two
global three
global cveta
cveta=0


def p2():
    
#основная часть       
    global a
    global aa
    global aaa
    global aaaa
    global c
    global cc
    global cm
    global ama
    global amaa
    btn.destroy ()
    one.destroy ()
    two.destroy ()
    global b
    global pl
    global po
    three.destroy ()
    p.delete("all")
    men.place(x=880,y=600)

    k=9*(10**9)
#защита от дурака и создание полей ввода
    n=StringVar()
    a=Entry(textvariable=n)
    a.place(x=920,y=25,anchor='w')
    p.create_text(910,25,text="x1", font='Times 15') 
    for i in range (0,841,20):
            p.create_line(i,0,i, 1000, fill='white')
    for j in range(0,1000,20):
            p.create_line(0, j,840,j, fill='white')
    
    p.create_line(15,1,15, 1000, fill='black')
    p.create_line(2,1,2, 1000, fill='black')
    for i in range (3,14,):
        p.create_line(i,1,i, 1000, fill='lightpink')
    p.create_text(910,470,text="x: от 40 до 800",font='Times 15')
    p.create_text(910,490,text="y: от 20 до 600",font='Times 15')
    p.create_text(910,510,text="φ: от -10 до 10",font='Times 15')
    p.create_text(900,530,text="σ: от -5 до 5",font='Times 15')
    

    

    global counter
    counter=0
    
    def foo(e):
        global x11
        global y11
        global counter
        if e.keysym in '0123456789'  and int(n.get())<800:
            counter+=1
            
     
        else:
            a.delete (counter,END)
        #print(x11,y11)
        p.create_oval(x11-14,y11-14,x11+14,y11+14,fill='lightblue',outline='lightblue')
        p.create_line(0, (y11//20)*20,840,(y11//20)*20, fill='white')
        p.create_line((x11//20)*20,0,(x11//20)*20, 1000, fill='white')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
        
        
        x11=int(n.get())
        y11=int(l.get())

        t.update()

        x=int(n.get())
        y=int(l.get())
        p.create_oval(x-14,y-14,x+14,y+14,fill='lightpink',outline='black')
        p.create_text(x,y,text="1")
        
    a.bind('<KeyRelease>', foo)


    l=StringVar()
    aa=Entry(textvariable=l)
    aa.place(x=920,y=55,anchor='w')
    p.create_text(910,55,text="y1", font='Times 15')
    
    global counter1
    counter1=0

    def foo(e):
        global x11
        global y11
        global counter1
        if e.keysym in '0123456789' and int(l.get())<800:
            counter1+=1
        else:
            aa.delete (counter1,END)
            
        print(x11,y11)
        p.create_oval(x11-14,y11-14,x11+14,y11+14,fill='lightblue',outline='lightblue')
        p.create_line(0, (y11//20)*20,840,(y11//20)*20, fill='white')
        p.create_line((x11//20)*20,0,(x11//20)*20, 1000, fill='white')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
            
        x11=int(n.get())
        
        y11=int(l.get())
        
        t.update()
        
        x=int(n.get())
        y=int(l.get())
        p.create_oval(x-14,y-14,x+14,y+14,fill='lightpink',outline='black')
        p.create_text(x,y,text="1")
    aa.bind('<KeyRelease>', foo)
        


    r=StringVar()
    c=Entry(textvariable=r)
    c.place(x=920,y=85,anchor='w')
    p.create_text(910,85,text="q1", font='Times 15' ) 
    global counter2
    counter2=0

    def foo(e):
        global counter2
        if (e.keysym in '0123456789' or e.keysym=="minus"or e.keysym=="period" )  and int(r.get())<10:
            counter2+=1
        
        else:
            c.delete (counter2,END)
        x=int(n.get())
        y=int(l.get())
        q=int(r.get())*(10**(-9))
        if q==0:
            p.create_oval(x-14,y-14,x+14,y+14,fill='lightblue',outline='lightblue')
            p.create_line(0, (y//20)*20,840,(y//20)*20, fill='white')
            p.create_line((x//20)*20,0,(x//20)*20, 1000, fill='white')
            p.create_line(15,1,15, 1000, fill='black')
            p.create_line(2,1,2, 1000, fill='black')
            for i in range (3,14,):
                p.create_line(i,1,i, 1000, fill='lightpink')
        else:
            p.create_oval(x-14,y-14,x+14,y+14,fill='lightpink',outline='black')
            p.create_text(x,y,text="1")
        #for i in range (0,841,20):
        #    p.create_line(i,0,i, 1000, fill='white')
        #for j in range(0,1000,20):
        #    p.create_line(0, j,840,j, fill='white')
    c.bind('<KeyRelease>', foo)

    m=StringVar()
    aaa=Entry(textvariable=m)
    aaa.place(x=920,y=115,anchor='w')
    p.create_text(910,115,text="x2", font='Times 15' ) 
    global counter3
    counter3=0

    def foo(e):
        global x22
        global y22
        global counter3
        if e.keysym in '0123456789' and int(m.get())<800:
            counter3+=1
        else:
            aaa.delete (counter3,END)
        p.create_oval(x22-14,y22-14,x22+14,y22+14,fill='lightblue',outline='lightblue')
        p.create_line(0, (y22//20)*20,840,(y22//20)*20, fill='white')
        p.create_line((x22//20)*20,0,(x22//20)*20, 1000, fill='white')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
        x22=int(m.get())
        y22=int(s.get())
        t.update()       
        x1=int(m.get())
        y1=int(s.get())
        p.create_oval(x1-14,y1-14,x1+14,y1+14,fill='lightpink',outline='black')
        p.create_text(x1,y1,text="2")
    aaa.bind('<KeyRelease>', foo)

    s=StringVar()
    aaaa=Entry(textvariable=s)
    aaaa.place(x=920,y=145,anchor='w')
    p.create_text(910,145,text="y2", font='Times 15' )
    global counter4
    counter4=0

    def foo(e):
        global counter4
        global x22
        global y22
        if e.keysym in '0123456789'  and int(s.get())<600:
            counter4+=1
        else:
            aaaa.delete (counter4,END)
        p.create_oval(x22-14,y22-14,x22+14,y22+14,fill='lightblue',outline='lightblue')
        p.create_line(0, (y22//20)*20,840,(y22//20)*20, fill='white')
        p.create_line((x22//20)*20,0,(x22//20)*20, 1000, fill='white')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
        x22=int(m.get())
        y22=int(s.get())
        t.update()

        x1=int(m.get())
        y1=int(s.get())
        p.create_oval(x1-14,y1-14,x1+14,y1+14,fill='lightpink',outline='black')
        p.create_text(x1,y1,text="2")
    aaaa.bind('<KeyRelease>', foo)

    ee=StringVar()
    cc=Entry(textvariable=ee)
    cc.place(x=920,y=175,anchor='w')
    p.create_text(910,175,text="q2",font='Times 15' )
    global counter5
    counter5=0

    def foo(e):
        global counter5
        if (e.keysym in '0123456789' or e.keysym=="minus" or e.keysym=="period")   and int(ee.get())<10:
            counter5+=1
        else:
            cc.delete (counter5,END)
        x1=int(m.get())
        y1=int(s.get())
        q1=int(ee.get())*(10**(-9))
        if q1==0:
            p.create_oval(x1-14,y1-14,x1+14,y1+14,fill='lightblue',outline='lightblue')
            p.create_line(0, (y1//20)*20,840,(y1//20)*20, fill='white')
            p.create_line((x1//20)*20,0,(x1//20)*20, 1000, fill='white')
            p.create_line(15,1,15, 1000, fill='black')
            p.create_line(2,1,2, 1000, fill='black')
            for i in range (3,14,):
                p.create_line(i,1,i, 1000, fill='lightpink')
        else:
             p.create_oval(x1-14,y1-14,x1+14,y1+14,fill='lightpink',outline='black')
             p.create_text(x1,y1,text="2")

        #for i in range (0,841,20):
        #    p.create_line(i,0,i, 1000, fill='white')
        #for j in range(0,1000,20):
        #    p.create_line(0, j,840,j, fill='white')
    cc.bind('<KeyRelease>', foo)


    z=StringVar()
    ama=Entry(textvariable=z)
    ama.place(x=920,y=205,anchor='w')
    p.create_text(910,205,text="x3",font='Times 15' )
    global counter6
    counter6=0

    def foo(e):
        global x33
        global y33
        global counter6
        if e.keysym in '0123456789' and int(z.get())<800:
            counter6+=1
        else:
            ama.delete (counter6,END)
        p.create_oval(x33-14,y33-14,x33+14,y33+14,fill='lightblue',outline='lightblue')
        p.create_line(0, (y33//20)*20,840,(y33//20)*20, fill='white')
        p.create_line((x33//20)*20,0,(x33//20)*20, 1000, fill='white')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
        x33=int(z.get())
        y33=int(w.get())
        t.update()
        
        
        x2=int(z.get())
        y2=int(w.get())
        p.create_oval(x2-14,y2-14,x2+14,y2+14,fill='lightpink',outline='black')
        p.create_text(x2,y2,text="3")
    ama.bind('<KeyRelease>', foo)

    w=StringVar()
    amaa=Entry(textvariable=w)
    amaa.place(x=920,y=235,anchor='w')
    p.create_text(910,235,text="y3", font='Times 15')
    global counter7
    counter7=0

    def foo(e):
        global x33
        global y33
        global counter7
        if e.keysym in '0123456789'   and int(w.get())<600:
            counter7+=1
        else:
            amaa.delete (counter7,END)
        p.create_oval(x33-14,y33-14,x33+14,y33+14,fill='lightblue',outline='lightblue')
        p.create_line(0, (y33//20)*20,840,(y33//20)*20, fill='white')
        p.create_line((x33//20)*20,0,(x33//20)*20, 1000, fill='white')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink') 
        x33=int(z.get())
        y33=int(w.get())
        t.update()
        
        x2=int(z.get())
        y2=int(w.get())
        p.create_oval(x2-14,y2-14,x2+14,y2+14,fill='lightpink',outline='black')
        p.create_text(x2,y2,text="3")
  
    amaa.bind('<KeyRelease>', foo)

    g=StringVar()
    cm=Entry(textvariable=g)
    cm.place(x=920,y=265,anchor='w')
    p.create_text(910,265,text="q3", font='Times 15' )
    global counter8
    counter8=0

    def foo(e):
        global counter8
        if (e.keysym in '0123456789' or e.keysym=="minus" or e.keysym=="period" )  and int(g.get())<10:
            counter8+=1
        else:
            cm.delete (counter8,END)
        x2=int(z.get())
        y2=int(w.get())
        q2=int(g.get())*(10**(-9))
        if q2==0:
            p.create_oval(x2-14,y2-14,x2+14,y2+14,fill='lightblue',outline='lightblue')
            p.create_line(0, (y2//20)*20,840,(y2//20)*20, fill='white')
            p.create_line((x2//20)*20,0,(x2//20)*20, 1000, fill='white')
            p.create_line(15,1,15, 1000, fill='black')
            p.create_line(2,1,2, 1000, fill='black')
            for i in range (3,14,):
                p.create_line(i,1,i, 1000, fill='lightpink')
        else:
            p.create_oval(x2-14,y2-14,x2+14,y2+14,fill='lightpink',outline='black')
            p.create_text(x2,y2,text="3")
        

    cm.bind('<KeyRelease>', foo)

    zpl=StringVar()
    pl=Entry(textvariable=zpl)
    pl.place(x=920,y=285)
    p.create_text(910,295,text="σ" , font='Times 15' )
    global counter9
    counter9=0

    def foo(e):
        global counter9
        if (e.keysym in '0123456789' or e.keysym=="minus" or e.keysym=="period")  and float(zpl.get())<10:
            counter9+=1
        else:
            pl.delete (counter9,END)

    pl.bind('<KeyRelease>', foo)

    zpo=StringVar()
    po=Entry(textvariable=zpo)
    po.place(x=920,y=315)
    p.create_text(910,315,text="φ" , font='Times 15' )
    global counter10
    counter10=0

    def foo(e):
        global counter10
        if (e.keysym in '0123456789' or e.keysym=="minus" or e.keysym=="period")  and float(zpo.get())<10:
            counter10+=1
        else:
            po.delete (counter9,END)

    po.bind('<KeyRelease>', foo)

#нарисовать


    def show():
        global cveta
        cveta+=1
        if cveta>6:
            cveta=1
        if cveta==1:
            color1='black'
        elif cveta==2:          
            color1='red'
        elif cveta==3:          
            color1='blue'
        elif cveta==4:          
            color1='orange'
        elif cveta==5:          
            color1='purple'
        elif cveta==6:          
            color1='limegreen'
        else:       
            color1='red'
        x=int(n.get())
        y=int(l.get())
        q=int(r.get())*(10**(-9))
         #   p.create_oval(x-14,y-14,x+14,y+14,fill='lightblue',outline='lightblue')
        
        x1=int(m.get())
        y1=int(s.get())
        q1=int(ee.get())*(10**(-9))
        #p.create_oval(x1-5,y1-5,x1+5,y1+5,fill='lightpink',outline='black')
       
        x2=int(z.get())
        y2=int(w.get())
        q2=int(g.get())*(10**(-9))
        #p.create_oval(x2-5,y2-5,x2+5,y2+5,fill='lightpink',outline='black')
        
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
       
        d=float(zpo.get())
        zzpl=float(zpl.get())
        xx=17
        if d<=1 and d>=-1:
            dpogr=1/17
        else:
            dpogr=(d**2)/100
 
        
        #for i in range (0,851,10):
        #    p.create_line(i,0,i, 1000, fill='white')
        #for j in range(0,1000,10):
        #    p.create_line(0, j,850,j, fill='white')
        for i in range(20, 841,2):
            for j in range(20,640,2):
                if (i!=x or j!=y) and (i!=x1 or j!=y1) and (i!=x2 or j!=y2) and i!=xx :
                    
                    #print((k*q/(sqrt((i-x)**2+(j-y)**2)/10)+(zzpl*10/(abs(i-xx))) +k*q2/(sqrt((i-x2)**2+(j-y2)**2)/10)+k*q1/(sqrt((i-x1)**2+(j-y1)**2)/10)),(zzpl*10/(abs(i-xx))) )
                    #print (zzpl*10/(abs(i-xx)))
                    if ((zzpl*100/(i-xx)+k*q/(sqrt((i-x)**2+(j-y)**2)/10)+k*q2/(sqrt((i-x2)**2+(j-y2)**2)/10)+k*q1/(sqrt((i-x1)**2+(j-y1)**2)/10))<(d+dpogr)) and  ((zzpl*100/(i-xx)+k*q/(sqrt((i-x)**2+(j-y)**2)/10)+k*q2/(sqrt((i-x2)**2+(j-y2)**2)/10)+k*q1/(sqrt((i-x1)**2+(j-y1)**2)/10))>(d-dpogr)) :
                        p.create_oval(i,j,i+1,j+1,fill=color1,outline=color1)
                        
            t.update()
    p.create_line(0, 20,840,20, fill='black')
    p.create_line(820,0,840,20, fill='black')
    p.create_line(820,40,840,20, fill='black')
    p.create_line(20, 0,20,640, fill='black')
    p.create_line(0,620,20,640, fill='black')
    p.create_line(40, 620,20,640, fill='black')
    p.create_text(25,27,text="0", font='Times 14')
    global b
    b=Button(text='построить', font='Times 13',command=show)
    b.place(x=900,y=390,anchor='w')
#очищение поверхности


    def stiranie():
        p.delete("all")
        p.create_text(910,470,text="x: от 40 до 800",font='Times 15')
        p.create_text(910,490,text="y: от 20 до 600",font='Times 15')
        p.create_text(910,510,text="φ: от -10 до 10",font='Times 15')
        p.create_text(900,530,text="σ: от -5 до 5",font='Times 15')
    

        p.create_text(910,25,text="x1", font='Times 14')
        p.create_text(910,55,text="y1", font='Times 14')
        p.create_text(910,85,text="q1", font='Times 14' )
        p.create_text(910,115,text="x2", font='Times 14')
        p.create_text(910,145,text="y2", font='Times 14')
        p.create_text(910,175,text="q2", font='Times 14' )
        p.create_text(910,205,text="x3", font='Times 14')
        p.create_text(910,235,text="y3", font='Times 14')
        p.create_text(910,265,text="q3", font='Times 14' )
        p.create_text(910,315,text="φ" , font='Times 15' )
        p.create_text(910,295,text="σ" , font='Times 15' )
        for i in range (0,841,20):
            p.create_line(i,0,i, 1000, fill='white')
        for j in range(0,1000,20):
            p.create_line(0, j,840,j, fill='white')
        #p.create_line(0, 20,840,20, fill='black')
        #p.create_line(20, 0,20,1000, fill='black')
        #p.create_text(25,27,text="0", font='Times 14')
        x=int(n.get())
        y=int(l.get())
        x2=int(z.get())
        y2=int(w.get())
        x1=int(m.get())
        y1=int(s.get())
        p.create_oval(x2-14,y2-14,x2+14,y2+14,fill='lightpink',outline='black')
        p.create_text(x2,y2,text="3")
        p.create_oval(x1-14,y1-14,x1+14,y1+14,fill='lightpink',outline='black')
        p.create_text(x1,y1,text="2")
        p.create_oval(x-14,y-14,x+14,y+14,fill='lightpink',outline='black')
        p.create_text(x,y,text="1")
        p.create_line(0, 20,840,20, fill='black')
        p.create_line(820,0,840,20, fill='black')
        p.create_line(820,40,840,20, fill='black')
        p.create_line(20, 0,20,640, fill='black')
        p.create_line(0,620,20,640, fill='black')
        p.create_line(40, 620,20,640, fill='black')
        p.create_text(25,27,text="0", font='Times 14')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        for i in range (3,14,):
            p.create_line(i,1,i, 1000, fill='lightpink')
       

            
    global stir
    stir=Button(text='oчистить', font='Times 13', command=stiranie)
    stir.place(x=905,y=400, anchor='w')
        

    def avtozap():
        p.delete("all")
        p.create_text(910,470,text="x: от 40 до 800",font='Times 15')
        p.create_text(910,490,text="y: от 20 до 600",font='Times 15')
        p.create_text(910,510,text="φ: от -10 до 10",font='Times 15')
        p.create_text(900,530,text="σ: от -5 до 5",font='Times 15')
    
        global a
        global aa
        global aaa
        global aaaa
        global c
        global cc
        global cm
        global ama
        global amaa
        global b
        global pl
        global po
        global x11
        global y11
        
        global x22
        global y22
        x22=220
        y22=210
        global x33
        global y33
        x33=600
        y33=400
        
        x11=300
        y11=100
        p.create_text(910,25,text="x1", font='Times 14')
        p.create_text(910,55,text="y1", font='Times 14')
        p.create_text(910,85,text="q1", font='Times 14' )
        p.create_text(910,115,text="x2", font='Times 14')
        p.create_text(910,145,text="y2", font='Times 14')
        p.create_text(910,175,text="q2", font='Times 14' )
        p.create_text(910,205,text="x3", font='Times 14')
        p.create_text(910,235,text="y3", font='Times 14')
        p.create_text(910,265,text="q3", font='Times 14' )
        p.create_text(910,315,text="φ" , font='Times 15' )
        p.create_text(910,295,text="σ" , font='Times 15' )
        
        for i in range (0,841,20):
            p.create_line(i,0,i, 1000, fill='white')
        for j in range(0,1000,20):
            p.create_line(0,j,840,j, fill='white')
        #p.create_line(0, 20,840,20, fill='black')
        #p.create_line(20, 0,20,1000, fill='black')
        #p.create_text(25,27,text="0", font='Times 14')
        
        p.create_oval(x11-14,y11-14,x11+14,y11+14,fill='lightpink',outline='black')
        p.create_oval(x33-14,y33-14,x33+14,y33+14,fill='lightpink',outline='black')
        p.create_oval(x22-14,y22-14,x22+14,y22+14,fill='lightpink',outline='black')
        p.create_line(15,1,15, 1000, fill='black')
        p.create_line(2,1,2, 1000, fill='black')
        p.create_line(0, 20,840,20, fill='black')
        p.create_line(820,0,840,20, fill='black')
        p.create_line(820,40,840,20, fill='black')
        p.create_line(20, 0,20,640, fill='black')
        p.create_line(0,620,20,640, fill='black')
        p.create_line(40, 620,20,640, fill='black')
        p.create_text(25,27,text="0", font='Times 14')
        for i in range (3,15):
            p.create_line(i,1,i, 1000, fill='lightpink')
       
        a.delete(0,10)
        aa.delete(0,10)
        c.delete(0,10)
        aaa.delete(0,10)
        aaaa.delete(0,10)
        cc.delete(0,10)
        ama.delete(0,10)
        amaa.delete(0,10)
        cm.delete(0,10)
        pl.delete(0,10)
        po.delete(0,10)
     
        a.insert(0,300)
        aa.insert(0,100)
        c.insert(0,1)
        aaa.insert(0,220)
        aaaa.insert(0,210)
        cc.insert(0,-2)
        ama.insert(0,600)
        amaa.insert(0,400)
        cm.insert(0,3)
        pl.insert(0,3.4)
        po.insert(0,2.7)
        
        p.create_text(x11,y11,text="1")
        p.create_text(x22,y22,text="2")
        p.create_text(x33,y33,text="3")
       
    
    b.place(x=905,y=360,anchor='w')
    global auto
    auto=Button(text="автозаполнение", font='Times 13', command=avtozap)
    auto.place(x=870, y=560)
    

def menu():
    global b
    global auto
    global a
    global aa
    global aaa
    global aaaa
    global c
    global cc
    global cm
    global ama
    global amaa
    global one
    global two
    global three
    global pl
    global po            
    global stir

    stir.place(x=-905,y=-5400, anchor='w')
        
    p.delete("all")
    btn.destroy ()
    men.place(x=1800,y=1200)
    auto.place(x=800,y=1600)
    one=Button(text="условие",command=p1,padx=8,pady=8, font='Times 20',background='lavenderblush' )
    
    
    one.place(x=340,y=300)
    p.create_line(303,242,303, 1000, fill='white', width=7)
    p.create_line(303,352,303, 1000, fill='white', width=7)

    p.create_line(300,246,600, 246, fill='white', width=7)
    p.create_line(603,246,603, 1000, fill='white', width=7)
    p.create_line(300,1000,600, 1000, fill='white', width=7)
    two=Button(text="демонстрация",command=p2, padx=8,pady=8, background='lavenderblush', font='Times 20')
    two.place(x=340,y=400)
    three=Button(text="помощь",command=p3, padx=8,pady=8, font='Times 20',background='lavenderblush')
    three.place(x=340,y=500)
    p.create_text(500,100, text="МЕНЮ", font='Times 47', fill='white')
    b.place(x=1500,y=1300)
    a.place(x=-5,y=-25) 
    aa.place(x=-5,y=-55)  
    c.place(x=-5,y=-85) 
    aaa.place(x=-5,y=-115)
    aaaa.place(x=-5,y=-145)
    cc.place(x=-5,y=-175)
    ama.place(x=-5,y=-205)
    amaa.place(x=-5,y=-235)  
    pl.place(x=-5,y=-290)
    cm.place(x=-5,y=-265)
    po.place(x=-5,y=-290)


    
   

def p3():
    global a
    global aa
    global aaa
    global aaaa
    global c
    global cc
    global cm
    global ama
    global amaa
    global men
    
    btn.destroy ()
    one.destroy ()
    
    a.place(x=-5,y=-25)
    aa.place(x=-5,y=-55)
    c.place(x=-5,y=-85) 
    aaa.place(x=-5,y=-115)
    aaaa.place(x=-5,y=-145)
    cc.place(x=-5,y=-175)
    ama.place(x=-5,y=-205)
    amaa.place(x=-5,y=-235)
    cm.place(x=-5,y=-265)
    global b
    b.place(x=-500,y=-300)
    two.destroy ()
    three.destroy ()
    p.delete("all")
    men.place(x=880,y=600)
    p.create_text(500,100, text="ПОМОЩЬ", font='Times 47', fill='white')
    p.create_text(450,380,text="для построения поверхностей все поля ввода должны быть заполнены",font='Times 15')
    p.create_text(450,400,text="для удаления заряда введите его величину ноль(q=0)",font='Times 15')
    p.create_text(450,360,text="для нажатия на кнопку используйте левую кнопку мыши",font='Times 15')
    p.create_text(450,420,text="x: от 40 до 800",font='Times 15')
    p.create_text(450,440,text="y: от 20 до 600",font='Times 15')
    p.create_text(450,460,text="φ: от -10 до 10",font='Times 15')
    p.create_text(450,480,text="σ: от -5 до 5",font='Times 15')
    
    

def p1():
    global b
    global a
    global aa
    global aaa
    global aaaa
    global c
    global cc
    global cm
    global ama
    global amaa
    global men
    b.place(x=-500,y=-300)
    a.place(x=-5,y=-25)
    aa.place(x=-5,y=-55)
    c.place(x=-5,y=-85)
    aaa.place(x=-5,y=-115)
    aaaa.place(x=-5,y=-145)
    cc.place(x=-5,y=-175)
    ama.place(x=-5,y=-205)
    amaa.place(x=-5,y=-235)
    cm.place(x=-5,y=-265)
    btn.destroy ()
    one.destroy ()
    two.destroy ()
    three.destroy ()
    p.delete("all")
    #men.place(x=800,y=600)
    p.create_text(500,100, text="УСЛОВИЕ", font='Times 47', fill='white')
    p.create_text(450,400,text="Составить программу, моделирующую построение эквипотенциальных \n поверхностей электростатического поля,\n создаваемого неподвижными зарядами (не более 3-х) и пластиной \n Пластина представляет собой бесконечную плоскость", font='Times 15')
    #men=Button(text="меню",command=menu)
    men.place(x=880,y=600) 
    

btn=Button(text="Запустить программу", font='Times 15',command=menu)
btn.place(x=450,y=450)
men=Button(text="меню",command=menu)
men.place(x=800,y=1200)
p.create_text(500,300, text="ЗАЧЕТНАЯ РАБОТА ПО ИНФОРМАТИКЕ", font='Times 27')
p.create_text(500,330, text="Построение эквипотенциальных поверхностей, создаваемых тремя зарядами и пластиной", font='Times 15')
p.create_text(600,600, text="Cтаткевич Катя 10Г",font='Times 15')
t.mainloop()
