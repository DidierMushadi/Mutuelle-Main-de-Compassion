import { useState } from "react";
import api from "../../api/client";
import { useNavigate } from "react-router-dom";

export default function ResponsableCreate() {
  const [nom, setNom] = useState("");
  const [telephone, setTelephone] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      await api.post("/responsables", {
        nom,
        telephone,
      });

      navigate("/responsables"); // retour liste
    } catch (e) {
      console.error("Erreur création :", e);
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-xl font-semibold mb-4">Nouveau responsable</h2>

      <form onSubmit={handleSubmit} className="space-y-3">
        <input
          className="w-full p-2 border rounded"
          placeholder="Nom complet"
          value={nom}
          onChange={(e) => setNom(e.target.value)}
          required
        />

        <input
          className="w-full p-2 border rounded"
          placeholder="Téléphone"
          value={telephone}
          onChange={(e) => setTelephone(e.target.value)}
          required
        />

        <button
          type="submit"
          className="w-full bg-blue-600 text-white p-2 rounded"
        >
          Enregistrer
        </button>
      </form>
    </div>
  );
}
