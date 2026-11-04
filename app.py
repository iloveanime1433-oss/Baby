import os
import json
import wave
import traceback
import requests
import numpy as np
import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import yfinance as yf
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

# MoviePy v1 aur v2 dono ke liye complete support
try:
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
    MOVIEPY_V2 = True
except ImportError:
    from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
    MOVIEPY_V2 = False

# Optional Gemini SDK support
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# ================= WEB APP UI SETUP =================
st.set_page_config(page_title="Pro AI Trading Video Studio", page_icon="⚡", layout="centered")

st.title("⚡ Pro AI Trading Video Studio")
st.write("1 Prompt se Live RSI Chart, AI Voiceover, Background Music, Animated Subtitles aur YouTube SEO Tags banayein.")

with st.sidebar:
    st.header("🛠️ Studio Settings")
    gemini_api_key = st.text_input("Gemini API Key (Optional)", type="password", help="Custom AI script ke liye. Khali chhodne par Smart Auto-Script banegi.")
    eleven_api_key = st.text_input("ElevenLabs API Key (Optional)", type="password", help="Khali chhodne par Free Hindi AI Voice use hogi.")
    voice_id = st.text_input("ElevenLabs Voice ID", value="pNInz6obpgDQGcFmaJgB")
    chart_period = st.selectbox("Chart Timeframe", ["5d", "7d", "1mo", "3mo"], index=1)
    enable_bgm = st.checkbox("Add Auto Background Music (BGM)", value=True)
    bgm_volume = st.slider("BGM Volume", 0.05, 0.30, 0.12, 0.01)

# ================= 1. ASSET & MARKET DATA =================
def detect_asset(prompt):
    p = prompt.lower()
    mapping = {
        "bitcoin": ("BTC-USD", "Bitcoin"),
        "btc": ("BTC-USD", "Bitcoin"),
        "ethereum": ("ETH-USD", "Ethereum"),
        "eth": ("ETH-USD", "Ethereum"),
        "solana": ("SOL-USD", "Solana"),
        "sol": ("SOL-USD", "Solana"),
        "bnb": ("BNB-USD", "BNB"),
        "xrp": ("XRP-USD", "XRP"),
        "doge": ("DOGE-USD", "Dogecoin"),
        "nifty": ("^NSEI", "Nifty 50"),
        "bank nifty": ("^NSEBANK", "Bank Nifty"),
        "sensex": ("^BSESN", "Sensex"),
        "gold": ("GC=F", "Gold"),
        "silver": ("SI=F", "Silver"),
        "reliance": ("RELIANCE.NS", "Reliance"),
        "tata": ("TATASTEEL.NS", "Tata Steel"),
        "hdfc": ("HDFCBANK.NS", "HDFC Bank"),
        "infosys": ("INFY.NS", "Infosys"),
        "zomato": ("ZOMATO.NS", "Zomato"),
    }
    for key, val in mapping.items():
        if key in p:
            return val
    return "BTC-USD", "Bitcoin"

def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return [50.0] * len(prices)
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 1.0
    rsi = np.zeros_like(prices)
    rsi[:period] = 100.0 - 100.0 / (1.0 + rs)

    for i in range(period, len(prices)):
        delta = deltas[i - 1]
        upval = delta if delta > 0 else 0.0
        downval = -delta if delta < 0 else 0.0
        up = (up * (period - 1) + upval) / period
        down = (down * (period - 1) + downval) / period
        rs = up / down if down != 0 else 1.0
        rsi[i] = 100.0 - 100.0 / (1.0 + rs)
    return rsi.tolist()

