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
<p align = "justify">Our study became feasible thanks to a large-scale and open-source speech corpus called 🇰🇿 <a href = "https://github.com/IS2AI/Kazakh_TTS">KazakhTTS2</a>. The corpus contains five voices (three female and two male) and more than 270 hours of high-quality transcribed data. KazakhTTS2 is publicly available, which permits both academic and commercial use.</p> 

## Approach 🛠
<p align = "justify">To enable speech synthesis for the Turkic languages, we constructed an <a href = "https://en.wikipedia.org/wiki/International_Phonetic_Alphabet">IPA</a>-based conversion module. The IPA-based converter takes letters from the alphabets of other Turkic languages and converts them into the letters of the Kazakh alphabet. For this purpose, the letters entered are first converted into the corresponding IPA representations. Next, the IPA symbols are converted into the letters of the Kazakh alphabet, which can be used as input for the TTS models constructed.</p>
<p align = "justify">The mappings of the Turkic alphabets onto IPA symbols were manually created based on our expertise, as we could not find a complete mapping that would allow an error-free conversion from Turkic to Kazakh and cover all the languages addressed. Since Kazakh is used as a source language, we selected only 42 IPA symbols corresponding to the 42 letters of the Kazakh alphabet. It is worth mentioning that, of the Turkic languages in question, Kazakh—along with Bashkir—has the most letters and contains a large majority of the phonemes of the target languages. The developed mappings can also be used as a guide for other work aimed at building multilingual systems for Turkic languages, such as speech recognition, speech translation, and so on. The mapping of the Turkic alphabets onto IPA symbols can be found <a href = "https://github.com/IS2AI/TurkicTTS/blob/branch/ipa_mapping.pdf">here</a>.</p>

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

## Evaluation results
<p align = "justify">The survey statistics for rater number (R), gender (F & M), and age ( < 45 & 45+) and the evaluation results of the overall quality (Q), comprehensibility (C), and intelligibility (I) of synthesised speech.</p>

| Language | R | F | M | < 45 | 45+ | Q | C | I |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Azerbaijani | 47 | 22 | 25 | 22 | 25 | 2.93 | 90% | 52% |
| Bashkir | 11 | 8 | 3 | 4 | 7 | 2.67 | 92% | 47% |
| Kazakh | 151 | 89 | 62 | 120 | 31 | 4.18 | 97% | 80% |
| Kyrgyz | 14 | 12 | 2 | 6 | 8 | 3.54 | 86% | 43% |
| Sakha | 254 | 155 | 99 | 147 | 107 | 2.85 | 93% | 15% |
| Tatar | 15 | 12 | 3 | 3 | 12 | 2.82 | 79% | 17% |
| Turkish | 18 | 6 | 12 | 15 | 3 | 3.25 | 91% | 61% |
| Turkmen | 6 | 0 | 6 | 6 | 0 | 2.37 | 67% | 57% |
| Uyghur | 10 | 6 | 4 | 6 | 4 | 3.01 | 45% | 26% |
| Uzbek | 22 | 2 | 20 | 19 | 3 | 2.85 | 80% | 45% |
| **Total** | **548** | **312** | **236** | **348** | **200** | **3.25** | **92%** | **41%** |

## Pretrained models ⚙️
Unzip both the pre-trained vocoder and the acoustic model in the same directory.

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

### specify path to the main model(transformer/tacotron2/fastspeech) and its config file
config_file = "exp/tts_train_raw_char/config.yaml"
model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"

text2speech = Text2Speech(
    config_file,
    model_path,
    device="cuda", ## if cuda not available use cpu
    ### only for Tacotron 2
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=True,
    backward_window=1,
    forward_window=3,
    ### only for FastSpeech & FastSpeech2
    speed_control_alpha=1.0,
)
text2speech.spc2wav = None  ### disable griffin-lim

text = "merhaba"
### available options are azerbaijani, bashkir, kazakh, kyrgyz, sakha, tatar, turkish, turkmen, uyghur, uzbek
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

**Tatar**

    Татарстан территориясе — урманлы җирдә яткан тигезлек.

https://github.com/IS2AI/TurkicTTS/assets/6375187/331fa695-bc85-4afb-bccd-43ad22c9cc33

---

**Turkish**

    Türk dünyası, tüm Türk halkları kapsayan bir kavramdır.

https://github.com/IS2AI/TurkicTTS/assets/6375187/527430a1-f8f3-472c-8b32-3540e4dc5d96

---

**Turkmen**

    Türkmenistan merkezi Aziýada bir döwletdir.

https://github.com/IS2AI/TurkicTTS/assets/6375187/57a70217-c618-4caf-8038-0d5668e840f8

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

## Acknowledgements 🙏
<p align = "justify">We would like to extend our heartfelt thanks to all individuals who contributed to the recruitment of participants for this study. Their efforts were critical to the success of our survey. In particular, we would like to express our deepest appreciation to Viktor Krivogornitsyn for his extraordinary dedication in attracting a substantial number of Sakha speakers. His contribution was invaluable, and we are grateful for his support.</p>

## Citation 🎓
<p align = "justify">We kindly request that if you utilise our model in your work, you consider citing our paper to acknowledge its contribution. Citing the appropriate sources helps promote academic integrity and ensures that credit is given to the original authors. By acknowledging our paper in your research, you contribute to the ongoing development and advancement of the scientific community. We appreciate your support and recognition of our efforts.</p>

```bibtex
@inproceedings{turkic_tts,
  title={Multilingual Text-to-Speech Synthesis for Turkic Languages Using Transliteration},
  author={Yeshpanov, Rustem and Mussakhojayeva, Saida and Khassanov, Yerbolat},
  journal={},
  year={2023}
}
```
