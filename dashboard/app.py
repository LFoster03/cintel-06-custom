# -------------------------------------
# Diamonds Explorer 💎
# -------------------------------------
from shiny.express import ui, input, render
from shiny import reactive
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
diamonds = sns.load_dataset("diamonds")

# -------------------
# UI Page Setup
# -------------------
ui.page_opts(title="Diamonds Explorer 💎", fillable=True)

# Sidebar with filters
with ui.sidebar():
    ui.h3("Filters")

    # Cut (single select)
    ui.input_select(
        "cut",
        "Select cut:",
        choices=diamonds["cut"].unique().tolist(),
        selected="Ideal"
    )

    # Color (multi-select via checkbox group)
    ui.input_checkbox_group(
        "color",
        "Select colors:",
        choices=diamonds["color"].unique().tolist(),
        selected=["D", "E", "F"]
    )

    # Price range slider
    ui.input_slider(
        "price_range",
        "Price range (USD):",
        min=int(diamonds["price"].min()),
        max=int(diamonds["price"].max()),
        value=(500, 5000),
        step=100
    )

# -------------------
# Reactive filtered data
# -------------------
@reactive.calc
def filtered_data():
    """Filter diamonds dataset based on sidebar inputs."""
    df = diamonds.copy()

    # Filter by cut
    df = df[df["cut"] == input.cut()]

    # Filter by color
    df = df[df["color"].isin(input.color())]

    # Filter by price range
    min_price, max_price = input.price_range()
    df = df[(df["price"] >= min_price) & (df["price"] <= max_price)]

    return df

# -------------------
# Output: Text summary inside a card
# -------------------
with ui.card():
    ui.card_header("Summary 💎")

    @render.text
    def summary_text():
        count = len(filtered_data())
        return f"{count} diamonds match your filters."

# -------------------
# Output: Table using HTML (no Jinja2)
# -------------------
@render.ui
def summary_table():
    """Render first 10 rows of filtered data as HTML table."""
    df = filtered_data().head(10)
    html_table = df.to_html(classes="table table-striped", index=False, border=0)
    return ui.HTML(html_table)

# -------------------
# Output: Histogram
# -------------------
@render.plot
def price_histogram():
    """Histogram of diamond prices."""
    plt.figure(figsize=(6, 4))
    sns.histplot(filtered_data()["price"], bins=30, kde=False, color="skyblue")
    plt.xlabel("Price (USD)")
    plt.ylabel("Count")
    plt.title("Price Distribution")
    return plt.gcf()

# -------------------
# Output: Scatterplot
# -------------------
@render.plot
def carat_vs_price():
    """Scatterplot of carat vs price, colored by clarity."""
    plt.figure(figsize=(6, 4))
    sns.scatterplot(
        data=filtered_data(),
        x="carat",
        y="price",
        hue="clarity",
        palette="viridis",
        alpha=0.7
    )
    plt.title("Carat vs Price by Clarity")
    return plt.gcf()
