# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define role = Character("诺缇蕾雅")

# 需要用到的经过缩放后的背景图
image gate = im.Scale("images/bg/城门5.jpg", 1920, 1080) #根据你的分辨率调整
image burnning_city = im.Scale("images/bg/火烧城市9.png", 1920, 1080) #根据你的分辨率调整
# image role stable = "images/差分/8_npc_.png"
image role stable = im.Scale("images/差分/1_女主差分/1_女主_差分_普通.png", 352,951)
 


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    # 进入序章世界观介绍 背景为纯黑
    scene black
    stop music fadeout 1.0
    "djiajdia"

    "dasda"
    # 序章 燃烧的城市
    scene burnning_city

    play music "bgm/1.序章BGM.mp3" # fadeout 1.0 fadein 1.0

    play sound "audio/效果音/环境音/1.大火灼烧效果音.mp3" volume 0.5

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show "images/差分/1_女主差分/1_女主_差分_普通.png"
    show role stable at Position(xalign=0.3, yalign=1.0)

    # 此处显示各行对话。

    role "您已创建一个新的 Ren'Py 游戏。"

    role "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
