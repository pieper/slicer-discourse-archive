# 3rd Proxy works only in SequenceBrowser 1, but not in SeqBrowser 2. What happened with the Scene file?

**Topic ID**: 25404
**Date**: 2022-09-22
**URL**: https://discourse.slicer.org/t/3rd-proxy-works-only-in-sequencebrowser-1-but-not-in-seqbrowser-2-what-happened-with-the-scene-file/25404

---

## Post #1 by @sunshine (2022-09-22 21:47 UTC)

<p>Hi everyone,</p>
<p>I saved a scene file that contains two SequenceBrowser info, each SequenceBrowser has three Sequence nodes.<br>
Please find the folder of the <a href="https://www.dropbox.com/s/crfzg4y189un571/33__SR__Aug_25_Test.zip" rel="noopener nofollow ugc">Scene files here</a></p>
<p>However, after I re-load this scene file, the third proxy node works only in the first SequenceBrowser, and does not work in the 2nd SequenceBrowser.</p>
<p>All the data seems fine to me, but as far as I know, the 3rd Sequence Node in the 2nd SequenceBrowser is has no access to the sequence data.</p>
<p>Could anyone help me take a look into the scene file, and let me know what was wrong in the scene file?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @sunshine (2022-10-10 16:01 UTC)

<p>There might be a problem with the Save procedure.<br>
Exact same sequence, here is the BeyoundCompare result between a good save and a bad save.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8282293ef5a856e0b3bfe2e3d42978031a31315e.png" data-download-href="/uploads/short-url/iCwWhBSw7PB2fvGlTHFUlhTI5pc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8282293ef5a856e0b3bfe2e3d42978031a31315e_2_690x349.png" alt="image" data-base62-sha1="iCwWhBSw7PB2fvGlTHFUlhTI5pc" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8282293ef5a856e0b3bfe2e3d42978031a31315e_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8282293ef5a856e0b3bfe2e3d42978031a31315e_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8282293ef5a856e0b3bfe2e3d42978031a31315e_2_1380x698.png 2x" data-dominant-color="F7F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1901×962 39.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please kindly share any ideas on how to avoid this.</p>
<p>All the sequence data work well before saving, however, after saving and re-load, the sequence is empty, and you can see the difference between a good save and a bad save.<br>
I am still trying to figure out why the saving procedure doesn’t work.</p>
<p>Thank you so much in advance!</p>

---

## Post #3 by @lassoan (2022-11-07 19:12 UTC)

<p>Thanks for reporting this and sorry for this taking a long time to respond. The issue has been <a href="https://github.com/Slicer/Slicer/commit/60f774c03c89a0061e8619760fa36d5501291808">fixed recently in the Slicer Preview Release</a> and will be included in the upcoming Slicer-5.2 Slicer Stable Release.</p>

---
