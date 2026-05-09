// mermaid-init.js
// Initializes Mermaid diagrams with proper theme matching (light/dark mode)
// Runs AFTER Mermaid CDN script is loaded in mkdocs.yml

document.addEventListener("DOMContentLoaded", function () {
  // Get current theme from Material theme
  const getTheme = () => {
    const scheme = document.body.getAttribute("data-md-color-scheme");
    return scheme === "slate" ? "dark" : "default";
  };

  // Initialize Mermaid with theme-aware config
  if (typeof mermaid !== "undefined") {
    mermaid.initialize({
      startOnLoad: false,
      theme: getTheme(),
      securityLevel: "loose",    // Required for external loading
      logLevel: "error",         // Suppress debug logs
      flowchart: {
        useMaxWidth: true,
      },
      sequence: {
        useMaxWidth: true,
      },
      er: {
        useMaxWidth: true,
      },
      mindmap: {
        useMaxWidth: true,
      },
    });

    // Render all mermaid diagrams (v10+ API)
    mermaid.run({ querySelector: ".mermaid" });
  }

  // Re-initialize on theme toggle
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (
        mutation.type === "attributes" &&
        mutation.attributeName === "data-md-color-scheme"
      ) {
        // Theme changed, reload to update Mermaid colors
        if (typeof mermaid !== "undefined") {
          // Force page reload on theme change (simplest approach)
          // Optional: Can implement intelligent re-render instead
          location.reload();
        }
      }
    });
  });

  // Watch for theme changes on body element
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });
});
