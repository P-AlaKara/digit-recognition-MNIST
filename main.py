# This file includes original code from:
# https://github.com/mohammed97ashraf/Real-time-Handwritten-Digit-Recognition/
# Modifications made:
# - Added extra UI elements (improved layout, colours & fonts, UI elements, instructions & feedback).
# - Used a different model for prediction.

import tensorflow as tf
from tensorflow.keras.models import load_model
from tkinter import *
import tkinter as tk
#import win32gui
from win32.win32gui import EnumWindows, GetWindowText, GetWindowRect
import os
import cv2
from PIL import ImageGrab, Image
import numpy as np

model = load_model('model/mnist_model.keras')

def get_handle():
    toplist = []
    windows_list = []
    canvas = 0
    def enum_win(hwnd, result):
        win_text = GetWindowText(hwnd)
        #print(hwnd, win_text)
        windows_list.append((hwnd, win_text))
    EnumWindows(enum_win, toplist)
    for (hwnd, win_text) in windows_list:
        if 'tk' == win_text:
            canvas = hwnd
    return canvas

def preprocessing_image():
    """function to preprocess the image to"""
    image = cv2.imread('test.jpg')
    #print(type(image))
    grey = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey.copy(), 75, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow('binarized image', thresh)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(type(contours[0]))
    # print(len(contours[0]))
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
    #cv2.imshow('Contours', image) 
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)        
        # Creating a rectangle around the digit in the original image (for displaying the digits fetched via contours)
        cv2.rectangle(image, (x,y), (x+w, y+h), color=(0, 255, 0), thickness=2)
        # Cropping out the digit from the image corresponding to the current contours in the for loop
        digit = thresh[y:y+h, x:x+w]        
        # Resizing that digit to (18, 18)
        resized_digit = cv2.resize(digit, (18,18))        
        # Padding the digit with 5 pixels of black color (zeros) in each side to finally produce the image of (28, 28)
        padded_digit = np.pad(resized_digit, ((5,5),(5,5)), "constant", constant_values=0)        
        # Adding the preprocessed digit to the list of preprocessed digits
        preprocessed_digit = (padded_digit)
    return preprocessed_digit

def predict_digit(img):
    """function to predict the digit. 
    Argument of function is PIL Image"""
    img.save('test.jpg')
    preprocessed_image = preprocessing_image()
    # print(type(preprocessed_image))
    # print(preprocessed_image.shape)
    img = preprocessed_image.reshape(1, 28, 28, 1)
    img = img/255.0
    #predicting the digit
    result = model.predict([img])[0]
    os.remove('test.jpg')
    return np.argmax(result), max(result)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Digit Recognizer")
        self.geometry("500x400")
        self.configure(bg="#f5f5f5")

        # Create UI Elements
        self.header = tk.Label(self, text="Handwritten Digit Recognition", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
        self.instructions = tk.Label(self, text="Draw a digit in the canvas below and click 'Recognize'.", font=("Helvetica", 12), bg="#f5f5f5", fg="#555")
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross", highlightthickness=2, highlightbackground="#ccc")
        self.result_label = tk.Label(self, text="Prediction will appear here", font=("Helvetica", 14), bg="#f5f5f5", fg="#007BFF")
        self.classify_btn = tk.Button(self, text="Recognize", command=self.classify_handwriting, bg="#007BFF", fg="white", font=("Helvetica", 12), width=12)
        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_all, bg="#FF5733", fg="white", font=("Helvetica", 12), width=12)

        # Layout UI Elements
        self.header.grid(row=0, column=0, columnspan=2, pady=10)
        self.instructions.grid(row=1, column=0, columnspan=2, pady=5)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
        self.classify_btn.grid(row=4, column=0, pady=10, padx=10, sticky="e")
        self.clear_btn.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        # Bindings
        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        """Clears the canvas."""
        self.canvas.delete("all")
        self.result_label.config(text="Prediction will appear here", fg="#007BFF")

    def classify_handwriting(self):
        """Captures the canvas, predicts the digit, and displays the result."""
        HWND = self.canvas.winfo_id()
        hwnd = get_handle()
        rect = GetWindowRect(HWND)
        x1, y1, x2, y2 = rect

        im = ImageGrab.grab((x1 + 40, y1 + 40, x2 + 100, y2 + 100))
        digit, acc = predict_digit(im)
        self.result_label.config(text=f"Digit: {digit}, Confidence: {int(acc * 100)}%", fg="#28A745")

    def draw_lines(self, event):
        """Allows the user to draw on the canvas."""
        r = 8
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="black")


app = App()
app.mainloop()
