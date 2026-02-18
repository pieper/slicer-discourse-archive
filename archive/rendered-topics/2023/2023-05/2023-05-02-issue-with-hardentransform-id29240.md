# Issue with HardenTransform

**Topic ID**: 29240
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/issue-with-hardentransform/29240

---

## Post #1 by @Gholl (2023-05-02 09:54 UTC)

<p>I’m writing a script and trying to apply HardenTransform on a segmentation node as follows.</p>
<pre><code class="lang-auto">seg_node.SetAndObserveTransformNodeID(transformNodeID.GetID())
seg_node.HardenTransform()
</code></pre>
<p>This works fine for most samples but sometimes the script crashes (triggered at HardenTransform) and yields the following error:</p>
<pre><code class="lang-auto">Unable to allocate 227735193073740 elements of size 4 bytes. 

"Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing swap size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at https://slicer.org\n\n\nThe message detail is:\n\nException thrown in event: std::bad_alloc"
</code></pre>
<p>transformNode has <code>slizeSizeMM = [float(15.0), float(15.0)]</code> but when changing to e.g. <code>slizeSizeMM = [float(13.0), float(13.0)]</code> the script works fine on the samples triggering this error.</p>
<p>From what I’ve read earlier there are some issues related to HardenTransform on large segmentations (see <a href="https://discourse.slicer.org/t/harden-transform-on-large-segmentation-hangs-3d-slicer/5643" class="inline-onebox">Harden transform on large segmentation hangs 3D Slicer</a>). In my case, the underlying segmentations seem to be “longer” than normal relative to other samples.</p>
<p>Is there any effective more general solution to this issue?</p>
<p>OS: Ubuntu 20.04<br>
Slicer3D version: 5.2.2</p>
<p>Thanks!</p>

---

## Post #2 by @Gholl (2023-05-02 13:02 UTC)

<p>Typo, should be:</p>
<pre><code class="lang-auto">seg_node.SetAndObserveTransformNodeID(transformNode.GetID())
seg_node.HardenTransform()
</code></pre>

---

## Post #3 by @lassoan (2023-05-02 19:51 UTC)

<p>If you specify a transform that would make the resulting segmentation so big that it cannot fit into memory then the operation is expected to fail. We can tell if it is a software issue or just incorrect input if you provide a sample data set and processing script that reproduces the problem.</p>

---

## Post #4 by @Gholl (2023-05-03 10:38 UTC)

<p>Ok, that makes sense. Unfortunately, I cannot provide you with sample data.   Is there any way to catch this error instead of having the script crash?</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2023-05-03 11:55 UTC)

<p>You can try to reproduce it with data sets in Slicer"s Sample Data module or other public data sets.</p>

---
