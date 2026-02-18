# Export DICOM in Colors

**Topic ID**: 19301
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/export-dicom-in-colors/19301

---

## Post #1 by @zlwei (2021-08-23 00:36 UTC)

<p>Dear all,<br>
I imported a set of DICOM files to Slicer. These DICOMs are for 3D echo doppler so they are colorful. Then, I export them in “Data” → “Export to DICOM” in the right-click menu. The exported files are grayscale. I tried to change the rendering in “Volume”, but can not fix the problem. Any insights?</p>
<p>thanks,<br>
Alan</p>

---

## Post #2 by @lassoan (2021-08-23 14:35 UTC)

<p>There is no widely used standard for 3D ultrasound (usually the 3D voxel data is stored as private fields in DICOM) and Doppler is even more hopeless.</p>
<p>What is the complete workflow that you are trying to implement? Where does the Doppler data comes from, what would you like to do with it in Slicer, and what software you want to process the exported data with?</p>
<p>Is your 3D echo Doppler data set is 2D+time (you have a time sequence of a colored slice) or 3D+time (you have a 3D array of voxels, each voxel having a 3D vector value)?</p>

---

## Post #3 by @zlwei (2021-08-23 18:42 UTC)

<p>Thanks for your reply.</p>
<p>I do not need to process the image. The only steps I need to do are:</p>
<ol>
<li>Click “Add Data” à “Choose Directory to Add” and select a directory that contains a set of DICOM files to Slicer. This set of DICOM files, similar to MRI images, represent slices of anatomy at one time point.</li>
<li>Modules → “Data” → “Export to DICOM” in the right-click menu.</li>
</ol>
<p>The problem is that the exported files are grayscale, while I wish they were colorful (the original data was in color).</p>
<p>Thanks,</p>
<p>Alan</p>

---

## Post #4 by @lassoan (2021-08-23 18:48 UTC)

<aside class="quote no-group" data-username="zlwei" data-post="3" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zlwei/48/8898_2.png" class="avatar"> zlwei:</div>
<blockquote>
<p>Click “Add Data” à “Choose Directory to Add” and select a directory that contains a set of DICOM files to Slicer. This set of DICOM files, similar to MRI images, represent slices of anatomy at one time point.</p>
</blockquote>
</aside>
<p>Do you get a Cartesian color Doppler 3D volume from DICOM? Do each voxel contain a speed vector, or just an RGB image that contains the B-mode image fused with some color overlay?</p>
<p>What software generates these volumes?</p>
<p>How do you visualize these images in Slicer? Can you attach a screenshot?</p>
<aside class="quote no-group" data-username="zlwei" data-post="3" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zlwei/48/8898_2.png" class="avatar"> zlwei:</div>
<blockquote>
<p>The problem is that the exported files are grayscale, while I wish they were colorful (the original data was in color).</p>
</blockquote>
</aside>
<p>We haven’t implemented color image DICOM export (these color images are usually just screenshots that do not have much use other than visualization), but if your input images are already color DICOM images and you don’t process them in Slicer, then you may not need to re-export them.</p>

---

## Post #5 by @zlwei (2021-08-29 19:22 UTC)

<blockquote>
<p>Blockquote<br>
We haven’t implemented color image DICOM export (these color images are usually just screenshots that do not have much use other than visualization), but if your input images are already color DICOM images and you don’t process them in Slicer, then you may not need to re-export them.</p>
</blockquote>
<p>I do not process my DICOM set in Slicer but need to process them in another software. However, somehow, that software does not recognize my DICOM set as one sequence, meaning if I load them, the software only read them seperately not one sequence of images as a whole. I need to do this “Import” and " Export" in Slicer then the software will recognize the exported DICOMs as a sequence. Unfortunately, the “Export” DICOM is grayscale. Any workaround you can think of to get the DICOM back to colored ones?</p>
<p>Thanks,<br>
Alan</p>

---

## Post #6 by @lassoan (2021-08-29 19:30 UTC)

<p>You can edit patient ID (maybe also name, birth date, etc) and study instance UID fields in the exported DICOM data set using <code>dcmodify.exe</code> (command-line tool in <a href="https://dcmtk.org/">DCMTK</a>) or pydicom.</p>
<p>However, this will not change the fact that most software will not allow you to use color images for any kind of analysis or quantification. This is why color image is not useful in general and export was not implemented in Slicer (we need to prioritize to work on features that are clinically useful).</p>
<p>Probably what you need is to export segmentation as DICOM Segmentation Object or DICOM RT structure set. Treatment planning or surgical planning software can then display those as color overlays on the images and also use for planning and analysis.</p>

---

## Post #7 by @zlwei (2021-08-29 19:41 UTC)

<p>Sounds great. Thanks for your prompt response!</p>
<p>Alan</p>

---

## Post #8 by @volkodavmyx (2023-08-16 06:15 UTC)

<p>Sorry for bringing up the old topic, but in our projects, the need to save color DICOM series is becoming more common.<br>
Basically, not for clinical use, but for training of various types of AI, as well as one of the projects is trying to implement 3D visualization using Anaglyph technology.<br>
Right now we are doing a lifehack by saving to NIFTI and converting back to DICOM, however, this is long and leads to the loss of some tags.</p>
<p>It would be great if you turn on colored DICOM on your next update.</p>

---

## Post #9 by @lassoan (2023-08-16 10:09 UTC)

