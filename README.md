# ACCAD6 Capstone Project
By Ryan, Kon Chern and Oswald

## Our App (Banana Clicker)
We created an app where users can click to get (bananas). 

### User flow
A user entering the app will first have to login with a username. If the user signs in with a unique username, they would enter the game with 0 (bananas). If the user is logging in to an existing account, the user would enter the game with their last saved number of (bananas) under that username. When the user wants to save their number of (bananas), they can click the `Save` button in the game. If the user wants to delete their account, they can click the `Delete Account` button in the game before being redirected back to the login screen. 

## Infrastructure

### App-side infrastructure
We created a flask app with 2 main sites, `/login` and `/app`. The `/app` page is the game. When the user logs into the game with `username`, we query the DynamoDB database to look for the primary key `username`. If the username is not found, we add a record where the username is `username` and (bananas) is 0.

The number of (bananas) from the database is stored as `bananas`. When the user clicks the button to gain a (banana), the session variable `clicks` increases by 1. When the user saves their new number of (bananas), we query the database to update `bananas` in case it has changed during the session. Then, we add up the `bananas` with `clicks` and then updating the database with their sum 

### AWS-side infrastructure
We used CodeBuild to create a build project. We also create a pipeline


## Considerations
1. Instead of the initial idea to update the database whenever the user clicks the button to gain (bananas), we added a `save` button for users to update their (banana) count. This greatly helps to reduce the number of writes to the DynamoDB database.
2. Since we did not implement a means to prevent multiple users from logging in to the same account concurrently, we decided that when a user saves their number of bananas, it queries the databse to obtain the updated (banana) count and store it as `bananas`. This prevent clashes when updating the (banana) count of the account
3. We used DynamoDB instead of RDS as RDS is more costly

## Challenges

### 1. Updating DynamoDB values
When we tried to implement the clicker, we were not able to increase the `clicks` count even though the number of clicks registered were increasing as per normal. Additionally, we were unable to update the database values to the updated total. We identified that this was because the `.add` method did not function the way we initially thought. We managed to fix this by storing the session variable `bananas` and incrementing it and used the `.set` method instead.