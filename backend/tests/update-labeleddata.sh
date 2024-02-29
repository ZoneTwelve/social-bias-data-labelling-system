#!/bin/bash
curl -X PUT http://localhost:5000/api/labeled_data/<label_id> \
-H "Content-Type: application/json" \
-d '{
    "isBias": false,
    "isMalice": true,
    "updateAt": "2023-01-03T00:00:00",
    "visitAt": "2023-01-04T00:00:00"
}'
