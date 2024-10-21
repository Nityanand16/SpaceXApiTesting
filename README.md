##The following scenarios are tested:

1. Status Code Validation: Ensure the API returns a 200 status code for the latest launch request.
2. Response Data Structure: Validate that the response contains the required fields: name, date_utc, rocket, and success.
3. Data Types and Format Validation: Ensure that the data types of the fields match expected types:
          name: string
          date_utc: ISO 8601 formatted string
          rocket: string
          success: boolean
