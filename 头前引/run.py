import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, "test.html")

gif_i = 1
png_i = 1

def repl_gif(match):
    global gif_i
    suffix = match.group("q") or ""   # 形如 ?xxx
    out = f'src="./images/{gif_i}.GIF{suffix}"'  # ✅ suffix 在引号内
    gif_i += 1
    return out

def repl_png(match):
    global png_i
    suffix = match.group("q") or ""
    out = f'src="./images/{png_i}.PNG{suffix}"'  # ✅ suffix 在引号内
    png_i += 1
    return out

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

gif_pattern = r'src="\./images/\.GIF(?P<q>\?[^"]*)?"'
png_pattern = r'src="\./images/\.PNG(?P<q>\?[^"]*)?"'

content = re.sub(gif_pattern, repl_gif, content)
content = re.sub(png_pattern, repl_png, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
