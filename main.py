import math, json, numpy as np
from PIL import Image
settings = json.loads(open('settings.json', 'r').read())
w,h,pixelsarray = settings["w"], settings["h"],np.array(Image.open(settings["photo"])).tolist()
if settings["Auto"]: h,w = len(pixelsarray),len(pixelsarray[0])
for a2 in range(h):
  a = a2
  if h != len(pixelsarray): a = a2 * (len(pixelsarray)/h)
  if a % ((len(pixelsarray)/h)*2) != 0:
    temp = ""
    for b2 in range(w):
      b,clr = b2,[0,0,0,0,0,0]
      if w != len(pixelsarray[0]): b = b2 * (len(pixelsarray[0])/w)
      try:
        for c in range(3): clr[c] = pixelsarray[math.floor(a)][math.floor(b)][c]
        for c in range(3): clr[c+3] = pixelsarray[math.floor(a)-1][math.floor(b)][c]
      except Exception:
        pass
      temp += f"\033[38;2;{clr[0]};{clr[1]};{clr[2]}m\033[48;2;{clr[3]};{clr[4]};{clr[5]}m▄\033[0m"
    print(temp)