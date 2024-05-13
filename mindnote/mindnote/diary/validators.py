from django.core.exceptions import ValidationError
import datetime

def validate_no_hash(value):
    if ('#' in value):
        raise ValidationError('"#"을 입력할 수 없습니다.', code='no-hash-error')
    
def validate_no_numbers(values):
    for value in values:
        if value.isdigit():
            raise ValidationError('"감정 상태"에는 숫자가 들어갈 수 없습니다.', code='no-numbers-error')
    return True

def validate_score(value):
    if (value < 0) or (value > 10):
        raise ValidationError('"감정 점수"는 0부터 10사이의 숫자만 들어갈 수 있습니다.', code='score-error')
    
def validate_date(value):
    try:
        datetime.datetime.strptime(str(value), "%Y-%m-%d")
    except ValueError:
        raise ValidationError('0000년 00월 00일의 형식으로 작성해주세요.', code='date-error')
