from moviepy import VideoFileClip  # 针对新版本的修正
import os

# 检查视频文件是否存在
input_path = "media/videos/start/480p15/MyFirstAnimation.mp4"
output_path = "preview.gif"

if os.path.exists(input_path):
    print("正在努力转换中，这可能需要几十秒，请稍等...")
    try:
        # 加载视频并进行转换
        clip = VideoFileClip(input_path)
        # resize(0.5) 缩小尺寸，防止 GIF 文件过大上传不了 GitHub
        clip.resized(0.5).write_gif(output_path, fps=10) 
        print(f"🎉 转换成功！生成了文件：{output_path}")
    except Exception as e:
        print(f"转换过程中出错了：{e}")
else:
    print(f"❌ 找不到视频文件！请确认路径是否正确：{input_path}")