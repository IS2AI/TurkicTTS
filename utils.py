import ipa_convert

dispatcher = {'kazakh' : ipa_convert.kazakh_to_ipa, 
              'turkish' : ipa_convert.turkish_to_ipa,
              'azerbaijani': ipa_convert.azerbaijani_to_ipa,
              'kyrgyz' : ipa_convert.kyrgyz_to_ipa,              
              'uzbek' : ipa_convert.uzbek_to_ipa,
              'turkmen' : ipa_convert.turkmen_to_ipa,
              'tatar' : ipa_convert.tatar_to_ipa,
              'bashkir' : ipa_convert.bashkir_to_ipa,
              'sakha' : ipa_convert.sakha_to_ipa,
              'uyghur' : ipa_convert.uyghur_to_ipa,              
              'tts_sent' : ipa_convert.ipa_to_kazakh}

def call_func(x, func):
    try:
        return dispatcher[func](x)
    except:
        return "Invalid function"

def normalization(x, lang="kazakh"):
    ipa_text = call_func(x, lang)
    kz_text = call_func(ipa_text, 'tts_sent')
    return kz_text