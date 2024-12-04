import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示用

# サンプルデータの生成
np.random.seed(42)  # 再現性のため乱数シードを設定
group1 = np.random.normal(100, 10, 200)  # 平均100、標準偏差10の正規分布
group2 = np.random.normal(90, 20, 200)   # 平均90、標準偏差20の正規分布
group3 = np.random.normal(150, 15, 200)  # 平均110、標準偏差15の正規分布

# データをリストにまとめる
data = [group1, group2, group3]

# 箱ヒゲ図の作成
plt.figure(figsize=(10, 6))
box_plot = plt.boxplot(data,
                      labels=['グループ1', 'グループ2', 'グループ3'],
                      patch_artist=True,  # 箱の中を塗りつぶす
                      medianprops={'color': 'green'},  # 中央値の線の色
                      boxprops={'facecolor': 'lightblue'},  # 箱の色
                      whiskerprops={'color': 'black'},  # ヒゲの色
                      capprops={'color': 'black'})  # ヒゲの先端の色

# グラフの設定
plt.title('3グループの箱ヒゲ図による比較')
plt.ylabel('値')
plt.grid(True, linestyle='--', alpha=0.7)

# グラフの表示
plt.show()