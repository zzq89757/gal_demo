# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define role = Character("诺缇蕾雅")

# 需要用到的经过缩放后的背景图和立绘
image gate = im.Scale("images/bg/城门5.jpg", 1920, 1080) #根据你的分辨率调整
image burnning_city = im.Scale("images/bg/火烧城市9.png", 1920, 1080) #根据你的分辨率调整
image forest = im.Scale("images/bg/森林1.jpg", 1920, 1080) #根据你的分辨率调整
# image role stable = "images/差分/8_npc_.png"
image role stable = im.Scale("images/差分/1_女主差分/1_女主_差分_普通.png", 700,1900)
image angle close eye = im.Scale("images/差分/2_天使差分/2_天使_差分_闭眼.png", 1200,1900)

init python:
    from process_text import *



# 游戏在此开始。
label start:
    # 进入序章世界观介绍 背景为纯黑 仅旁白 无角色发言
    scene black
    stop music fadeout 1.0

    ############################## 序章 燃烧的城市
    $ idx = 0

    while idx < len(prologue_text_li):
        $ name, sentence = prologue_text_li[idx]

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
                # 停止BGN 引入分支0_1文本
                "求求你救救我！":
                    stop music fadeout 1.0
                    $ j = 0
                    while j < len(selection_0_1_text_li):
                        $ name_s, sentence_s = selection_0_1_text_li[j]
                        "[name_s]" "[sentence_s]"
                        $ j += 1

        "[name]" "[sentence]"

        if idx == len(prologue_text_li) - 1:
            # 背景淡出
            scene black with dissolve
            pass


        $ idx += 1

    ###################################### 第一章
    $ idx = 0
    while idx < len(charpter1_text_li):
        $ name, sentence = charpter1_text_li[idx]
        # 背景跳转至森林 引入bgm
        if idx == 1:
            scene forest with dissolve
            play music "bgm/22.战斗曲.mp3" # fadeout 1.0 fadein 1.0
        "[name]" "[idx][sentence]"
        # 女主立绘出现
        if idx == 2:
            show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 3:
            hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 10:
            play music "bgm/1.序章BGM.mp3"  fadein 1.0
        if idx == 14:
            show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 16:
            hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 17:
            play sound "audio/效果音/环境音/2.拨开草丛.mp3" volume 0.8 fadein 1.0
            play sound "audio/效果音/环境音/4.走过草丛的音效.mp3" volume 0.8 fadein 1.0 loop
        if idx == 19:
            stop sound
        if idx == 27:
            show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 28:
            hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 43:
            show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
            play sound "audio/效果音/环境音/4.走过草丛的音效.mp3" volume 0.8 fadein 1.0 loop
        if idx == 45:
            hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
            stop sound
        if idx == 49:
            show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 50:
            hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 51:
            play sound "audio/效果音/环境音/2.拨开草丛.mp3" volume 0.8 fadein 1.0 loop
        if idx == 52:
            show role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 53:
            hide role stable at Position(xpos=0.5,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 54:
            play sound "audio/效果音/环境音/4.走过草丛的音效.mp3" volume 0.8 fadein 1.0 loop
        if idx == 55:
            stop sound
        if idx == 57:
            show angle close eye at Position(xpos=0.5,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 58:
            show angle close eye at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
            show role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0) with dissolve
        if idx == 59:
            hide angle close eye at Position(xpos=0.9,ypos=0.2,xanchor=0.5,yanchor=0)
            hide role stable at Position(xpos=0.12,ypos=-0.2,xanchor=0.5,yanchor=0)
            show angle close eye at Position(xpos=0.5,ypos=0.2,xanchor=0.5,yanchor=0) with dissolve
            
        $idx += 1

    # 显示角色立绘
    
    # show role stable at Position(xalign=0.3, yalign=1.0)

    # 此处为游戏结尾。

    return
