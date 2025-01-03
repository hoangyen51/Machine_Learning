from numpy import nan as NA
import pandas as pd

# Filling In Missing Data
data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)

# Điền các NA bằng giá trị trung bình của cột
cleaned_mean=data.fillna(data.mean())
print(cleaned_mean)

# Điền các NA bằng giá trị trung vị của cột
cleaned_median=data.fillna(data.median())
print(cleaned_median)

# Điền các NA bằng giá trị yếu vị của cột
cleaned_mode=data.fillna(data.mode())
print(cleaned_mode)

# Điền các NA bằng giá trị cụ thể: 0
cleaned_specific=data.fillna(0)
print(cleaned_specific)

# Điền các NA bằng giá trị trước/sau đó trong cùng cột
cleaned_forward=data.fillna(method='ffill')
cleaned_backward=data.fillna(method='bfill')
print(cleaned_forward)
print(cleaned_backward)
