import os
import eyed3
from datetime import timedelta

def get_audio_files():
    # 初始化一个空列表来存储音频文件信息
    audio_files = []
    # 遍历 'audio' 目录下的所有文件
    for file in os.listdir('audio'):
        # 如果文件是 mp3 文件
        if file.endswith('.mp3'):
            # 使用 eyed3 加载音频文件
            audio_file = eyed3.load(os.path.join('audio', file))
            # 获取音频文件的描述信息
            description = [comment.text for comment in audio_file.tag.comments]
            # 将描述信息列表转换为字符串
            description_str = ', '.join(description)
            # 获取音频文件的持续时间，并将其格式化为字符串
            duration = str(timedelta(seconds=int(audio_file.info.time_secs)))
            # 获取音频文件的大小
            length = os.path.getsize(os.path.join('audio', file))
            # 将文件大小格式化为逗号分隔的格式
            length_str = format(length, ',')
            # 创建一个字典来存储音频文件的信息
            audio_info = {
                'title': audio_file.tag.title,
                'description': description_str,
                'duration': duration,
                'file': '/audio/' + file,
                'length': length_str
            }
            # 将音频文件的信息添加到列表中
            audio_files.append(audio_info)
    # 返回音频文件信息列表
    return audio_files

# 调用函数并将返回的列表写入到一个文件
import yaml

# 打开一个名为 'episodes.yaml' 的文件，准备写入
with open('episodes.yaml', 'w') as file:
    # 将音频文件信息列表转换为 YAML 格式，并写入到文件中
    yaml.dump(get_audio_files(), file, sort_keys=False)