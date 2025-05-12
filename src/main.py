from flask import Flask, render_template, request
from api.client import AutomyClient
from services.filter_service import filter_races_by_date
from services.message_service import format_races_message, show_full_history

app = Flask(__name__, template_folder="../frontend")

@app.route("/", methods=["GET", "POST"])
def home():
    client = AutomyClient()
    email = request.form.get("email", "john.doe@gmail.com") if request.method == "POST" else "john.doe@gmail.com"
    try:
        races_data = client.get_races(email)
        past_races, upcoming_races = filter_races_by_date(races_data)
        
        if request.path == "/toggle-history":
            return render_template(
                "index.html",
                upcoming_races=upcoming_races,
                past_races=past_races,
                show_history=True
            )
        
        return render_template(
            "index.html",
            upcoming_races=upcoming_races,
            past_races=past_races,
            show_history=False
        )
    except Exception as e:
        return render_template(
            "index.html",
            upcoming_races=[],
            past_races=[],
            show_history=False,
            error=f"Erro ao carregar dados: {str(e)}"
        )

@app.route("/toggle-history")
def toggle_history():
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)