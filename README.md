# 🇹🇷 Turkish Text-to-Speech (XTTS-v2 Demo)

🎙️ **Generate natural Turkish speech** using the [Coqui XTTS-v2](https://github.com/coqui-ai/TTS) multilingual voice cloning model.  
This project demonstrates instant Turkish voice synthesis — cloning a short reference clip and speaking new text naturally.

---

##  Project Overview

This repository shows how to:
- Load and run the **XTTS-v2** text-to-speech model.
- Clone a Turkish voice from a short `.wav` sample.
- Synthesize Turkish text into lifelike speech output.

**Example Text:**
> “Bugün veri bilimi çalışıyorum.”  
➡️ Output: `outputs/xtts_tr.wav`

---

## 🧩 Folder Structure

turkish-tts-xtts/
demo_xtts_turkish.py      # Main TTS demo script
requirements.txt           # Project dependencies
constraints.txt            # Version pinning
samples/                   # Input Turkish voice samples
ref_tr.wav             # Reference audio
testsampler.m4a        # Alternate sample
outputs/                   # Synthesized output speech
  xtts_tr.wav

README.md


## 🧠 Model & Tools

| Component | Description |
|------------|-------------|
| **XTTS-v2** | Multilingual voice cloning model (Coqui TTS) |
| **Python** | Core programming language |
| **SoundFile / NumPy** | Audio processing & array operations |
| **Conda Environment** | Isolated, reproducible setup |
| **macOS** | Local environment for running the model |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ozturkipec/turkish-tts-xtts.git
cd turkish-tts-xtts

### 2️⃣ Create environment
conda create -n turkish_tts python=3.10
conda activate turkish_tts

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the demo
python demo_xtts_turkish.py "Bugün veri bilimi çalışıyorum."

Output will be saved as:
outputs/xtts_tr.wav

🎧 Example Output

Input: “Bugün veri bilimi çalışıyorum.”
Output Audio: 🔊 Listen on GitHub (xtts_tr.wav)

👩‍💻 Author

Ipek Ozturk
🎓 Data Analyst & Data scientist
📍 Santa Monica, CA
📧 ipekozturk26@gmail.com
🌐 GitHub Profile

🧾 License

This project uses the Coqui Community Public Model License (CPML) for XTTS-v2.
Commercial usage requires a separate license from Coqui.ai


💬 Acknowledgments
	•	Coqui.ai for the XTTS-v2 model
	•	OpenAI ChatGPT for build support and debugging
	•	Inspired by multilingual voice cloning research



