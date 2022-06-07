import pygame

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400, 700]
screen = pygame.display.set_mode(size)

title = "Swipe 벽돌깨기"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x=0
        self.y=0
    def put_img(self,address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            
    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img,(sx,sy))
        self.sx,self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img,(self.x,self.y))

#class 없이 이미지 속성
#ss = pygame.image.load("C:/Users/jjojj/Desktop/Ai project/ball.png").convert_alpha()
#ss = pygame.transform.scale(ss,(15,15))
#ss_sx,ss_sy = ss.get_size()
#ss_x = round(size[0]/2-ss_sx/2)
#ss_y = round(size[1])-200-ss_sy


#class 사용한 이미지 속성
ss = obj()
ss.put_img("C:/Users/jjojj/Desktop/Ai project/ball.png")
ss.change_size(15,15)
ss.x = round(size[0]/2-ss.sx/2)
ss.y = round(size[1])-200-ss.sy

rr = obj()
rr.put_img("C:/Users/jjojj/Desktop/Ai project/toball.png")
rr.change_size(15,15)
rr.x = round(size[0]/2-ss.sx/2)
rr.y = round(size[1])-200-ss.sy+20

br_11 = obj()
br_11.put_img("C:/Users/jjojj/Desktop/Ai project/brick-1.png")
br_11.change_size(size[0]/7,size[1]/17)
br_11.x = round(size[0]/7-ss.sx/2)
br_11.y = round(size[1])-500-ss.sy

br_12 = obj()
br_12.put_img("C:/Users/jjojj/Desktop/Ai project/brick-1.png")
br_12.change_size(size[0]/7,size[1]/17)
br_12.x = round(2*size[0]/7-ss.sx/2)
br_12.y = round(size[1])-500-ss.sy

br_21 = obj()
br_21.put_img("C:/Users/jjojj/Desktop/Ai project/brick-1.png")
br_21.change_size(size[0]/7,size[1]/17)
br_21.x = round(size[0]/7-ss.sx/2)
br_21.y = round(size[1]+size[1]/17)-500-ss.sy

black = (0,0,0)
white = (255,255,255)
k = 0

# 4. 메인 이벤트
SB = 0
while SB == 0:

    # 4-1. FPS 설정
    clock.tick(60)

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        print(event)

    # 4-3. 입력, 시간에 따른 변화
    k += 1

    # 4-4. 그리기
    screen.fill(white)
    ss.show()
    rr.show()
    br_11.show()
    br_12.show()
    br_21.show()

    # 4-5. 업데이트
    pygame.display.flip()





# 5. 게임 종료
pygame.quit()