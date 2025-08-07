#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
app = Flask(__name__)

symptoms = {
    "sore throat": "Drink warm fluids, gargle salt water. May be viral or bacterial.",
    "headache": "Rest in a quiet room, hydrate. If severe or frequent, consult a doctor.",
    "stomach pain": "Could be indigestion, gas, or serious. Eat light, monitor symptoms.",
}

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "").lower()
    results = []
    for key, text in symptoms.items():
        if key in query:
            results.append({
                "title": f"Info on {key}",
                "body": text,
                "url": f"https://example.com/{key.replace(' ', '-')}"
            })
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

