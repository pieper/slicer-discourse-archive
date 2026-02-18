# Problem with loading ct scan

**Topic ID**: 6707
**Date**: 2019-05-06
**URL**: https://discourse.slicer.org/t/problem-with-loading-ct-scan/6707

---

## Post #1 by @JoeCrozier (2019-05-06 19:13 UTC)

<p>Operating system:Windows 10 Pro<br>
Slicer version: 4.11<br>
Expected behavior:  Import dicom images of ct scan<br>
Actual behavior:<br>
I am working on a project with several of the residents here at the hospital I work at, and they have a shared online drive with ct scans of patients that we are working on.  I have downloaded the scans to my computer and tried to load them into slicer to no avail.  They are “normal” head ct files (i.e. normal in that it shouldn’t be a 3d volume or anything, should just be individual 2d dicom images) and when I try to load them, the reader sees this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89092b3efbed7637eef9f65852920375d8f441ea.png" data-download-href="/uploads/short-url/jyh3A9HoNRJA6wakM7WUO4o9tpM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89092b3efbed7637eef9f65852920375d8f441ea.png" alt="image" data-base62-sha1="jyh3A9HoNRJA6wakM7WUO4o9tpM" width="690" height="82" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1497×180 4.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I then try to load either volume in, it errors out.</p>
<p>I also have access to the software AnalyzePro, and I opened the scan in there.  It did open, and seems to look normal, except the hounsfield units are WAYY off of what I would expect, the highest number is like 250.  When I “export” the images from AnalyzePro (to see if that fixes something somehow) and then try to reload them in 3d Slicer, I see this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/592f4bae74c2144fbfaa04b3e835002ae0cdc81c.png" data-download-href="/uploads/short-url/cIXPaq4o51K7AFVWLSpyNLRNEyo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/592f4bae74c2144fbfaa04b3e835002ae0cdc81c_2_690x83.png" alt="image" data-base62-sha1="cIXPaq4o51K7AFVWLSpyNLRNEyo" width="690" height="83" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/592f4bae74c2144fbfaa04b3e835002ae0cdc81c_2_690x83.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/592f4bae74c2144fbfaa04b3e835002ae0cdc81c_2_1035x124.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/592f4bae74c2144fbfaa04b3e835002ae0cdc81c_2_1380x166.png 2x" data-dominant-color="FCFCFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1452×175 2.79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And it does not load.   I’ve anonymized the data and uploaded it here:<br>
<a href="https://drive.google.com/open?id=1Wsew2VvZOngNjnhxlweYOYrOVqyVRyPv" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/open?id=1Wsew2VvZOngNjnhxlweYOYrOVqyVRyPv</a></p>
<p>Would anyone be able to help me figure out why I can’t load it?  I’m assuming it has to do with how the residents got it off of our server, but nobody seems to be able to clue me in to how they did that, and I believe the “original” data is gone on our servers… so it’d be awesome if there was a way to salvage these.</p>

---

## Post #2 by @lassoan (2019-05-08 00:06 UTC)

<p>The data set is not a real 3D CT volume but a series of screenshots of an application screen showing CT slices. I would recommend to change export options in the software that exported the data set and choose a full CT export instead of just screenshots (secondary capture).</p>
<p>If you want to see what’s in the data set then you can follow these steps:</p>
<ul>
<li>in menu, select File / Add data (DICOM module can only load grayscale volumes and the screenshots are RGB volumes)</li>
<li>select one of the files</li>
<li>select Volume in Description column</li>
<li>check “Show options” checkbox, uncheck “Single file” option</li>
<li>click OK</li>
<li>go to Volumes module and in Volume information section, set the correct spacing values (you can verify correct scale by measuring length of the around the image)</li>
<li>use Vector to scalar volume module to convert RGB to grayscale volume</li>
<li>use Crop volume module to crop away annotations around the image region</li>
</ul>
<p>Even after all these steps, the image quality is severely impacted because the image resolution and bit depth are much lower than in a typical CT image.</p>

---

## Post #3 by @JoeCrozier (2019-05-08 11:40 UTC)

<p>Thank you. That stinks to hear the image quality is so impacted as I believe the original images are gone from our hospital server (not totally gone, but they dump half the slices after a certain point of time to save server space.  I know this because I went to go retrieve them directly myself as a work around and saw), so it sounds like a good quality image may not exist anymore.  Oh well.</p>

---
