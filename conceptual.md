### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgeSQL is a database system used to bring the data from databases to the Flask app

- What is the difference between SQL and PostgreSQL?
  PostgreSQL is an object-relational database

- In `psql`, how do you connect to a database?
  'app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///DATABASE NAME'

- What is the difference between `HAVING` and `WHERE`?
  WHERE is before a group is made, HAVING is filtering from a group

- What is the difference between an `INNER` and `OUTER` join?
  INNER and OUTER joins are based on which database is the 'inside' or 'outside'
  database and will join where you put the keyword. Then based on that it will merge a certain way based on what keyword was input


- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  Pulling different info from the 'Left' Database and visa versa

- What is an ORM? What do they do?
  Object Relational Mapper, it translates between the database and the code

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  Server side requests are generally better in my opinion because it lowers the chance of an attack being succesful because the server sends the request itself based on user input and returns something to the user

- What is CSRF? What is the purpose of the CSRF token?
  CSRF token is a Cross-Site Reference Token, These are used to verify the transaction

- What is the purpose of `form.hidden_tag()`?
  The above code snippet is because the CSRF token is automatically under a hidden class so this will be able to hide or show the token.
