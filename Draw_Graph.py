import wx                       #wxpython(GUI)

import matplotlib as mpl        #グラフ描画
import matplotlib.pyplot as plt #matplotlibパッケージ内のモジュール
from mpl_toolkits.mplot3d import Axes3D

import numpy as np              #ベクトルや行列の計算を高速に処理するためのライブラリ
import seaborn                  #グラフの体裁が良くなる？
import seaborn as sns           #文字設定のため

import random                   #random

import csv                      #CSV
import pandas as pd             #データの統計量を表示したり、グラフ化するなど、データ分析や機械学習で必要となる作業を簡単に行うことができる

import sympy as sym             #式をそのままグラフにしてくれる
from sympy.plotting import plot #式をそのままグラフにしてくれる

#例外処理のために追加
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog


#GUI関連
class MyFrame(wx.Frame):
    #コンボボックス内選択肢作成
    items = ['CSV読み込み',  '数式をグラフ表示', '散布図','3次元等高線','複数グラフ描画']

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "グラフ描画", size=(250,100))

        # Create widgets.(コンボボックス、ボタン実装)
        panel = wx.Panel(self)

        #self←クラスのインスタンス変数宣言
        self.combo = wx.ComboBox(panel, choices=self.items,style=wx.CB_READONLY)
        #self.combo.Bind(wx.EVT_COMBOBOX, self.SelectItem)

        button_1 = wx.Button(panel, wx.ID_ANY, '実行')
        #Bindイベントを関連付ける
        button_1.Bind(wx.EVT_BUTTON, self.click_button_1)
        button_2 = wx.Button(panel, wx.ID_ANY, '閉じる')
        button_2.Bind(wx.EVT_BUTTON, self.click_button_2)
   

        # Set sizer.(レイアウト設定)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.combo, flag=wx.GROW)

        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        sizer_h.Add(button_1,1)
        sizer_h.Add(button_2,1)

        #sizerにsizer_hを追加してレイアウト表示
        sizer.Add(sizer_h,0, wx.ALIGN_RIGHT | wx.RIGHT, 45)
        panel.SetSizer(sizer)


    #コンボボックス選択時の処理
#    def SelectItem(self,event):
#        plt.clf()
#        plt.close()

    #実行ボタン押下時の処理
    def click_button_1(self,event):
#        plt.close()
        #コンボボックスの選択index取得
        c_id=self.combo.GetSelection()

        #選択内容による分岐
        if c_id == 0:               #CSV読み込み選択
            Graph_draw.csv_g()
        elif c_id == 1:             #数式選択
            Graph_draw.Formula_g()
        elif c_id == 2:             #散布図選択
            Graph_draw.Sample_g()
        elif c_id == 3:
            Graph_draw.Axes3D_g()   #3次元等高線
        elif c_id == 4:
            Graph_draw.Multiple_g()   #複数グラフ描画
        else:
            print("エラー")

#        event.Skip()実装前に使用

    #閉じるボタン押下時の処理
    def click_button_2(self, event):  # wxGlade: MyFrame.<event_handler>
        #アプリケーション終了
        self.Destroy()


class Graph_draw():
    def csv_g():#CSV読み込み
        #データフレーム作成し、データの先頭から読み込み
        try:
            df=pd.read_csv('data.csv',index_col=0)

            #Fontの設定(exe化のときの文字化け対策)
            sns.set(font=["Meiryo","Yu Gothic","HIiragino Maru Gothic Pro"])

            #グラフの詳細設定
            df.plot(title='6月の気温',      #タイトル設定
                    grid=True,              #グリッドの表示
                    colormap='Accent',      #色
                    legend=True,            #凡例表示
                    alpha=0.8)              #透過率（0〜1）

            plt.xlabel("日付")              # x軸のラベル
            plt.ylabel("気温")              # y軸のラベル

            #グラフ表示
            plt.show()

        except FileNotFoundError:           #ファイルの例外処理
            root = tk.Tk()
            #小さなウィンドウを表示させない
            root.withdraw()
            messagebox.showerror("File error", "does not exsist")

#リアルタイムで正弦波
#class R_sin():
#   def sin_g():

       # 描画領域を取得
#        fig, ax = plt.subplots(1, 1)

        # y軸方向の描画幅を指定
#        ax.set_ylim((-1.1, 1.1))

        # x軸:時刻
#        x = np.arange(0, 100, 0.5)

        # 周波数を高くしていく
#        for Hz in np.arange(0.1, 10.1, 0.01):
          # sin波を取得
#          y = np.sin(2.0 * np.pi * (x * Hz) / 100)
          # グラフを描画する
#          line, = ax.plot(x, y, color='blue')
#          # 次の描画まで0.01秒待つ
#          plt.pause(0.01)
          # グラフをクリア
#          line.remove()

