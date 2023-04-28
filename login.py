from graphics import *
import time

root = GraphWin("Enter Credentials",350,200)
root.setBackground(color_rgb(206,237,244))

# fails checker
fails = 0
exits = 0
# function for passwd
login = [('admin','password'),('host','abcd')]

def check():
    global fails
    global allow_entry
    global exits
    
    if fails >= 2:
        if fails < 3 and (e1,e2) in login:
            ac_bg = Rectangle(Point(120,30),Point(230,10))
            ac_bg.setFill('ivory')
            ac_bg.setWidth(0)
            ac_bg.draw(root)
            
            access = Text(Point(175,20),"ACCESS GRANTED")
            access.setFace("Franklin Gothic Demi Cond")
            access.setSize(11)
            access.setTextColor(color_rgb(102,206,110))
            access.draw(root)
            time.sleep(0.8)
            access.undraw()
            ac_bg.undraw()
            
            allow_entry = 'yes'
            exits = 1
            
        else:
            fails += 1
            
            ac_bg = Rectangle(Point(120,30),Point(230,10))
            ac_bg.setFill('ivory')
            ac_bg.setWidth(0)
            ac_bg.draw(root)
            
            access = Text(Point(175,20),"INVALID ID")
            access.setFace("Franklin Gothic Demi Cond")
            access.setSize(11)
            access.setTextColor('red')
            access.draw(root)
            time.sleep(0.8)
            access.undraw()
            ac_bg.undraw()

            username_entry.undraw()
            username_entry.setText('')
            username_entry.draw(root)

            passw_entry.undraw()
            passw_entry.setText('')
            passw_entry.draw(root)

        exits = 1
    else:
        
        if fails < 3 and (e1,e2) in login:
            ac_bg = Rectangle(Point(120,30),Point(230,10))
            ac_bg.setFill('ivory')
            ac_bg.setWidth(0)
            ac_bg.draw(root)
            
            access = Text(Point(175,20),"ACCESS GRANTED")
            access.setFace("Franklin Gothic Demi Cond")
            access.setSize(11)
            access.setTextColor(color_rgb(102,206,110))
            access.draw(root)
            time.sleep(0.8)
            access.undraw()
            ac_bg.undraw()
            
            allow_entry = 'yes'
            exits = 1
            
        else:
            fails += 1
            
            ac_bg = Rectangle(Point(120,30),Point(230,10))
            ac_bg.setFill('ivory')
            ac_bg.setWidth(0)
            ac_bg.draw(root)
            
            access = Text(Point(175,20),"INVALID ID")
            access.setFace("Franklin Gothic Demi Cond")
            access.setSize(11)
            access.setTextColor('red')
            access.draw(root)
            time.sleep(0.8)
            access.undraw()
            ac_bg.undraw()

            username_entry.undraw()
            username_entry.setText('')
            username_entry.draw(root)

            passw_entry.undraw()
            passw_entry.setText('')
            passw_entry.draw(root)
            

    
username = Text(Point(115,40),"Username")
username.setFace("PT Sans Narrow")
username.setSize(12)
username.draw(root)

username_entry = Entry(Point(175,60),20)
username_entry.setFace("Product Sans Light")
username_entry.setSize(11)
username_entry.setFill('ivory')
username_entry.setBorderWidth(0)
username_entry.setCursor('dot')
username_entry.draw(root)

passw = Text(Point(115, 110),"Password")
passw.setFace("PT Sans Narrow")
passw.setSize(12)
passw.draw(root)

passw_entry = Entry(Point(175,130),20)
passw_entry.setFace("Product Sans Light")
passw_entry.setSize(11)
passw_entry.setFill('ivory')
passw_entry.setBorderWidth(0)
passw_entry.setCursor('dot')
passw_entry.show('*')
passw_entry.draw(root)

enter_button = Rectangle(Point(145,158),Point(205,192))
enter_button.setWidth(0)
enter_button.setFill(color_rgb(47,180,213))
enter_button.draw(root)

enter_text = Text(Point(175,175),"ENTER")
enter_text.setFace("Product Sans Medium")
enter_text.setSize(12)
enter_text.setTextColor('ivory')
enter_text.draw(root)


while True:
    allowance = root.getMouse()
    
    if 145 <= allowance.getX() <= 205 and 158 <= allowance.getY() <= 192:
        e1 = username_entry.getText()
        e2 = passw_entry.getText()

        enter_button = Rectangle(Point(145,158),Point(205,192))
        enter_button.setWidth(2)
        enter_button.setOutline(color_rgb(47,180,213))
        enter_button.setFill('ivory')
        enter_button.draw(root)

        enter_text = Text(Point(175,175),"ENTER")
        enter_text.setFace("Product Sans Medium")
        enter_text.setSize(12)
        enter_text.setTextColor(color_rgb(47,180,213))
        enter_text.draw(root)

        time.sleep(0.1)
        enter_button.undraw()
        enter_text.undraw()
        time.sleep(0.2)

        check()

    if exits == 1:
        break
    else:
        pass
    
if exits == 1:
    root.close()
else:
    pass
    
