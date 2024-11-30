# PotterShop API

To run this API, you need to create a `.env` file in the root directory of the api directory. This file should contain the following environment variables:

```
API_KEY=your_api_key_here
API_URL='http://localhost:8080/api'
PROJECT_PATH=your_project_path_here
```

## API_KEY Generation

To generate an `API_KEY`, go to the admin panel, navigate to `Advanced Settings -> API`, and click `"Add New API Key"`.

## API_KEY Permissions

The `API_KEY` should have permissions to access the following resources:

- categories
- images
- product_options
- products
- stock_availables
- stock_movement_reasons
- stock_movements
- stocks
