# Minimum Slicer installation for fast launch

**Topic ID**: 8642
**Date**: 2019-10-01
**URL**: https://discourse.slicer.org/t/minimum-slicer-installation-for-fast-launch/8642

---

## Post #1 by @Joshua_Broder (2019-10-01 18:44 UTC)

<p>I’d like to optimize Slicer to launch and display a volume as quickly as possible.  The minimum functions I need are the intersecting multiplanar view, each slice view (red/green/yellow), and measurement calipers.  Reformat and volume render are desirable but not necessary.</p>
<ol>
<li>Which modules can I disable (in settings) to speed launching while preserving these functions?</li>
<li>Can Slicer be pre-launched and then triggered to open a data file from other software, rather than launching a new Slicer instance?</li>
</ol>

---

## Post #2 by @lassoan (2019-10-02 00:44 UTC)

<aside class="quote no-group" data-username="Joshua_Broder" data-post="1" data-topic="8642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ecccb3/48.png" class="avatar"> Joshua_Broder:</div>
<blockquote>
<p>Which modules can I disable (in settings) to speed launching while preserving these functions?</p>
</blockquote>
</aside>
<p>You can try disabling all modules and see how much startup time improvement can be achieved that way. You can also remove module shared libraries, that may make the startup a bit faster, but still most probably the startup time will be still about 5 seconds.</p>
<aside class="quote no-group" data-username="Joshua_Broder" data-post="1" data-topic="8642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ecccb3/48.png" class="avatar"> Joshua_Broder:</div>
<blockquote>
<p>Can Slicer be pre-launched and then triggered to open a data file from other software, rather than launching a new Slicer instance?</p>
</blockquote>
</aside>
<p>Yes, there are multiple extensions for Slicer that provide various server interfaces that can be used to trigger loading of a data set. You can probably use/slightly modify one of these:</p>
<ul>
<li><a href="https://github.com/pieper/SlicerWeb">Web server</a></li>
<li><a href="https://github.com/Slicer/SlicerJupyter">Jupyter notebook server</a></li>
<li><a href="https://github.com/openigtlink/SlicerOpenIGTLink">OpenIGTLink server</a></li>
</ul>
<p>Let us know what you ended up using (or if you need further help).</p>

---
