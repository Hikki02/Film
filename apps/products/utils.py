import os
from datetime import datetime

"""зделать автоматическое создание папки"""


def get_upload_path(instance, filename):
    return os.path.join('product/image/', datetime.now().date().strftime("%Y/%m/%d"), filename)