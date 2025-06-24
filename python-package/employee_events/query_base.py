# Import any dependencies needed to execute sql queries
# YOUR CODE HERE

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE

    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
        
        # Return an empty list
        # YOUR CODE HERE


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

#### Code inserted with requirements from above below

# Import any dependencies needed to execute SQL queries
import pandas as pd
from report.src.sql_execution import execute_dataframe

# Define a class called QueryBase
# Use inheritance to add methods for querying the employee_events database.
class QueryBase:
    
    # Create a class attribute called `name`
    # Set the attribute to an empty string
    name = ""

    # Define a `names` method that receives no passed arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method that receives an `id` argument
    # This method should return a pandas DataFrame
    def event_counts(self, id):
        # QUERY 1
        query = f"""
            SELECT event_date,
                   SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date
        """
        return execute_dataframe(query)

    # Define a `notes` method that receives an id argument
    # This function should return a pandas DataFrame
    def notes(self, id):
        # QUERY 2
        query = f"""
            SELECT note_date, note
            FROM notes
            JOIN {self.name}
                USING({self.name}_id)
            WHERE {self.name}_id = {id}
        """
        return execute_dataframe(query)

