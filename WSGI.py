from flask import Flask, render_template, redirect
import pyautogui

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/forward")
def forward():
    pyautogui.press("right")
    return redirect("/")

@app.route("/back")
def back():
    pyautogui.press("left")
    return redirect("/")