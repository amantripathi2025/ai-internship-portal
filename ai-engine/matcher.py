from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient

# MongoDB connect karo
MONGO_URL = "mongodb+srv://amantripathi7550_db_user:D9L1RpYChCvpBpGj@ai-internship-portal.ftfkc7h.mongodb.net/?appName=ai-internship-portal"
client = MongoClient(MONGO_URL)
db = client["internship-portal"]

def match_student_to_internships(student_skills):
    """
    Student ki skills le aao
    Saari internships se match karo
    Score ke hisaab se sort karo
    Top matches return karo
    """
    
    # MongoDB se saari internships laao
    internships = list(db["internships"].find())
    
    if not internships:
        print("Koi internship nahi mili database mein!")
        return []
    
    # Har internship ki description banao matching ke liye
    internship_texts = []
    for internship in internships:
        # Title + skills + description combine karo
        skills = " ".join(internship.get("requiredSkills", []))
        text = f"{internship['title']} {skills} {internship.get('description', '')}"
        internship_texts.append(text)
    
    # Student skills + saari internships ko ek saath vectorize karo
    all_texts = [student_skills] + internship_texts
    
    # TF-IDF magic!
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Student (index 0) aur har internship ka similarity score nikalo
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Results banao
    results = []
    for i, score in enumerate(similarity_scores):
        internship = internships[i]
        results.append({
            "title": internship["title"],
            "company": internship["company"],
            "location": internship.get("location", "N/A"),
            "stipend": internship.get("stipend", "N/A"),
            "matchScore": round(float(score) * 100, 2),
            "applyLink": internship.get("applyLink", "N/A")
        })
    
    # Score ke hisaab se sort karo - best match pehle
    results.sort(key=lambda x: x["matchScore"], reverse=True)
    
    return results

# Test karte hain!
print("🤖 AI Matching Engine Test\n")
student_skills = "Java Python MongoDB Backend Development"
print(f"Student Skills: {student_skills}\n")

matches = match_student_to_internships(student_skills)

print("Top 5 Matches:")
print("-" * 50)
for i, match in enumerate(matches[:5]):
    print(f"{i+1}. {match['title']}")
    print(f"   Company: {match['company']}")
    print(f"   Match Score: {match['matchScore']}%")
    print(f"   Stipend: {match['stipend']}")
    print()