# Finn
A trading bot that is trained from a dataset of stocks, bases decision to sell, buy, and/or hold trading decisions. Made with Flask, Next.js, and PostgreSQL.

## Project Structure
Finn/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── config.py
│   ├── requirements.txt
│   ├── run.py
│   └── Dockerfile
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   ├── package.json
│   ├── next.config.js
│   └── Dockerfile
│
├── ml-model/
│   ├── data/
│   ├── notebooks/
│   ├── train.py
│   └── predict.py
│
├── docker-compose.yml
└── README.md
