import axios from "axios";
const api = axios.create({
    baseURL: "https://hrms-backend-wu2i.onrender.com/"
});

export default api;