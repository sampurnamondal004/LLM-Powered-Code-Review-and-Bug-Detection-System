import openai

openai.api_key = "YOUR_API_KEY"

def review_with_llm(code, language):
    prompt = f"""
    You are a senior software engineer.
    Review the following {language} code.
    Identify:
    - Bugs
    - Security issues
    - Code smells
    - Improvements

    Code:
    {code}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
