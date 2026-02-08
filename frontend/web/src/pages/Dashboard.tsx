import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold mb-6">
        Tableau de bord
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Membres */}
        <Link
          to="/members"
          className="bg-white p-6 rounded shadow hover:shadow-md transition"
        >
          <h2 className="text-lg font-semibold mb-2">Membres</h2>
          <p className="text-gray-600">
            Gérer les membres de la mutuelle
          </p>
        </Link>

        {/* Notifications */}
        <Link
          to="/notifications"
          className="bg-white p-6 rounded shadow hover:shadow-md transition"
        >
          <h2 className="text-lg font-semibold mb-2">Notifications</h2>
          <p className="text-gray-600">
            Envoyer et consulter les notifications
          </p>
        </Link>

        {/* Responsables */}
        <Link
          to="/responsables"
          className="bg-white p-6 rounded shadow hover:shadow-md transition"
        >
          <h2 className="text-lg font-semibold mb-2">Responsables</h2>
          <p className="text-gray-600">
            Gestion des responsables
          </p>
        </Link>
      </div>
    </div>
  );
}
