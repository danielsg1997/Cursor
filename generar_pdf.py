"""
Ejemplo de Generación de PDF con Gráficos y Texto

Este módulo demuestra cómo crear un PDF que contiene tanto texto como gráficos
usando matplotlib con PdfPages. También se muestra un ejemplo alternativo con ReportLab.

Métodos disponibles:
    1. matplotlib.backends.backend_pdf.PdfPages - Simple y directo
    2. reportlab - Más control sobre diseño y formato
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np


def generar_pdf_con_matplotlib(nombre_archivo="reporte.pdf"):
    """
    Genera un PDF con múltiples páginas que incluyen texto y gráficos usando matplotlib.
    
    Args:
        nombre_archivo (str): Nombre del archivo PDF a generar
    """
    # Leer datos (si existe el archivo)
    try:
        datos = pd.read_csv("datos_numericos.csv")
        tiene_datos = True
    except FileNotFoundError:
        # Generar datos de ejemplo si no existe el archivo
        datos = pd.DataFrame({
            'columna_1': np.random.normal(100, 15, 100),
            'columna_2': np.random.normal(50, 10, 100)
        })
        tiene_datos = False
    
    # Crear el PDF
    with PdfPages(nombre_archivo) as pdf:
        # Página 1: Portada con texto
        fig = plt.figure(figsize=(8.5, 11))  # Tamaño carta
        fig.text(0.5, 0.5, 'REPORTE DE ANÁLISIS DE DATOS\n\n'
                          'Generado con Python y Matplotlib',
                ha='center', va='center', fontsize=20, fontweight='bold')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # Página 2: Estadísticas descriptivas como texto
        fig = plt.figure(figsize=(8.5, 11))
        fig.text(0.1, 0.9, 'ESTADÍSTICAS DESCRIPTIVAS', 
                fontsize=16, fontweight='bold')
        
        texto_estadisticas = f"""
COLUMNA 1:
  Media: {datos['columna_1'].mean():.2f}
  Mediana: {datos['columna_1'].median():.2f}
  Desviación Estándar: {datos['columna_1'].std():.2f}
  Mínimo: {datos['columna_1'].min():.2f}
  Máximo: {datos['columna_1'].max():.2f}

COLUMNA 2:
  Media: {datos['columna_2'].mean():.2f}
  Mediana: {datos['columna_2'].median():.2f}
  Desviación Estándar: {datos['columna_2'].std():.2f}
  Mínimo: {datos['columna_2'].min():.2f}
  Máximo: {datos['columna_2'].max():.2f}
        """
        
        fig.text(0.1, 0.7, texto_estadisticas, fontsize=12, 
                verticalalignment='top', family='monospace')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # Página 3: Gráfico de dispersión
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.scatter(datos['columna_1'], datos['columna_2'], alpha=0.6)
        ax.set_xlabel('Columna 1', fontsize=12)
        ax.set_ylabel('Columna 2', fontsize=12)
        ax.set_title('Gráfico de Dispersión: Columna 1 vs Columna 2', 
                    fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # Página 4: Histogramas
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 11))
        
        ax1.hist(datos['columna_1'], bins=20, edgecolor='black', alpha=0.7)
        ax1.set_title('Histograma de Columna 1', fontsize=12, fontweight='bold')
        ax1.set_xlabel('Valores')
        ax1.set_ylabel('Frecuencia')
        ax1.grid(True, alpha=0.3)
        
        ax2.hist(datos['columna_2'], bins=20, edgecolor='black', alpha=0.7, color='orange')
        ax2.set_title('Histograma de Columna 2', fontsize=12, fontweight='bold')
        ax2.set_xlabel('Valores')
        ax2.set_ylabel('Frecuencia')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # Añadir metadatos al PDF
        d = pdf.infodict()
        d['Title'] = 'Reporte de Análisis de Datos'
        d['Author'] = 'Python Script'
        d['Subject'] = 'Análisis Estadístico'
        d['Keywords'] = 'datos, estadísticas, gráficos'
    
    print(f"PDF generado exitosamente: {nombre_archivo}")


def generar_pdf_con_reportlab(nombre_archivo="reporte_reportlab.pdf"):
    """
    Genera un PDF usando ReportLab (requiere instalación: pip install reportlab).
    Ofrece más control sobre el diseño y formato.
    
    Args:
        nombre_archivo (str): Nombre del archivo PDF a generar
    """
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.pdfgen import canvas
        import matplotlib.pyplot as plt
        import io
        
        # Leer datos
        try:
            datos = pd.read_csv("datos_numericos.csv")
        except FileNotFoundError:
            datos = pd.DataFrame({
                'columna_1': np.random.normal(100, 15, 100),
                'columna_2': np.random.normal(50, 10, 100)
            })
        
        # Crear el documento PDF
        doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Título
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=30,
            alignment=TA_CENTER
        )
        story.append(Paragraph("REPORTE DE ANÁLISIS DE DATOS", title_style))
        story.append(Spacer(1, 0.5*inch))
        
        # Estadísticas
        story.append(Paragraph("Estadísticas Descriptivas", styles['Heading2']))
        story.append(Spacer(1, 0.2*inch))
        
        stats_text = f"""
        <b>Columna 1:</b><br/>
        Media: {datos['columna_1'].mean():.2f}<br/>
        Mediana: {datos['columna_1'].median():.2f}<br/>
        Desviación Estándar: {datos['columna_1'].std():.2f}<br/><br/>
        
        <b>Columna 2:</b><br/>
        Media: {datos['columna_2'].mean():.2f}<br/>
        Mediana: {datos['columna_2'].median():.2f}<br/>
        Desviación Estándar: {datos['columna_2'].std():.2f}
        """
        story.append(Paragraph(stats_text, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Crear gráfico temporal
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(datos['columna_1'], datos['columna_2'], alpha=0.6)
        ax.set_xlabel('Columna 1')
        ax.set_ylabel('Columna 2')
        ax.set_title('Gráfico de Dispersión')
        ax.grid(True, alpha=0.3)
        
        # Guardar gráfico en buffer
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
        img_buffer.seek(0)
        plt.close()
        
        # Añadir gráfico al PDF
        story.append(Paragraph("Gráfico de Dispersión", styles['Heading2']))
        story.append(Spacer(1, 0.2*inch))
        img = Image(img_buffer, width=6*inch, height=4*inch)
        story.append(img)
        
        # Construir el PDF
        doc.build(story)
        print(f"PDF generado exitosamente con ReportLab: {nombre_archivo}")
        
    except ImportError:
        print("ReportLab no está instalado. Instálalo con: pip install reportlab")
        print("Usando método matplotlib en su lugar...")
        generar_pdf_con_matplotlib(nombre_archivo)


if __name__ == "__main__":
    # Generar PDF con matplotlib (método más simple)
    print("Generando PDF con matplotlib...")
    generar_pdf_con_matplotlib("reporte_matplotlib.pdf")
    
    # Generar PDF con ReportLab (método más avanzado)
    print("\nGenerando PDF con ReportLab...")
    generar_pdf_con_reportlab("reporte_reportlab.pdf")
