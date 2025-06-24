# Import the QueryBase class
# YOUR CODE HERE

# Import dependencies for sql execution
#### YOUR CODE HERE

# Create a subclass of QueryBase
# called  `Team`
#### YOUR CODE HERE

    # Set the class attribute `name`
    # to the string "team"
    #### YOUR CODE HERE


    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE
        
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        #### YOUR CODE HERE
    

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE

        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        #### YOUR CODE HERE


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):

        return f"""
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                   )
                """

#### team.py was updated with my code below

# Import the QueryBase class
from report.src.sql_base import QueryBase

# Import dependencies for SQL execution
from report.src.sql_execution import execute_query, execute_dataframe

# Create a subclass of QueryBase called `Team`
class Team(QueryBase):

    # Set the class attribute `name` to the string "team"
    name = "team"

    # Define a `names` method that receives no arguments
    # and returns a list of tuples from an SQL execution
    def names(self):
        # Query 5: Select team_name and team_id from all teams
        query = f"""
            SELECT team_name, team_id
            FROM {self.name}
        """
        return execute_query(query)

    # Define a `username` method that receives an ID argument
    # and returns a list of tuples from an SQL execution
    def username(self, id):
        # Query 6: Select team_name where team_id matches
        query = f"""
            SELECT team_name
            FROM {self.name}
            WHERE {self.name}_id = {id}
        """
        return execute_query(query)

    # Use a dataframe execution method to return ML-ready data
    def model_data(self, id):
        query = f"""
            SELECT positive_events, negative_events FROM (
                SELECT employee_id,
                       SUM(positive_events) AS positive_events,
                       SUM(negative_events) AS negative_events
                FROM {self.name}
                JOIN employee_events
                    USING({self.name}_id)
                WHERE {self.name}.{self.name}_id = {id}
                GROUP BY employee_id
            )
        """
        return execute_dataframe(query)
