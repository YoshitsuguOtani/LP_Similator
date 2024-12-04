import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import japanize_matplotlib  # 日本語表示用

#plt.rcParams['font.family'] = 'MS Gothic'

# サンプルデータの作成
np.random.seed(42)
data = pd.DataFrame({
    'Point': np.random.normal(70, 15, 100),
    'Time': np.random.normal(5, 2, 100),
    'Group': np.random.choice(['A', 'B', 'C'], 100)
})

# プロットのスタイル設定
sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

# サブプロットの作成
plt.subplot(2, 2, 1)
# 箱ヒゲ図
sns.boxplot(x='Group', y='Point', data=data)
plt.title('Point of group(Hakohige)')

plt.subplot(2, 2, 2)
# バイオリンプロット
sns.violinplot(x='Group', y='Point', data=data)
plt.title('Plot')

plt.subplot(2, 2, 3)
# 散布図
sns.scatterplot(x='Time', y='Point', hue='Group', data=data)
plt.title('Time and Point of group(Scatter)')

plt.subplot(2, 2, 4)
# ヒストグラム
sns.histplot(data=data, x='Point', hue='Group', multiple="stack")
plt.title('Point Histgram')

# レイアウトの調整
plt.tight_layout()
plt.show()

# ヒートマップの例（別ウィンドウで表示）
#plt.figure(figsize=(8, 6))
# 相関行列の作成
#correlation = data[['得点', '学習時間']].corr()
#sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
#plt.title('相関ヒートマップ')
#plt.show()