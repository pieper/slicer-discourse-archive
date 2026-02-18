# Slicer-RT Contour Analysis 

**Topic ID**: 18563
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/slicer-rt-contour-analysis/18563

---

## Post #1 by @liam-stubbington (2021-07-07 12:30 UTC)

<p>Hi,</p>
<p>Massive fun of the 3D slicer project but a newbie.</p>
<p>I want to install the Slicer RT extension - specifically I want to make liberal use of the contour analysis module.</p>
<p>I am working within a hospital network so I suspect that security settings are wreaking havoc because I cannot download extensions via the extension manager.</p>
<p>I have had some success downloading Slicer RT manually.</p>
<p>However, when I use the install extensions from file button I get as far as the point at which the restart option should become available - but it just hangs.</p>
<p>I’m running 3D Slicer r29738 and the SlicerRT extension I have downloaded is r26654 - could this be the issue?</p>
<p>If I can’t get around this, would it be feasible to just add the Contour Analysis Module manually to 3D Slicer, since this is all I wish to do with SlicerRT at the moment.</p>
<p>Thanks for you help.</p>

---

## Post #2 by @cpinter (2021-07-07 12:42 UTC)

<aside class="quote no-group" data-username="liam-stubbington" data-post="1" data-topic="18563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/liam-stubbington/48/11513_2.png" class="avatar"> liam-stubbington:</div>
<blockquote>
<p>I’m running 3D Slicer r29738 and the SlicerRT extension I have downloaded is r26654 - could this be the issue?</p>
</blockquote>
</aside>
<p>Yes, it will not be compatible.</p>
<p>Please download and install the latest preview version. Due to a recent change now you can install Slicer in your user’s local directory, and the extensions and settings will be stored there as well, so permissions will not be a problem.</p>

---

## Post #3 by @liam-stubbington (2021-07-07 13:15 UTC)

<p>Will do, thanks!</p>
<p>Does this also explain why, after matching the extension and Slicer version number, I keep on running out of memory when calculating DICE for two simple structure sets?</p>
<p>Thanks for you help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10aa84d34496cb1bc8f9d7c71a9845d290688bbb.png" data-download-href="/uploads/short-url/2nqYpSOVf54oNZTDeUwIbxqtX63.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10aa84d34496cb1bc8f9d7c71a9845d290688bbb_2_690x359.png" alt="image" data-base62-sha1="2nqYpSOVf54oNZTDeUwIbxqtX63" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10aa84d34496cb1bc8f9d7c71a9845d290688bbb_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10aa84d34496cb1bc8f9d7c71a9845d290688bbb_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10aa84d34496cb1bc8f9d7c71a9845d290688bbb_2_1380x718.png 2x" data-dominant-color="B1C3B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1924×1003 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2021-07-07 13:22 UTC)

<p>No, this is unrelated. After a quick search on memory allocation you will see several topics here on the forum that will help you.</p>

---
