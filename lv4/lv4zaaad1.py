import pandas as pd
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('titanic.csv')

broj_zena = titanic_df[titanic_df['Sex'] == 'female'].shape[0]
print(f'a) Broj žena u skupu podataka: {broj_zena}')

postotak_ne_prezivjelih = (1 - titanic_df['Survived'].mean()) * 100
print(f'b) Postotak osoba koje nisu preživjele potonuće broda: {postotak_ne_prezivjelih:.2f}%')

prezivjeli_po_spolu = titanic_df.groupby('Sex')['Survived'].mean() * 100

plt.bar(prezivjeli_po_spolu.index, prezivjeli_po_spolu.values, color=['yellow', 'green'])
plt.xlabel('Spol')
plt.ylabel('Postotak preživjelih')
plt.title('Postotak preživjelih po spolu')
plt.show()

prosjecna_dob_zena = titanic_df[titanic_df['Sex'] == 'female']['Age'].mean()
prosjecna_dob_muskaraca = titanic_df[titanic_df['Sex'] == 'male']['Age'].mean()

print(f'd) Prosječna dob preživjelih žena: {prosjecna_dob_zena:.2f} godina')
print(f'   Prosječna dob preživjelih muškaraca: {prosjecna_dob_muskaraca:.2f} godina')

najstariji_muškarac_po_klasi = titanic_df[titanic_df['Sex'] == 'male'].groupby('Pclass')['Age'].max()
print('e) Najstariji preživjeli muškarac po klasi:')
print(najstariji_muškarac_po_klasi)