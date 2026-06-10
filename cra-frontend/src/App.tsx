import { useEffect, useState } from "react";

interface WorkLog {
  id: number;
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
    <div style={{ padding: "20px" }}>
      <h1>📋 Mes Work Logs</h1>
      <ul>
        {logs.map(log => (
          <li key={log.id}>
            <strong>{log.project}</strong> – {log.task} ({log.status})  
            → {log.hours}h le {log.date}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
