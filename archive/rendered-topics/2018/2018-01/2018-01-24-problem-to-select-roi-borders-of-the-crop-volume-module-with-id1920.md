---
topic_id: 1920
title: "Problem To Select Roi Borders Of The Crop Volume Module With"
date: 2018-01-24
url: https://discourse.slicer.org/t/1920
---

# Problem to select ROI borders of the Crop VOlume module with the mouse

**Topic ID**: 1920
**Date**: 2018-01-24
**URL**: https://discourse.slicer.org/t/problem-to-select-roi-borders-of-the-crop-volume-module-with-the-mouse/1920

---

## Post #1 by @terajnol (2018-01-24 11:28 UTC)

<p>Operating system: Win 10, 64 bits<br>
Slicer version: 4.9.0 2018-01-23</p>
<p>Hi all,</p>
<p>I had no problem before to use the Crop volume Module and its ROI.<br>
But since this morning, after creating a ROI, it is almost impossible to select with the mouse the colored points to expand ROI borders. From the 3D view, I have no problem. But from slice views, even if the ROI and the points to select are visible, I can barely click on the points to move them. Sometimes, especially in the Red Slice View, I can select and move a point but it is random.</p>
<p>I think I may have changed an option on the Slice views from my python script but I cant figure out what or when. The problem appears when I use the Crop Volume in my python script and when I use the initial Crop Volume module in Slicer.</p>
<p>If some of you has any idea …<br>
Thanks,</p>

---

## Post #2 by @lassoan (2018-01-24 13:52 UTC)

<p>Are the handle circles just too small to hit them with your mouse?<br>
Does it look different with the latest stable version (4.8.1)?<br>
What does your Python script do? Is the appearance or behavior of the ROI widget different if you don’t run your script? Can you take a screenshot?</p>

---

## Post #3 by @terajnol (2018-01-24 14:22 UTC)

<p>The size of the handles circles could be the problem but I don’t think so. They are around the same size in the 3D view and I have no problem to click and drag them. Also, the size hasn’t change and I was perfectly able to select them before.</p>
<p>Slicer version does not seem to be the issue. I first discovered the problem in a 2-months old nightly version. I uninstalled it and try with latest nightly version and latest stable build version (4.8.1) and the problem is still the same.</p>
<p>Here is a screenshot but everything seems normal to me.</p>
<p>In my script, I am calling the crop volume module with vtkMRMLCropVolumeParametersNode.<br>
But when the ROI got wrong, I had not touched this part of the script for weeks, I was working with fiducials…<br>
Moreover, if I remove my module from Slicer, or just after the installation of a new version, the problem to select the ORI is still here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb50db821153b29298d24b26706538caaac65f4f.png" data-download-href="/uploads/short-url/t0Ca5MSP38iEt8WR1Te9EuiPzen.png?dl=1" title="crop" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb50db821153b29298d24b26706538caaac65f4f_2_690x371.png" alt="crop" data-base62-sha1="t0Ca5MSP38iEt8WR1Te9EuiPzen" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb50db821153b29298d24b26706538caaac65f4f_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb50db821153b29298d24b26706538caaac65f4f_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb50db821153b29298d24b26706538caaac65f4f_2_1380x742.png 2x" data-dominant-color="A6A6AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crop</span><span class="informations">1921×1033 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your fast answer and your time,</p>

---

## Post #4 by @lassoan (2018-01-24 15:02 UTC)

<p>Have you switched to a different computer? Changed the image resolution?<br>
You can try to reset your application settings by temporarily removing Slicer.ini file (see more information <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues">here</a>) and see if it helps.</p>

---

## Post #5 by @terajnol (2018-01-24 15:56 UTC)

<p>I changed the resolutions of the screen and tried another screen with different resolution but problem is still here.<br>
And unfortunately, temporarily removing Slicer Settings didn’t hep either.</p>
<p>What is weird, and links my problem with a potential resolution problem, is that if I click a lot on the point of the ROI, I ends to select it. But it can be after 5 or 100 clicks… But again, I am still working on the same computer and with the same resolution as yesterday…</p>
<p>I will be able to switch to a different computer once at home and I will: download the latest stable version of Slicer, try if Crop Volume is working correctly, install my module and check again the Crop Volume.</p>
<p>If, as expected, everything is working well on the second computer, how can I totally supress all setting files when I uninstall Slicer ? I tried to uninstall Slicer 4.8.1 and to delete the NA-MIC folder in User\AppData\Roaming without any success after the re-installation of Slicer but maybe I forgot some config files ?</p>

---

## Post #6 by @torquil (2018-06-15 21:22 UTC)

<p>I have the same problem, using Windows 10 and a brand new installation of Slicer 4.8.1. Did you by chance solve the problem?</p>

---

## Post #7 by @lassoan (2018-06-15 21:38 UTC)

<p>It is fixed in recent nightly versions.</p>

---
