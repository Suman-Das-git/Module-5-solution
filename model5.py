from flask import Flask, render_template_string

app = Flask(__name__)

def get_all_categories():
    return ["Lunch", "Dinner", "Sushi", "Specials", "Breakfast"]

@app.route('/')
def home():
    categories = get_all_categories()
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Restaurant App</title>
            <script>
                // Array of category short names
                const categories = {{ categories|tojson }};
        
                // Function to load menu items for a random category
                function loadRandomCategory() {
                    const randomCategory = categories[Math.floor(Math.random() * categories.length)];
                    window.location.href = `/category/${randomCategory}`;
                }
            </script>
        </head>
        <body>
            <div class="tile-container">
                <div class="tile" onclick="window.location.href='/menu'">Menu</div>
                <div class="tile">
                    <a href="#" onclick="loadRandomCategory();">Specials</a>
                </div>
                <div class="tile" onclick="window.location.href='/map'">Map</div>
            </div>
        </body>
        </html>
    ''', categories=categories)

@app.route('/category/<category_name>')
def show_category(category_name):
    categories = get_all_categories()
    if category_name not in categories:
        return "Category not found", 404
    return f"Showing items for category: {category_name}"

if __name__ == "__main__":
    app.run(debug=True)
