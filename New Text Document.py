ModuleNotFoundError: No module named 'PIL'
>>>
>>> # MoviePy v1 aur v2 dono ke liye compatibility
>>> try:
...         from moviepy import ImageClip, AudioFileClip
...             MOVIEPY_V2 = True
...             except ImportError:
...                         from moviepy.editor import ImageClip, AudioFileClip
...                             MOVIEPY_V2 = False
...
  File "<python-input-10>", line 3
    MOVIEPY_V2 = True
IndentationError: unexpected indent
>>> # ================= CONFIGURATION =================
>>> GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Yahan apni Gemini API key daalein
>>> TICKER = "BTC-USD"  # Example: 'BTC-USD' (Bitcoin), '^NSEI' (Nifty 50), 'RELIANCE.NS'
>>> ASSET_NAME = "Bitcoin"
>>> LANGUAGE = "hi"  # 'hi' Hindi ke liye, 'en' English ke liye
>>> OUTPUT_VIDEO = "ai_trading_video.mp4"
>>> # =================================================
>>>
>>> def generate_trading_chart(ticker, asset_name):
...             print(f"1. {asset_name} ka live trading data aur chart ban raha hai...")
...                 data = yf.Ticker(ticker).history(period="7d", interval="1h")
...
  File "<python-input-19>", line 3
    data = yf.Ticker(ticker).history(period="7d", interval="1h")
IndentationError: unexpected indent
>>>     if data.empty:
  File "<python-input-20>", line 1
    if data.empty:
IndentationError: unexpected indent
>>>         raise ValueError("Market data nahi mila. Ticker symbol check karein.")
  File "<python-input-21>", line 1
    raise ValueError("Market data nahi mila. Ticker symbol check karein.")
IndentationError: unexpected indent
>>>
>>>     latest_price = round(data['Close'].iloc[-1], 2)
  File "<python-input-23>", line 1
    latest_price = round(data['Close'].iloc[-1], 2)
IndentationError: unexpected indent
>>>     start_price = round(data['Close'].iloc[0], 2)
  File "<python-input-24>", line 1
    start_price = round(data['Close'].iloc[0], 2)
IndentationError: unexpected indent
>>>     change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
  File "<python-input-25>", line 1
    change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
IndentationError: unexpected indent
>>>     trend = "Bullish (Upar)" if change_pct >= 0 else "Bearish (Neeche)"
  File "<python-input-26>", line 1
    trend = "Bullish (Upar)" if change_pct >= 0 else "Bearish (Neeche)"
IndentationError: unexpected indent
>>>
>>>     # 9:16 Vertical Background aur Chart banana
>>>     plt.style.use('dark_background')
  File "<python-input-29>", line 1
    plt.style.use('dark_background')
IndentationError: unexpected indent
>>>     fig, ax = plt.subplots(figsize=(9, 16), dpi=100)
  File "<python-input-30>", line 1
    fig, ax = plt.subplots(figsize=(9, 16), dpi=100)
IndentationError: unexpected indent
>>>     fig.patch.set_facecolor('#0b0e14')
  File "<python-input-31>", line 1
    fig.patch.set_facecolor('#0b0e14')
IndentationError: unexpected indent
>>>     ax.set_facecolor('#0b0e14')
  File "<python-input-32>", line 1
    ax.set_facecolor('#0b0e14')
IndentationError: unexpected indent
>>>
>>>     line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
  File "<python-input-34>", line 1
    line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
IndentationError: unexpected indent
>>>     ax.plot(data.index, data['Close'], color=line_color, linewidth=4)
  File "<python-input-35>", line 1
    ax.plot(data.index, data['Close'], color=line_color, linewidth=4)
IndentationError: unexpected indent
>>>     ax.fill_between(data.index, data['Close'], data['Close'].min(), color=line_color, alp\ha=0.15)
  File "<python-input-36>", line 1
    ax.fill_between(data.index, data['Close'], data['Close'].min(), color=line_color, alpha=0.15)
IndentationError: unexpected indent
>>>
>>>     # Chart styling
>>>     ax.set_title(f"{asset_name} Live Update\nPrice: {latest_price} ({change_pct}%)",
  File "<python-input-39>", line 1
    ax.set_title(f"{asset_name} Live Update\nPrice: {latest_price} ({change_pct}%)",
IndentationError: unexpected indent
>>>                  fontsize=26, fontweight='bold', color='white', pad=40)
  File "<python-input-40>", line 1
    fontsize=26, fontweight='bold', color='white', pad=40)
IndentationError: unexpected indent
>>>     ax.grid(color='#1f2937', linestyle='--', linewidth=1)
  File "<python-input-41>", line 1
    ax.grid(color='#1f2937', linestyle='--', linewidth=1)
IndentationError: unexpected indent
>>>     ax.tick_params(axis='x', rotation=30, labelsize=12)
  File "<python-input-42>", line 1
    ax.tick_params(axis='x', rotation=30, labelsize=12)
IndentationError: unexpected indent
>>>     ax.tick_params(axis='y', labelsize=14)
  File "<python-input-43>", line 1
    ax.tick_params(axis='y', labelsize=14)
IndentationError: unexpected indent
>>>
>>>     for spine in ['top', 'right']:
  File "<python-input-45>", line 1
    for spine in ['top', 'right']:
IndentationError: unexpected indent
>>>         ax.spines[spine].set_visible(False)
  File "<python-input-46>", line 1
    ax.spines[spine].set_visible(False)
IndentationError: unexpected indent
>>>
>>>     plt.tight_layout(rect=[0.03, 0.15, 0.97, 0.85])
  File "<python-input-48>", line 1
    plt.tight_layout(rect=[0.03, 0.15, 0.97, 0.85])
IndentationError: unexpected indent
>>>     chart_path = "chart_bg.png"
  File "<python-input-49>", line 1
    chart_path = "chart_bg.png"
IndentationError: unexpected indent
>>>     plt.savefig(chart_path, facecolor=fig.get_facecolor())
  File "<python-input-50>", line 1
    plt.savefig(chart_path, facecolor=fig.get_facecolor())
IndentationError: unexpected indent
>>>     plt.close()
  File "<python-input-51>", line 1
    plt.close()
IndentationError: unexpected indent
>>>
>>>     return chart_path, latest_price, change_pct, trend
  File "<python-input-53>", line 1
    return chart_path, latest_price, change_pct, trend
IndentationError: unexpected indent
>>>
>>> def generate_ai_script(asset_name, price, change_pct, trend):
...                 print("2. Gemini AI se viral trading script likhwayi ja rahi hai...")
...                     client = genai.Client(api_key=GEMINI_API_KEY)
...
  File "<python-input-55>", line 3
    client = genai.Client(api_key=GEMINI_API_KEY)
IndentationError: unexpected indent
>>>     prompt = (
  File "<python-input-56>", line 1
    prompt = (
IndentationError: unexpected indent
>>>         f"Tum ek expert financial aur trading content creator ho. "
  File "<python-input-57>", line 1
    f"Tum ek expert financial aur trading content creator ho. "
IndentationError: unexpected indent
>>>         f"{asset_name} abhi {price} par trade kar raha hai, pichle 7 din mein {change_pct\}% move hua hai "
  File "<python-input-58>", line 1
    f"{asset_name} abhi {price} par trade kar raha hai, pichle 7 din mein {change_pct}% move hua hai "
IndentationError: unexpected indent
>>>         f"aur trend {trend} hai. Is par 25 se 30 second ki YouTube Shorts ke liye ekdum e\ngaging, "
  File "<python-input-59>", line 1
    f"aur trend {trend} hai. Is par 25 se 30 second ki YouTube Shorts ke liye ekdum engaging, "
IndentationError: unexpected indent
>>>         f"तज aur viral trading update script likho. "
  File "<python-input-60>", line 1
    f"तज aur viral trading update script likho. "
IndentationError: unexpected indent
>>>         f"Sirf bolne wali lines likho (Hinglish ya simple English mein), koi stage direct\ion ya emoji mat daalna."
  File "<python-input-61>", line 1
    f"Sirf bolne wali lines likho (Hinglish ya simple English mein), koi stage direction ya emoji mat daalna."
IndentationError: unexpected indent
>>>     )
  File "<python-input-62>", line 1
    )
IndentationError: unexpected indent
>>>
>>>     response = client.models.generate_content(
  File "<python-input-64>", line 1
    response = client.models.generate_content(
IndentationError: unexpected indent
>>>         model="gemini-2.5-flash",
  File "<python-input-65>", line 1
    model="gemini-2.5-flash",
IndentationError: unexpected indent
>>>         contents=prompt
  File "<python-input-66>", line 1
    contents=prompt
IndentationError: unexpected indent
>>>     )
  File "<python-input-67>", line 1
    )
IndentationError: unexpected indent
>>>     script_text = response.text.replace("*", "").replace("#", "").strip()
  File "<python-input-68>", line 1
    script_text = response.text.replace("*", "").replace("#", "").strip()
IndentationError: unexpected indent
>>>     print(f"\n--- AI Script ---\n{script_text}\n-----------------\n")
  File "<python-input-69>", line 1
    print(f"\n--- AI Script ---\n{script_text}\n-----------------\n")
IndentationError: unexpected indent
>>>     return script_text
  File "<python-input-70>", line 1
    return script_text
IndentationError: unexpected indent
>>>
>>> def generate_voiceover(script_text, lang="hi"):
...                     print("3. AI Voiceover generate ho raha hai...")
...                         tts = gTTS(text=script_text, lang=lang, slow=False)
...                             audio_path = "voiceover.mp3"
...                                 tts.save(audio_path)
...                                     return audio_path
...
  File "<python-input-72>", line 3
    tts = gTTS(text=script_text, lang=lang, slow=False)
IndentationError: unexpected indent
>>> def create_video(image_path, audio_path, output_path):
...                         print("4. Final MP4 video render ho raha hai...")
...                             audio_clip = AudioFileClip(audio_path)
...                                 duration = audio_clip.duration
...
  File "<python-input-73>", line 3
    audio_clip = AudioFileClip(audio_path)
IndentationError: unexpected indent
>>>     if MOVIEPY_V2:
  File "<python-input-74>", line 1
    if MOVIEPY_V2:
IndentationError: unexpected indent
>>>         video_clip = ImageClip(image_path).with_duration(duration).with_audio(audio_clip)
  File "<python-input-75>", line 1
    video_clip = ImageClip(image_path).with_duration(duration).with_audio(audio_clip)
IndentationError: unexpected indent
>>>     else:
  File "<python-input-76>", line 1
    else:
IndentationError: unexpected indent
>>>         video_clip = ImageClip(image_path).set_duration(duration).set_audio(audio_clip)
  File "<python-input-77>", line 1
    video_clip = ImageClip(image_path).set_duration(duration).set_audio(audio_clip)
IndentationError: unexpected indent
>>>
>>>     video_clip.write_videofile(
  File "<python-input-79>", line 1
    video_clip.write_videofile(
IndentationError: unexpected indent
>>>         output_path,
  File "<python-input-80>", line 1
    output_path,
IndentationError: unexpected indent
>>>         fps=24,
  File "<python-input-81>", line 1
    fps=24,
IndentationError: unexpected indent
>>>         codec="libx264",
  File "<python-input-82>", line 1
    codec="libx264",
IndentationError: unexpected indent
>>>         audio_codec="aac"
  File "<python-input-83>", line 1
    audio_codec="aac"
IndentationError: unexpected indent
>>>     )
  File "<python-input-84>", line 1
    )
IndentationError: unexpected indent
>>>
>>>     audio_clip.close()
  File "<python-input-86>", line 1
    audio_clip.close()
IndentationError: unexpected indent
>>>     video_clip.close()
  File "<python-input-87>", line 1
    video_clip.close()
IndentationError: unexpected indent
>>>     print(f"\nSuccess! Aapka video taiyaar hai: {output_path}")
  File "<python-input-88>", line 1
    print(f"\nSuccess! Aapka video taiyaar hai: {output_path}")
IndentationError: unexpected indent
>>>
>>> if __name__ == "__main__":
...                             try:
...                                                                 chart_img, price, pct, tr\end = generate_trading_chart(TICKER, ASSET_NAME)
...                                                                         script = generate\_ai_script(ASSET_NAME, price, pct, trend)
...                                                                                 audio_fil\e = generate_voiceover(script, LANGUAGE)
...                                                                                         c\reate_video(chart_img, audio_file, OUTPUT_VIDEO)
...                                                                                          \   except Exception as e:
...                                                                                          \                                       print(f"Error aaya hai: {e}")
...                                                                                          \
  File "<python-input-90>", line 4
    script = generate_ai_script(ASSET_NAME, price, pct, trend)
IndentationError: unexpected indent
>>>
>>> pip install yfinance matplotlib gtts moviepy pillow
  File "<python-input-92>", line 1
    pip install yfinance matplotlib gtts moviepy pillow
        ^^^^^^^
SyntaxError: invalid syntax
>>> import os
>>> import traceback
>>> import matplotlib
Traceback (most recent call last):
  File "<python-input-95>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> matplotlib.use('Agg')  # Display error rokne ke liye zaroori fix
Traceback (most recent call last):
  File "<python-input-96>", line 1, in <module>
    matplotlib.use('Agg')  # Display error rokne ke liye zaroori fix
    ^^^^^^^^^^
NameError: name 'matplotlib' is not defined
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<python-input-97>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import yfinance as yf
Traceback (most recent call last):
  File "<python-input-98>", line 1, in <module>
    import yfinance as yf
ModuleNotFoundError: No module named 'yfinance'
>>> from gtts import gTTS
Traceback (most recent call last):
  File "<python-input-99>", line 1, in <module>
    from gtts import gTTS
