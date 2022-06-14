from Game import SBBGame
from Model import DDQN_Model
import random, time

now_state = {}
act = 0.5

epsilon = 1
game_attempt = 0

EPSILON_DECREASE_PER_GAME = 1e-4
EPOCH = 100000

brain = DDQN_Model()

game = SBBGame()
#game.ui = False
game.user = False
game.start()

for _ in range(EPOCH):
    # while game.dqn_state == None: time.sleep(0.1)
    # state = game.dqn_state

    # print(state)
    input('press to countinue')
    
    # game.dqn_state = None
    
    #set action from state
    game.guide_line = act
    if epsilon > random.random():
        game.setACT(random.randint(0, 16) / 16)
    else:
        game.setACT(act)
        
    while game.dqn_data == None: time.sleep(0.1)
    result = game.dqn_data
    if result[2] == 1:
        game_attempt += 1
        #died
    print(result)
    game.dqn_data = None

