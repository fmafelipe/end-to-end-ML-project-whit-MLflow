# Wine Quality Prediction: An End-to-End MLOps Solution

Este proyecto implementa un modelo de Machine Learning para predecir la calidad del vino, integrando un ciclo de vida completo de MLOps. La solución abarca desde la validación de datos y el entrenamiento de modelos hasta el despliegue de una web app interactiva para inferencia en tiempo real.

## 🌟 Características Principales
- **Arquitectura Modular:** Código organizado en componentes (ingesta, validación, transformación, entrenamiento y evaluación) para máxima mantenibilidad.
- **MLflow Tracking:** Gestión de experimentos, registro de métricas y versionado de modelos integrados con DagsHub.
- **Pipeline de Inferencia:** Pipeline dedicado para procesar datos de entrada y generar predicciones consistentes.
- **Interfaz Web:** Aplicación Flask para facilitar la interacción del usuario con el modelo.
- **Preparado para Producción:** Incluye configuración de Docker y flujos de CI/CD para despliegues automatizados.
- **Despliegue en Render:** Despliegue automático de la web app en Render.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.11.9.
- **Machine Learning:** Scikit-Learn (ElasticNet), Pandas, NumPy.
- **MLOps:** MLflow, DagsHub.
- **Web Framework:** Flask.
- **DevOps:** Docker, GitHub Actions.
- **Despliegue:** Render.

## 🏗️ Arquitectura del Proyecto
El flujo de trabajo sigue una estructura de etapas claramente definidas:
1. **Configuración:** Definición de esquemas de datos (`schema.yaml`) e hiperparámetros (`params.yaml`).
2. **Data Validation:** Verificación automatizada de tipos y presencia de columnas antes del procesamiento.
3. **Model Training:** Entrenamiento de un regresor ElasticNet con seguimiento de parámetros.
4. **Deployment:** Exposición del modelo a través de la web app.

## 📊 Seguimiento con MLflow y DagsHub
El proyecto está configurado para registrar automáticamente todos los experimentos en DagsHub. Para visualizar los resultados: https://dagshub.com/fmafelipe/end-to-end-ML-project-whit-MLflow

## 📦 Despliegue en Render
El despliegue de la web app se realiza automáticamente a través de GitHub Actions. Para ingresar a la web app para la inferencia: https://end-to-end-ml-project-8dho.onrender.com
