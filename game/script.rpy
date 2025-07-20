# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define role = Character("诺缇蕾雅")

# 需要用到的经过缩放后的背景图和立绘
image forest = im.Scale("images/bg/森林1.jpg", 1920, 1080) #根据你的分辨率调整
image plain = im.Scale("images/bg/平原2.jpg", 1920, 1080) #根据你的分辨率调整
image village = im.Scale("images/bg/小乡村3.jpg", 1920, 1080) #根据你的分辨率调整
image urben = im.Scale("images/bg/城市4.jpg", 1920, 1080) #根据你的分辨率调整
image gate = im.Scale("images/bg/城门5.jpg", 1920, 1080) #根据你的分辨率调整
image river = im.Scale("images/bg/小溪6.jpg", 1920, 1080) #根据你的分辨率调整
image ruin = im.Scale("images/bg/废墟7.jpg", 1920, 1080) #根据你的分辨率调整
image stone_road = im.Scale("images/bg/石头路8.jpg", 1920, 1080) #根据你的分辨率调整
image burnning_city = im.Scale("images/bg/火烧城市9.png", 1920, 1080) #根据你的分辨率调整
image town = im.Scale("images/bg/市区10.jpg", 1920, 1080) #根据你的分辨率调整
image urben night = im.Scale("images/bg/市区11.jpg", 1920, 1080) #根据你的分辨率调整
image room night = im.Scale("images/bg/室内 晚上12.jpg", 1920, 1080) #根据你的分辨率调整
image room = im.Scale("images/bg/室内 白天13.jpg", 1920, 1080) #根据你的分辨率调整
# image role stable = "images/差分/8_npc_.png"

image role stable = Transform("images/差分/1_女主差分/1_女主_差分_普通.png", zoom=0.18)

image angle close eye = Transform("images/差分/2_天使差分/2_天使_差分_闭眼.png", zoom=0.18)

image angle plain = Transform("images/差分/2_天使差分/2_天使_差分_普通.png", zoom=0.18)

image rider plain = Transform("images/差分/5_骑士差分/5_骑士_差分_普通.png", zoom=0.18)

init python:
    import json

    def json2li(json_file: str) -> list:
        # 读取原始JSON
        # with open("/tl/Raw/xuzhang_1.json", "", encoding="utf-8") as f:
        # with open(json_file, "", encoding="utf-8") as f:
        with renpy.loader.load(json_file) as f:
            data = json.load(f)

        sentences = data.get("sentence", [])
        text_li = []
        # 写入列表
        for entry in sentences:
            role = entry.get("name_zh_cn", "").strip()
            text = entry.get("text_zh_cn", "").strip()
            bg = entry.get("backGround", "")
            bgm = entry.get("bgm", "")
            bgs = entry.get("bgs", "")
            se = entry.get("se", "")
            is_hide_text = entry.get("hiddenText", "")
            is_menu = entry.get("choose", "")
            char_info = []
            for i in range(1,7):
                ch_show, ch_pos = entry.get(f"character_{i}", "")
                ch_move = entry.get(f"character_{i}_Move", "")
                ch_act = entry.get(f"character_{i}_Action", "")
                char_info.append([ch_show, ch_pos, ch_move[0], ch_act[0]])
            if text:
                text_li.append((role, text, [bg, bgm, bgs, se], char_info, is_menu, is_hide_text))
        return text_li

    prologue_text_li = json2li("/tl/Raw/xuzhang_1.json")

    selection_0_1_text_li = json2li("/tl/Raw/fenzhi0_1.json")

    charpter1_text_li = json2li("/tl/Raw/zhangjie_1.json")

    selection_1_1_text_li = json2li("/tl/Raw/fenzhi1_1.json")

    selection_1_2_text_li = json2li("/tl/Raw/fenzhi1_2.json")

    selection_1_3_text_li = json2li("/tl/Raw/fenzhi1_3.json")

    selection_2_1_text_li = json2li("/tl/Raw/fenzhi2_1 +-.json")

    selection_2_2_text_li = json2li("/tl/Raw/fenzhi2_2 +.json")

    selection_2_3_text_li = json2li("/tl/Raw/fenzhi2_3 -.json")

    charpter2_text_li = json2li("/tl/Raw/zhangjie_2.json")

