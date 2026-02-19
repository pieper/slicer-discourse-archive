---
topic_id: 23252
title: "Update Related To Available Cdash Projects"
date: 2022-05-03
url: https://discourse.slicer.org/t/23252
---

# Update related to available CDash projects

**Topic ID**: 23252
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/update-related-to-available-cdash-projects/23252

---

## Post #1 by @jcfr (2022-05-03 06:23 UTC)

<p>As originally discussed in hangout from <a href="https://discourse.slicer.org/t/2019-03-26-hangout/6288/2">2019-03-26</a>, and later tracked in issue <a href="https://github.com/Slicer/Slicer/issues/4644">#4644</a>, build reports associated with Stable and Preview builds are submitted to dedicated CDash projects hosted at <code>https://slicer.cdash.org</code>:</p>
<ul>
<li><a href="https://slicer.cdash.org/index.php?project=SlicerStable">SlicerStable</a></li>
<li><a href="https://slicer.cdash.org/index.php?project=SlicerPreview">SlicerPreview</a></li>
</ul>
<p>Now that we are moving forward with Slicer 5.0, there is no need to keep around the older <code>Slicer4</code> CDash project and it has been removed (see issue <a href="https://github.com/Slicer/Slicer/issues/6063">#6063</a>).</p>
<p>For future reference, here are some historical details:</p>
<h2><a name="p-77560-history-1" class="anchor" href="#p-77560-history-1" aria-label="Heading link"></a>History</h2>
<p>The <code>Slicer4</code> project was created in Sept 2010 <sup class="footnote-ref"><a href="#footnote-77560-1" id="footnote-ref-77560-1">[1]</a></sup> and was used until Feb 2018 to organize both Stable and Nightly (now called Preview) submissions.</p>
<p>Then from Feb 2018 to April 2022, the <code>Slicer4</code> project was used to organize the extensions build associated with the stable release <sup class="footnote-ref"><a href="#footnote-77560-2" id="footnote-ref-77560-2">[2]</a></sup>.</p>
<p>Between 2010 and 2022, 254367 builds have been submitted to <code>Slicer4</code> project.</p>
<p>Starting with Slicer 5.0, the <code>Slicer4</code> project is defunct and a new project called <code>SlicerStable</code> is used <sup class="footnote-ref"><a href="#footnote-77560-3" id="footnote-ref-77560-3">[3]</a></sup>.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-77560-1" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/commit/cfb3499485486eeecd407aa9b6c7c7c3eb49962f" class="inline-onebox">ENH: Switch dashboard to submit to new slicer4 dashboard. · Slicer/Slicer@cfb3499 · GitHub</a> <a href="#footnote-ref-77560-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-77560-2" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/commit/19180ec0db26ff1b246765e686d5890b1af9b527" class="inline-onebox">ENH: Rename CDash project associated with "nightly release" to "Slice… · Slicer/Slicer@19180ec · GitHub</a> <a href="#footnote-ref-77560-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-77560-3" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/commit/62e4d8544f2a6f30b707a87288a5e1b9fc5a5a86" class="inline-onebox">ENH: Rename CDash project name from "Slicer4" to "SlicerPreview" · Slicer/Slicer@62e4d85 · GitHub</a> <a href="#footnote-ref-77560-3" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
