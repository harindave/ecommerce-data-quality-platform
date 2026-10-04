ecommerce-data-quality-platform/
├── README.md              # problem, architecture, how to run, results
├── LICENSE                # MIT is fine for a portfolio project
├── requirements.txt       # pandas, numpy, faker, pyyaml, pytest, sqlalchemy
├── .gitignore             # data/raw, data/olist_clean, venv/
├── config/
│   └── generator.yaml     # row counts, seed, defect rates
├── data/
│   ├── olist_clean/       # Olist as downloaded — never edit (gitignored, keep a small sample committed)
│   └── raw/                # defective copy + defect_log.csv (gitignored)
├── data_generator/
│   ├── profiler.py         # profiles the Olist data
│   ├── generate.py         # builds returns, shipments, new orders, SCD history
│   └── inject_defects.py   # injects + logs defects
├── sql/
│   └── ...                 # added in the SQL phase
├── tests/
│   └── ...                 # pytest added in a later phase
└── docs/
    ├── schema.md
    ├── olist_profile.md
    ├── defect_catalog.md
    ├── business_rules.md
    └── progress_log.md