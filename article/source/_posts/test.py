import re
import os

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.realpath(__file__))

# 查找脚本所在目录的子目录
subdirectories = [d for d in os.listdir(script_dir) if os.path.isdir(os.path.join(script_dir, d))]

# 遍历每个子目录
for subdirectory in subdirectories:
    # 构建子目录的完整路径
    subdirectory_path = os.path.join(script_dir, subdirectory)

    # 获取子目录中的所有 Markdown 文件
    markdown_files = [f for f in os.listdir(subdirectory_path) if f.endswith(".md")]

    # 遍历每个 Markdown 文件
    for markdown_file in markdown_files:
        file_path = os.path.join(subdirectory_path, markdown_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件内容
            content = file.read()

            # 使用正则表达式匹配一级标题
            match = re.search(r'# (.+)', content)

            # 提取一级标题内容
            title = match.group(1)

            # 构建 title 部分
            title_section = f'---\ntitle: {title}\n---\n'

            # 在文件开头插入 title 部分
            content = title_section + content

            # 删除一级标题及其后的内容
            content = re.sub(r'# .+\n', '', content, count=1)

            # 将修改后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as updated_file:
                updated_file.write(content)