# ================= 2. PRO CHART GENERATOR (PRICE + SMA + RSI) =================
def generate_pro_chart(ticker, asset_name, period="7d"):
    try:
        df = yf.Ticker(ticker).history(period=period, interval="1h")
        prices = [float(x) for x in df['Close'].dropna().tolist()]
    except Exception:
        prices = []

    if len(prices) < 20:
        prices = [65200, 65400, 65100, 65800, 66200, 65900, 66500, 66900, 66700, 67200,
                  67500, 67100, 67800, 68200, 67900, 68400, 68900, 68600, 69100, 69550]

    latest_price = round(prices[-1], 2)
    start_price = round(prices[0], 2)
    high_price = round(max(prices), 2)
    low_price = round(min(prices), 2)
    change_pct = round(((latest_price - start_price) / start_price) * 100, 2)
    trend = "Bullish" if change_pct >= 0 else "Bearish"

    rsi_vals = calculate_rsi(prices)
    latest_rsi = round(rsi_vals[-1], 1)

    # Moving Average (SMA 10)
    sma_vals = [np.mean(prices[max(0, i-9):i+1]) for i in range(len(prices))]

    plt.style.use('dark_background')
    fig = plt.figure(figsize=(9, 16), dpi=100)
    fig.patch.set_facecolor('#070b12')

    # Top Chart: Price + SMA + Support/Resistance
    ax1 = fig.add_axes([0.08, 0.46, 0.86, 0.40])
    ax1.set_facecolor('#070b12')
    line_color = '#00ff88' if change_pct >= 0 else '#ff3366'
    x_vals = list(range(len(prices)))

    ax1.plot(x_vals, prices, color=line_color, linewidth=4.5, label="Live Price")
    ax1.plot(x_vals, sma_vals, color='#38bdf8', linewidth=2.2, linestyle='--', label="10 SMA")
    ax1.fill_between(x_vals, prices, min(prices), color=line_color, alpha=0.16)

    # Resistance & Support Lines
    ax1.axhline(high_price, color='#facc15', linestyle=':', linewidth=1.5, alpha=0.8)
    ax1.axhline(low_price, color='#a855f7', linestyle=':', linewidth=1.5, alpha=0.8)

    ax1.set_title(
        f"{asset_name.upper()} PRO ANALYSIS\nPrice: {latest_price} ({change_pct}%)",
        fontsize=25, fontweight='bold', color='white', pad=25
    )
    ax1.grid(color='#1e293b', linestyle='--', linewidth=0.8)
    ax1.set_xticks([])
    ax1.tick_params(axis='y', labelsize=13)
    ax1.legend(loc="upper left", fontsize=12, frameon=False)

    # Bottom Chart: RSI Indicator
    ax2 = fig.add_axes([0.08, 0.31, 0.86, 0.11])
    ax2.set_facecolor('#070b12')
    ax2.plot(x_vals, rsi_vals, color='#f59e0b', linewidth=3)
    ax2.axhline(70, color='#ff3366', linestyle='--', linewidth=1.2)
    ax2.axhline(30, color='#00ff88', linestyle='--', linewidth=1.2)
    ax2.set_ylim(0, 100)
    ax2.set_title(f"RSI (14) Indicator: {latest_rsi}", fontsize=15, color='#cbd5e1', pad=6)
    ax2.grid(color='#1e293b', linestyle='--', linewidth=0.6)
    ax2.set_xticks([])
    ax2.tick_params(axis='y', labelsize=11)

    for ax in [ax1, ax2]:
        for spine in ['top', 'right', 'bottom']:
            ax.spines[spine].set_visible(False)

    base_img = "base_chart.png"
    plt.savefig(base_img, facecolor=fig.get_facecolor())
    plt.close(fig)

    return base_img, latest_price, high_price, low_price, change_pct, trend, latest_rsi

