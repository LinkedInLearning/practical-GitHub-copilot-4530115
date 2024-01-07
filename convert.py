import os

# 从 audio 文件夹中读取 mp3 文件并返回一个列表
def read_mp3_files():
    audio_files = []
    for file in os.listdir("audio"):
        if file.endswith(".mp3"):
            audio_files.append(file)
    return audio_files

# 调用函数并打印返回的列表
print(read_mp3_files())