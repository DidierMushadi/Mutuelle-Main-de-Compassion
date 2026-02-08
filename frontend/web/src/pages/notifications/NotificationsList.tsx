import { Link } from "react-router-dom";

export default function NotificationsList() {
  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">Notifications</h1>
        <Link
          to="/notifications/create"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Nouvelle notification
        </Link>
      </div>

      <p className="text-gray-600">Aucune notification.</p>
    </div>
  );
}
