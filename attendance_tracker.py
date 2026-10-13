from sklearn.preprocessing import MinMaxScaler
values=[[200000],[500000],[800000]]
scaler=MinMaxScaler()
scaled_values=scaler.fit_transform(values)
print(scaled_values)