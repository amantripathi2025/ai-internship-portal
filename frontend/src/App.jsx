import { useState, useEffect } from "react"
import axios from "axios"
import Navbar from "./components/Navbar"
import Footer from "./components/Footer"
import InternshipCard from "./InternshipCard"

function App() {
  const [internships, setInternships] = useState([])
  const [loading, setLoading] = useState(true)
  const [skills, setSkills] = useState("")
  const [matches, setMatches] = useState([])
  const [searching, setSearching] = useState(false)
  const [searched, setSearched] = useState(false)

  useEffect(() => {
    axios.get("http://localhost:8080/api/internships")
      .then(res => {
        setInternships(res.data)
        setLoading(false)
      })
      .catch(err => {
        console.log(err)
        setLoading(false)
      })
  }, [])

  const findMatches = () => {
    if (!skills.trim()) return
    setSearching(true)
    setSearched(true)
    axios.post("http://127.0.0.1:5000/match", { skills })
      .then(res => {
        setMatches(res.data)
        setSearching(false)
      })
      .catch(err => {
        console.log(err)
        setSearching(false)
      })
  }

  return (
    <div className="min-h-screen bg-gray-100">

      <Navbar />

      {/* Hero Section */}
      <div className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-16 px-4 text-center">
        <h1 className="text-5xl font-bold mb-4">🎯 AI Internship Portal</h1>
        <p className="text-xl text-blue-100 mb-2">
          Find your perfect internship using Artificial Intelligence
        </p>
        <p className="text-blue-200 text-sm">
          Powered by TF-IDF + Cosine Similarity matching
        </p>
      </div>

      {/* AI Search Box */}
      <div className="max-w-2xl mx-auto mt-10 px-4" id="search">
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-2">
            🤖 AI Skill Matcher
          </h2>
          <p className="text-gray-500 mb-4 text-sm">
            Enter your skills and AI will find the best internships for you!
          </p>
          <input
            type="text"
            placeholder="e.g. Java Python MongoDB Backend Development"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && findMatches()}
            className="w-full border-2 border-gray-200 rounded-xl px-4 py-3 text-gray-700 focus:outline-none focus:border-blue-500"
          />
          <button
            onClick={findMatches}
            className="mt-4 w-full bg-blue-600 text-white py-3 rounded-xl font-bold hover:bg-blue-700 transition text-lg"
          >
            🚀 Find Best Internships for Me
          </button>
        </div>
      </div>

      {/* AI Match Results */}
      {searched && (
        <div className="max-w-6xl mx-auto mt-10 px-4">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">
            🎯 AI Matched Results for "{skills}"
          </h2>
          {searching ? (
            <p className="text-center text-gray-500 py-8">
              🤖 AI match dhundh raha hai...
            </p>
          ) : matches.filter(m => m.matchScore > 0).length === 0 ? (
            <p className="text-center text-gray-500 py-8">
              Koi match nahi mila — alag skills try karo!
            </p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {matches.filter(m => m.matchScore > 0).map((match, index) => (
                <div key={index}
                  className="bg-white rounded-xl shadow-md p-6 border-l-4 border-blue-500 hover:shadow-xl transition">
                  <div className="flex justify-between items-start mb-2">
                    <h2 className="text-lg font-bold text-gray-800 flex-1">
                      {match.title}
                    </h2>
                    <span className="bg-blue-100 text-blue-700 text-sm font-bold px-3 py-1 rounded-full ml-2">
                      {match.matchScore}%
                    </span>
                  </div>
                  <p className="text-blue-500 font-medium">🏢 {match.company}</p>
                  <p className="text-gray-500 mt-1 text-sm">📍 {match.location}</p>
                  <p className="text-green-600 font-medium mt-1 text-sm">
                    💰 {match.stipend}
                  </p>
                  <a href={match.applyLink} target="_blank"
                    className="mt-4 block text-center bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition font-medium">
                    Apply Now →
                  </a>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* All Internships */}
      <div className="max-w-6xl mx-auto mt-10 px-4 pb-12" id="all">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">
          📋 All Internships ({internships.length})
        </h2>
        {loading ? (
          <p className="text-center text-gray-500 py-8">Loading internships...</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {internships.map((internship) => (
              <InternshipCard key={internship.id} internship={internship} />
            ))}
          </div>
        )}
      </div>

      <Footer />

    </div>
  )
}

export default App