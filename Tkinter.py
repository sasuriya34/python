#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# ------------------------------------------------------------
# 上記は シバン/シェバン(Shebang) と 文字コードの指定
# 文字コード指定で "-*-" にて囲むのは、どちらかと言えば慣例的
# また 大文字 "UTF-8" など 色々なエイリアス名が許容されている
# ------------------------------------------------------------


# ======================================
# Tkinter for Python 3.8
# サンプル・コード  [雛形フォーム]
#
# [環境]
#   Xubntu 20.04 LTS
#   Python 3.8.10
#   python3-tk Ver3.8.10
#   VSCode 1.62
#   <拡張>
#     |- Python  V2021.12
#     |- Pylance V2021.12
#
# [更新履歴]
#   2021/12/18 イベントルーチンをClass内に収める
#   2021/12/10 新規作成
# ======================================

import tkinter as tk                            # Tkinter
from tkinter.constants import LEFT              # .pack(side=LEFT) で必要


class TkForm(tk.Frame):                         # 継承クラスとして宣言

    """
        Tk-Frame の継承クラス を定義
    """
    def __init__(self, master:tk.Tk) -> None:   # "->None" は "def"の型ヒント (アノテーション)
        super().__init__(master)                # 親クラスの__init__にて初期化は必須 (らしい)
#       tk.Frame.__init__(self)                 # こちらでも可能なようだが、super() との使い分けは不明
        self.pack()                             # self.pack() をする必要性は未確認
        #                                       # 実質的には self.pack() が無くても問題ないようだ

        master.title("[雛形] Python Standerd TKフォーム")
        master.geometry("320x80")               # VSCode上において、変数 master に対しての
        #                                       # 型ヒント[master:tk.Tk)] を設定しないと、
        #                                       # 入力補完ができない模様

        button = tk.Button(master, text="ボタンA", command=self.clicked) # 配置のDefaultは (多分) side=tk.TOP。マウスUpイベント
        button.pack(side=LEFT, anchor=tk.N, padx=20, pady=25)       # 左記の指定は 左詰めで横並びにする指定方法
        #                                                           # 通常は、縦並びになる

        button = tk.Button(master, text="ボタンB")                  # 変数 button を共用的に使っても問題なさそう
        button.pack(side=LEFT, anchor=tk.N, pady=25)                # padx は 左右両方なので１つ飛び指定
        button.bind("<ButtonRelease-1>", self.click2ed)             # マウスUp イベント (左クリック)  [右クリックなら"-3"]

        button = tk.Button(master, text="ボタンC")                  # 変数 button を共用的に使っても問題なさそう
        button.pack(side=LEFT, anchor=tk.N, padx=20, pady=25)       # 左詰め横並びの配置指定
        button.bind("<Button-1>", lambda e:self.click3ing("'ボタンC’ を押下した"))  # マウスDown イベント (左クリック)

    def clicked(self):                              # "command=関数名" の指定は
        print("'ボタンA' を押下した")               # マウスUp イベント

    def click2ed(self, e):                          # .bind("<ButtonRelease-1>") 指定は 
        print("'ボタンB' を押下した  ", end="")     # マウスUp イベント (左クリック)
        ss:str = "X:{0}  Y:{1}  text={2}".format(e.x, e.y, e.widget["text"])
        print(ss)                                   # コールバック関数には マウス座標などの情報が引き渡される

    def click3ing(self, s:str):                     # .bind("<Button-1>") 指定は
        print(s)                                    # マウスDown イベント (左クリック)
        #                                           # ラムダ式で 文字列のみを受け取る
        #                                           # この方法はあまり使わないかな？ ("ボタンA"形式で十分)
        #                                           # "s:str" は 型ヒント(アノテーション)
        # 仮引数 self [これは予約語ではない、慣例的に使われる語句] は、今回の場合において
        # 実質的には不要ではある(利用していない)が、Class内 の関数ルーチンとはしては必要になる。


if __name__ == "__main__":
    """
        エントリポイント
    """
    win = tk.Tk()
    app = TkForm(master=win)
    app.mainloop()


# -- 以下は Class を使わない平文の構成の場合 (ボタン設定などは省略) -------------------
#    root = tk.Tk()
#    root.title("[雛形] Python Standerd TKフォーム") 
#    root.geometry("450x650")
#            |
#    [ここに各ウィジット[ボタンなど]の設定を記述する]
#            |
#    root.mainloop()