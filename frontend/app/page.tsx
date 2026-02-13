"use client";
import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]); 
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-[#030712] text-slate-200 font-sans selection:bg-blue-500/30">
      
      {/* 1. CYBER NAVIGATION */}
      <nav className="border-b border-white/5 bg-black/20 backdrop-blur-xl sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-tr from-blue-600 to-cyan-400 rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20">
              <span className="text-white font-black text-xl">D</span>
            </div>
            <span className="text-xl font-bold tracking-tighter text-white">DATA RIDERS</span>
          </div>
          <div className="hidden md:flex gap-8 text-sm font-medium uppercase tracking-widest text-slate-400">
            <a href="#engine" className="hover:text-cyan-400 transition-colors">The Engine</a>
            <a href="#faculty" className="hover:text-cyan-400 transition-colors">Directory</a>
            <button className="border border-blue-500/50 text-blue-400 px-5 py-2 rounded-full hover:bg-blue-500/10 transition-all">
              Launch Search
            </button>
          </div>
        </div>
      </nav>

      {/* 2. NEURAL HERO SECTION */}
      <header className="relative pt-24 pb-32 px-6 overflow-hidden">
        {/* Animated Background Element */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-blue-900/20 via-transparent to-transparent -z-10" />
        
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-block px-4 py-1.5 mb-6 rounded-full border border-blue-500/20 bg-blue-500/5 text-blue-400 text-xs font-bold uppercase tracking-widest animate-pulse">
            Semantic Search Active
          </div>
          <h1 className="text-5xl md:text-7xl font-black text-white mb-8 tracking-tight leading-[1.1]">
            Find Your <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">Research DNA.</span>
          </h1>
          
          {/* THE COMMAND CENTER SEARCH BAR */}
          <div className="relative group max-w-3xl mx-auto">
            <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-cyan-500 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
            <div className="relative flex flex-col md:flex-row gap-2 bg-[#0f172a] p-3 rounded-2xl border border-white/10 shadow-2xl">
              <input 
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Describe your research vision..."
                className="flex-1 bg-transparent px-6 py-4 outline-none text-white text-lg placeholder:text-slate-500"
              />
              <button className="bg-blue-600 hover:bg-blue-500 text-white px-10 py-4 rounded-xl font-bold transition-all flex items-center justify-center gap-2 group">
                RIDE THE DATA 
                <span className="group-hover:translate-x-1 transition-transform">→</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* 3. FLOATING STATS (Glassmorphism) */}
      <section className="max-w-6xl mx-auto px-6 -mt-16 relative z-10">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {[
            { label: "Faculty Indexed", val: "109+" },
            { label: "Semantic Layers", val: "384" },
            { label: "Response Time", val: "ms" },
            { label: "Match Logic", val: "Cosine" }
          ].map((s, i) => (
            <div key={i} className="p-6 rounded-2xl bg-white/5 backdrop-blur-md border border-white/10 hover:border-blue-500/50 transition-colors">
              <p className="text-xs font-bold text-slate-500 uppercase mb-1 tracking-tighter">{s.label}</p>
              <p className="text-3xl font-mono font-bold text-white">{s.val}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 4. TEAM FOOTER */}
      <footer className="mt-40 border-t border-white/5 py-12 px-6 bg-black/40">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
          <div>
            <h4 className="text-white font-bold text-lg mb-2">Developed by Data Riders</h4>
            <div className="flex gap-4 text-slate-400 text-sm">
              <span className="flex items-center gap-1.5"><div className="w-1.5 h-1.5 rounded-full bg-blue-500"/> Kunal Pramanik</span>
              <span className="flex items-center gap-1.5"><div className="w-1.5 h-1.5 rounded-full bg-cyan-500"/> Jinal Sasiya</span>
            </div>
          </div>
          <div className="text-slate-500 text-xs uppercase tracking-[0.2em]">
            © 2026 Semantic Intelligence Hub
          </div>
        </div>
      </footer>
    </div>
  );
}
