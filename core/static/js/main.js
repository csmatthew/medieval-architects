const toggleInput = document.getElementById("cb1");
const themeToggle = document.getElementById("theme-toggle");

function applyTheme(theme) {
    const normalizedTheme = theme === "dark" ? "dark" : "light";

    document.documentElement.setAttribute("data-theme", normalizedTheme);
    document.body.classList.toggle("day-background", normalizedTheme === "light");

    if (toggleInput) {
        toggleInput.checked = normalizedTheme === "dark";
    }

    localStorage.setItem("theme", normalizedTheme);
}

function initializeTheme() {
    const savedTheme = localStorage.getItem("theme");
    const preferredTheme = window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";

    applyTheme(savedTheme || preferredTheme);
}

if (themeToggle && toggleInput) {
    initializeTheme();

    toggleInput.addEventListener("change", (event) => {
        applyTheme(event.target.checked ? "dark" : "light");
    });
}
