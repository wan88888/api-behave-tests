def before_all(context):
    """Setup that runs once before all tests"""
    context.base_url = "https://jsonplaceholder.typicode.com"
    context.default_headers = {'Content-Type': 'application/json'}
    context.timeout = 10  # Reduced timeout for faster tests