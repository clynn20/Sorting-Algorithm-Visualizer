import pygame
from display import Display
from algo import Algorithm


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BAR_AMOUNT = 42
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREEN = 0, 255, 0
RED = 255, 0, 0
GREY = 128, 128, 128
GRADIENTS = [(128, 128, 128), (160,160,160), (192,192,192)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Sorting Algo Visualizer')
    clock = pygame.time.Clock()
    bars = Algorithm(WINDOW_WIDTH, WINDOW_HEIGHT, BAR_AMOUNT, GRADIENTS, "Bubble Sort", screen)
    bars.set_list()
    bars.draw_all()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                bars.bubble_sort()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                bars.selection_sort()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                bars.insertion_sort()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                bars.merge_sort(0, BAR_AMOUNT-1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                bars.cocktail_sort()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                bars.heap_sort()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                bars.radix_sort()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                bars.quick_sort(0, BAR_AMOUNT-1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                bars.set_list()
                bars.draw_all()
        pygame.display.update()

        clock.tick(100)
    pygame.quit()


if __name__ == "__main__":
    main()