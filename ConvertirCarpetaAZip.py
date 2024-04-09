import zipfile
import os
import sys

def comprimir_carpeta(carpeta_a_comprimir):
    # Obtener el nombre base de la carpeta
    nombre_carpeta = os.path.basename(carpeta_a_comprimir)
    nombre_archivo_zip = f'{nombre_carpeta}.zip'

    # Crear un objeto ZipFile en modo escritura
    with zipfile.ZipFile(nombre_archivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Recorrer recursivamente la carpeta y agregar cada archivo/directorio al archivo ZIP
        for raiz, directorios, archivos in os.walk(carpeta_a_comprimir):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                # Agregar archivo al archivo ZIP usando ruta relativa
                zipf.write(ruta_completa, os.path.relpath(ruta_completa, carpeta_a_comprimir))

    print(f'Carpeta "{carpeta_a_comprimir}" comprimida correctamente como "{nombre_archivo_zip}".')

if __name__ == '__main__':
    # Verificar que se proporcionó la ruta de la carpeta como argumento de línea de comandos
    if len(sys.argv) != 2:
        print('Uso: python programa.py "Ruta/de/la/carpeta"')
        sys.exit(1)

    # Obtener la ruta de la carpeta desde el argumento de línea de comandos
    ruta_carpeta = sys.argv[1]

    # Verificar si la ruta es válida
    if not os.path.isdir(ruta_carpeta):
        print(f'Error: La ruta "{ruta_carpeta}" no es una carpeta válida.')
        sys.exit(1)

    # Comprimir la carpeta especificada
    comprimir_carpeta(ruta_carpeta)
