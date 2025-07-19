import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# --- Base and Mixin Classes ---
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
    def __init__(self, db_name, view_mode="employee", shift=None):
        super().__init__(db_name)
        self.connect()
        self.view_mode = view_mode    # View mode: "employee" or "team"
        self.shift = shift            # Optional shift filter: "day", "night", etc.

    def fetch_performance_data(self):
        base_query = """
            SELECT 
                e.first_name || ' ' || e.last_name AS full_name,
                SUM(ev.positive_events) - SUM(ev.negative_events) AS performance_score
            FROM employee e
            JOIN employee_events ev ON e.employee_id = ev.employee_id
        """

        filters = []
        if self.shift:
            filters.append(f"e.shift = '{self.shift}'")

        where_clause = f"WHERE {' AND '.join(filters)}" if filters else ""
        group_order_clause = "GROUP BY e.employee_id ORDER BY performance_score DESC"

        full_query = f"{base_query} {where_clause} {group_order_clause}"
        return self.execute_query(full_query)

    def generate_performance_plot(self):
        data = self.fetch_performance_data()

        if not data:
            print("No performance data available for the selected filter.")
            return

        names, scores = zip(*data)

        # Color scale from red (low) to green (high)
        norm = plt.Normalize(min(scores), max(scores))
        colors = plt.cm.RdYlGn(norm(scores))

        plt.figure(figsize=(10, 6))
        plt.barh(names, scores, color=colors)
        plt.xlabel("Performance Score")
        title = f"{'Employee' if self.view_mode == 'employee' else 'Team'} Performance"
        if self.shift:
            title += f" - {self.shift.capitalize()} Shift"
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def __del__(self):
        self.close()

# --- Usage ---
if __name__ == "__main__":
    # Choose view_mode="employee" or "team", and optionally set shift="day", "night", etc.
    dashboard = Dashboard("employee_events.db", view_mode="employee", shift="night")
    dashboard.generate_performance_plot()
