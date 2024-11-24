import random
import matplotlib.pyplot as plt
#import japanize_matplotlib  # 日本語表示用

def flip_coin(bias=0.5):
    """
    コインを投げるシミュレーション
    bias: 表が出る確率（0.0から1.0の間）
    戻り値: True=表、False=裏
    """
    return random.random() < bias

# パラメータ設定
flips = 10000  # 試行回数
bias = 0.5    # 表が出る確率
heads = 0     # 表が出た回数

# シミュレーション実行
for _ in range(flips):
    if flip_coin(bias):
        heads += 1

tails = flips - heads  # 裏の回数

# グラフの作成
plt.figure(figsize=(8, 6))
labels = ['表', '裏']
counts = [heads, tails]
colors = ['#2ecc71', '#e74c3c']  # 緑と赤

# 棒グラフの作成
plt.bar(labels, counts, color=colors)

# グラフの設定
plt.title(f'コイントスのシミュレーション結果\n(試行回数: {flips}, バイアス: {bias})')
plt.ylabel('回数')

# 各棒グラフの上に数値を表示
for i, count in enumerate(counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

# パーセンテージを表示
percentages = [count/flips*100 for count in counts]
for i, percentage in enumerate(percentages):
    plt.text(i, counts[i]/2, f'{percentage:.1f}%', ha='center', va='center')

# グラフの表示
plt.show()