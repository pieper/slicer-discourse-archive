# SliceTracker module cannot be loaded on Slicer 4.11.20200930

**Topic ID**: 13895
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/slicetracker-module-cannot-be-loaded-on-slicer-4-11-20200930/13895

---

## Post #1 by @tokjun (2020-10-06 15:35 UTC)

<p>Hi,</p>
<p>I am trying to use SliceTracker on the new Slicer release (4.11.20200930 Stable Release), but the Slicer fails to load the module (see the error message below). I’m wondering if anyone is facing the same issue. I’m running it on Ubuntu 20.04 LTS.</p>
<p>Thanks,</p>
<p>Junichi</p>
<p>Here’s the message I got on the Python Interactor:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/junichi/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/home/junichi/.config/NA-MIC/Extensions-29402/DeepInfer/lib/Slicer-4.11/qt-scripted-modules/DeepInfer.py", line 1, in &lt;module&gt;
    import Queue
ModuleNotFoundError: No module named 'Queue'
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/junichi/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/home/junichi/.config/NA-MIC/Extensions-29402/SliceTracker/lib/Slicer-4.11/qt-scripted-modules/SliceTracker.py", line 6, in &lt;module&gt;
    from SliceTrackerUtils.configuration import SliceTrackerConfiguration
  File "/home/junichi/.config/NA-MIC/Extensions-29402/SliceTracker/lib/Slicer-4.11/qt-scripted-modules/SliceTrackerUtils/configuration.py", line 1, in &lt;module&gt;
    import ConfigParser
ModuleNotFoundError: No module named 'ConfigParser'
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/junichi/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 674, in exec_module
  File "&lt;frozen importlib._bootstrap_external&gt;", line 781, in get_code
  File "&lt;frozen importlib._bootstrap_external&gt;", line 741, in source_to_code
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/home/junichi/.config/NA-MIC/Extensions-29402/SliceTracker/lib/Slicer-4.11/qt-scripted-modules/SliceTrackerRegistration.py", line 309
    raise AttributeError, "File not found: %s" % inputFile
                        ^
SyntaxError: invalid syntax
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/junichi/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/home/junichi/.config/NA-MIC/Extensions-29402/SliceTracker/lib/Slicer-4.11/qt-scripted-modules/SurfaceCutToLabel.py", line 11, in &lt;module&gt;
    from SegmentEditorSurfaceCutLib import SurfaceCutLogic
  File "/home/junichi/.config/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorSurfaceCutLib/__init__.py", line 4, in &lt;module&gt;
    from SegmentEditorEffect import *
ModuleNotFoundError: No module named 'SegmentEditorEffect'
TypeError: module.__init__() argument 1 must be str, not qSlicerScriptedLoadableModule</code></pre>

---

## Post #2 by @lassoan (2020-10-06 15:38 UTC)

<p>These module not found errors are probably just Python 2 -&gt; 3 changes. See these links for details:</p>
<ul>
<li><a href="https://stackoverflow.com/questions/46363871/no-module-named-queue">https://stackoverflow.com/questions/46363871/no-module-named-queue</a></li>
<li><a href="https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser">https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser</a></li>
</ul>

---

## Post #3 by @fedorov (2020-10-06 16:05 UTC)

<p><a class="mention" href="/u/che85">@che85</a> was the lead developer of this module, and it has not been maintained since he left the lab. Would be great to have it updated, contributions are most welcomed.</p>

---

## Post #4 by @tokjun (2020-10-06 16:27 UTC)

<p>Thanks! I’ll take a look when I find time.</p>

---

## Post #5 by @tokjun (2020-10-08 21:28 UTC)

<p>There seem to be several issues in SliceTracker as well as DeepInfer and SlicerSegmentEditorExtraEffects. See:</p>
<ul>
<li><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/37" rel="noopener nofollow ugc">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/37</a></li>
<li><a href="https://github.com/DeepInfer/Slicer-DeepInfer/pull/14" rel="noopener nofollow ugc">https://github.com/DeepInfer/Slicer-DeepInfer/pull/14</a></li>
<li><a href="https://github.com/SlicerProstate/SliceTracker/issues/358" rel="noopener nofollow ugc">https://github.com/SlicerProstate/SliceTracker/issues/358</a></li>
</ul>
<p>I made quick fixes to these modules, and SliceTracker seems to be loaded successfully.</p>

---

## Post #6 by @fedorov (2020-10-08 21:30 UTC)

<p>Thank you Junichi! Will you make pull requests with those modifications to the main repos?</p>

---

## Post #7 by @tokjun (2020-10-08 21:43 UTC)

<p>I’ve just sent pull requests for SliceTracker and SegmentEditorExtraEffects. I sent a request for DeepInfer, but Alireza mentioned that he still needed to fix other issues.</p>

---

## Post #8 by @tokjun (2020-10-14 04:01 UTC)

<p>Just an update - I worked on the module further, and it is working under limited conditions (no DeepInfer / mpReview). See: <a href="https://github.com/SlicerProstate/SliceTracker/issues/358" rel="noopener nofollow ugc">https://github.com/SlicerProstate/SliceTracker/issues/358</a></p>
<p>SliceTracker, SlicerDevelopmentToolbox, and DeepInfer must be updated. I mentioned earlier that SlicerSegmentEditorExtraEffects has an issue, but <a class="mention" href="/u/lassoan">@lassoan</a> advised me how to avoid it on the SliceTracker side.</p>

---

## Post #9 by @fedorov (2020-10-14 13:59 UTC)

<p><a class="mention" href="/u/tokjun">@tokjun</a> thank you for working on this.  I have not yet, but I will review and test PRs. <a class="mention" href="/u/che85">@che85</a> will you have a chance to take a look?</p>

---
