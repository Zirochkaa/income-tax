[![pytest](https://github.com/Zirochkaa/income-tax/actions/workflows/run_tests.yml/badge.svg?branch=master)](https://github.com/Zirochkaa/income-tax/actions/workflows/run_tests.yml)

# Income tax

This repository contains pet project - telegram bot designed for calculating income tax for England, Northern Ireland and Wales :)

### Link to the working telegram bot here - [@income_tax_uk_bot](https://t.me/income_tax_uk_bot).

## Run project locally

1. Setup and activate your local python environment. [Here](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3) are few guides on how to do it.
2. Install requirements:
   ```shell 
   pip install -r requirements-local.txt
   ```
3. Create `.env` file:
   ```shell 
   cp app/.env.template app/.env
   ```
4. Obtain Telegram Bot Token by creating Telegram Bot. 
[Here](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) (`Obtain Your Bot Token` section) is a guide on how to do it. 
Update `TELEGRAM_BOT_TOKEN` in `.env` file.
5. This app uses a webhook approach to processing bot updates. 
In order to do it your localhost has to be put on the internet.
You can achieve this by using [ngrok](https://ngrok.com). You need to [install](https://ngrok.com/download) it and run:
   ```shell 
   ./ngrok http 8000
   ```
   After running above command you will see something like this: 
<img width="829" alt="image" src="https://github.com/airbytehq/airbyte/assets/19872253/b1afc285-4fff-4f7f-b6fd-f03a67655b4c">

   You will need to copy `Forwarding` part (for example, on the screenshot it will be `https://03d2-146-70-181-35.ngrok-free.app`) and update `APP_BASE_URL` in `.env` file.
6. It's time to run application:
   ```shell 
   uvicorn app.run:app --reload
   ```
7. Go to [127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

## Tests

To run tests use following command:
   ```shell 
   pytest tests/
   ```

If you want to check code coverage use following command:
   ```shell 
   pytest --cov-config=.coveragerc --cov=app tests/
   ```
