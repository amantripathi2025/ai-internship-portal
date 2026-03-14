from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connect karo
MONGO_URL = "mongodb+srv://amantripathi7550_db_user:D9L1RpYChCvpBpGj@ai-internship-portal.ftfkc7h.mongodb.net/?appName=ai-internship-portal"
client = MongoClient(MONGO_URL, tlsAllowInvalidCertificates=True)
db = client["internship-portal"]

@app.route('/match', methods=['POST'])
def match():
    # Student ki skills lo
    data = request.json
    student_skills = data.get('skills', '')
    
    if not student_skills:
        return jsonify({"error": "Skills provide karo!"}), 400
    
    # MongoDB se internships laao
    internships = list(db["internships"].find())
    
    if not internships:
        return jsonify({"error": "Koi internship nahi mili!"}), 404
    
    # Texts banao
    internship_texts = []
    for internship in internships:
        skills = " ".join(internship.get("requiredSkills", []))
        text = f"{internship['title']} {skills} {internship.get('description', '')}"
        internship_texts.append(text)
    
    # TF-IDF matching
    all_texts = [student_skills] + internship_texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Results banao
    results = []
    for i, score in enumerate(scores):
        internship = internships[i]
        results.append({
            "id": str(internship["_id"]),
            "title": internship["title"],
            "company": internship["company"],
            "location": internship.get("location", "N/A"),
            "stipend": internship.get("stipend", "N/A"),
            "matchScore": round(float(score) * 100, 2),
            "applyLink": internship.get("applyLink", "N/A")
        })
    
    # Sort by score
    results.sort(key=lambda x: x["matchScore"], reverse=True)
    
    return jsonify(results[:10])

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "AI Engine chal raha hai!"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)