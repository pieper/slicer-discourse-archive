---
topic_id: 12699
title: "Set Color And Opacity To All Visible Models"
date: 2020-07-22
url: https://discourse.slicer.org/t/12699
---

# Set Color and Opacity to all Visible Models

**Topic ID**: 12699
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/set-color-and-opacity-to-all-visible-models/12699

---

## Post #1 by @Ryan_Morrison (2020-07-22 23:07 UTC)

<p>I’d like to apply a R,G,B value and opacity to hundreds of models all at once. I would like to apply the color and opacity only to visible models in the 3D view. I’ve created a <a href="https://github.com/rgmorrison/Color_All_Visible_Models" rel="noopener nofollow ugc">python extension</a>, but the code is not quite there yet. Would someone be able to take a look and guide me as to how to fix the code?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05ab3bff3e73dc55e660a764fdb5ee15f6993c74.jpeg" data-download-href="/uploads/short-url/O9fPjk0dgdRlXn614WTrPeBnTK.jpeg?dl=1" title="color" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05ab3bff3e73dc55e660a764fdb5ee15f6993c74_2_690x331.jpeg" alt="color" data-base62-sha1="O9fPjk0dgdRlXn614WTrPeBnTK" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05ab3bff3e73dc55e660a764fdb5ee15f6993c74_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05ab3bff3e73dc55e660a764fdb5ee15f6993c74_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05ab3bff3e73dc55e660a764fdb5ee15f6993c74_2_1380x662.jpeg 2x" data-dominant-color="BCBDD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">color</span><span class="informations">2442×1174 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2020-07-22 23:28 UTC)

<p>You can use something like this to iterate over all of the model nodes in the scene, and change their color.</p>
<pre><code class="lang-auto">for modelNode in slicer.util.getNodesByClass("vtkMRMLModelNode"):
  if modelNode.GetHideFromEditors():
    continue # Skip hidden nodes, such as Red/Green/Yellow slice models
  modelDisplayNode = modelNode.GetDisplayNode()
  modelDisplayNode.SetColor(red,green,blue)
  modelDisplayNode.SetOpacity(opacity)
</code></pre>

---

## Post #3 by @lassoan (2020-07-23 01:19 UTC)

<p>You may also consider creating a hierarchy in Data module, as you can set color of all the nodes in a folder by right-clicking on the eye icon of the folder and choosing “Apply color to all children”.</p>

---

## Post #4 by @Ryan_Morrison (2020-07-23 02:21 UTC)

<p>Thanks Andras, I was not aware of the “Apply color to all children” option. This is a separate issue but do you know why 3DSlicer takes such a long time to turn and off visibility or apply a color to a large amount of models in a hierarchy (100+ models)?</p>

---

## Post #5 by @lassoan (2020-07-23 02:25 UTC)

<p>Update of hundreds of nodes is probably much faster if you start batch processing before the mass update and end batch processing when you finished. Also make sure you use latest Slicer Preview Release, as it contains lots of improvements and fixes.</p>

---

## Post #6 by @Ryan_Morrison (2020-07-23 02:35 UTC)

<p>I am using the most recent 3DSlicer. Toggling visibility in the data module is what is taking a long time when there are lot of models in one hierarchy.</p>

---

## Post #7 by @lassoan (2020-07-23 02:37 UTC)

<p>How long does it take? Can you share the scene with us?</p>
<p>Showing/hiding all the nodes in the entire NAC brain atlas (containing 300 models) takes less than a a second (by toggling visibility of a branch in data module). Can you check the performance of this on your computer? (you can get NAC brain atlas from DataStore module, Atlas collection category).</p>

---

## Post #8 by @Ryan_Morrison (2020-07-23 03:18 UTC)

<p>I did as you asked with the NAC brain atlas. The issue seems to be my computer as toggling visibility causes 3D slicer to hang for about a 45 seconds. Strange because my computer is a decently powerful computer since I built it myself (AMD 8320 cpu, GTX660ti gpu, 8gb 2600Mhz ram). None of the cpu, gpu, or ram percent usage are that high either in Task Manager during toggling of the nodes.</p>

---

## Post #9 by @lassoan (2020-07-23 03:42 UTC)

<p>Can you record a screen capture video or take a screenshot and mark where you click? Is it slow if you don’t add any observers to the scene?</p>

---

## Post #10 by @Ryan_Morrison (2020-07-23 03:52 UTC)

<p><a href="https://youtu.be/4Qrf7xjS5Cg" rel="nofollow noopener">Here is the video</a>. Even if I only view the red slice only and not the 3D view, the issue is still there.</p>

---

## Post #11 by @lassoan (2020-07-23 14:00 UTC)

<p>You still use the Slicer Stable Release. Please use latest Slicer Preview Release, as it contains lots of performance improvements, including show/hide of branches in hierarchies.</p>

---

## Post #12 by @Ryan_Morrison (2020-07-23 18:11 UTC)

<p>Wow, what an incredible performance difference! Upgrading to 4.11.0 fixed the issue. I really cannot thank you enough Andras and Kyle! Your fast response times and insightful tips are what enabled me to complete my project with 3DSlicer.</p>

---
