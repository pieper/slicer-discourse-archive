---
topic_id: 25943
title: "Extension Stopped Working In Slicer 5"
date: 2022-10-27
url: https://discourse.slicer.org/t/25943
---

# Extension stopped working in Slicer 5

**Topic ID**: 25943
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/extension-stopped-working-in-slicer-5/25943

---

## Post #1 by @koeglfryderyk (2022-10-27 22:13 UTC)

<p>My extension <a href="https://github.com/koegl/SlicerMRUSLandmarking" rel="noopener nofollow ugc">MRUSLandmarking</a> stopped working when Slicer 5 was introduced.</p>
<p>It works when I add it ‘locally’ through Extension Wizard → Select Extension, however, when it is installed through the Extension Manager it cannot be loaded.</p>
<p>The error comes from an import statement from the beginning of the main file, where I import a .py file where I have additional code:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer-stable.app/Contents/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/Applications/Slicer-stable.app/Contents/Extensions-30893/MRUSLandmarking/lib/Slicer-5.0/qt-scripted-modules/MRUSLandmarking.py", line 12, in &lt;module&gt;
    import Resources.utils
ModuleNotFoundError: No module named 'Resources.utils'
</code></pre>
<p>I’m confused why this error only happens through the extension manager.</p>
<p>I couldn’t find any guidelines on how to correctly do those imports in Slicer extensions, and I came up with the current way through trial and error.</p>
<p>What is the correct way of doing this?</p>

---

## Post #2 by @lassoan (2022-10-27 22:24 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="25943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p><code>Resources.utils</code></p>
</blockquote>
</aside>
<p>Provably you have put some Python scripts into the resources folder but you have forgot to add it to the install package. You need to list files that you want to be installed on the user’s computer in the CMakeLists.txt file.</p>
<p>A proper fix is not simply add this file to the resources folder, because that file is intended only for resource files (images, data files, etc), not code. See how to add more Python files to your module <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-include-python-modules-in-an-extension">here</a>.</p>

---
