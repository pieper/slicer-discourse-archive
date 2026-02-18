# Load as a sagittal not axial

**Topic ID**: 2288
**Date**: 2018-03-11
**URL**: https://discourse.slicer.org/t/load-as-a-sagittal-not-axial/2288

---

## Post #1 by @timeanddoctor (2018-03-11 14:37 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bae3ab29346adda8f57a5e4cb233aa883ab846d.jpeg" data-download-href="/uploads/short-url/fmAnb8p6HvvtvlRfTJYwWUBR8tv.jpg?dl=1" title="360%E6%88%AA%E5%9B%BE-387699394" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bae3ab29346adda8f57a5e4cb233aa883ab846d_2_690x292.jpg" alt="360%E6%88%AA%E5%9B%BE-387699394" data-base62-sha1="fmAnb8p6HvvtvlRfTJYwWUBR8tv" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bae3ab29346adda8f57a5e4cb233aa883ab846d_2_690x292.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bae3ab29346adda8f57a5e4cb233aa883ab846d_2_1035x438.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bae3ab29346adda8f57a5e4cb233aa883ab846d.jpeg 2x" data-dominant-color="58565E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">360%E6%88%AA%E5%9B%BE-387699394</span><span class="informations">1051×445 44.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
how to load a picture as a yellow slicer without transform 90 degeree…</p>

---

## Post #2 by @lassoan (2018-03-11 17:27 UTC)

<p>Set the yellow slice orientation to Axial.</p>

---

## Post #3 by @timeanddoctor (2018-03-12 11:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/099e7464ede1def84d033f627fccd03d80efab67.jpeg" data-download-href="/uploads/short-url/1n5MEJ0xQppSerT003965LMSAh9.jpg?dl=1" title="2018-03-12_192210" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/099e7464ede1def84d033f627fccd03d80efab67_2_690x327.jpg" alt="2018-03-12_192210" data-base62-sha1="1n5MEJ0xQppSerT003965LMSAh9" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/099e7464ede1def84d033f627fccd03d80efab67_2_690x327.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/099e7464ede1def84d033f627fccd03d80efab67_2_1035x490.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/099e7464ede1def84d033f627fccd03d80efab67.jpeg 2x" data-dominant-color="8D8B8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-03-12_192210</span><span class="informations">1354×642 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @timeanddoctor (2018-03-12 11:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/ded83665677936c6bb2adb03ec803a8e236027ab.jpeg" data-download-href="/uploads/short-url/vNnem5jO9qlQ0sL6Il1PbAkzGNZ.jpg?dl=1" title="2018-03-12_192407" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded83665677936c6bb2adb03ec803a8e236027ab_2_690x373.jpg" alt="2018-03-12_192407" data-base62-sha1="vNnem5jO9qlQ0sL6Il1PbAkzGNZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded83665677936c6bb2adb03ec803a8e236027ab_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded83665677936c6bb2adb03ec803a8e236027ab_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/ded83665677936c6bb2adb03ec803a8e236027ab.jpeg 2x" data-dominant-color="848283"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-03-12_192407</span><span class="informations">1157×626 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-03-12 12:58 UTC)

<p>2D image files are always loaded as axial. If you want to load an image as sagittal then you need to use a 3D image file format, such as nrrd or metaimage (mhd). You can also change image orientation using Python scripting.</p>

---

## Post #6 by @timeanddoctor (2018-03-16 12:05 UTC)

<p>thank you very much！<br>
where can I find this Python scripting.<br>
Thanks.</p>

---

## Post #7 by @lassoan (2018-03-16 12:18 UTC)

<p>Press Ctrl-3 to see the Python console. You can then enter your Python commands there. You may complete <a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Programming_Tutorial">this tutorial</a> to get started.</p>

---
