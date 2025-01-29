import pyautogui
import random
import time
import sys


def perform_random_click(base_x, base_y, offset_range=15):
    """在指定坐标基础上，随机偏移并点击。"""
    offset_x = random.randint(-offset_range, offset_range)
    offset_y = random.randint(-offset_range, offset_range)

    click_x = base_x + offset_x
    click_y = base_y + offset_y

    # 可随机添加短暂停顿模拟人工行为
    delay = random.uniform(0.1, 0.25)
    time.sleep(delay)

    pyautogui.click(click_x, click_y)
    return click_x, click_y


def run_click_simulation(click_count=500, base_x=950, base_y=600):
    print("开始执行点击事件...")
    try:
        for i in range(1, click_count + 1):
            current_x, current_y = perform_random_click(base_x, base_y)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f"第{i}次点击：坐标({current_x}, {current_y})，时间：{timestamp}")

            # 每 50 次点击时询问是否退出，可根据需求调整
            if i % 50 == 0:
                user_input = input("已点击 500 次，按 Enter 继续，输入 q 退出：").strip().lower()
                if user_input == 'q':
                    print("用户选择退出，程序结束...")
                    break

    except KeyboardInterrupt:
        print("\n检测到用户中断，程序结束...")
    except Exception as e:
        print(f"发生错误：{e}")
        sys.exit(1)


if __name__ == "__main__":
    # 程序启动前延迟 5 秒
    time.sleep(5)
    # 使用说明：
    # 分别设置 点击多少次（500）、点击位置的x坐标（950） 点击的Y坐标（600）
    # 因每人页面大小不一样，可以启动脚本后，在页面上观察鼠标自动点击的位置进行X y的调整
    run_click_simulation(500, 950, 600)
