import os
import eyed3

# 从 audio 文件夹中读取 mp3 文件并返回一个包含 title 和 comments 的列表
def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            audio_files.append({
                'title': audio_file.tag.title,
                'comments': audio_file.tag.comments
            })
    return audio_files

# 调用函数并打印返回的列表
print(get_audio_files())