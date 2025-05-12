import pandas as pd

df = pd.read_csv('Task_2\companies_10k_reports.csv', usecols=range(7))

for col in df.columns[2:]:
    df[col] = df[col].str.replace(',', '').astype(int)

df = df.sort_values(by=['Company', 'Fiscal Year'])
df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue (in millions USD)'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income (in millions USD)'].pct_change() * 100

summary_stats = df.groupby('Company')[[
    'Total Revenue (in millions USD)',
    'Net Income (in millions USD)',
    'Operating Cash Flow (in millions USD)',
    'Revenue Growth (%)',
    'Net Income Growth (%)'
]].agg(['mean', 'std', 'min', 'max'])

trend_by_year = df.groupby('Fiscal Year')[[
    'Total Revenue (in millions USD)',
    'Net Income (in millions USD)'
]].mean().reset_index()


def simple_chatbot(user_query):
    canned_responses = {
        "What is the total revenue of Microsoft in 2024?": "Microsoft's total revenue in 2024 was $245.1 billion.",
        "How has net income changed for Tesla from 2023 to 2024?": "Tesla's net income decreased by 52.2% from 2023 to 2024.",
        "What was Apple’s operating cash flow in 2022?": "Apple's operating cash flow in 2022 was $122.2 billion.",
        "Which company had the highest revenue in 2024?": "Microsoft had the highest revenue in 2024 at $245.1 billion.",
        "What is the revenue growth of Apple in 2023?": "Apple's revenue decreased by 2.8% in 2023."
    }

    response = canned_responses.get(user_query, "Sorry, I can only provide information on predefined queries.")
    return response

# Example interaction
while True:
    user_input = input("Ask a financial question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(simple_chatbot(user_input))