import curses


def main(stdscr):
    # --- 初期設定 ---
    stdscr.clear()

    # --- メインループ ---
    stdscr.addstr(0, 0, "Hello World! 続行するには何かキーを押してください...")
    stdscr.getkey()  # 何かキーが押されるまで待つ


curses.wrapper(main)

print("Editor closed.")
