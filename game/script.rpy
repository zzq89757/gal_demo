# 游戏的脚本可置于此文件中。
transform pos_1(y=0):
    xalign 0.15
    yalign 0.5
    xanchor 0.5
    yanchor 0.4
    yoffset y


transform pos_2(y=0):
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.4
    yoffset y


transform pos_3(y=0):
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.4
    yoffset y


transform pos_4(y=0):
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.4
    yoffset y


transform pos_5(y=0):
    xalign 0.85
    yalign 0.5
    xanchor 0.5
    yanchor 0.4
    yoffset y

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
# define role = Character("诺缇蕾雅")

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
image role unhappy = Transform("images/差分/1_女主差分/1_女主_差分_不高兴.png", zoom=0.18)
image role anger = Transform("images/差分/1_女主差分/1_女主_差分_愤怒.png", zoom=0.18)
image role happy = Transform("images/差分/1_女主差分/1_女主_差分_开心.png", zoom=0.18)
image role sad = Transform("images/差分/1_女主差分/1_女主_差分_伤心.png", zoom=0.18)
image role hurt = Transform("images/差分/1_女主差分/1_女主_差分_战损.png", zoom=0.18)
image role open_mouth = Transform("images/差分/1_女主差分/1_女主_差分_张嘴.png", zoom=0.18)


image angel stable = Transform("images/差分/2_天使差分/2_天使_差分_普通.png", zoom=0.16)
image angel close_eye = Transform("images/差分/2_天使差分/2_天使_差分_闭眼.png", zoom=0.16)
image angel happy = Transform("images/差分/2_天使差分/2_天使_差分_笑.png", zoom=0.16)
image angel sad = Transform("images/差分/2_天使差分/2_天使_差分_伤心.png", zoom=0.16)
image angel none = Transform("images/差分/2_天使差分/2_天使_差分_面无表情.png", zoom=0.16)
image angel anger = Transform("images/差分/2_天使差分/2_天使_差分_生气.png", zoom=0.16)
image angel hurt = Transform("images/差分/2_天使差分/2_天使_差分_战损.png", zoom=0.16)


image dead stable = Transform("images/差分/3_死神差分/3_死神_差分_普通.png", zoom=0.16)
image dead dumb = Transform("images/差分/3_死神差分/2_死神_差分_呆.png", zoom=0.16)
image dead happy = Transform("images/差分/3_死神差分/3_死神_差分_开心.png", zoom=0.16)
image dead unhappy = Transform("images/差分/3_死神差分/3_死神_差分_不开心.png", zoom=0.16)
image dead series = Transform("images/差分/3_死神差分/3_死神_差分_严肃.png", zoom=0.16)
image dead anger = Transform("images/差分/3_死神差分/3_死神_差分_生气.png", zoom=0.16)
image dead hurt = Transform("images/差分/3_死神差分/3_死神_差分_战损.png", zoom=0.16)


image rider stable = Transform("images/差分/5_骑士差分/5_骑士_差分_普通.png", zoom=0.14)
image rider iijanai = Transform("images/差分/5_骑士差分/5_骑士_差分_不也挺好的吗.png", zoom=0.14)
image rider power = Transform("images/差分/5_骑士差分/5_骑士_差分_斗志满满.png", zoom=0.14)
image rider open_mouth = Transform("images/差分/5_骑士差分/5_骑士_差分_张嘴.png", zoom=0.14)
image rider anger = Transform("images/差分/5_骑士差分/5_骑士_差分_生气.png", zoom=0.14)
image rider another_type = Transform("images/差分/5_骑士差分/5_骑士_差分_生气.png", zoom=0.14)


image boss_npc homo = Transform("images/差分/7_boss/7_boss_人形.png", zoom=0.2)
image boss_npc raw = Transform("images/差分/7_boss/7_boss_怪物.png", zoom=0.2)
image boss_npc np6 = Transform("images/差分/8_npc_.png", zoom=0.14)

