from pyngrok import ngrok
import os

# Set your ngrok authtoken
NGROK_AUTH_TOKEN = "2oQFcYppYVC2gyzwqg4944wuqKB_4Cqkik6md8ZiVy5drsZse"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Start ngrok tunnel
public_url = ngrok.connect(8000)
print(f'Your public URL is: {public_url}')

# Run the Django server
os.system('python manage.py runserver 8000')