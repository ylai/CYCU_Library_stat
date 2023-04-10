###############################################################
#
#      CYCU Library Books Statistics
#
# 2023.03.25 V1.0
# (1)簡單的敘述性統計:
#    計算每位學生，每個系別和每本書的平均值、中位數、眾數、標準差和範圍。
#    這將有助於識別最受歡迎的書籍，系別和經常借書的學生。
###############################################################
import pandas as pd
import matplotlib.pyplot as plt
# 讀取 CSV 文件
#df = pd.read_csv('data-1679628612278.csv')
#testing
df = pd.read_csv('test1.csv')

# 將時間列轉換為日期格式
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d %H:%M:%S')
#print(df['Date'])
# 按照月份分組，計算每月借出的書籍數量
books_per_month = df.groupby(pd.Grouper(key='Date', freq='M'))['Title'].count()

# Print the latest and oldest date
oldest_date = df['Date'].min().strftime("%Y-%m-%d")
latest_date = df['Date'].max().strftime("%Y-%m-%d")
print(f"Oldest date: {oldest_date}")
print(f"Latest date: {latest_date}")

# 計算月借出的書籍數量的平均值、中位數和標準差
mean_books_per_month = books_per_month.mean()
median_books_per_month = books_per_month.median()
std_books_per_month = books_per_month.std()

# 印結果
print('月借出的書籍平均值：', mean_books_per_month)
print('月借出的書籍中位數：', median_books_per_month)
print('月借出的書籍標準差：', std_books_per_month)
# 繪製條形圖
plt.figure(figsize=(15, 7.5))  # Set size of figure to 1024 x 768
plt.bar(books_per_month.index.strftime('%Y-%m'), books_per_month.values)
#plt.plot(books_per_month.index, books_per_month.values, marker='.')
plt.title('Monthly Book Borrowing Record')
plt.xlabel('Month')
plt.ylabel('Number of Books Borrowed')
fig1 = plt.gcf() # Get current figure
fig1.savefig('monthly_borrowing_record.png', dpi=300) # Save as png with 300 dpi resolution
plt.show()# Save the figure using savefig()