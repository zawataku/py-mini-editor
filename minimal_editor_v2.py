import curses


def main(stdscr):
    # --- 初期設定 ---
    stdscr.clear()
    lines = [""]
    cy, cx = 0, 0

    # --- メインループ ---
    while True:
        stdscr.clear()
        for i, line in enumerate(lines):
            stdscr.addstr(i, 0, line)
        stdscr.move(cy, cx)

        # キー入力の受付
        key = stdscr.getch()

        # 終了コマンド (Ctrl + Q)
        if key == 17:
            break

        # 保存コマンド (Ctrl + S)
        elif key == 19:
            # ファイル名を 'output.txt' に固定して保存
            with open("output.txt", "w") as f:
                f.write("\n".join(lines))
            stdscr.addstr(len(lines), 0, "File saved to output.txt")
            stdscr.refresh()
            curses.napms(1000)
            continue  # メインループの先頭に戻る

        # バックスペースキー (文字の消去)
        elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:  # バックスペースが127の場合と8の場合があるっぽい...？
            if cx > 0:
                lines[cy] = lines[cy][:cx - 1] + lines[cy][cx:]
                cx -= 1
            elif cy > 0:
                # 行頭なら上の行と結合
                content = lines.pop(cy)
                cy -= 1
                cx = len(lines[cy])
                lines[cy] += content

        # Enterキー (改行)
        elif key == curses.KEY_ENTER or key == 10:
            # カーソル位置以降の文字列を新しい行に移動
            rest_of_line = lines[cy][cx:]
            lines[cy] = lines[cy][:cx]
            cy += 1
            cx = 0
            lines.insert(cy, rest_of_line)

        # 通常の文字入力
        elif 32 <= key < 127:
            lines[cy] = lines[cy][:cx] + chr(key) + lines[cy][cx:]
            cx += 1


# --- プログラムの実行 ---
curses.wrapper(main)
print("Editor closed successfully.")
