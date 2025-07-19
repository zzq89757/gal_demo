import json

# 读取原始JSON
with open(r"E:\Ren\first_project\gal_demo\game\tl\Raw\xuzhang_1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

sentences = data.get("sentence", [])
text_li = []
# 写入列表
for entry in sentences:
    role = entry.get("name_zh_cn", "").strip()
    text = entry.get("text_zh_cn", "").strip()
    if text:
        text_li.append((role, text))
