---
topic_id: 10509
title: "Error When Using Segmentmesher"
date: 2020-03-02
url: https://discourse.slicer.org/t/10509
---

# Error when using segmentmesher

**Topic ID**: 10509
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/error-when-using-segmentmesher/10509

---

## Post #1 by @Aep93 (2020-03-02 22:37 UTC)

<p>Hello all,<br>
I got the following error when I want to mesh my segmentations in segmentmesher:</p>
<p>./config/NA-MIC/Extensions-28797/SegmentMesher/lib/Slicer-4.11/qt-scripted-modules/SegmentMesher.py", line 296, in onApplyButton<br>
self.cleaverPaddingPercentSpinBox.value * 0.01)</p>
<p>./config/NA-MIC/Extensions-28797/SegmentMesher/lib/Slicer-4.11/qt-scripted-modules/SegmentMesher.py", line 569, in createMeshFromSegmentationCleaver<br>
self.logProcessOutput(ep, self.cleaverFilename)</p>
<p>./config/NA-MIC/Extensions-28797/SegmentMesher/lib/Slicer-4.11/qt-scripted-modules/SegmentMesher.py", line 472, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, processName)<br>
subprocess.CalledProcessError: Command ‘cleaver-cli’ died with &lt;Signals.SIGKILL: 9&gt;.</p>
<p>Does any body know what are these errors related to?</p>

---

## Post #2 by @lassoan (2020-03-03 01:28 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="1" data-topic="10509">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>Signals.SIGKILL: 9</p>
</blockquote>
</aside>
<p>It means that the kernel killed your process, <a href="https://stackoverflow.com/questions/726690/what-killed-my-process-and-why">most likely because you have run out of memory</a>. Increase the swap space or lower your memory usage (by reducing the size of input volume or resolution of the output mesh).</p>

---

## Post #3 by @Aep93 (2020-03-03 15:05 UTC)

<p>Thank you very much for your answer. You are correct I monitored my memory and found that the memory limit is causing this error. How can I reduce the size of input volume? Should I do the segmentations again?<br>
Thanks</p>

---

## Post #4 by @lassoan (2020-03-05 01:39 UTC)

<p>No need to segment again. You can tune meshing parameters as described here: <a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters">https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters</a>. If the description is not clear enough then just try to change the parameters and see how it impacts the output. You may learn it on a smaller, simpler mesh, and once you are confident you can switch to your large mesh.</p>
<p>You can also increase swap space to prevent running out of memory (but execution may become much slower).</p>

---

## Post #5 by @Aep93 (2020-03-05 16:29 UTC)

<p>Thank you very much for your help.</p>

---
