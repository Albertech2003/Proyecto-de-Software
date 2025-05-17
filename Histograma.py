import numpy as np
import cv2
import os

print("Creando la matriz...")
# Crear una imagen de 256x256 con un gradiente horizontal
image = np.zeros((256, 256), dtype=np.uint8)
print("Matriz creada.")

print("Asignando valores a las columnas...")
# Asignar valores de 0 a 255 a las columnas
for col in range(256):
    image[:, col] = col
print("Valores asignados.")

print("Guardando la imagen...")
# Guardar la imagen en la ruta actual
output_path = os.path.join(os.getcwd(), 'gradient_image.png')
try:
    success = cv2.imwrite(output_path, image)
    if success:
        print(f"Imagen guardada exitosamente en: {output_path}")
    else:
        print("Error al guardar la imagen.")
except Exception as e:
    print(f"Ocurrió un error al guardar la imagen: {e}")