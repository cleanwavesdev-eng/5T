import ccxt
import pandas as pd
import pandas-ta as ta

def fetch_data(symbol='BTC/USDT', timeframe='15m', limit=100):
    exchange = ccxt.binance()
    bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def analyze():
    print("--- جاري سحب بيانات BTC/USDT الحالية ---")
    df = fetch_data()
    
    # حساب المؤشرات
    df['ema_8'] = ta.ema(df['close'], length=8)
    df['ema_21'] = ta.ema(df['close'], length=21)
    
    last_row = df.iloc[-1]
    prev_row = df.iloc[-2]
    
    print(f"السعر الحالي: {last_row['close']}")
    
    # منطق التقاطع البسيط للتجربة
    if prev_row['ema_8'] < prev_row['ema_21'] and last_row['ema_8'] > last_row['ema_21']:
        print("🚀 إشارة CleanWave: تقاطع ذهبي صاعد!")
    elif prev_row['ema_8'] > prev_row['ema_21'] and last_row['ema_8'] < last_row['ema_21']:
        print("🛑 إشارة CleanWave: تقاطع بيعي!")
    else:
        print("⏳ حالة السوق: انتظار تقاطع واضح...")

if __name__ == "__main__":
    analyze()
