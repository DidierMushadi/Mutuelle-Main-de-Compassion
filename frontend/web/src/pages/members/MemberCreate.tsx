import { useState } from "react";
import { createMember, Member } from "../../services/members.service";

interface Props {
  onNewMember: (m: Member) => void;
}

export default function MemberCreate({ onNewMember }: Props) {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const newMember = await createMember({ name, phone });
    onNewMember(newMember);
    setName("");
    setPhone("");
  };

  return (
    <form className="space-y-4 max-w-md" onSubmit={handleSubmit}>
      <input
        className="w-full border p-2 rounded"
        placeholder="Nom complet"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        className="w-full border p-2 rounded"
        placeholder="Téléphone"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
        required
      />

      <button className="bg-green-600 text-white px-4 py-2 rounded">
        Enregistrer
      </button>
    </form>
  );
}
