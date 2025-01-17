# Finn
a platform designed to make investing accessible, educational, and personalized for everyone, especially beginners.

The platform combines:

- Simulated Trading for hands-on learning in a risk-free environment.
- Micro-Investing to allow users to start small with real investments.
- AI-Based Financial Planning to provide tailored investment advice and help users grow their wealth responsibly.


## Project Structure
Finn/
├── frontend/             # Frontend (Next.js)
│   ├── components/       # Reusable React components
│   ├── pages/            # Application pages
│   ├── styles/           # CSS/SCSS files or Tailwind configurations
│   ├── utils/            # Frontend utilities (API calls, helpers)
│   ├── public/           # Static files (images, assets)
│   └── package.json      # Frontend dependencies
├── backend/              # Backend (Flask/FastAPI)
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── models/       # Database models (e.g., MongoDB schemas)
│   │   ├── services/     # Business logic (e.g., AI recommendation engine)
│   │   ├── utils/        # Helpers and shared utilities
│   │   ├── config.py     # Configuration settings
│   │   └── main.py       # Backend entry point
│   └── requirements.txt  # Backend dependencies
├── database/             # Database setup and management
│   ├── migrations/       # Database migrations
│   └── seed-data.py      # Script to seed the database with test data
├── tests/                # Test suite
│   ├── frontend/         # Frontend tests (e.g., React Testing Library, Cypress)
│   ├── backend/          # Backend tests (e.g., pytest)
│   └── integration/      # End-to-end tests
├── docs/                 # Documentation
│   ├── README.md         # Project overview
│   ├── API.md            # API documentation
│   └── DESIGN.md         # Architectural and design decisions
├── docker-compose.yml    # Docker for deployment and local testing
├── .env                  # Environment variables
└── README.md             # Main project README
