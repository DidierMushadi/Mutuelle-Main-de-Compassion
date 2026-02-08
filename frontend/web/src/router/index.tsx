import { Routes, Route } from "react-router-dom";

// Pages publiques
import Login from "../pages/auth/Login";

// Pages protégées
import Dashboard from "../pages/Dashboard";
import MembersPage from "../pages/members/MembersPage";
import NotificationsPage from "../pages/notifications/NotificationsPage";
import ResponsablesPage from "../pages/responsables/ResponsablesPage";

// Wrapper pour l'authentification
import RequireAuth from "../auth/RequireAuth";

// Page 404
import NotFoundPage from "../pages/NotFoundPage";

export default function AppRouter() {
  return (
    <Routes>
      {/* Page publique */}
      <Route path="/login" element={<Login />} />

      {/* Routes protégées */}
      <Route
        path="/dashboard"
        element={
          <RequireAuth>
            <Dashboard />
          </RequireAuth>
        }
      />
      <Route
        path="/members"
        element={
          <RequireAuth>
            <MembersPage />
          </RequireAuth>
        }
      />
      <Route
        path="/notifications"
        element={
          <RequireAuth>
            <NotificationsPage />
          </RequireAuth>
        }
      />
      <Route
        path="/responsables"
        element={
          <RequireAuth>
            <ResponsablesPage />
          </RequireAuth>
        }
      />

      {/* Page 404 */}
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
