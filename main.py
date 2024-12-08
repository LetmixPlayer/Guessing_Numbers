# -*- coding utf8 -*-
from random import randint
from tkinter import *
from tkinter import messagebox
from random import randint
from . import log

def setshu(big : int, small : int):
    global root, shu
    shu.set(str(small) + '~' + str(big))
    shu.set(f"请输入一个数({ shu.get() })")
    log.log("[Info|Counter] Reset text2")

def buttonclick(event = None):
    log.log("[Info|Button] Button is click")
    global a, mx, mn, l3, lab, ci
    b = l3.get()
    log.log("[Info|Entry] Input: " + l3.get())
    try:
        b = int(b)
        if (a == b):
            lab.set(f"猜对了, 共猜了{ str(ci) }次")
            ci = 0
            log.log("[Info|Comparator] The number is right")
            mx, mn = 1000, 1
            a = randint(1, 1000)
            shu.set("请输入一个数(1~1000)")
            l3.delete(0, len(l3.get()))
            return
        else:
            if (a > b):
                lab.set(f"猜小了，还剩{ 10 - ci - 1 }次!")
                ci += 1
                if (b > mn): mn = b
                log.log("[Info|Comparator] The number is small")
            if (a < b):
                lab.set(f"猜大了，还剩{ 10 - ci - 1 }次!")
                if (b < mx): mx = b
                ci += 1
                log.log("[Info|Comparator] The number is big")
    except:
        if (b != ""):
            lab.set("你在里面输入了字符!")
            log.log("[Error|Comparator] Inputed some char!")
        else:
            lab.set("你没有输入!")
            log.log("[Error|Comparator] No Input!")
    if (ci == 10):
        lab.set("对不起, 你输了")
        log.log("[Info|Fail] Reset settings")
        mx, mn = 1000, 1
        a = randint(1, 1000)
        ci = 0
    l3.delete(0, len(l3.get()))
    log.log("[Info|Entry] Deleted all input")
    setshu(mx, mn)

def labelclick(event = None):
    messagebox.showinfo("关于 猜数游戏", "By Letmix Player\nPowered by Python Tkinter")
    log.log("[Info|PaintedEggshell] Trigger about")



a = randint(1, 1000)
log.init()
mx, mn = 1000, 1
ci = 0
log.log("[Info|Count] Set max, min & times")

root = Tk(className="猜数游戏")
log.log("[Info|Init] Windows was created")
shu = StringVar(root)
shu.set("请输入一个数(1~1000)")

lab = StringVar(root)
l1 = Label(root, text='猜数游戏', width=40)
l2 = Label(root, textvariable=shu, height=2)
l3 = Entry(root)
l4 = Button(root, text='猜数', command=buttonclick)
l5 = Label(root, textvariable=lab)
l1.bind("<Button-1>", labelclick)
root.bind_all("<KeyPress-Return>", buttonclick)
log.log("[Info|Init] Model was created")
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
log.log("[Info|Init] Models was packed")
log.log("[Info|Init] Initialized all settings")
root.mainloop()

log.log("[Info|Exit] Exit")
log.clear()