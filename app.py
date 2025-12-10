from shiny import App, render, ui
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the UI
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h3("Controls"),
        ui.input_slider(
            "n_points",
            "Number of points:",
            min=10,
            max=500,
            value=100,
            step=10
        ),
        ui.input_select(
            "plot_type",
            "Plot type:",
            choices={"scatter": "Scatter Plot", "histogram": "Histogram", "line": "Line Plot"},
            selected="scatter"
        ),
        ui.input_text(
            "title",
            "Plot Title:",
            value="My Plot"
        )
    ),
    ui.h2("Dante's Simple Shiny App in Python"),
    ui.output_plot("main_plot"),
    ui.h4("Summary Statistics (if working)"),
    ui.output_table("summary_table")
)

# Define the server logic
def server(input, output, session):

    @output
    @render.plot
    def main_plot():
        # Generate random data
        np.random.seed(42)
        x = np.random.normal(0, 1, input.n_points())
        y = np.random.normal(0, 1, input.n_points())

        fig, ax = plt.subplots(figsize=(8, 6))

        if input.plot_type() == "scatter":
            ax.scatter(x, y, alpha=0.6)
            ax.set_xlabel("X values")
            ax.set_ylabel("Y values")
        elif input.plot_type() == "histogram":
            ax.hist(x, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
            ax.set_xlabel("Values")
            ax.set_ylabel("Frequency")
        elif input.plot_type() == "line":
            sorted_indices = np.argsort(x)
            ax.plot(x[sorted_indices], y[sorted_indices], marker='o', markersize=3)
            ax.set_xlabel("X values")
            ax.set_ylabel("Y values")

        ax.set_title(input.title())
        ax.grid(True, alpha=0.3)

        return fig

    @output
    @render.table
    def summary_table():
        # Generate the same random data for consistency
        np.random.seed(42)
        x = np.random.normal(0, 1, input.n_points())
        y = np.random.normal(0, 1, input.n_points())

        # Create summary statistics
        summary_data = {
            "Statistic": ["Count", "Mean X", "Mean Y", "Std X", "Std Y", "Min X", "Max X", "Min Y", "Max Y"],
            "Value": [
                len(x),
                f"{np.mean(x):.3f}",
                f"{np.mean(y):.3f}",
                f"{np.std(x):.3f}",
                f"{np.std(y):.3f}",
                f"{np.min(x):.3f}",
                f"{np.max(x):.3f}",
                f"{np.min(y):.3f}",
                f"{np.max(y):.3f}"
            ]
        }

        return pd.DataFrame(summary_data)

# Create the app
app = App(app_ui, server)

if __name__ == "__main__":
    app.run(port=8001)
