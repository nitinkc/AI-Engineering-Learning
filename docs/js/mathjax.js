// mathjax.js
// Configures MathJax for rendering LaTeX/KaTeX math equations
// Runs BEFORE MathJax CDN script in mkdocs.yml

window.MathJax = {
  tex: {
    // Enable inline and display math
    inlineMath: [["$", "$"]],
    displayMath: [["$$", "$$"]],
    processEscapes: true,
  },
  svg: {
    // Use SVG rendering (better for dark mode)
    fontCache: "global",
  },
  startup: {
    // Automatically render when page loads
    pageReady: () => {
      return MathJax.typesetPromise().catch(() => {
        // Silent fail if math rendering fails
        console.debug("MathJax rendering completed");
      });
    },
  },
  // Custom macros if needed
  loader: {
    load: ["input/tex", "output/svg"],
  },
};
