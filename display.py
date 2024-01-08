import pygame
import random


class Display:
    
    def __init__(self, width, height, barAmount, gradients, sort_name, surface):
        self.width = width
        self.height = height
        self.barAmount = barAmount
        self.gradients = gradients
        self.surface = surface
        self.sort_name = sort_name
    
    def set_list(self):
        self.barLoc = [ i*18 for i in range(1, self.barAmount+1)]
        self.barH = [ random.randrange(10,400) for _ in range(self.barAmount)]
        self.barColor = [ self.gradients[i % 3] for i in range(self.barAmount)] 
    
    def draw_all(self):
        font = pygame.font.SysFont('arial', 20)
        self.surface.fill("WHITE")
        current = font.render(f"{self.sort_name}", 1, 'Blue')
        label = font.render("R - Reset | ↑ - Ascending", 1, 'BLACK')
        type1 = font.render("B - Bubble sort | S - Selection sort | I - Insertion sort | M - Merge sort | C - Cocktail sort", 1, 'BLACK')
        type2 = font.render("Q - Quick sort | H - Heap sort | A - Radix sort", 1, 'BLACK')
        self.surface.blit(current, (self.width/2 - current.get_width()/2, 10))
        self.surface.blit(label, (self.width/2 - label.get_width()/2, 40))
        self.surface.blit(type1, (self.width/2 - type1.get_width()/2, 70))
        self.surface.blit(type2, (self.width/2 - type2.get_width()/2, 100))
        self.draw_bars({},True)
        pygame.display.update()

    def draw_bars(self, color_pos={}, clear_bg = False):
        if clear_bg:
            pygame.draw.rect(self.surface, 'white', (0, 140, self.width, self.height))
        for i, (lft, top, color) in enumerate(zip(self.barLoc, self.barH, self.barColor)):
            if i in color_pos:
                color = color_pos[i]
            pygame.draw.rect(self.surface, color, (lft, self.height-top, 15, top))
            
        if clear_bg:
            pygame.display.update()
    
    def recolor_bar(self, idx, color):
        pygame.draw.rect(self.surface, color ,(self.barLoc[idx], self.height-self.barH[idx], 15, self.barH[idx]))
        self.update(10)
    
    def update(self, timeDelay):
        pygame.time.delay(timeDelay)
        pygame.display.update()
