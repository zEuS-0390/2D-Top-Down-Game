from os import path
SCALE = 20
LEFT_CLICK = 1
RIGHT_CLICK = 3
IMAGESDIRECTORY = "images"
ANIMDIRECTORY = path.join(IMAGESDIRECTORY, "anim")
SPRITEIMAGES = {
            'GRASS': path.join(IMAGESDIRECTORY, 'grass.png'),
            'WALL': path.join(IMAGESDIRECTORY, 'wall.png')
         }
ANIMIMAGES = {
               'FOLLOWER':{'UP':path.join(ANIMDIRECTORY,'follower', 'up.png'),
                           'UPLEFT':path.join(ANIMDIRECTORY,'follower', 'upleft.png'),
                           'UPRIGHT':path.join(ANIMDIRECTORY,'follower', 'upright.png'),
                           'DOWN':path.join(ANIMDIRECTORY,'follower', 'down.png'),
                           'DOWNLEFT':path.join(ANIMDIRECTORY,'follower', 'downleft.png'),
                           'DOWNRIGHT':path.join(ANIMDIRECTORY,'follower', 'downright.png'),
                           'LEFT':path.join(ANIMDIRECTORY,'follower', 'left.png'),
                           'RIGHT':path.join(ANIMDIRECTORY,'follower', 'right.png'),}
             }