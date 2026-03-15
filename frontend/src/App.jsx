import { useState, useEffect } from "react"
import axios from "axios"

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
      
      {/* Header */}
      <div className="bg-blue-600 text-white p-6 text-center">
        <h1 className="text-4xl font-bold">🎯 AI Internship Portal</h1>
        <p className="mt-2 text-blue-100">
          Find your perfect internship using AI
        </p>
      </div>

      {/* AI Search Box */}
      <div className="max-w-2xl mx-auto mt-8 px-4">
        <div className="bg-white rounded-xl shadow-md p-6">
          <h2 className="text-xl font-bold text-gray-800 mb-4">
            🤖 AI Match — Enter Your Skills
          </h2>
          <input
            type="text"
            placeholder="e.g. Java Python MongoDB Backend"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
            className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-700 focus:outline-none focus:border-blue-500"
          />
          <button
            onClick={findMatches}
            className="mt-4 w-full bg-blue-600 text-white py-3 rounded-lg font-bold hover:bg-blue-700"
          >
            Find Best Internships for Me 🚀
          </button>
        </div>
      </div>

      {/* AI Match Results */}
      {searched && (
        <div className="max-w-6xl mx-auto mt-8 px-4">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">
            🎯 AI Matched Results
          </h2>
          {searching ? (
            <p className="text-center text-gray-500">AI match dhundh raha hai...</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {matches.filter(m => m.matchScore > 0).map((match, index) => (
                <div key={index}
                  className="bg-white rounded-xl shadow-md p-6 border-l-4 border-blue-500">
                  <div className="flex justify-between items-start">
                    <h2 className="text-lg font-bold text-gray-800">
                      {match.title}
                    </h2>
                    <span className="bg-blue-100 text-blue-700 text-sm font-bold px-2 py-1 rounded-full">
                      {match.matchScore}%
                    </span>
                  </div>
                  <p className="text-blue-500 font-medium mt-1">{match.company}</p>
                  <p className="text-gray-500 mt-1">📍 {match.location}</p>
                  <p className="text-green-600 font-medium mt-1">
                    💰 {match.stipend}
                  </p>
                  <a href={match.applyLink} target="_blank"
                    className="mt-4 block text-center bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600">
                    Apply Now
                  </a>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* All Internships */}
      <div className="max-w-6xl mx-auto mt-8 px-4 pb-12">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">
          📋 All Internships
        </h2>
        {loading ? (
          <p className="text-center text-gray-500">Loading...</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {internships.map((internship) => (
              <div key={internship.id}
                className="bg-white rounded-xl shadow-md p-6 hover:shadow-lg transition">
                <h2 className="text-xl font-bold text-gray-800">
                  {internship.title}
                </h2>
                <p className="text-blue-500 font-medium mt-1">
                  {internship.company}
                </p>
                <p className="text-gray-500 mt-1">📍 {internship.location}</p>
                <p className="text-green-600 font-medium mt-1">
                  💰 {internship.stipend}
                </p>
                <a href={internship.applyLink} target="_blank"
                  className="mt-4 block text-center bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600">
                  Apply Now
                </a>
              </div>
            ))}
          </div>
        )}
      </div>

    </div>
  )
}

export default App