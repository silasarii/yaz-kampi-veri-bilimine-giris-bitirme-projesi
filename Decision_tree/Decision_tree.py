#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv('dava_sonuclari.csv')
data.head()


# ## VERİ SETİ İNCELEME : 
# Case Type: Davanın türü (Criminal, Civil, Commercial)  
# Case Duration (Days): Davanın süresi (gün olarak)  
# Judge Experience (Years): Hakimin deneyim yılı  
# Number of Witnesses: Tanık sayısı  
# Legal Fees (USD): Hukuk masrafları (USD olarak)  
# Plaintiff's Reputation: Davacının itibarı (1: Düşük, 2: Orta, 3: Yüksek)  
# Defendant's Wealth (USD): Davalının serveti  
# Number of Evidence Items: Delil sayısı  
# Number of Legal Precedents: İlgili hukuki emsal sayısı  
# Settlement Offered (USD): Teklif edilen uzlaşma miktarı  
# Severity: Davanın ciddiyet derecesi (1: Düşük, 2: Orta, 3: Yüksek)  
# Outcome: Davanın sonucu (0: Kaybetmek, 1: Kazanmak)  

# ## Görevler
# 
# ### Veri Ön İşleme:
# * Veri setini inceleyin ve eksik veya aykırı değerler olup olmadığını kontrol edin.  
# * Gerektiğinde eksik verileri doldurun veya çıkarın.  
# * Özelliklerin ölçeklendirilmesi gibi gerekli veri dönüşümlerini uygulayın. 

print(data.head())
print(data.info())
print(data.describe())

print("Eksik değer sayısı:\n", data.isnull().sum())


import matplotlib.pyplot as plt

num_cols = data.select_dtypes(include=['int64','float64']).columns

for col in num_cols:
    plt.figure()
    data.boxplot([col])
    plt.title(col)
    plt.show()

data_encoded = pd.get_dummies(data, drop_first=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_encoded.drop("Outcome", axis=1))

# ### Veri Setini Ayırma:
# * Veri setini eğitim ve test setleri olarak ayırın (örn. %80 eğitim, %20 test).  


from sklearn.model_selection import train_test_split

# Özellikler (X) ve hedef değişken (y)
X = data_encoded.drop('Outcome', axis=1)  
y = data_encoded['Outcome']

# Eğitim - Test ayırma (%80 eğitim, %20 test)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("Eğitim veri boyutu:", x_train.shape)
print("Test veri boyutu:", x_test.shape)

# ### Model Kurulumu:
# * Karar ağacı modelini oluşturun ve eğitim verileri üzerinde eğitin.

from sklearn.tree import DecisionTreeClassifier

# Karar ağacı modelini oluştur
dt_model = DecisionTreeClassifier(random_state=42)

# Modeli eğitim verileri üzerinde eğit
dt_model.fit(x_train, y_train)

print("Karar ağacı modeli başarıyla eğitildi")

# ### Modeli Değerlendirme:
# * Test verilerini kullanarak modelin doğruluğunu değerlendirin.
# * Doğruluk, precision, recall ve F1-score gibi performans metriklerini hesaplayın.

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Test verileri üzerinde tahmin yap
y_pred = dt_model.predict(x_test)

# Performans metriklerini hesapla
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print("Model Değerlendirme Sonuçları:")
print(f"Doğruluk (Accuracy): {accuracy:.4f}")
print(f"Kesinlik (Precision): {precision:.4f}")
print(f"Duyarlılık (Recall): {recall:.4f}")
print(f"F1 Skoru: {f1:.4f}")
print("\nDetaylı Sınıflandırma Raporu:\n")
print(classification_report(y_test, y_pred))


# ### Sonuçları Görselleştirme:
# * Karar ağacının yapısını görselleştirin.
# * Karar ağacının nasıl çalıştığını ve hangi özelliklerin davanın sonucunu belirlemede en etkili olduğunu açıklayın.

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(
    dt_model, 
    feature_names=x.columns, 
    class_names=['Kaybet', 'Kazan'], 
    filled=True, 
    rounded=True
)
plt.show()

# In[ ]:




