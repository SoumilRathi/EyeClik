import cv2
import numpy as np
import mediapipe as mp
import time
import pyautogui
import math
from tkinter import *
import threading 
import sys
from PIL import ImageTk, Image
import subprocess

#Keyboard section'
BUTTON_BACKGROUND   = "black"
MAIN_FRAME_BACKGROUND  = "cornflowerblue"
BUTTON_LOOK    = "groove" #flat, groove, raised, ridge, solid, or sunken
TOP_BAR_TITLE    = "EyeClik KeyBoard"
TOPBAR_BACKGROUND   = "skyblue"
TRANSPARENCY    = 1
FONT_COLOR     = "blue"
pending_text = False
textToAdd = "" 
keyboard_showing = False

from pydoc import text
from tkinter import ttk

keys =[ 
[
# =========================================
# ===== Keyboard Configurations ===========
# =========================================

 [
  # Layout Name
  ("Number_Keys"),

  # Layout Frame Pack arguments
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   # list of Keys
   ('1', '2','3','4','5','6','7','8','9','0')
  ]
 ],

 [
  ("Character_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   ('`',',','.','/','-','=','\\','[',']','backspace'),
   ('~','!','@','#','$','%','^','&','*','(',')','_','+','|', '='),
   ('tab','q','w','e','r','t','y','u','i','o','p','{','}',";",'\''),
   ('capslock','a','s','d','f','g','h','j','k','l',':',"\"","enter"),
   ('z','x','c','v','b','n','m','<','>','?'),
   ('alt', 'opt', 'space', 'cntl', 'alt')
  ]
 ]
]

]

# Create key event
def create_keyboard_event(numlock, capslock, controler, key):
 return

##  Frame Class
class Keyboard(Frame):
 
 def __init__(self, *args, **kwargs):
  Frame.__init__(self, *args, **kwargs)
  
  self.caps = False
  self.alt = False
  self.cntl = False
  # Function For Creating Buttons
  self.create_frames_and_buttons()



 # Function For Extracting Data From KeyBoard Table
 # and then provide us a well looking
 # keyboard gui
 def create_frames_and_buttons(self):
  # take section one by one
  
  for key_section in keys:
   # create Sperate Frame For Every Section
   store_section = Frame(self)
   store_section.pack(side='left',expand='yes',fill='both',padx=10,pady=10,ipadx=10,ipady=10)
   
   for layer_name, layer_properties, layer_keys in key_section:
    store_layer = LabelFrame(store_section)#, text=layer_name)
    #store_layer.pack(side='top',expand='yes',fill='both')
    store_layer.pack(layer_properties)
    for key_bunch in layer_keys:
     store_key_frame = Frame(store_layer)
     store_key_frame.pack(side='top',expand='yes',fill='both')
     for k in key_bunch:
      k=k.capitalize()
      if len(k)<=3:
       store_button = Button(store_key_frame, text=k, width=2, height=2)
      else:
       store_button = Button(store_key_frame, text=k.center(5,' '), height=2)
      if " " in k:
       store_button['state']='disable'
      
      store_button['relief']=BUTTON_LOOK
      store_button['bg']=BUTTON_BACKGROUND
      store_button['fg']=FONT_COLOR

      store_button['command']=lambda q=k.lower(): self.button_command(q)
      store_button.pack(side='left',fill='both',expand='yes')
  return

  # Function For Detecting Pressed Keyword.
 def button_command(self, event):
   if(event == "enter"):
     root.destroy()
     global keyboard_showing
     keyboard_showing = False
     global pending_text
     pending_text = True
     global textToAdd
     textToAdd = text.get()
     return
   elif(event == "tab"):
     text.set(text.get() + "    ")
   elif(event == "space"):
     text.set(text.get() + " ")
   elif(event == "backspace"):
     text.set(text.get()[:-1])
   elif(event == "capslock"):
     if(self.caps == True):
       self.caps = False
     else:
       self.caps = True
   elif(event == "cntl"):
     if(self.cntl == True):
       self.cntl = False
     else:
       self.cntl = True
   elif(event == "alt"):
     if(self.alt == True):
       self.alt = False
     else:
       self.alt = True
   else:
     if(self.caps):
       text.set(text.get() + event.upper())
     else:
       text.set(text.get() + event)
   root.update()
   return
            
