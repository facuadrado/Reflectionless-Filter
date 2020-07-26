# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 00:47:08 2020

@author: facua
"""
# import required classes
import os
import shutil
from PIL import Image, ImageDraw, ImageFont

def DrawText(draw, text, color, font, x, y):
    (x, y) = (x, y)
    draw.text((x, y), text, fill=color, font=font)

def DrawCircuit(filterType, z0='N/A', l='N/A', c='N/A', ls='N/A', lx='N/A', cs='N/A', cx='N/A'):
    # create Image object with the input image
    
    image = Image.open(filterType + '.png')    
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('arial.ttf', size=28)
    color = 'rgb(0, 0, 0)'
    if filterType == 'lowpass':
        # Draw Inductors Values
        DrawText(draw, l, color, font, 555, 107)
        DrawText(draw, l, color, font, 832, 107)
        DrawText(draw, l, color, font, 215, 362)
        DrawText(draw, l, color, font, 1131, 362)
        
        # Draw Capacitors Values
        DrawText(draw, c, color, font, 469, 234)
        DrawText(draw, c, color, font, 1024, 234)
        DrawText(draw, c, color, font, 469, 640)
        DrawText(draw, c, color, font, 1024, 640)
        
        # Draw Resistance Values
        DrawText(draw, z0, color, font, 469, 490)
        DrawText(draw, z0, color, font, 1024, 490)
        
        try:
            shutil.rmtree('output')
            os.mkdir('output')
        except: 
            os.mkdir('output')
        image.save('output/lowpassfilter.png')
        print('Filter schematic saved to Output folder.')
        image.show()
        
    elif filterType == 'highpass':
        # Draw Conductor Values
        DrawText(draw, c, color, font, 555, 107)
        DrawText(draw, c, color, font, 832, 107)
        DrawText(draw, c, color, font, 215, 362)
        DrawText(draw, c, color, font, 1131, 362)
        
        # Draw Inductors Values
        DrawText(draw, l, color, font, 469, 234)
        DrawText(draw, l, color, font, 1024, 234)
        DrawText(draw, l, color, font, 469, 640)
        DrawText(draw, l, color, font, 1024, 640)
        
        # Draw Resistance Values
        DrawText(draw, z0, color, font, 469, 490)
        DrawText(draw, z0, color, font, 1024, 490)
        
        try:
            shutil.rmtree('output')
            os.mkdir('output')
        except: 
            os.mkdir('output')
        image.save('output/highpassfilter.png')
        print('Filter schematic saved to Output folder.')
        image.show()
        
    elif filterType == 'bandpass':
        # Draw Series Conductor Values
        DrawText(draw, cs, color, font, 638, 112)
        DrawText(draw, cs, color, font, 914, 112)
        DrawText(draw, cs, color, font, 334, 423)
        DrawText(draw, cs, color, font, 1090, 423)

        # Draw Parallel Conductor Values
        DrawText(draw, cx, color, font, 220, 245)
        DrawText(draw, cx, color, font, 796, 245)
        DrawText(draw, cx, color, font, 220, 690)
        DrawText(draw, cx, color, font, 796, 690)
        
        # Draw Series Inductors Values
        DrawText(draw, ls, color, font, 480, 112)
        DrawText(draw, ls, color, font, 770, 112)
        DrawText(draw, ls, color, font, 134, 423)
        DrawText(draw, ls, color, font, 1245, 423)
        
        # Draw Parallel Inductors Values
        DrawText(draw, lx, color, font, 578, 266)
        DrawText(draw, lx, color, font, 1156, 266)
        DrawText(draw, lx, color, font, 578, 712)
        DrawText(draw, lx, color, font, 1156, 712)
        
        # Draw Resistance Values
        DrawText(draw, z0, color, font, 489, 556)
        DrawText(draw, z0, color, font, 1066, 556)
        
        try:
            shutil.rmtree('output')
            os.mkdir('output')
        except: 
            os.mkdir('output')
        image.save('output/bandpassfilter.png')
        print('Filter schematic saved to Output folder.')
        image.show()
    else:
        # Draw Series Conductor Values
        DrawText(draw, cs, color, font, 256, 186)
        DrawText(draw, cs, color, font, 900, 186)
        DrawText(draw, cs, color, font, 256, 612)
        DrawText(draw, cs, color, font, 900, 612)

        # Draw Parallel Conductor Values
        DrawText(draw, cx, color, font, 203, 495)
        DrawText(draw, cx, color, font, 995, 495)
        DrawText(draw, cx, color, font, 517, 240)
        DrawText(draw, cx, color, font, 682, 240)
        
        # Draw Series Inductors Values
        DrawText(draw, ls, color, font, 425, 317)
        DrawText(draw, ls, color, font, 720, 317)
        DrawText(draw, ls, color, font, 425, 720)
        DrawText(draw, ls, color, font, 720, 720)
        
        # Draw Parallel Inductors Values
        DrawText(draw, lx, color, font, 405, 22)
        DrawText(draw, lx, color, font, 775, 22)
        DrawText(draw, lx, color, font, 184, 261)
        DrawText(draw, lx, color, font, 978, 261)
        
        # Draw Resistance Values
        DrawText(draw, z0, color, font, 425, 500)
        DrawText(draw, z0, color, font, 900, 500)
        
        try:
            shutil.rmtree('output')
            os.mkdir('output')
        except: 
            os.mkdir('output')
        image.save('output/bandstopfilter.png')
        print('Filter schematic saved to Output folder.')
        image.show()