Folder with all API endpoints.<br>
Each API method is realized through flask `Blueprint` concept and should be kept in different file.<br>
Each API method __needs to start with /api/__<br>


## GET Endpoints
- `/api/songs` - Returns list of all songs and respective info.


## POST Endpoints
- `/api/user_import` - Adds a user to db.users table

## Folder content
* __api_getter.py__
    - Consists of all API __GET__ endpoints.
* __api_post.py__
    - Consists of all API __POST__ endpoints.
