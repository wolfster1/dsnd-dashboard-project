import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# --- Base and Mixin Classes (unchanged) ---
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def close(self):
        if self.connection:
            self.connection.close()

class QueryMixin:
    def execute_query(self, query):
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        else:
            raise ConnectionError("Database connection not established.")

# --- Dashboard Class ---
class Dashboard(DatabaseConnection, QueryMixin):
    def __init__(self, db_name, view_mode="employee"):
        super().__init__(db_name)
        self.connect()
        self.view_mode = view_mode  # Determines title: "employee" or "team"

    def fetch_performance_data(self):
        query = "SELECT name, performance_score FROM employee_performance"
        return self.execute_query(query)

    def generate_performance_plot(self):
        data = self.fetch_performance_data()
        names, scores = zip(*data)

        # Color scale from red (low) to green (high)
        norm = plt.Normalize(min(scores), max(scores))
        colors = plt.cm.RdYlGn(norm(scores))

        plt.figure(figsize=(10, 6))
        plt.barh(names, scores, color=colors)
        plt.xlabel("Performance Score")
        title = "Employee Performance" if self.view_mode == "employee" else "Team Performance"
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def __del__(self):
        self.close()

# --- Usage ---
if __name__ == "__main__":
    dashboard = Dashboard("employee_events_db.db", view_mode="team")  # Try "employee" or "team"
    dashboard.generate_performance_plot()
