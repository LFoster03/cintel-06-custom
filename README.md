# cintel-06-custom Diamonds Explorer 💎
An interactive Shiny for Python app built with Shiny Express to explore the Seaborn diamonds dataset. Users can filter diamonds by cut, color, and price range, and view filtered data as tables and visualizations.

## Features
### Reactive Aspects
@reactive.calc: filtered_data() dynamically updates whenever sidebar inputs change.

All outputs (text, table, plots) depend on this reactive dataset.

### UI Inputs
Cut (Dropdown) – Select a single cut (e.g., Ideal, Premium).

Color (Checkbox Group) – Select multiple color grades.

Price Range (Slider) – Adjust the minimum and maximum diamond price.

### Sidebar Components
Contains all filtering inputs for controlling the dataset.

### Main Content
Summary Card (Text Output) – Shows count of diamonds matching filters.

HTML Table (First 10 Rows) – Displays filtered data without requiring Jinja2.

Histogram (Matplotlib + Seaborn) – Price distribution of filtered diamonds.

Scatterplot (Matplotlib + Seaborn) – Carat vs Price, colored by clarity.

### Dataset
Uses the built-in Seaborn diamonds dataset:

54,000 rows of diamond data

Columns: carat, cut, color, clarity, price, dimensions (x, y, z)