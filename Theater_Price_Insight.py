import pandas as pd
from io import StringIO

def find_cheapest_space_per_seat(df, show_price_column):
    num_shows = int(show_price_column.split()[0])
    price_per_seat = df[show_price_column] / (df['Maximum Seats'] * num_shows)
    min_index = price_per_seat.idxmin()

    return df.loc[min_index, 'Theater'], round(price_per_seat[min_index], 3)

# provided data
given_string = """Theater,Maximum Seats,3 Show Price,5 Show Price
Stephanie Feury,42,$988,$1512
McCadden Place Theater,60,$1074,$1690
Shirley Dawn,50,$774,$1060"""

# Convert string to pandas dataframe
my_options = given_string.replace('$', '')
df = pd.read_csv(StringIO(my_options))

# run function and print dictionary
shows3results = find_cheapest_space_per_seat(df, '3 Show Price')
shows5results = find_cheapest_space_per_seat(df, '5 Show Price')
print({3: shows3results, 5: shows5results})

import math

def find_break_even_point(theater_name, show_price_column):
    theater_price = df.loc[df['Theater'] == theater_name, show_price_column]
    sales_per_person = math.ceil(theater_price/10)/6
    return sales_per_person


average_3 = find_break_even_point(shows3results[0], '3 Show Price')
average_5 = find_break_even_point(shows3results[0], '5 Show Price')

print([average_3, average_5, abs(average_3-average_5)])