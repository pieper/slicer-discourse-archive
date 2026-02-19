---
topic_id: 31886
title: "Revisit Github Actions For Slicer Ci"
date: 2023-09-25
url: https://discourse.slicer.org/t/31886
---

# Revisit GitHub Actions for Slicer CI?

**Topic ID**: 31886
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/revisit-github-actions-for-slicer-ci/31886

---

## Post #1 by @fedorov (2023-09-25 14:01 UTC)

<p>I recently learned that as hard as it is to believe, it appears that GitHub Actions provide free usage  or runners for public repositories, and have exceedingly generous limits - 6 hours per job and 35 DAYS per workflow.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration">
  <header class="source">
      <img src="https://docs.github.com/assets/cb-803/images/site/favicon.svg" class="site-icon" width="16" height="16">

      <a href="https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration" target="_blank" rel="noopener">GitHub Docs</a>
  </header>

  <article class="onebox-body">
    <img width="500" height="500" src="https://github.githubassets.com/images/modules/open_graph/github-logo.png" class="thumbnail onebox-avatar">

<h3><a href="https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration" target="_blank" rel="noopener">Usage limits, billing, and administration - GitHub Docs</a></h3>

  <p>There are usage limits for GitHub Actions workflows. Usage charges apply to repositories that go beyond the amount of free minutes and storage for a repository.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Maybe it is time to give it another consideration for building and packaging Slicer and extensions?</p>

---

## Post #2 by @pieper (2023-09-25 14:05 UTC)

<p>It would be great if someone could try that out.  I haven’t tried for a couple of years, but as I recall the VMs had 2 pretty slow cores, so a linux build that could take as little as 30 minutes on a fast multicore machine took much longer.</p>
<p>Caching build directories for the superbuild prerequisites could definitely speed things up.  I think that’s doable but I didn’t try very hard.</p>

---

## Post #3 by @jcfr (2023-09-25 14:30 UTC)

<p>Thanks for the pointers. In the context of SlicerDMRI<sup class="footnote-ref"><a href="#footnote-100969-1" id="footnote-ref-100969-1">[1]</a></sup>, we worked with <a class="mention" href="/u/jhlegarreta">@jhlegarreta</a> to setup CI for the extension so that it builds Slicer and the associated extension.</p>
<p>Total time for building Slicer alone<sup class="footnote-ref"><a href="#footnote-100969-2" id="footnote-ref-100969-2">[2]</a></sup> using the <code>ubuntu-22.04</code> worker  is ~3.5hrs and I anticipate that the macOS and Windows build times would be longer (at least using the default worker made available for open-source project).</p>
<p>That said, with the availability of dedicated resources to both support the implementation of the infrastructure as well as more performant workers, we should be able to further leverage GitHub Actions infrastructure.</p>
<p>In the meantime, here are some issues we need to address:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/issues/3353" class="inline-onebox">Create develeper package / SDK · Issue #3353 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://discourse.slicer.org/t/proposal-install-simpleitk-from-wheels-instead-of-building-from-source/25635" class="inline-onebox">Proposal: Install SimpleITK from wheels instead of building from source</a></li>
</ul>
<p>Lastly, to fully adapt the GitHub Actions infrastructure, we would also need runner for M1 to be available. See <a href="https://github.com/github/roadmap/issues/528" class="inline-onebox">GitHub Actions: Apple Silicon (M1) powered macOS runners (Public Beta) · Issue #528 · github/roadmap · GitHub</a></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-100969-1" class="footnote-item"><p><a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/master" class="inline-onebox">GitHub - SlicerDMRI/SlicerDMRI: Diffusion MRI analysis and visualization in 3D Slicer open source medical imaging platform.</a> <a href="#footnote-ref-100969-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-100969-2" class="footnote-item"><p><a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/5755237502/job/15602531663" class="inline-onebox">DOC: Sync the license file with the current Slicer license file content · SlicerDMRI/SlicerDMRI@6758b84 · GitHub</a> <a href="#footnote-ref-100969-2" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