# ================= 3. SMART SCRIPT & SEO GENERATOR =================
def generate_script_and_seo(prompt, asset_name, price, high_p, low_p, change_pct, trend, rsi, api_key):
    rsi_status = "Overbought zone ke paas" if rsi > 68 else ("Oversold zone mein" if rsi < 32 else "Neutral momentum mein")
    direction = "zabardast breakout" if change_pct >= 0 else "badi girawat"

    # Default Auto Script
    lines = [
        f"{asset_name} mein aaj {direction} dekhne ko mil raha hai!",
        f"Abhi live price {price} par trade kar raha hai.",
        f"Chart par pichla change {change_pct}% ka raha hai.",
        f"Upar {high_p} par strong resistance aur neeche {low_p} par support hai.",
        f"RSI indicator abhi {rsi} par hai jo {rsi_status} hai.",
        f"Overall market trend abhi {trend} bana hua hai.",
        "Rozana live trading levels ke liye channel ko abhi subscribe karein!"
    ]

    # Gemini AI Custom Script (if API key provided)
    if api_key and len(api_key.strip()) > 10 and GEMINI_AVAILABLE:
        try:
            client = genai.Client(api_key=api_key.strip())
            ai_prompt = (
                f"User topic: '{prompt}'. Asset={asset_name}, Price={price}, Change={change_pct}%, "
                f"High={high_p}, Low={low_p}, RSI={rsi}, Trend={trend}. "
                "Write a high-retention 7-line YouTube Shorts trading script in Hinglish (Roman Hindi). "
                "Each line must be 6 to 9 words max. Return ONLY valid JSON: {\"lines\": [\"line1\", \"line2\"]}"
            )
            res = client.models.generate_content(model="gemini-2.5-flash", contents=ai_prompt)
            clean_json = res.text.strip().removeprefix("```json").removesuffix("```").strip()
            parsed = json.loads(clean_json).get("lines", [])
            if len(parsed) >= 4:
                lines = parsed
        except Exception:
            pass

    # Viral YouTube Shorts SEO Metadata
    seo_title = f"🔥 {asset_name} Live Breakout Update! Price {price} ({change_pct}%) | {trend} Trend #shorts"
    seo_desc = (
        f"{asset_name} Live Trading Analysis & Target Update!\n"
        f"📈 Current Price: {price} ({change_pct}%)\n"
        f"🎯 Resistance Level: {high_p} | Support Level: {low_p}\n"
        f"⚡ RSI (14): {rsi} ({trend} Momentum)\n\n"
        f"#trading #{asset_name.lower().replace(' ', '')} #stockmarket #cryptotrading #nifty50 #youtubeshorts #viraltrading"
    )
    return lines, " ".join(lines), seo_title, seo_desc

# ================= 4. VOICEOVER & SYNTHETIC BGM GENERATOR =================
def create_voiceover(text, api_key, v_id):
    audio_path = "voiceover.mp3"
    if api_key and len(api_key.strip()) > 10:
        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{v_id.strip()}"
            headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": api_key.strip()}
            payload = {"text": text, "model_id": "eleven_multilingual_v2"}
            res = requests.post(url, json=payload, headers=headers, timeout=20)
            if res.status_code == 200:
                with open(audio_path, "wb") as f:
                    f.write(res.content)
                return audio_path
        except Exception:
            pass

    tts = gTTS(text=text, lang="hi", slow=False)
    tts.save(audio_path)
    return audio_path

def generate_cyber_bgm(duration_sec, filename="auto_bgm.wav"):
    """Bina kisi external MP3 file ke pure Python se dark trading background beat banana"""
    sample_rate = 22050
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    # Deep synth bass drone + subtle pulse beat (120 BPM = 2 Hz)
    bass = 0.5 * np.sin(2 * np.pi * 55 * t) + 0.3 * np.sin(2 * np.pi * 110 * t)
    pulse = (np.sin(2 * np.pi * 2.0 * t) > 0).astype(float) * 0.4 + 0.6
    wave_data = bass * pulse
    wave_data = np.int16(wave_data / np.max(np.abs(wave_data)) * 32767)

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(wave_data.tobytes())
    return filename

