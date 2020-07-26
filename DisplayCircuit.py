# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 00:47:08 2020

@author: facua
"""
# import required classes

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
        
        image.save('lowpassfilter.png')
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
        
        image.save('highpassfilter.png')
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
        
        image.save('bandpassfilter.png')
        image.show()
    else:
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
        
        image.save('bandstopfilter.png')
        image.show()