// Reusable dual-mode code-panel builder.
// Preserve indentation by rendering trusted source lines with textContent.

function buildCodePanel(codeLines, containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";

  codeLines.forEach((line, index) => {
    const row = document.createElement("div");
    row.className = "code-line";
    row.id = "cl" + index;

    const lineNumber = document.createElement("span");
    lineNumber.className = "code-line-number inline-block w-7 text-right mr-3 text-[10px] md:text-xs select-none";
    lineNumber.textContent = index + 1;
    row.appendChild(lineNumber);

    const codeText = document.createElement("span");
    codeText.textContent = line || " ";
    row.appendChild(codeText);

    container.appendChild(row);
  });
}

function buildDualCodePanels(realCodeLines, pseudoCodeLines) {
  buildCodePanel(realCodeLines, "realCodePanel");
  buildCodePanel(pseudoCodeLines, "pseudoCodePanel");
  setCodeMode("real");
}

function setCodeMode(mode) {
  const realPanel = document.getElementById("realCodePanel");
  const pseudoPanel = document.getElementById("pseudoCodePanel");
  const realBtn = document.getElementById("modeReal");
  const pseudoBtn = document.getElementById("modePseudo");

  const showReal = mode === "real";
  realPanel?.classList.toggle("hidden", !showReal);
  pseudoPanel?.classList.toggle("hidden", showReal);
  realBtn?.classList.toggle("active", showReal);
  pseudoBtn?.classList.toggle("active", !showReal);
}
