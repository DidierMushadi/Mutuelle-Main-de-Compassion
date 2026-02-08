// src/pages/notifications/NotificationsPage.tsx
import { useEffect, useState } from "react";
import {
  getNotifications,
  Notification,
} from "../../services/notifications.service";

export default function NotificationsPage() {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getNotifications()
      .then(setNotifications)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p className="p-4">Chargement des notifications...</p>;

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">
        Liste des notifications
      </h2>

      {notifications.length === 0 ? (
        <p>Aucune notification disponible.</p>
      ) : (
        <ul className="space-y-2">
          {notifications.map((n) => (
            <li
              key={n.id}
              className="border p-2 rounded flex justify-between"
            >
              <span>{n.title}</span>
              <span className="text-gray-500">{n.date}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// 🔒 force TypeScript à traiter le fichier comme module
export {};
