import cv2
import numpy as np

count =0
# Görüntüyü yükle
image_path = 'deneme5.jpg'
image = cv2.imread(image_path)

x = 100  # Başlangıç x koordinatı
y = 50  # Başlangıç y koordinatı
width = 400  # Kırpma genişliği
height = 400  # Kırpma yüksekliği

# Görüntüyü kırp
cropped_image = image[y:y+height, x:x+width]
#cv2.imshow("croppede",cropped_image)

denoised = cv2.medianBlur(image, 21)

# Görüntüyü gri tonlamaya dönüştür
gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

_, thresholded = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

edges = cv2.Canny(gray, threshold1=20, threshold2=70)

# Görüntüdeki yuvarlakları tespit et
circles = cv2.HoughCircles(
    edges,
    cv2.HOUGH_GRADIENT,
    dp=1, minDist=80, param1=50, param2=10, minRadius=15, maxRadius=30
)

# Tespit edilen yuvarlakları çiz
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        
        # Yuvarlağı çiz
        cv2.circle(image, center, radius, (0, 255, 0), 2)
        
        # Merkezi çiz
        cv2.circle(image, center, 2, (0, 0, 255), 3)
        count +=1



font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  
font_thickness = 2


cv2.putText(image, str(count), (50, 50), font, font_scale, font_color, font_thickness)


cv2.imshow('Circle Detection', image)
#cv2.imshow("threshold image", thresholded)

cv2.waitKey(0)
cv2.destroyAllWindows()
