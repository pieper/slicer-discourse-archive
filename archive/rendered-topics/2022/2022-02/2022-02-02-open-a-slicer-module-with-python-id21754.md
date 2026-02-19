---
topic_id: 21754
title: "Open A Slicer Module With Python"
date: 2022-02-02
url: https://discourse.slicer.org/t/21754
---

# Open a slicer module with python

**Topic ID**: 21754
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/open-a-slicer-module-with-python/21754

---

## Post #1 by @koeglfryderyk (2022-02-02 16:36 UTC)

<p>I want to open my custom scripted module every time I open Slicer.</p>
<p>I know that I have to edit the .slicerrc.py file, but I don’t know what lines of code to put in there.</p>

---

## Post #2 by @pieper (2022-02-02 16:38 UTC)

<p>As an example I add this to the command line when I start slicer:</p>
<pre><code class="lang-auto">--python-code "selectModule('WebServer')"
</code></pre>
<p>But you can put the same in <code>.slicerrc.py</code>, maybe using <code>slicer.util.selectModule</code> for style purposes.</p>

---

## Post #3 by @jamesobutler (2022-02-02 16:38 UTC)

<p>The Slicer script repository has many python examples that may be helpful for you. One includes setting the slicer module for startup.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-a-new-default-module-at-startup" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-a-new-default-module-at-startup</a></p>

---

## Post #4 by @jamesobutler (2022-02-02 16:48 UTC)

<p>Using the GUI, you can go to Settings-&gt;Modules and set the Default startup module from the list of loaded modules. Here I have set “OpenIGTLinkIF” as my new default.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb120dbc07dd0541e38d8248a242edd1ce7cfb5d.png" data-download-href="/uploads/short-url/zP4wxwvxx0VCjYW2j70sr58tFcp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb120dbc07dd0541e38d8248a242edd1ce7cfb5d.png" alt="image" data-base62-sha1="zP4wxwvxx0VCjYW2j70sr58tFcp" width="553" height="500" data-dominant-color="F2EFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">674×609 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
