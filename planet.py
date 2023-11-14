import math
import pygame
class planet:
    AU = 149.6e6 * 1000
    GRAVITY = 6.67428e-11
    SCALE = 250/AU #1AU = 100px
    TIMESTEP = 3600*24 #1day
    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit= []
        self.sun=False
        self.to_sun = 0
        self.x_vel=0
        self.y_vel=0
        
    def draw(self,scene,w,h,font):
        x = self.x * self.SCALE + w/2
        y = self.y * self.SCALE + h/2
        if len(self.orbit)>2:
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x* self.SCALE + w/2
                y = y*self.SCALE + h/2  
                updated_points.append((x,y))
            pygame.draw.lines(scene,self.color,False,updated_points,2)
        
        pygame.draw.circle(scene,self.color,(x,y),self.radius)
        
        if not self.sun:
            distance_text = font.render(f"{round(self.to_sun/1000,1)}km",1,(255,255,255))
            scene.blit(distance_text,(x - distance_text.get_width()/2,y- distance_text.get_height()/2))
        
    def attraction(self,other):
        other_x,other_y = other.x,other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        if other.sun:
            self.to_sun = distance
        force = self.GRAVITY*self.mass*other.mass/distance**2
        theta = math.atan2(distance_y,distance_x)
        force_x = math.cos(theta) *force
        force_y = math.sin(theta) *force
        return force_x,force_y
    
    def update_positiion(self,planets):
        total_fx = total_fy=0
        for p in planets:
            if self == p:
                continue
            fx,fy = self.attraction(p)
            total_fx += fx
            total_fy += fy
            
        self.x_vel += total_fx/self.mass*self.TIMESTEP
        self.y_vel += total_fy/self.mass*self.TIMESTEP
        
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x,self.y))