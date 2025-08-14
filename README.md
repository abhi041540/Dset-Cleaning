# 🧠 Dset-Cleaning — Smart Dataset Preprocessing for Ml

[🚀 Live App](https://dset-cleaning.streamlit.app/) • [📁 GitHub Repository](https://github.com/abhi041540/Dset-Cleaning)

**Dset-Cleaning** is an intelligent, one-click solution for cleaning datasets before training machine learning models. Designed for both regression and classification tasks, it automates the most critical preprocessing steps to ensure minimal data loss and maximum usability.

---

## ✨ What It Does

- 🧼 **Null Value Handling**
  - Automatically detects and removes or replaces missing values
  - Smart thresholding: removes low-impact nulls, replaces high-impact ones

- 📉 **Outlier Detection**
  - Identifies and handles outliers to preserve data integrity

- 🧾 **Column Optimization**
  - Drops columns with excessive nulls or low contribution
  - Retains only meaningful features for supervised learning

- 🎯 **Output Column Detection**
  - Automatically treats the last column as the target variable
  - Supports both regression and classification workflows

---

## 🖼️ Visual Preview

### 📂 Upload & Clean Interface

![Upload Interface](https://res.cloudinary.com/dqjorntxe/image/upload/v1755190341/vuzkx79r6mpjhpqjgcjn.png)

Drag and drop your dataset, then click to clean—no manual coding required.

---

### 📊 Null Value Analysis

![Null Value Handling](https://res.cloudinary.com/dqjorntxe/image/upload/v1755190337/agyspwwaq6qlsewzfrho.png)

Smart logic determines whether to drop or impute missing values based on their impact.

---

### 📈 Outlier Detection & Column Pruning

![Outlier Detection](https://res.cloudinary.com/dqjorntxe/image/upload/v1755190332/ndoyyb7kno8xfm94ie43.png)

Outliers are flagged and handled, while low-value columns are removed to optimize learning.

---

### 🧠 Output Column Recognition

![Output Column](https://res.cloudinary.com/dqjorntxe/image/upload/v1755190328/a51fdjmck3srrlngcihw.png)

The app automatically identifies the output column for supervised learning tasks.

---

## 🛠️ Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Frontend    | Streamlit      |
| Backend     | Python         |
| Core Logic  | Pandas, NumPy  |
| Hosting     | Streamlit Cloud |

---

## 🚀 Getting Started

To run locally:

```bash
# Clone the repository
git clone https://github.com/abhi041540/Dset-Cleaning.git
cd Dset-Cleaning

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
