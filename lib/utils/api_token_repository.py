# Provides utility functions for accessing various API tokens required by the application

def get_telegram_access_token(fp: str) -> str:
    with open(fp) as bot_key_file:
        return bot_key_file.read()
