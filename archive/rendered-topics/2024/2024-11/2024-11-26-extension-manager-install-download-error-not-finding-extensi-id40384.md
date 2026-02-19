---
topic_id: 40384
title: "Extension Manager Install Download Error Not Finding Extensi"
date: 2024-11-26
url: https://discourse.slicer.org/t/40384
---

# Extension Manager install/download error (not finding extension id)

**Topic ID**: 40384
**Date**: 2024-11-26
**URL**: https://discourse.slicer.org/t/extension-manager-install-download-error-not-finding-extension-id/40384

---

## Post #1 by @acsenrafilho (2024-11-26 14:55 UTC)

<p>Hi Slicers,</p>
<p>I have updated the Slicer Extension Index to contain the support for <code>5.6</code> extension version.<br>
My extension is: <a href="https://slicer.cdash.org/builds/3603576" rel="noopener nofollow ugc">https://slicer.cdash.org/builds/3603576</a> (for Linux build)</p>
<p>I checked that the CDash report have built correctly all version (Win, Mac and Linux), showing the packing symbol on it and referencing to the correct git commit hash.</p>
<p>However, I have tested installing it on Slicer (user installation, 5.6.2 r32448 / f10cd8c), just to be sure everything is ok. The Extension Index shows my extension in the list, by searching <code>Diffusion Complexity</code>, but when I click to install it an error pops up on the screen:</p>
<pre><code class="lang-auto">Download of extension failed, could not find an extension with id = 6745a15376aed8e33340f5c6
</code></pre>
<p>What happens here? I do not know what went wrong here…<br>
Is this the correct way to inform a extension to be available to a Slicer stable version?<br>
I found confusing that is citing in the CDash build information that Slicer is at <code>Type: Extensions-5.6-Nightly</code>.</p>

---
