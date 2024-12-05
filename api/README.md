# PotterShop API

To run this API, you need to create a `.env` file in the root directory of the api directory. This file should contain the following environment variables:

```
API_KEY='your_api_key_here'
API_URL='http://localhost:8080/api'
PROJECT_PATH='your_project_path_here'
```

## Setting up a Virtual Environment

To set up a virtual environment for this project, follow these steps:

1. Navigate to the root directory of the project:
    ```sh
    cd ..
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r api/requirements.txt
    ```

## API_KEY Generation

To generate an `API_KEY`, go to the admin panel, navigate to `Advanced Settings -> API`, and click `"Add New API Key"`.

## API_KEY Permissions

The `API_KEY` should have permissions to access the following resources:

- categories
- images
- products
- stock_availables
