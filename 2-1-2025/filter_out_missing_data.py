from numpy import nan as NA
import pandas as pd

# Filtering Out Missing Data
data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)

# Xóa hàng có NA
cleaned_row = data.dropna()
print(cleaned_row)

# Xóa cột có NA
cleaned_col = data.dropna(axis=1)
print(cleaned_col)

#Xóa hàng có tất cả các giá trị là NA
cleaned2=data.dropna(how='all')
print(cleaned2)


