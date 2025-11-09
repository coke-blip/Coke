import tkinter as tk
import random
import threading
import time

# 全局变量：存储所有温馨提示窗口 + 主线程根对象
all_windows = []
root = tk.Tk()
root.withdraw()  # 隐藏主线程默认的空白窗口


def show_warm_tip():
    """创建单个温馨提示窗口（主线程调度，线程安全）"""

    def create_single_window():
        # 基于主线程root创建子窗口，避免跨线程问题
        window = tk.Toplevel(root)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 250
        window_height = 60
        # 随机位置（避免窗口完全重叠）
        x = random.randrange(0, screen_width - window_width)
        y = random.randrange(0, screen_height - window_height)

        window.title('温馨提示')
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # 温馨提示窗口也置顶（但后续会被控制窗口压制）
        window.attributes('-topmost', True)

        # 随机提示语和背景色
        tips = ['生理期多休息！', '保持微笑呀', '每天都要元气满满', '记得吃水果，保持好心情',
                '好好爱自己', '我想你了', '龙小呆！', '期待下一次见面', '看看龙二狗！',
                '早点休息，愿所有烦恼都消失', '少熬夜', '今天过得开心嘛', '天冷了，多穿衣服']
        bg_colors = ['lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
                     'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew']

        tk.Label(
            window,
            text=random.choice(tips),
            bg=random.choice(bg_colors),
            font=('微软雅黑', 16),
            width=30,
            height=3
        ).pack()

        all_windows.append(window)  # 加入全局列表管理

    # 关键：所有tkinter操作交给主线程执行
    root.after(0, create_single_window)


def create_control_window():
    """创建控制窗口（永久置顶，不被覆盖）"""
    control_window = tk.Toplevel(root)
    control_window.title('程序控制中心')
    control_window.geometry('280x140')  # 适当放大窗口，方便点击
    control_window.resizable(False, False)  # 禁止调整窗口大小

    # 1. 基础置顶：确保窗口默认在顶层
    control_window.attributes('-topmost', True)

    # 2. 核心：定时刷新置顶状态（每500毫秒执行一次，防止被其他窗口覆盖）
    def keep_control_window_top():
        if control_window.winfo_exists():  # 窗口存在时才执行
            control_window.lift()  # 强制将窗口提到最顶层
            # 循环调用自身，持续维持置顶
            control_window.after(500, keep_control_window_top)

    # 启动置顶刷新任务
    keep_control_window_top()

    # 终止所有窗口的逻辑
    def terminate_all():
        # 关闭所有温馨提示窗口
        for window in all_windows:
            if window.winfo_exists():
                window.destroy()
        all_windows.clear()
        # 关闭控制窗口自身
        control_window.destroy()
        # 退出主线程事件循环（彻底结束程序）
        root.quit()

    # 终止按钮（放大尺寸，提升点击体验）
    tk.Button(
        control_window,
        text='一键终止所有窗口',
        font=('微软雅黑', 12, 'bold'),
        bg='#FF4444',  # 红色背景，醒目
        fg='white',  # 白色文字，对比清晰
        width=18,
        height=2,
        command=terminate_all
    ).pack(pady=30)


def batch_create_windows():
    """子线程：批量触发温馨提示窗口创建（仅触发，不直接操作tkinter）"""
    for _ in range(180):  # 可调整窗口数量
        show_warm_tip()
        time.sleep(0.005)  # 控制窗口弹出速度，避免卡顿


if __name__ == '__main__':
    # 1. 先创建控制窗口（主线程执行，确保优先显示）
    create_control_window()

    # 2. 启动子线程，批量创建温馨提示窗口
    batch_thread = threading.Thread(target=batch_create_windows)
    batch_thread.daemon = True  # 主线程结束时，子线程自动退出
    batch_thread.start()

    # 3. 启动主线程事件循环（所有tkinter窗口的核心）
    root.mainloop()