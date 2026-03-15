function Navbar() {
  return (
    <nav className="bg-blue-600 text-white px-8 py-4 flex justify-between items-center shadow-lg">
      <h1 className="text-2xl font-bold">🎯 AI Internship Portal</h1>
      <div className="flex gap-6">
        <a href="#all" className="hover:text-blue-200 font-medium">All Internships</a>
        <a href="#search" className="hover:text-blue-200 font-medium">AI Search</a>
      </div>
    </nav>
  )
}

export default Navbar