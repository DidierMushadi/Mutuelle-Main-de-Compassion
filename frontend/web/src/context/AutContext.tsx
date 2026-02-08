import React, { createContext, useState, ReactNode } from "react";
import { login as loginApi, logout as logoutApi } from "../api/auth.api";

interface AuthContextType {
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  token: string | null;
}

export const AuthContext = createContext<AuthContextType>({
  login: async () => {},
  logout: () => {},
  token: null,
});

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [token, setToken] = useState<string | null>(null);

  const login = async (username: string, password: string) => {
    const result = await loginApi(username, password);
    if (result.success) setToken(result.token);
  };

  const logout = () => {
    logoutApi();
    setToken(null);
  };

  return (
    <AuthContext.Provider value={{ login, logout, token }}>
      {children}
    </AuthContext.Provider>
  );
};
