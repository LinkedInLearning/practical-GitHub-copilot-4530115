import os
import eyed3

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            comments = [comment.text for comment in audio_file.tag.comments]
            comments_str = ', '.join(comments)
            audio_info = {
                'title': audio_file.tag.title,
                'comments': comments_str,
                'file': '/audio/' + file  # 添加 /audio/ 前缀并将键名改为 file
            }
            audio_files.append(audio_info)
    return audio_files

# 调用函数并打印返回的列表
import yaml
print(yaml.dump(get_audio_files(), sort_keys=False))