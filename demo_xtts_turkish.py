# Turkish TTS with instant voice cloning via XTTS-v2
# Run: python demo_xtts_turkish.py "Bugün veri bilimi çalışıyorum."
# Output: outputs/xtts_tr.wav

import sys
from pathlib import Path
import soundfile as sf
from TTS.api import TTS

OUTDIR = Path("outputs")
OUTDIR.mkdir(parents=True, exist_ok=True)

TEXT = "Merhaba! Bu, Türkçe seslendirme ve ses klonlama demosudur."
if len(sys.argv) > 1:
    TEXT = " ".join(sys.argv[1:])

REF_WAV = Path("samples/ref_tr.wav")   # 3–15s mono Turkish sample
REF_TXT = Path("samples/ref_tr.txt")   # exact transcript

assert REF_WAV.exists(), "⚠️ Missing samples/ref_tr.wav"
assert REF_TXT.exists(), "⚠️ Missing samples/ref_tr.txt"

print("🔄 Loading XTTS-v2 model (this may take a minute)...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

print(f"🎙️ Synthesizing:\nText: {TEXT}\nVoice: {REF_WAV}")
audio = tts.tts(
    text=TEXT,
    speaker_wav=str(REF_WAV),
    language="tr"
)

out_path = OUTDIR / "xtts_tr.wav"
sf.write(out_path, audio, 24000)
print(f"✅ Wrote output file: {out_path.resolve()}")
