import pygame
pygame.init()
s = pygame.display.set_mode((400,400))
done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  
  pygame.draw.circle(s,(150,175,125),(300,300),50)
  
  pygame.display.flip()