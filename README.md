<h1 align="center">TurkicTTS <br> ⌨️ 🗣 </h1>

<p align="center">
  <a href="https://github.com/IS2AI/TurkicTTS/stargazers">
    <img src="https://img.shields.io/github/stars/IS2AI/TurkicTTS.svg?colorA=orange&colorB=orange&logo=github"
         alt="GitHub stars">
  </a>
  <a href="https://github.com/IS2AI/TurkicTTS/issues">
    <img src="https://img.shields.io/github/issues/IS2AI/TurkicTTS.svg"
         alt="GitHub issues">
  </a>
  <a href="https://issai.nu.edu.kz">
    <img src="https://img.shields.io/static/v1?label=ISSAI&amp;message=official site&amp;color=blue&amp"
         alt="ISSAI Official Website">
  </a> 
</p>

<p align = "center">This repository provides a demo and a pre-trained model for the paper <br><b>Multilingual Text-to-Speech Synthesis for Turkic Languages Using Transliteration</b></p>

## Languages 💬
<p align = "justify">The model supports ten <a href="https://en.wikipedia.org/wiki/Turkic_languages">Turkic languages</a>, including <a href="https://en.wikipedia.org/wiki/Azerbaijani_language">Azerbaijani</a>, <a href="https://en.wikipedia.org/wiki/Bashkir_language">Bashkir</a>, <a href="https://en.wikipedia.org/wiki/Kazakh_language">Kazakh</a>, <a href="https://en.wikipedia.org/wiki/Kyrgyz_language">Kyrgyz</a>, <a href="https://en.wikipedia.org/wiki/Yakut_language">Sakha</a>, <a href="https://en.wikipedia.org/wiki/Tatar_language">Tatar</a>, <a href="https://en.wikipedia.org/wiki/Turkish_language">Turkish</a>, <a href="https://en.wikipedia.org/wiki/Turkmen_language">Turkmen</a>, <a href="https://en.wikipedia.org/wiki/Uyghur_language">Uyghur</a>, and <a href="https://en.wikipedia.org/wiki/Uzbek_language">Uzbek</a>. Spoken across a wide geographical area stretching from the Balkans through Central Asia to northeastern Siberia, these languages share a wide range of common 🫂 linguistic features, such as vowel harmony, extensive agglutination, subject-object-verb order, and the absence of grammatical gender and articles.</p>


