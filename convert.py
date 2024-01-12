import os
import eyed3
import yaml

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            comments = [comment.text for comment in audio_file.tag.comments]
            comments_str = ', '.join(comments)
            audio_info = {
                'title': audio_file.tag.title,
                'comments': comments_str
            }
            audio_files.append(audio_info)
    return yaml.dump(audio_files)

# 调用函数并打印返回的列表
print(get_audio_files())