<aside class="quote no-group" data-username="volkodavmyx" data-post="8" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/volkodavmyx/48/15588_2.png" class="avatar"> volkodavmyx:</div>
<blockquote>
<p>for training of various types of AI</p>
</blockquote>
</aside>
<p>Can you explain how saving color images would help training AI?</p>
<p>Anaglyph technology was not adopted in the medical imaging community for many decades and it did not get anywhere. 3D Slicer has been supporting it from very early days, yet there is no sign that anybody would even want to use it (except maybe 1-2 isolated cases a year). With the inexpensive and wide availability of virtual reality headsets, it is really hard to imagine any real-world use case for anaglyph visualization.</p>
<p>Saving color DICOM should be quite easy to implement and if you implement it then we would accept the pull request and merge it, but if there is no strong supporting use case or funding dedicated for developing this feature then we cannot spend time with this, as it would take time away from implementing more impactful improvements.</p>
<p>I move this topic to the “Feature request” category so that users can vote on it. If it gets many votes then it will move up on our priority list.</p>

---

## Post #10 by @Lukas (2024-02-05 09:41 UTC)

<p>Dear all,</p>
<p>sorry for piggybacking this topic but since it was changed to a feature request I hope that it is okay this time <img src="https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=12" title=":man_shrugging:" class="emoji" alt=":man_shrugging:" loading="lazy" width="20" height="20"></p>
<p>I would also like to export color images as dicom since I’m working with 4D flow MRI data (both Philips and Siemens) that I process using GTFlow (V 3.2). For in house demonstration I need to show these data during rounds. Currently we show exported .avi files from the file system. But preferably I would like to be able to upload the 4D movie into our PACS system.</p>
<p>This is what I’ve got so far:<br>
1.) Process 4D data using GTFlow and export movie as .tiff series<br>
2.) Using fiji convert .tiff to .jpeg (since exporting .tiff to .dcm did not work in slicer)<br>
3.) Open folder containing .jpeg files using slicer → works perfectly fine with color images shown in slicer<br>
4.) save as dicom and filling out some header information → works perfectly fine, but makes gray scale images<br>
5.) use rename .dcm ‘’ *.dcm to remove filename ending (otherwise the filenames would be too long for dcmtools<br>
6.) use dcmmkdir to create dicomdir (needed for PACS import)<br>
7.) use in house program intended for external patient data import from cd</p>
<p>Works all fine and i can view the grayscale images from our PACS. But unfortunately the color coding is missing which makes 4D flow images way less satisfying and unseful to watch <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thank you in advance!</p>

---

## Post #11 by @lassoan (2024-02-05 11:25 UTC)

<p>Thanks for describing your workflow - it sounds awfully complicated, considering that this should all be a one-click operation.</p>
<p>Conversion to grayscale could be avoided with small changes if we exported the image stack as slices of a 3D volume. Unfortunately, this is not the right thing to do (and image viewers may refuse to load such images) as the images are actually correspond to a time sequence.</p>
<p>So, ideally we would need to load the image stack as a time sequence and then export it to DICOM as a time sequence. We can already load a few compressed video formats from mkv containers, but if GTFlow cannot export into a compatible format then we need to go through jpeg/Tiff stack. We could add a time series option to ImageStacks module (in SlicerMorph extension).</p>
<p>The, to export as time series, we could add a Python scripted exporter in the image sequence DICOM plugin.</p>
<p>Would you have time to do some Python scripting, or funding, to move this forward?</p>
<p>FYI, as part of SlicerHeart, we have developed Slicer modules for importing 4D flow MRI, visualizing it, making measurements, and exporting as 5D array for further analysis. We’ll make these modules public once papers describing them get published. If GTGlow license is not easily available then you’ll be able to use Slicer to manage and share these flow images. We’ll probably also work on flow simulation using these images as inputs. If you are interested in these topics then let us know, maybe we can share some of the development work.</p>

---

## Post #12 by @Lukas (2024-02-06 16:30 UTC)

<p>Thanks for your quick and insightful response. It is very much appreciated.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Thanks for describing your workflow - it sounds awfully complicated, considering that this should all be a one-click operation.</p>
</blockquote>
</aside>
<p>It is <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> but in the mean time I’ve managed to shorten it a bit and get color dicom from jpeg using dcmtk’s img2dcm tool. Still “a bit” messy but for now it works.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you have time to do some Python scripting, or funding, to move this forward?</p>
</blockquote>
</aside>
<p>I’d love to. But unfortunately at the moment I’m very much at the limit of what I can do besides clinical work. In addition (so far) I only do basic python scripting for data analyses and easy image processing but have no experience in working on large projects.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>FYI, as part of SlicerHeart, we have developed Slicer modules for importing 4D flow MRI, visualizing it, making measurements, and exporting as 5D array for further analysis. We’ll make these modules public once papers describing them get published. If GTGlow license is not easily available then you’ll be able to use Slicer to manage and share these flow images. We’ll probably also work on flow simulation using these images as inputs.</p>
</blockquote>
</aside>
<p>That sounds very promising. I’m definitely looking forward to this!</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="19301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you are interested in these topics then let us know, maybe we can share some of the development work.</p>
</blockquote>
</aside>
<p>I’ll have to coordinate with my Prof first but will let you know as soon as I hear back from him. Flow simulation is very much of interest to us and our approach currently is quite manual…</p>
<p>Again, thank you so much!</p>

---
