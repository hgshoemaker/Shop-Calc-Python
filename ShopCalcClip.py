# Command for shortcut
# C:\Windows\System32\cmd.exe /k "C:\Users\Office Main\Documents\pysrc\shopPriceCalc.py"
# Our cost to retail matrix
import pyperclip


# retail = 0.00

def my_calc(c):
    if .01 <= c <= 5:
        retail_in = c / 0.30
        return retail_in

    elif 5.01 <= c <= 10:
        retail_in = c / 0.40
        return retail_in

    elif 10.01 <= c <= 75:
        retail_in = c / 0.45
        return retail_in

    elif 75.01 <= c <= 200:
        retail_in = c / 0.50
        return retail_in

    elif 200.01 <= c <= 500:
        retail_in = c / 0.58
        return retail_in

    elif 500.01 <= c <= 750:
        retail_in = c / 0.65
        return retail_in

    else:
        retail_in = c / 0.65
        return retail_in


cost = pyperclip.paste()
d = float(cost)
retail = my_calc(d)
output = "{:.2f}".format(retail)
pyperclip.copy(output)
