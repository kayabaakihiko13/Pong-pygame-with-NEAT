import pygame

pygame.init()

'''
ASSET
'''
WHITE=(255,255,255)
BLACK=(0,0,0)
FPS=60
WIDTH,HEIGHT=700,500
PADDLE_WIDTH,PADDLE_HEIGHT=20,100
layar=pygame.display.set_mode((WIDTH,HEIGHT))

class Paddle:
    """
    class ini merupakan membuat paddle object untuk
    game object tersebut
    """
    COLOR=WHITE
    MOV=5
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))
    def move(self,up):
        if up:
            self.y-=self.MOV
        else:
            self.y+=self.MOV
def draw(win,paddles):
    """
    menggambar asset window dan render update
    """
    win.fill(BLACK)
    for paddle in paddles:
        paddle.draw(win)
    for i in range(10,HEIGHT,HEIGHT//20):
        if i%2 ==1:
            continue
        pygame.draw.rect(win,WHITE,(WIDTH//2-5,i,10,HEIGHT//20))
    pygame.display.update()

def handle_paddle_movement(keys,left_paddle,right_paddle):
    if keys[pygame.K_w] and left_paddle.y-left_paddle.MOV>=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s]and left_paddle.y+left_paddle.MOV+left_paddle.height<=HEIGHT:
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and right_paddle.y-right_paddle.MOV>=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y+right_paddle.MOV+right_paddle.height<=HEIGHT:
        right_paddle.move(up=False)

def main():
    run=True
    clock=pygame.time.Clock()
    left_paddle=Paddle(10,
                       HEIGHT//2-PADDLE_HEIGHT//2,
                       PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle=Paddle(WIDTH-10-PADDLE_WIDTH,
                        HEIGHT//2-PADDLE_HEIGHT//2,
                        PADDLE_WIDTH,PADDLE_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        draw(layar,[left_paddle,right_paddle])
        keys=pygame.key.get_pressed()
        handle_paddle_movement(keys,left_paddle,right_paddle)
if __name__=="__main__":
    main()
