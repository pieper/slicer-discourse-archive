---
topic_id: 24409
title: "Understanding Coordinates"
date: 2022-07-20
url: https://discourse.slicer.org/t/24409
---

# Understanding coordinates

**Topic ID**: 24409
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/understanding-coordinates/24409

---

## Post #1 by @anitakh1 (2022-07-20 11:35 UTC)

<p>Kindly let me know what these negative coordinated of coorX, coorY and coorZ means in this .csv file. when i open patient’s data in 3D slicer, I can view x,y,z coordinates in positive values<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/726cb8d301c0cf5c430587e59cb03a0f45601988.png" data-download-href="/uploads/short-url/gkfmMce4n64Sr3cjcLF04qAq2dG.png?dl=1" title="Screenshot (98)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726cb8d301c0cf5c430587e59cb03a0f45601988_2_690x388.png" alt="Screenshot (98)" data-base62-sha1="gkfmMce4n64Sr3cjcLF04qAq2dG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726cb8d301c0cf5c430587e59cb03a0f45601988_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726cb8d301c0cf5c430587e59cb03a0f45601988_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726cb8d301c0cf5c430587e59cb03a0f45601988_2_1380x776.png 2x" data-dominant-color="DDE1DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (98)</span><span class="informations">1920×1080 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-07-21 17:55 UTC)

<p>Can you describe where you got the csv file and what you expect the values to mean?</p>

---

## Post #3 by @muratmaga (2022-07-21 22:00 UTC)

<p>This comes up quite often for new users. Slicer uses RAS internally to display the point coordinates, but writes them as LPS to disk (fcsv or json files) for compatibility with other software. RAS to LPS involves negation of the values of first two coordinates. In recent slicers, you can export a table of of these coordinates either LPS or RAS, using the export Table option.</p>
<p><strong>LPS Exported coordinates</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0daec64730eb8300e1d66ab2a500eae7dd50032.jpeg" data-download-href="/uploads/short-url/rw4ImCXyS9em6K41nSUKkBXyw70.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0daec64730eb8300e1d66ab2a500eae7dd50032_2_687x500.jpeg" alt="image" data-base62-sha1="rw4ImCXyS9em6K41nSUKkBXyw70" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0daec64730eb8300e1d66ab2a500eae7dd50032_2_687x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0daec64730eb8300e1d66ab2a500eae7dd50032.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0daec64730eb8300e1d66ab2a500eae7dd50032.jpeg 2x" data-dominant-color="BBBCBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×720 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>RAS Exported coords</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11d176300b935cdcd23f38307e38768820cbaa7c.png" data-download-href="/uploads/short-url/2xCSXVpjIKdtGOqiHnczbfm0wdm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11d176300b935cdcd23f38307e38768820cbaa7c_2_669x500.png" alt="image" data-base62-sha1="2xCSXVpjIKdtGOqiHnczbfm0wdm" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11d176300b935cdcd23f38307e38768820cbaa7c_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11d176300b935cdcd23f38307e38768820cbaa7c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11d176300b935cdcd23f38307e38768820cbaa7c.png 2x" data-dominant-color="BDBEBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">974×727 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @anitakh1 (2022-07-27 05:23 UTC)

<p>thanks for reply. But how to find “export coordinate system”. what about CoorZ values sir? Can I see images showing LPS coordinates and not RAS?</p>

---

## Post #5 by @anitakh1 (2022-07-27 05:25 UTC)

<p>I am try to scan LUNA16 images and they have provided annotated .csv file to look for cancer location which i shared.<br>
thank you</p>

---

## Post #6 by @lassoan (2022-07-27 10:42 UTC)

<p>LUNA16 sample data set providers have chosen ambiguous names in their coordinate system axes (<code>coordX</code>, <code>coordY</code>, and <code>coordZ</code>), but it seems that the coordinates are actually in LPS coordinate system.</p>
<p>Therefore, you can load these points by renaming the columns to <code>label</code>, <code>r</code>, <code>a</code>, <code>s</code>, and load them into Slicer as a table:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07df691cd23b17be394d2796d9289b037f9618f9.png" data-download-href="/uploads/short-url/17DZPzyDcDlF6F7UxVuF5SEtL2F.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07df691cd23b17be394d2796d9289b037f9618f9_2_488x500.png" alt="image" data-base62-sha1="17DZPzyDcDlF6F7UxVuF5SEtL2F" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07df691cd23b17be394d2796d9289b037f9618f9_2_488x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07df691cd23b17be394d2796d9289b037f9618f9_2_732x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07df691cd23b17be394d2796d9289b037f9618f9_2_976x1000.png 2x" data-dominant-color="393939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1199×1227 81.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then in Markups module create a new point list and import the table:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/202585dc584756f96ef4bbf63984d8b81be6a65b.png" data-download-href="/uploads/short-url/4AnFDb9CTWCZaBMGWBhjVyaseAH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/202585dc584756f96ef4bbf63984d8b81be6a65b_2_441x499.png" alt="image" data-base62-sha1="4AnFDb9CTWCZaBMGWBhjVyaseAH" width="441" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/202585dc584756f96ef4bbf63984d8b81be6a65b_2_441x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/202585dc584756f96ef4bbf63984d8b81be6a65b_2_661x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/202585dc584756f96ef4bbf63984d8b81be6a65b_2_882x998.png 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1161×1315 83.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This makes all points to show up, which may be impractical (and very slow, unless you hide the point labels and/or disable interaction with the points).</p>
<p>Instead of dumping all points into a point list, you may want to display a sphere at the specified position. See an example code snippet for that in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node">script repository</a>.</p>

---