## Dataset 🗃️
Our study became feasible thanks to a large-scale and open-source speech corpus called 🇰🇿 [KazakhTTS2](https://github.com/IS2AI/Kazakh_TTS).

## Surveys 🎧 → 😡☹️😐🙂😀 → ✅ → ⌨️
<p align = "justify">Below are the links to the ten questionnaires used in the study to collect subjective evaluations. These questionnaires were distributed on popular social media platforms operating in the Turkic languages. If you are interested, feel free to check them out. Your participation and input are greatly appreciated in helping us gather valuable data for our research. Your insights will contribute to a deeper understanding of the subject matter under investigation.</p> 

Each questionnaire consists of 20 short questions and should take you about 5 minutes. No background knowledge is required.
You will be asked to
- listen to 10 audio recordings and rate their quality,
- listen to 5 short questions and choose answers,
- listen to 5 short sentences and type them.

Thank you for your time and consideration.

<p align = "center">
<a href="https://nukz.qualtrics.com/jfe/form/SV_bNu5RvcsYMKkU8m"><b>Azerbaijani</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_cvl3H1U8EbFM4Tk"><b>Bashkir</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_3WelDTOVyKK5iom"><b>Kazakh</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_cAT00TOsCNKsSZE"><b>Kyrgyz</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_2awH2YEoL5V7biC"><b>Sakha</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_0dEAXvcHxAiEYxo"><b>Tatar</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_cItR7tzYRRjlkYC"><b>Turkish</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_cVgQk4lgS17HBgW"><b>Turkmen</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_ezZO1jNowvrAdds"><b>Uyghur</b></a>
▫️ <a href="https://nukz.qualtrics.com/jfe/form/SV_01BJgR96UMZ3fOm"><b>Uzbek</b></a>
  </p>


## Pretrained models ⚙️
Unzip both the pre-trained vocoder and the acoustic model in the current directory.

### vocoder: parallelwavegan_male2_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_male2_checkpoint.zip

### acoustic model: kaztts_male2_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_male2_tacotron2_train.loss.ave.zip

## Inference 🐍
```python
from parallel_wavegan.utils import load_model
from espnet2.bin.tts_inference import Text2Speech
from scipy.io.wavfile import write
from utils import normalization
import torch

fs = 22050
vocoder_checkpoint="parallelwavegan_male2_checkpoint/checkpoint-400000steps.pkl" ### specify vocoder path
vocoder = load_model(vocoder_checkpoint).to("cuda").eval()
vocoder.remove_weight_norm()

## specify path to the main model(transformer/tacotron2/fastspeech) and its config file
config_file = "exp/tts_train_raw_char/config.yaml"
model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"

text2speech = Text2Speech(
    config_file,
    model_path,
    device="cuda", ## if cuda not available use cpu
    # Only for Tacotron 2
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=True,
    backward_window=1,
    forward_window=3,
    # Only for FastSpeech & FastSpeech2
    speed_control_alpha=1.0,
)
text2speech.spc2wav = None  # Disable griffin-lim

text = "merhaba"
### available options are azerbaijani, bashkir, kazakh, kyrgyz, sakha, turkish, turkmen, tatar, uyghur, uzbek
lang = "turkish"

text = normalization(text, lang)
with torch.no_grad():
    c_mel = text2speech(text)['feat_gen']
    wav = vocoder.inference(c_mel)
write("result.wav", fs, wav.view(-1).cpu().numpy())
```
## Synthesised samples 🔈
**Azerbaijani**

    Azərbaycan Xəzər dənizi hövzəsinin qərbində yerləşir.

https://github.com/IS2AI/TurkicTTS/assets/6375187/8ead9d0f-459b-4d1f-8fa1-4836f76cdd0a

---

**Bashkir**

    Башҡортостан Республикаһы шарттарында ауыл хужалығы етерлек хеҙмәт ресурстарына нигеҙләнә.
    
https://github.com/IS2AI/TurkicTTS/assets/6375187/a86f8638-d3e9-47fb-974f-e2b2a820fd3d

---

**Kazakh**

    Қазақстан — Шығыс Еуропа мен Орталық Азияда орналасқан мемлекет.

https://github.com/IS2AI/TurkicTTS/assets/6375187/847121e5-a2ef-45db-9418-f62e3ad0bfb0

---

**Kyrgyz**

    Кыргыз Республикасы — Борбордук Азияда жайгашкан мамлекет.

https://github.com/IS2AI/TurkicTTS/assets/6375187/cf6f4c78-d87d-4e58-a556-059e26f2e901

---

**Sakha**

    Саха Өрөспүүбүлүкэтэ Сибиир хотугулуу-илин өттүгэр сытар.

https://github.com/IS2AI/TurkicTTS/assets/6375187/4bb36e22-768e-41fd-a9c5-24ff6d35cbd2

---

**Turkmen**

    Türkmenistan merkezi Aziýada bir döwletdir.

https://github.com/IS2AI/TurkicTTS/assets/6375187/57a70217-c618-4caf-8038-0d5668e840f8

---

**Turkish**

    Türkiye'nin adı, ''Türk'' etnik kimliği adından gelir.

https://github.com/IS2AI/TurkicTTS/assets/6375187/fbceeace-4ae4-45a9-8376-a7fb477ca0ca

---

**Tatar**

    Татарстан территориясе — урманлы җирдә яткан тигезлек.

https://github.com/IS2AI/TurkicTTS/assets/6375187/331fa695-bc85-4afb-bccd-43ad22c9cc33

---

**Uyghur**

    Arabic: ئۇيغۇر خەلقى تۈركىي مىللەتلىرىنىڭ ئايرىلماس بىر قىسمى ھەم مۇھىم بىر تەركىبىي قىسمى.
    Cyrillic: Уйғур хәлқи түркий милләтлириниң айрилмас бир қисми һәм муһим бир тәркибий қисми.
    Latin: Uyghur xelqi türkiy milletlirining ayrilmas bir qismi hem muhim bir terkibiy qismi.

https://github.com/IS2AI/TurkicTTS/assets/6375187/6695091e-4fdd-4ed4-b785-289e3425326f

---

**Uzbek**

    Oʻzbekiston — Markaziy Osiyoning markaziy qismida joylashgan mamlakat.

https://github.com/IS2AI/TurkicTTS/assets/6375187/b5674d03-f977-4975-9d32-a9036c791b2d
