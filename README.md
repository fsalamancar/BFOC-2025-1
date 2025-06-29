# BFOC-2025-1

**Bioinformatics for Omics Sciences | UNAL 2025**

Este repositorio contiene los talleres prácticos desarrollados durante el curso _Bioinformatics for Omics Sciences_ en la Universidad Nacional de Colombia, 2025.

Los talleres abordan diferentes etapas del análisis de datos ómicos, desde el control de calidad hasta el ensamblaje de novo y por referencia.

---

## 📁 Estructura del repositorio

Taller1_Calidad/ # Evaluación de calidad con FastQC
└── src/ # Scripts y análisis
Taller2_FASTQC/ # Consolidación de calidad con MultiQC
├── data/fastqc/output/ # Resultados de FastQC
└── images/ # Imágenes de reporte
Taller3_Trimming/ # Recorte de secuencias
├── fastp/ # Recorte con Fastp
└── trimmomatic/ # Recorte con Trimmomatic
Taller4_EnsamblajeDeNovo/ # Ensamblaje de novo
├── megahit_out/ # Resultado de MEGAHIT
└── velvet31/ # Resultado de Velvet



---

## 🧪 Talleres cubiertos

1. **Taller 1 – Calidad de Lecturas**
   - Evaluación con FastQC
   - Análisis de per base quality, GC content, duplications, etc.

2. **Taller 2 – MultiQC**
   - Agregación de reportes de calidad
   - Comparación entre múltiples archivos FastQC

3. **Taller 3 – Recorte de Lecturas**
   - Uso de Fastp y Trimmomatic
   - Parámetros de trimming: sliding window, quality threshold, length

4. **Taller 4 – Ensamblaje de novo**
   - Ensamblaje con MEGAHIT y Velvet
   - Comparación de métricas de contigs generados

---

## 📌 Requisitos

- Python 3.x
- FastQC
- MultiQC
- fastp
- Trimmomatic
- MEGAHIT
- Velvet

---

## 📘 Notas

Este repositorio tiene fines académicos y documenta el proceso de análisis paso a paso. Los datos utilizados son ejemplos para prácticas de laboratorio.

---

## 👤 Autor

Francisco Salamanca  
Estudiante de Maestría en Bioinformática – UNAL  
[GitHub: fsalamancar](https://github.com/fsalamancar)
