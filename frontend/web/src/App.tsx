import { AuthProvider } from "./auth/AuthContext";
import AppRouter from "./router/AppRouter";
import Navbar from "./components/Navbar";
import logo from "./assets/logo.png";

export default function App() {
  return (
    <AuthProvider>
      <div className="min-h-screen flex bg-gray-50">
        {/* Navbar verticale */}
        <Navbar />

        {/* Zone principale */}
        <div className="flex-1 flex flex-col">
          {/* Header */}
          <header className="flex items-center justify-center gap-3 px-6 py-4 border-b bg-white">
            <img
              src={logo}
              alt="Mutuelle Main de Compassion UMOJA"
              className="h-10" // ≈ -20%
            />
            <h1 className="text-lg font-semibold">
              Mutuelle Main de Compassion UMOJA
            </h1>
          </header>

          {/* Contenu */}
          <main className="flex-1 p-6">
            <AppRouter />
          </main>
        </div>
      </div>
    </AuthProvider>
  );
}
