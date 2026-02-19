---
topic_id: 30226
title: "Previously Available Extensions No Longer Available On 5 2 2"
date: 2023-06-26
url: https://discourse.slicer.org/t/30226
---

# Previously available extensions no longer available on 5.2.2

**Topic ID**: 30226
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/previously-available-extensions-no-longer-available-on-5-2-2/30226

---

## Post #1 by @jhlegarreta (2023-06-26 02:15 UTC)

<p>Hi,<br>
I am using 3D Slicer 5.2.2 r31382 / fb46bd1, and when trying to install the following extensions it seems like the do not exist in the extension database (no match is shown), and thus cannot be installed:</p>
<ul>
<li>DTI-Reg</li>
<li>DTIAtlasBuilder</li>
<li>DTIAtlasFiberAnalyzer</li>
<li>DTIProcess</li>
</ul>
<p>Is this expected? How can it be fixed (sticking to the above Slicer version)?</p>
<p>I am using Slicer on an Ubuntu 22.04 machine.</p>
<p>These extensions were available in previous Slicer versions (at least, 4.10.2 to my knowledge).</p>
<p>Thanks for developing and maintaining Slicer.</p>

---

## Post #2 by @jamesobutler (2023-06-26 02:28 UTC)

<p>These DTI extensions were removed from the Slicer Extensions Manager in March 2022 because the builds had been failing for quite some time with no developer available to maintain the projects.</p>
<p>See the following</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/tree/main/ARCHIVE#optional-extension-documentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/ExtensionsIndex/tree/main/ARCHIVE#optional-extension-documentation" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/ExtensionsIndex/tree/main/ARCHIVE#optional-extension-documentation" target="_blank" rel="noopener nofollow ugc">ExtensionsIndex/ARCHIVE at main · Slicer/ExtensionsIndex - Optional extension documentation:</a></h3>

  <p><a href="https://github.com/Slicer/ExtensionsIndex/tree/main/ARCHIVE#optional-extension-documentation" target="_blank" rel="noopener nofollow ugc">main/ARCHIVE</a></p>

  <p><span class="label1">Slicer extensions index. Contribute to Slicer/ExtensionsIndex development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jhlegarreta (2023-06-26 13:47 UTC)

<p>OK, thanks for the answer James.</p>

---
