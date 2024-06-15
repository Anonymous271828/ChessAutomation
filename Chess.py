from stockfish import Stockfish
import stockfish
import cv2
import numpy as np
import pyautogui
import time

# REQUIREMENTS:
# ONLY FOR PUZZLES
# VERY IMPORTANT: EACH SQUARE IS 108 BY 108 PIXELS. THE STARTING PIXEL IS 288, 119 FOR GAMES. GAMES MUST BE IN THEATER/FOCUS MODE AND MUST HAVE COORDINATES OUTSIDE. STARTING PIXEL FOR GAMES AGAINST BOTS IS 414, 169 and SQUARE SIZE IS 96 BY 96.
# VERY IMPORTANT: EACH SQUARE IS 108 by 108 PIXELS. THE STARTING PIXEL IS 353, 119 FOR PUZZLES.
# ALSO, COORDINATES MUST BE OUTSIDE THE GRID AND HIGHLIGHT MOVES MUST BE OFF

#castling = {"w":True, "b":True}
column = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
def turn(puzzles):
    if puzzles:
        img = pyautogui.screenshot(r"c:\Users\kiss1\PycharmProjects\Automation\Chess_player\turn.png", region=(1390, 135, 222, 45))
        img = cv2.imread("turn.png")
        who = cv2.imread("white_turn.png")
        diff = cv2.subtract(img, who)
        #print(np.sum(diff**2))
        total = np.sum(diff**2)
        if total < 300000 and total != 0:
            return "w"
        else:
            return "b"
    else:
        return "w"

def find_fen(game, who, castling, fish, increase):
    #s = time.time()
    fen = [[], [], [], [], [], [], [], []]
    #fen_str = ""
    c = 0
    pieces = ["wpw", "wnw", "wbw", "wqw", "wkw", "wrw", "bpw", "bnw", "bbw", "bqw", "bkw", "brw", "wpb", "wnb", "wbb", "wqb", "wkb", "wrb", "bpb", "bnb", "bbb", "bqb", "bkb", "brb"]
    for y in range(8):
        for x in range(8):
            img = pyautogui.screenshot(r"c:\Users\kiss1\PycharmProjects\Automation\Chess_player\screenshot.png", region=(353 + 108 * x, 119 + 108 * y, 108, 108))
            img = cv2.imread("screenshot.png")
            for i in pieces:
                piece = cv2.imread("{}.png".format(i))
                diff = cv2.subtract(img, piece)
                diff2 = cv2.subtract(piece, img)
                print(np.sum(diff**2), np.sum(diff2**2), i, x ,y)
                if np.sum(diff**2) < 5000 and np.sum(diff2**2) < 7000 + increase:
                    if i[:2] == "wk" and (x != 4 or y != 7):
                        castling["wk"] = ""
                        castling["wq"] = ""
                    if i[:2] == "wr" and (x != 7 or y != 7):
                        castling["wk"] = ""
                    if i[:2] == "wr" and (x != 0 or y != 7):
                        castling["wq"] = ""
                    if i[:2] == "bk" and (x != 4 or y != 0):
                        castling["bk"] = ""
                        castling["bq"] = ""
                    if i[:2] == "br" and (x != 7 or y != 0):
                        castling["bk"] = ""
                    if i[:2] == "br" and (x != 0 or y != 0):
                        castling["bq"] = ""
                    if c > 0:
                        fen[y].append(str(c))
                        c = 0
                    if i[0] == "w":
                        fen[y].append(i[1].capitalize())
                    else:
                        fen[y].append(i[1])
                    break
            else:
                c = c + 1
        if c > 0:
            fen[y].append(str(c))
            c = 0
    #print(castling, fen)
    fen = "/".join(["".join(x) for x in fen])
    final_fen = "{} {} ".format(fen, who)
    final_fen = final_fen + castling["wk"] + castling["wq"] + castling["bk"] + castling["bq"]
    final_fen = " {} - 0 0".format(final_fen, who)
    return castling, final_fen
    #if fish.is_fen_valid(final_fen):
        #return castling, final_fen
    #else:
        #return find_fen(game, who, castling, fish, increase+1000)
    #print(time.time() - s, fen)

