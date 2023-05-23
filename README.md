<h1 align="center">TurkicTTS <br> ⌨️ 🗣 </h1>

This repository provides the demo and the pre-trained models for the paper [Multilingual Text-to-Speech Synthesis for Turkic Languages Using Transliteration](link-once-published).

## Dataset 🗃️
Our study became feasible thanks to a large-scale and open-source speech corpus called 🇰🇿 [KazakhTTS2](https://github.com/IS2AI/Kazakh_TTS).

## Surveys 🎧 → 😡☹️😐🙂😀 → ⌨️
Below are the links to the ten questionnaires used in the study to collect subjective evaluations. These questionnaires were distributed on popular social media platforms operating in the Turkic languages. If you are interested, feel free to check them out. Your participation and input are greatly appreciated in helping us gather valuable data for our research. Your insights will contribute to a deeper understanding of the subject matter under investigation. 

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
 
