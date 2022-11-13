import axios from 'axios';

const apiService = axios.create({
  baseURL: "http://127.0.0.1:8001",
  timeout: 10000
});

export default apiService;
