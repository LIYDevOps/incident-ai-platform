const API_BASE = "http://localhost:8000";
/*
async function checkHealth() {
  const res = await fetch(`${API_BASE}/health`);
  const data = await res.json();
  document.getElementById("healthResult").textContent =
    JSON.stringify(data, null, 2);
} */

function validateIncident(data) {
  const errors = [];

  if (!data.title || data.title.trim().length < 5) {
    errors.push("Title is required (min 5 characters).");
  }

  if (!data.priority) {
    errors.push("Priority is mandatory.");
  }

  if (!data.application_ci) {
    errors.push("Application CI is mandatory.");
  }

  return errors;
}

async function submitIncident(event) {
  event.preventDefault();

  // Collect data
  const incident = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    priority: document.getElementById("priority").value,
    application_ci: document.getElementById("application_ci").value,
    reported_by: document.getElementById("reported_by").value
  };

  // Pre-check validation
  const errors = validateIncident(incident);

  document.getElementById("errorResult").textContent = "";
  document.getElementById("incidentResult").textContent = "";

  if (errors.length > 0) {
    document.getElementById("errorResult").textContent =
      errors.join("\n");
    return;
  }

  // API call
  try {
    const response = await fetch(`${API_BASE}/api/incidents`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(incident)
    });

    if (!response.ok) {
      throw new Error("Failed to create incident");
    }

    const result = await response.json();
    document.getElementById("incidentResult").textContent =
      JSON.stringify(result, null, 2);

  } catch (err) {
    document.getElementById("errorResult").textContent =
      err.message;
  }
}

async function runPrecheck() {
  const payload = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    priority: document.getElementById("priority").value,
    application_ci: document.getElementById("application_ci").value,
    reported_by: document.getElementById("reported_by").value
  };

  document.getElementById("aiHints").textContent = "";

  const response = await fetch(`${API_BASE}/api/incidents/precheck`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const result = await response.json();

  if (result.hint_count === 0) {
    document.getElementById("aiHints").textContent =
      "✅ No issues found. Ready to create incident.";
  } else {
    document.getElementById("aiHints").textContent =
      "⚠ AI Suggestions:\n- " + result.hints.join("\n- ");
  }
}