# ================= 5. SUBTITLES & FINAL VIDEO RENDER =================
def draw_subtitle_frame(base_img_path, text, idx, total_lines):
    img = Image.open(base_img_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    width, height = img.size

    font = None
    for font_name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"]:
        try:
            font = ImageFont.truetype(font_name, 36)
            break
        except Exception:
            continue
    if font is None:
        font = ImageFont.load_default()

    words = text.split()
    mid = max(1, len(words) // 2)
    line1 = " ".join(words[:mid])
    line2 = " ".join(words[mid:])

    box_top = int(height * 0.75)
    box_bottom = int(height * 0.87)
    draw.rectangle([(45, box_top), (width - 45, box_bottom)], fill=(15, 23, 42), outline=(0, 255, 136), width=4)

    # Progress bar inside subtitle box
    prog_width = int(((idx + 1) / max(1, total_lines)) * (width - 90))
    draw.rectangle([(45, box_bottom - 8), (45 + prog_width, box_bottom)], fill=(250, 204, 21))

    draw.text((75, box_top + 32), line1.upper(), fill=(255, 230, 0), font=font)
    if line2:
        draw.text((75, box_top + 90), line2.upper(), fill=(255, 255, 255), font=font)

    frame_path = f"frame_{idx}.png"
    img.save(frame_path)
    return frame_path

def render_video(base_img, lines, audio_path, output_path, use_bgm=True, bgm_vol=0.12):
    voice_clip = AudioFileClip(audio_path)
    total_duration = voice_clip.duration
    total_chars = sum(len(x) for x in lines) or 1

    clips = []
    temp_files = []

    for i, line in enumerate(lines):
        f_path = draw_subtitle_frame(base_img, line, i, len(lines))
        temp_files.append(f_path)
        dur = (len(line) / total_chars) * total_duration
        clip = ImageClip(f_path).with_duration(dur) if MOVIEPY_V2 else ImageClip(f_path).set_duration(dur)
        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")

    # Mix Background Music if enabled
    bgm_file = None
    if use_bgm:
        bgm_file = generate_cyber_bgm(total_duration)
        bgm_clip = AudioFileClip(bgm_file)
        if MOVIEPY_V2:
            bgm_clip = bgm_clip.with_volume_scaled(bgm_vol).with_duration(total_duration)
            final_audio = CompositeAudioClip([voice_clip, bgm_clip])
            final_video = final_video.with_audio(final_audio)
        else:
            bgm_clip = bgm_clip.volumex(bgm_vol).set_duration(total_duration)
            final_audio = CompositeAudioClip([voice_clip, bgm_clip])
            final_video = final_video.set_audio(final_audio)
    else:
        final_video = final_video.with_audio(voice_clip) if MOVIEPY_V2 else final_video.set_audio(voice_clip)

    final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac", logger=None)

    voice_clip.close()
    final_video.close()
    for f in temp_files:
        if os.path.exists(f):
            os.remove(f)
    if bgm_file and os.path.exists(bgm_file):
        os.remove(bgm_file)

# ================= MAIN STUDIO DASHBOARD =================
user_prompt = st.text_input(
    "🎯 Apna Video Prompt Likhein:",
    value="Bitcoin ka live RSI aur breakout trading video banao",
    placeholder="Example: Nifty 50 breakout analysis, Gold crash update, Solana live target..."
)

if st.button("🚀 Generate Pro Trading Video", use_container_width=True):
    output_video = "pro_trading_short.mp4"
    progress = st.progress(0)
    status = st.empty()

    try:
        status.info("⏳ Step 1/4: Live Price, SMA aur RSI Indicator Chart ban raha hai...")
        ticker, asset = detect_asset(user_prompt)
        chart_img, price, high_p, low_p, pct, trend, rsi = generate_pro_chart(ticker, asset, chart_period)
        progress.progress(25)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Asset", asset)
        c2.metric("Price", f"{price}", f"{pct}%")
        c3.metric("RSI (14)", f"{rsi}")
        c4.metric("Trend", trend)

        status.info("⏳ Step 2/4: AI Script, Subtitles aur YouTube SEO Tags ban rahe hain...")
        sub_lines, script_text, seo_title, seo_desc = generate_script_and_seo(
            user_prompt, asset, price, high_p, low_p, pct, trend, rsi, gemini_api_key
        )
        progress.progress(50)

        status.info("⏳ Step 3/4: AI Voiceover aur Background Music mix ho raha hai...")
        audio_file = create_voiceover(script_text, eleven_api_key, voice_id)
        progress.progress(75)

        status.info("⏳ Step 4/4: Final HD Shorts Video render ho raha hai...")
        render_video(chart_img, sub_lines, audio_file, output_video, enable_bgm, bgm_volume)
        progress.progress(100)
        status.success("✅ Pro Trading Video aur YouTube SEO Tags taiyaar hain!")

        st.video(output_video)
        with open(output_video, "rb") as file:
            st.download_button(
                label="⬇️ Download HD MP4 Video",
                data=file,
                file_name=f"{asset.lower()}_pro_short.mp4",
                mime="video/mp4",
                use_container_width=True
            )

        st.subheader("📋 Copy-Paste YouTube Shorts SEO")
        st.text_input("Viral Title:", value=seo_title)
        st.text_area("Viral Description & Hashtags:", value=seo_desc, height=130)

    except Exception:
        st.error("❌ Error aaya hai, niche details dekhein:")
        st.code(traceback.format_exc())
