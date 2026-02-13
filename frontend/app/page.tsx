"use client";
import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]); 
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [errorMessage, setErrorMessage] = useState(""); // Track backend errors

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);
    setHasSearched(true);
    setErrorMessage(""); // Reset error on new search

    try {
      const response = await fetch("https://faculty-connect.onrender.com/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query }),
      });

      const data = await response.json();

      // 🛡️ SAFETY CHECK: Only set results if it's actually an array
      if (data && Array.isArray(data.results)) {
        setResults(data.results);
      } else {
        setResults([]);
        // If the backend sent a custom message (like "AI warming up"), show it
        setErrorMessage(data.message || "Unexpected response from server.");
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setErrorMessage("Failed to connect to the server. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 p-8 font-sans">
      {/* HEADER */}
      <div className="max-w-4xl mx-auto text-center mb-12 pt-10">
        <h1 className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 mb-6">
          🎓 Faculty Finder
        </h1>
        <p className="text-lg text-gray-600 mb-8 max-w-2xl mx-auto leading-relaxed">
          Don't just search for names. Search for <strong>ideas</strong>. <br />
          Tell us what you want to learn, and we'll find the perfect mentor.
        </p>

        {/* SEARCH BAR */}
        <div className="relative max-w-2xl mx-auto shadow-2xl rounded-full bg-white p-2 flex items-center border border-gray-100 transform hover:scale-105 transition-transform duration-300">
          <span className="pl-6 text-2xl">🔍</span>
          <input
            type="text"
            className="flex-1 px-4 py-4 rounded-l-full outline-none text-gray-700 text-lg placeholder-gray-400"
            placeholder="E.g., 'I want to build a deep learning model...'"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSearch()}
          />
          <button
            onClick={handleSearch}
            disabled={loading}
            className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-4 rounded-full font-bold text-lg transition-all disabled:opacity-50 shadow-md"
          >
            {loading ? "Searching..." : "Find Faculty"}
          </button>
        </div>
      </div>

      {/* LOADING STATE */}
      {loading && (
        <div className="text-center py-20">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-500 animate-pulse">Consulting the AI Brain...</p>
        </div>
      )}

      {/* ERROR MESSAGE DISPLAY */}
      {errorMessage && !loading && (
        <div className="max-w-2xl mx-auto mb-8 p-4 bg-red-50 border border-red-200 text-red-600 rounded-xl text-center">
          {errorMessage}
        </div>
      )}

      {/* RESULTS GRID */}
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 pb-20">
        {/* 🛡️ LOOP SAFETY: Use Array.isArray check */}
        {Array.isArray(results) && results.map((faculty, index) => (
          <div
            key={index}
            className="bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 border border-gray-100 overflow-hidden flex flex-col group"
          >
            {/* CARD HEADER */}
            <div className="p-6 flex items-start gap-4 border-b border-gray-50 bg-gray-50/50">
              <img
                src={faculty.image_url && faculty.image_url.startsWith("http") 
                      ? faculty.image_url 
                      : `https://www.daiict.ac.in${faculty.image_url || ""}`
                    }
                alt={faculty.name}
                className="w-20 h-20 rounded-full object-cover border-4 border-white shadow-md group-hover:scale-110 transition-transform duration-300"
                onError={(e: any) => { e.target.src = "https://via.placeholder.com/150?text=No+Img"; }}
              />
              <div>
                <h2 className="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
                  {faculty.name}
                </h2>
                <div className="mt-2 inline-block bg-green-100 text-green-700 text-xs px-3 py-1 rounded-full font-bold">
                  {(faculty.score * 100).toFixed(0)}% Match
                </div>
              </div>
            </div>

            {/* CARD BODY */}
            <div className="p-6 flex-1 space-y-4">
              <div>
                <p className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Specialization</p>
                <p className="text-sm text-gray-700 font-medium leading-snug">{faculty.specialization || "N/A"}</p>
              </div>
              
              {faculty.teaching && (
                <div>
                  <p className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Teaching</p>
                  <p className="text-sm text-gray-600 line-clamp-2" title={faculty.teaching}>
                    {faculty.teaching}
                  </p>
                </div>
              )}
            </div>

            {/* CARD FOOTER */}
            <a
              href={faculty.profile_url}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-gray-50 p-4 text-center text-blue-600 font-bold hover:bg-blue-600 hover:text-white transition-all duration-300 flex items-center justify-center gap-2"
            >
              View Full Profile <span>→</span>
            </a>
          </div>
        ))}
      </div>

      {/* EMPTY STATE */}
      {!loading && hasSearched && results.length === 0 && !errorMessage && (
        <div className="text-center py-20 text-gray-500">
          <p className="text-xl">No matches found. Try describing it differently!</p>
        </div>
      )}
    </div>
  );
}