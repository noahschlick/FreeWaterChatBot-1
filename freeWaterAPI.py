import requests

# Call the FreeWater AI API to get a response
async def getAnswer(user_querie):
    response = requests.get(f'https://freewaterchatbotapi.onrender.com/api?input={user_querie}')
    return response.json()