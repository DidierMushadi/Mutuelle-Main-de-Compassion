import { useState } from "react";
import { login } from "../../services/auth.service";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    try {
      const res = await login(username, password);
      localStorage.setItem("access_token", res.access_token);
      navigate("/dashboard");
    } catch {
      setError("Identifiants incorrects");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded shadow w-80 space-y-4"
      >
        <h1 className="text-xl font-bold text-center">Connexion</h1>

        {error && <p className="text-red-600">{error}</p>}

        <input
          className="w-full border p-2 rounded"
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <input
          type="password"
          className="w-full border p-2 rounded"
          placeholder="Mot de passe"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button className="w-full bg-blue-600 text-white py-2 rounded">
          Se connecter
        </button>
      </form>
    </div>
  );
}
