// src/services/notifications.service.ts
import api from "../api/client";

export interface Notification {
  id: number;
  title: string;
  date: string;
}

// Version API réelle
export async function getNotifications(): Promise<Notification[]> {
  try {
    const res = await api.get("/notifications"); // endpoint à adapter
    return res.data;
  } catch (err) {
    console.error("Erreur lors de la récupération des notifications", err);
    return [];
  }
}

// Version mockée pour tester sans backend
export async function getNotificationsMock(): Promise<Notification[]> {
  return new Promise((resolve) =>
    setTimeout(
      () =>
        resolve([
          { id: 1, title: "Réunion demain 10h", date: "2026-01-15" },
          { id: 2, title: "Nouvelle cotisation disponible", date: "2026-01-12" },
        ]),
      500
    )
  );
}
