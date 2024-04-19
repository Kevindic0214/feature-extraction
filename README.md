# 特徵提取專案

這個專案展示了如何使用 OpenCV 進行基本的圖像處理和特徵提取。

## 功能描述
- 讀取圖像
- 轉換成灰度圖像
- 使用 Canny 算法進行邊緣檢測
- 使用霍夫線變換檢測圖像中的直線
- 繪製檢測到的線條並展示結果

## 如何使用

1. 確保你的 Python 環境已經安裝了 `opencv-python` 和 `numpy`。
2. 將 `Test_Before-model_2.png` 替換成你自己的圖像文件。
3. 執行 `feature_extraction.py`。

## 範例程式碼

```python
import cv2
import numpy as np

# 讀取圖像
image_path = 'Test_Before-model_2.png'  # 更換成您牆壁圖像的路徑
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny邊緣檢測
edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

# 霍夫線變換
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=5, minLineLength=20, maxLineGap=20)

# 初始化一個新圖像來繪製線條
line_image = np.copy(image) * 0  

# 繪製線條
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 3)

# 合併原始圖像與線條圖像
combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 0) 

# 顯示圖像
cv2.imshow('Feature Extraction', combo_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 可以保存提取的特徵圖像
cv2.imwrite('feature_extraction.png', combo_image)


