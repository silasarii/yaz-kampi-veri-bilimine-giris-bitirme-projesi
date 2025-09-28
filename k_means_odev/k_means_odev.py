#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[5]:


data = pd.read_csv('dava.csv')
data


# ## Veri Seti inceleme
# Veri Seti Özellikleri:  
# Case Duration (Gün): Davanın tamamlanması için geçen süre (gün cinsinden).  
# Number of Witnesses (Tanık Sayısı): Dava boyunca dinlenen tanık sayısı.  
# Legal Fees (Hukuk Maliyetleri): Dava süresince oluşan toplam hukuk maliyetleri (USD cinsinden).  
# Number of Evidence Items (Delil Sayısı): Davada kullanılan delil sayısı.  
# Severity (Ciddiyet Düzeyi): Davanın ciddiyet düzeyi (1: Düşük, 2: Orta, 3: Yüksek).  
# Outcome (Sonuç): Davanın sonucu (0: Aleyhte, 1: Lehinde).  

# ## GÖREV: 
# Özellik Seçimi: Hangi özelliklerin kümeleme için kullanılacağına karar verin.  
# Küme Sayısını Belirleme: Elbow yöntemi gibi tekniklerle optimal küme sayısını belirleyin.  
# Kümeleme İşlemi: K-Means algoritmasını kullanarak verileri kümeleyin.  
# Sonuçları Görselleştirme: Kümeleme sonuçlarını uygun grafiklerle görselleştirin ve yorumlayın.  

# In[ ]:

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Özellik seçimi
features = ['Case Duration (Gün)', 'Number of Witnesses', 'Legal Fees', 'Number of Evidence Items', 'Severity']
X = data[features]

# 2. Özellikleri ölçeklendirme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Elbow yöntemi ile optimal küme sayısını bulma
inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Elbow grafiği
plt.figure(figsize=(8,5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Küme Sayısı (k)')
plt.ylabel('Inertia')
plt.title('Elbow Yöntemi ile Optimal Küme Sayısı')
plt.show()

# 4. K-Means ile kümeleme (örneğin k=3)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
data['Cluster'] = clusters

# 5. Kümeleme sonuçlarını görselleştirme
plt.figure(figsize=(8,6))
plt.scatter(data['Case Duration (Gün)'], data['Legal Fees'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Case Duration (Gün)')
plt.ylabel('Legal Fees')
plt.title('K-Means Kümeleme Sonuçları')
plt.show()







