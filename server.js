import http from "http";
import app from "./app.js";

const server = http.createServer((req, res) => {
    app(req, res);
});

server.listen(5000, () => {
  console.log("Server is running on http://localhost:5000");
});