import openai
import time


def classify_news(news_title, news_content):
    prompt = f"""
    제목 : "{news_title}"
    내용 : "{news_content}"
    카테고리: 정치, 경제, 사회, 문화, 스포츠, 과학, IT
    해당하는 카테고리 하나만 말해줘.
    여기에 없으면 새로 만들어서 말해줘도 괜찮아
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        category = response['choices'][0]['message']['content'].strip()
        return category

    except openai.error.RateLimitError:
        print("Rate limit에 걸렸습니다. 5초 후 재시도합니다...")
        time.sleep(5)
        return classify_news(news_title, news_content)  # 재귀 호출로 재시도

    except Exception as e:
        print("기타 오류:", e)
        return "분류 실패"

#3줄용약
def news_summary_by_gpt(news_content):
    prompt = f"""
    내용 : "{news_content}"
    위 내용을 너무 길지않게 3줄 요약해줘.
    내용이 짧다면 2줄, 1줄 요약해도 괜찮아
    """

    try:
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [{'role':'user', 'content':prompt}],
            temperature=0.2,
        )

        summary = response['choices'][0]['message']['content'].strip()
        return summary

    except Exception as e:
        print('에러 발생 : ', e)
        return False
