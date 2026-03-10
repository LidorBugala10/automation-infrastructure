# Automation Infrastructure Framework

A robust, multi-layered automation framework designed for end-to-end testing across **Web**, **Mobile**, and **API** platforms. Built with Python, this framework leverages modern tools to provide scalable and maintainable test suites.

## 🚀 Features

- **Multi-Platform Support**: Unified infrastructure for Web (Playwright), Mobile (Appium), and API (Requests).
- **Page Object Model (POM)**: Clean separation between page elements and test logic.
- **Workflow Layer**: Encapsulated business flows for reusable test steps.
- **Data-Driven Testing (DDT)**: Support for external data sources like CSV and SQL databases.
- **Advanced Reporting**: Integrated with Allure for detailed, visual test execution reports.
- **Configuration Management**: Centralized settings via `config.json`.
- **Custom Extensions**: Wrappers for UI actions and database operations for enhanced stability.

## 🛠️ Tech Stack

*   **Language**: Python 3.10+
*   **Test Runner**: [Pytest](https://docs.pytest.org/)
*   **Web Automation**: [Playwright](https://playwright.dev/python/)
*   **Mobile Automation**: [Appium](http://appium.io/)
*   **API Testing**: [Requests](https://requests.readthedocs.io/)
*   **Reporting**: [Allure Framework](https://docs.qameta.io/allure/)
*   **Assertions**: [Smart Assertions](https://pypi.org/project/smart-assertions/)

## 📁 Project Structure

```text
automation_infrastructure/
├── config/             # Configuration files (config.json)
├── data/               # Test data (API templates, DB, CSV)
├── extensions/          # Custom UI and DB action wrappers
├── page_objects/        # POM classes for Web and Mobile
├── tests/              # Test suites categorized by platform
│   ├── web/
│   ├── api/
│   └── mobile/
├── utils/              # Common utilities and helpers
├── workflows/           # Business logic flows (Web, API, Mobile)
├── conftest.py          # Pytest fixtures and hooks
└── requirements.txt     # Project dependencies
```

## ⚙️ Setup & Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd automation_infrastructure
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Playwright Browsers**:
    ```bash
    playwright install
    ```

## 🏃 Running Tests

### Run all tests:
```bash
pytest
```

### Run specific platform tests:
```bash
pytest tests/web
pytest tests/api
pytest tests/mobile
```

### Run with Allure reporting:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## 📊 Configuration

Modify `config/config.json` to adjust framework behavior:
- `BROWSER_TYPE`: CHROME, FIREFOX, or WEBKIT.
- `HEADLESS`: Toggle UI visibility.
- `SLOW_MO`: Global delay for UI actions.
- `DB_PATH`: Path to the local SQLite database.

## 🛡️ Best Practices

- Use **Workflows** for complex multi-step scenarios.
- Keep **Page Objects** free of assertions; perform assertions in tests or workflows.
- Environment-specific variables should be stored in `.env` (template provided).
