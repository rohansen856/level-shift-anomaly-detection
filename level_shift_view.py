from load_data import load_data, plot_base_line


filename = 'dau.csv'
x_column = 'Date'
y_column = 'DAU'
df = load_data(filename,x_column,y_column)

# df = df['2022-09-01':'2022-11-12']
plot_base_line(df,y_column)