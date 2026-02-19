---
topic_id: 9356
title: "Loading A Scalars File Mgh Overlay For A Model Node Pial Via"
date: 2019-12-02
url: https://discourse.slicer.org/t/9356
---

# Loading a Scalars file (.mgh) Overlay for a Model Node (.pial) via Python

**Topic ID**: 9356
**Date**: 2019-12-02
**URL**: https://discourse.slicer.org/t/loading-a-scalars-file-mgh-overlay-for-a-model-node-pial-via-python/9356

---

## Post #1 by @Aping (2019-12-02 21:26 UTC)

<p>Hi slicer experts,<br>
I am working to load &gt;100 .mgh files overlay model which I want to make a video for demo.<br>
I can load the model by:<br>
model  = slicer.util.loadModel(‘lh.pial’)<br>
But, how to load the surface file (.mgh) overlay the model. I tested these command but failed.<br>
surface = slicer.util.loadScalarOverlay(‘lh_filed.mgh’)<br>
I found the function (slicer.util.openAddScalarOverlayDialog()) works, but you had to select the (.mgh) file manually.<br>
Is there a function can load .mgh automatically to overlay the loaded model?</p>
<p>Best wishes,</p>
<p>Operating system: Centos 7<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #3 by @lassoan (2019-12-03 04:42 UTC)

<p>It seems that <code>loadScalarOverlay</code> convenience function does not expose the option to specify referenced node.</p>
<pre><code class="lang-python">modelNode = slicer.util.loadModel(surfaceFilename)
slicer.util.loadNodeFromFile(overlayFilename, 'ScalarOverlayFile', {'modelNodeId': modelNode.GetID()})
</code></pre>
<p>(this above works on recent Slicer Preview Releases, for stable release, you need to specify <code>returnNode=True</code> for loadModel and it returns a success flag and a model node)</p>
<p>I’ll update <code>slicer.util.loadScalarOverlay</code> to take an optional model node ID.</p>

---

## Post #4 by @Aping (2019-12-03 19:39 UTC)

<p>Thanks, Iassoan.<br>
I found it still cannot overlay.<br>
I run as follows:</p>
<pre><code class="lang-auto"> modelNode = slicer.util.loadModel('lh.pial',  returnNode=True) % it can load the model to 3DSlicer, but I fount the modelNode did not have attribution GetID
 slicer.util.loadNodeFromFile(overlayFilename, 'ScalarOverlayFile', {'modelNodeId': modelNode.GetID()})
% it failed.
</code></pre>
<p>The error message as follows:<br>
AttributeError: ‘tuple’ object has no attribute ‘GetID’<br>
Can you tell me how to deal with the problem? how to obtain the node ID as you said above?</p>
<p>Thanks in advance.</p>

---

## Post #5 by @Aping (2019-12-03 19:41 UTC)

<p>About version: I tested 4.8.1 and 4.10.1</p>

---

## Post #6 by @Aping (2019-12-03 20:13 UTC)

<p>Thanks Iassoan. I update the version and it works now.<br>
Thanks again.</p>
<p>Best wishes,</p>

---
