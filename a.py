import asyncio
from telethon.sync import TelegramClient, events
import requests

# Replace with your OpenWeatherMap API key
OWM_API_KEY = '19f929233df1d7aa07502a63cdc9bbf4'

# Replace with your Telegram API credentials
API_ID = '5948230'
API_HASH = 'dd19a00b085a219421a3717d0ae9c0d0'
BOT_TOKEN = '5231238723:AAGMilP_hDxn3qz4Whox3YTop4MuuHQwdX8'

# Set up the Telethon client
client = TelegramClient('weather_bot', API_ID, API_HASH)

async def send_weather_update():
    # Replace 'London' with the city you want weather updates for
    city = 'London'

    # Fetch weather data from OpenWeatherMap API
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}'
    response = requests.get(api_url)
    weather_data = response.json()

    # Extract relevant information from the API response
    temperature = weather_data.get('main', {}).get('temp')
    description = weather_data.get('weather', [{}])[0].get('description')

    # Prepare a stylishly formatted message
    message = (
        f"🌡️ **Temperature in {city}:** {temperature} K\n"
        f"🌦️ **Description:** {description}\n"
        "------------------------------------------"
    )

    await client.send_message('1237712948', message, parse_mode='Markdown')  # Replace with your destination

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi! I am your Stylish Weather Update Bot.')

async def main():
    while True:
        await send_weather_update()
        await asyncio.sleep(30)  # Wait for 30 seconds

if __name__ == '__main__':
    client.start(bot_token=BOT_TOKEN)
    asyncio.get_event_loop().run_until_complete(main())
    client.run_until_disconnected()
