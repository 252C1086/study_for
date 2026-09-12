import pandas as pd
import numpy as np

data = {
    "名前": ["佐藤さん", "鈴木さん", "高橋さん"],
    "身長": [175.0, 161.8, 165.4] 
}

df = pd.DataFrame(data)
print(df)