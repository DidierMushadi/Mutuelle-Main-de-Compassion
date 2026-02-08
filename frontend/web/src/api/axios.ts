// src/api/axios.ts
import axios from "axios";

// L'URL de l'API est lue depuis les variables d'environnement
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:8000",
});

export default api;
