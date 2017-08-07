import pyautogui
import clipboard

#mouse example
pyautogui.moveTo(x, y)
pyautogui.click(button = 'left')

#keyboard example
pyautogui.hotkey('ctrl', 'c')
name = clipboard.paste()
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('esc')

#clipboard action
clipbaord.copy(...)
