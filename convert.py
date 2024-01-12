import os
import eyed3

# 从 audio 文件夹中读取 mp3 文件并返回一个包含 title 和 comments 的列表
def read_mp3_files():
    audio_files = []
    for file in os.listdir("audio"):
        if file.endswith(".mp3"):
            audiofile = eyed3.load(os.path.join("audio", file))
            comments = audiofile.tag.comments
            comments_text = [comment.text for comment in comments] if comments else None
            audio_files.append((file, audiofile.tag.title, comments_text))
    return audio_files

# 调用函数并打印返回的列表
for file_info in read_mp3_files():
    print(f"File: {file_info[0]}, Title: {file_info[1]}, Comments: {file_info[2]}")