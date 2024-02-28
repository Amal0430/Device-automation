import pyautogui
import time
import json
import cv2
import numpy as np
import pytesseract
import mss
import mss.tools
import threading
from PIL import Image


with open("coordinates.json", "r") as file1:
    data = json.load(file1)
with open("config.json", "r") as file2:
    data2 = json.load(file2)

def login (password):
    time.sleep(2)
    pyautogui.moveTo(data["loginPage"]["1_user"]["x"], data["loginPage"]["1_user"]["y"], duration=0.5)
    pyautogui.click(button='left')

    for i in password :
        if i == "0" :
            pyautogui.moveTo(data["loginPage"]["0"]["x"], data["loginPage"]["0"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "1" :
            pyautogui.moveTo(data["loginPage"]["1"]["x"], data["loginPage"]["1"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "2" :
            pyautogui.moveTo(data["loginPage"]["2"]["x"], data["loginPage"]["2"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "3" :
            pyautogui.moveTo(data["loginPage"]["3"]["x"], data["loginPage"]["3"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "4" :
            pyautogui.moveTo(data["loginPage"]["4"]["x"], data["loginPage"]["4"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "5" :
            pyautogui.moveTo(data["loginPage"]["5"]["x"], data["loginPage"]["5"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "6" :
            pyautogui.moveTo(data["loginPage"]["6"]["x"], data["loginPage"]["6"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "7" :
            pyautogui.moveTo(data["loginPage"]["7"]["x"], data["loginPage"]["7"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "8" :
            pyautogui.moveTo(data["loginPage"]["8"]["x"], data["loginPage"]["8"]["y"], duration=0.2)
            pyautogui.click(button='left')
        elif i == "9" :
            pyautogui.moveTo(data["loginPage"]["9"]["x"], data["loginPage"]["9"]["y"], duration=0.2)
            pyautogui.click(button='left')

    pyautogui.moveTo(data["loginPage"]["login_btn"]["x"], data["loginPage"]["login_btn"]["y"],duration=0.5)
    pyautogui.click(button='left')

def navigateTo (pageName) :

    pyautogui.moveTo(data["navBar"]["settingIcon"]["x"], data["navBar"]["settingIcon"]["y"], duration=0.7)
    pyautogui.click(button='left')

    if pageName == "calibSettings" :
        pyautogui.moveTo(data["settingsPage"]["calib_icon"]["x"], data["settingsPage"]["calib_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif pageName == "unitSettings" :
        pyautogui.moveTo(data["settingsPage"]["unit_icon"]["x"], data["settingsPage"]["unit_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif pageName == "scaleSettings" :
        pyautogui.moveTo(data["settingsPage"]["scale_icon"]["x"], data["settingsPage"]["scale_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif pageName == "barcodeSettings" :
        pyautogui.moveTo(data["settingsPage"]["barcode_icon"]["x"], data["settingsPage"]["barcode_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif pageName == "metrologicalSettings" :
        pyautogui.moveTo(data["settingsPage"]["config_icon"]["x"], data["settingsPage"]["config_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["settingsPage"]["config_icon"]["Metrological_icon"]["x"], data["settingsPage"]["config_icon"]["Metrological_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif pageName == "cailbSettings" :
        pyautogui.moveTo(data["settingsPage"]["config_icon"]["x"], data["settingsPage"]["config_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["settingsPage"]["config_icon"]["calibSettings_icon"]["x"], data["settingsPage"]["config_icon"]["calibSettings_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif pageName == "sysSettings" :
        pyautogui.moveTo(data["settingsPage"]["config_icon"]["x"], data["settingsPage"]["config_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["settingsPage"]["config_icon"]["sysSettings_icon"]["x"], data["settingsPage"]["config_icon"]["sysSettings_icon"]["y"], duration=0.7)
        pyautogui.click(button='left')


def scaleSelection (sName, sUnit):

    time.sleep(2)
    pyautogui.moveTo(data["scalePage"]["scale_dropDown"]["x"], data["scalePage"]["scale_dropDown"]["y"], duration=0.7)
    pyautogui.click(button='left')

    #selecting the weighing scale
    if sName == "bc60" :
        pyautogui.moveTo(data["scalePage"]["bc60_scale"]["x"], data["scalePage"]["bc60_scale"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif sName == "essaeDS" :
        pyautogui.moveTo(data["scalePage"]["easseDS_scale"]["x"], data["scalePage"]["easseDS_scale"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif sName == "fairbanks" :
        pyautogui.moveTo(data["scalePage"]["fairbanks_scale"]["x"], data["scalePage"]["fairbanks_scale"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif sName == "dymo" :
        pyautogui.moveTo(data["scalePage"]["dymo"]["x"], data["scalePage"]["dymo"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif sName == "avery" :
        pyautogui.moveTo(data["scalePage"]["avery"]["x"], data["scalePage"]["avery"]["y"], duration=0.7)
        pyautogui.click(button='left')

    #selecting the scale unit
    if sUnit == "lb-oz" :
        pyautogui.moveTo(data["scalePage"]["scaleUnits_dropdown"]["x"], data["scalePage"]["scaleUnits_dropdown"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["scalePage"]["lb-oz"]["x"], data["scalePage"]["lb-oz"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif sUnit == "kg" :
        pyautogui.moveTo(data["scalePage"]["scaleUnits_dropdown"]["x"], data["scalePage"]["scaleUnits_dropdown"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["scalePage"]["kg"]["x"], data["scalePage"]["kg"]["y"], duration=0.7)
        pyautogui.click(button='left')
    else :
        pass

    #saving the scale
    pyautogui.moveTo(data["scalePage"]["save_btn"]["x"], data["scalePage"]["save_btn"]["y"], duration=0.7)
    pyautogui.click(button='left')
    if sName in ["bc30", "bc60", "bc150"]:
        pyautogui.moveTo(1281, 706, duration=0.7)
        pyautogui.click(button='left')
    else :
        pass

def unitSelection(mUnit):
    
    time.sleep(2)
    pyautogui.moveTo(data["unitsPage"]["mUnits_dropdown"]["x"], data["unitsPage"]["mUnits_dropdown"]["y"], duration=0.7)
    pyautogui.click(button='left')

    #selecting the measurement unit
    if mUnit == "cm-kg" :
        pyautogui.moveTo(data["unitsPage"]["cm-kg"]["x"], data["unitsPage"]["cm-kg"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif mUnit == "inch-lb" :
        pyautogui.moveTo(data["unitsPage"]["inch-lb"]["x"], data["unitsPage"]["inch-lb"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif mUnit == "cm-gram" :
        pyautogui.moveTo(data["unitsPage"]["cm-gram"]["x"], data["unitsPage"]["cm-gram"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif mUnit == "inch-kg" :
        pyautogui.moveTo(data["unitsPage"]["inch-kg"]["x"], data["unitsPage"]["inch-kg"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif mUnit == "inch-lb-oz" :
        pyautogui.moveTo(data["unitsPage"]["inch-lb-oz"]["x"], data["unitsPage"]["inch-lb-oz"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif mUnit == "mm-gram" :
        pyautogui.moveTo(data["unitsPage"]["mm-gram"]["x"], data["unitsPage"]["mm-gram"]["y"], duration=0.7)
        pyautogui.click(button='left')
    
    #saving the measurement unit
    pyautogui.moveTo(data["unitsPage"]["save_btn"]["x"], data["unitsPage"]["save_btn"]["y"], duration=0.7)
    pyautogui.click(button='left')


def calibration(height):

    time.sleep(2)

    #calibrating device based on setupheight
    if height == "1.1" :
        pyautogui.moveTo(data["calibPage"]["1.1"]["x"], data["calibPage"]["1.1"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["calibPage"]["confirmBtn"]["x"], data["calibPage"]["confirmBtn"]["y"], duration=1.2)
        pyautogui.click(button='left')
    elif height == "E1.1" :
        pyautogui.moveTo(data["calibPage"]["E1.1"]["x"], data["calibPage"]["E1.1"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["calibPage"]["confirmBtn"]["x"], data["calibPage"]["confirmBtn"]["y"], duration=1.2)
        pyautogui.click(button='left')
    elif height == "1.5" :
        pyautogui.moveTo(data["calibPage"]["1.5"]["x"], data["calibPage"]["1.5"]["y"], duration=0.7)
        pyautogui.click(button='left')
        pyautogui.moveTo(data["calibPage"]["confirmBtn"]["x"], data["calibPage"]["confirmBtn"]["y"], duration=1.2)
        pyautogui.click(button='left')
    elif height == "2.2" :
        pyautogui.moveTo(data["calibPage"]["2.2"]["x"], data["calibPage"]["2.2"]["y"], duration=0.7)
        pyautogui.click(button='left')

    #closing the calibration page
    #pyautogui.moveTo(data["calibPage"]["close_btn"]["x"], data["calibPage"]["close_btn"]["y"], duration=0.7)
    #pyautogui.click(button='left')
        
def barcodeSelection (barcodeName) :
    pyautogui.moveTo(data["barcodePage"]["barcode_dropdown"]["x"], data["barcodePage"]["barcode_dropdown"]["y"], duration=0.7)
    pyautogui.click(button='left')

    if barcodeName == "zebra" :
        pyautogui.moveTo(data["barcodePage"]["barcode_dropdown"]["x"], data["barcodePage"]["barcode_dropdown"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif barcodeName == "HID" :
        pyautogui.moveTo(data["barcodePage"]["barcode_dropdown"]["x"], data["barcodePage"]["barcode_dropdown"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif barcodeName == "none" :
        pyautogui.moveTo(data["barcodePage"]["none"]["x"], data["barcodePage"]["none"]["y"], duration=0.7)
        pyautogui.click(button='left')

    #saving the barcode
    pyautogui.moveTo(data["unitsPage"]["save_btn"]["x"], data["unitsPage"]["save_btn"]["y"], duration=0.7)
    pyautogui.click(button='left')

def metrologicalStandardSelection (metrologicalStandardValue) :
    pyautogui.moveTo(data["MetrologicalSettings"]["metrologicalStandard_dropdown"]["x"], data["MetrologicalSettings"]["metrologicalStandard_dropdown"]["y"], duration=0.7)
    pyautogui.click(button='left')

    if metrologicalStandardValue == "default" :
        pyautogui.moveTo(data["MetrologicalSettings"]["default"]["x"], data["MetrologicalSettings"]["default"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif metrologicalStandardValue == "raw" :
        pyautogui.moveTo(data["MetrologicalSettings"]["raw"]["x"], data["MetrologicalSettings"]["raw"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif metrologicalStandardValue == "NTEP" :
        pyautogui.moveTo(data["MetrologicalSettings"]["NTEP"]["x"], data["MetrologicalSettings"]["NTEP"]["y"], duration=0.7)
        pyautogui.click(button='left')

    #saving the metrological settings
    pyautogui.moveTo(data["unitsPage"]["save_btn"]["x"], data["unitsPage"]["save_btn"]["y"], duration=0.7)
    pyautogui.click(button='left')

def calibTypeSelection (calibTypeValue) :
    pyautogui.moveTo(data["calibSettings_icon"]["metrologicalStandard_dropdown"]["x"], data["calibSettings_icon"]["metrologicalStandard_dropdown"]["y"], duration=0.7)
    pyautogui.click(button='left')

    if calibTypeValue == "legacy" :
        pyautogui.moveTo(data["calibSettings"]["legacy"]["x"], data["calibSettings_icon"]["legacy"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif calibTypeValue == "marker based" :
        pyautogui.moveTo(data["calibSettings"]["marker_based"]["x"], data["calibSettings_icon"]["marker_based"]["y"], duration=0.7)
        pyautogui.click(button='left')
    elif calibTypeValue == "region based" :
        pyautogui.moveTo(data["calibSettings"]["region_based"]["x"], data["calibSettings_icon"]["region_based"]["y"], duration=0.7)
        pyautogui.click(button='left')

    #saving the metrological settings
    pyautogui.moveTo(data["unitsPage"]["save_btn"]["x"], data["unitsPage"]["save_btn"]["y"], duration=0.7)
    pyautogui.click(button='left')

def measurement():
    pyautogui.moveTo(data["navBar"]["measureIcon"]["x"], data["navBar"]["measureIcon"]["y"], duration=0.7)
    pyautogui.click(button='left')

    #capturing addImages
    if data2["addImages"]["status"] == True :
            for i in range(data2["addImages"]["count"]) :
                time.sleep(2)
                pyautogui.moveTo(data["addImages"]["captureBtn"]["x"], data["addImages"]["captureBtn"]["y"], duration=0.5)
                pyautogui.click(button='left')
    
    #recording measurement video
    if data2["measurementVideo"]["status"] == True :
            time.sleep(4)
            pyautogui.moveTo(data["measurementVideo"]["startBtn"]["x"], data["measurementVideo"]["startBtn"]["y"], duration=0.5)
            pyautogui.click(button='left')
            time.sleep(data2["measurementVideo"]["duration"] + 5)
            pyautogui.moveTo(data["measurementVideo"]["startBtn"]["x"], data["measurementVideo"]["startBtn"]["y"], duration=0.5)
            pyautogui.click(button='left')

    #measuring
    time.sleep(2)
    if data2["measurementPage"]["barcodeStatus"] == True :
        pyautogui.moveTo(data["measurementPage"]["barcodeField"]["x"], data["measurementPage"]["barcodeField"]["y"], duration=0.5)
        pyautogui.click(button='left')
        time.sleep(2)
        pyautogui.write(data2["measurementPage"]["barcodeValue"])
        pyautogui.moveTo(data["measurementPage"]["measureBtn"]["x"], data["measurementPage"]["measureBtn"]["y"], duration=2)
        pyautogui.click(button='left')
    pyautogui.moveTo(data["measurementPage"]["measureBtn"]["x"], data["measurementPage"]["measureBtn"]["y"], duration=2)
    pyautogui.click(button='left')

def snapAndGetText(leftX, topY, rightX, bottomY):
    snapShot = pyautogui.screenshot()
    snapShot.save("snap.png")

    img = Image.open("snap.png")
    crop_region = (leftX, topY, rightX, bottomY)
    cropped_img = img.crop(crop_region)

    text = pytesseract.image_to_string(cropped_img)
    str_text = str(text)
    img.close()
    
    return str_text.strip()


# Define screen size
SCREEN_SIZE = (1920, 1200)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

# Function to continuously record screen
def record_screen():
    global out, recording
    try:
        with mss.mss() as sct:
            while recording:
                frame = np.array(sct.grab(sct.monitors[1]))
                frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
                out.write(frame)
    except Exception as e:
        print("An error occurred while recording:", e)
        stop_recording()

# Function to start recording
def start_recording(VideoName):
    global recording, out
    out = cv2.VideoWriter(VideoName + ".avi", fourcc, 10.0, SCREEN_SIZE)
    recording = True
    record_thread = threading.Thread(target=record_screen)
    record_thread.start()

# Function to stop recording
def stop_recording():
    global recording, out
    recording = False
    if out is not None:
        out.release()
    cv2.destroyAllWindows()
