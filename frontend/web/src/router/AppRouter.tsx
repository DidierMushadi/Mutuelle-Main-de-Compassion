import { Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/auth/Login";
import Dashboard from "../pages/Dashboard";
import MembersPage from "../pages/members/MembersPage";
import CotisationsPage from "../pages/cotisations/CotisationsPage";
import RapportsPage from "../pages/rapports/RapportsPage";
import NotFoundPage from "../pages/NotFoundPage";

import RequireAuth from "../auth/RequireAuth";
import AppLayout from "../layouts/AppLayout";

export default function AppRouter() {
  return (
    <Routes>
      {/* Page publique */}
      <Route path="/login" element={<Login />} />

      {/* Redirection racine */}
      <Route path="/" element={<Navigate to="/dashboard" replace />} />

      {/* Pages protégées */}
      <Route
        path="/dashboard"
        element={
          <RequireAuth>
            <AppLayout>
              <Dashboard />
            </AppLayout>
          </RequireAuth>
        }
      />

      <Route
        path="/membres"
        element={
          <RequireAuth>
            <AppLayout>
              <MembersPage />
            </AppLayout>
          </RequireAuth>
        }
      />

      <Route
        path="/cotisations"
        element={
          <RequireAuth>
            <AppLayout>
              <CotisationsPage />
            </AppLayout>
          </RequireAuth>
        }
      />

      <Route
        path="/rapports"
        element={
          <RequireAuth>
            <AppLayout>
              <RapportsPage />
            </AppLayout>
          </RequireAuth>
        }
      />

      {/* 404 */}
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
