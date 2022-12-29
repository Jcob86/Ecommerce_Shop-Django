from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_kb = 5120
    
    if file.size > max_size_kb * 1024:
        raise ValidationError('Files cannot be larger than 5MB')