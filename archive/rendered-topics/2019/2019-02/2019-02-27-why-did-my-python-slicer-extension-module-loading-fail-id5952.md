# Why did my python slicer extension module loading fail?

**Topic ID**: 5952
**Date**: 2019-02-27
**URL**: https://discourse.slicer.org/t/why-did-my-python-slicer-extension-module-loading-fail/5952

---

## Post #1 by @John_DiMatteo (2019-02-27 21:07 UTC)

<p>Operating system: Linux Mint Tara (Ubuntu 18.04 Bionic)<br>
Slicer version: 4.10.0<br>
Expected behavior: Loading of module or an explanation of why loading failed<br>
Actual behavior: Module loading failed with no details</p>
<p>Hi All, I’m new to slicer development.  When I try to load my slicer extension I get an error “Module loading failed”.  Are there any more detailed logs that can help me fix this?  This was previously working, and since it was last working I’ve updated the extension code and removed the module from Slicer &gt; Edit &gt; Settings &gt; Modules.  The following details steps I’m taking when I get the error:</p>
<ol>
<li>start Slicer</li>
<li>select module Developer Tools &gt; Extension Wizard</li>
<li>click “Select Extension”</li>
<li>choose my slicer extension directory</li>
<li>a window pops up saying “The following modules can be loaded.  Would you like to load them now?”</li>
<li>I select the module I want to load (with “Add selected modules to search paths” checked) and click “Yes”</li>
<li>Following error dialog pops up:</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2835782c42f14bf8d2c01c9218fb3de88261c9.png" alt="image" data-base62-sha1="vgKIdfsrqIFBBo7zvhn2WiLCwCl" width="347" height="149"></p>
<p>Is there any more information to pinpoint the cause of the error?  Is the error in the python code or the CMakeLists.txt or something else?</p>

---

## Post #2 by @John_DiMatteo (2019-02-27 21:58 UTC)

<p>I upgraded to Slicer 4.10.1 and the module loads successfully now.</p>

---

## Post #3 by @John_DiMatteo (2019-02-27 23:08 UTC)

<p>I reproduced this same problem in slicer 4.10.1.  It seems that once a module is added and removed, attempting to add it will always result in the above “Module loading failed” error.  Removing settings (e.g. <code>~/.config/NA-MIC/</code> as described at <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ</a>) resolved the problem.</p>
<p>Should I submit a bug report somewhere?</p>

---

## Post #4 by @lassoan (2019-02-27 23:22 UTC)

<p>For a specific Slicer version, you need to add a module to additional module paths only once (the paths are stored in application settings ini file). Maybe this could be made more clear in the documentation.</p>

---
