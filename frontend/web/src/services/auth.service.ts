import apiClient from "../api/client";

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export async function login(
  username: string,
  password: string
): Promise<LoginResponse> {
  const res = await apiClient.post("/auth/login", {
    username,
    password,
  });

  return res.data;
}

export function logout() {
  localStorage.removeItem("access_token");
}

export function isAuthenticated(): boolean {
  return !!localStorage.getItem("access_token");
}
