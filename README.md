# 🏦 IntelliLoan – AI-Driven Loan Approval Prediction System 

A deployed machine learning web app that predicts whether a loan will be approved, using applicant details like income, credit history, and loan amount. Built with **XGBoost** for accuracy and **Streamlit** for an intuitive user interface.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-0B9EDC?logo=python&logoColor=white)

---

## 🔗 Live App

**👉 [Launch App on Streamlit](https://loan-approval-predictor-dwxrcjeftxvtj2yunu9nxx.streamlit.app/)**  
*Interact with the model directly via this public link.*

---

## 💡 Features

- Takes user input via a clean web form
- Predicts loan approval status with a confidence score
- Uses a trained **XGBoost** model for realistic performance
- Works end-to-end: from model training → deployment

---

## 🚀 Tech Stack

| Layer     | Technology           |
|-----------|----------------------|
| Frontend  | Streamlit            |
| Backend   | XGBoost, Scikit-learn|
| Data      | Pandas               |
| Deployment| Streamlit Cloud      |

---

## 🧾 Project Structure
loan-approval-predictor/
├── app/ # Streamlit frontend
│ └── app.py
├── model/ # Saved model
│ └── loan_approval_model.pkl
├── data/ # Training dataset
├── notebooks/ # EDA & Model development
├── requirements.txt
└── README.md

---

## 📈 Usage

To run locally:

```bash
git clone https://github.com/JayJ1504/loan-approval-predictor.git
cd loan-approval-predictor
pip install -r requirements.txt
streamlit run app/app.py

🧠 Author
Jay Jahagirdar

✅ Contributions and feedback are welcome!


