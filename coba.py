import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')

# print (data.info())
# print (data.describe())
# print (data.head())

# print('rata rata', data['Nilai'].mean())
# print('median', data['Nilai'].median())
# print('modus', data['Nilai'].mode()[0])

# matematika = data[data['Matpel'] == 'Matematika']
# print(matematika)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data .groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color=['red', 'blue', 'green', 'orange', 'purple'])
plt.title('Rata-rata Nilai Siswa per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai rata -rata')
plt.show()

sn.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Distribusi Nilai Siswa per Matpel')
plt.tight_layout()
plt.show()
