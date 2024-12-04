import yfinance as yf

try:
    # データ取得
    nikkei = yf.download('^N225', start='2023-01-01', end='2024-03-20')
    
    # データが空でないか確認
    if nikkei.empty:
        print("データを取得できませんでした")
    else:
        print("データ取得成功!")
        print("\n=== データの基本情報 ===")
        print(f"データ期間: {nikkei.index[0]} から {nikkei.index[-1]}")
        print(f"取得行数: {len(nikkei)}")
        print(f"カラム: {nikkei.columns.tolist()}")
        
        print("\n=== 最新5件のデータ ===")
        print(nikkei.tail())
        
        print("\n=== 基本統計量 ===")
        print(nikkei['Close'].describe())

except Exception as e:
    print(f"エラーが発生しました: {str(e)}")