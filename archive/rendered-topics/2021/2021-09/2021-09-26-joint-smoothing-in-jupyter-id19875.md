# Joint smoothing in jupyter

**Topic ID**: 19875
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/joint-smoothing-in-jupyter/19875

---

## Post #1 by @Tekk_ya (2021-09-26 17:28 UTC)

<p>Hi,</p>
<p>I want to read two files, one as a volume and another as a segmentation. The segmentation file is the label map including different segments. I am interested in applying a “joint smoothing” on the adjacent segments. I have several questions in this regard:</p>
<ol>
<li>What is the proper way for reading/importing a .nii file as a segmentation with a python code?</li>
<li>What is the proper way for selecting the desired segments for the joint smoothing function?</li>
<li>What is the correct syntax for activating the joint smoothing function? I have seen several examples for median smoothing like bellow, but I am missing the syntax for enabling the joint smoothing?<br>
Here is the example for the median filter that I have found:</li>
</ol>
<p>segmentEditorWidget.setActiveEffectByName(“Smoothing”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“SmoothingMethod”, “MEDIAN”)<br>
effect.setParameter(“KernelSizeMm”, 3)<br>
effect.self().onApply()</p>
<p>Thank you in advance for your help.</p>

---

## Post #2 by @lassoan (2021-09-27 03:39 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="19875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>What is the proper way for reading/importing a .nii file as a segmentation with a python code?</p>
</blockquote>
</aside>
<p>The simplest is to use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadSegmentation"><code>slicer.util.loadSegmentation</code></a> function:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentationNode = slicer.util.loadSegmentation('c:/tmp/Segmentation.nii')
</code></pre>
<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="19875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>What is the proper way for selecting the desired segments for the joint smoothing function?</p>
</blockquote>
</aside>
<p>Joint smoothing is applied to all visible segments. You can adjust visibility using <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#aee65fdd850b42e1b1d1f7117bc082b92">SetSegmentVisibility</a> method of the segmentation display node. See examples <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-segmentation-display-options">here</a>.</p>
<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="19875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>What is the correct syntax for activating the joint smoothing function?</p>
</blockquote>
</aside>
<p>See description of the Smoothing effect parameters <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#smoothing">here</a>.</p>
<p>You need to use <code>SmoothingMethod</code> = <code>JOINT_TAUBIN</code> and <code>JointTaubinSmoothingFactor</code> = the smoothing factor you want to use.</p>

---

## Post #3 by @Tekk_ya (2021-09-28 10:52 UTC)

<p>Dear Andras,</p>
<p>Thank you for your quick reply. I found your suggested links super helpful. Best</p>

---

## Post #4 by @lassoan (2021-10-07 13:46 UTC)

<p>A post was split to a new topic: <a href="/t/making-joint-smoothing-faster/20053">Making joint smoothing faster</a></p>

---
