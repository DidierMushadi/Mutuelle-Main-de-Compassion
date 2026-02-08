// src/api/auth.api.ts

export const login = async (username: string, password: string) => {
  // Ici tu peux mettre un vrai appel API plus tard
  console.log("login function called", username, password);
  return { success: true, token: "fake-token" };
};

export const logout = () => {
  console.log("logout function called");
};