label start:
    # scene burnning_city
    scene black
    # $ renpy.show("burnning_city")
    # $ renpy.music.play("bgm/1.序章BGM.mp3", channel='music', fadein=1.0, if_changed=True)
    python:
        bg_li = ["black", "forest","plain", "village", "urben", "gate", "river", "ruin", "stone_road", "burnning_city", "town", "urben night", "room night", "room"]
        bgm_li = [None] + sorted([f for f in renpy.list_files() if f.startswith("audio/bgm") and f.endswith(".mp3")],key=lambda x:int(x.split("/")[-1].split(".")[0]))[1:]
        bgs_li = [None] + sorted([f for f in renpy.list_files() if f.startswith("audio/bgs") and f.endswith(".mp3")],key=lambda x:int(x.split("/")[-1].split(".")[0]))
        se_li = [None] + sorted([f for f in renpy.list_files() if f.startswith("audio/se") and f.endswith(".mp3")],key=lambda x:int(x.split("/")[-1].split(".")[0]))
        print(bgm_li)
        current_bgm_idx = None
        current_bgs_idx = None
        current_bg_idx = None
        current_se_idx = None
        renpy.music.stop(fadeout=1.0)
        for role, text, bg_idx_li, char_info, is_menu, is_hide_text in charpter1_text_li:

            bg_idx, bgm_idx, bgs_idx, se_idx = bg_idx_li

            # 背景
            if bg_idx != current_bg_idx:
                bg_name = bg_li[bg_idx]
                current_bg_idx = bg_idx
                renpy.scene()
                renpy.show(bg_name)
                renpy.with_statement(fade, always=False)
                current_bg_idx = bg_idx

            # # BGM
            if bgm_idx != current_bgm_idx:
                bgm = bgm_li[bgm_idx]
                # renpy.music.stop(fadeout=1.0)
                renpy.music.play(bgm, fadein=1.0, loop=True)
                # renpy.music.play("bgm/1.序章BGM.mp3", fadein=1.0)
                current_bgm_idx = bgm_idx
            # # 音效
            if bgs_idx != 0 and bgs_idx != current_bgs_idx:
                bgs = bgs_li[bgs_idx]
                renpy.music.play(bgs, channel = "sound", fadein=1.0)
                # renpy.music.play("bgm/1.序章BGM.mp3", fadein=1.0)
                current_bgs_idx = bgs_idx
            if bgs_idx == 0 and current_bgs_idx != 0:
                renpy.music.stop(channel = "sound", fadeout=1.0)
                current_bgs_idx = bgs_idx
            # # se
            if se_idx != 0 and se_idx != current_se_idx:
                se = se_li[se_idx]
                renpy.music.play(se, channel = "sound", fadein=1.0)
                # renpy.music.play("bgm/1.序章BGM.mp3", fadein=1.0)
                current_se_idx = se_idx
            if se_idx == 0 and current_se_idx != 0:
                renpy.music.stop(channel = "sound", fadeout=1.0)
                current_se_idx = se_idx

            # # 角色
            # if char_info and char_info[0]:
            #     ch_show, ch_pos, ch_move, ch_act = char_info
            #     renpy.show(ch_show, at_list=[])

            for ch in char_info:
                for i in range(6):
                    ch_show, ch_pos, ch_move, ch_act = ch[i]
                    if ch_show == 0:continue
                    # 渲染立绘 解析位置动作等


            # 显示对话
            if role:
                renpy.say(role, text)
            else:
                renpy.say(None, text)

    return

# 游戏在此开始。
# label start:
#     # 进入序章世界观介绍 背景为纯黑 仅旁白 无角色发言
#     scene black
#     stop music fadeout 1.0

#     ############################## 序章 燃烧的城市
#     $ idx = 0

#     while idx < len(prologue_text_li):
#         $ name, sentence, bg_info, char_info = prologue_text_li[idx]

#         # 引入火焰音效
#         if idx == 3:
#             play sound "audio/效果音/环境音/1.大火灼烧效果音.mp3" volume 0.8 fadein 1.0 loop
#         # 燃烧的城市   
#         if idx == 11:
#             scene burnning_city with dissolve
#         # bgm in
#         if idx == 16:
#             play music "bgm/1.序章BGM.mp3" fadein 1.0 # fadeout 1.0 fadein 1.0
#         # selection
#         if idx == 58:
#             menu:
#                 # 引入分支0_1文本
#                 "求求你救救我！":
#                     $ j = 0
#                     while j < len(selection_0_1_text_li):
#                         $ name_s, sentence_s = selection_0_1_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1

#         "[name]" "[sentence]"

#         if idx == len(prologue_text_li) - 1:
#             # 背景淡出
#             scene black with dissolve
#             stop sound
#             pass


#         $ idx += 1

