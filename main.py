import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')

# Перевірка на пропуски
print("Пропуски в даних:\n", df.isnull().sum())

# Очищення даних
# Заповнення пропусків у стовпці "Revenue (Millions)" середнім значенням
df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean())

# Видалення рядків з пропусками в інших стовпцях
df_cleaned = df.dropna()

# Підсумкова таблиця
print("\nОчищені дані:\n", df_cleaned)


# Гіпотеза 1: Фільми після 2015 року мають середню оцінку вище 7.0
avg_rating_post_2015 = df_cleaned[df_cleaned['Year'] > 2015]['Rating'].mean()
hypothesis_1 = "Так" if avg_rating_post_2015 > 7.0 else "Ні"

# Гіпотеза 2: Фільми жанру "Action" мають більший середній дохід
df_cleaned['Is_Action'] = df_cleaned['Genre'].str.contains("Action")
action_revenue_mean = df_cleaned[df_cleaned['Is_Action']]['Revenue (Millions)'].mean()
non_action_revenue_mean = df_cleaned[~df_cleaned['Is_Action']]['Revenue (Millions)'].mean()
hypothesis_2 = "Так" if action_revenue_mean > non_action_revenue_mean else "Ні"

# Гіпотеза 3: Фільми з рейтингом понад 8.0 мають більше голосів
high_rating_votes = df_cleaned[df_cleaned['Rating'] > 8.0]['Votes'].mean()
low_rating_votes = df_cleaned[df_cleaned['Rating'] <= 8.0]['Votes'].mean()
hypothesis_3 = "Так" if high_rating_votes > low_rating_votes else "Ні"

# Результати
print(f"Гіпотеза 1: {hypothesis_1}")
print(f"Гіпотеза 2: {hypothesis_2}")
print(f"Гіпотеза 3: {hypothesis_3}")


# Сортування даних за рейтингом у спадному порядку та вибір топ-100 фільмів
top_10_movies = df.nlargest(10, 'Rating')

# Побудова лінійного графіка для топ-10 фільмів за рейтингом
plt.figure(figsize=(10, 6))
plt.plot(top_10_movies['Year'], top_10_movies['Rating'], marker='o', label='Рейтинг')
plt.title('Рейтинг топ-10 фільмів')
plt.xlabel('Рік')
plt.ylabel('Рейтинг')
plt.grid(True)
# plt.legend()
plt.show()

# 2. Стовпчаста діаграма: Кількість голосів для кожного фільму
plt.figure(figsize=(12, 6))
plt.bar(df['Title'], df['Votes'], color='skyblue')
plt.title('Кількість голосів для кожного фільму')
plt.xlabel('Фільм')
plt.ylabel('Голосів')
plt.xticks(rotation=45, ha='right')
plt.show()

# 3. Кругова діаграма: Розподіл жанрів
genre_counts = df['Genre'].apply(lambda x: x.split(',')[0]).value_counts()
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Розподіл жанрів фільмів')
plt.show()

# 4. Гістограма: Розподіл тривалості фільмів
plt.figure(figsize=(10, 6))
plt.hist(df['Runtime (Minutes)'], bins=10, color='purple', edgecolor='black')
plt.title('Розподіл тривалості фільмів')
plt.xlabel('Тривалість (хвилини)')
plt.ylabel('Кількість фільмів')
plt.show()

# 5. Діаграма розсіювання: Рейтинг проти доходу
plt.figure(figsize=(10, 6))
plt.scatter(df['Rating'], df['Revenue (Millions)'], color='green', alpha=0.7)
plt.title('Рейтинг проти доходу')
plt.xlabel('Рейтинг')
plt.ylabel('Дохід (млн)')
plt.grid(True)
plt.show()

