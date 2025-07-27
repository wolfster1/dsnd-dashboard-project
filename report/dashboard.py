import matplotlib.pyplot as plt
import numpy as np

# --- Import core classes from the package ---
from employee_events.report.src.base_dashboard import QueryBase
from employee_events.report.src.employee import Employee
from employee_events.report.src.team import Team

# --- Dashboard Class ---
class Dashboard:
    def __init__(self, db_name, view_mode="employee", shift=None):
        self.db_name = db_name
        self.view_mode = view_mode.lower()      # "employee" or "team"
        self.shift = shift                      # Optional: "day", "night", etc.
        self.model = self._get_model_class()    # Set based on view_mode

    def _get_model_class(self):
        # Use inheritance from QueryBase subclasses
        if self.view_mode == "team":
            return Team(self.db_name)
        else:
            return Employee(self.db_name)

    def fetch_performance_data(self):
        return self.model.performance_by_shift(self.shift)

    def generate_performance_plot(self):
        data = self.fetch_performance_data()

        if not data:
            print("No performance data available for selected filter.")
            return

        names, scores = zip(*data)
        norm = plt.Normalize(min(scores), max(scores))
        colors = plt.cm.RdYlGn(norm(scores))

        plt.figure(figsize=(10, 6))
        plt.barh(names, scores, color=colors)
        plt.xlabel("Performance Score")
        title = f"{self.view_mode.capitalize()} Performance"
        if self.shift:
            title += f" - {self.shift.capitalize()} Shift"
        plt.title(title)
        plt.tight_layout()
        plt.show()

# --- Usage ---
if __name__ == "__main__":
    # Example usage
    dashboard = Dashboard("employee_events.db", view_mode="employee", shift="night")
    dashboard.generate_performance_plot()
