# Usage of CLI modules outside Slicer

**Topic ID**: 5851
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/usage-of-cli-modules-outside-slicer/5851

---

## Post #1 by @cpinter (2019-02-20 18:13 UTC)

<p>Hi there!</p>
<p>I’d would like to ask about some details of CLI modules that I wasn’t able to find online for my PhD thesis.</p>
<p>Are CLIs (/SEM/CLP) actually used outside Slicer? I found evidence for that in MITK (the links on the bottom of <a href="http://docs.mitk.org/2016.11/org_mitk_views_cmdlinemodules.html" rel="nofollow noopener">this</a> page), but what about MeVisLab or others? I heard in the past that MeVisLab also supports them but could not find proof. Is there a common repository that they use? (Slicer uses SEM but it seems to be Slicer-specific).</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-02-20 20:01 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="1" data-topic="5851">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Are CLIs (/SEM/CLP) actually used outside Slicer?</p>
</blockquote>
</aside>
<p>Yes, by many groups, for example MITK, Gimias, MedInria, <a href="https://github.com/hmeine/MeVisLab-CLI/blob/master/Modules/Scripts/python/cli_to_macro.py">MeVisLab</a>, Girder, <a href="https://github.com/NifTK/NifTK/tree/master/Applications/Add">Niftk</a>. You can find evidence by inspecting their source code.</p>

---

## Post #3 by @jcfr (2019-02-20 20:21 UTC)

<p>An other example is <a href="https://digitalslidearchive.github.io/HistomicsTK/" rel="nofollow noopener">HistomicsTK</a> with <a href="https://github.com/girder/slicer_cli_web#readme" rel="nofollow noopener">slicer_cli_web</a></p>

---
