---
topic_id: 34131
title: "Generating Surface Area From A 3D Region"
date: 2024-02-03
url: https://discourse.slicer.org/t/34131
---

# Generating surface area from a 3D region

**Topic ID**: 34131
**Date**: 2024-02-03
**URL**: https://discourse.slicer.org/t/generating-surface-area-from-a-3d-region/34131

---

## Post #1 by @Logan_Moore (2024-02-03 06:58 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.6.1</p>
<p>Hi all!</p>
<p>I am currently working on a set of human crania, and I am trying to quantify the 3D surface area of the region in the closed curve. I see that it generates an area but I am assuming that is just the area of the closed circle. How could I go about getting the surface area of the whole region up to the F1 landmark?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/965ba843b320b6242f4b8c2fffefa0adafdbb45f.jpeg" data-download-href="/uploads/short-url/ls7ZIhrbO2pwDJ3wFYA93ptp4tx.jpeg?dl=1" title="ROI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/965ba843b320b6242f4b8c2fffefa0adafdbb45f_2_633x500.jpeg" alt="ROI" data-base62-sha1="ls7ZIhrbO2pwDJ3wFYA93ptp4tx" width="633" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/965ba843b320b6242f4b8c2fffefa0adafdbb45f_2_633x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/965ba843b320b6242f4b8c2fffefa0adafdbb45f_2_949x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/965ba843b320b6242f4b8c2fffefa0adafdbb45f_2_1266x1000.jpeg 2x" data-dominant-color="574630"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI</span><span class="informations">1356×1071 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is worth noting that these images are derived from a 3D surface scanner as we don’t have access to a CT machine. I will say that I am primarily used to working with CT data, so some of this is different for me. I have tried to convert the model to a segment and then cut out the regions I am not interested in to obtain a surface area from the Segment Statistics section, but I have two concerns.</p>
<ol>
<li>The model fills in the voided regions (it is a 3/4 scan), and it becomes extremely low quality in comparison.</li>
<li>Because the regions are filled in now, I am unsure if it calculates the entirety of what is left for the surface area.</li>
</ol>
<p>Because I am only interested in that highly specific region is there an easier way you would suggest doing it?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2024-02-03 07:03 UTC)

<p>Segmentation is for representing volumes (represented internally by labelmap images, closed surfaces, etc.). It seems that you want to analyze open surfaces, therefore segmentations are not relevant bánt for you.</p>
<p>Instead, you can colour out surface patches that you are interested in using Dynamic Modeler module and get the surface area in Modules module / Information section.</p>

---

## Post #3 by @Logan_Moore (2024-02-04 03:15 UTC)

<p>This worked exactly as I needed it to. Thank you so much!</p>

---

## Post #4 by @Logan_Moore (2024-02-07 22:55 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> I was hoping to ask you about some weird behavior with the Dynamic Modeler module. I have found a scan of an individual where I don’t get the expected result.</p>
<p>Here it is before cutting<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfb8306e5c8e088f3d851a36c7cb8981fcc3e89d.jpeg" data-download-href="/uploads/short-url/rm1ORtluAr2vXNQSHKcouAzXKDr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfb8306e5c8e088f3d851a36c7cb8981fcc3e89d_2_612x500.jpeg" alt="image" data-base62-sha1="rm1ORtluAr2vXNQSHKcouAzXKDr" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfb8306e5c8e088f3d851a36c7cb8981fcc3e89d_2_612x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfb8306e5c8e088f3d851a36c7cb8981fcc3e89d_2_918x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfb8306e5c8e088f3d851a36c7cb8981fcc3e89d_2_1224x1000.jpeg 2x" data-dominant-color="A29E76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1384×1130 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here it is after cutting<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b15dbaadaa82b99187e68fd5e702ef2ffb10a13e.png" data-download-href="/uploads/short-url/pj3kdQ3IWGERlGkMXeWo1OcmQ9M.png?dl=1" title="ui 158 cranium cut 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15dbaadaa82b99187e68fd5e702ef2ffb10a13e_2_690x427.png" alt="ui 158 cranium cut 3" data-base62-sha1="pj3kdQ3IWGERlGkMXeWo1OcmQ9M" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15dbaadaa82b99187e68fd5e702ef2ffb10a13e_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15dbaadaa82b99187e68fd5e702ef2ffb10a13e_2_1035x640.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15dbaadaa82b99187e68fd5e702ef2ffb10a13e_2_1380x854.png 2x" data-dominant-color="6B6C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ui 158 cranium cut 3</span><span class="informations">2149×1332 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is a general mock-up scheme of how we are placing the CC edges. We are generating a segmentation to only use the planes, it has been turned off in the tree.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5518a3f2886d963d60859812f76115ade7d2e6a.png" data-download-href="/uploads/short-url/pS17uym5u9iP75CuAsRNjQVjwtI.png?dl=1" title="thumbnail_ui 158 cranium cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5518a3f2886d963d60859812f76115ade7d2e6a_2_635x500.png" alt="thumbnail_ui 158 cranium cut" data-base62-sha1="pS17uym5u9iP75CuAsRNjQVjwtI" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5518a3f2886d963d60859812f76115ade7d2e6a_2_635x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5518a3f2886d963d60859812f76115ade7d2e6a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5518a3f2886d963d60859812f76115ade7d2e6a.png 2x" data-dominant-color="B7645C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_ui 158 cranium cut</span><span class="informations">830×653 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know why the Dynamic Modeler would cut so far away from the demarcated area? That is the specified “inside” section being rendered there as well. So I initially thought it was an issue with the model. So I rescanned a smaller section today, but I had a similar issue with generating smaller pieces, albeit at least inside the circle. Just now, I tried to replicate the behavior again on the original and not the new scan, and it worked. This behavior seems strange to me as I was able to cut out about 20 regions so far without issue.</p>
<p>It is worth noting that two versions of the slicer are being used, 5.21 and 5.6.1, but I did have the issue across both versions.</p>
<p>I have included a google drive link here for replication:<a href="https://drive.google.com/drive/folders/1TmX1VHD2gZ4j2iPT9Ni4cKpoz2muXpNr?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">For slicer - Google Drive</a></p>
<p>Thanks ahead for any input you or others may have to offer!</p>

---
