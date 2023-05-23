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
<!--   <a href="https://arxiv.org/abs/2303.00747">
        <img src="http://img.shields.io/badge/Arxiv-2303.00747-B31B1B.svg"
             alt="ArXiv paper">
  </a> -->
  <a href="https://twitter.com/intent/tweet?text=&url=https%3A%2F%2Fgithub.com%2Fm-bain%2FwhisperX">
  <img src="https://img.shields.io/twitter/url/https/github.com/m-bain/whisperX.svg?style=social" alt="Twitter">
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

[Azerbaijani](https://nukz.qualtrics.com/jfe/form/SV_bNu5RvcsYMKkU8m) | [Bashkir](https://nukz.qualtrics.com/jfe/form/SV_cvl3H1U8EbFM4Tk) | [Kazakh](https://nukz.qualtrics.com/jfe/form/SV_3WelDTOVyKK5iom) | [Kyrgyz](https://nukz.qualtrics.com/jfe/form/SV_cAT00TOsCNKsSZE) | [Sakha](https://nukz.qualtrics.com/jfe/form/SV_2awH2YEoL5V7biC) | [Tatar](https://nukz.qualtrics.com/jfe/form/SV_0dEAXvcHxAiEYxo) | [Turkish](https://nukz.qualtrics.com/jfe/form/SV_cItR7tzYRRjlkYC) | [Turkmen](https://nukz.qualtrics.com/jfe/form/SV_cVgQk4lgS17HBgW) | [Uyghur](https://nukz.qualtrics.com/jfe/form/SV_ezZO1jNowvrAdds) | [Uzbek](https://nukz.qualtrics.com/jfe/form/SV_01BJgR96UMZ3fOm)
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

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
 
