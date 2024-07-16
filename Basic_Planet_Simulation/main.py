import pygame as pg
from planet import *
import math

pg.init()
width,heigh = 800,800
scene = pg.display.set_mode((width,heigh))
pg.display.set_caption('Planets Simulation')

FONT = pg.font.SysFont("comicsans",16)

def main():
    run = True
    clock = pg.time.Clock()
    
    sun = planet(0,0,30,(255,255,0),1.98892*10**30)
    sun.sun = True
    earth = planet(-1*planet.AU,0,16,(100,149,237),5.9742*10**24)
    earth.y_vel = 29.783*1000
    mars = planet(-1.524 * planet.AU,0,12,(188,39,50),6.39*10**23)
    mars.y_vel = 24.077 * 1000
    mercury = planet(0.287*planet.AU,0,8,(80,78,81),3.30*10**23)
    mercury.y_vel = 47.4*1000
    venus = planet(0.723*planet.AU,0,14,(255,255,255),4.8685*10*24)
    venus.y_vel = -35.02 * 1000
    planets = [sun,earth,mars,mercury,venus]
    
    while run:
        clock.tick(60)
        scene.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        for p in planets:
            p.update_positiion(planets)
            p.draw(scene,width,heigh,FONT)
            
        pg.display.update()
    pg.quit()
    
main()