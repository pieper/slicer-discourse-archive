# New extension does not show in Slicer 4.8 ExtensonManager

**Topic ID**: 1729
**Date**: 2017-12-26
**URL**: https://discourse.slicer.org/t/new-extension-does-not-show-in-slicer-4-8-extensonmanager/1729

---

## Post #1 by @fedorov (2017-12-26 19:27 UTC)

<p>A new extension (TOMAAT) was recently added to the ExtensionsIndex 4.8 branch (see <a href="https://github.com/Slicer/ExtensionsIndex/pull/1502">https://github.com/Slicer/ExtensionsIndex/pull/1502</a>). The extension was built and packaged without problems, based on <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=tomaat">CDash content here</a>, but nevertheless the new extension does not show up in the Extension manager for the stable. Can someone explain what is going on, and how this can be fixed?</p>

---

## Post #2 by @lassoan (2017-12-27 04:27 UTC)

<p>It’ll take a few more days until the new stable version (Slicer 4.8.1) is released. Updated extensions should be available after that.</p>

---

## Post #3 by @jcfr (2017-12-27 08:49 UTC)

<blockquote>
<p>Slicer 4.8.1 packages have been marked as released (see <a href="http://slicer.kitware.com/midas3/folder/4989">http://slicer.kitware.com/midas3/folder/4989</a>) and should show up on <a href="http://download.slicer.org/">http://download.slicer.org/</a> shortly.</p>
</blockquote>
<p>See <a href="https://discourse.slicer.org/t/slicer-4-8-1-release-and-transition-to-qt5-and-vtk9/1551/9" class="inline-onebox">Slicer 4.8.1 release and transition to Qt5 and VTK9 - #9 by jcfr</a></p>

---

## Post #4 by @fedorov (2017-12-27 15:00 UTC)

<p>Sorry, but this does not completely answer my question. It is still not clear to me whether it is expected that no new extensions can be introduced into 4.8.</p>
<p>Is it the only way to wait for the new release to be able to add new extensions to the stable package?</p>

---

## Post #5 by @jcfr (2017-12-27 15:29 UTC)

<p>Extensions for Slicer 4.8 will be built for Slicer 4.8.1 only.</p>

---

## Post #6 by @fedorov (2017-12-27 15:35 UTC)

<p>According to CDash, the new extension added to the 4.8 branch last week is being built and packaged every night, see for the extension in question: <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=tomaat">http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=tomaat</a>.  It is build, but does not show up in the extension manager of 4.8. To me, this is confusing. If they are not supposed to show up in the ExtensionManager, then why building them.</p>

---

## Post #7 by @lassoan (2017-12-27 15:57 UTC)

<p>Is it possible that you had 4.8.0 installed, while extensions were built for 4.8.1?</p>

---

## Post #8 by @fedorov (2017-12-27 15:59 UTC)

<p>Yes, I think that is what was happening. All makes sense now, thank you! I installed 4.8.1, and I can see it there.</p>

---
