# Django_LLM_Integration

This Django application integrated with two open-source Language Models (LLMs) from Hugging Face. The application will allow users to choose which LLM they want to chat with, and for each LLM, the responses will be stored in a MongoDB database.

## Requirement Libraries
1. Django
2. djongo
3. dnspython
4. pymongo
5. pytz
6. requests

## Steps to create a new Database
1. Create a new database in the name of __'djangollm'__ in MongoDB Atlas.
2. Create a username and password for the particular DB Project.
3. Collecte the config link for django framework from Atlas.

## Steps to create Huggingface access token
1. Login to the Huggingface account.
2. Click the settings menu.
3. Click the access token option.
4. Now create a new token and copy it.


## Steps to run the application
1. Download the application from github.
2. Install the required libraries.
3. Open the settings file.
4. Update your DB username and password in the __'DATABASES'__ config.
5. Update the __'HUGGINGFACE_API_TOKEN'__ which copied from Huggingface.
6. Now run the following commands
   * __'python manage.py makemigrations'__
   * __'python manage.py migrate'__
   * __'python manage.py runserver'__
7. Now copy/click the link that displayed in the console to open the application.
