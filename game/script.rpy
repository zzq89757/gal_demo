# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define role = Character("诺缇蕾雅")

# 需要用到的经过缩放后的背景图和立绘
image gate = im.Scale("images/bg/城门5.jpg", 1920, 1080) #根据你的分辨率调整
image burnning_city = im.Scale("images/bg/火烧城市9.png", 1920, 1080) #根据你的分辨率调整
# image role stable = "images/差分/8_npc_.png"
image role stable = im.Scale("images/差分/1_女主差分/1_女主_差分_普通.png", 352,951)

init python:
    from process_text import text_li



# 游戏在此开始。
label start:
    # 进入序章世界观介绍 背景为纯黑 仅旁白 无角色发言
    scene black
    stop music fadeout 1.0
    # python:
    #     for role, text in text_li:
    #         renpy.say(role, text)        # 显示文本

    # 序章 燃烧的城市
    $ idx = 0

    while idx < len(text_li):
        $ name, sentence = text_li[idx]

        # 引入火焰音效
        if idx == 3:
            play sound "audio/效果音/环境音/1.大火灼烧效果音.mp3" volume 0.8 fadein 1.0
        # 燃烧的城市   
        if idx == 11:
            scene burnning_city with dissolve
        # bgm in
        if idx == 16:
            play music "bgm/1.序章BGM.mp3" # fadeout 1.0 fadein 1.0
        # selection
        if idx == 58:
            menu:
                # 引入分支0_1文本
                "求求你救救我！":
                    stop music fadeout 1.0

        "[name]" "[sentence]"

        if idx == len(text_li) - 1:
            # 背景淡出
            pass


        $ idx += 1

    
    


    # 显示角色立绘
    
    show role stable at Position(xalign=0.3, yalign=1.0)

    # 此处显示各行对话。

    role "您已创建一个新的 Ren'Py 游戏。"

    role "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
