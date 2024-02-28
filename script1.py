from reusableCodes import *
import time

file = open("report.txt", "a")
file.truncate(0)

# #login to application
# login("0000")
# time.sleep(8)
# text = snapAndGetText(290, 356, 739, 424)
# if text == "Calibration" :
#     print("Login successfull")
#     file.write("Case1: Pass - login successfull\n")
# else:
#     print("Login failed")
#     file.write("Case1: Fail - login failed\n")


# #select and saving measurement units
# unitToSave = ["cm-kg", "inch-lb", "cm-gram", "inch-kg", "inch-lb-oz", "mm-gram"]
# navigateTo("unitSettings")

# for i in unitToSave :

#     unitSelection(i)
#     time.sleep(5)
#     text = snapAndGetText(192, 1014, 644, 1155)
#     if text == "Data saved successfully" :
#         print("Measurement unit " + i + " saved successfully")
#         file.write("Verify able to change the Measurement unit to " + i  + " - PASS \n")
#     elif text == "" :
#         print("Measurement unit " + i + " already saved")
#         # file.write("Verify able to change the Measurement unit to " + i  + " - PASS \n")
#     else:
#         print("error in saving measurement unit " + i)
#         file.write("Verify able to change the Measurement unit to " + i  + " - FAIL \n")
#         file.write("Error is --> " + text + "\n")

#select and saving scale
start_recording("scale_saving")
time.sleep(2)
scaleToSave = "essaeDS"
navigateTo("scaleSettings")
scaleSelection(scaleToSave, "null")
time.sleep(5)
text = snapAndGetText(183, 1050, 1419, 1129)
if text == "Weighing scale settings updated, Please Calibrate before proceeding" or text == "Weighing scale settings updated" :
    print( scaleToSave + " weighing scale saved successfully")
    file.write("Verify able to save the " + scaleToSave + " weighing scale - PASS \n")
else:
    print( "Error in saving " + scaleToSave + " weighing scale")
    file.write("Verify able to save the " + scaleToSave + " weighing scale - FAIL \n")
    file.write("Error is --> " + text)
time.sleep(2)
stop_recording()

# #selecting and saving barcode
# barcodeToSave = "zebra"
# navigateTo("barcodeSettings")
# barcodeSelection(barcodeToSave)
# time.sleep(5)
# text = snapAndGetText(192, 1014, 644, 1155)
# print(text)
# if text == "Data saved successfully" :
#     print( barcodeToSave + " barcode saved successfully")
#     file.write("Verify able to save the " + barcodeToSave + " barcode - PASS \n")
# else:
#     print( "Error in saving " + barcodeToSave + " barcode")
#     file.write("Verify able to save the " + barcodeToSave + " barcode - FAIL \n")
#     file.write("Error is --> " + text)

# #selecting and saving the metrological standards
# metrologicalSetting_ToSave = "default"
# navigateTo("metrologicalSettings")
# metrologicalStandardSelection (metrologicalSetting_ToSave)
# time.sleep(5)
# text = snapAndGetText(192, 1014, 644, 1155)
# print(text)
# if text == "Data saved successfully" :
#     print( metrologicalSetting_ToSave + " metrological setting saved successfully")
#     file.write("Verify able to save the " + metrologicalSetting_ToSave + " metrological setting - PASS \n")
# else:
#     print( "Error in saving " + metrologicalSetting_ToSave + " metrological setting")
#     file.write("Verify able to save the " + metrologicalSetting_ToSave + " metrological setting - FAIL \n")
#     file.write("Error is --> " + text)

# #selecting and saving calibration type
# calibTypeToSave = "legacy"
# navigateTo("cailbSettings")
# calibTypeSelection(calibTypeToSave)
# time.sleep(5)
# text = snapAndGetText(192, 1014, 644, 1155)
# print(text)
# if text == "Data saved successfully" :
#     print( calibTypeToSave + " calibration setting saved successfully")
#     file.write("Verify able to save the " + calibTypeToSave + " calibration setting - PASS \n")
# else:
#     print( "Error in saving " + calibTypeToSave + " calibration setting")
#     file.write("Verify able to save the " + calibTypeToSave + " calibration setting - FAIL \n")
#     file.write("Error is --> " + text)

# #calibrating the device
# calibration("1.5")
# time.sleep(9)
# text = snapAndGetText(490, 470, 1433, 566)
# if text == "SYSTEM CALIBRATED SUCCESSFULLY" :
#     print("System calibrated successfully")
#     file.write("Case4: Pass - System calibrated successfully\n")
# else:
#     print("Calibration failed")
#     file.write("Case4: fail - Calibration failed\n")

# #measuring
# measurement()
# time.sleep(5)
# text = snapAndGetText(101, 1050, 630, 1100)
# if text == "Object Measured Successfully" :
#     print("Measurement successfull")
#     file.write("Case5: Pass - Measurement successfull\n")
# else:
#     print("Measurement failed")
#     file.write("Case5: fail - Measurement failed\n")

file.close()