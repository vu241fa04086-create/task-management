import google.generativeai as genai


genai.configure(
    api_key="AQ.Ab8RN6KpFH3TbWql9k6pXuHNS6lmC5xyx9PBGU6oSroshn5a3g"
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_ai_service(message):

    response = model.generate_content(
        message
    )

    return response.text