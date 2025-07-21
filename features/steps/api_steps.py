import requests
from behave import *

@given('the JSONPlaceholder API is available')
def given_jsonplaceholder_api_available(context):
    """Check if the JSONPlaceholder API is available"""
    response = requests.get(f"{context.base_url}/posts/1", timeout=context.timeout)
    assert response.status_code == 200, f"API not available. Status: {response.status_code}"

@when('I send a {method} request to "{path}"')
def when_send_request(context, method, path):
    url = f"{context.base_url}{path}"
    if method == "GET":
        context.response = requests.get(url, timeout=context.timeout)
    elif method == "POST":
        context.response = requests.post(
            url, data=context.text, headers=context.default_headers, timeout=context.timeout
        )

@when('I send a POST request to "{path}" with body')
def when_send_post_request_with_body(context, path):
    url = f"{context.base_url}{path}"
    context.response = requests.post(
        url, data=context.text, headers=context.default_headers, timeout=context.timeout
    )

@then('the response status code should be {status_code:d}')
def then_response_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the response body should be a JSON array')
def then_response_body_json_array(context):
    json_data = context.response.json()
    assert isinstance(json_data, list), "Response body is not a JSON array"

@then('the response body should contain "{key}"')
def then_response_body_contains_key(context, key):
    json_data = context.response.json()
    assert key in json_data, f"Response body does not contain key: {key}"

@then('the response body should have "{key}" with value "{value}"')
def then_response_body_contains_key_with_value(context, key, value):
    json_data = context.response.json()
    actual_value = json_data[key]
    # Convert to same type for comparison
    expected_value = int(value) if value.isdigit() else value
    assert actual_value == expected_value, f"Expected {key}={expected_value}, got {actual_value}"

@then('the response should contain posts data')
def then_response_contains_posts_data(context):
    json_data = context.response.json()
    assert isinstance(json_data, list) and len(json_data) > 0, "Expected non-empty array"
    # Check first post has required fields
    first_post = json_data[0]
    required_fields = ['id', 'title', 'body', 'userId']
    for field in required_fields:
        assert field in first_post, f"Missing field: {field}"