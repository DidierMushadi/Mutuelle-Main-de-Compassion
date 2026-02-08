import { Member } from "../../services/members.service";

export default function MembersList({ members }: { members: Member[] }) {
  return (
    <ul className="space-y-2">
      {members.map((m) => (
        <li key={m.id} className="border p-2 rounded flex justify-between">
          <span>{m.name}</span>
          <span className="text-gray-500">{m.phone}</span>
        </li>
      ))}
    </ul>
  );
}