def make_move(best_move, turn):
    #print(best_move)
    pyautogui.moveTo((column[best_move[0]] - 1) * 108 + 375, (8 - int(best_move[1])) * 108 + 150)
    pyautogui.click()
    pyautogui.moveTo((column[best_move[2]] - 1) * 108 + 375, (8 - int(best_move[3])) * 108 + 150)
    pyautogui.click()
    pyautogui.click()
    pyautogui.moveTo(197, 968)
    pyautogui.click()
def load_game():
    pyautogui.moveTo(400, 1066)
    pyautogui.click()

#time.sleep(2)
#img = pyautogui.screenshot(r"c:\Users\kiss1\PycharmProjects\Automation\Chess_player\screenshot.png", region = (288+108*3, 119+108*6, 108, 108))
#img.save(r"c:\Users\kiss1\PycharmProjects\Automation\Chess_player\brw.png")
#img.save(r"c:\Users\kiss1\PycharmProjects\Automation\Chess_player")
#who = turn(True)
#castling, final_fen = find_fen("f", who, castling)
#print(final_fen)

# img = pyautogui.screenshot(r"c:\Users\kiss1\PycharmProjects\Automation\Chess_player\screenshot.png", region=(288+108*7, 119+108*7, 108, 108))
# img = cv2.imread("screenshot.png")
# piece = cv2.imread("brw.png")
# diff = cv2.subtract(img, piece)
# result = not np.any(diff)
# #print(diff)
# if result is True:
#     print(img)
#     print("Yay")
# else:
#     print(img)
#     print("AAAAA")
#     print(piece)
#     print(np.sum(diff**2))
#     cv2.imshow("gf", diff)
#     cv2.imshow("gfg", img)
#     cv2.imshow("gff", piece)
#     cv2.waitKey(-1)
# print("trhgrhgrthtyhty")
        #print(i, loc)


    # wp = cv2.imread("wp.png")
    # bp = cv2.imread("bp.png")
    # wr = cv2.imread("wr.png")
    # br = cv2.imread("br.png")
    # wn = cv2.imread("wn.png")
    # bn = cv2.imread("bn.png")
    # wb = cv2.imread("wb.png")
    # bb = cv2.imread("bb.png")
    # wq = cv2.imread("wq.png")
    # bq = cv2.imread("bq.png")
    # wk = cv2.imread("wk.png")
    # bk = cv2.imread("bk.png")
fish = Stockfish(path=r"\Users\kiss1\PycharmProjects\Automation\Chess_player\stockfish-windows-2022-x86-64-avx2.exe", depth = 18, parameters = {"Threads": 3, "Minimum Thinking Time": 3})
castling = {"wk": "K", "bk": "k", "wq":"Q", "bq":"q"}
load_game()
time.sleep(2)
while True:
    #castling = {"wk": "K", "bk": "k", "wq":"Q", "bq":"q"}
    t = turn(True)
    castling, final_fen = find_fen("f", t, castling, fish, 100000000)
    print(final_fen)
    #print(final_fen)
    try:
        fish.set_fen_position(final_fen)
            #print(fish.get_best_move())
        make_move(fish.get_best_move(), t)
    except stockfish.models.StockfishException:
        pass
    time.sleep(3)
#game = cv2.imread("Bqueen.png", 0)
#pos = []
#pos = find_fen(game)
#print(pos)
#w, h = 75, 75
#print(w, h)
#for i in pos:
    #for i2 in zip(*i[::-1]):
        #print(i)
        #cv2.rectangle(game, i2, (i2[0] + w, i2[1] + h),(0, 255, 255), 2)
#cv2.imshow("game",game)
#cv2.waitKey(-1)