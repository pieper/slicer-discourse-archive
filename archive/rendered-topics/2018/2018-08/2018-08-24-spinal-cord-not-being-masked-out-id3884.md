# Spinal cord not being masked out

**Topic ID**: 3884
**Date**: 2018-08-24
**URL**: https://discourse.slicer.org/t/spinal-cord-not-being-masked-out/3884

---

## Post #1 by @Saba_Shahab (2018-08-24 14:13 UTC)

<p>Operating system:<br>
NAME=“Ubuntu”<br>
VERSION=“16.04.3 LTS (Xenial Xerus)”<br>
ID=ubuntu<br>
ID_LIKE=debian<br>
PRETTY_NAME=“Ubuntu 16.04.3 LTS”<br>
VERSION_ID=“16.04”</p>
<p>Slicer version:<br>
Slicer nightly (updated as of 2018-08-20)</p>
<p>For a subset of subjects (all subjects from a single site), the mask generated includes the spinal cord. I am concerned that this may be a problem when subjects across all sites are being registered.</p>
<p>Is it a problem to have the spinal cord included in a subset of tractography results? If so, how do I mask it out?</p>
<p>Here is the code I am running: <a href="https://github.com/sabashahab/STOPPD_DTI/blob/master/SlicerTractography_edit.sh" rel="nofollow noopener">https://github.com/sabashahab/STOPPD_DTI/blob/master/SlicerTractography_edit.sh</a></p>

---

## Post #2 by @ljod (2018-08-24 14:30 UTC)

<p>Hi Saba. One possibility is to manually edit the mask to disconnect the brain part from the spinal cord part, then to remove the “island” of the spinal cord.</p>

---

## Post #3 by @Saba_Shahab (2018-08-24 14:51 UTC)

<p>Would that mean manually editing it for every single subject? There are 72 subjects - manually editing them would be very time-consuming.</p>

---

## Post #4 by @ljod (2018-08-24 15:13 UTC)

<p>IT could be pretty quick. Choose one axial slice, erase the connection between brain and spinal cord, then save only the largest island (the brain). This should be only a few minutes at most. Others on here know more about the new Segment Editor, which may be even faster. With the old Editor I think this should take maybe 2-3 minutes per subject once you have decided how to do it.</p>

---

## Post #5 by @Saba_Shahab (2018-08-24 19:07 UTC)

<p>Sure. Where can I find instructions on how to do this?</p>

---

## Post #6 by @ihnorton (2018-08-25 17:51 UTC)

<blockquote>
<p>Where can I find instructions on how to do this?</p>
</blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>
<p>and</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>
<p>Specifically, for the task <a class="mention" href="/u/ljod">@ljod</a> mentioned, you can use the scissors tool to quickly clear all of the unwanted label region with a cut in one slice. For example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38b1b4d8e93c407a2de323f7c31ee95356a814bf.gif" data-download-href="/uploads/short-url/85xtiLXjr0pY6NuG5Oc63otFU6z.gif?dl=1" title="2"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38b1b4d8e93c407a2de323f7c31ee95356a814bf_2_690x377.gif" alt="2" data-base62-sha1="85xtiLXjr0pY6NuG5Oc63otFU6z" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38b1b4d8e93c407a2de323f7c31ee95356a814bf_2_690x377.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38b1b4d8e93c407a2de323f7c31ee95356a814bf_2_1035x565.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38b1b4d8e93c407a2de323f7c31ee95356a814bf.gif 2x" data-dominant-color="A7A7AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1265×692 787 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @ljod (2018-08-25 20:34 UTC)

<p>Thanks Isaiah. Regarding the video, it is probably faster if you edit in one axial slice to separate the brain and spinal cord at the level corresponding to the other scans in your study. Then figure out how to remove the smaller segmented “island” of the spinal cord. If I understand the video it is only removing some of the spinal cord and instead you want to do it all by separating it.</p>

---

## Post #8 by @ihnorton (2018-08-26 00:57 UTC)

<aside class="quote no-group" data-username="ljod" data-post="7" data-topic="3884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ljod/48/652_2.png" class="avatar"> ljod:</div>
<blockquote>
<p>edit in one axial slice to separate the brain and spinal cord at the level corresponding to the other scans in your study. Then figure out how to remove the smaller segmented “island” of the spinal cord.</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d3bd30155c2521ca5b8617f6cd9053e7bb6723.gif" data-download-href="/uploads/short-url/inELqwwO770K3VFSz8VSwO1dhmz.gif?dl=1" title="4"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80d3bd30155c2521ca5b8617f6cd9053e7bb6723_2_690x374.gif" alt="4" data-base62-sha1="inELqwwO770K3VFSz8VSwO1dhmz" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80d3bd30155c2521ca5b8617f6cd9053e7bb6723_2_690x374.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/80d3bd30155c2521ca5b8617f6cd9053e7bb6723_2_1035x561.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80d3bd30155c2521ca5b8617f6cd9053e7bb6723.gif 2x" data-dominant-color="A5A5AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1265×686 642 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @ihnorton (2018-08-26 01:03 UTC)

<aside class="quote no-group" data-username="ljod" data-post="7" data-topic="3884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ljod/48/652_2.png" class="avatar"> ljod:</div>
<blockquote>
<p>If I understand the video it is only removing some of the spinal cord and instead you want to do it all by separating it.</p>
</blockquote>
</aside>
<p>Btw, the scissors cut in all planes at once by default, so the first <a href="https://discourse.slicer.org/t/spinal-cord-not-being-masked-out/3884/6">example</a> was deleting in the other planes too with the one swipe.</p>
<p>However, there is also a negative (or positive) mode, which allows to cut only above/below a specific slice. Doing that is similar to the one-slice-separation/island-removal strategy.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9ecfc2cf6f66684f76f8cc5a2b86263690701f.png" data-download-href="/uploads/short-url/4e267ZPiJ96zwmo1JtUSQQgVIMn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9ecfc2cf6f66684f76f8cc5a2b86263690701f.png" alt="image" data-base62-sha1="4e267ZPiJ96zwmo1JtUSQQgVIMn" width="690" height="201" data-dominant-color="EBEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">870×254 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37a7e10fdb10137ed02aa31f0aa0c132e6465041.gif" alt="3" data-base62-sha1="7WlWitDOS89nvVdydodTHiUyAlH" width="653" height="326"></p>

---

## Post #10 by @ljod (2018-08-26 01:53 UTC)

<p>This looks like the perfect way to do this. Thanks Isaiah.</p>

---

## Post #11 by @Saba_Shahab (2018-08-27 18:02 UTC)

<p>Thank you, Isaiah and Lauren. The solution works!</p>

---
