import tkinter
import autoboot




window=tkinter.Tk()

window.title("YUN DAE HEE")
window.geometry("640x500+100+100")
window.resizable(False, False)

#종료
def close():
    window.quit()
    window.destroy()

#크롬매크로시작

def startChrome():
    global USER_ID
    global USER_PWD
    USER_ID = etry_userid.get()
    USER_PWD = etry_pwd.get()

    autoboot.countUP2()

lb_userid = tkinter.Label(window, text="아이디")
lb_pwd = tkinter.Label(window, text="비밀번호")
lb_userid.place(x=10, y=10)
lb_pwd.place(x=10, y=40)

etry_userid = tkinter.Entry(window)
etry_pwd = tkinter.Entry(window)
etry_userid.place(x=100, y=10)
etry_pwd.place(x=100, y=40)


b1=tkinter.Button(window, text="작업시작", command=startChrome)
b1.place(x=10, y=80)



window.mainloop()