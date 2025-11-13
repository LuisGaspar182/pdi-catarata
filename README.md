# 📘 Projeto de Processamento Digital de Imagens – Detecção e Análise de Catarata

Este repositório contém um pipeline completo para pré-processamento, extração de frames, detecção, segmentação e análise de vídeos de cirurgia ocular, com foco na identificação e estudo de cataratas.  
O projeto foi construído para rodar em **Ubuntu 20.04+**, utilizando **Python**, **OpenCV** e **PyTorch (CPU)**.

---

## 🧱 Estrutura do Projeto

```
pdi-catarata/
│
├── data/
│   ├── raw_videos/          # Coloque aqui os vídeos originais
│   ├── preprocessed/        # Frames extraídos automaticamente
│   └── annotations/         # Máscaras (criação opcional)
│
├── notebooks/               # Notebooks exploratórios
│
├── src/
│   ├── preprocessing.py     # Extrai frames e padroniza vídeos
│   ├── detection.py         # Detecta estruturas (a ser implementado)
│   ├── tracking.py          # Rastreia estruturas (a ser implementado)
│   └── metrics.py           # Calcula métricas (a ser implementado)
│
├── models/                  # Modelos treinados (opcional)
│
├── results/                 # Resultados gerados automaticamente
│
├── requirements.txt
└── README.md
```

---

## 🚀 Como instalar e rodar o projeto

### 1️⃣ Requisitos

- Ubuntu 20.04+
- Python 3.8+
- FFmpeg instalado
- Virtualenv (recomendado)

### 2️⃣ Crie e ative o ambiente virtual

```bash
python3 -m venv pdi_env
source pdi_env/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🎬 Como usar

### ▶️ 1. Coloque seus vídeos na pasta:

```
data/raw_videos/
```

Aceita arquivos `.mp4`, `.avi`, `.mov`, etc.

---

### ▶️ 2. Execute o pré-processamento

Ele cria uma pasta de frames para cada vídeo automaticamente.

```bash
python src/preprocessing.py
```

Resultado esperado:

```
data/preprocessed/NOME_DO_VIDEO/
    frame_000001.png
    frame_000002.png
    ...
```

---

### ▶️ 3. Utilize os notebooks

Os notebooks dentro da pasta `notebooks/` permitem:

- Visualizar os frames
- Testar detecção
- Rodar segmentação
- Avaliar métricas

Exemplo:

```bash
jupyter lab
```

---

## 🧪 Scripts do pipeline

### 📌 `preprocessing.py`

- Extrai frames dos vídeos
- Padroniza FPS
- Organiza frames por pasta
- Mantém os vídeos originais intactos

### 📌 `detection.py` _(a definir)_

- Será responsável por detectar estruturas oculares
- Pode usar OpenCV ou modelos leves em PyTorch

### 📌 `tracking.py` _(a definir)_

- Acompanha estruturas ao longo do tempo
- Exemplo: dilatação da pupila, movimentação da lente, etc.

### 📌 `metrics.py` _(a definir)_

- Calcula métricas para avaliação quantitativa
- Ex: acurácia, IoU, distância, área, etc.

---

## 🛠 Tecnologias usadas

- **Python 3.8**
- **OpenCV**
- **PyTorch CPU**
- **Scikit-Image**
- **FFmpeg**
- **JupyterLab**

---

## 📄 Licença

Este projeto pode utilizar uma licença à sua escolha (MIT, GPL, etc.).  
Se quiser, posso gerar uma licença para você.
