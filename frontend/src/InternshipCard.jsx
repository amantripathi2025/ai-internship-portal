function InternshipCard({ internship }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6 hover:shadow-xl transition duration-300 border border-gray-100">
      <div className="flex justify-between items-start">
        <h2 className="text-lg font-bold text-gray-800 flex-1">
          {internship.title}
        </h2>
      </div>
      <p className="text-blue-500 font-medium mt-2">
        🏢 {internship.company}
      </p>
      <p className="text-gray-500 mt-1 text-sm">
        📍 {internship.location}
      </p>
      <p className="text-green-600 font-medium mt-1 text-sm">
        💰 {internship.stipend}
      </p>
      {internship.requiredSkills && internship.requiredSkills.length > 0 && (
        <div className="mt-3 flex flex-wrap gap-2">
          {internship.requiredSkills.map((skill, i) => (
            <span key={i}
              className="bg-blue-50 text-blue-600 text-xs px-2 py-1 rounded-full">
              {skill}
            </span>
          ))}
        </div>
      )}
      <a href={internship.applyLink} target="_blank"
        className="mt-4 block text-center bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition font-medium">
        Apply Now →
      </a>
    </div>
  )
}

export default InternshipCard