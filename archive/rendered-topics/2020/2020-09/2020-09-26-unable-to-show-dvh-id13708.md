# Unable to show DVH

**Topic ID**: 13708
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/unable-to-show-dvh/13708

---

## Post #1 by @calvin.kohwy (2020-09-26 06:07 UTC)

<p>Hi all</p>
<p>Upon loading my dose dicom in my slicer, I am able to compute DVH and show the dvh curve of my tumor target.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05dcc118c6b21d15a69ee6ee4ca95ded42edb5fc.png" data-download-href="/uploads/short-url/PRlM6LO1h4cINlhkYbY2V0Rlc8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcc118c6b21d15a69ee6ee4ca95ded42edb5fc_2_690x369.png" alt="image" data-base62-sha1="PRlM6LO1h4cINlhkYbY2V0Rlc8" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcc118c6b21d15a69ee6ee4ca95ded42edb5fc_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcc118c6b21d15a69ee6ee4ca95ded42edb5fc_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcc118c6b21d15a69ee6ee4ca95ded42edb5fc_2_1380x738.png 2x" data-dominant-color="F8F9F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×1013 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I tried computing the dvh for OAR for eg. Brainstem, it computes and showed the volume and intensity values. However, the graph does not show anything.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7be4443449b6a88104c5aa9d598130e2dacc7c77.png" data-download-href="/uploads/short-url/hFZMOQov2KDhmfvMXoSXiRk6UFV.png?dl=1" title="oardvh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be4443449b6a88104c5aa9d598130e2dacc7c77_2_690x370.png" alt="oardvh" data-base62-sha1="hFZMOQov2KDhmfvMXoSXiRk6UFV" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be4443449b6a88104c5aa9d598130e2dacc7c77_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be4443449b6a88104c5aa9d598130e2dacc7c77_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be4443449b6a88104c5aa9d598130e2dacc7c77_2_1380x740.png 2x" data-dominant-color="F9FBFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">oardvh</span><span class="informations">1914×1028 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I had tried exporting the dvh to csv file, but it showed no values.</p>
<p>Can anyone please advice!</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2020-09-26 13:49 UTC)

<p>First of all, please use a recent nightly, because 4.10.2 is two years old.</p>
<p>Second, if you open the individual structure list, then the DVH is calculated for the structure you have selected. It is usually better to calculate all.</p>

---

## Post #3 by @calvin.kohwy (2020-09-26 18:39 UTC)

<p>Hi Csaba</p>
<p>I found the issue which is if there is negative values in the dicom, it will stop it from plotting the dvh…</p>
<p>All is good now. Thank you</p>

---

## Post #4 by @cpinter (2020-09-28 11:09 UTC)

<p><a class="mention" href="/u/calvin.kohwy">@calvin.kohwy</a> Thanks for the update! This looks like a bug (I think negative dose values should be treated as 0 during calculation). Does this occur in the latest preview version as well?</p>

---

## Post #5 by @calvin.kohwy (2020-10-05 06:49 UTC)

<p>Yes, in the latest version, it happened as well!</p>

---
