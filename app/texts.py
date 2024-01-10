start_text = (
    "Hello, I will help you with calculating income tax for England, Northern Ireland and Wales.\n"
    "Just send me your annual income (like <code>70000</code> or <code>25000</code>) and "
    "I will calculate how much money you will have left after taxes.\n\n"
    "Here are few related links:\n"
    "- information about things for which you pay and do not pay taxes is <a href='https://www.gov.uk/income-tax'>here</a>\n"
    "- information about different allowances is <a href='https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past#other-allowances'>here</a>\n"
    "- information about income limit for personal allowance is <a href='https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past#personal-allowances'>here</a>\n"
    "- information about Employee National Insurance rates is <a href='https://www.gov.uk/national-insurance-rates-letters#employee-national-insurance-rates'>here</a>\n"
    "- information about National Insurance categories is <a href='https://www.gov.uk/national-insurance-rates-letters/category-letters'>here</a>\n"
)

calculated_tax_text = (
    "Calculated taxes for <code>£{annual_income}</code> annual income:\n"
    "- Personal Allowance (tax-free) = <code>£{pa}</code>\n"
    "- Basic rate (20%) = <code>£{brt}</code> (based on <code>£{brta}</code> of taxable amount)\n"
    "- Higher rate (40%) = <code>£{hrt}</code> (based on <code>£{hrta}</code> of taxable amount)\n"
    "- Additional rate (45%) = <code>£{art}</code> (based on <code>£{arta}</code> of taxable amount)\n\n"
    "Total tax amount = <code>£{tta}</code>\n"
    "Estimated take-home pay = <code>£{ethpy}</code>/year or <code>£{ethpm}</code>/month\n"
    "<i>Please note that estimated take-home pay does not include deductions for <a href='https://www.gov.uk/national-insurance-rates-letters#employee-national-insurance-rates'>National Insurance</a>.</i>"
)
