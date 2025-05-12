/**
 * SKAI Documentation JavaScript
 * Provides interactive functionality for documentation pages
 */

document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const sidebar = document.querySelector('.sidebar');
  
  if (menuToggle && sidebar) {
    menuToggle.addEventListener('click', function() {
      sidebar.classList.toggle('active');
    });
  }
  
  // Add copy button to code blocks
  const codeBlocks = document.querySelectorAll('pre');
  codeBlocks.forEach(function(codeBlock) {
    const copyButton = document.createElement('button');
    copyButton.className = 'copy-button';
    copyButton.textContent = 'Copy';
    
    // Position the button
    codeBlock.style.position = 'relative';
    codeBlock.appendChild(copyButton);
    
    copyButton.addEventListener('click', function() {
      const code = codeBlock.querySelector('code').textContent;
      navigator.clipboard.writeText(code)
        .then(() => {
          copyButton.textContent = 'Copied!';
          setTimeout(() => {
            copyButton.textContent = 'Copy';
          }, 2000);
        })
        .catch(err => {
          console.error('Failed to copy: ', err);
          copyButton.textContent = 'Failed!';
          setTimeout(() => {
            copyButton.textContent = 'Copy';
          }, 2000);
        });
    });
  });
  
  // Active link highlighting
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.sidebar-nav a');
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });
  
  // Collapsible sidebar sections
  const collapsibleHeadings = document.querySelectorAll('.sidebar-nav .collapsible');
  collapsibleHeadings.forEach(heading => {
    heading.addEventListener('click', function() {
      this.classList.toggle('collapsed');
      const content = this.nextElementSibling;
      if (content.style.maxHeight) {
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });
  
  // Search functionality
  const searchInput = document.querySelector('.search-input');
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      const query = this.value.toLowerCase();
      const searchIndex = window.searchIndex || [];
      
      if (query.length < 2) {
        document.querySelector('.search-results').innerHTML = '';
        return;
      }
      
      const results = searchIndex.filter(item => {
        return item.title.toLowerCase().includes(query) || 
               item.content.toLowerCase().includes(query);
      });
      
      displaySearchResults(results, query);
    });
  }
  
  function displaySearchResults(results, query) {
    const searchResults = document.querySelector('.search-results');
    if (!searchResults) return;
    
    searchResults.innerHTML = '';
    
    if (results.length === 0) {
      searchResults.innerHTML = '<p>No results found for "' + query + '"</p>';
      return;
    }
    
    const resultsList = document.createElement('ul');
    resultsList.className = 'search-results-list';
    
    results.slice(0, 10).forEach(result => {
      const listItem = document.createElement('li');
      const link = document.createElement('a');
      link.href = result.url;
      link.textContent = result.title;
      
      const snippet = document.createElement('p');
      snippet.className = 'search-snippet';
      
      // Create a snippet of content around the matched query
      const contentLower = result.content.toLowerCase();
      const queryIndex = contentLower.indexOf(query);
      if (queryIndex > -1) {
        const start = Math.max(0, queryIndex - 50);
        const end = Math.min(result.content.length, queryIndex + query.length + 50);
        let snippetText = result.content.substring(start, end);
        
        if (start > 0) snippetText = '...' + snippetText;
        if (end < result.content.length) snippetText = snippetText + '...';
        
        snippet.textContent = snippetText;
      } else {
        snippet.textContent = result.content.substring(0, 100) + '...';
      }
      
      listItem.appendChild(link);
      listItem.appendChild(snippet);
      resultsList.appendChild(listItem);
    });
    
    searchResults.appendChild(resultsList);
  }
  
  // Table of contents generation
  generateTableOfContents();
  
  function generateTableOfContents() {
    const contentSection = document.querySelector('.main-content');
    const tocContainer = document.querySelector('.table-of-contents');
    
    if (!contentSection || !tocContainer) return;
    
    const headings = contentSection.querySelectorAll('h1, h2, h3');
    if (headings.length < 3) {
      tocContainer.style.display = 'none';
      return;
    }
    
    const tocList = document.createElement('ul');
    tocList.className = 'toc-list';
    
    headings.forEach((heading, index) => {
      // Add ID to heading if it doesn't have one
      if (!heading.id) {
        heading.id = 'heading-' + index;
      }
      
      const listItem = document.createElement('li');
      listItem.className = 'toc-item toc-level-' + heading.tagName.toLowerCase();
      
      const link = document.createElement('a');
      link.href = '#' + heading.id;
      link.textContent = heading.textContent;
      
      listItem.appendChild(link);
      tocList.appendChild(listItem);
    });
    
    tocContainer.appendChild(tocList);
  }
  
  // Version switcher
  const versionSelector = document.querySelector('.version-dropdown select');
  if (versionSelector) {
    versionSelector.addEventListener('change', function() {
      window.location.href = this.value;
    });
  }
  
  // Add smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 20,
          behavior: 'smooth'
        });
        
        // Update URL without reloading page
        history.pushState(null, null, '#' + targetId);
      }
    });
  });
  
  // Handle initial hash in URL
  if (window.location.hash) {
    const targetId = window.location.hash.substring(1);
    const targetElement = document.getElementById(targetId);
    
    if (targetElement) {
      setTimeout(() => {
        window.scrollTo({
          top: targetElement.offsetTop - 20,
          behavior: 'smooth'
        });
      }, 200);
    }
  }
  
  // Add syntax highlighting if Prism.js is available
  if (typeof Prism !== 'undefined') {
    Prism.highlightAll();
  }
});