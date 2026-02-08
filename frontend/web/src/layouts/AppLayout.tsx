import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo.png";

interface AppLayoutProps {
  children: React.ReactNode;
}

export default function AppLayout({ children }: AppLayoutProps) {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      {/* Header */}
      <header className="flex items-center gap-3 px-6 py-3 border-b bg-white">
        <img src={logo} alt="Mutuelle Logo" className="h-12" />
        <h1 className="text-lg font-semibold">
          Mutuelle Main de Compassion UMOJA
        </h1>
      </header>

      <div className="flex flex-1">
        {/* Sidebar */}
        <aside className="w-64 bg-gray-100 p-6 flex-shrink-0">
          <h2 className="font-bold text-lg mb-4">Menu</h2>
          <nav className="flex flex-col gap-2">
            <Link to="/dashboard" className="hover:underline">Dashboard</Link>
            <Link to="/members" className="hover:underline">Membres</Link>
            <Link to="/notifications" className="hover:underline">Notifications</Link>
            <Link to="/responsables" className="hover:underline">Responsables</Link>
          </nav>
        </aside>

        {/* Main content */}
        <main className="flex-1 p-6">{children}</main>
      </div>
    </div>
  );
}
