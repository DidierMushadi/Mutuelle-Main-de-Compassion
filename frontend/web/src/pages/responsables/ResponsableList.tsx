import { useEffect, useState } from "react";
import api from "../../api/client";
import { Link } from "react-router-dom";

export default function ResponsableList() {
  const [responsables, setResponsables] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const res = await api.get("/responsables");
      setResponsables(res.data);
    } catch (e) {
      console.error("Erreur lors du chargement :", e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDelete = async (id: number) => {
    if (!confirm("Supprimer ce responsable ?")) return;

    try {
      await api.delete(`/responsables/${id}`);
      setResponsables((prev) => prev.filter((r) => r.id !== id));
    } catch (e) {
      console.error("Erreur suppression :", e);
    }
  };

  if (loading) return <p>Chargement…</p>;

  return (
    <div className="p-4">
      <div className="flex justify-between mb-4">
        <h2 className="text-xl font-semibold">Liste des responsables</h2>

        <Link
          to="/responsables/create"
          className="px-4 py-2 bg-blue-600 text-white rounded"
        >
          + Nouveau
        </Link>
      </div>

      <table className="w-full border border-gray-300">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">ID</th>
            <th className="p-2 border">Nom</th>
            <th className="p-2 border">Téléphone</th>
            <th className="p-2 border">Actions</th>
          </tr>
        </thead>
        <tbody>
          {responsables.map((r) => (
            <tr key={r.id} className="border">
              <td className="p-2 border">{r.id}</td>
              <td className="p-2 border">{r.nom}</td>
              <td className="p-2 border">{r.telephone}</td>
              <td className="p-2 border flex gap-2">
                <button
                  onClick={() => handleDelete(r.id)}
                  className="px-2 py-1 bg-red-600 text-white rounded"
                >
                  Supprimer
                </button>

                <Link
                  to={`/responsables/edit/${r.id}`}
                  className="px-2 py-1 bg-green-600 text-white rounded"
                >
                  Modifier
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
