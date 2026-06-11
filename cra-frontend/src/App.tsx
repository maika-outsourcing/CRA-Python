import { useEffect, useState } from "react";
import WorkLogForm from "./components/WorkLogForm";

interface WorkLog {
  id: number;
  collaborator_id: number;
  collaborator_name?: string;
  project: string;
  task: string;
  hours: number;
  date: string;
  status: string;
  description?: string;
}

function App() {
  const [logs, setLogs] = useState<WorkLog[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/work_logs")
      .then(res => res.json())
      .then(data => setLogs(data));
  }, []);

  return (
    <div className="App">
      <h1>📋 Compte Rendu d'Activité</h1>
        <WorkLogForm />

        <h2>Liste des WorkLogs</h2>

      <table style={{ margin: "20px auto", borderCollapse: "collapse", width: "90%" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Collaborateur</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Projet</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Tâche</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Heures</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Date</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Statut</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Description</th>
          </tr>
        </thead>
        <tbody>
          {logs.map(log => (
            <tr key={log.id}>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.collaborator_name}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.project}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.task}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.hours}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.date}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.status}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{log.description}</td>
              
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}

export default App;
