from django.core.exceptions import ValidationError

def file_size(value):
    filesize = value.size
    if filesize > 1200000000:
        raise ValidationError("Maximum size is 150Mb")