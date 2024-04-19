import cv2
import numpy as np

def draw_lines(img, lines, color):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, 3)
    return img

image_path = 'Test_Before-model_2.png'  # 更換成您的圖像路徑
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用Canny邊緣檢測器
edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

# 使用霍夫線變換檢測直線
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)

# 分類直線為實牆（交叉直線）或落地窗（平行直線）
# 這裡需要一個聰明的算法來做這個分類，我們暫時使用一個簡單的方法：
# 如果直線幾乎平行於某個軸，我們假設它是落地窗的一部分
wall_lines = []
window_lines = []
for line in lines:
    for x1, y1, x2, y2 in line:
        if abs(x2 - x1) > abs(y2 - y1):  # 水平線
            wall_lines.append([[x1, y1, x2, y2]])
        else:  # 垂直線
            window_lines.append([[x1, y1, x2, y2]])

# 繪製實牆線條
wall_image = draw_lines(np.copy(image), wall_lines, (255, 0, 0))  # 藍色

# 繪製落地窗線條
window_image = draw_lines(np.copy(image), window_lines, (0, 255, 0))  # 綠色

# 組合兩種線條
combo_image = cv2.addWeighted(wall_image, 0.5, window_image, 0.5, 0)

# 顯示結果
cv2.imshow('Result', combo_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 可以保存結果
cv2.imwrite('classified_lines.png', combo_image)
