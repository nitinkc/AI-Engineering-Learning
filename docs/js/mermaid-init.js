(function () {
  const mermaidLanguagePattern = /\blanguage-mermaid\b/;
  const processedAttribute = 'data-mermaid-processed';
  let mermaidInitialized = false;

  function initializeMermaid() {
    if (mermaidInitialized || typeof mermaid === 'undefined') {
      return;
    }

    mermaid.initialize({ startOnLoad: false, theme: 'default' });
    mermaidInitialized = true;
  }

  function runMermaid(nodes) {
    if (!nodes.length || typeof mermaid === 'undefined') {
      return;
    }

    initializeMermaid();
    if (typeof mermaid.run === 'function') {
      mermaid.run({ nodes: nodes });
    } else {
      mermaid.init(undefined, nodes);
    }

    nodes.forEach(function (node) {
      node.setAttribute(processedAttribute, 'true');
    });
  }

  function render(root) {
    if (typeof mermaid === 'undefined') {
      return;
    }

    const directNodes = root.querySelectorAll('.mermaid:not([' + processedAttribute + '="true"])');
    const nodes = Array.from(directNodes);
    const blocks = root.querySelectorAll('.highlight code, pre > code');

    blocks.forEach(function (codeBlock) {
      const className = codeBlock.className || '';
      if (!mermaidLanguagePattern.test(className)) {
        return;
      }

      const wrapper = codeBlock.closest('.highlight') || codeBlock.closest('pre');
      if (!wrapper) {
        return;
      }

      const div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = codeBlock.textContent.trim();
      wrapper.replaceWith(div);
      nodes.push(div);
    });

    runMermaid(nodes);
  }

  document.addEventListener('DOMContentLoaded', function () {
    render(document);
  });

  if (typeof document$ !== 'undefined' && typeof document$.subscribe === 'function') {
    document$.subscribe(function (root) {
      render(root);
    });
  }
})();

