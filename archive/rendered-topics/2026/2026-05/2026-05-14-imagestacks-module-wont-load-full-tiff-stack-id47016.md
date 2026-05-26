---
topic_id: 47016
title: "ImageStacks module won't load full tiff stack"
date: 2026-05-14
url: https://discourse.slicer.org/t/47016
last_bumped: 2026-05-14T16:39:03.268Z
---

# ImageStacks module won't load full tiff stack

**Topic ID**: 47016
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/imagestacks-module-wont-load-full-tiff-stack/47016

---

## Post #1 by @Jknaub (2026-05-14 01:05 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.8.1<br>
Expected behavior: importing a tiff stack with the slicermorph ImageStacks (3,867 images)<br>
Actual behavior: only selects a subset of the stack</p>
<p>Hello,</p>
<p>I’m trying to import a tiff stack that I downloaded from morphosource - <a href="https://www.morphosource.org/concern/media/000531361?locale=en" class="inline-onebox" rel="noopener nofollow ugc">Making sure you're not a bot!</a></p>
<p>It’s a CT scan of a shark and when I load it into slicer, it’s missing the head.  I have imported the stack into FIJI to verify the head is indeed captured in the image stack.</p>
<p>I unzipped the morphosource download and when I try to import it into 3DSlicer via ImageStacks, it only loads some of the stack–In the 2D views I can see everything except the head of the shark, it seems cut off.  I’ve made sure to enter the spacing information from the morphosource page so I’m unsure what I"m doing wrong. In the ImageStacks module I tried selecting all the files manually rather than the “Browse” and selecting one file, and when I added them all manually the scan alignment became jagged.</p>
<p>I’m including screenshots of the stack in FIJI where the shark’s head is visible, and a screenshot of how it looks in slicer when I use the “browse” feature, and “select files”.</p>
<p>Any guidace would be super appreciated, I’m sure I’m missing something just not sure what. Thanks in advance!</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/061cd94acbd7fbc20693dbe91d047dcbc08bea1e.jpeg" data-download-href="/uploads/short-url/S4FJlkE8ElnUESnJ4N18FpbyNw.jpeg?dl=1" title="Ctaurus stack in FIJI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/061cd94acbd7fbc20693dbe91d047dcbc08bea1e_2_690x172.jpeg" alt="Ctaurus stack in FIJI" data-base62-sha1="S4FJlkE8ElnUESnJ4N18FpbyNw" width="690" height="172" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/061cd94acbd7fbc20693dbe91d047dcbc08bea1e_2_690x172.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/061cd94acbd7fbc20693dbe91d047dcbc08bea1e_2_1035x258.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/061cd94acbd7fbc20693dbe91d047dcbc08bea1e.jpeg 2x" data-dominant-color="514F51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ctaurus stack in FIJI</span><span class="informations">1295×323 94.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9736ee0f438cb22b4537a65c41bf5fc19b712654.jpeg" data-download-href="/uploads/short-url/lzHMEXC9pTXx0uviWFDEaEwDYl6.jpeg?dl=1" title="Ctaurus stack in Slicer using imagestacks browse" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9736ee0f438cb22b4537a65c41bf5fc19b712654_2_673x500.jpeg" alt="Ctaurus stack in Slicer using imagestacks browse" data-base62-sha1="lzHMEXC9pTXx0uviWFDEaEwDYl6" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9736ee0f438cb22b4537a65c41bf5fc19b712654_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9736ee0f438cb22b4537a65c41bf5fc19b712654_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9736ee0f438cb22b4537a65c41bf5fc19b712654.jpeg 2x" data-dominant-color="3C3B45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ctaurus stack in Slicer using imagestacks browse</span><span class="informations">1178×874 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06b952812489405442a35be4b44e70d5390fd510.jpeg" data-download-href="/uploads/short-url/XtUN2oboQWl3AgtYtneuHL8goM.jpeg?dl=1" title="Ctaurus stack in Slicer using imagestacks select all files" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06b952812489405442a35be4b44e70d5390fd510_2_680x499.jpeg" alt="Ctaurus stack in Slicer using imagestacks select all files" data-base62-sha1="XtUN2oboQWl3AgtYtneuHL8goM" width="680" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06b952812489405442a35be4b44e70d5390fd510_2_680x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06b952812489405442a35be4b44e70d5390fd510_2_1020x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06b952812489405442a35be4b44e70d5390fd510.jpeg 2x" data-dominant-color="121412"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ctaurus stack in Slicer using imagestacks select all files</span><span class="informations">1188×873 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>

