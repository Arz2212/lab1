import matplotlib.pyplot as plt
import pandas as pd
data = []
with open('3.csv', 'r', encoding='utf-8') as f:
    for line in f:
        prep, group, mark = line.strip().split(';')
        data.append({'prep': prep, 'group': group, 'mark': int(mark)})

df = pd.DataFrame(data)
plt.figure(figsize=(14, 8))
plt.subplot(2, 1, 1)
prep_marks = df.groupby(['prep', 'mark']).size().unstack()
prep_marks.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='viridis')
plt.title('Распределение оценок по преподавателям', pad=20)
plt.ylabel('Количество студентов')
plt.xlabel('Преподаватель')
plt.legend(title='Оценка', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.subplot(2, 1, 2)
group_marks = df.groupby(['group', 'mark']).size().unstack()
group_marks.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='plasma')
plt.title('Распределение оценок по группам', pad=20)
plt.ylabel('Количество студентов')
plt.xlabel('Группа')
plt.legend(title='Оценка', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout()
plt.show()