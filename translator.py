# Before starting, you need to install dependencies by running the command:
# pip install -r requirements.txt

from googletrans import Translator


def get_translation(data, translate_from='auto', translate_to='ru', attr_error_limit=10):
    """

    :param data: str - data to translate
    :param translate_from: str
    :param translate_to:  str
    :param attr_error_limit: int - limit of attempts to translate text with returned Attribute Error.
    :return: dict
    """
    attr_error_count = 0

    while True:
        try:
            t_obj = Translator().translate(data, translate_to, translate_from)
            return dict(text=t_obj.text, warning=f'Number of Attribute Errors: {attr_error_count}') \
                if attr_error_count else dict(text=t_obj.text)

        except TimeoutError:
            return dict(text=data, error='Timeout Error')
        except ConnectionError:
            return dict(text=data, error='Connection Error')
        except AttributeError:
            attr_error_count += 1
            if attr_error_count >= attr_error_limit:
                return dict(text=data, error=f'Attribute Error Limit Exceeded: {attr_error_count}')
        except ValueError:
            return dict(text=data, error='ValueError')
