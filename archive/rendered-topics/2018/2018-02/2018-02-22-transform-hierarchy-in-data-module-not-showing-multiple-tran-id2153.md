# "Transform Hierarchy" in data module not showing multiple transforms correctly

**Topic ID**: 2153
**Date**: 2018-02-22
**URL**: https://discourse.slicer.org/t/transform-hierarchy-in-data-module-not-showing-multiple-transforms-correctly/2153

---

## Post #1 by @Nathan (2018-02-22 18:57 UTC)

<p>Hello,</p>
<p>I just updated to Slicer 4.8.1 and noticed that the “Transform hierarchy” is not behaving correctly. It does not show the correct “tree” of transformations. For example, I have images that have four transformations on them. It should show them like this:</p>
<p>A<br>
.B<br>
…C<br>
…D</p>
<p>However, it is showing transformation “C” not under transformation “B”</p>
<p>A<br>
.B<br>
C<br>
.D</p>
<p>If that doesn’t make sense, I can try to get a screenshot</p>
<p>It shows them correctly in the transformation module. This is a shame - I find it much easier to organize data/transforms in the data module.</p>
<p>This bug was actually present for me in version 4.5.0. However, I could get it to show the correct “tree” by switching back and forth between “displayable” and “transform” with the “Scene Model” popup. The new version tabbed screen doesn’t do that.</p>
<p>I am running Windows 7</p>
<p>-Nathan</p>

---

## Post #2 by @lassoan (2018-02-22 19:32 UTC)

<p>Please record a screen capture video or provide step-by-step instructions that we can use to reproduce it.</p>

---

## Post #3 by @Nathan (2018-02-26 18:54 UTC)

<p>Here is what I get when I open Slicer 4.6<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c89cbf46bdb1f9b44ec23176fe44ff227d14ae2d.png" data-download-href="/uploads/short-url/sCHk2ZCFHrds1V4VBNU59S5oiT3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c89cbf46bdb1f9b44ec23176fe44ff227d14ae2d_2_220x500.png" alt="image" data-base62-sha1="sCHk2ZCFHrds1V4VBNU59S5oiT3" width="220" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c89cbf46bdb1f9b44ec23176fe44ff227d14ae2d_2_220x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c89cbf46bdb1f9b44ec23176fe44ff227d14ae2d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c89cbf46bdb1f9b44ec23176fe44ff227d14ae2d.png 2x" data-dominant-color="F0F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">301×684 24.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is not correct. If I select the “Scene Model” popup and change to “Displayable” and then back to “Transform”, it appears correctly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75c2591c4cac1e7846ece7c4124f54f0fc4bb57.png" data-download-href="/uploads/short-url/uJa4Wd8AvCkYXnpkG8EXth0mYD5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d75c2591c4cac1e7846ece7c4124f54f0fc4bb57_2_217x500.png" alt="image" data-base62-sha1="uJa4Wd8AvCkYXnpkG8EXth0mYD5" width="217" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d75c2591c4cac1e7846ece7c4124f54f0fc4bb57_2_217x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75c2591c4cac1e7846ece7c4124f54f0fc4bb57.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75c2591c4cac1e7846ece7c4124f54f0fc4bb57.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">298×684 31.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In Slicer 4.8 it is always wrong.</p>

---

## Post #4 by @lassoan (2018-02-26 20:47 UTC)

<p>Please record a screen capture video or provide step-by-step instructions that we can use to reproduce it. If we cannot reproduce the problem we cannot fix it.</p>

---

## Post #5 by @Nathan (2018-02-26 21:09 UTC)

<p>There are no steps. I open up the scene and the transformation tree is wrong.</p>
<p>In slicer 4.5, you can switch the “Scene Model” popup as I described and it fixes it.</p>
<p>In slicer 4.8, this workaround doesn’t work.</p>
<p>Perhaps I have too many levels?</p>

---

## Post #6 by @lassoan (2018-02-26 22:07 UTC)

<p>Can you share the scene file with us (upload somewhere and post the link)? How did you create this scene?</p>

---

## Post #7 by @cpinter (2018-02-27 00:35 UTC)

<p>HI Nathan,</p>
<p>Sorry if this is too basic, but since 4.5 we overhauled the module, and now there is no Scene Model selection, but three tabs, in which Transform Hierarchy is not the default. Please double check that you select the middle tab in the Data module.</p>
<pre><code>                   |
                   V
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bccff3c01c74583d3a93904df20a52ed6dc12fe.png" data-download-href="/uploads/short-url/fnEibQDPaA5LZyt2523CE7C917g.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bccff3c01c74583d3a93904df20a52ed6dc12fe.png" alt="image" data-base62-sha1="fnEibQDPaA5LZyt2523CE7C917g" width="404" height="500" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">409×506 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Nathan (2018-02-27 12:19 UTC)

<p>Yes – I know about that.</p>
<p>I will show Andrey when he visits me today.</p>
<p>It’s probably something weird in my particular scene.</p>
<p>Thanks</p>

---

## Post #9 by @fedorov (2018-02-28 03:41 UTC)

<p>I checked, and Nathan was selecting the right tab.</p>

---

## Post #10 by @cpinter (2018-02-28 15:03 UTC)

<p>Of course, I suspected that my suggestion is too basic, but it was a possibility.</p>
<p>However at this point I can only say what Andras says:</p>
<ul>
<li>Please do a screen capture showing how to reproduce this from an empty scene</li>
<li>Or send us a scene where this issue is present when loading</li>
</ul>
<p>Both using a recent nightly please.</p>
<p>Thanks!</p>

---

## Post #11 by @mholden8 (2018-03-06 15:55 UTC)

<p>I experience the same issue as Nathan. Here are the steps that I can do to reproduce the issue (latest Slicer nightly 2018-03-05, Windows 10):</p>
<ol>
<li>Open fresh Slicer.</li>
<li>Create a transform node. Call it FirstTransformNode.</li>
<li>Save the scene.</li>
<li>Create a another transform node. Call it SecondTransformNode.</li>
<li>Make SecondTransformNode the parent of FirstTransformNode.</li>
<li>Save the scene.</li>
<li>Clear the scene.</li>
<li>Reload the saved scene created in Step 6.</li>
</ol>
<p>In the reloaded scene, SecondTransformNode does not appear to be the parent of FirstTransformNode in the Data module GUI (transform hierarchy tab). Likewise, in the Transforms module, FirstTransformNode does not appear to be transformed by SecondTransformNode in the GUI. But I observe that if I check the parent node of FirstTransformNode through the Python interactor, it is SecondTransformNode. See commands below:</p>
<p>firstTransformNode = slicer.util.getNode( “FirstTransformNode” )<br>
parentTransformNode = firstTransformNode.GetParentTransformNode()<br>
print( parentTransformNode )</p>

---

## Post #12 by @lassoan (2018-03-10 18:26 UTC)

<p>Thank you all, these steps helped a lot identifying the issue and develop a fix. See details in this issue: <a href="https://issues.slicer.org/view.php?id=4080">https://issues.slicer.org/view.php?id=4080</a></p>

---
