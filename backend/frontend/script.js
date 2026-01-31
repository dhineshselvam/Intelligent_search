document.getElementById("search-btn").addEventListener("click", async () => {
  const query = document.getElementById("query").value.trim();
  if (!query) return alert("Please enter a search query.");

  const res = await fetch("/search", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: query, k: 5 })
  });

  const data = await res.json();

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = ""; // clear previous results

  if (data.length === 0) {
    resultsDiv.innerHTML = "<p>No papers found.</p>";
    return;
  }

  data.forEach((paper, i) => {
    const div = document.createElement("div");
    div.className = "paper";

    div.innerHTML = `
      <h3>${i + 1}. ${paper.title}</h3>
      <p>${paper.abstract}</p>
    `;

    resultsDiv.appendChild(div);
  });
});