ModuleNotFoundError: No module named 'gtts'
>>> from PIL import Image, ImageDraw, ImageFont
Traceback (most recent call last):
  File "<python-input-100>", line 1, in <module>
    from PIL import Image, ImageDraw, ImageFont
ModuleNotFoundError: No module named 'PIL'
>>>
>>> # MoviePy v1 aur v2 dono ke liye automatic support
>>> try:
...                                 from moviepy import ImageClip, AudioFileClip, concatenate\_videoclips
...                                     MOVIEPY_V2 = True
...                                     except ImportError:
...                                                                         from moviepy.edit\or import ImageClip, AudioFileClip, concatenate_videoclips
...                                                                             MOVIEPY_V2 = \
 False
...
  File "<python-input-103>", line 3
    MOVIEPY_V2 = True
IndentationError: unexpected indent
>>> # ================= SETTINGS =================
>>> # Bas yahan apna prompt likhein (Kisi API Key ki zaroorat nahi hai!)
>>> USER_PROMPT = "Bitcoin ka live trading breakout analysis"
>>> OUTPUT_VIDEO = "ai_trading_short.mp4"
>>> # ============================================
>>>
>>> def detect_asset(prompt):
...                                     p = prompt.lower()
...                                         mapping = {
...                                                 "bitcoin": ("BTC-USD", "Bitcoin"),
...                                                         "btc": ("BTC-USD", "Bitcoin"),
...                                                                 "ethereum": ("ETH-USD", "Ethereum"),
...                                                                         "eth": ("ETH-USD", "Ethereum"),
...                                                                                 "solana": ("SOL-USD", "Solana"),
...                                                                                         "nifty": ("^NSEI", "Nifty 50"),
...                                                                                                 "bank nifty": ("^NSEBANK", "Bank Nifty"),
...                                                                                                         "gold": ("GC=F", "Gold"),
...                                                                                                                 "reliance": ("RELIANCE.NS", "Reliance"),
...                                                                                                                         "tata": ("TATASTEEL.NS", "Tata Steel"),
...                                                                                                                             }
...                                                                                                                                 for key, val in mapping.items():
...                                                                                                                                                                   \          if key in p:
...                                                                                                                                                                   \                                                          return val
...                                                                                                                                                                   \                                                              return "BTC-USD", "Bitcoin"
...                                                                                                                                                                   \
  File "<python-input-110>", line 3
    mapping = {
IndentationError: unexpected indent
>>> def generate_chart_and_data(ticker, asset_name):
...                                         print(f"1. {asset_name} ({ticker}) ka live data nikaala ja raha hai...")
...                                             try:
...                                                                                             df = yf.Ticker(ticker).history(period="7d", interval="1h")
...                                                                                                     prices = [float(x) for x in df['Close'].dropna().tolist()]
...                                                                                                         except Exception:
...                                                                                                                                                         prices = [\]
...
  File "<python-input-111>", line 3
    try:
IndentationError: unexpected indent
>>>     # Agar internet ya Yahoo Finance slow ho toh fallback data
>>>     if len(prices) < 5:
  File "<python-input-113>", line 1
    if len(prices) < 5:
IndentationError: unexpected indent
>>>         print("Live data slow hai, sample market data use ho raha hai...")
  File "<python-input-114>", line 1
    print("Live data slow hai, sample market data use ho raha hai...")
IndentationError: unexpected indent
>>>         prices = [65200, 65800, 65400, 66100, 66900, 66500, 67400, 68200, 67900, 68850]
  File "<python-input-115>", line 1
    prices = [65200, 65800, 65400, 66100, 66900, 66500, 67400, 68200, 67900, 68850]
IndentationError: unexpected indent
>>>
>>>     latest_price = round(prices[-1], 2)
  File "<python-input-117>", line 1
    latest_price = round(prices[-1], 2)
IndentationError: unexpected indent
>>>     start_price = round(prices[0], 2)
  File "<python-input-118>", line 1
    start_price = round(prices[0], 2)
IndentationError: unexpected indent
>>>     high_price = round(max(prices), 2)
  File "<python-input-119>", line 1
    high_price = round(max(prices), 2)
IndentationError: unexpected indent
>>>     low_price = round(min(prices), 2)
  File "<python-input-120>", line 1
    low_price = round(min(prices), 2)
IndentationError: unexpected indent
>>>     change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
  File "<python-input-121>", line 1
    change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
IndentationError: unexpected indent
>>>     trend = "Bullish" if change_pct >= 0 else "Bearish"
  File "<python-input-122>", line 1
    trend = "Bullish" if change_pct >= 0 else "Bearish"
IndentationError: unexpected indent
>>>
>>>     # 9:16 Vertical Chart banana
>>>     plt.style.use('dark_background')
  File "<python-input-125>", line 1
    plt.style.use('dark_background')
IndentationError: unexpected indent
>>>     fig, ax = plt.subplots(figsize=(9, 16), dpi=100)
  File "<python-input-126>", line 1
    fig, ax = plt.subplots(figsize=(9, 16), dpi=100)
IndentationError: unexpected indent
>>>     fig.patch.set_facecolor('#090d16')
  File "<python-input-127>", line 1
    fig.patch.set_facecolor('#090d16')
IndentationError: unexpected indent
>>>     ax.set_facecolor('#090d16')
  File "<python-input-128>", line 1
    ax.set_facecolor('#090d16')
IndentationError: unexpected indent
>>>
>>>     line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
  File "<python-input-130>", line 1
    line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
IndentationError: unexpected indent
>>>     x_vals = list(range(len(prices)))
  File "<python-input-131>", line 1
    x_vals = list(range(len(prices)))
IndentationError: unexpected indent
>>>     ax.plot(x_vals, prices, color=line_color, linewidth=5)
  File "<python-input-132>", line 1
    ax.plot(x_vals, prices, color=line_color, linewidth=5)
IndentationError: unexpected indent
>>>     ax.fill_between(x_vals, prices, min(prices), color=line_color, alpha=0.2)
  File "<python-input-133>", line 1
    ax.fill_between(x_vals, prices, min(prices), color=line_color, alpha=0.2)
IndentationError: unexpected indent
>>>
>>>     ax.set_title(
  File "<python-input-135>", line 1
    ax.set_title(
IndentationError: unexpected indent
>>>         f"{asset_name.upper()} LIVE UPDATE\nPrice: {latest_price} ({change_pct}%)",
  File "<python-input-136>", line 1
    f"{asset_name.upper()} LIVE UPDATE\nPrice: {latest_price} ({change_pct}%)",
IndentationError: unexpected indent
>>>         fontsize=26, fontweight='bold', color='white', pad=35
  File "<python-input-137>", line 1
    fontsize=26, fontweight='bold', color='white', pad=35
IndentationError: unexpected indent
>>>     )
  File "<python-input-138>", line 1
    )
IndentationError: unexpected indent
>>>     ax.grid(color='#1e293b', linestyle='--', linewidth=1)
  File "<python-input-139>", line 1
    ax.grid(color='#1e293b', linestyle='--', linewidth=1)
IndentationError: unexpected indent
>>>     ax.set_xticks([])
  File "<python-input-140>", line 1
    ax.set_xticks([])
IndentationError: unexpected indent
>>>     ax.tick_params(axis='y', labelsize=14)
  File "<python-input-141>", line 1
    ax.tick_params(axis='y', labelsize=14)
IndentationError: unexpected indent
>>>
>>>     for spine in ['top', 'right', 'bottom']:
  File "<python-input-143>", line 1
    for spine in ['top', 'right', 'bottom']:
IndentationError: unexpected indent
>>>         ax.spines[spine].set_visible(False)
  File "<python-input-144>", line 1
    ax.spines[spine].set_visible(False)
IndentationError: unexpected indent
>>>
>>>     plt.tight_layout(rect=[0.04, 0.28, 0.96, 0.88])
  File "<python-input-146>", line 1
    plt.tight_layout(rect=[0.04, 0.28, 0.96, 0.88])
IndentationError: unexpected indent
>>>     base_img = "base_chart.png"
  File "<python-input-147>", line 1
    base_img = "base_chart.png"
IndentationError: unexpected indent
>>>     plt.savefig(base_img, facecolor=fig.get_facecolor())
  File "<python-input-148>", line 1
    plt.savefig(base_img, facecolor=fig.get_facecolor())
IndentationError: unexpected indent
>>>     plt.close(fig)
  File "<python-input-149>", line 1
    plt.close(fig)
IndentationError: unexpected indent
>>>
>>>     return base_img, latest_price, high_price, low_price, change_pct, trend
  File "<python-input-151>", line 1
    return base_img, latest_price, high_price, low_price, change_pct, trend
IndentationError: unexpected indent
>>>
>>> def build_auto_script(asset_name, price, high_price, low_price, change_pct, trend):
...                                             print("2. Automatic viral trading script aur subtitles ban rahe hain...")
...                                                 direction = "zabardast tezi" if change_pct >= 0 else "badi girawat"
...                                                     action_line = (
...                                                             f"Agla bada breakout {high_price} ke upar aayega!"
...                                                                     if change_pct >= 0
...                                                                             else f"Neeche {low_price} par strong support zone hai!"
...                                                                                 )
...
  File "<python-input-153>", line 3
    direction = "zabardast tezi" if change_pct >= 0 else "badi girawat"
IndentationError: unexpected indent
>>>     lines = [
  File "<python-input-154>", line 1
    lines = [
IndentationError: unexpected indent
>>>         f" {asset_name} mein aaj {direction} dikh rahi hai!",
  File "<python-input-155>", line 1
    f" {asset_name} mein aaj {direction} dikh rahi hai!",
IndentationError: unexpected indent
>>>         f"Abhi live price {price} par trade kar raha hai.",
  File "<python-input-156>", line 1
    f"Abhi live price {price} par trade kar raha hai.",
IndentationError: unexpected indent
>>>         f"Pichle 7 din mein market {change_pct}% move hua hai.",
  File "<python-input-157>", line 1
    f"Pichle 7 din mein market {change_pct}% move hua hai.",
IndentationError: unexpected indent
>>>         f"Is hafte ka high {high_price} aur low {low_price} raha.",
  File "<python-input-158>", line 1
    f"Is hafte ka high {high_price} aur low {low_price} raha.",
IndentationError: unexpected indent
>>>         f"Market ka overall trend abhi {trend} hai.",
  File "<python-input-159>", line 1
    f"Market ka overall trend abhi {trend} hai.",
IndentationError: unexpected indent
>>>         action_line,
  File "<python-input-160>", line 1
    action_line,
IndentationError: unexpected indent
>>>         "Daily live trading updates ke liye abhi subscribe karein!"
  File "<python-input-161>", line 1
    "Daily live trading updates ke liye abhi subscribe karein!"
IndentationError: unexpected indent
>>>     ]
  File "<python-input-162>", line 1
    ]
IndentationError: unexpected indent
>>>     full_script = " ".join(lines)
  File "<python-input-163>", line 1
    full_script = " ".join(lines)
IndentationError: unexpected indent
>>>     print(f"\n--- Script ---\n{full_script}\n--------------\n")
  File "<python-input-164>", line 1
    print(f"\n--- Script ---\n{full_script}\n--------------\n")
IndentationError: unexpected indent
>>>     return lines, full_script
  File "<python-input-165>", line 1
    return lines, full_script
IndentationError: unexpected indent
>>>
>>> def create_voiceover(text):
...                                                 print("3. AI Voiceover generate ho raha hai...")
...                                                     audio_path = "voiceover.mp3"
...                                                         tts = gTTS(text=text, lang="hi", slow=False)
...                                                             tts.save(audio_path)
...                                                                 return audio_path
...
  File "<python-input-167>", line 3
    audio_path = "voiceover.mp3"
IndentationError: unexpected indent
>>> def draw_subtitle_frame(base_img_path, text, idx):
...                                                     img = Image.open(base_img_path).convert("RGB")
...                                                         draw = ImageDraw.Draw(img)
...                                                             width, height = img.size
...
  File "<python-input-168>", line 3
    draw = ImageDraw.Draw(img)
IndentationError: unexpected indent
>>>     # Har system par chalne wala safe font loader
>>>     font = None
  File "<python-input-170>", line 1
    font = None
IndentationError: unexpected indent
>>>     for font_name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"]:
  File "<python-input-171>", line 1
    for font_name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"]:
IndentationError: unexpected indent
>>>         try:
  File "<python-input-172>", line 1
    try:
IndentationError: unexpected indent
>>>             font = ImageFont.truetype(font_name, 38)
  File "<python-input-173>", line 1
    font = ImageFont.truetype(font_name, 38)
IndentationError: unexpected indent
>>>             break
  File "<python-input-174>", line 1
    break
IndentationError: unexpected indent
>>>         except Exception:
  File "<python-input-175>", line 1
    except Exception:
IndentationError: unexpected indent
>>>             continue
  File "<python-input-176>", line 1
    continue
IndentationError: unexpected indent
>>>     if font is None:
  File "<python-input-177>", line 1
    if font is None:
IndentationError: unexpected indent
>>>         font = ImageFont.load_default()
  File "<python-input-178>", line 1
    font = ImageFont.load_default()
IndentationError: unexpected indent
>>>
>>>     # Text ko 2 choti lines mein todna
>>>     words = text.split()
  File "<python-input-181>", line 1
    words = text.split()
IndentationError: unexpected indent
>>>     mid = max(1, len(words) // 2)
  File "<python-input-182>", line 1
    mid = max(1, len(words) // 2)
IndentationError: unexpected indent
>>>     line1 = " ".join(words[:mid])
  File "<python-input-183>", line 1
    line1 = " ".join(words[:mid])
IndentationError: unexpected indent
>>>     line2 = " ".join(words[mid:])
  File "<python-input-184>", line 1
    line2 = " ".join(words[mid:])
IndentationError: unexpected indent
>>>
>>>     box_top = int(height * 0.74)
  File "<python-input-186>", line 1
    box_top = int(height * 0.74)
IndentationError: unexpected indent
>>>     box_bottom = int(height * 0.86)
  File "<python-input-187>", line 1
    box_bottom = int(height * 0.86)
IndentationError: unexpected indent
>>>     draw.rectangle(
  File "<python-input-188>", line 1
    draw.rectangle(
IndentationError: unexpected indent
>>>         [(50, box_top), (width - 50, box_bottom)],
  File "<python-input-189>", line 1
    [(50, box_top), (width - 50, box_bottom)],
IndentationError: unexpected indent
>>>         fill=(18, 24, 38),
  File "<python-input-190>", line 1
    fill=(18, 24, 38),
IndentationError: unexpected indent
>>>         outline=(0, 255, 136),
  File "<python-input-191>", line 1
    outline=(0, 255, 136),
IndentationError: unexpected indent
>>>         width=4
  File "<python-input-192>", line 1
    width=4
IndentationError: unexpected indent
>>>     )
  File "<python-input-193>", line 1
    )
IndentationError: unexpected indent
>>>
>>>     # Safe text positioning (bina anchor crash ke)
>>>     draw.text((90, box_top + 35), line1.upper(), fill=(255, 230, 0), font=font)
  File "<python-input-196>", line 1
    draw.text((90, box_top + 35), line1.upper(), fill=(255, 230, 0), font=font)
IndentationError: unexpected indent
>>>     if line2:
  File "<python-input-197>", line 1
    if line2:
IndentationError: unexpected indent
>>>         draw.text((90, box_top + 95), line2.upper(), fill=(255, 255, 255), font=font)
  File "<python-input-198>", line 1
    draw.text((90, box_top + 95), line2.upper(), fill=(255, 255, 255), font=font)
IndentationError: unexpected indent
>>>
>>>     frame_path = f"frame_{idx}.png"
  File "<python-input-200>", line 1
    frame_path = f"frame_{idx}.png"
IndentationError: unexpected indent
>>>     img.save(frame_path)
  File "<python-input-201>", line 1
    img.save(frame_path)
IndentationError: unexpected indent
>>>     return frame_path
  File "<python-input-202>", line 1
    return frame_path
IndentationError: unexpected indent
>>>
>>> def render_video(base_img, lines, audio_path, output_path):
...                                                         print("4. Subtitles ke saath MP4 video render ho raha hai...")
...                                                             audio_clip = AudioFileClip(audio_path)
...                                                                 total_duration = audio_clip.duration
...                                                                     total_chars = sum(len(x) for x in lines) or 1
...
  File "<python-input-204>", line 3
    audio_clip = AudioFileClip(audio_path)
IndentationError: unexpected indent
>>>     clips = []
  File "<python-input-205>", line 1
    clips = []
IndentationError: unexpected indent
>>>     temp_files = []
  File "<python-input-206>", line 1
    temp_files = []
IndentationError: unexpected indent
>>>
>>>     for i, line in enumerate(lines):
  File "<python-input-208>", line 1
    for i, line in enumerate(lines):
IndentationError: unexpected indent
>>>         f_path = draw_subtitle_frame(base_img, line, i)
  File "<python-input-209>", line 1
    f_path = draw_subtitle_frame(base_img, line, i)
IndentationError: unexpected indent
>>>         temp_files.append(f_path)
  File "<python-input-210>", line 1
    temp_files.append(f_path)
IndentationError: unexpected indent
>>>         dur = (len(line) / total_chars) * total_duration
  File "<python-input-211>", line 1
    dur = (len(line) / total_chars) * total_duration
IndentationError: unexpected indent
>>>
>>>         if MOVIEPY_V2:
  File "<python-input-213>", line 1
    if MOVIEPY_V2:
IndentationError: unexpected indent
>>>             clip = ImageClip(f_path).with_duration(dur)
  File "<python-input-214>", line 1
    clip = ImageClip(f_path).with_duration(dur)
IndentationError: unexpected indent
>>>         else:
  File "<python-input-215>", line 1
    else:
IndentationError: unexpected indent
>>>             clip = ImageClip(f_path).set_duration(dur)
  File "<python-input-216>", line 1
    clip = ImageClip(f_path).set_duration(dur)
IndentationError: unexpected indent
>>>         clips.append(clip)
  File "<python-input-217>", line 1
    clips.append(clip)
IndentationError: unexpected indent
>>>
>>>     final_video = concatenate_videoclips(clips, method="compose")
  File "<python-input-219>", line 1
    final_video = concatenate_videoclips(clips, method="compose")
IndentationError: unexpected indent
>>>     if MOVIEPY_V2:
  File "<python-input-220>", line 1
    if MOVIEPY_V2:
IndentationError: unexpected indent
>>>         final_video = final_video.with_audio(audio_clip)
  File "<python-input-221>", line 1
    final_video = final_video.with_audio(audio_clip)
IndentationError: unexpected indent
>>>     else:
  File "<python-input-222>", line 1
    else:
IndentationError: unexpected indent
>>>         final_video = final_video.set_audio(audio_clip)
  File "<python-input-223>", line 1
    final_video = final_video.set_audio(audio_clip)
IndentationError: unexpected indent
>>>
>>>     final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
  File "<python-input-225>", line 1
    final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
IndentationError: unexpected indent
>>>
>>>     audio_clip.close()
  File "<python-input-227>", line 1
    audio_clip.close()
IndentationError: unexpected indent
>>>     final_video.close()
  File "<python-input-228>", line 1
    final_video.close()
IndentationError: unexpected indent
>>>     for f in temp_files:
  File "<python-input-229>", line 1
    for f in temp_files:
IndentationError: unexpected indent
>>>         if os.path.exists(f):
  File "<python-input-230>", line 1
    if os.path.exists(f):
IndentationError: unexpected indent
>>>             os.remove(f)
  File "<python-input-231>", line 1
    os.remove(f)
IndentationError: unexpected indent
>>>
>>>     print(f"\nSUCCESS! Video taiyaar hai: {output_path}")
  File "<python-input-233>", line 1
    print(f"\nSUCCESS! Video taiyaar hai: {output_path}")
IndentationError: unexpected indent
>>>
>>> if __name__ == "__main__":
...                                                             try:
...                                                                                                                                 ticker, asset = detect_asset(USER_\PROMPT)
...                                                                                                                                         chart_img, price, high_p, \low_p, pct, trend = generate_chart_and_data(ticker, asset)
...                                                                                                                                                 sub_lines, script_\text = build_auto_script(asset, price, high_p, low_p, pct, trend)
...                                                                                                                                                         audio_file\ = create_voiceover(script_text)
...                                                                                                                                                                 re\nder_video(chart_img, sub_lines, audio_file, OUTPUT_VIDEO)
...                                                                                                                                                                   \  except Exception as e:
...                                                                                                                                                                   \                                                                      print("\n--- EXACT ERROR NICHE DEKHEIN ---")
...                                                                                                                                                                   \                                                                              traceback.print_exc()
...                                                                                                                                                                   \
  File "<python-input-235>", line 4
    chart_img, price, high_p, low_p, pct, trend = generate_chart_and_data(ticker, asset)
IndentationError: unexpected indent
>>> pip install google-genai yfinance matplotlib requests gtts moviepy pillow
  File "<python-input-236>", line 1
    pip install google-genai yfinance matplotlib requests gtts moviepy pillow
        ^^^^^^^
SyntaxError: invalid syntax
>>> import os
>>> import json
>>> import requests
Traceback (most recent call last):
  File "<python-input-239>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
>>> import yfinance as yf
Traceback (most recent call last):
  File "<python-input-240>", line 1, in <module>
    import yfinance as yf
ModuleNotFoundError: No module named 'yfinance'
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<python-input-241>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> from google import genai
Traceback (most recent call last):
  File "<python-input-242>", line 1, in <module>
    from google import genai
ModuleNotFoundError: No module named 'google'
>>> from google.genai import types
Traceback (most recent call last):
  File "<python-input-243>", line 1, in <module>
    from google.genai import types
ModuleNotFoundError: No module named 'google'
>>> from gtts import gTTS
Traceback (most recent call last):
  File "<python-input-244>", line 1, in <module>
    from gtts import gTTS
ModuleNotFoundError: No module named 'gtts'
>>> from PIL import Image, ImageDraw, ImageFont
Traceback (most recent call last):
  File "<python-input-245>", line 1, in <module>
    from PIL import Image, ImageDraw, ImageFont
ModuleNotFoundError: No module named 'PIL'
>>>
>>> # MoviePy v1 aur v2 dono ke liye support
>>> try:
...                                                                 from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
...                                                                     MOVIEPY_V2 = True
...                                                                     except ImportError:
...                                                                                                                                         from moviepy.editor import\ ImageClip, AudioFileClip, concatenate_videoclips
...                                                                                                                                             MOVIEPY_V2 = False
...
  File "<python-input-248>", line 3
    MOVIEPY_V2 = True
IndentationError: unexpected indent
>>> # ================= API KEYS & PROMPT =================
>>> GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"          # Apni Gemini API key yahan daalein
>>> ELEVENLABS_API_KEY = "YOUR_ELEVENLABS_API_KEY"  # Optional: Na hone par free voice use hogi
>>> ELEVENLABS_VOICE_ID = "pNInz6obpgDQGcFmaJgB"    # Default Adam Voice ID
>>>
>>> # Yahan bas apna 1 single prompt likhein:
>>> USER_PROMPT = "Bitcoin ka live trading analysis aur breakout update par viral short video banao"
>>> OUTPUT_VIDEO = "viral_trading_short.mp4"
>>> # =====================================================
>>>
>>> client = genai.Client(api_key=GEMINI_API_KEY)
Traceback (most recent call last):
  File "<python-input-259>", line 1, in <module>
    client = genai.Client(api_key=GEMINI_API_KEY)
             ^^^^^
NameError: name 'genai' is not defined
>>>
>>> def extract_ticker_from_prompt(prompt):
...                                                                     print("1. AI aapke prompt se market ticker pehchan raha hai...")
...                                                                         res = client.models.generate_content(
...                                                                                 model="gemini-2.5-flash",
...                                                                                         contents=(
...                                                                                                     f"User prompt: '{prompt}'. "
...                                                                                                                 "Extract the Yahoo Finance ticker symbol and asset\ name from this prompt. "
...                                                                                                                             "Examples: Bitcoin -> BTC-USD, Ethereu\m -> ETH-USD, Nifty 50 -> ^NSEI, "
...                                                                                                                                         "Bank Nifty -> ^NSEBANK, G\old -> GC=F, Reliance -> RELIANCE.NS. "
...                                                                                                                                                     "If no specifi\c asset is mentioned, default to BTC-USD and Bitcoin. "
...                                                                                                                                                                 "R\eturn ONLY valid JSON like: {\"ticker\": \"BTC-USD\", \"asset_name\": \"Bitcoin\"}"
...                                                                                                                                                                   \      ),
...                                                                                                                                                                   \              config=types.GenerateContentConfig(response_mime_type="application/json")
...                                                                                                                                                                   \                  )
...                                                                                                                                                                   \                      data = json.loads(res.text)
...                                                                                                                                                                   \                          return data.get("ticker", "BTC-USD"), data.get("asset_name", "Bitcoin")
...                                                                                                                                                                   \
  File "<python-input-261>", line 3
    res = client.models.generate_content(
IndentationError: unexpected indent
>>> def generate_chart_base(ticker, asset_name):
...                                                                         print(f"2. {asset_name} ({ticker}) ka live chart download ho raha hai...")
...                                                                             df = yf.Ticker(ticker).history(period="7d", interval="1h")
...                                                                                 if df.empty:
...                                                                                                                                                                 df\ = yf.Ticker("BTC-USD").history(period="7d", interval="1h")
...                                                                                                                                                                   \      asset_name = "Bitcoin"
...                                                                                                                                                                   \
  File "<python-input-262>", line 3
    df = yf.Ticker(ticker).history(period="7d", interval="1h")
IndentationError: unexpected indent
>>>     latest_price = round(df['Close'].iloc[-1], 2)
  File "<python-input-263>", line 1
    latest_price = round(df['Close'].iloc[-1], 2)
IndentationError: unexpected indent
>>>     start_price = round(df['Close'].iloc[0], 2)
  File "<python-input-264>", line 1
    start_price = round(df['Close'].iloc[0], 2)
IndentationError: unexpected indent
>>>     change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
  File "<python-input-265>", line 1
    change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
IndentationError: unexpected indent
>>>     trend = "Bullish" if change_pct >= 0 else "Bearish"
  File "<python-input-266>", line 1
    trend = "Bullish" if change_pct >= 0 else "Bearish"
IndentationError: unexpected indent
>>>
>>>     plt.style.use('dark_background')
  File "<python-input-268>", line 1
    plt.style.use('dark_background')
IndentationError: unexpected indent
>>>     fig, ax = plt.subplots(figsize=(9, 16), dpi=100)
  File "<python-input-269>", line 1
    fig, ax = plt.subplots(figsize=(9, 16), dpi=100)
IndentationError: unexpected indent
>>>     fig.patch.set_facecolor('#090d16')
  File "<python-input-270>", line 1
    fig.patch.set_facecolor('#090d16')
IndentationError: unexpected indent
>>>     ax.set_facecolor('#090d16')
  File "<python-input-271>", line 1
    ax.set_facecolor('#090d16')
IndentationError: unexpected indent
>>>
>>>     color = '#00ff88' if change_pct >= 0 else '#ff3366'
  File "<python-input-273>", line 1
    color = '#00ff88' if change_pct >= 0 else '#ff3366'
IndentationError: unexpected indent
>>>     ax.plot(df.index, df['Close'], color=color, linewidth=4.5)
  File "<python-input-274>", line 1
    ax.plot(df.index, df['Close'], color=color, linewidth=4.5)
IndentationError: unexpected indent
>>>     ax.fill_between(df.index, df['Close'], df['Close'].min(), color=color, alpha=0.18)
  File "<python-input-275>", line 1
    ax.fill_between(df.index, df['Close'], df['Close'].min(), color=color, alpha=0.18)
IndentationError: unexpected indent
>>>
>>>     ax.set_title(f"{asset_name.upper()} LIVE CHART\nPrice: {latest_price} ({change_pct}%)",
  File "<python-input-277>", line 1
    ax.set_title(f"{asset_name.upper()} LIVE CHART\nPrice: {latest_price} ({change_pct}%)",
IndentationError: unexpected indent
>>>                  fontsize=28, fontweight='bold', color='white', pad=35)
  File "<python-input-278>", line 1
    fontsize=28, fontweight='bold', color='white', pad=35)
IndentationError: unexpected indent
>>>     ax.grid(color='#1e293b', linestyle='--', linewidth=1)
  File "<python-input-279>", line 1
    ax.grid(color='#1e293b', linestyle='--', linewidth=1)
IndentationError: unexpected indent
>>>     ax.tick_params(axis='x', rotation=25, labelsize=11)
  File "<python-input-280>", line 1
    ax.tick_params(axis='x', rotation=25, labelsize=11)
IndentationError: unexpected indent
>>>     ax.tick_params(axis='y', labelsize=13)
  File "<python-input-281>", line 1
    ax.tick_params(axis='y', labelsize=13)
IndentationError: unexpected indent
>>>
>>>     for spine in ['top', 'right']:
  File "<python-input-283>", line 1
    for spine in ['top', 'right']:
IndentationError: unexpected indent
>>>         ax.spines[spine].set_visible(False)
  File "<python-input-284>", line 1
    ax.spines[spine].set_visible(False)
IndentationError: unexpected indent
>>>
>>>     # Neeche subtitles ke liye jagah chhodna
>>>     plt.tight_layout(rect=[0.04, 0.28, 0.96, 0.88])
  File "<python-input-287>", line 1
    plt.tight_layout(rect=[0.04, 0.28, 0.96, 0.88])
IndentationError: unexpected indent
>>>     base_img = "base_chart.png"
  File "<python-input-288>", line 1
    base_img = "base_chart.png"
IndentationError: unexpected indent
>>>     plt.savefig(base_img, facecolor=fig.get_facecolor())
  File "<python-input-289>", line 1
    plt.savefig(base_img, facecolor=fig.get_facecolor())
IndentationError: unexpected indent
>>>     plt.close()
  File "<python-input-290>", line 1
    plt.close()
IndentationError: unexpected indent
>>>
>>>     return base_img, latest_price, change_pct, trend
  File "<python-input-292>", line 1
    return base_img, latest_price, change_pct, trend
IndentationError: unexpected indent
>>>
>>> def generate_script_lines(prompt, asset_name, price, change_pct, trend):
...                                                                             print("3. Gemini AI viral script aur subtitles bana raha hai...")
...                                                                                 ai_prompt = (
...                                                                                         f"User request: '{prompt}'. "
...                                                                                                 f"Live Market Data: Asset={asset_name}, Current Price={price}, 7-D\ay Change={change_pct}%, Trend={trend}. "
...                                                                                                         "Create a high-retention 25-second YouTube Shorts trading \script in Hinglish (Roman Hindi). "
...                                                                                                                 "Break the script into 6 to 8 short, punchy subtit\le lines (maximum 6 to 8 words per line). "
...                                                                                                                         "Return ONLY valid JSON in this exact form\at: "
...                                                                                                                                 "{\"lines\": [\"Line 1\", \"Line 2\\", \"Line 3\"]}"
...                                                                                                                                     )
...                                                                                                                                         res = client.models.genera\te_content(
...                                                                                                                                                 model="gemini-2.5-\flash",
...                                                                                                                                                         contents=a\i_prompt,
...                                                                                                                                                                 co\nfig=types.GenerateContentConfig(response_mime_type="application/json")
...                                                                                                                                                                   \  )
...                                                                                                                                                                   \      lines = json.loads(res.text).get("lines", [])
...                                                                                                                                                                   \          full_script = " ".join(lines)
...                                                                                                                                                                   \              print(f"\n--- Generated Script ---\n{full_script}\n------------------------\n")
...                                                                                                                                                                   \                  return lines, full_script
...                                                                                                                                                                   \
  File "<python-input-294>", line 3
    ai_prompt = (
IndentationError: unexpected indent
>>> def generate_voiceover(full_script):
...                                                                                 audio_path = "voiceover.mp3"
...                                                                                     if ELEVENLABS_API_KEY and ELEVENLABS_API_KEY != "YOUR_ELEVENLABS_API_KEY":
...                                                                                                                                                                   \          print("4. ElevenLabs se realistic AI voiceover ban raha hai...")
...                                                                                                                                                                   \                  url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
...                                                                                                                                                                   \                          headers = {
...                                                                                                                                                                   \                                      "Accept": "audio/mpeg",
...                                                                                                                                                                   \                                                  "Content-Type": "application/json",
...                                                                                                                                                                   \                                                              "xi-api-key": ELEVENLABS_API_KEY
...                                                                                                                                                                   \                                                                      }
...                                                                                                                                                                   \                                                                              payload = {
...                                                                                                                                                                   \                                                                                          "text": full_script,
...                                                                                                                                                                   \                                                                                                      "model_id": "eleven_multilingual_v2",
...                                                                                                                                                                   \                                                                                                                  "voice_settings": {"stability": 0.5, "similarity_boo\st": 0.75}
...                                                                                                                                                                   \                                                                                                                          }
...                                                                                                                                                                   \                                                                                                                                  response = requests.post(url, json=p\ayload, headers=headers)
...                                                                                                                                                                   \                                                                                                                                          if response.status_code == 2\00:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                with open(audio_path, "wb") as f:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                f.writ\e(response.content)
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                      \      return audio_path
...                                                                                                                                                                   \                                                                                                                                                                      \
              else:
...                                                                                                                                                                   \                                                                                                                                                                      \
                                                                                                          print("ElevenLabs error, free TTS voice use ki ja rahi hai..\.")
...                                                                                                                                                                   \
                                                                                                                                                                      \
  File "<python-input-295>", line 3
    if ELEVENLABS_API_KEY and ELEVENLABS_API_KEY != "YOUR_ELEVENLABS_API_KEY":
IndentationError: unexpected indent
>>>     print("4. Free AI Voiceover generate ho raha hai...")
  File "<python-input-296>", line 1
    print("4. Free AI Voiceover generate ho raha hai...")
IndentationError: unexpected indent
>>>     tts = gTTS(text=full_script, lang="hi", slow=False)
  File "<python-input-297>", line 1
    tts = gTTS(text=full_script, lang="hi", slow=False)
IndentationError: unexpected indent
>>>     tts.save(audio_path)
  File "<python-input-298>", line 1
    tts.save(audio_path)
IndentationError: unexpected indent
>>>     return audio_path
  File "<python-input-299>", line 1
    return audio_path
IndentationError: unexpected indent
>>>
>>> def create_subtitle_frame(base_img_path, subtitle_text, index):
...                                                                                     img = Image.open(base_img_path).convert("RGB")
...                                                                                         draw = ImageDraw.Draw(img)
...                                                                                             width, height = img.size
...
  File "<python-input-301>", line 3
    draw = ImageDraw.Draw(img)
IndentationError: unexpected indent
>>>     try:
  File "<python-input-302>", line 1
    try:
IndentationError: unexpected indent
>>>         font = ImageFont.truetype("arialbd.ttf", 44)
  File "<python-input-303>", line 1
    font = ImageFont.truetype("arialbd.ttf", 44)
IndentationError: unexpected indent
>>>     except Exception:
  File "<python-input-304>", line 1
    except Exception:
IndentationError: unexpected indent
>>>         try:
  File "<python-input-305>", line 1
    try:
IndentationError: unexpected indent
>>>             font = ImageFont.load_default(size=42)
  File "<python-input-306>", line 1
    font = ImageFont.load_default(size=42)
IndentationError: unexpected indent
>>>         except Exception:
  File "<python-input-307>", line 1
    except Exception:
IndentationError: unexpected indent
>>>             font = ImageFont.load_default()
  File "<python-input-308>", line 1
    font = ImageFont.load_default()
IndentationError: unexpected indent
>>>
>>>     # Text ko 2 lines mein wrap karna taaki screen se bahar na jaye
>>>     words = subtitle_text.split()
  File "<python-input-311>", line 1
    words = subtitle_text.split()
IndentationError: unexpected indent
>>>     mid = len(words) // 2
  File "<python-input-312>", line 1
    mid = len(words) // 2
IndentationError: unexpected indent
>>>     if len(words) > 4:
  File "<python-input-313>", line 1
    if len(words) > 4:
IndentationError: unexpected indent
>>>         wrapped_text = " ".join(words[:mid]) + "\n" + " ".join(words[mid:])
  File "<python-input-314>", line 1
    wrapped_text = " ".join(words[:mid]) + "\n" + " ".join(words[mid:])
IndentationError: unexpected indent
>>>     else:
  File "<python-input-315>", line 1
    else:
IndentationError: unexpected indent
>>>         wrapped_text = subtitle_text
  File "<python-input-316>", line 1
    wrapped_text = subtitle_text
IndentationError: unexpected indent
>>>
>>>     # Subtitle background box
>>>     box_top = int(height * 0.73)
  File "<python-input-319>", line 1
    box_top = int(height * 0.73)
IndentationError: unexpected indent
>>>     box_bottom = int(height * 0.86)
  File "<python-input-320>", line 1
    box_bottom = int(height * 0.86)
IndentationError: unexpected indent
>>>     draw.rounded_rectangle(
  File "<python-input-321>", line 1
    draw.rounded_rectangle(
IndentationError: unexpected indent
>>>         [(60, box_top), (width - 60, box_bottom)],
  File "<python-input-322>", line 1
    [(60, box_top), (width - 60, box_bottom)],
IndentationError: unexpected indent
>>>         radius=25,
  File "<python-input-323>", line 1
    radius=25,
IndentationError: unexpected indent
>>>         fill=(20, 26, 41),
  File "<python-input-324>", line 1
    fill=(20, 26, 41),
IndentationError: unexpected indent
>>>         outline=(0, 255, 136),
  File "<python-input-325>", line 1
    outline=(0, 255, 136),
IndentationError: unexpected indent
>>>         width=4
  File "<python-input-326>", line 1
    width=4
IndentationError: unexpected indent
>>>     )
  File "<python-input-327>", line 1
    )
IndentationError: unexpected indent
>>>
>>>     # Subtitle text draw karna
>>>     draw.multiline_text(
  File "<python-input-330>", line 1
    draw.multiline_text(
IndentationError: unexpected indent
>>>         (width // 2, (box_top + box_bottom) // 2),
  File "<python-input-331>", line 1
    (width // 2, (box_top + box_bottom) // 2),
IndentationError: unexpected indent
>>>         wrapped_text.upper(),
  File "<python-input-332>", line 1
    wrapped_text.upper(),
IndentationError: unexpected indent
>>>         fill=(255, 230, 0),
  File "<python-input-333>", line 1
    fill=(255, 230, 0),
IndentationError: unexpected indent
>>>         font=font,
  File "<python-input-334>", line 1
    font=font,
IndentationError: unexpected indent
>>>         anchor="mm",
  File "<python-input-335>", line 1
    anchor="mm",
IndentationError: unexpected indent
>>>         align="center",
  File "<python-input-336>", line 1
    align="center",
IndentationError: unexpected indent
>>>         spacing=12
  File "<python-input-337>", line 1
    spacing=12
IndentationError: unexpected indent
>>>     )
  File "<python-input-338>", line 1
    )
IndentationError: unexpected indent
>>>
>>>     frame_path = f"sub_frame_{index}.png"
  File "<python-input-340>", line 1
    frame_path = f"sub_frame_{index}.png"
IndentationError: unexpected indent
>>>     img.save(frame_path)
  File "<python-input-341>", line 1
    img.save(frame_path)
IndentationError: unexpected indent
>>>     return frame_path
  File "<python-input-342>", line 1
    return frame_path
IndentationError: unexpected indent
>>>
>>> def build_final_video(base_img, lines, audio_path, output_path):
...                                                                                         print("5. Animated Subtitles aur Final Video render ho raha hai...")
...                                                                                             audio_clip = AudioFileClip(audio_path)
...                                                                                                 total_duration = audio_clip.duration
...
  File "<python-input-344>", line 3
    audio_clip = AudioFileClip(audio_path)
IndentationError: unexpected indent
>>>     total_chars = sum(len(line) for line in lines) or 1
  File "<python-input-345>", line 1
    total_chars = sum(len(line) for line in lines) or 1
IndentationError: unexpected indent
>>>     clips = []
  File "<python-input-346>", line 1
    clips = []
IndentationError: unexpected indent
>>>     temp_files = []
  File "<python-input-347>", line 1
    temp_files = []
IndentationError: unexpected indent
>>>
>>>     for i, line in enumerate(lines):
  File "<python-input-349>", line 1
    for i, line in enumerate(lines):
IndentationError: unexpected indent
>>>         frame_file = create_subtitle_frame(base_img, line, i)
  File "<python-input-350>", line 1
    frame_file = create_subtitle_frame(base_img, line, i)
IndentationError: unexpected indent
>>>         temp_files.append(frame_file)
  File "<python-input-351>", line 1
    temp_files.append(frame_file)
IndentationError: unexpected indent
>>>         # Har subtitle line ki timing uski length ke hisaab se set hoti hai
>>>         line_duration = (len(line) / total_chars) * total_duration
  File "<python-input-353>", line 1
    line_duration = (len(line) / total_chars) * total_duration
IndentationError: unexpected indent
>>>
>>>         if MOVIEPY_V2:
  File "<python-input-355>", line 1
    if MOVIEPY_V2:
IndentationError: unexpected indent
>>>             clip = ImageClip(frame_file).with_duration(line_duration)
  File "<python-input-356>", line 1
    clip = ImageClip(frame_file).with_duration(line_duration)
IndentationError: unexpected indent
>>>         else:
  File "<python-input-357>", line 1
    else:
IndentationError: unexpected indent
>>>             clip = ImageClip(frame_file).set_duration(line_duration)
  File "<python-input-358>", line 1
    clip = ImageClip(frame_file).set_duration(line_duration)
IndentationError: unexpected indent
>>>         clips.append(clip)
  File "<python-input-359>", line 1
    clips.append(clip)
IndentationError: unexpected indent
>>>
>>>     final_video = concatenate_videoclips(clips, method="compose")
  File "<python-input-361>", line 1
    final_video = concatenate_videoclips(clips, method="compose")
IndentationError: unexpected indent
>>>     if MOVIEPY_V2:
  File "<python-input-362>", line 1
    if MOVIEPY_V2:
IndentationError: unexpected indent
>>>         final_video = final_video.with_audio(audio_clip)
  File "<python-input-363>", line 1
    final_video = final_video.with_audio(audio_clip)
IndentationError: unexpected indent
>>>     else:
  File "<python-input-364>", line 1
    else:
IndentationError: unexpected indent
>>>         final_video = final_video.set_audio(audio_clip)
  File "<python-input-365>", line 1
    final_video = final_video.set_audio(audio_clip)
IndentationError: unexpected indent
>>>
>>>     final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
  File "<python-input-367>", line 1
    final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
IndentationError: unexpected indent
>>>
>>>     audio_clip.close()
  File "<python-input-369>", line 1
    audio_clip.close()
IndentationError: unexpected indent
>>>     final_video.close()
  File "<python-input-370>", line 1
    final_video.close()
IndentationError: unexpected indent
>>>     for f in temp_files:
  File "<python-input-371>", line 1
    for f in temp_files:
IndentationError: unexpected indent
>>>         if os.path.exists(f):
  File "<python-input-372>", line 1
    if os.path.exists(f):
IndentationError: unexpected indent
>>>             os.remove(f)
  File "<python-input-373>", line 1
    os.remove(f)
IndentationError: unexpected indent
>>>
>>>     print(f"\nDONE! Aapka video ban kar taiyaar hai: {output_path}")
  File "<python-input-375>", line 1
    print(f"\nDONE! Aapka video ban kar taiyaar hai: {output_path}")
IndentationError: unexpected indent
>>>
>>> if __name__ == "__main__":
...                                                                                             prompt_input = input(f"Apna prompt likhein (Enter dabayein default ke \liye): ").strip()
...                                                                                                 final_prompt = prompt_input if prompt_input else USER_PROMPT
...
  File "<python-input-377>", line 3
    final_prompt = prompt_input if prompt_input else USER_PROMPT
IndentationError: unexpected indent
>>>     ticker, asset = extract_ticker_from_prompt(final_prompt)
  File "<python-input-378>", line 1
    ticker, asset = extract_ticker_from_prompt(final_prompt)
IndentationError: unexpected indent
>>>     chart_img, price, pct, trend = generate_chart_base(ticker, asset)
  File "<python-input-379>", line 1
    chart_img, price, pct, trend = generate_chart_base(ticker, asset)
IndentationError: unexpected indent
>>>     script_lines, full_text = generate_script_lines(final_prompt, asset, price, pct, trend)
  File "<python-input-380>", line 1
    script_lines, full_text = generate_script_lines(final_prompt, asset, price, pct, trend)
IndentationError: unexpected indent
>>>     voice_file = generate_voiceover(full_text)
  File "<python-input-381>", line 1
    voice_file = generate_voiceover(full_text)
IndentationError: unexpected indent
>>>     build_final_video(chart_img, script_lines, voice_file, OUTPUT_VIDEO)
  File "<python-input-382>", line 1
    build_final_video(chart_img, script_lines, voice_file, OUTPUT_VIDEO)
IndentationError: unexpected indent
>>> import os
>>> import json
>>> import wave
>>> import traceback
>>> import requests
Traceback (most recent call last):
  File "<python-input-387>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
>>> import numpy as np
Traceback (most recent call last):
  File "<python-input-388>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import streamlit as st
Traceback (most recent call last):
  File "<python-input-389>", line 1, in <module>
    import streamlit as st
ModuleNotFoundError: No module named 'streamlit'
>>> import matplotlib
Traceback (most recent call last):
  File "<python-input-390>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> matplotlib.use('Agg')
Traceback (most recent call last):
  File "<python-input-391>", line 1, in <module>
    matplotlib.use('Agg')
    ^^^^^^^^^^
NameError: name 'matplotlib' is not defined
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<python-input-392>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import yfinance as yf
Traceback (most recent call last):
  File "<python-input-393>", line 1, in <module>
    import yfinance as yf
ModuleNotFoundError: No module named 'yfinance'
>>> from gtts import gTTS
Traceback (most recent call last):
  File "<python-input-394>", line 1, in <module>
    from gtts import gTTS
ModuleNotFoundError: No module named 'gtts'
>>> from PIL import Image, ImageDraw, ImageFont
Traceback (most recent call last):
  File "<python-input-395>", line 1, in <module>
    from PIL import Image, ImageDraw, ImageFont
ModuleNotFoundError: No module named 'PIL'
>>>
>>> # MoviePy v1 aur v2 dono ke liye complete support
>>> try:
...                                                                                                 from moviepy import ImageClip, AudioFileClip, concatenate_videocli\ps, CompositeAudioClip
...                                                                                                     MOVIEPY_V2 = True
...                                                                                                     except ImportError:
...                                                                                                                                                                   \                                      from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
...                                                                                                                                                                   \                                          MOVIEPY_V2 = False
...                                                                                                                                                                   \
  File "<python-input-398>", line 3
    MOVIEPY_V2 = True
IndentationError: unexpected indent
>>> # Optional Gemini SDK support
>>> try:
...                                                                                                     from google import genai
...                                                                                                         GEMINI_AVAILABLE = True
...                                                                                                         except ImportError:
...                                                                                                                                                                   \                                              GEMINI_AVAILABLE = False
...                                                                                                                                                                   \
  File "<python-input-400>", line 3
    GEMINI_AVAILABLE = True
IndentationError: unexpected indent
>>> # ================= WEB APP UI SETUP =================
>>> st.set_page_config(page_title="Pro AI Trading Video Studio", page_icon="", layout="centered")
Traceback (most recent call last):
  File "<python-input-402>", line 1, in <module>
    st.set_page_config(page_title="Pro AI Trading Video Studio", page_icon="", layout="centered")
    ^^
NameError: name 'st' is not defined. Did you mean: 'set'?
>>>
>>> st.title(" Pro AI Trading Video Studio")
Traceback (most recent call last):
  File "<python-input-404>", line 1, in <module>
    st.title(" Pro AI Trading Video Studio")
    ^^
NameError: name 'st' is not defined. Did you mean: 'set'?
>>> st.write("1 Prompt se Live RSI Chart, AI Voiceover, Background Music, Animated Subtitles aur YouTube SEO Tags banayein.")
Traceback (most recent call last):
  File "<python-input-405>", line 1, in <module>
    st.write("1 Prompt se Live RSI Chart, AI Voiceover, Background Music, Animated Subtitles aur YouTube SEO Tags banayein.")
    ^^
NameError: name 'st' is not defined. Did you mean: 'set'?
>>>
>>> with st.sidebar:
...                                                                                                         st.header(" Studio Settings")
...                                                                                                             gemini_api_key = st.text_input("Gemini API Key (Option\al)", type="password", help="Custom AI script ke liye. Khali chhodne par Smart Auto-Script banegi.")
...                                                                                                                 eleven_api_key = st.text_input("ElevenLabs API Key\ (Optional)", type="password", help="Khali chhodne par Free Hindi AI Voice use hogi.")
...                                                                                                                     voice_id = st.text_input("ElevenLabs Voice ID"\, value="pNInz6obpgDQGcFmaJgB")
...                                                                                                                         chart_period = st.selectbox("Chart Timefra\me", ["5d", "7d", "1mo", "3mo"], index=1)
...                                                                                                                             enable_bgm = st.checkbox("Add Auto Bac\kground Music (BGM)", value=True)
...                                                                                                                                 bgm_volume = st.slider("BGM Volume\", 0.05, 0.30, 0.12, 0.01)
...
  File "<python-input-407>", line 3
    gemini_api_key = st.text_input("Gemini API Key (Optional)", type="password", help="Custom AI script ke liye. Khali chhodne par Smart Auto-Script banegi.")
IndentationError: unexpected indent
>>> # ================= 1. ASSET & MARKET DATA =================
>>> def detect_asset(prompt):
...                                                                                                             p = prompt.lower()
...                                                                                                                 mapping = {
...                                                                                                                         "bitcoin": ("BTC-USD", "Bitcoin"),
...                                                                                                                                 "btc": ("BTC-USD", "Bitcoin"),
...                                                                                                                                         "ethereum": ("ETH-USD", "E\thereum"),
...                                                                                                                                                 "eth": ("ETH-USD",\ "Ethereum"),
...                                                                                                                                                         "solana": \("SOL-USD", "Solana"),
...                                                                                                                                                                 "s\ol": ("SOL-USD", "Solana"),
...                                                                                                                                                                   \      "bnb": ("BNB-USD", "BNB"),
...                                                                                                                                                                   \              "xrp": ("XRP-USD", "XRP"),
...                                                                                                                                                                   \                      "doge": ("DOGE-USD", "Dogecoin"),
...                                                                                                                                                                   \                              "nifty": ("^NSEI", "Nifty 50"),
...                                                                                                                                                                   \                                      "bank nifty": ("^NSEBANK", "Bank Nifty"),
...                                                                                                                                                                   \                                              "sensex": ("^BSESN", "Sensex"),
...                                                                                                                                                                   \                                                      "gold": ("GC=F", "Gold"),
...                                                                                                                                                                   \                                                              "silver": ("SI=F", "Silver"),
...                                                                                                                                                                   \                                                                      "reliance": ("RELIANCE.NS", "Reliance"),
...                                                                                                                                                                   \                                                                              "tata": ("TATASTEEL.NS", "Tata Steel"),
...                                                                                                                                                                   \                                                                                      "hdfc": ("HDFCBANK.NS", "HDFC Bank"),
...                                                                                                                                                                   \                                                                                              "infosys": ("INFY.NS", "Infosys"),
...                                                                                                                                                                   \                                                                                                      "zomato": ("ZOMATO.NS", "Zomato"),
...                                                                                                                                                                   \                                                                                                          }
...                                                                                                                                                                   \                                                                                                              for key, val in mapping.items():
...                                                                                                                                                                   \                                                                                                                                                                      \                                                            if key in p:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                      \              return val



                  return "BTC-USD", "Bitcoin"




  File "<python-input-409>", line 3
    mapping = {
IndentationError: unexpected indent
>>> def calculate_rsi(prices, period=14):
...                                                                                                                 if len(prices) < period + 1:
...                                                                                                                                                                   \                                                                      return [50.0] * len(prices)
...                                                                                                                                                                   \                                                                          deltas = np.diff(prices)
...                                                                                                                                                                   \                                                                              seed = deltas[:period]
...                                                                                                                                                                   \                                                                                  up = seed[seed >= 0].sum() / period
...                                                                                                                                                                   \                                                                                      down = -seed[seed < 0].sum() / period
...                                                                                                                                                                   \                                                                                          rs = up / down if down != 0 else 1.0
...                                                                                                                                                                   \                                                                                              rsi = np.zeros_like(prices)
...                                                                                                                                                                   \                                                                                                  rsi[:period] = 100.0 - 100.0 / (1.0 + rs)
...                                                                                                                                                                   \
  File "<python-input-410>", line 4
    deltas = np.diff(prices)
IndentationError: unexpected indent
>>>     for i in range(period, len(prices)):
  File "<python-input-411>", line 1
    for i in range(period, len(prices)):
IndentationError: unexpected indent
>>>         delta = deltas[i - 1]
  File "<python-input-412>", line 1
    delta = deltas[i - 1]
IndentationError: unexpected indent
>>>         upval = delta if delta > 0 else 0.0
  File "<python-input-413>", line 1
    upval = delta if delta > 0 else 0.0
IndentationError: unexpected indent
>>>         downval = -delta if delta < 0 else 0.0
  File "<python-input-414>", line 1
    downval = -delta if delta < 0 else 0.0
IndentationError: unexpected indent
>>>         up = (up * (period - 1) + upval) / period
  File "<python-input-415>", line 1
    up = (up * (period - 1) + upval) / period
IndentationError: unexpected indent
>>>         down = (down * (period - 1) + downval) / period
  File "<python-input-416>", line 1
    down = (down * (period - 1) + downval) / period
IndentationError: unexpected indent
>>>         rs = up / down if down != 0 else 1.0
  File "<python-input-417>", line 1
    rs = up / down if down != 0 else 1.0
IndentationError: unexpected indent
>>>         rsi[i] = 100.0 - 100.0 / (1.0 + rs)
  File "<python-input-418>", line 1
    rsi[i] = 100.0 - 100.0 / (1.0 + rs)
IndentationError: unexpected indent
>>>     return rsi.tolist()
  File "<python-input-419>", line 1
    return rsi.tolist()
IndentationError: unexpected indent
>>>
>>> # ================= 2. PRO CHART GENERATOR (PRICE + SMA + RSI) =================
>>> def generate_pro_chart(ticker, asset_name, period="7d"):
...                                                                                                                     try:
...                                                                                                                                                                   \                                                                              df = yf.Ticker(ticker).history(period=period, interval="1h")
...                                                                                                                                                                   \                                                                                      prices = [float(x) for x in df['Close'].dropna().tolist()]
...                                                                                                                                                                   \                                                                                          except Exception:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                prices = []
...                                                                                                                                                                   \                                                                                                                                                                      \
  File "<python-input-422>", line 4
    prices = [float(x) for x in df['Close'].dropna().tolist()]
IndentationError: unexpected indent
>>>     if len(prices) < 20:
  File "<python-input-423>", line 1
    if len(prices) < 20:
IndentationError: unexpected indent
>>>         prices = [65200, 65400, 65100, 65800, 66200, 65900, 66500, 66900, 66700, 67200,
  File "<python-input-424>", line 1
    prices = [65200, 65400, 65100, 65800, 66200, 65900, 66500, 66900, 66700, 67200,
IndentationError: unexpected indent
>>>                   67500, 67100, 67800, 68200, 67900, 68400, 68900, 68600, 69100, 69550]
  File "<python-input-425>", line 1
    67500, 67100, 67800, 68200, 67900, 68400, 68900, 68600, 69100, 69550]
IndentationError: unexpected indent
>>>
>>>     latest_price = round(prices[-1], 2)
  File "<python-input-427>", line 1
    latest_price = round(prices[-1], 2)
IndentationError: unexpected indent
>>>     start_price = round(prices[0], 2)
  File "<python-input-428>", line 1
    start_price = round(prices[0], 2)
IndentationError: unexpected indent
>>>     high_price = round(max(prices), 2)
  File "<python-input-429>", line 1
    high_price = round(max(prices), 2)
IndentationError: unexpected indent
>>>     low_price = round(min(prices), 2)
  File "<python-input-430>", line 1
    low_price = round(min(prices), 2)
IndentationError: unexpected indent
>>>     change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
  File "<python-input-431>", line 1
    change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
IndentationError: unexpected indent
>>>     trend = "Bullish" if change_pct >= 0 else "Bearish"
  File "<python-input-432>", line 1
    trend = "Bullish" if change_pct >= 0 else "Bearish"
IndentationError: unexpected indent
>>>
>>>     rsi_vals = calculate_rsi(prices)
  File "<python-input-434>", line 1
    rsi_vals = calculate_rsi(prices)
IndentationError: unexpected indent
>>>     latest_rsi = round(rsi_vals[-1], 1)
  File "<python-input-435>", line 1
    latest_rsi = round(rsi_vals[-1], 1)
IndentationError: unexpected indent
>>>
>>>     # Moving Average (SMA 10)
>>>     sma_vals = [np.mean(prices[max(0, i-9):i+1]) for i in range(len(prices))]
  File "<python-input-438>", line 1
    sma_vals = [np.mean(prices[max(0, i-9):i+1]) for i in range(len(prices))]
IndentationError: unexpected indent
>>>
>>>     plt.style.use('dark_background')
  File "<python-input-440>", line 1
    plt.style.use('dark_background')
IndentationError: unexpected indent
>>>     fig = plt.figure(figsize=(9, 16), dpi=100)
  File "<python-input-441>", line 1
    fig = plt.figure(figsize=(9, 16), dpi=100)
IndentationError: unexpected indent
>>>     fig.patch.set_facecolor('#070b12')
  File "<python-input-442>", line 1
    fig.patch.set_facecolor('#070b12')
IndentationError: unexpected indent
>>>
>>>     # Top Chart: Price + SMA + Support/Resistance
>>>     ax1 = fig.add_axes([0.08, 0.46, 0.86, 0.40])
  File "<python-input-445>", line 1
    ax1 = fig.add_axes([0.08, 0.46, 0.86, 0.40])
IndentationError: unexpected indent
>>>     ax1.set_facecolor('#070b12')
  File "<python-input-446>", line 1
    ax1.set_facecolor('#070b12')
IndentationError: unexpected indent
>>>     line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
  File "<python-input-447>", line 1
    line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
IndentationError: unexpected indent
>>>     x_vals = list(range(len(prices)))
  File "<python-input-448>", line 1
    x_vals = list(range(len(prices)))
IndentationError: unexpected indent
>>>
>>>     ax1.plot(x_vals, prices, color=line_color, linewidth=4.5, label="Live Price")
  File "<python-input-450>", line 1
    ax1.plot(x_vals, prices, color=line_color, linewidth=4.5, label="Live Price")
IndentationError: unexpected indent
>>>     ax1.plot(x_vals, sma_vals, color='#38bdf8', linewidth=2.2, linestyle='--', label="10 SMA")
  File "<python-input-451>", line 1
    ax1.plot(x_vals, sma_vals, color='#38bdf8', linewidth=2.2, linestyle='--', label="10 SMA")
IndentationError: unexpected indent
>>>     ax1.fill_between(x_vals, prices, min(prices), color=line_color, alpha=0.16)
  File "<python-input-452>", line 1
    ax1.fill_between(x_vals, prices, min(prices), color=line_color, alpha=0.16)
IndentationError: unexpected indent
>>>
>>>     # Resistance & Support Lines
>>>     ax1.axhline(high_price, color='#facc15', linestyle=':', linewidth=1.5, alpha=0.8)
  File "<python-input-455>", line 1
    ax1.axhline(high_price, color='#facc15', linestyle=':', linewidth=1.5, alpha=0.8)
IndentationError: unexpected indent
>>>     ax1.axhline(low_price, color='#a855f7', linestyle=':', linewidth=1.5, alpha=0.8)
  File "<python-input-456>", line 1
    ax1.axhline(low_price, color='#a855f7', linestyle=':', linewidth=1.5, alpha=0.8)
IndentationError: unexpected indent
>>>
>>>     ax1.set_title(
  File "<python-input-458>", line 1
    ax1.set_title(
IndentationError: unexpected indent
>>>         f"{asset_name.upper()} PRO ANALYSIS\nPrice: {latest_price} ({change_pct}%)",
  File "<python-input-459>", line 1
    f"{asset_name.upper()} PRO ANALYSIS\nPrice: {latest_price} ({change_pct}%)",
IndentationError: unexpected indent
>>>         fontsize=25, fontweight='bold', color='white', pad=25
  File "<python-input-460>", line 1
    fontsize=25, fontweight='bold', color='white', pad=25
IndentationError: unexpected indent
>>>     )
  File "<python-input-461>", line 1
    )
IndentationError: unexpected indent
>>>     ax1.grid(color='#1e293b', linestyle='--', linewidth=0.8)
  File "<python-input-462>", line 1
    ax1.grid(color='#1e293b', linestyle='--', linewidth=0.8)
IndentationError: unexpected indent
>>>     ax1.set_xticks([])
  File "<python-input-463>", line 1
    ax1.set_xticks([])
IndentationError: unexpected indent
>>>     ax1.tick_params(axis='y', labelsize=13)
  File "<python-input-464>", line 1
    ax1.tick_params(axis='y', labelsize=13)
IndentationError: unexpected indent
>>>     ax1.legend(loc="upper left", fontsize=12, frameon=False)
  File "<python-input-465>", line 1
    ax1.legend(loc="upper left", fontsize=12, frameon=False)
IndentationError: unexpected indent
>>>
>>>     # Bottom Chart: RSI Indicator
>>>     ax2 = fig.add_axes([0.08, 0.31, 0.86, 0.11])
  File "<python-input-468>", line 1
    ax2 = fig.add_axes([0.08, 0.31, 0.86, 0.11])
IndentationError: unexpected indent
>>>     ax2.set_facecolor('#070b12')
  File "<python-input-469>", line 1
    ax2.set_facecolor('#070b12')
IndentationError: unexpected indent
>>>     ax2.plot(x_vals, rsi_vals, color='#f59e0b', linewidth=3)
  File "<python-input-470>", line 1
    ax2.plot(x_vals, rsi_vals, color='#f59e0b', linewidth=3)
IndentationError: unexpected indent
>>>     ax2.axhline(70, color='#ff3366', linestyle='--', linewidth=1.2)
  File "<python-input-471>", line 1
    ax2.axhline(70, color='#ff3366', linestyle='--', linewidth=1.2)
IndentationError: unexpected indent
>>>     ax2.axhline(30, color='#00ff88', linestyle='--', linewidth=1.2)
  File "<python-input-472>", line 1
    ax2.axhline(30, color='#00ff88', linestyle='--', linewidth=1.2)
IndentationError: unexpected indent
>>>     ax2.set_ylim(0, 100)
  File "<python-input-473>", line 1
    ax2.set_ylim(0, 100)
IndentationError: unexpected indent
>>>     ax2.set_title(f"RSI (14) Indicator: {latest_rsi}", fontsize=15, color='#cbd5e1', pad=6)
  File "<python-input-474>", line 1
    ax2.set_title(f"RSI (14) Indicator: {latest_rsi}", fontsize=15, color='#cbd5e1', pad=6)
IndentationError: unexpected indent
>>>     ax2.grid(color='#1e293b', linestyle='--', linewidth=0.6)
  File "<python-input-475>", line 1
    ax2.grid(color='#1e293b', linestyle='--', linewidth=0.6)
IndentationError: unexpected indent
>>>     ax2.set_xticks([])
  File "<python-input-476>", line 1
    ax2.set_xticks([])
IndentationError: unexpected indent
>>>     ax2.tick_params(axis='y', labelsize=11)
  File "<python-input-477>", line 1
    ax2.tick_params(axis='y', labelsize=11)
IndentationError: unexpected indent
>>>
>>>     for ax in [ax1, ax2]:
  File "<python-input-479>", line 1
    for ax in [ax1, ax2]:
IndentationError: unexpected indent
>>>         for spine in ['top', 'right', 'bottom']:
  File "<python-input-480>", line 1
    for spine in ['top', 'right', 'bottom']:
IndentationError: unexpected indent
>>>             ax.spines[spine].set_visible(False)
  File "<python-input-481>", line 1
    ax.spines[spine].set_visible(False)
IndentationError: unexpected indent
>>>
>>>     base_img = "base_chart.png"
  File "<python-input-483>", line 1
    base_img = "base_chart.png"
IndentationError: unexpected indent
>>>     plt.savefig(base_img, facecolor=fig.get_facecolor())
  File "<python-input-484>", line 1
    plt.savefig(base_img, facecolor=fig.get_facecolor())
IndentationError: unexpected indent
>>>     plt.close(fig)
  File "<python-input-485>", line 1
    plt.close(fig)
IndentationError: unexpected indent
>>>
>>>     return base_img, latest_price, high_price, low_price, change_pct, trend, latest_rsi
  File "<python-input-487>", line 1
    return base_img, latest_price, high_price, low_price, change_pct, trend, latest_rsi
IndentationError: unexpected indent
>>>
>>> # ================= 3. SMART SCRIPT & SEO GENERATOR =================
>>> def generate_script_and_seo(prompt, asset_name, price, high_p, low_p, change_pct, trend, rsi, api_key):
...                                                                                                                         rsi_status = "Overbought zone ke paas" if \rsi > 68 else ("Oversold zone mein" if rsi < 32 else "Neutral momentum mein")
...                                                                                                                             direction = "zabardast breakout" if ch\ange_pct >= 0 else "badi girawat"
...
  File "<python-input-490>", line 3
    direction = "zabardast breakout" if change_pct >= 0 else "badi girawat"
IndentationError: unexpected indent
>>>     # Default Auto Script
>>>     lines = [
  File "<python-input-492>", line 1
    lines = [
IndentationError: unexpected indent
>>>         f"{asset_name} mein aaj {direction} dekhne ko mil raha hai!",
  File "<python-input-493>", line 1
    f"{asset_name} mein aaj {direction} dekhne ko mil raha hai!",
IndentationError: unexpected indent
>>>         f"Abhi live price {price} par trade kar raha hai.",
  File "<python-input-494>", line 1
    f"Abhi live price {price} par trade kar raha hai.",
IndentationError: unexpected indent
>>>         f"Chart par pichla change {change_pct}% ka raha hai.",
  File "<python-input-495>", line 1
    f"Chart par pichla change {change_pct}% ka raha hai.",
IndentationError: unexpected indent
>>>         f"Upar {high_p} par strong resistance aur neeche {low_p} par support hai.",
  File "<python-input-496>", line 1
    f"Upar {high_p} par strong resistance aur neeche {low_p} par support hai.",
IndentationError: unexpected indent
>>>         f"RSI indicator abhi {rsi} par hai jo {rsi_status} hai.",
  File "<python-input-497>", line 1
    f"RSI indicator abhi {rsi} par hai jo {rsi_status} hai.",
IndentationError: unexpected indent
>>>         f"Overall market trend abhi {trend} bana hua hai.",
  File "<python-input-498>", line 1
    f"Overall market trend abhi {trend} bana hua hai.",
IndentationError: unexpected indent
>>>         "Rozana live trading levels ke liye channel ko abhi subscribe karein!"
  File "<python-input-499>", line 1
    "Rozana live trading levels ke liye channel ko abhi subscribe karein!"
IndentationError: unexpected indent
>>>     ]
  File "<python-input-500>", line 1
    ]
IndentationError: unexpected indent
>>>
>>>     # Gemini AI Custom Script (if API key provided)
>>>     if api_key and len(api_key.strip()) > 10 and GEMINI_AVAILABLE:
  File "<python-input-503>", line 1
    if api_key and len(api_key.strip()) > 10 and GEMINI_AVAILABLE:
IndentationError: unexpected indent
>>>         try:
  File "<python-input-504>", line 1
    try:
IndentationError: unexpected indent
>>>             client = genai.Client(api_key=api_key.strip())
  File "<python-input-505>", line 1
    client = genai.Client(api_key=api_key.strip())
IndentationError: unexpected indent
>>>             ai_prompt = (
  File "<python-input-506>", line 1
    ai_prompt = (
IndentationError: unexpected indent
>>>                 f"User topic: '{prompt}'. Asset={asset_name}, Price={price}, Change={change_pct}%, "
  File "<python-input-507>", line 1
    f"User topic: '{prompt}'. Asset={asset_name}, Price={price}, Change={change_pct}%, "
IndentationError: unexpected indent
>>>                 f"High={high_p}, Low={low_p}, RSI={rsi}, Trend={trend}. "
  File "<python-input-508>", line 1
    f"High={high_p}, Low={low_p}, RSI={rsi}, Trend={trend}. "
IndentationError: unexpected indent
>>>                 "Write a high-retention 7-line YouTube Shorts trading script in Hinglish (Roman Hindi). "
  File "<python-input-509>", line 1
    "Write a high-retention 7-line YouTube Shorts trading script in Hinglish (Roman Hindi). "
IndentationError: unexpected indent
>>>                 "Each line must be 6 to 9 words max. Return ONLY valid JSON: {\"lines\": [\"line1\", \"line2\"]}"
  File "<python-input-510>", line 1
    "Each line must be 6 to 9 words max. Return ONLY valid JSON: {\"lines\": [\"line1\", \"line2\"]}"
IndentationError: unexpected indent
>>>             )
  File "<python-input-511>", line 1
    )
IndentationError: unexpected indent
>>>             res = client.models.generate_content(model="gemini-2.5-flash", contents=ai_prompt)
  File "<python-input-512>", line 1
    res = client.models.generate_content(model="gemini-2.5-flash", contents=ai_prompt)
IndentationError: unexpected indent
>>>             clean_json = res.text.strip().removeprefix("```json").removesuffix("```").strip()
  File "<python-input-513>", line 1
    clean_json = res.text.strip().removeprefix("```json").removesuffix("```").strip()
IndentationError: unexpected indent
>>>             parsed = json.loads(clean_json).get("lines", [])
  File "<python-input-514>", line 1
    parsed = json.loads(clean_json).get("lines", [])
IndentationError: unexpected indent
>>>             if len(parsed) >= 4:
  File "<python-input-515>", line 1
    if len(parsed) >= 4:
IndentationError: unexpected indent
>>>                 lines = parsed
  File "<python-input-516>", line 1
    lines = parsed
IndentationError: unexpected indent
>>>         except Exception:
  File "<python-input-517>", line 1
    except Exception:
IndentationError: unexpected indent
>>>             pass
  File "<python-input-518>", line 1
    pass
IndentationError: unexpected indent
>>>
>>>     # Viral YouTube Shorts SEO Metadata
>>>     seo_title = f" {asset_name} Live Breakout Update! Price {price} ({change_pct}%) | {trend} Trend #shorts"
  File "<python-input-521>", line 1
    seo_title = f" {asset_name} Live Breakout Update! Price {price} ({change_pct}%) | {trend} Trend #shorts"
IndentationError: unexpected indent
>>>     seo_desc = (
  File "<python-input-522>", line 1
    seo_desc = (
IndentationError: unexpected indent
>>>         f"{asset_name} Live Trading Analysis & Target Update!\n"
  File "<python-input-523>", line 1
    f"{asset_name} Live Trading Analysis & Target Update!\n"
IndentationError: unexpected indent
>>>         f" Current Price: {price} ({change_pct}%)\n"
  File "<python-input-524>", line 1
    f" Current Price: {price} ({change_pct}%)\n"
IndentationError: unexpected indent
>>>         f" Resistance Level: {high_p} | Support Level: {low_p}\n"
  File "<python-input-525>", line 1
    f" Resistance Level: {high_p} | Support Level: {low_p}\n"
IndentationError: unexpected indent
>>>         f" RSI (14): {rsi} ({trend} Momentum)\n\n"
  File "<python-input-526>", line 1
    f" RSI (14): {rsi} ({trend} Momentum)\n\n"
IndentationError: unexpected indent
>>>         f"#trading #{asset_name.lower().replace(' ', '')} #stockmarket #cryptotrading #nifty50 #youtubeshorts #viraltrading"
  File "<python-input-527>", line 1
    f"#trading #{asset_name.lower().replace(' ', '')} #stockmarket #cryptotrading #nifty50 #youtubeshorts #viraltrading"
IndentationError: unexpected indent
>>>     )
  File "<python-input-528>", line 1
    )
IndentationError: unexpected indent
>>>     return lines, " ".join(lines), seo_title, seo_desc
  File "<python-input-529>", line 1
    return lines, " ".join(lines), seo_title, seo_desc
IndentationError: unexpected indent
>>>
>>> # ================= 4. VOICEOVER & SYNTHETIC BGM GENERATOR =================
>>> def create_voiceover(text, api_key, v_id):
...                                                                                                                             audio_path = "voiceover.mp3"
...                                                                                                                                 if api_key and len(api_key.strip()\) > 10:
...                                                                                                                                                                   \                                                                                                  try:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                    url = f"https://api.elevenlabs.io/v1/text-to-speech/{v_id.strip()}"
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": a\pi_key.strip()}
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                            payload = {"text": text, "model_id": "eleven_multilingual_v2"}
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                        res = requests.post(url, json=payload, headers=headers, timeou\t=20)
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                    if res.status_code == 200:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                      \                                                                                          with open(audio_path, "wb") as f:
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                      \                                                                                                                                                                      \                                                                    f.write(res.content)
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                      \                                                                                                                                                                      \                                                                                    return audio_path
...                                                                                                                                                                   \                                                                                                                                                                      \                                                                                                                                                                      \                                                                                                                                                                      \                                                                                            except Exception:
...                                                                                                                                                                   \                                                                                                                                                                      \
                                                                                                                                                                      \                                                                                                                                                                      \                                                              pass






  File "<python-input-532>", line 3
    if api_key and len(api_key.strip()) > 10:
IndentationError: unexpected indent
>>>     tts = gTTS(text=text, lang="hi", slow=False)
  File "<python-input-533>", line 1
    tts = gTTS(text=text, lang="hi", slow=False)
IndentationError: unexpected indent
>>>     tts.save(audio_path)
  File "<python-input-534>", line 1
    tts.save(audio_path)
IndentationError: unexpected indent
>>>     return audio_path
  File "<python-input-535>", line 1
    return audio_path
IndentationError: unexpected indent
>>>
>>> def generate_cyber_bgm(duration_sec, filename="auto_bgm.wav"):
...                                                                                                                                 """Bina kisi external MP3 file ke \pure Python se dark trading background beat banana"""
...                                                                                                                                     sample_rate = 22050
...                                                                                                                                         t = np.linspace(0, duratio\n_sec, int(sample_rate * duration_sec), endpoint=False)
...                                                                                                                                             # Deep synth bass dron\e + subtle pulse beat (120 BPM = 2 Hz)
...                                                                                                                                                 bass = 0.5 * np.si\n(2 * np.pi * 55 * t) + 0.3 * np.sin(2 * np.pi * 110 * t)
...                                                                                                                                                     pulse = (np.si\n(2 * np.pi * 2.0 * t) > 0).astype(float) * 0.4 + 0.6
...                                                                                                                                                         wave_data \= bass * pulse
...                                                                                                                                                             wave_d\ata = np.int16(wave_data / np.max(np.abs(wave_data)) * 32767)
...
  File "<python-input-537>", line 3
    sample_rate = 22050
IndentationError: unexpected indent
>>>     with wave.open(filename, "w") as wav_file:
  File "<python-input-538>", line 1
    with wave.open(filename, "w") as wav_file:
IndentationError: unexpected indent
>>>         wav_file.setnchannels(1)
  File "<python-input-539>", line 1
    wav_file.setnchannels(1)
IndentationError: unexpected indent
>>>         wav_file.setsampwidth(2)
  File "<python-input-540>", line 1
    wav_file.setsampwidth(2)
IndentationError: unexpected indent
>>>         wav_file.setframerate(sample_rate)
  File "<python-input-541>", line 1
    wav_file.setframerate(sample_rate)
IndentationError: unexpected indent
>>>         wav_file.writeframes(wave_data.tobytes())
  File "<python-input-542>", line 1
    wav_file.writeframes(wave_data.tobytes())
IndentationError: unexpected indent
>>>     return filename
  File "<python-input-543>", line 1
    return filename
IndentationError: unexpected indent
>>>
>>> # ================= 5. SUBTITLES & FINAL VIDEO RENDER =================
>>> def draw_subtitle_frame(base_img_path, text, idx, total_lines):
...                                                                                                                                     img = Image.open(base_img_path\).convert("RGB")
...                                                                                                                                         draw = ImageDraw.Draw(img)
...                                                                                                                                             width, height = img.si\ze
...
  File "<python-input-546>", line 3
    draw = ImageDraw.Draw(img)
IndentationError: unexpected indent
>>>     font = None
  File "<python-input-547>", line 1
    font = None
IndentationError: unexpected indent
>>>     for font_name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"]:
  File "<python-input-548>", line 1
    for font_name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"]:
IndentationError: unexpected indent
>>>         try:
  File "<python-input-549>", line 1
    try:
IndentationError: unexpected indent
>>>             font = ImageFont.truetype(font_name, 36)
  File "<python-input-550>", line 1
    font = ImageFont.truetype(font_name, 36)
IndentationError: unexpected indent
>>>             break
  File "<python-input-551>", line 1
    break
IndentationError: unexpected indent
>>>         except Exception:
  File "<python-input-552>", line 1
    except Exception:
IndentationError: unexpected indent
>>>             continue
  File "<python-input-553>", line 1
    continue
IndentationError: unexpected indent
>>>     if font is None:
  File "<python-input-554>", line 1
    if font is None:
IndentationError: unexpected indent
>>>         font = ImageFont.load_default()
  File "<python-input-555>", line 1
    font = ImageFont.load_default()
IndentationError: unexpected indent
>>>
>>>     words = text.split()
  File "<python-input-557>", line 1
    words = text.split()
IndentationError: unexpected indent
>>>     mid = max(1, len(words) // 2)
  File "<python-input-558>", line 1
    mid = max(1, len(words) // 2)
IndentationError: unexpected indent
>>>     line1 = " ".join(words[:mid])
  File "<python-input-559>", line 1
    line1 = " ".join(words[:mid])
IndentationError: unexpected indent
>>>     line2 = " ".join(words[mid:])
  File "<python-input-560>", line 1
    line2 = " ".join(words[mid:])
IndentationError: unexpected indent
>>>
>>>     box_top = int(height * 0.75)
  File "<python-input-562>", line 1
    box_top = int(height * 0.75)
IndentationError: unexpected indent
>>>     box_bottom = int(height * 0.87)
  File "<python-input-563>", line 1
    box_bottom = int(height * 0.87)
IndentationError: unexpected indent
>>>     draw.rectangle([(45, box_top), (width - 45, box_bottom)], fill=(15, 23, 42), outline=(0, 255, 136), width=4)
  File "<python-input-564>", line 1
    draw.rectangle([(45, box_top), (width - 45, box_bottom)], fill=(15, 23, 42), outline=(0, 255, 136), width=4)
IndentationError: unexpected indent
>>>
>>>     # Progress bar inside subtitle box
>>>     prog_width = int(((idx + 1) / max(1, total_lines)) * (width - 90))
  File "<python-input-567>", line 1
    prog_width = int(((idx + 1) / max(1, total_lines)) * (width - 90))
IndentationError: unexpected indent
>>>     draw.rectangle([(45, box_bottom - 8), (45 + prog_width, box_bottom)], fill=(250, 204, 21))
  File "<python-input-568>", line 1
    draw.rectangle([(45, box_bottom - 8), (45 + prog_width, box_bottom)], fill=(250, 204, 21))
IndentationError: unexpected indent
>>>
>>>     draw.text((75, box_top + 32), line1.upper(), fill=(255, 230, 0), font=font)
  File "<python-input-570>", line 1
    draw.text((75, box_top + 32), line1.upper(), fill=(255, 230, 0), font=font)
IndentationError: unexpected indent
>>>     if line2:
  File "<python-input-571>", line 1
    if line2:
IndentationError: unexpected indent
>>>         draw.text((75, box_top + 90), line2.upper(), fill=(255, 255, 255), font=font)
  File "<python-input-572>", line 1
    draw.text((75, box_top + 90), line2.upper(), fill=(255, 255, 255), font=font)
IndentationError: unexpected indent
>>>
>>>     frame_path = f"frame_{idx}.png"
  File "<python-input-574>", line 1
    frame_path = f"frame_{idx}.png"
IndentationError: unexpected indent
>>>     img.save(frame_path)
  File "<python-input-575>", line 1
    img.save(frame_path)
IndentationError: unexpected indent
>>>     return frame_path
  File "<python-input-576>", line 1
    return frame_path
IndentationError: unexpected indent
>>>
>>> def render_video(base_img, lines, audio_path, output_path, use_bgm=True, bgm_vol=0.12):
...                                                                                                                                         voice_clip = AudioFileClip\(audio_path)
...                                                                                                                                             total_duration = voice\_clip.duration
...                                                                                                                                                 total_chars = sum(\len(x) for x in lines) or 1
...
  File "<python-input-578>", line 3
    total_duration = voice_clip.duration
IndentationError: unexpected indent
>>>     clips = []
  File "<python-input-579>", line 1
    clips = []
IndentationError: unexpected indent
>>>     temp_files = []
  File "<python-input-580>", line 1
    temp_files = []
IndentationError: unexpected indent
>>>
>>>     for i, line in enumerate(lines):
  File "<python-input-582>", line 1
    for i, line in enumerate(lines):
IndentationError: unexpected indent
>>>         f_path = draw_subtitle_frame(base_img, line, i, len(lines))
  File "<python-input-583>", line 1
    f_path = draw_subtitle_frame(base_img, line, i, len(lines))
IndentationError: unexpected indent
>>>         temp_files.append(f_path)
  File "<python-input-584>", line 1
    temp_files.append(f_path)
IndentationError: unexpected indent
>>>         dur = (len(line) / total_chars) * total_duration
  File "<python-input-585>", line 1
    dur = (len(line) / total_chars) * total_duration
IndentationError: unexpected indent
>>>         clip = ImageClip(f_path).with_duration(dur) if MOVIEPY_V2 else ImageClip(f_path).set_duration(dur)
  File "<python-input-586>", line 1
    clip = ImageClip(f_path).with_duration(dur) if MOVIEPY_V2 else ImageClip(f_path).set_duration(dur)
IndentationError: unexpected indent
>>>         clips.append(clip)
  File "<python-input-587>", line 1
    clips.append(clip)
IndentationError: unexpected indent
>>>
>>>     final_video = concatenate_videoclips(clips, method="compose")
  File "<python-input-589>", line 1
    final_video = concatenate_videoclips(clips, method="compose")
IndentationError: unexpected indent
>>>
>>>     # Mix Background Music if enabled
>>>     bgm_file = None
  File "<python-input-592>", line 1
    bgm_file = None
IndentationError: unexpected indent
>>>     if use_bgm:
  File "<python-input-593>", line 1
    if use_bgm:
IndentationError: unexpected indent
>>>         bgm_file = generate_cyber_bgm(total_duration)
  File "<python-input-594>", line 1
    bgm_file = generate_cyber_bgm(total_duration)
IndentationError: unexpected indent
>>>         bgm_clip = AudioFileClip(bgm_file)
  File "<python-input-595>", line 1
    bgm_clip = AudioFileClip(bgm_file)
IndentationError: unexpected indent
>>>         if MOVIEPY_V2:
  File "<python-input-596>", line 1
    if MOVIEPY_V2:
IndentationError: unexpected indent
>>>             bgm_clip = bgm_clip.with_volume_scaled(bgm_vol).with_duration(total_duration)
  File "<python-input-597>", line 1
    bgm_clip = bgm_clip.with_volume_scaled(bgm_vol).with_duration(total_duration)
IndentationError: unexpected indent
>>>             final_audio = CompositeAudioClip([voice_clip, bgm_clip])
  File "<python-input-598>", line 1
    final_audio = CompositeAudioClip([voice_clip, bgm_clip])
IndentationError: unexpected indent
>>>             final_video = final_video.with_audio(final_audio)
  File "<python-input-599>", line 1
    final_video = final_video.with_audio(final_audio)
IndentationError: unexpected indent
>>>         else:
  File "<python-input-600>", line 1
    else:
IndentationError: unexpected indent
>>>             bgm_clip = bgm_clip.volumex(bgm_vol).set_duration(total_duration)
  File "<python-input-601>", line 1
    bgm_clip = bgm_clip.volumex(bgm_vol).set_duration(total_duration)
IndentationError: unexpected indent
>>>             final_audio = CompositeAudioClip([voice_clip, bgm_clip])
  File "<python-input-602>", line 1
    final_audio = CompositeAudioClip([voice_clip, bgm_clip])
IndentationError: unexpected indent
>>>             final_video = final_video.set_audio(final_audio)
  File "<python-input-603>", line 1
    final_video = final_video.set_audio(final_audio)
IndentationError: unexpected indent
>>>     else:
  File "<python-input-604>", line 1
    else:
IndentationError: unexpected indent
>>>         final_video = final_video.with_audio(voice_clip) if MOVIEPY_V2 else final_video.set_audio(voice_clip)
  File "<python-input-605>", line 1
    final_video = final_video.with_audio(voice_clip) if MOVIEPY_V2 else final_video.set_audio(voice_clip)
IndentationError: unexpected indent
>>>
>>>     final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac", logger=None)
  File "<python-input-607>", line 1
    final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac", logger=None)
IndentationError: unexpected indent
>>>
>>>     voice_clip.close()
  File "<python-input-609>", line 1
    voice_clip.close()
IndentationError: unexpected indent
>>>     final_video.close()
  File "<python-input-610>", line 1
    final_video.close()
IndentationError: unexpected indent
>>>     for f in temp_files:
  File "<python-input-611>", line 1
    for f in temp_files:
IndentationError: unexpected indent
>>>         if os.path.exists(f):
  File "<python-input-612>", line 1
    if os.path.exists(f):
IndentationError: unexpected indent
>>>             os.remove(f)
  File "<python-input-613>", line 1
    os.remove(f)
IndentationError: unexpected indent
>>>     if bgm_file and os.path.exists(bgm_file):
  File "<python-input-614>", line 1
    if bgm_file and os.path.exists(bgm_file):
IndentationError: unexpected indent
>>>         os.remove(bgm_file)
  File "<python-input-615>", line 1
    os.remove(bgm_file)
IndentationError: unexpected indent
>>>
>>> # ================= MAIN STUDIO DASHBOARD =================
>>> user_prompt = st.text_input(
...     " Apna Video Prompt Likhein:",
...         value="Bitcoin ka live RSI aur breakout trading video banao",
...             placeholder="Example: Nifty 50 breakout analysis, Gold crash update, Solana live target..."
...             )
Traceback (most recent call last):
  File "<python-input-618>", line 1, in <module>
    user_prompt = st.text_input(
                  ^^
NameError: name 'st' is not defined. Did you mean: 'set'?
>>>
>>> if st.button(" Generate Pro Trading Video", use_container_width=True):
...         output_video = "pro_trading_short.mp4"
...             progress = st.progress(0)
...                 status = st.empty()
...
  File "<python-input-620>", line 3
    progress = st.progress(0)
IndentationError: unexpected indent
>>>     try:
  File "<python-input-621>", line 1
    try:
IndentationError: unexpected indent
>>>         status.info(" Step 1/4: Live Price, SMA aur RSI Indicator Chart ban raha hai...")
  File "<python-input-622>", line 1
    status.info(" Step 1/4: Live Price, SMA aur RSI Indicator Chart ban raha hai...")
IndentationError: unexpected indent
>>>         ticker, asset = detect_asset(user_prompt)
  File "<python-input-623>", line 1
    ticker, asset = detect_asset(user_prompt)
IndentationError: unexpected indent
>>>         chart_img, price, high_p, low_p, pct, trend, rsi = generate_pro_chart(ticker, asset, chart_period)
  File "<python-input-624>", line 1
    chart_img, price, high_p, low_p, pct, trend, rsi = generate_pro_chart(ticker, asset, chart_period)
IndentationError: unexpected indent
>>>         progress.progress(25)
  File "<python-input-625>", line 1
    progress.progress(25)
IndentationError: unexpected indent
>>>
>>>         c1, c2, c3, c4 = st.columns(4)
  File "<python-input-627>", line 1
    c1, c2, c3, c4 = st.columns(4)
IndentationError: unexpected indent
>>>         c1.metric("Asset", asset)
  File "<python-input-628>", line 1
    c1.metric("Asset", asset)
IndentationError: unexpected indent
>>>         c2.metric("Price", f"{price}", f"{pct}%")
  File "<python-input-629>", line 1
    c2.metric("Price", f"{price}", f"{pct}%")
IndentationError: unexpected indent
>>>         c3.metric("RSI (14)", f"{rsi}")
  File "<python-input-630>", line 1
    c3.metric("RSI (14)", f"{rsi}")
IndentationError: unexpected indent
>>>         c4.metric("Trend", trend)
  File "<python-input-631>", line 1
    c4.metric("Trend", trend)
IndentationError: unexpected indent
>>>
>>>         status.info(" Step 2/4: AI Script, Subtitles aur YouTube SEO Tags ban rahe hain...")
  File "<python-input-633>", line 1
    status.info(" Step 2/4: AI Script, Subtitles aur YouTube SEO Tags ban rahe hain...")
IndentationError: unexpected indent
>>>         sub_lines, script_text, seo_title, seo_desc = generate_script_and_seo(
  File "<python-input-634>", line 1
    sub_lines, script_text, seo_title, seo_desc = generate_script_and_seo(
IndentationError: unexpected indent
>>>             user_prompt, asset, price, high_p, low_p, pct, trend, rsi, gemini_api_key
  File "<python-input-635>", line 1
    user_prompt, asset, price, high_p, low_p, pct, trend, rsi, gemini_api_key
IndentationError: unexpected indent
>>>         )
  File "<python-input-636>", line 1
    )
IndentationError: unexpected indent
>>>         progress.progress(50)
  File "<python-input-637>", line 1
    progress.progress(50)
IndentationError: unexpected indent
>>>
>>>         status.info(" Step 3/4: AI Voiceover aur Background Music mix ho raha hai...")
  File "<python-input-639>", line 1
    status.info(" Step 3/4: AI Voiceover aur Background Music mix ho raha hai...")
IndentationError: unexpected indent
>>>         audio_file = create_voiceover(script_text, eleven_api_key, voice_id)
  File "<python-input-640>", line 1
    audio_file = create_voiceover(script_text, eleven_api_key, voice_id)
IndentationError: unexpected indent
>>>         progress.progress(75)
  File "<python-input-641>", line 1
    progress.progress(75)
IndentationError: unexpected indent
>>>
>>>         status.info(" Step 4/4: Final HD Shorts Video render ho raha hai...")
  File "<python-input-643>", line 1
    status.info(" Step 4/4: Final HD Shorts Video render ho raha hai...")
IndentationError: unexpected indent
>>>         render_video(chart_img, sub_lines, audio_file, output_video, enable_bgm, bgm_volume)
  File "<python-input-644>", line 1
    render_video(chart_img, sub_lines, audio_file, output_video, enable_bgm, bgm_volume)
IndentationError: unexpected indent
>>>         progress.progress(100)
  File "<python-input-645>", line 1
    progress.progress(100)
IndentationError: unexpected indent
>>>         status.success(" Pro Trading Video aur YouTube SEO Tags taiyaar hain!")
  File "<python-input-646>", line 1
    status.success(" Pro Trading Video aur YouTube SEO Tags taiyaar hain!")
IndentationError: unexpected indent
>>>
>>>         st.video(output_video)
  File "<python-input-648>", line 1
    st.video(output_video)
IndentationError: unexpected indent
>>>         with open(output_video, "rb") as file:
  File "<python-input-649>", line 1
    with open(output_video, "rb") as file:
IndentationError: unexpected indent
>>>             st.download_button(
  File "<python-input-650>", line 1
    st.download_button(
IndentationError: unexpected indent
>>>                 label=" Download HD MP4 Video",
  File "<python-input-651>", line 1
    label=" Download HD MP4 Video",
IndentationError: unexpected indent
>>>                 data=file,
  File "<python-input-652>", line 1
    data=file,
IndentationError: unexpected indent
>>>                 file_name=f"{asset.lower()}_pro_short.mp4",
  File "<python-input-653>", line 1
    file_name=f"{asset.lower()}_pro_short.mp4",
IndentationError: unexpected indent
>>>                 mime="video/mp4",
  File "<python-input-654>", line 1
    mime="video/mp4",
IndentationError: unexpected indent
>>>                 use_container_width=True
  File "<python-input-655>", line 1
    use_container_width=True
IndentationError: unexpected indent
>>>             )
  File "<python-input-656>", line 1
    )
IndentationError: unexpected indent
>>>
>>>         st.subheader(" Copy-Paste YouTube Shorts SEO")
  File "<python-input-658>", line 1
    st.subheader(" Copy-Paste YouTube Shorts SEO")
IndentationError: unexpected indent
>>>         st.text_input("Viral Title:", value=seo_title)
  File "<python-input-659>", line 1
    st.text_input("Viral Title:", value=seo_title)
IndentationError: unexpected indent
>>>         st.text_area("Viral Description & Hashtags:", value=seo_desc, height=130)
  File "<python-input-660>", line 1
    st.text_area("Viral Description & Hashtags:", value=seo_desc, height=130)
IndentationError: unexpected indent
>>>
>>>     except Exception:
  File "<python-input-662>", line 1
    except Exception:
IndentationError: unexpected indent
>>>         st.error(" Error aaya hai, niche details dekhein:")
  File "<python-input-663>", line 1
    st.error(" Error aaya hai, niche details dekhein:")
IndentationError: unexpected indent
>>>         st.code(traceback.format_exc())
  File "<python-input-664>", line 1
    st.code(traceback.format_exc())
IndentationError: unexpected indent
>>>
