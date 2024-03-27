#!/bin/bash

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL
URL=$1

# Send a request to the URL and store the response body in a temporary file
response=$(curl -s -w "%{size_download}" -o /tmp/response_body "$URL")

# Check if curl was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to fetch URL $URL"
    exit 1
fi

# Display the size of the response body
echo "Size of the response body: $response bytes"

# Clean up temporary file
rm -f /tmp/response_body