image sister stable = Transform("images/差分/6_妹妹差分/6_妹妹_差分_普通.png", zoom=0.14)
image sister happy = Transform("images/差分/6_妹妹差分/6_妹妹_差分_开心.png", zoom=0.14)
image sister unhappy = Transform("images/差分/6_妹妹差分/6_妹妹_差分_伤心.png", zoom=0.14)
image sister mask = Transform("images/差分/6_妹妹差分/6_妹妹_差分_面具.png", zoom=0.14)
image sister anger = Transform("images/差分/6_妹妹差分/6_妹妹_差分_普通_生气.png", zoom=0.14)
image sister sad = Transform("images/差分/6_妹妹差分/6_妹妹_差分_失落.png", zoom=0.14)

init python:
    position_dict = {
        1: pos_1,
        2: pos_2,
        3: pos_3,
        4: pos_4,
        5: pos_5,
    }
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

    selection_3_1_text_li = json2li("/tl/Raw/fenzhi3_1+-.json")

    selection_3_2_text_li = json2li("/tl/Raw/fenzhi3_2-.json")

    selection_3_3_text_li = json2li("/tl/Raw/fenzhi3_3+.json")

    selection_4_1_text_li = json2li("/tl/Raw/fenzhi4_1+-.json")

    selection_4_2_text_li = json2li("/tl/Raw/fenzhi4_2+.json")

    selection_4_3_text_li = json2li("/tl/Raw/fenzhi4_3-.json")

    selection_5_1_text_li = json2li("/tl/Raw/fenzhi5_1+-.json")

    selection_5_2_text_li = json2li("/tl/Raw/fenzhi5_2+.json")

    selection_5_3_text_li = json2li("/tl/Raw/fenzhi5_3-.json")

    selection_6_1_text_li = json2li("/tl/Raw/fenzhi6_1++.json")

    selection_6_2_text_li = json2li("/tl/Raw/fenzhi6_2--.json")

    selection_6_3_text_li = json2li("/tl/Raw/fenzhi6_3+.json")

    selection_7_1_text_li = json2li("/tl/Raw/fenzhi 7_1++.json")

    selection_7_2_text_li = json2li("/tl/Raw/fenzhi 7_2-.json")

    selection_7_3_text_li = json2li("/tl/Raw/fenzhi 7_3+.json")

    selection_8_1_text_li = json2li("/tl/Raw/fenzhi 8_1 +.json")

    selection_8_2_text_li = json2li("/tl/Raw/fenzhi 8_2 +-.json")

    selection_8_3_text_li = json2li("/tl/Raw/fenzhi 8_3 -.json")

    charpter2_text_li = json2li("/tl/Raw/zhangjie_2.json")


    charpter3_text_li = json2li("/tl/Raw/zhangjie_3.json")


    charpter4_text_li = json2li("/tl/Raw/zhangjie_4.json")


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
        role_name_li = ["role", "angel", "dead", "empire", "rider", "boss_npc", "sister"]
        yoffset_dict = {
            "role":100, "angel":200, "dead":100, "empire":0, "rider":200, "boss_npc":0, "sister":0
        }
        role_shown_li = [0] * 6
        role_expressions_dict = {"role": [
            None, "stable", "open_mouth", "happy",
            "unhappy", "sad", "anger", "hurt"
            ]
        ,"angel": [
            None, "stable", "close_eye", "happy",
            "sad", "none", "anger", "hurt"
        ],"dead":[
            None, "stable", "dumb", "happy", "series", "unhappy", "anger", "hurt"
        ],"rider":
        [None, "stable", "iijanai", "power", "open_mouth", "power", "anger", "another_type"
        ],"sister":[
            None, "mask", "mask", ""
        ],"boss_npc":[
            None, "homo", "raw", "npc"
        ]

        }

        menu_dict = {"prologue":[
            [
                ("求求你救救我！", selection_0_1_text_li)
            ],
        ],
        "charpter1":[
            [("......", selection_1_1_text_li),
            ("......滚", selection_1_2_text_li),
            ("(挥剑示意)", selection_1_3_text_li)]
        ,
            [("(继续不理她)", selection_2_1_text_li),
            ("(提醒让她隐藏光环)", selection_2_2_text_li),
            ("(用刀指向她)", selection_2_3_text_li)]
        ],
        "charpter2":[
            [("(捂住她的嘴)", selection_3_1_text_li),
            ("(仍由她询问下去)", selection_3_2_text_li),
            ("(妳就当没听见算了)", selection_3_3_text_li)]
        ,
            [("(按住阿希蕾尔的头)", selection_4_1_text_li),
            ("(按住两人的头)", selection_4_2_text_li),
            ("(直接走出去)", selection_4_3_text_li)]
        ,
            [("......", selection_5_1_text_li),
            ("我叫......", selection_5_2_text_li),
            ("(继续举起刀)", selection_5_3_text_li)]
        ],
        "charpter3":[
            [("(决定去找人)", selection_6_1_text_li),
            ("(那女孩和我无关)", selection_6_2_text_li),
            ("(那妳们去找她吧)", selection_6_3_text_li)]
        ,
            [("(摸摸她的头)", selection_7_1_text_li),
            ("(沉默不语)", selection_7_2_text_li),
            ("(妳为什么要乱跑)", selection_7_3_text_li)]
            
        ],
        "charpter4":[
            [("(伸手护住阿希蕾尔)", selection_8_1_text_li),
            ("(准备拔刀)", selection_8_2_text_li),
            ("(询问对方身份)", selection_8_3_text_li)]
        ],
        }

        renpy.music.stop(fadeout=1.0)

        def run(text_li,menu_li=[]) -> None:
            menu_idx = 0
            current_bgm_idx = None
            current_bgs_idx = None
            current_bg_idx = None
            current_se_idx = None
            for role, text, bg_idx_li, char_info, is_menu, is_hide_text in text_li:

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
                for i in range(6):
                    ch_show, ch_pos, ch_move, ch_act = char_info[i]
                    role_name = role_name_li[i]
                    if ch_pos == 0 and ch_show != 0:
                        ch_show = 0
                    # 由出现到隐藏
                    if role_shown_li[i] != 0 and ch_show == 0:
                        e_motion = role_expressions_dict[role_name][ch_show]
                        renpy.hide(f"{role_name} {e_motion}")
                        role_shown_li[i] = ch_show
                    if ch_show != 0:
                        e_motion = role_expressions_dict[role_name][ch_show]
                        # 渲染立绘 解析位置动作等
                        renpy.show(f"{role_name} {e_motion}", at_list=[position_dict[ch_pos](yoffset_dict[role_name])])
                        role_shown_li[i] = ch_show
                # 菜单
                if is_menu:
                    choice_list = menu_li[menu_idx]  # 这是列表：多组 (选项文本, 剧情)

                    menu_items = [(choice_text, idx) for idx, (choice_text, _) in enumerate(choice_list)]

                    choice_idx = renpy.display_menu(menu_items)

                    _, inner_text_li = choice_list[choice_idx]

                    run(inner_text_li)  # 玩家选中后再进入支线

                    menu_idx += 1
                    # run_li=[]
                    # for sele in menu_li[menu_idx]:
                    #     choice_text, inner_text_li = sele
                    #     run_li.append((choice_text, run(inner_text_li)))
                    # choice = renpy.display_menu(run_li)
                    # renpy.say(None, f"你选择了 {choice}")
                    # menu_idx += 1

                # 显示对话
                if role:
                    renpy.say(role, text)
                else:
                    renpy.say(None, text)
        # run(prologue_text_li,menu_dict["prologue"])
        run(charpter1_text_li,menu_dict["charpter1"])
        run(charpter2_text_li,menu_dict["charpter2"])
        run(charpter3_text_li,menu_dict["charpter3"])
        run(charpter4_text_li,menu_dict["charpter4"])
        # run(charpter4_text_li)


    return
    

#     # 此处为游戏结尾。
#     role "试玩结束"
#     role "......"
#     return
