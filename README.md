# GoogleCloudFunctionTemplate

Simple template for Google Cloud Function projects



## Usage
* Clone the repo
* Add environment variable files
  * Add **.env** - for local environment variables
  * Add **.production-env.yaml** - for production environment variables
  * Add **.staging-env.yaml** - for staging environment variables
* Add your changes to the **main.py** file 
* Update the **main_tests.py** file to test your function
* Deploy your function
  * Update the **deploy-production.sh** for production deployment
  * Update the **deploy-staging.sh** for staging deployment
  * Run **./deploy-production.sh** or **./deploy-staging.sh** for production and staging deployments respectively.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the main function and tests as appropriate.

Happy Hacking!

## License
[MIT](https://choosealicense.com/licenses/mit/)