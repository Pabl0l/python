import sys
import pyperclip
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QScrollArea, QCheckBox, QPushButton,
    QMessageBox, QFrame
)
from PyQt6.QtCore import Qt


# Diccionario con los criterios y sus mensajes detallados
criterios = {
    "Presentación Formal": (
        "El documento debe cumplir estrictamente con las normas APA 7ma edición en todos sus aspectos formales."
    ),
    "Formato de página": (
        "Márgenes: 2.54 cm (1 pulgada) en todos los lados, papel tamaño carta, texto alineado a la izquierda "
        "con margen izquierdo de 4cm para encuadernación, fuente Times New Roman 12 pts o Arial 11 pts, doble espacio."
    ),
    "Portada": (
        "Debe incluir: título del trabajo, nombre del autor, afiliación institucional, curso, nombre del profesor, "
        "y fecha en formato día mes año (ej: 15 de noviembre de 2024). Todos centrados en la página."
    ),
    "Encabezado y numeración": (
        "Encabezado de página con título abreviado en mayúsculas alineado a la izquierda y número de página "
        "alineado a la derecha. Numeración consecutiva desde la portada."
    ),
    "Títulos y encabezados": (
        "Niveles de encabezado correctamente aplicados:\n"
        "Nivel 1: Centrado en negrita, mayúsculas y minúsculas\n"
        "Nivel 2: Alineado a la izquierda en negrita, mayúsculas y minúsculas\n"
        "Nivel 3: Sangría, negrita, punto final, texto continuo en la misma línea"
    ),
    "Citas textuales": (
        "Citas menores de 40 palabras entre comillas dentro del párrafo.\n"
        "Citas de 40+ palabras en bloque sangrado, sin comillas, con referencia al final entre paréntesis."
    ),
    "Referencias bibliográficas": (
        "Lista de referencias en página separada, orden alfabético, sangría francesa, "
        "formato específico según tipo de fuente (libros, artículos, web, etc.)."
    ),
    "Citas y paráfrasis": (
        "Todas las ideas externas deben citarse adecuadamente con autor y año.\n"
        "Sistema autor-fecha correctamente aplicado tanto en citas directas como indirectas."
    ),
    "Tablas y figuras": (
        "Tablas numeradas consecutivamente con título arriba, figuras con leyenda abajo.\n"
        "Todas las imágenes deben estar alineadas al centro, con calidad adecuada y referencia en el texto."
    ),
    "Abreviaturas y siglas": (
        "La primera vez que se usen, escribir completo seguido de la abreviatura entre paréntesis.\n"
        "Posteriormente usar solo la abreviatura."
    ),
    "Puntuación y espacios": (
        "Un espacio después de cada signo de puntuación.\n"
        "Sin espacio antes de dos puntos, punto y coma, o comas."
    ),
    "Uso de mayúsculas y negritas": (
        "Solo usar negritas en títulos y etiquetas de figuras/tablas.\n"
        "Evitar uso excesivo de mayúsculas, solo donde corresponda según APA."
    ),
    "Imágenes bien alineadas": (
        "Todas las imágenes deben estar alineadas al centro en un buen formato, "
        "manteniendo la coherencia estética del documento según normas APA."
    ),
    "Margen de 4 cm a la izquierda": (
        "El texto debe tener un margen de 4cm a la izquierda para que pueda imprimirse correctamente, "
        "manteniendo los 2.54 cm en los demás lados según adaptación para encuadernación."
    )
}


class CorreoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📧 Generador de Correcciones")
        self.setMinimumSize(650, 800)

        # Layout principal
        layout = QVBoxLayout()

        # Título
        titulo = QLabel("Generador de Correcciones")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(`
            font-size: 22px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        `)
        layout.addWidget(titulo)

        # Instrucciones
        instrucciones = QLabel(
            "Ingresa el nombre del estudiante, tu nombre, comentarios adicionales y selecciona los criterios:"
        )
        instrucciones.setWordWrap(True)
        instrucciones.setStyleSheet("color: #555; font-size: 14px;")
        layout.addWidget(instrucciones)

        # Campo de texto para el nombre del estudiante
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre del estudiante")
        self.nombre_input.setStyleSheet(`
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                outline: none;
            }
        `)
        layout.addWidget(self.nombre_input)

        # Campo de texto para el nombre del firmante
        self.firmante_input = QLineEdit()
        self.firmante_input.setPlaceholderText("Tu nombre (firmante)")
        self.firmante_input.setStyleSheet(`
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
            }
            QLineEdit:focus {
                border: 2px solid #2ecc71;
                outline: none;
            }
        `)
        layout.addWidget(self.firmante_input)

        # Campo para comentarios adicionales
        self.comentarios_input = QLineEdit()
        self.comentarios_input.setPlaceholderText("Comentarios adicionales (opcional)")
        self.comentarios_input.setStyleSheet(`
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
            }
            QLineEdit:focus {
                border: 2px solid #9b59b6;
                outline: none;
            }
        `)
        layout.addWidget(self.comentarios_input)

        # Área con scroll para criterios
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        self.checkboxes = {}
        for criterio in criterios:
            checkbox = QCheckBox(criterio)
            checkbox.setStyleSheet(`
                QCheckBox {
                    font-size: 14px;
                    padding: 4px;
                }
            `)
            scroll_layout.addWidget(checkbox)
            self.checkboxes[criterio] = checkbox

        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)

        # Botón para copiar texto
        copiar_btn = QPushButton("📋 Copiar texto al portapapeles")
        copiar_btn.setStyleSheet(`
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        `)
        copiar_btn.clicked.connect(self.copiar_texto)
        layout.addWidget(copiar_btn)

        # Línea divisoria
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        # Establecer layout principal
        self.setLayout(layout)

    def copiar_texto(self):
        nombre = self.nombre_input.text().strip()
        firmante = self.firmante_input.text().strip()
        comentarios = self.comentarios_input.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error", "Por favor ingresa el nombre del estudiante.")
            return
        if not firmante:
            QMessageBox.warning(self, "Error", "Por favor ingresa tu nombre para la firma.")
            return

        # Obtener criterios seleccionados
        seleccionados = [c for c, cb in self.checkboxes.items() if cb.isChecked()]
        if not seleccionados and not comentarios:
            QMessageBox.warning(self, "Error", "Selecciona al menos un criterio o agrega comentarios.")
            return

        # Generar texto del correo
        texto = f"Hola {nombre},\n\nHe revisado tu proyecto de vida y encontré algunos puntos a corregir:\n\n"
        for criterio in seleccionados:
            texto += f"🔹 {criterio}:\n{criterios[criterio]}\n\n"
        if comentarios:
            texto += f"💡 Comentarios adicionales:\n{comentarios}\n\n"
        texto += (
            "Por favor realiza los ajustes y vuelve a enviar el trabajo especificando los cambios que le realizó al documento.\n\n"

            "Te dejo adjunto una plantilla para que te guíes de cómo debería quedar tu documento. \n"
            f"Atentamente,\n{firmante}"
        )

        # Copiar al portapapeles
        pyperclip.copy(texto)

        # Limpiar nombre del estudiante, comentarios y checkboxes; mantener firmante
        self.nombre_input.clear()
        self.comentarios_input.clear()
        for cb in self.checkboxes.values():
            cb.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ventana = CorreoApp()
    ventana.show()
    sys.exit(app.exec())
