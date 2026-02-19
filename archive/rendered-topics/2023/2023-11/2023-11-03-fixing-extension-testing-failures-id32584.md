---
topic_id: 32584
title: "Fixing Extension Testing Failures"
date: 2023-11-03
url: https://discourse.slicer.org/t/32584
---

# Fixing extension testing failures

**Topic ID**: 32584
**Date**: 2023-11-03
**URL**: https://discourse.slicer.org/t/fixing-extension-testing-failures/32584

---

## Post #1 by @jhlegarreta (2023-11-03 15:11 UTC)

<p>Hi,<br>
there are a number of tests in the <code>SlicerDMRI</code> extension build that I would like to fix:<br>
<a href="https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=3198672" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>
<p>Some of them (e.g. <a href="https://slicer.cdash.org/test/25944478" rel="noopener nofollow ugc">py_TractographyExportPLY</a>, <a href="https://slicer.cdash.org/test/25944480" rel="noopener nofollow ugc">py_TractographyDownsample</a>) report a short message saying</p>
<pre><code class="lang-auto">[/Users/svc-dashboard/D/S/A/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.
</code></pre>
<p>I’ve found these potentially related threads, and have read the information in the corresponding links:<br>
<a href="https://github.com/Slicer/Slicer/issues/6484" class="inline-onebox" rel="noopener nofollow ugc">PythonSlicer problem with vtk and ReadData · Issue #6484 · Slicer/Slicer · GitHub</a><br>
<a href="https://discourse.slicer.org/t/extension-tests-fail-on-cdash-why/26571/13" class="inline-onebox">Extension tests fail on CDash, why? - #13 by RafaelPalomar</a></p>
<p>However, it is unclear what the appopriate sorting for the imports is: is this documented somewhere? Otherwise, what is the recipe? I have tried a few different sortings without success for e.g.:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/372675b96e917acb61bc8cb2ac9262d87cc5b06a/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py#L6" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/SlicerDMRI/blob/372675b96e917acb61bc8cb2ac9262d87cc5b06a/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py#L6</a><br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/372675b96e917acb61bc8cb2ac9262d87cc5b06a/Modules/Scripted/TractographyDownsample/TractographyDownsample.py#L9" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/SlicerDMRI/blob/372675b96e917acb61bc8cb2ac9262d87cc5b06a/Modules/Scripted/TractographyDownsample/TractographyDownsample.py#L9</a></p>
<p>Also, there are a number of tests (e.g. <a href="https://slicer.cdash.org/test/25944472" rel="noopener nofollow ugc">py_fiber_visibility_crash2438</a>) that fail because data nodes are not available in the scene, e.g.</p>
<pre><code class="lang-auto"> tractNode = slicer.util.getNode('tract1')
 (...)
 slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'tract1'
</code></pre>
<p>I’ve seen that the data does not get loaded into the scene (it does if I use a <code>ModelFile</code> type, but then fails to get other fiber data type-specific properties):<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/372675b96e917acb61bc8cb2ac9262d87cc5b06a/Modules/Loadable/TractographyDisplay/Testing/Python/fiber_visibility_crash2438.py#L191" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/SlicerDMRI/blob/372675b96e917acb61bc8cb2ac9262d87cc5b06a/Modules/Loadable/TractographyDisplay/Testing/Python/fiber_visibility_crash2438.py#L191</a></p>
<p>The command looks correct, though.  What am I missing here? How can this be tested properly/fixed?</p>
<p>Note that the data was moved (related topic <a href="https://discourse.slicer.org/t/actual-data-content-of-slicer-kitware-com-midas3-archive/30921" class="inline-onebox">Actual data content of slicer.kitware.com-midas3-archive</a>) and the correct <code>uris</code> for the data would be <a href="https://github.com/Slicer/slicer.kitware.com-midas3-archive/releases/download/SHA256/06d5b5777915857fbac7b3cbd9c371523d1371f29b0c89eb7a33d86d780d5b2b" rel="noopener nofollow ugc">https://github.com/Slicer/slicer.kitware.com-midas3-archive/releases/download/SHA256/06d5b5777915857fbac7b3cbd9c371523d1371f29b0c89eb7a33d86d780d5b2b</a>.</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-11-03 20:50 UTC)

<p>Are you able to replicate the test crashes in a local debug build?</p>
<p>Regarding the import order difference maybe you can join one the Tuesday morning developer meeting and we can discuss.  It should just be a matter of following the class hierarchy and library dependencies.</p>

---

## Post #3 by @jhlegarreta (2023-11-06 00:10 UTC)

<p>Thanks for answering Steve.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="32584">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Are you able to replicate the test crashes in a local debug build?</p>
</blockquote>
</aside>
<p>Have not tried debugging; I am able to reproduce the issue from a command line run. Have read the debugging instructions in the Slicer documentation, but it is unclear to me how this can be debugged (this being an extension, this being a Python module, etc.).</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="32584">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Regarding the import order difference maybe you can join one the Tuesday morning developer meeting and we can discuss. It should just be a matter of following the class hierarchy and library dependencies.</p>
</blockquote>
</aside>
<p>Have a meeting 11:00-12:00 ET. If it does not conflict, I may join.</p>

---
