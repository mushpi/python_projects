import tkinter as tk
from random import randint,uniform,random
import math

#scale (radio bubble diameter) in light year
SCALE = 225
#number of civilization according to drakes equation
NUM_CIVS = 15600000

#setting up tkinter canvas
root = tk.Tk()
root.title("Milky way galaxy")
c = tk.Canvas(root, height=800,width=1000,bg="black")
c.grid()
c.configure(scrollregion=(-500,-400,500,400))
