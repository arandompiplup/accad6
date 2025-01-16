# ACCAD6 Capstone Project
By Ryan, Kon Chern and Oswald

## Banana Clicker App
We created an app where users can click to get bananas.

## Links
Github repo:https://github.com/arandompiplup/accad6/tree/main
App: https://4ngigjfepj.ap-southeast-1.awsapprunner.com/

### User flow
A user entering the app will first have to login with a username. If the user signs in with a unique username, they would enter the game with 0 bananas. If the user is logging in to an existing account, the user would enter the game with their last saved number of bananas under that username.

When the user wants to save their number of bananas, they can click the `Save` button in the game. If the user wants to delete their account, they can click the `Delete Account` button in the game before being redirected back to the login screen.


## Infrastructure

### App-side infrastructure
We created a flask app with 2 main sites, `/login` and `/app`. The `/app` page is the game. When the user logs into the game with `username`, we query the DynamoDB database to look for the primary key `username`. If the username is not found, we add a record where the username is `username` and bananas is 0.

The number of bananas from the database is stored as session variable `bananas`. When the user clicks the button to gain a banana, `bananas` increases by 1. When the user clicks the `Send Bananas` button, a query is sent to update the database to reflect the change in banana count

### AWS-side infrastructure
We used CodeBuild to create a build project. We also create a pipeline whose source is from our GitHub Repo. The pipeline places an output image in ECR. For storing accounts and their number of bananas, we opted to use DynamoDB. Using the image, we created a service via AppRunner.


## Considerations
1. Instead of our initial idea to update the database whenever the user clicks the button to gain bananas, we added a `Send Bananas` button for users to update their banana count. This greatly helps to reduce the number of queries to the DynamoDB database.


## Challenges

### 1. Updating DynamoDB values
When we tried to implement the clicker, we were not able to increase the `clicks` count even though the number of clicks registered was increasing as expected. Additionally, we were unable to update the database values to the updated total. We identified that this was because the `.add` method did not function the way we initially thought. We managed to fix this by incrementing a session variable `bananas` and using the `.set` method instead.

### 2. Testing constantly fails
We were only able to run tests locally rather than on the test stage in the pipeline
Furthermore, the tests only really work on Ryan's machine

### 3. Exceed API limit
We constantly exceed Docker's API limits because the pipeline restarts after every push. To prevent this, we made the updating of the pipeline to be manual rather than automated

## References
Banana: https://www.svgfind.com/svg/10902481/banana-republic