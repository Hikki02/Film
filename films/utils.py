import os
from hashlib import sha1


def get_clinic_image_path(instance, filename):
    hashname = sha1(filename).hexdigest() + '.jpg'
    return os.path.join('clinic', hashname[:2], hashname[2:4],
                        hashname)