#        plt.clf()
#        plt.close()


    def Formula_g():#数式をグラフ表示

        #数式の作成

        #変数定義
        x = sym.Symbol('x')
        #size = 5

        #xの二乗＋5x＋4
        expr = x**2 + 5*x + 4
 
        #グラフ表示
        plot(expr, (x, -10, 10), title='X', xlabel='x', ylabel='x**2+5x+4')

    def Sample_g():#散布図

        #標準正規分布に従った乱数を100個生成
        x = np.random.randn(100)*0.5
        y = np.random.randn(100)
        x1 = np.random.randn(100)*0.5+0.5
        y1 = np.random.randn(100)

        #x軸とy軸にラベル付け
        plt.xlabel("xの乱数")
        plt.ylabel("yの乱数")

        #散布図を作成
        plt.scatter(x, y,s=100, c='blue',  marker='*', alpha=0.5,label="star")
        plt.scatter(x1, y1,s=100, c='orange',  marker='*', alpha=0.5,label="star2")
        plt.title("標準正規分布に従った乱数を100個生成")
        plt.legend()

        #colorbarを表示 
        plt.colorbar()

        #散布図を表示
        plt.show()

    def Axes3D_g():#3次元等高線
        # Figureと3DAxeS
        fig = plt.figure(figsize = (6, 6))
        ax = fig.add_subplot(111, projection="3d")

        # 軸ラベルを設定
        ax.set_xlabel("x", size = 16)
        ax.set_ylabel("y", size = 16)
        ax.set_zlabel("z", size = 16)

        # 円周率の定義
        pi = np.pi

        # (x,y)データを作成
        x = np.linspace(-3*pi, 3*pi, 256)
        y = np.linspace(-3*pi, 3*pi, 256)

        # 格子点を作成
        X, Y = np.meshgrid(x, y)

        # 高度の計算式
        Z = np.cos(X/pi) * np.sin(Y/pi)

        # 曲面を描画
        ax.plot_surface(X, Y, Z, cmap = "summer")

        # 底面に等高線を描画
        ax.contour(X, Y, Z, colors = "black", offset = -1)

        plt.show()

    def Multiple_g():#複数グラフ描画
        #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
        fig = plt.figure()

        x=np.linspace(0,10,100)
        y1=np.sin(x)
        y2=np.cos(x)

        ax1 = fig.add_subplot(2, 2, 1)#左上
        ax2 = fig.add_subplot(2, 2, 2)#右上
        ax3 = fig.add_subplot(2, 2, 3)#左下
        ax4 = fig.add_subplot(2, 2, 4)#右下

        #左上
        ax1.set_ylim(-1.5,1.5)                      #y軸の描画範囲の調整
        ax1.set_title("sin(x)&cos(x)",fontsize=10)
        ax1.set_xlabel("x",fontsize=10)
        ax1.set_ylabel("y",fontsize=10)
        ax1.grid(True)                              #グリッドの表示
        ax1.tick_params(labelsize=8)                #y軸目盛間隔を調整(目盛り、目盛りラベル、グリッド線のパラメーターを設定)
        ax1.plot(x,y1,color='b',label="sin(x)")
        ax1.plot(x,y2,color='r',label="cos(x)")

        #右上
        labels = 'label1', 'label2', 'label3'
        size = 0.3
        vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3)*4)
        inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

        ax2.pie(vals.sum(axis=1), labels=labels, radius=1, colors=outer_colors, autopct='%1.1f%%', wedgeprops=dict(width=size, edgecolor='w'))
        ax2.pie(vals.flatten(), radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))
        ax2.set(aspect="equal", title='Pie plot with `ax.pie`')

        #左下        ax3.set_title('Test score')

        math = [71, 80, 95, 52, 93, 68, 98, 30, 78, 60]
        english = [62, 89, 82, 95, 92, 89, 91, 72, 75, 93]

        data = (math, english)

        #箱ひげ図を作成
        bp=ax3.boxplot(data)

        #グラフタイトルと箱ひげ図のラベルを設定
        ax3.set_xticklabels(['Math', 'English'])
        ax3.set_title('Test set_xticklabelsscore')
        ax3.set_xlabel('exams')
        ax3.set_ylabel('point')

        # Y軸のメモリの長さ
        ax3.set_ylim([0,100])
        ax3.grid()

        #右下
        np.random.seed(2018)                        #ランダムシードは、疑似乱数ジェネレータを初期化するために使用される数値
        x1 = np.random.normal(40, 10, 1000)
        x2 = np.random.normal(80, 20, 1000)

        ax4.hist(x1, bins=50, alpha=0.6)
        ax4.hist(x2, bins=50, alpha=0.6)
        ax4.set_title("histogram",fontsize=10)
        ax4.set_xlabel('length [cm]')

        ax4.set_xlabel('x')
        ax4.set_ylabel('y')
        ax4.grid(True)

        fig.tight_layout()              #レイアウトの設定
        plt.show()

if __name__ == '__main__':
    #wx.AppのMainLoop関数を呼び出しを行い，イベントのキャッチを開始
    app = wx.App(False)
    MyFrame().Show(True)
    app.MainLoop()