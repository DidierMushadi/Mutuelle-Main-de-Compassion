// src/pages/members/MembersPage.tsx
import { useEffect, useState } from "react";
import { getMembers, Member } from "../../services/members.service";
import MembersList from "./MembersList";      // Liste réutilisable
import MemberCreate from "./MemberCreate";    // Formulaire création

export default function MembersPage() {
  const [members, setMembers] = useState<Member[]>([]);
  const [loading, setLoading] = useState(true);

  // Récupérer la liste des membres depuis l'API
  useEffect(() => {
    getMembers()
      .then(setMembers)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p className="p-4">Chargement des membres...</p>;

  return (
    <div className="p-4">
      {/* Formulaire création membre */}
      <h2 className="text-xl font-semibold mb-4">Créer un nouveau membre</h2>
      <MemberCreate onNewMember={(m: Member) => setMembers([...members, m])} />

      {/* Liste des membres */}
      <h2 className="text-xl font-semibold mb-4 mt-6">Liste des membres</h2>
      <MembersList members={members} />
    </div>
  );
}
