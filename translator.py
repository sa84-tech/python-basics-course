import googletrans


def get_translation(text, translate_from='auto', translate_to='ru'):
    try:
        translator = googletrans.Translator()
        t_obj = translator.translate(text, translate_to, translate_from)
        return t_obj.text

    except TimeoutError:
        return 'Timeout Error'
    except ConnectionError:
        return 'Connection Error'
    except AttributeError:
        return 'Attribute Error'
    except ValueError:
        return 'TypeError'
