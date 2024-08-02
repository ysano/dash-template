# Dash Application Template

This is a template for creating Dash applications with a development container configuration, optimized for use with VS Code.

## Features

- Python 3.12 environment
- Dash framework for building analytical web applications
- Development container configuration for VS Code
- Git integration with pre-configured extensions
- BigQuery integration with secure credential management
- Customized VS Code settings and extensions

## Project Structure

```
project-root/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── layout.py
│   ├── callbacks.py
│   └── utils.py
│
├── assets/
│   ├── custom.css
│   └── favicon.ico
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── credentials/
│   └── .gitkeep
│
├── data/
│   └── .gitkeep
│
├── tests/
│   ├── __init__.py
│   ├── test_layout.py
│   └── test_callbacks.py
│
├── .vscode/
│   └── settings.json
│
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Getting Started

1. Use this template to create a new repository
2. Clone your new repository
3. Ensure you have Docker and VS Code with the Remote - Containers extension installed
4. Open the project folder in VS Code
5. When prompted, click "Reopen in Container" or run the "Remote-Containers: Reopen in Container" command
6. Wait for the container to build and initialize (this may take a few minutes the first time)

## Credential Management

For secure credential management:

1. Create a Google Cloud service account key file (JSON)
2. Place the key file in the `credentials` folder
3. Rename the key file to `bigquery-credentials.json`
4. The `credentials` folder is included in `.gitignore` to prevent accidental commits
5. Copy the `.env.example` file to `.env` and update the values:
   - Set `GCP_PROJECT` to your Google Cloud project ID
   - Set `GOOGLE_APPLICATION_CREDENTIALS` to the path of your credentials file (e.g., `/workspace/credentials/bigquery-credentials.json`)

### .env File

The project includes a `.env.example` file with the following content:

```
GCP_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/workspace/credentials/your-credentials-file.json
```

Copy this file to `.env` and replace the placeholder values with your actual Google Cloud project ID and the path to your credentials file. The `.env` file is included in `.gitignore` to prevent sensitive information from being committed to the repository.

### Creating a Service Account for BigQuery Access

To set up a service account for BigQuery access:

1. Go to the Google Cloud Console (https://console.cloud.google.com/)
2. Select your project
3. Navigate to "IAM & Admin" > "Service Accounts"
4. Click "Create Service Account"
5. Enter a name for the service account (e.g., "bigquery-dash-app")
6. Click "Create and Continue"
7. Assign the following roles to the service account:
   - BigQuery Data Viewer
   - BigQuery Job User
   - BigQuery Read Session User (for BigQuery Storage API access)
8. Click "Continue" and then "Done"
9. Find the newly created service account in the list and click on it
10. Go to the "Keys" tab
11. Click "Add Key" > "Create new key"
12. Choose JSON as the key type and click "Create"
13. Save the downloaded JSON file in the `credentials` folder of your project and rename it to `bigquery-credentials.json`

### Required Permissions and APIs

The service account should have the following permissions:

- `bigquery.jobs.create`: Allows the application to run BigQuery jobs
- `bigquery.tables.getData`: Allows reading data from BigQuery tables
- `bigquery.jobs.list`: Allows listing and monitoring of BigQuery jobs
- `bigquery.readsessions.create`: Allows creation of read sessions for the BigQuery Storage API
- `bigquery.readsessions.getData`: Allows reading data using the BigQuery Storage API

These permissions are typically included in the "BigQuery Data Viewer", "BigQuery Job User", and "BigQuery Read Session User" roles assigned earlier.

Additionally, you need to enable the BigQuery Storage API for your project:

1. Go to the Google Cloud Console
2. Navigate to "APIs & Services" > "Dashboard"
3. Click on "+ ENABLE APIS AND SERVICES"
4. Search for "BigQuery Storage API"
5. Click on it and then click "ENABLE"

Using the BigQuery Storage API can significantly improve performance for large data transfers from BigQuery to your application. It's especially useful when working with large datasets or when you need to stream data efficiently.

## Customization

- Modify files in the `app/` directory to build your Dash application
- Update `requirements.txt` to add new dependencies
- Adjust VS Code settings in `.vscode/settings.json`
- Modify the development container configuration in `.devcontainer/devcontainer.json` as needed

## Development

- The main application code is in the `app/` directory
- `run.py` is the entry point for running the application
- Use the integrated terminal in VS Code to run commands inside the container

To run the application:

```bash
python run.py
```

## Testing

Tests are located in the `tests/` directory. To run tests:

```bash
pytest
```

## Deployment

This template includes a Dockerfile for easy deployment. You can use it to build and run your application in various cloud environments. For production deployments, ensure you use appropriate secret management services like Google Cloud Secret Manager.

## VS Code Extensions

The following extensions are automatically installed in the development container:

- Python
- Pylance
- Pylint
- Black Formatter
- Docker
- AutoDocstring
- GitLens
- Git History
- Git Graph

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.