---
topic_id: 10546
title: "Geodesicslicer Extension Published"
date: 2020-03-04
url: https://discourse.slicer.org/t/10546
---

# GeodesicSlicer extension published

**Topic ID**: 10546
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/geodesicslicer-extension-published/10546

---

## Post #1 by @Frederic (2020-03-04 16:57 UTC)

<p>Dear all,<br>
We are pleased to inform you that our article about one 3D Slicer extension (<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/GeodesicSlicer" rel="nofollow noopener">GeodesicSlicer</a>) has just been published in NeuroInformatics:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://link.springer.com/oscar-static/images/favicons/springerlink/favicon-eb9f5576a3.ico" class="site-icon" width="48" height="48">
      <a href="https://link.springer.com/article/10.1007/s12021-020-09457-9" target="_blank" rel="nofollow noopener">Neuroinformatics</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:110/145;"><img src="https://media.springernature.com/w110/springer-static/cover/journal/12021.jpg" class="thumbnail" width="110" height="145"></div>

<h3><a href="https://link.springer.com/article/10.1007/s12021-020-09457-9" target="_blank" rel="nofollow noopener">GeodesicSlicer: a Slicer Toolbox for Targeting Brain Stimulation</a></h3>

<p>NonInvasive Brain Stimulation (NIBS) is a potential therapeutic tool with growing interest, but neuronavigation-guided software and tools available for the target determination are mostly either expensive or closed proprietary applications. To...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Once again, thanks to <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a> for their valuable help.</p>
<p>Frederic</p>

---

## Post #2 by @muntahi398 (2020-03-10 09:38 UTC)

<p>Hi  Frederic,<br>
thanks for the news, I tried to intall the extension. But in slicer it shows error at starting</p>
<pre><code>/NA-MIC/Extensions-28812/GeodesicSlicer/lib/Slicer-4.11/qt-scripted-modules/GeodesicSlicer.py", line 103
ScriptedLoadableModuleWidget.setup(self)
                                       ^
</code></pre>
<p>TabError: inconsistent use of tabs and spaces in indentation &gt;</p>

---

## Post #3 by @Frederic (2020-03-10 14:11 UTC)

<p>Hi <a class="mention" href="/u/muntahi398">@muntahi398</a>,<br>
I advise you to use the last stable version of 3D Slicer. The software works well on the version 4.10.2.<br>
After that, I am discovering your bug in the Preview Release. However, this is exactly the same code than the release version. Do you have an idea <a class="mention" href="/u/jcfr">@jcfr</a> ? Some compilation mistake?<br>
Thanks.</p>

---

## Post #4 by @lassoan (2020-03-10 15:26 UTC)

<p>The error is due to inconsistent use of whitespace: you must either indent only tabs or only spaces, but in the <a href="https://github.com/FredericBr/SlicerGeodesic/edit/master/GeodesicSlicer/GeodesicSlicer.py">GeodesicSlicer.py</a> you have a random mixture. It should have failed with Slicer-4.10 as well.</p>
<p>I did a quick automatic formatting of the file in Visual Studio Code and submitted a <a href="https://github.com/FredericBr/SlicerGeodesic/pull/2">pull request</a>. I haven’t tested it, so make sure to test the changes yourself.</p>

---

## Post #5 by @Frederic (2020-03-11 08:17 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
Once again, I don’t understand why it’s work on the previous version and not now, but the inconsistent mixture seems to be the way out of the issue.</p>

---
