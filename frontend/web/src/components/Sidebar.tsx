// src/components/Sidebar.tsx
import React from "react";
import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 min-h-screen p-4">
      <h2 className="font-bold text-lg mb-4">Menu</h2>
      <nav className="flex flex-col gap-2">
        <Link to="/dashboard" className="hover:underline">Dashboard</Link>
        <Link to="/members" className="hover:underline">Membres</Link>
        <Link to="/notifications" className="hover:underline">Notifications</Link>
        <Link to="/responsables" className="hover:underline">Responsables</Link>
      </nav>
    </aside>
  );
}
