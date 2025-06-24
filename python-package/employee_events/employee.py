# Import the QueryBase class
#### YOUR CODE HERE

# Import dependencies needed for sql execution
# from the `sql_execution` module
#### YOUR CODE HERE

# Define a subclass of QueryBase
# called Employee
#### YOUR CODE HERE

    # Set the class attribute `name`
    # to the string "employee"
    #### YOUR CODE HERE


    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        #### YOUR CODE HERE
    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
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
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """

#### Project code is below with requirements 

# Import the QueryBase class
from report.src.sql_base import QueryBase

# Import dependencies needed for SQL execution
# from the `sql_execution` module
from report.src.sql_execution import execute_query, execute_dataframe

# Define a subclass of QueryBase called Employee
class Employee(QueryBase):

    # Set the class attribute `name` to the string "employee"
    name = "employee"

    # Define a method called `names` that receives no arguments
    # and returns a list of tuples from an SQL execution
    def names(self):
        # Query 3
        # Write an SQL query that selects two columns:
        # 1. The employee's full name
        # 2. The employee's id
        query = f"""
            SELECT full_name, {self.name}_id
            FROM {self.name}
        """
        return execute_query(query)

    # Define a method called `username` that receives an `id` argument
    # and returns a list of tuples from an SQL execution
    def username(self, id):
        # Query 4
        # Write an SQL query that selects an employee's full name
        # where the employee ID matches the given `id`
        query = f"""
            SELECT full_name
            FROM {self.name}
            WHERE {self.name}_id = {id}
        """
        return execute_query(query)

    # Return a pandas DataFrame from the executed SQL query
    def model_data(self, id):
        query = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}_id = {id}
        """
        return execute_dataframe(query)
