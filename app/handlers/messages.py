from aiogram import types

from app.bot import dp
from app.loggers import handlers_messages_log as logger
from app.texts import start_text, calculated_tax_text


@dp.message_handler(regexp=r"^\d+$")
async def income_text(message: types.Message):
    """
    Personal Allowance limit is under 12570.
    Basic rate is between [12571; 50270].
    Higher rate is between [50271; 125140].
    Additional rate is above 125140.
    """
    logger.error(f"message:\n{message}\n---")
    annual_income = float(message.text)

    pa_limit = 12570.0
    br_limit = 50270.0
    hr_limit = 125140.0

    br_tax_rate = 0.2
    hr_tax_rate = 0.4
    ad_tax_rate = 0.45

    basic_rate_tax = 0.0
    basic_rate_taxable_amount = 0.0
    higher_rate_tax = 0.0
    higher_rate_taxable_amount = 0.0
    additional_rate_tax = 0.0
    additional_rate_taxable_amount = 0.0

    excess_amount = annual_income
    if excess_amount > hr_limit:
        additional_rate_taxable_amount = excess_amount - hr_limit
        additional_rate_tax = additional_rate_taxable_amount * ad_tax_rate
        excess_amount = hr_limit

    if excess_amount > br_limit:
        higher_rate_taxable_amount = excess_amount - br_limit
        higher_rate_tax = higher_rate_taxable_amount * hr_tax_rate
        excess_amount = br_limit

    if excess_amount > pa_limit:
        basic_rate_taxable_amount = excess_amount - pa_limit
        basic_rate_tax = basic_rate_taxable_amount * br_tax_rate
        excess_amount = pa_limit

    personal_allowance = excess_amount

    total_tax_amount = round(basic_rate_tax + higher_rate_tax + additional_rate_tax, 2)
    take_home_pay = round(annual_income - total_tax_amount, 2)
    await message.answer(
        text=calculated_tax_text.format(
            annual_income=annual_income,
            pa=personal_allowance,
            brt=basic_rate_tax,
            brta=basic_rate_taxable_amount,
            hrt=higher_rate_tax,
            hrta=higher_rate_taxable_amount,
            art=additional_rate_tax,
            arta=additional_rate_taxable_amount,
            tta=total_tax_amount,
            ethpy=take_home_pay,
            ethpm=round(take_home_pay / 12, 2),
        ),
    )


@dp.message_handler()
async def unknown_text(message: types.Message):
    logger.error(f"unknown message:\n{message}\n---")
    await message.answer(text=start_text)
