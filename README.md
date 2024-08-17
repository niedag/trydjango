Learning the Django Web Framework (4.2.6)
- Facebook Pages API integration
- Facebook login authentication
- Twitter Login and API calling
- Twitter posts scraping
- Requests and remote data retrieval
- (Dynamic) URL routing, local SQlite3 database storage and retrieval
- HTML, JavaScript 
- Django templating basics
- Class/Function based views
- In-App URLs and Namespacing

Only function that works properly is the Facebook login authentication.
Requires a local https server - can use ngrok in order to host a temporary server but there are still problems with  csrf tokens and callback urls.

The best Facebook integration uses the request python library. Other python facebook apis are mostly deprecated. 
New django sandbox is the django-okta-skyflow-integration project

See DOSSI-demo (now private) for Django Okta Stripe, Skyflow integrations.
