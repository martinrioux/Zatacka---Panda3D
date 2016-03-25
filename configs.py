def init_defines():

    global PANDA3D
    global ENTITY_ID
    ENTITY_ID = 0
    global ENTITIES
    ENTITIES  = {}
    global GAME_ONGOING
    GAME_ONGOING  = 0
    global IN_MENU
    IN_MENU  = False
    global SCALE
    SCALE  = 2
    global DEFAULT_SCALE
    DEFAULT_SCALE  = 2
    global DOTS
    DOTS  = []
    global COLLISION_MAP
    COLLISION_MAP  = []
    global NEXT_BONUS_TIME
    global ESC_PRESSED
    ESC_PRESSED  = False
    global BORDER
    BORDER  = True
    global MENU_LOCKED
    MENU_LOCKED  = False
    global RIGHT_ANGLE_TURN
    RIGHT_ANGLE_TURN  = False
    global FORCE_RIGHT_ANGLE_TURN
    FORCE_RIGHT_ANGLE_TURN  = False
    global TURN_SPEED
    TURN_SPEED = 3
    global LAST_KEYSTROKE
    LAST_KEYSTROKE = ''
    global DEFAULT_FORWARD_SPEED
    DEFAULT_FORWARD_SPEED = 0.004
    global FORWARD_SPEED
    FORWARD_SPEED = 0.004
    global GAME_WON
    GAME_WON = False
    global LINE_GAP
    LINE_GAP = True
    global EMPTY_COLLISION_MAP
    global SCREEN_FLIPPED
    SCREEN_FLIPPED = False
    global BONUS_START_TIME
    BONUS_START_TIME = [-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100]
    global ARDUINO_MODE
    ARDUINO_MODE = False
    global ARDUINO_PLAYER_ON
    ARDUINO_PLAYER_ON = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    global BUTTONS_MAP
    BUTTONS_MAP = [  
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', ''],
                ['', '']
                ]

    global ARDUINO_BUTTONS_MAP
    ARDUINO_BUTTONS_MAP = [  
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False],
                [False,False]
                ]

    global COLORS_MAP
    COLORS_MAP = [
                    [(0.849039856888, 0.179789163344, 0.960655383393, 1)],
                    [(0.0454329971067, 0.589286953278, 0.889305754359, 1)],
                    [(0.768018021368, 0.966743190289, 0.988540284505, 1)],
                    [(0.282809394753, 0.583680152571, 0.0361250425779, 1)],
                    [(0.591341893371, 0.478824388857, 0.079365733773, 1)],
                    [(0.199449718076, 0.165326100516, 0.38813552007, 1)],
                    [(0.282021141127, 0.591916482705, 0.243798266905, 1)],
                    [(0.583368749554, 0.602125671953, 0.580170643419, 1)],
                    [(0.447196113344, 0.0243613541139, 0.196444417924, 1)],
                    [(0.194220306736, 0.0014082511874, 0.0382037847883, 1)],
                    [(0.347420788079, 0.520054354005, 0.0409105514601, 1)],
                    [(0.686503568073, 0.437218106099, 0.161961704929, 1)],
                    [(0.579385028523, 0.797304028733, 4.83925327651e-05, 1)],
                    [(0.687661746377, 0.840115095476, 0.318198344829, 1)],
                    [(0.383330121821, 0.829632076057, 0.0318957895047, 1)],
                    [(0.551779755415, 0.454981843035, 0.163372422308, 1)],
                    [(0.298264225421, 0.766290405122, 0.496108458311, 1)],
                    [(0.296716168317, 0.768643588493, 0.115200534811, 1)],
                    [(0.459728344536, 0.114569692155, 0.968472309478, 1)],
                    [(0.897293332771, 0.490865649236, 0.696062915737, 1)],
                    [(0.613706935284, 0.320310177736, 0.136104667011, 1)],
                    [(0.519867202495, 0.712811643162, 0.33709858479, 1)],
                    [(0.89314258442, 0.787216171494, 0.537891524686, 1)],
                    [(0.228319766143, 0.300321267252, 0.864816389074, 1)],
                    [(0.213585927205, 0.714442013667, 0.07217700473, 1)],
                    [(0.383770203513, 0.853616271358, 0.401672110593, 1)],
                    [(0.480517371274, 0.726557651108, 0.0246547280709, 1)],
                    [(0.520409356835, 0.586539927476, 0.373610911296, 1)],
                    [(0.106010067557, 0.698425253437, 0.268364653746, 1)],
                    [(0.650633575551, 0.909095289933, 0.348587965988, 1)],
                    [(0.581458976792, 0.760212028681, 0.846139544767, 1)],
                    [(0.696933566293, 0.908627792293, 0.255547197879, 1)],
                    [(0.271311645968, 0.23878747306, 0.459352494848, 1)],
                    [(0.883178812027, 0.541418055772, 0.85796636799, 1)],
                    [(0.182929080218, 0.389716117336, 0.372727344286, 1)],
                    [(0.910074372314, 0.949369738396, 0.17325591772, 1)],
                    [(0.827011953367, 0.390709917547, 0.711840786408, 1)],
                    [(0.451052287275, 0.450823694069, 0.645599869489, 1)],
                    [(0.802151947527, 0.299365371378, 0.63075706166, 1)],
                    [(0.687173328961, 0.979904259383, 0.514821029605, 1)],
                    [(0.143793295007, 0.149907303432, 0.540225387797, 1)],
                    [(0.224433266618, 0.473537631658, 0.192158087867, 1)],
                    [(0.773248378627, 0.373842380866, 0.667538745588, 1)],
                    [(0.979908034376, 0.184183484984, 0.741070962164, 1)],
                    [(0.354279761715, 0.954670387675, 0.906653592992, 1)],
                    [(0.0874967571657, 0.956943643946, 0.096793917443, 1)],
                    [(0.827467995262, 0.463809677335, 0.181948685069, 1)],
                    [(0.109354657249, 0.169034672765, 0.507362913817, 1)],
                    [(0.479622712883, 0.517233332706, 0.355391180927, 1)],
                    [(0.670838823328, 0.531835197002, 0.755230079273, 1)]
                ]