import { useState } from "react";
import { FaMicrochip } from "react-icons/fa6";

function App() {
  const [repository, setRepository] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const analyzeRepository = async () => {
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          repository: repository,
        }),
      });

      const data = await response.json();

      setResult(data.message);
    } catch (error) {
      setResult("Failed to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6">
      <div className="w-full max-w-3xl text-center">

        <div className="flex items-center justify-center gap-4 mb-6">
          <FaMicrochip className="text-6xl text-cyan-400" />
          <h1 className="text-6xl font-extrabold text-white">
            MOLTA
          </h1>
        </div>

        <p className="text-xl text-slate-300">
          AI Software Modernization Assistant
        </p>

        <p className="mt-3 text-slate-400">
          Analyze legacy repositories using AI and generate modernization recommendations in minutes.
        </p>

        <div className="mt-10">
          <input
  type="text"
  value={repository}
  onChange={(e) => setRepository(e.target.value)}
  onKeyDown={(e) => {
    if (e.key === "Enter") {
      analyzeRepository();
    }
  }}
  placeholder="Paste your GitHub repository URL..."
  className="w-full rounded-xl border border-slate-700 bg-slate-900 p-4 text-white outline-none focus:border-blue-500"
/>
        </div>

        <button
          onClick={analyzeRepository}
          className="mt-6 rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white transition hover:bg-blue-700"
        >
          {loading ? "Analyzing..." : "Analyze Repository"}
        </button>

        {result && (
          <div className="mt-8 rounded-xl bg-slate-900 p-4 text-cyan-400">
            {result}
          </div>
        )}

      </div>
    </div>
  );
}

export default App;