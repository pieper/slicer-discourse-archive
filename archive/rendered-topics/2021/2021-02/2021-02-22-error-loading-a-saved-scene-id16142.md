---
topic_id: 16142
title: "Error Loading A Saved Scene"
date: 2021-02-22
url: https://discourse.slicer.org/t/16142
---

# Error loading a saved scene

**Topic ID**: 16142
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/error-loading-a-saved-scene/16142

---

## Post #1 by @Hapietsch (2021-02-22 22:03 UTC)

<p>Hi Slicer gurus!<br>
I’m having trouble loading some saved data. I “saved the scene” I was working on yesterday that included reformatted slice planes, some fiducials, as well as some linear and closed loop measurements from a CT scan DICOM.</p>
<p>Slicer version 4.13.0-2021-02-19<br>
I’m using this instead of the stable version because I need area of the closed loop measurements.</p>
<p>What I did:<br>
I tried the Load Data button and selected the directory where I saved the scene.<br>
Response:<br>
Instead of the “Four Up” standard view, it shows all of the data three times and indifferent orientations (see image). It then gives an error window that says “Error while loading the selected files. Click ‘Show details’ button and check the application log for more information.”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/052f642fc8aae3bb5b2857472eab827c38b168f0.jpeg" data-download-href="/uploads/short-url/JRVdtq57xJ1xmaDXnQvRi6FnwY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/052f642fc8aae3bb5b2857472eab827c38b168f0_2_690x377.jpeg" alt="image" data-base62-sha1="JRVdtq57xJ1xmaDXnQvRi6FnwY" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/052f642fc8aae3bb5b2857472eab827c38b168f0_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/052f642fc8aae3bb5b2857472eab827c38b168f0_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/052f642fc8aae3bb5b2857472eab827c38b168f0_2_1380x754.jpeg 2x" data-dominant-color="83808C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2101 909 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The error log shows a VTK error “vtkMRMLStorageNode::ReadData: Failed to read node L2.mrk.json (vtkMRMLScalarVolumeNode1) from filename”. And another VTK error “Failed to determine texture parameters. IF=0 F=6407 T=5121”</p>
<p>Questions:</p>
<ol>
<li>Is there a tutorial on saving/reloading scenes properly? I could not find one in the website tutorials.</li>
<li>Is there a way to get back to what I’ve saved? Or do I need to start over?</li>
<li>How do I avoid doing the same thing again?</li>
<li>Why does it show the data multiple times and rotated?</li>
</ol>
<p>Appreciate any advice as I’m fairly new to this software. I did not see another topic with the same error.  Hopefully someone has seen it before.</p>
<p>Thanks very much,<br>
Hollie</p>

---

## Post #2 by @lassoan (2021-02-22 22:10 UTC)

<p>Could you check the error log (menu: Help / Report a bug) to see if there were any more details about why L2.mrk.json failed to load?</p>
<p>The images that you see on the screen is screenshot that you took (or that was taken automatically when you saved the scene). Single-slice images are loaded in all views in the specific Slicer version you use, but in tomorrow’s version it’ll be only displayed in one view, so it will not be this confusing.</p>
<p>To load the data that you saved, only load the .mrml file into Slicer, not all the files in the folder. If you find working with multiple files confusing then click the “package” icon in the Save data window to save everything into a single .mrb file.</p>

---

## Post #3 by @Sunderlandkyl (2021-02-22 22:17 UTC)

<p>I think the markup loading issue was fixed by this PR: <a href="https://github.com/Slicer/Slicer/pull/5479" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix default storage node creation in LoadMarkupsFromJson by Sunderlandkyl · Pull Request #5479 · Slicer/Slicer · GitHub</a>.<br>
It should be fixed in tomorrow’s preview release.</p>

---

## Post #4 by @Hapietsch (2021-02-22 22:32 UTC)

<p>Thank you both for the quick replies!</p>

---

## Post #5 by @Hapietsch (2021-02-22 22:43 UTC)

<p>When I open the files individually, it does get rid of the weird multiple images. I don’t seem to have access to the measurements, however, only the fiducials marks/labels. Are the linear and loop measured markers not saved in the annotations file? Are they transient or can they be saved if I follow a different process for saving them than just saving the scene?<br>
Thank you.</p>

---

## Post #6 by @lassoan (2021-02-22 22:59 UTC)

<aside class="quote no-group" data-username="Hapietsch" data-post="5" data-topic="16142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> Hapietsch:</div>
<blockquote>
<p>Are the linear and loop measured markers not saved in the annotations file?</p>
</blockquote>
</aside>
<p>Measurements are saved in the measurement (.mrk.json) files. You can open them in any text editor. If you need to do dozens of measurements then you may write a short Python script that saves everything into a single csv file (we can help with this, if you are not sure where to start).</p>

---

## Post #7 by @pieper (2021-02-22 23:30 UTC)

<p>Also it appears you added back all the files, including the screen captures that are saved automatically with the scene.  You only need to reload the .mrml file, and it will pull back all the files that you had loaded.  Or when you save you can click the ‘package’ button on the save dialog and save everything in a .mrb file (which is just a zip with all the data from your scene) that you can share or reload.</p>

---

## Post #8 by @Hapietsch (2021-03-14 10:48 UTC)

<p>Mr. Lasso,<br>
I am finding myself taking approximately 40 dimensions per DICOM image set. Now that I have done a few, I think it would be much easier to have a single output file with all of the dimensions in the same order for each DICOM set to ensure I don’t have a bunch of typos in my data. I do not have any experience in coding in Python. Is your suggested script fairly easy to implement? I appreciate any further advice you have. I am taking linear dimensions (length in mm) and closed loop dimensions (length mm &amp; area mm^2).<br>
Thank you.</p>

---

## Post #9 by @lassoan (2021-03-27 19:25 UTC)

<p>A similar feature is available now - see <a href="https://discourse.slicer.org/t/markups-creating-a-single-file-including-landmarks-fixed-and-curves-semilandmarks-problem-while-resampling/16158/8" class="inline-onebox">Markups - Creating a SINGLE file including Landmarks (fixed) and Curves (semilandmarks) - problem while resampling - #8 by muratmaga</a>. You can ask the SlicerMorph team for assistance with your quantification workflow.</p>

---
