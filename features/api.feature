Feature: JSONPlaceholder API Testing

  Scenario: Retrieve all posts
    Given the JSONPlaceholder API is available
    When I send a GET request to "/posts"
    Then the response status code should be 200
    And the response body should be a JSON array
    And the response should contain posts data

  Scenario: Retrieve a specific user
    Given the JSONPlaceholder API is available
    When I send a GET request to "/users/1"
    Then the response status code should be 200
    And the response body should have "id" with value "1"
    And the response body should contain "name"
    And the response body should contain "email"

  Scenario: Create a new post
    Given the JSONPlaceholder API is available
    When I send a POST request to "/posts" with body
      """
      {
        "title": "Test Post",
        "body": "This is a test post content",
        "userId": 1
      }
      """
    Then the response status code should be 201
    And the response body should contain "id"
    And the response body should have "title" with value "Test Post"
    And the response body should have "userId" with value "1"