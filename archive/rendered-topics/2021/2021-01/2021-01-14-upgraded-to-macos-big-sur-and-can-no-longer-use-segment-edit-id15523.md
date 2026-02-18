# Upgraded to macOS Big Sur and can no longer use Segment Editor on saved scenes (mrml)

**Topic ID**: 15523
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/upgraded-to-macos-big-sur-and-can-no-longer-use-segment-editor-on-saved-scenes-mrml/15523

---

## Post #1 by @Wesley_Thornton (2021-01-14 14:12 UTC)

<p>Operating system: macOS Big Sur<br>
Slicer version: 4.13.0-2021<br>
Expected behavior:<br>
Actual behavior: When I upload a saved mrml I either get kicked out of Slicer and an error message pops up, or the scene loads with just colored segments with a black background, but no structures (i.e. I can’t see the lower leg muscles on the MRI just colors). Furthermore, the Segment Editor functions don’t work. I can’t move slice by slice or adjust brightness.</p>
<p>Any suggestions?</p>

---

## Post #2 by @Wesley_Thornton (2021-01-14 14:12 UTC)

<p>Operating system: macOS Mojave<br>
Slicer version: 4.11.20200930<br>
Expected behavior:<br>
Actual behavior: I posted about having trouble with macOS Big Sur. I downloaded this version of Slicer onto a computer running Mojave. When I opened up saved Scenes to Slicer on this mac, it was as if I had done no work on the project and it was being opened for the first time. No colored segments were revealed. It was like no work had been completed. Suggestions?</p>

---

## Post #3 by @lassoan (2021-01-14 14:18 UTC)

<p>Please clarify:</p>
<ul>
<li>What Slicer version did you use to create the scene (let’s call this Slicer version A)?</li>
<li>What Slicer version did you have trouble opening the scene with (let’s call this Slicer version B)?</li>
<li>Can you read/edit the scene created using Slicer version A using Slicer version A?</li>
<li>Can you read/edit the scene created using Slicer version B using Slicer version B?</li>
<li>Do you have problems reading/editing scene created using Slicer version A in Slicer version B? Do you see any errors in the application logs?</li>
<li>Can you reproduce the problem with some segmentation that you quickly create on some sample data set? Could you upload the saved .mrb file to somewhere and post the link here?</li>
</ul>

---

## Post #4 by @Wesley_Thornton (2021-01-14 19:59 UTC)

<p>Slicer A: 4.11.20200930<br>
Slicer B:  4.13.0-2021</p>
<p>I did all of my original work on Slicer A. Then when I upgraded my mac’s OS  (Big Sur) I had trouble opening the saved scene with both versions (getting the “closed unexpectedly” error). As I tried to troubleshoot, I downloaded both Slicer versions to another Mac running Mojave. It was on this mac, despite the version of Slicer, that when I opened a saved scene it came up brand new as if no work had been completed. I don’t get any errors with this set-up, but my work is just not there.</p>
<p>As I just went into Slicer B to show you the issue with not being able to edit with the newest version of Slicer with Big Sur, all of my saved mrml files are now just a black screen despite the different muscles I identified being present when I click on Explore Data.</p>

---

## Post #5 by @hherhold (2021-01-14 20:06 UTC)

<p>Apologies if you already knew this - the mrml file is just a project file that contains pointers to the other data files, such as segmentation data (.seg.nrrd) and so on. Just copying the mrml file is not sufficient to open an entire project.</p>
<p>You can save the entire project out as a Medical Records Bundle or mrb file (I think that’s what it stands for). This is the mrml and all other files zipped up. This is very handy for moving projects around but a bit cumbersome to work with on a daily basis for working on segmentations, etc.</p>
<p>Hope this helps.</p>

---

## Post #6 by @lassoan (2021-01-14 20:42 UTC)

<p>Can you share one of the scenes that you cannot open so that we can investigate? You can save the entire scene content as a .mrb file by clicking the package icon in the Save data window, upload it somewhere (dropbox, onedrive, etc.) and send the link.</p>

---

## Post #7 by @Wesley_Thornton (2021-01-15 12:25 UTC)

<p>Slicer allowed me to save this previous mrml as an mrb, but then the program crashed. Tried to reopen and save multiple mrml files on two different versions of Slicer and got this message every time:</p>
<p>Error Message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc36cac8e5dc1870cb50bfa6bdd76581f9e64d09.jpeg" data-download-href="/uploads/short-url/zZbIhaXTnc7Yf0EE8R1mdfYoIgp.jpeg?dl=1" title="Image 1-12-21 at 5.47 AM.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc36cac8e5dc1870cb50bfa6bdd76581f9e64d09_2_472x295.jpeg" alt="Image 1-12-21 at 5.47 AM.jpg" data-base62-sha1="zZbIhaXTnc7Yf0EE8R1mdfYoIgp" width="472" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc36cac8e5dc1870cb50bfa6bdd76581f9e64d09_2_472x295.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc36cac8e5dc1870cb50bfa6bdd76581f9e64d09_2_708x442.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc36cac8e5dc1870cb50bfa6bdd76581f9e64d09_2_944x590.jpeg 2x" data-dominant-color="D4B1C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 1-12-21 at 5.47 AM.jpg</span><span class="informations">1440×900 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Link to mrb scene: <a href="https://1drv.ms/u/s!AgievV_QxHORdg7RqxIxdI7t4N8" rel="noopener nofollow ugc">https://1drv.ms/u/s!AgievV_QxHORdg7RqxIxdI7t4N8</a></p>
<p>Thank you.</p>

---

## Post #8 by @lassoan (2021-01-16 07:23 UTC)

<p>The scene file that you attached is essentially empty (you can rename the file extension to .zip and have a look inside yourseld). The screenshot embedded into the file shows that it is a re-save of an scene that was not loaded completely. From this file it is hard to tell what went wrong when you opened it or saved it before (you have unchecked saving of data files, the data files were misplaced later, some error occurred during saving, etc.).</p>
<p>Latest Slicer Preview Release does not crash anymore when you attempt to load the file, but it does not make a difference, as the file is empty anyway.</p>
<p>We have improved error reporting during saving in recent Slicer versions, so I would recommend to use at least the latest stable release, but maybe even the latest preview release (as it contains a number of additional improvements in error reporting).</p>

---

## Post #9 by @Wesley_Thornton (2021-01-16 15:30 UTC)

<p>Now I am confused. For months I have been working on over a dozen scenes like the one I sent you. I would routinely save unfinished work as the default mrml and return later to continue work through Segment Editor with no issue. It wasn’t until after I recently got the error message that this became an issue as I went to other mrml files to check work and they either wouldn’t load or the software would crash. Is there a way to retrieve the work I have done if I have saved mrml files?</p>

---

## Post #10 by @lassoan (2021-01-16 15:39 UTC)

<p>Segmentation is not saved in the scene file (.mrml) but in the segmentation (.seg.nrrd) file. The scene file just lists what files make up the scene and how they should be loaded. If you still have the .seg.nrrd files then you can load them directly into Slicer.</p>
<p>If you don’t want to deal with multiple files then you can start using .mrb files, which contain all data in a single file. Since you need to package all data in a single file it takes a bit longer to save, but it is easier to make complete and independent copies of all data that you are working on.</p>

---
