#!/bin/bash
curl -X POST http://localhost:5000/api/add_labeled_data \
-H "Content-Type: application/json" \
-d '{
    "sentence_id": 1,
    "isBias": true,
    "isMalice": false,
    "updateAt": "2023-01-01T00:00:00",
    "visitAt": "2023-01-02T00:00:00"
}'
