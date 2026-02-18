# Different file formats unavailable

**Topic ID**: 9105
**Date**: 2019-11-11
**URL**: https://discourse.slicer.org/t/different-file-formats-unavailable/9105

---

## Post #1 by @Purkinje (2019-11-11 19:50 UTC)

<p>Dear All,</p>
<p>I have installed 3D Slicer recently. I have been working with some maps, but when I go to save the file, I just can choose the format *.nrrd/.nhdr… There are not other file formats to choose.</p>
<p>Do you know the reasons?</p>
<p>Thanks in advance,</p>
<p>Operating system:Windows<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-11-11 19:53 UTC)

<p>I assume you would like to export image segmentation as a labelmap volume to use in a third-party software. For this, go to Data module, right-click on the segmentatation node, and choose Export to labelmap. Then using File / Save scene, you can save into a wide range of file formats.</p>
<p>I would recommend to upgrade to latest stable release of Slicer (currently 4.10.2).</p>

---

## Post #3 by @Purkinje (2019-11-11 23:40 UTC)

<p>Thanks. But the problem I have found it is that when I am going to save I cannot find other file formats. I have been working with texture maps, and then, when I want to save the map, it just allows me .nrrd format. No other formats are available, like .nii.</p>

---

## Post #4 by @lassoan (2019-11-12 00:24 UTC)

<p>Go to Data module, right-click on the segmentatation node, and choose Export to labelmap. Then using File / Save scene, you can save the exported labelmap into a wide range of file formats, including nifti (.nii).</p>

---

## Post #5 by @Purkinje (2019-11-12 13:47 UTC)

<p>Thanks again for your answer.<br>
I have followed your guide, but still I have problems. Please, see attached two screenshots.<br>
Regardless of the message, it is true that when I go to File/Save, now I can find a wide range of formats. If I save it, the image is empty. Should I select any other parameter in the segmentation tool?<br>
Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/817af43bf7295f5490cc4bc266b93828c293c923.jpeg" data-download-href="/uploads/short-url/itr1kEW5pzXylyRQ6DoEJUjUYan.jpeg?dl=1" title="print_screen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/817af43bf7295f5490cc4bc266b93828c293c923_2_690x365.jpeg" alt="print_screen" data-base62-sha1="itr1kEW5pzXylyRQ6DoEJUjUYan" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/817af43bf7295f5490cc4bc266b93828c293c923_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/817af43bf7295f5490cc4bc266b93828c293c923_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/817af43bf7295f5490cc4bc266b93828c293c923_2_1380x730.jpeg 2x" data-dominant-color="6E6D6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">print_screen</span><span class="informations">2555×1354 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bd2d0c8c1f393c2a83e68c69e72238a8cbbb45b.jpeg" data-download-href="/uploads/short-url/fnQL5TNCuaHaY8zMaLbaKukkBPd.jpeg?dl=1" title="print_screen_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd2d0c8c1f393c2a83e68c69e72238a8cbbb45b_2_690x370.jpeg" alt="print_screen_2" data-base62-sha1="fnQL5TNCuaHaY8zMaLbaKukkBPd" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd2d0c8c1f393c2a83e68c69e72238a8cbbb45b_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd2d0c8c1f393c2a83e68c69e72238a8cbbb45b_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bd2d0c8c1f393c2a83e68c69e72238a8cbbb45b_2_1380x740.jpeg 2x" data-dominant-color="8D8C8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">print_screen_2</span><span class="informations">2560×1374 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2019-11-12 13:58 UTC)

<p>You don’t have any segments in your segmentation node, so there is nothing to save.</p>

---

## Post #7 by @Purkinje (2019-11-12 14:57 UTC)

<p>Now there is a segment in the segmentation node and the result is the same…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/defc9e8e17f7171cb5344e53ebb0f5e544194e9f.jpeg" data-download-href="/uploads/short-url/vODerjHVAvyQyel4DPO8PKX79gz.jpeg?dl=1" title="print_screen_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/defc9e8e17f7171cb5344e53ebb0f5e544194e9f_2_690x363.jpeg" alt="print_screen_3" data-base62-sha1="vODerjHVAvyQyel4DPO8PKX79gz" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/defc9e8e17f7171cb5344e53ebb0f5e544194e9f_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/defc9e8e17f7171cb5344e53ebb0f5e544194e9f_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/defc9e8e17f7171cb5344e53ebb0f5e544194e9f_2_1380x726.jpeg 2x" data-dominant-color="696868"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">print_screen_3</span><span class="informations">2560×1350 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2019-11-12 18:40 UTC)

<p>Do you have anything in that segment?</p>
<aside class="quote no-group" data-username="Purkinje" data-post="1" data-topic="9105">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/7bcc69/48.png" class="avatar"> Purkinje:</div>
<blockquote>
<p>I have been working with some maps, but when I go to save the file</p>
</blockquote>
</aside>
<p>I assumed that by “map” you mean segmentation. Is that correct?</p>
<p>On the screenshots all I see is a masked volume, so it is not clear what you would like to with it.</p>

---

## Post #9 by @Purkinje (2019-11-13 17:34 UTC)

<p>I have found the solution through texture features.</p>
<p>Thanks</p>

---
