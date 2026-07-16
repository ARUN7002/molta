import { FaMicrochip } from "react-icons/fa6";

function App() {
  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6">
      <div className="w-full max-w-3xl text-center">

        <div className="flex items-center justify-center gap-4 mb-6">
          <FaMicrochip className="text-6xl text-cyan-400" />
          <h1 className="text-6xl font-extrabold tracking-wide text-white">
            MOLTA
          </h1>
        </div>

        <p className="mt-4 text-xl text-slate-300">
          AI Software Modernization Assistant
        </p>

        <p className="mt-3 text-slate-400">
          Analyze legacy repositories using AI and generate
          modernization recommendations in minutes.
        </p>

        <div className="mt-10">
          <input
            type="text"
            placeholder="Paste your GitHub repository URL..."
            className="w-full rounded-xl border border-slate-700 bg-slate-900 p-4 text-white outline-none focus:border-blue-500"
          />
        </div>

        <button
          className="mt-6 rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white transition hover:bg-blue-700"
        >
          Analyze Repository
        </button>

      </div>
    </div>
  );
}

export default App;
