import os

# 从 audio 文件夹中读取 mp3 文件并返回一个列表
def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_files.append(file)
    return audio_files

# 打印 audio 文件夹中的 mp3 文件
print(get_audio_files())