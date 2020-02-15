from sys import exit
from random import randint
from textwrap import dedent
class Scene(object):
#场景 类
    def enter(self):
        print("This scene is not yet configured.") #场景尚未配置
        print ("Subclass it and implement enter().") #分类并实现enter（）
        exit(1)


class Engine(object):
#引擎 类
    def __init__(self,scene_map):
       self.scene_map = scene_map #场景图

    def play(self):
        current_scene = self.scene_map.opening_scene() #当前运行地图
        last_scene = self.scene_map.next_scene('finished')#获取最后一张地图变量
        while current_scene != last_scene: 
            next_scene_name = current_scene.enter() 
            #下一张地图名字 = 进行当前运行场景的enter主函数的返回值 返回下一张地图名字
            current_scene = self.scene_map.next_scene(next_scene_name)
            #当前运行地图名称更改为 scene_map map类的next_scene函数（上一场景的返回值）
            #be sure to print out the last scene
            #current_scene.enter()
            #继续执行场景主函数
            if current_scene == last_scene:
                last_scene.enter()
    # def yes_no (self):
    #     while True:
    #         put = input("yes or no >> ")
    #         if put == 'no':
    #             exit()
    #         elif put == 'yes':
    #             break
    #         else:
    #             print("plase agent ") 
    # def judge_dead(self,life):
    #     if life == 0:
    #         x = Death()
    #         x.enter()
class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]
    def enter(self):
        print (Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print (dedent(""""
                here we go 
                shoot 
                dodge
                tell a joke
                """))
        action = input("> ")

        if action == "shoot!":
            print (dedent(""""
                    Then he eats you.
                    """))
            return 'death'
        elif action == "dodge!":
            print (dedent(""""
                     Gothon stomps on your head and eats you.
                    """))
            return 'death'
        elif action == "tell a joke":
            print (dedent(""""
                        Lucky for you 
                        """))
            return 'laser_weapon_armory'

        else:
            print ("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeponArmory(Scene):
    #武器库 类
    def enter(self):
        print (dedent("""
                武器库 开锁 十次三位数密码
                """))
        
        #code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}" 
        #设定三位数随机密码
        code = 233
        guess_1 = input("[keypad]> ")
        guess = int(guess_1)
        guesses = 0
        while guess != code and guesses < 10:
            print ("BZZZZEDDD!")
            if guess > code:
                print ("so big")
            elif guess < code:
                print ("so small")
            guesses +=1
            guess_1 = input("[keypad]> ")
            guess = int(guess_1)

        if guess == code:
            print (dedent("""
                    成功 继续
                    """))
            return 'the_bridge'
        else:
            print (dedent("""
                    错误~~
                    """))
            return 'death'


class TheBridge(Scene):
#舰桥
    def enter(self):
        print (dedent("""
                炸桥~
                扔炸弹？ throw the bomb
                慢慢放？ slowly place the bomb 
                """))
        action = input("> ")
        if action == "god":
            return 'finished'
        if action == "throw the bomb":
            print (dedent("""
                    you die
                    """))
            return 'death'
        
        elif action == "slowly place the bomb":
            print (dedent("""
                    lucky ~
                    """))
            return 'escape_pod'
        else:
            print ("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print (dedent("""
                五个逃生舱 选一个

                """))
        
        good_pod = 5
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print (dedent("""
                    你选择了 {guess} you die
                    """))
            return 'death'
        else :
            print ((dedent("""
                   你选择了 {guess} lucky~
                    """)))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print ("You won! Good job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished(),
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene
        #定义变量 当前地图名称
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        #返回scene_name 对应的 地图类
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')
a_game = Engine(a_map)

a_game.play()

# test = globals()
# print (test)
