---
topic_id: 43505
title: "Dynamic Badge For Papers With Code Number Of Citations"
date: 2025-06-26
url: https://discourse.slicer.org/t/43505
---

# Dynamic badge for papers with code, number of citations

**Topic ID**: 43505
**Date**: 2025-06-26
**URL**: https://discourse.slicer.org/t/dynamic-badge-for-papers-with-code-number-of-citations/43505

---

## Post #1 by @mau_igna_06 (2025-06-26 17:18 UTC)

<p>Hi</p>
<p>You can get the markdown code of the dynamic badge just from your paper’s DOI so you can add it to your README.md</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mauigna06/81a593644ec46e520adf4a7561d2075e">
  <header class="source">

      <a href="https://gist.github.com/mauigna06/81a593644ec46e520adf4a7561d2075e" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mauigna06/81a593644ec46e520adf4a7561d2075e" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/mauigna06/81a593644ec46e520adf4a7561d2075e</a></h4>

  <h5>get_dynamic_citations_number_badge.py</h5>
  <pre><code class="Python">sources = {
    "semanticscholar": {
        "preffix": "https://api.semanticscholar.org/graph/v1/paper/DOI:",
        "suffix": "?fields=citationCount",
        "citationCountFieldName": ["citationCount"],
    },
    "crossref": {
        "preffix": "https://api.crossref.org/works/",
        "suffix": "",
        "citationCountFieldName": ["message","is-referenced-by-count"],</code></pre>
   This file has been truncated. <a href="https://gist.github.com/mauigna06/81a593644ec46e520adf4a7561d2075e" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For example, for some relatively successful paper with more than 500 citations, you get an image that updates every day according to latest stats:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://img.shields.io/badge/dynamic/json?label=Citations&amp;query=%24.citationCount&amp;url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2FDOI%3A10.48550%2FarXiv.2211.02701%3Ffields%3DcitationCount">
  <header class="source">

      <a href="https://img.shields.io/badge/dynamic/json?label=Citations&amp;query=%24.citationCount&amp;url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2FDOI%3A10.48550%2FarXiv.2211.02701%3Ffields%3DcitationCount" target="_blank" rel="noopener nofollow ugc">img.shields.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://img.shields.io/badge/dynamic/json?label=Citations&amp;query=%24.citationCount&amp;url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2FDOI%3A10.48550%2FarXiv.2211.02701%3Ffields%3DcitationCount" target="_blank" rel="noopener nofollow ugc">Citations: 510</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please share with others</p>

---
