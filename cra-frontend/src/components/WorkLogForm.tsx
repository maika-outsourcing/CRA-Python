/*import React, { useState } from "react";
import "./WorkLogForm.css";

const WorkLogForm: React.FC = () => {
  const [collaborator, setCollaborator] = useState("");
  const [project, setProject] = useState("");
  const [task, setTask] = useState("");
  const [hours, setHours] = useState("");
  const [date, setDate] = useState("");
  const [status, setStatus] = useState("En cours");
  const [description, setDescription] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const workLog = {
      collaborator,
      project,
      task,
      hours: parseFloat(hours),
      date,
      status,
      description,
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/work_logs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(workLog),
      });

      if (response.ok) {
        alert("WorkLog ajouté avec succès !");
        // reset du formulaire
        setCollaborator("");
        setProject("");
        setTask("");
        setHours("");
        setDate("");
        setStatus("En cours");
        setDescription("");
      } else {
        alert("Erreur lors de l'ajout du WorkLog");
      }
    } catch (error) {
      console.error(error);
      alert("Impossible de contacter l'API");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ajouter un WorkLog</h2>

      <label>Collaborateur :</label>
      <input
        type="text"
        value={collaborator}
        onChange={(e) => setCollaborator(e.target.value)}
        required
      />

      <label>Projet :</label>
      <input
        type="text"
        value={project}
        onChange={(e) => setProject(e.target.value)}
        required
      />

      <label>Tâche :</label>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        required
      />

      <label>Heures :</label>
      <input
        type="number"
        value={hours}
        onChange={(e) => setHours(e.target.value)}
        required
      />

      <label>Date :</label>
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
        required
      />

      <label>Statut :</label>
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="En cours">En cours</option>
        <option value="Terminé">Terminé</option>
        <option value="En attente">En attente</option>
      </select>

      <label>Description :</label>
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <button type="submit">Enregistrer</button>
    </form>
  );
};

export default WorkLogForm;*/

import React, { useState, useEffect } from "react";
import "./WorkLogForm.css";

const WorkLogForm: React.FC = () => {
  const [collaborators, setCollaborators] = useState<{id: number, name: string}[]>([]);
  const [collaboratorId, setCollaboratorId] = useState<number | null>(null);
  const [project, setProject] = useState("");
  const [task, setTask] = useState("");
  const [hours, setHours] = useState("");
  const [date, setDate] = useState("");
  const [status, setStatus] = useState("En cours");
  const [description, setDescription] = useState("");

  // Charger les collaborateurs depuis l’API
  useEffect(() => {
    fetch("http://127.0.0.1:8000/collaborators")
      .then(res => res.json())
      .then(data => setCollaborators(data));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!collaboratorId) {
      alert("Choisis un collaborateur !");
      return;
    }

    const workLog = {
      collaborator_id: collaboratorId,
      project,
      task,
      hours: parseFloat(hours),
      date,
      status,
      description,
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/work_logs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(workLog),
      });

      if (response.ok) {
        alert("WorkLog ajouté avec succès !");
        // reset du formulaire
        setCollaboratorId(null);
        setProject("");
        setTask("");
        setHours("");
        setDate("");
        setStatus("En cours");
        setDescription("");
      } else {
        alert("Erreur lors de l'ajout du WorkLog");
      }
    } catch (error) {
      console.error(error);
      alert("Impossible de contacter l'API");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ajouter un WorkLog</h2>

      <label>Collaborateur :</label>
      <select
        value={collaboratorId ?? ""}
        onChange={(e) => setCollaboratorId(Number(e.target.value))}
        required
      >
        <option value="">-- Choisir --</option>
        {collaborators.map(c => (
          <option key={c.id} value={c.id}>{c.name}</option>
        ))}
      </select>

      <label>Projet :</label>
      <input
        type="text"
        value={project}
        onChange={(e) => setProject(e.target.value)}
        required
      />

      <label>Tâche :</label>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        required
      />

      <label>Heures :</label>
      <input
        type="number"
        value={hours}
        onChange={(e) => setHours(e.target.value)}
        required
      />

      <label>Date :</label>
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
        required
      />

      <label>Statut :</label>
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="En cours">En cours</option>
        <option value="Terminé">Terminé</option>
        <option value="En attente">En attente</option>
      </select>

      <label>Description :</label>
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <button type="submit">Enregistrer</button>
    </form>
  );
};

export default WorkLogForm;


