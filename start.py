from manim import *

class MyFirstAnimation(Scene):
    def construct(self):
        # 1. 创建物体
        # 创建一个红色的正方形
        square = Square(color=RED, fill_opacity=0.8)
        # 创建一个蓝色的圆形
        circle = Circle(color=BLUE, fill_opacity=0.8)
        
        # 2. 编排动画脚本
        # 第一幕：显示正方形（像画出来一样）
        self.play(Create(square), run_time=1.5)
        self.wait(1)
        
        # 第二幕：正方形平滑地变形成圆形
        self.play(Transform(square, circle), run_time=2)
        
        # 第三幕：写下成功的文字
        # 我们先用英文，防止你的系统暂时没配置中文字体导致乱码
        text = Text("Success!", font_size=48).next_to(circle, UP)
        self.play(Write(text))
        
        # 停留一会儿看结果
        self.wait(2)