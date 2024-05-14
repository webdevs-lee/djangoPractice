from .models import Page
import random

def validate_pages():
    pages = Page.objects.all()

    for page in pages:
        if page.score < 0 or page.score > 10:
            print(page.id, '번의 감정점수가 수정되었습니다.')
            page.score = random.randrange(0,10)
            page.save()