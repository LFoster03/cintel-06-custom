# Diamonds Explorer 💎
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

### How It Meets Project Requirements
Reactive calc: filtered_data() used by text, table, and plots.

UI Inputs in Sidebar: Dropdown, checkbox group, slider.

Main Content Outputs: Card with text, table, two charts.

Template: Uses ui.page_opts (basic template, no columns or navigation required).

Visual Enhancements: Emojis added to title and summary for engagement.

### Resources
Dataset
Diamonds dataset (CSV)

Input Component API
ui.input_slider – Shiny Express API

Output Component API (Data)
ui.HTML – Shiny Express API

Output Component API (Charts)
render.plot – Shiny Express API

## Additional Features (Live Simulation)
#### Simulated Metric
A reactive calc fake_metric() generates a random “average price” every 5 seconds to mimic live data.

Displayed in a value box with an emoji: 💰.

Automatically refreshes without user input (demonstrates reactive.invalidate_later()).

#### Live Histogram
Tracks the last 50 simulated metric values using a reactive value price_history.

Uses @reactive.effect combined with @reactive.event(fake_metric) to append new data points only when fake_metric changes (avoiding infinite loops).

Plots a histogram (orange) of simulated price values updating every 5 seconds.

#### How It Works
Reactive Flow

fake_metric() → triggers every 5 seconds.

@reactive.effect listens for changes and appends to price_history.

simulated_price_histogram() renders a histogram of recent values.

Performance Handling

price_history is trimmed to last 50 values to prevent memory bloat or slow rendering.

UI Placement

Value box and live histogram are shown in the main content area alongside filtered data visuals.

#### Project Requirement Highlights
Reactive Aspects:

filtered_data() for user-driven filtering

fake_metric() + price_history for time-driven updates

Multiple Output Types:

Static histogram & scatterplot (filtered diamonds)

Live histogram (simulated metric)

Summary card and HTML table

Demonstrates advanced reactivity:

Combination of reactive.calc, reactive.event, and reactive.value.

#### Helpful API References
Reactive calc: reactive.calc()

Reactive effect/event: reactive.effect() and reactive.event()

Value box: ui.value_box()

Plot output: render.plot()

