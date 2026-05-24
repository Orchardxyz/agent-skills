// Reusable player logic for single-file LeetCode walkthrough pages.
// Adapt variable names and render hooks, but preserve the overall behavior.

let currentFrameIndex = 0;
let playing = false;
let timer = null;
let speed = 1800;
let theme = localStorage.getItem("leetcode-visualization-theme") || "dark";

function nextFrame(totalFrames, render) {
  if (currentFrameIndex < totalFrames - 1) {
    currentFrameIndex += 1;
    render();
  }
  if (currentFrameIndex === totalFrames - 1) {
    pause(render);
  }
}

function prevFrame(render) {
  if (currentFrameIndex > 0) {
    currentFrameIndex -= 1;
    render();
  }
}

function restart(render) {
  pause(render);
  currentFrameIndex = 0;
  render();
}

function togglePlay(totalFrames, render) {
  if (playing) {
    pause(render);
  } else {
    play(totalFrames, render);
  }
}

function play(totalFrames, render) {
  playing = true;
  render();
  timer = setInterval(() => {
    if (currentFrameIndex < totalFrames - 1) {
      currentFrameIndex += 1;
      render();
    } else {
      pause(render);
    }
  }, speed);
}

function pause(render) {
  playing = false;
  if (timer) {
    clearInterval(timer);
  }
  timer = null;
  render();
}

function setSpeed(nextSpeed, render) {
  speed = nextSpeed;
  document.getElementById("spSlow")?.classList.toggle("active", speed === 3000);
  document.getElementById("spNormal")?.classList.toggle("active", speed === 1800);
  document.getElementById("spFast")?.classList.toggle("active", speed === 800);
  if (playing) {
    pause(render);
    play(window.frames.length, render);
  }
}

function applyTheme() {
  const isLight = theme === "light";
  document.body.classList.toggle("theme-light", isLight);
  document.body.classList.toggle("theme-dark", !isLight);
}

function toggleTheme() {
  theme = theme === "dark" ? "light" : "dark";
  localStorage.setItem("leetcode-visualization-theme", theme);
  applyTheme();
}
