import json

def json2li(json_file: str) -> list:
    # 读取原始JSON
    # with open(r"E:\Ren\first_project\gal_demo\game\tl\Raw\xuzhang_1.json", "r", encoding="utf-8") as f:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = data.get("sentence", [])
    text_li = []
    # 写入列表
    for entry in sentences:
        role = entry.get("name_zh_cn", "").strip()
        text = entry.get("text_zh_cn", "").strip()
        if text:
            text_li.append((role, text))
    return text_li

prologue_text_li = json2li(r"E:\Ren\first_project\gal_demo\game\tl\Raw\xuzhang_1.json")

selection_0_1_text_li = json2li(r"E:\Ren\first_project\gal_demo\game\tl\Raw\fenzhi0_1.json")

charpter1_text_li = json2li(r"E:\Ren\first_project\gal_demo\game\tl\Raw\zhangjie_1.json")


print(charpter1_text_li)