
class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self,scene_map):
       print (f"really playing {scene_map.start_scene}")

    def play(self):
        print ("Let's go ~")
    def yes_no (self):
        while True:
            put = input("yes or no >> ")
            if put == 'no':
                exit()
            elif put == 'yes':
                break
            else:
                print("plase agent ") 
    def judge_dead(self,life):
        if life == 0:
            x = Death()
            x.enter()
class Death(Scene):
    
    def enter(self):
        print (" You are dead! ")

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeponArmory(Scene):
    
    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self,start_scene):
        print (f"Now,open map {start_scene}")
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.yes_no()
a_game.play()
a_game.judge_dead(0)