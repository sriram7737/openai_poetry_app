from flask import Flask, render_template, request, jsonify
import openai
import config
import mysql.connector

openai.api_key = config.API_KEY

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'poetry_app'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route("/")
def index():
    # Render the main page with forms for generating poetry, submitting feedback, etc.
    return render_template("index.html")

@app.route("/generate_poetry", methods=['POST'])
def generate_poetry():
    theme = request.form['theme']
    style = request.form['style']
    # Adjust the prompt based on parameters and generate poetry using OpenAI
    prompt = f"Write a {style} about {theme}"
    response = generate_with_openai(prompt)
    # Save the generated poem to the database
    if response['success']:
        save_poem_to_db(theme, style, response['content'])
    return jsonify(response)

def generate_with_openai(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1,
        )
        return {"success": True, "content": response.choices[0].text}
    except openai.Error as e:
        return {"success": False, "error": str(e)}

def save_poem_to_db(theme, style, content):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO poems (theme, style, content) VALUES (%s, %s, %s)"
    cursor.execute(query, (theme, style, content))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    app.run(debug=True)
