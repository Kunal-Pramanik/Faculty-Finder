"use client";
import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]); 
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-gray-50 font-sans text-gray-900">
      
      {/* 1. STICKY NAVIGATION */}
      <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🎓</span>
            <span className="font-bold text-xl tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-blue-900 to-indigo-700">
              NEXTOD
            </span>
          </div>
          <div className="hidden md:flex items-center gap-8 text-sm font-medium text-gray-600">
            <a href="#" className="hover:text-blue-600 transition-colors">Home</a>
            <a href="#" className="hover:text-blue-600 transition-colors">Faculty</a>
            <a href="#" className="hover:text-blue-600 transition-colors">How It Works</a>
            <a href="#" className="hover:text-blue-600 transition-colors">Data Insights</a>
            <button className="bg-blue-900 text-white px-5 py-2 rounded-lg hover:bg-blue-800 transition-all shadow-md">
              Find Faculty
            </button>
          </div>
        </div>
      </nav>

      {/* 2. HERO SECTION (Blue Theme) */}
      <section className="bg-gradient-to-br from-blue-950 via-blue-900 to-indigo-800 text-white py-20 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-6xl font-extrabold mb-6 leading-tight">
            Find the Right Faculty for Your <br className="hidden md:block"/>
            Research — Using AI
          </h1>
          <p className="text-lg md:text-xl text-blue-100 mb-10 opacity-90 max-w-2xl mx-auto">
            Discover faculty expertise beyond titles using intelligent semantic search.
          </p>

          {/* INTEGRATED SEARCH BAR */}
          <div className="relative max-w-2xl mx-auto flex flex-col md:flex-row gap-3 p-2 bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20">
            <input 
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="flex-1 bg-white text-gray-900 px-6 py-4 rounded-xl outline-none focus:ring-2 ring-blue-400"
              placeholder="Search research interests (e.g. Machine Learning)..."
            />
            <button className="bg-emerald-500 hover:bg-emerald-400 text-white px-8 py-4 rounded-xl font-bold flex items-center justify-center gap-2 transition-all shadow-lg active:scale-95">
              <span>🔍</span> Search
            </button>
          </div>
        </div>
      </section>

      {/* 3. STATS GRID (Matching the video sample) */}
      <section className="max-w-6xl mx-auto -mt-10 px-4 mb-20">
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          {[
            { label: "Total Faculty", val: "111" },
            { label: "Regular Faculty", val: "68" },
            { label: "Adjunct Faculty", val: "26" },
            { label: "International", val: "11" },
            { label: "Distinguished", val: "2" }
          ].map((stat, i) => (
            <div key={i} className="bg-white p-6 rounded-2xl shadow-xl border border-gray-100 text-center transform hover:-translate-y-1 transition-all">
              <p className="text-3xl font-bold text-blue-900">{stat.val}</p>
              <p className="text-xs text-gray-500 font-semibold uppercase mt-1">{stat.label}</p>
            </div>
          ))}
        </div>
      </section>
      
      {/* 4. CONTENT PLACEHOLDER (How it works / Results) */}
      <main className="max-w-7xl mx-auto px-4 pb-20">
         {/* We will add your AI recommendation cards here next! */}
      </main>
    </div>
  );
}
