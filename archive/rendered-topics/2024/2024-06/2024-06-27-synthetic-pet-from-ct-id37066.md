# Synthetic PET from CT 

**Topic ID**: 37066
**Date**: 2024-06-27
**URL**: https://discourse.slicer.org/t/synthetic-pet-from-ct/37066

---

## Post #1 by @oismaster (2024-06-27 12:31 UTC)

<p>This paper ( PMID: [38471502] <a href="https://pubmed.ncbi.nlm.nih.gov/38471502" class="inline-onebox" rel="noopener nofollow ugc">Synthetic PET from CT improves diagnosis and prognosis for lung cancer: Proof of concept - PubMed</a>) describes a process to use a CT to predict what the PET will look like.</p>
<p>Is this a useful module to reproduce in Slicer?<br>
Steps would be:</p>
<ol>
<li>Import CT</li>
<li>Run algorithms</li>
<li>Export PET to same folder with included translation object to be ready to import into viewing software.</li>
</ol>
<p>(I am a radiation oncologist without coding skills to implement this, hence my request.)<br>
The purpose is twofold, firstly for my own research use, but secondly also for availability in LMICs which cannot afford PET scans but where CTs are reasonably available.</p>

---

## Post #2 by @pieper (2024-07-04 16:49 UTC)

<p>Yes, I think this looks like a very cool model that would be good to add.</p>
<p>It looks like the code and the model weights used to generate the results in the paper are available in github:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/WuLabMDA/Synthetic-PET-from-CT/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/WuLabMDA/Synthetic-PET-from-CT/" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d98723d18807114825751bf06a7ae2e119f5e790acd4fd6c3d9cc7f334bdabe9/WuLabMDA/Synthetic-PET-from-CT" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/WuLabMDA/Synthetic-PET-from-CT/" target="_blank" rel="noopener">GitHub - WuLabMDA/Synthetic-PET-from-CT</a></h3>

  <p>Contribute to WuLabMDA/Synthetic-PET-from-CT development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Maybe someone here will want to take on packaging this into an extension.</p>
<p>Or <a class="mention" href="/u/oismaster">@oismaster</a> you may want to contact the people at <a href="https://mhub.ai/">https://mhub.ai/</a> for advice.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> do you have any suggestions?</p>

---

## Post #3 by @ciro.raggio (2025-09-12 19:24 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> It would be great to include it in the new ModalityConverter extension. I see that there are still some open issues. Let me know what I can do <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