---

## Post #2 by @muratmaga (2026-05-14 01:16 UTC)

<p>Please try with the latest stable, v5.10.0 (your Slicer is couple years old). It worked perfectly fine for me:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e6d3a6e06255fae12a79e7400568a4322c8ee62.jpeg" data-download-href="/uploads/short-url/bbNgjrwMl0TG6Tsn7PK1DSwyZRE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e6d3a6e06255fae12a79e7400568a4322c8ee62_2_687x500.jpeg" alt="image" data-base62-sha1="bbNgjrwMl0TG6Tsn7PK1DSwyZRE" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e6d3a6e06255fae12a79e7400568a4322c8ee62_2_687x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e6d3a6e06255fae12a79e7400568a4322c8ee62_2_1030x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e6d3a6e06255fae12a79e7400568a4322c8ee62_2_1374x1000.jpeg 2x" data-dominant-color="858384"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1662×1208 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Jknaub (2026-05-14 02:00 UTC)

<p>Hi Murat,</p>
<p>Thanks for your prompt reply. I downloaded slicer5.10 and am still having the same issue. I tried again by using the “browse” option of the ImageStacks module and it still won’t load the head. If I manually select all the files it still gets the jagged appearance (screenshots attached).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbe65c90ca5c4f1fdb9d98cc401df757683a60e0.jpeg" data-download-href="/uploads/short-url/qOePJp1aOvfTArBCE9E4ODRlGAU.jpeg?dl=1" title="slicer5.10_screengrab_manualselectfiles" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbe65c90ca5c4f1fdb9d98cc401df757683a60e0_2_690x361.jpeg" alt="slicer5.10_screengrab_manualselectfiles" data-base62-sha1="qOePJp1aOvfTArBCE9E4ODRlGAU" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbe65c90ca5c4f1fdb9d98cc401df757683a60e0_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbe65c90ca5c4f1fdb9d98cc401df757683a60e0_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbe65c90ca5c4f1fdb9d98cc401df757683a60e0_2_1380x722.jpeg 2x" data-dominant-color="3E3C3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer5.10_screengrab_manualselectfiles</span><span class="informations">1919×1004 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d1f3de9d3b26e11fc9a3995c724fd04729316cc.jpeg" data-download-href="/uploads/short-url/fzkYJHKNTUD1ZNc91zjCx4nSqAI.jpeg?dl=1" title="slicer5.10_screengrab" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d1f3de9d3b26e11fc9a3995c724fd04729316cc_2_690x360.jpeg" alt="slicer5.10_screengrab" data-base62-sha1="fzkYJHKNTUD1ZNc91zjCx4nSqAI" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d1f3de9d3b26e11fc9a3995c724fd04729316cc_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d1f3de9d3b26e11fc9a3995c724fd04729316cc_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d1f3de9d3b26e11fc9a3995c724fd04729316cc_2_1380x720.jpeg 2x" data-dominant-color="3C3A3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer5.10_screengrab</span><span class="informations">1916×1002 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2026-05-14 02:24 UTC)

<p>The one the top is right, there are 3867 slices in this sequence. The one in the bottom is incorrect, because it leaving out about 1000 slices for some reason.</p>
<p>If you select the files yourself, ImageStacks uses the sorting provided by the file system, which can be wrong (e.g., sorted by dates, filesize instead of the correct sequence) etc… I suggest clearing your scene (CTRL+W) and then dragging the very first file (Ctau_Highres_FullBody0000.tif) into the slicer, and then let slicer sort the files.</p>
<p>It should look something like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4904d4fca7de0c2f97af17f6bb4af2427d984c61.png" alt="image" data-base62-sha1="apXcSPzF7tugaSd9znMAM435zyh" width="690" height="74" data-dominant-color="EDEDED"></p>
<p>%04d means the sequences in filenames are expected to have four (4) numerical digits, which is the correct format for this.</p>

---

## Post #5 by @Jknaub (2026-05-14 14:15 UTC)

<p>Hi Murat,</p>
<p>Thanks for the suggestion. Weird that the drag and drop of one file allowed all files to be imported correctly but the browse feature doesn’t. Regardless, that solved my issue. Thanks so much!</p>

---

## Post #6 by @muratmaga (2026-05-14 16:39 UTC)

<p>Browse relies on sorting provided by your operating system, which may not be by default set to filenames (it can be dates, file size, file type etc). If you click on sort by file name before in the file browser selector, it should work.</p>
<p>Nevertheless, I add an issue to force sorting for browsing.</p>

---
