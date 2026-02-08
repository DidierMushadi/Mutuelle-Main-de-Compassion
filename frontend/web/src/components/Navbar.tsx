import { NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <aside className="w-64 bg-white border-r">
      <nav className="flex flex-col p-4 gap-2">

        <NavLink
          to="/"
          end
          className={({ isActive }) =>
            `px-4 py-2 rounded transition ${
              isActive
                ? "bg-green-600 text-white"
                : "text-gray-700 hover:bg-gray-100"
            }`
          }
        >
          Tableau de bord
        </NavLink>

        <NavLink
          to="/membres"
          className={({ isActive }) =>
            `px-4 py-2 rounded transition ${
              isActive
                ? "bg-green-600 text-white"
                : "text-gray-700 hover:bg-gray-100"
            }`
          }
        >
          Membres
        </NavLink>

        <NavLink
          to="/cotisations"
          className={({ isActive }) =>
            `px-4 py-2 rounded transition ${
              isActive
                ? "bg-green-600 text-white"
                : "text-gray-700 hover:bg-gray-100"
            }`
          }
        >
          Cotisations
        </NavLink>

        <NavLink
          to="/rapports"
          className={({ isActive }) =>
            `px-4 py-2 rounded transition ${
              isActive
                ? "bg-green-600 text-white"
                : "text-gray-700 hover:bg-gray-100"
            }`
          }
        >
          Rapports
        </NavLink>

      </nav>
    </aside>
  );
}
