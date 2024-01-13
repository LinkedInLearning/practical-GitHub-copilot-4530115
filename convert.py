import os
import eyed3
from datetime import timedelta

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            description = [comment.text for comment in audio_file.tag.comments]
            description_str = ', '.join(description)
            duration = str(timedelta(seconds=int(audio_file.info.time_secs)))  # 格式化 duration 字段
            audio_info = {
                'title': audio_file.tag.title,
                'description': description_str,
                'duration': duration,
                'file': '/audio/' + file
            }
            audio_files.append(audio_info)
    return audio_files

# 调用函数并打印返回的列表
import yaml
print(yaml.dump(get_audio_files(), sort_keys=False))