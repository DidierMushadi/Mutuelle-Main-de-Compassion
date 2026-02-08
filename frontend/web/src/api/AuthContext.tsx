import { createContext, useContext, useState, ReactNode } from "react";
import { login as loginApi } from "../api/auth.api";

interface AuthContextType {
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("access_token")
  );

  async function login(email: string, password: string) {
    const data = await loginApi(email, password);

    // ✅ CORRECTION ICI
    localStorage.setItem("access_token", data.token);
    setToken(data.token);
  }

  function logout() {
    localStorage.removeItem("access_token");
    setToken(null);
  }

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return ctx;
}
