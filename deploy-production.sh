#!/bin/bash
FUNCTION_NAME=someName
PYTHON_VERSION=python38
REGION=us-east4

cp -f .env .production-env.yaml
sed -r -i 's/\s+//g' .production-env.yaml
sed -i -e 's/="/: /g' .production-env.yaml
sed -i -e 's/"//g' .production-env.yaml
pytest
test_result=$?
if [ $test_result == 0 ]
then
   gcloud functions deploy $FUNCTION_NAME --env-vars-file .production-env.yaml --entry-point main --runtime $PYTHON_VERSION --trigger-http --allow-unauthenticated --region $REGION
else
   echo "Failed Test ${test_result}"
fi