def keyboardManage():
    global keyboard_showing
    if(keyboard_showing == False):
        keyboard_showing = True
        width, height = pyautogui.size()
        # Creating Main Window
        global root
        root = Toplevel()
        geo = "+" + str(width//2 - 400) + "+" + str(height - 420)
        root.geometry(geo)
        global text
        text = StringVar()
        Dis_entry = ttk.Entry(root,state= 'readonly',textvariable = text)
        Dis_entry.pack(side='top',fill='both',expand='yes')
        k =Keyboard(root, bg=MAIN_FRAME_BACKGROUND)
        # Confifuration
        root.overrideredirect(True)
        root.wait_visibility(root)
        root.wm_attributes('-alpha',TRANSPARENCY)
        # Custum
        f = Frame(root)
        t_bar=Label(f, text=TOP_BAR_TITLE, bg=TOPBAR_BACKGROUND)
        t_bar.pack(side='left',expand="yes", fill="both")
        Button(f, text="[X]", command= root.destroy).pack(side='right')
        f.pack(side='top', expand='yes',fill='both')
        k.pack(side='top')
        root.mainloop()

class TkinterCustomButton(Frame):
    """ tkinter custom button with border, rounded corners and hover effect
        Arguments:  master= where to place button
                    bg_color= background color, None is standard,
                    fg_color= foreground color, blue is standard,
                    hover_color= foreground color, lightblue is standard,
                    border_color= foreground color, None is standard,
                    border_width= border thickness, 0 is standard,
                    command= callback function, None is standard,
                    width= width of button, 110 is standard,
                    height= width of button, 35 is standard,
                    corner_radius= corner radius, 10 is standard,
                    text_font= (<Name>, <Size>),
                    text_color= text color, white is standard,
                    text= text of button,
                    hover= hover effect, True is standard,
                    image= PIL.PhotoImage, standard is None"""

    def __init__(self,
                 bg_color=None,
                 fg_color="#2874A6",
                 hover_color="#5499C7",
                 border_color=None,
                 border_width=0,
                 command=None,
                 width=120,
                 height=40,
                 corner_radius=10,
                 text_font=None,
                 text_color="white",
                 text="CustomButton",
                 hover=True,
                 image=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        if bg_color is None:
            self.bg_color = self.master.cget("bg")
        else:
            self.bg_color = bg_color

        self.fg_color = fg_color
        self.hover_color = hover_color
        self.border_color = border_color

        self.width = width
        self.height = height

        if corner_radius*2 > self.height:
            self.corner_radius = self.height/2
        elif corner_radius*2 > self.width:
            self.corner_radius = self.width/2
        else:
            self.corner_radius = corner_radius

        self.border_width = border_width

        if self.corner_radius >= self.border_width:
            self.inner_corner_radius = self.corner_radius - self.border_width
        else:
            self.inner_corner_radius = 0

        self.text = text
        self.text_color = text_color
        if text_font is None:
            if sys.platform == "darwin":  # macOS
                self.text_font = ("Avenir", 13)
            elif "win" in sys.platform:  # Windows
                self.text_font = ("Century Gothic", 11)
            else:
                self.text_font = ("TkDefaultFont")
        else:
            self.text_font = text_font

        self.image = image

        self.function = command
        self.hover = hover

        self.configure(width=self.width, height=self.height)

        if sys.platform == "darwin" and self.function is not None:
            self.configure(cursor="pointinghand")

        self.canvas = Canvas(master=self,
                                     highlightthicknes=0,
                                     background=self.bg_color,
                                     width=self.width,
                                     height=self.height)
        self.canvas.place(x=0, y=0)

        if self.hover is True:
            self.canvas.bind("<Enter>", self.on_enter)
            self.canvas.bind("<Leave>", self.on_leave)

        self.canvas.bind("<Button-1>", self.clicked)
        self.canvas.bind("<Button-1>", self.clicked)

        self.canvas_fg_parts = []
        self.canvas_border_parts = []
        self.text_part = None
        self.text_label = None
        self.image_label = None

        self.draw()

    def draw(self):
        self.canvas.delete("all")
        self.canvas_fg_parts = []
        self.canvas_border_parts = []
        self.canvas.configure(bg=self.bg_color)

        # border button parts
        if self.border_width > 0:

            if self.corner_radius > 0:
                self.canvas_border_parts.append(self.canvas.create_oval(0,
                                                                        0,
                                                                        self.corner_radius * 2,
                                                                        self.corner_radius * 2))
                self.canvas_border_parts.append(self.canvas.create_oval(self.width - self.corner_radius * 2,
                                                                        0,
                                                                        self.width,
                                                                        self.corner_radius * 2))
                self.canvas_border_parts.append(self.canvas.create_oval(0,
                                                                        self.height - self.corner_radius * 2,
                                                                        self.corner_radius * 2,
                                                                        self.height))
                self.canvas_border_parts.append(self.canvas.create_oval(self.width - self.corner_radius * 2,
                                                                        self.height - self.corner_radius * 2,
                                                                        self.width,
                                                                        self.height))

            self.canvas_border_parts.append(self.canvas.create_rectangle(0,
                                                                         self.corner_radius,
                                                                         self.width,
                                                                         self.height - self.corner_radius))
            self.canvas_border_parts.append(self.canvas.create_rectangle(self.corner_radius,
                                                                         0,
                                                                         self.width - self.corner_radius,
                                                                         self.height))

        # inner button parts

        if self.corner_radius > 0:
            self.canvas_fg_parts.append(self.canvas.create_oval(self.border_width,
                                                                self.border_width,
                                                                self.border_width + self.inner_corner_radius * 2,
                                                                self.border_width + self.inner_corner_radius * 2))
            self.canvas_fg_parts.append(self.canvas.create_oval(self.width - self.border_width - self.inner_corner_radius * 2,
                                                                self.border_width,
                                                                self.width - self.border_width,
                                                                self.border_width + self.inner_corner_radius * 2))
            self.canvas_fg_parts.append(self.canvas.create_oval(self.border_width,
                                                                self.height - self.border_width - self.inner_corner_radius * 2,
                                                                self.border_width + self.inner_corner_radius * 2,
                                                                self.height-self.border_width))
            self.canvas_fg_parts.append(self.canvas.create_oval(self.width - self.border_width - self.inner_corner_radius * 2,
                                                                self.height - self.border_width - self.inner_corner_radius * 2,
                                                                self.width - self.border_width,
                                                                self.height - self.border_width))

        self.canvas_fg_parts.append(self.canvas.create_rectangle(self.border_width + self.inner_corner_radius,
                                                                 self.border_width,
                                                                 self.width - self.border_width - self.inner_corner_radius,
                                                                 self.height - self.border_width))
        self.canvas_fg_parts.append(self.canvas.create_rectangle(self.border_width,
                                                                 self.border_width + self.inner_corner_radius,
                                                                 self.width - self.border_width,
                                                                 self.height - self.inner_corner_radius - self.border_width))

        for part in self.canvas_fg_parts:
            self.canvas.itemconfig(part, fill=self.fg_color, width=0)

        for part in self.canvas_border_parts:
            self.canvas.itemconfig(part, fill=self.border_color, width=0)

        # no image given
        if self.image is None:
            # create tkinter.Label with text
            self.text_label = Label(master=self,
                                            text=self.text,
                                            font=self.text_font,
                                            bg=self.fg_color,
                                            fg=self.text_color)
            self.text_label.place(relx=0.5, rely=0.5, anchor=CENTER)

            # bind events the the button click and hover events also to the text_label
            if self.hover is True:
                self.text_label.bind("<Enter>", self.on_enter)
                self.text_label.bind("<Leave>", self.on_leave)

            self.text_label.bind("<Button-1>", self.clicked)
            self.text_label.bind("<Button-1>", self.clicked)

            self.set_text(self.text)

        # use the given image
        else:
            # create tkinter.Label with image on it
            self.image_label = Label(master=self,
                                             image=self.image,
                                             bg=self.fg_color)

            self.image_label.place(relx=0.5,
                                   rely=0.5,
                                   anchor=CENTER)

            # bind events the the button click and hover events also to the image_label
            if self.hover is True:
                self.image_label.bind("<Enter>", self.on_enter)
                self.image_label.bind("<Leave>", self.on_leave)

            self.image_label.bind("<Button-1>", self.clicked)
            self.image_label.bind("<Button-1>", self.clicked)

    def configure_color(self, bg_color=None, fg_color=None, hover_color=None, text_color=None):
        if bg_color is not None:
            self.bg_color = bg_color
        else:
            self.bg_color = self.master.cget("bg")

        if fg_color is not None:
            self.fg_color = fg_color

            # change background color of image_label
            if self.image is not None:
                self.image_label.configure(bg=self.fg_color)

        if hover_color is not None:
            self.hover_color = hover_color

        if text_color is not None:
            self.text_color = text_color
            if self.text_part is not None:
                self.canvas.itemconfig(self.text_part, fill=self.text_color)

        self.draw()

    def set_text(self, text):
        if self.text_label is not None:
            self.text_label.configure(text=text)

    def on_enter(self, event=0):
        for part in self.canvas_fg_parts:
            self.canvas.itemconfig(part, fill=self.hover_color, width=0)

        if self.text_label is not None:
            # change background color of image_label
            self.text_label.configure(bg=self.hover_color)

        if self.image_label is not None:
            # change background color of image_label
            self.image_label.configure(bg=self.hover_color)

    def on_leave(self, event=0):
        for part in self.canvas_fg_parts:
            self.canvas.itemconfig(part, fill=self.fg_color, width=0)

        if self.text_label is not None:
            # change background color of image_label
            self.text_label.configure(bg=self.fg_color)

        if self.image_label is not None:
            # change background color of image_label
            self.image_label.configure(bg=self.fg_color)

    def clicked(self, event=0):
        if self.function is not None:
            self.function()
            self.on_leave()
def sensing():
    n = 0
    if(beginSensing):
        with facemesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face:
            while beginSensing:
                start = time.time()
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                op = face.process(frame)
                x_values = []
                y_values = []
                eyeValsLeft = []
                eyeValsRight = []
                if op.multi_face_landmarks:

                    #Eventually find a way to tie these two together rn im just copying code for simplicity's sake
                    meshcoords = [(int(point.x * frame.shape[0]), int(point.y * frame.shape[1])) for point in op.multi_face_landmarks[0].landmark]
                    for i in op.multi_face_landmarks:
                        for j in i.landmark:
                            x_values.append(j.x)
                            y_values.append(j.y)

                #Blink mechanism
                rightRight = meshcoords[RIGHT_EYE[0]] #Rightmost point of right eye and so on
                rightLeft = meshcoords[RIGHT_EYE[8]]

                rightTop = meshcoords[RIGHT_EYE[12]]
                rightBottom = meshcoords[RIGHT_EYE[4]]


                leftRight = meshcoords[LEFT_EYE[0]]
                leftLeft = meshcoords[LEFT_EYE[8]]

                leftTop = meshcoords[LEFT_EYE[12]]
                leftTop = meshcoords[LEFT_EYE[4]]

                rightWidth = math.hypot(abs(rightRight[0] - rightLeft[0]), abs(rightRight[1] - rightLeft[1]))
                rightHeight = math.hypot(abs(rightTop[0] - rightBottom[0]), abs(rightTop[1] - rightBottom[1]))
                leftWidth = math.hypot(abs(leftRight[0] - leftLeft[0]), abs(leftRight[1] - leftLeft[1]))
                leftHeight = math.hypot(abs(rightTop[0] - rightBottom[0]), abs(rightTop[1] - rightBottom[1]))
                leftRatio = (rightHeight * 100)/rightWidth #These have to be switched because the computer sees it from the image pov. This makes it intuitively easier. 
                rightRatio = (leftHeight/leftWidth) * 100 #The * 100 has been done to make results easier to see
                
                totalRatio = (leftRatio + rightRatio) /2
                mouthHeight = abs(meshcoords[13][1] - meshcoords[14][1])
                mouthWidth = abs(meshcoords[78][0] - meshcoords[292][0])
                mouthRatio = mouthHeight/mouthWidth 
                
                if(n == 0):
                    #Introduce all changing variables here
                    originalAverage = [sum(x_values)/len(x_values), sum(y_values)/len(y_values)]
                    leftBlinkStreak = 0

                

                averageVal = [sum(x_values)/len(x_values), sum(y_values)/len(y_values)] #this giving 0 errors
                differenceX = originalAverage[0] - averageVal[0] #This will result in a positive value for looking right and a negative value for looking left
                differenceY = averageVal[1] - originalAverage[1]
                
                
                #Getting mouse to move
                if(differenceX > 0.03):
                    pyautogui.moveRel(10, 0)
                elif(-differenceX > 0.03):
                    pyautogui.moveRel(-10, 0)
                elif(differenceY > 0.03):
                    pyautogui.moveRel(0, 10)
                elif(-differenceY > 0.03):
                    pyautogui.moveRel(0, -10)
                else:
                    #Clicking should only happen if nothing else is happening
                    if(leftRatio < LEFT_BLINK_THRESHOLD):
                        #print("Blinking")
                        if(totalRatio > TOTAL_BLINK_THRESHOLD):
                            leftBlinkStreak += 1
                        else:
                            leftBlinkStreak = 0 
                    else:
                        #To check if we just returned from a click
                        if(leftBlinkStreak >= NUMBER_BLINK_THRESHOLD):
                            #print("now")
                            if(mouthRatio > MOUTH_OPEN_THRESHOLD): #For some reason right wink sensing wasnt working so i had to get a diff trigger for right click
                                pyautogui.rightClick()
                                leftBlinkStreak = 0
                            else:
                                global pending_text
                                if(pending_text):
                                    pyautogui.click()
                                    pyautogui.write(textToAdd)
                                    pending_text = False
                                else:
                                    pyautogui.click()
                                leftBlinkStreak = 0
                        else:
                            if(leftBlinkStreak != 0):
                                leftBlinkStreak = 0
                n += 1
                if(cv2.waitKey(1) == 27): #press escape key
                    cap.release()
                    cv2.destroyAllWindows()
                    break
    window.after(1000, sensing_background)
    

def showKeyBoard():
    global key
    key = Toplevel()
    geometString = "100x50+" + str(width - 120) + "+" + str(height - 70)
    key.geometry(geometString)
    key.resizable(False, False)
    toShow = TkinterCustomButton(master = key, bg_color="#03AC13",
                                            fg_color="#03AC13",
                                            border_color="#000000",
                                            hover_color="#566573",
                                            text_font=None,
                                            text="Keyboard",
                                            text_color="#000000",
                                            corner_radius=0,
                                            border_width=2,
                                            width=100,
                                            height=50,
                                            hover=True,
                                            command = keyboardManage
    )
    toShow.pack()

def hideKeyBoard():
    global key
    global keyboard_showing
    print("happened")
    keyboard_showing = False
    key.destroy()

def sensing_background():
    
    t = threading.Thread(target=sensing)
    
    t.start()
    
def sensingStart():
    global beginSensing
    showKeyBoard()
    pyautogui.moveTo(width/2, height/2)
    time.sleep(2)
    beginSensing = True
def sensingStop():
    global beginSensing
    hideKeyBoard()
    beginSensing = False
cap = cv2.VideoCapture(0)
facemesh = mp.solutions.face_mesh
draw = mp.solutions.drawing_utils
width, height = pyautogui.size()
LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]  
LOWER_LIPS =[61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95]
UPPER_LIPS =[185, 40, 39, 37,0 ,267 ,269 ,270 ,409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78] 
LEFT_BLINK_THRESHOLD = 80 #Less than 80 is blinking...There needs to be a way to change this dynamically when the program starts...like a set of calib. 
NUMBER_BLINK_THRESHOLD = 2 #Equal to more than 3 times in a row is blinking
MOUTH_OPEN_THRESHOLD = 0.1 #Greater than 0.1 means mouth is open
TOTAL_BLINK_THRESHOLD = 20 #If less than 20, proper blinking...as in both eyes. 
beginSensing = False

originalAverage = []
startedOnce = False

class Resize(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("Bg.jpeg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
window = Tk()
back = Resize(window)

window.title("EyeClik")
window.geometry("400x400")
window.maxsize(853, 480)
back.pack(fill=BOTH, expand=YES)

label = Label(window)  

startButton= TkinterCustomButton(master = window, bg_color="#03AC13",
                                            fg_color="#03AC13",
                                            border_color="#000000",
                                            hover_color="#566573",
                                            text_font=None,
                                            text="Start",
                                            text_color="#000000",
                                            corner_radius=0,
                                            border_width=2,
                                            width=120,
                                            height=40,
                                            hover=True,
                                            command=lambda: [sensingStart()])
stopButton = TkinterCustomButton(master = window,bg_color="#E60026",

                                            fg_color= "#E60026",
                                            border_color="#000000",
                                            hover_color="#566573",
                                            text_font=None,
                                            text="Stop",
                                            text_color="#000000",
                                            corner_radius=0,
                                            border_width=2,
                                            width=120,
                                            height=40,
                                            hover=True,
                                            command=lambda: [sensingStop()])
 

startButton.place(relx = 0.5, rely = 0.4, anchor= CENTER)
stopButton.place(relx = 0.5, rely = 0.6, anchor= CENTER)
window.after(1000, sensing_background)
window.mainloop()

