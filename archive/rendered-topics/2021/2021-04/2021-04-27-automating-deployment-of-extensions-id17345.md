# Automating deployment of extensions

**Topic ID**: 17345
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/automating-deployment-of-extensions/17345

---

## Post #1 by @LorenzE (2021-04-27 08:07 UTC)

<p>I am trying to automate the deployment (building and packaging) of a Slicer extension (including a C++ and Python module). From what I understand I need a working slicer build (from source) in order to build and package the extension correctly? The slicer build is quite big (couple of GB) and therefore hard to put into a Docker container or into a CI system (e.g. GitHub Actions). So my questions are:</p>
<ol>
<li>Is there any possibility to make the Slicer build more lightweight, i.e., reduce it in size?</li>
<li>Also, is there maybe a work around for extensions which only include a Python module or do we absolutely need a slicer build here, too?</li>
</ol>

---

## Post #2 by @pieper (2021-04-27 18:59 UTC)

<aside class="quote no-group" data-username="LorenzE" data-post="1" data-topic="17345">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ab992/48.png" class="avatar"> LorenzE:</div>
<blockquote>
<p>Is there any possibility to make the Slicer build more lightweight, i.e., reduce it in size?</p>
</blockquote>
</aside>
<p>Turning off SimpleITK and Testing will save a lot.  Also QWebEngine is big.  Also CLIs can be big.  It depends on what you need for your extension.</p>
<aside class="quote no-group" data-username="LorenzE" data-post="1" data-topic="17345">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ab992/48.png" class="avatar"> LorenzE:</div>
<blockquote>
<p>Also, is there maybe a work around for extensions which only include a Python module or do we absolutely need a slicer build here, too?</p>
</blockquote>
</aside>
<p>If your extension includes any C++ then you need to have the locally compiled version of the libs to compile against.</p>
<p>From a CI/container perspective it would be great if we had could create build environments all the Slicer superbuild projects (VTK, ITK, CTK, etc) since they don’t change very often.  But so far I don’t think anyone has found time to work on that.</p>

---
