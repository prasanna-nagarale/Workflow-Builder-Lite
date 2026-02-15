// Workflow Builder
async function createWorkflow() {
    const name = document.getElementById("name").value.trim();
    const steps = Array.from(document.querySelectorAll("input[type=checkbox]:checked"))
        .map(c => c.value);

    if (!name) {
        alert("⚠️ Please enter a workflow name");
        return;
    }

    if (steps.length === 0) {
        alert("⚠️ Please select at least one step");
        return;
    }

    try {
        const response = await fetch("/api/workflows/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, steps })
        });

        if (response.ok) {
            alert("✅ Workflow created successfully!");
            document.getElementById("name").value = "";
            document.querySelectorAll("input[type=checkbox]").forEach(cb => cb.checked = false);
        } else {
            alert("❌ Failed to create workflow");
        }
    } catch (error) {
        alert("❌ Error: " + error.message);
    }
}

// Load workflows into dropdown
async function loadWorkflows() {
    try {
        const response = await fetch("/api/workflows/");
        const workflows = await response.json();

        const select = document.getElementById("workflowSelect");
        select.innerHTML = "";

        if (workflows.length === 0) {
            const option = document.createElement("option");
            option.text = "No workflows yet - create one first";
            option.disabled = true;
            select.appendChild(option);
            return;
        }

        workflows.forEach(w => {
            const option = document.createElement("option");
            option.value = w.id;
            option.text = `${w.name} (${w.steps.length} steps)`;
            select.appendChild(option);
        });
    } catch (error) {
        console.error("Failed to load workflows:", error);
    }
}

// Run workflow
async function runWorkflow() {
    const text = document.getElementById("text").value.trim();
    const workflowId = document.getElementById("workflowSelect").value;

    if (!text) {
        alert("⚠️ Please enter some text to process");
        return;
    }

    const loading = document.getElementById("loading");
    const results = document.getElementById("results");
    const runBtn = document.querySelector("button");

    loading.style.display = "block";
    results.innerHTML = "";
    runBtn.disabled = true;

    try {
        const response = await fetch("/api/runs/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                workflow_id: parseInt(workflowId),
                input_text: text
            })
        });

        const data = await response.json();
        loading.style.display = "none";
        runBtn.disabled = false;

        // Display results
        for (const [step, output] of Object.entries(data)) {
            const box = document.createElement("div");
            box.className = "output-box";
            box.innerHTML = `
                <h3>📌 ${step}</h3>
                <pre>${output}</pre>
            `;
            results.appendChild(box);
        }
    } catch (error) {
        loading.style.display = "none";
        runBtn.disabled = false;
        alert("❌ Error: " + error.message);
    }
}

// Load run history
async function loadHistory() {
    try {
        const response = await fetch("/api/runs/history");
        const runs = await response.json();

        const container = document.getElementById("history");
        container.innerHTML = "";

        if (runs.length === 0) {
            container.innerHTML = "<p>No runs yet. Create a workflow and run it!</p>";
            return;
        }

        runs.forEach(run => {
            const item = document.createElement("div");
            item.className = "history-item";
            item.innerHTML = `
                <h3>${run.workflow_name || "Workflow #" + run.workflow_id}</h3>
                <p><strong>Input:</strong> ${run.input_preview}</p>
                <p><small>📅 ${new Date(run.created_at).toLocaleString()}</small></p>
            `;
            container.appendChild(item);
        });
    } catch (error) {
        console.error("Failed to load history:", error);
    }
}

// Load status
async function loadStatus() {
    try {
        const response = await fetch("/api/status");
        const data = await response.json();

        const container = document.getElementById("status");
        container.innerHTML = "";

        const statusGrid = document.createElement("div");
        statusGrid.className = "status-grid";

        for (const [key, value] of Object.entries(data)) {
            const item = document.createElement("div");
            item.className = "status-item";
            
            const label = key.replace(/_/g, " ").replace(/\b\w/g, l => l.toUpperCase());
            const statusClass = value === "OK" || value === true ? "status-ok" : "status-error";
            const displayValue = typeof value === "boolean" ? (value ? "✅ Loaded" : "❌ Missing") : value;
            
            item.innerHTML = `
                <span><strong>${label}:</strong></span>
                <span class="${statusClass}">${displayValue}</span>
            `;
            statusGrid.appendChild(item);
        }

        container.appendChild(statusGrid);
    } catch (error) {
        console.error("Failed to load status:", error);
    }
}