#     ###################################### 第一章
#     $ idx = 0
#     while idx < len(charpter1_text_li):
#         $ name, sentence, bg_info, char_info = charpter1_text_li[idx]
#         # 背景跳转至森林 引入bgm
#         if idx == 1:
#             scene forest with dissolve
#             play music "bgm/22.战斗曲.mp3" fadein 1.0 # fadeout 1.0 fadein 1.0
#         "[name]" "[sentence]"
#         # 女主立绘出现
#         if idx == 2:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 3:
#             hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         # if idx == 10:
#         #     play music "bgm/1.序章BGM.mp3"  fadein 1.0
#         if idx == 14:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 16:
#             hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 17:
#             play sound "audio/效果音/环境音/2.拨开草丛.mp3" volume 0.8 fadein 1.0
#             play sound "audio/效果音/环境音/4.走过草丛的音效.mp3" volume 0.8 fadein 1.0 loop
#         if idx == 19:
#             stop sound 
#         if idx == 27:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 28:
#             hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 43:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#             play sound "audio/效果音/环境音/4.走过草丛的音效.mp3" volume 0.8 fadein 1.0 loop
#         if idx == 45:
#             hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#             stop sound
#         if idx == 49:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 50:
#             hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 51:
#             play sound "audio/效果音/环境音/2.拨开草丛.mp3" volume 0.8 fadein 1.0
#         if idx == 52:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#             stop sound
#             stop music fadeout 0.5
#         if idx == 53:
#             hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 54:
#             play sound "audio/效果音/环境音/4.走过草丛的音效.mp3" volume 0.8 fadein 1.0 loop
#         if idx == 55:
#             stop sound
#         if idx == 57:
#             show angle close eye at Position(xpos=0.5,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 58:
#             show angle close eye at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 59:
#             hide angle close eye at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             hide role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#             show angle plain at Position(xpos=0.5,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 60:
#             hide angle plain at Position(xpos=0.5,ypos=0.2,xanchor=0.5,yanchor=0)
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
#         if idx == 61:
#             # 女主立绘向右移动 天使立绘抖动
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset 340
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0):
#                 linear 0.03 xoffset -120
#                 linear 0.03 xoffset 120
#                 repeat 6
#         if idx == 62:
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset 0
#         if idx == 78:
#             menu:
#                 "......":
#                     $ j = 0
#                     while j < len(selection_1_1_text_li):
#                         $ name_s, sentence_s = selection_1_1_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1
#                 "......滚":
#                     $ j = 0
#                     while j < len(selection_1_2_text_li):
#                         $ name_s, sentence_s = selection_1_2_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1
#                 "(挥剑示意)":
#                     $ j = 0
#                     while j < len(selection_1_3_text_li):
#                         $ name_s, sentence_s = selection_1_3_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1
#         if idx == 93:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset -340
#         if idx == 94:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset 0
#         if idx == 122:
#             scene gate
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 123:
#             menu:
#                 "(继续不理她)":
#                     $ j = 0
#                     while j < len(selection_2_1_text_li):
#                         $ name_s, sentence_s = selection_2_1_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1
#                 "(提醒让她隐藏光环)":
#                     $ j = 0
#                     while j < len(selection_2_2_text_li):
#                         $ name_s, sentence_s = selection_2_2_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1
#                 "(用刀指向她)":
#                     $ j = 0
#                     while j < len(selection_2_3_text_li):
#                         $ name_s, sentence_s = selection_2_3_text_li[j]
#                         "[name_s]" "[sentence_s]"
#                         $ j += 1
#         if idx == 124:
#             scene room night
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 125:
#             scene urben night
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 126:
#             scene room night
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         $idx += 1

#     ############# 第二章
#     scene room night
#     $ idx = 0
#     while idx < len(charpter2_text_li):
#         $ name, sentence, bg_info, char_info = charpter2_text_li[idx]
#         if idx == 1:
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 2:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#         if idx == 3:
#             show angle plain at Position(xpos=0.5,ypos=0.2,xanchor=0.5,yanchor=0)
#             hide role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)

#         if idx == 5:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)

#         if idx == 9:
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)

#         if idx == 12:
#             scene urben
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 13:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset -740
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset 720
#         if idx == 15:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset 0
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset 0
#         if idx == 20:
#             scene plain
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 27:
#             scene town
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
#         if idx == 43:
#             hide angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0)

#         if idx == 55:
#             show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0):
#                 linear 0.3 xoffset -740
#         if idx == 56:
#             show angle plain at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
#         if idx == 67:
#             hide angle plain
#             hide role stable
#             show rider plain at Position(xpos=0.5,ypos=0.1,xanchor=0.5,yanchor=0)
#         "[name]" "[idx][sentence]"
#         $idx += 1
#     # 显示角色立绘
    

#     # 此处为游戏结尾。
#     role "试玩结束"
#     role "......"
#     return
