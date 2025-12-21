async function reviewCode() {
  const code = document.getElementById("code").value;
  const language = document.getElementById("language").value;

  if (!code.trim()) {
    alert("Please paste some code first.");
    return;
  }

  document.getElementById("loader").classList.remove("hidden");
  document.getElementById("llmOutput").innerText = "";
  document.getElementById("staticOutput").innerText = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/review", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        code: code,
        language: language
      })
    });

    const data = await response.json();

    document.getElementById("llmOutput").innerText =
      data.llm_review || "No AI feedback received.";

    document.getElementById("staticOutput").innerText =
      data.static_analysis || "No static analysis output.";

  } catch (error) {
    alert("Error connecting to backend.");
    console.error(error);
  }

  document.getElementById("loader").classList.add("hidden");
}
