// src/services/members.service.ts
import api from "../api/client";

// Interface d'un membre
export interface Member {
  id: number;
  name: string;
  phone: string;
}

// ⚡ Version API réelle
export async function getMembers(): Promise<Member[]> {
  try {
    const res = await api.get("/members"); // endpoint à adapter selon ton backend
    return res.data;
  } catch (err) {
    console.error("Erreur lors de la récupération des membres", err);
    return [];
  }
}

// 🧪 Version mockée pour tester sans backend
export async function getMembersMock(): Promise<Member[]> {
  return new Promise((resolve) =>
    setTimeout(
      () =>
        resolve([
          { id: 1, name: "Jean Dupont", phone: "0600000000" },
          { id: 2, name: "Marie Curie", phone: "0611111111" },
          { id: 3, name: "Paul Martin", phone: "0622222222" },
        ]),
      500
    )
  );
}

// ✅ Fonction pour créer un nouveau membre
export async function createMember(member: { name: string; phone: string }): Promise<Member> {
  try {
    const res = await api.post("/members", member); // endpoint à adapter selon ton backend
    return res.data;
  } catch (err) {
    console.error("Erreur lors de la création du membre", err);
    throw err;
  }
}
