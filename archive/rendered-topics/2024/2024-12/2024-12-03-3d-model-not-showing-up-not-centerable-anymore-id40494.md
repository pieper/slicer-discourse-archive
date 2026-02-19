---
topic_id: 40494
title: "3D Model Not Showing Up Not Centerable Anymore"
date: 2024-12-03
url: https://discourse.slicer.org/t/40494
---

# 3D model not showing up/not centerable anymore

**Topic ID**: 40494
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/3d-model-not-showing-up-not-centerable-anymore/40494

---

## Post #1 by @mitra (2024-12-03 15:04 UTC)

<p>Hey,<br>
I just finished making an awesome 3D model after many hours and then suddenly the 3D image disappeared and now whenever I load up the Project, my 3D section does not work; Initially there is the cube without a 3D model in the center, but once i make one single left click in the 3D area, it is going away. I cant center view it, no lines appear when i try to toggle on 3D cube and 3D axis lable, nothing shows up. Current version is 5.6.2 - please tell me this is fixable and my data is now lost <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>I also already tried to use the “Refocus camera on this point” option in the CT data but it did not solve the problem.</p>
<p>Could it be that my 3D image and center is so far out of my screen, that i cant even see it anymore? Even scrolling madly into one or the other direction didnt solve it for me… Is there a way to complete recenter it? I can also make a video for you if that helps.</p>
<p>Or maybe is there a way to just reopen the dicom images and import my segmentations again? Because if I use them over the same Dicom images i could just create a new project if that makes sense?</p>
<p>When I enter a new project the 3D viewer works normally, but once I open the scene from this project I can not happen to find my 3D model…</p>
<p>Any help is much appreciated! Thank you in advance!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df2c683d504d19812c5f4d4f05c490847b862a9.jpeg" data-download-href="/uploads/short-url/dp6y1p6s3DTmiYxFjTKYt9ExawF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df2c683d504d19812c5f4d4f05c490847b862a9_2_690x363.jpeg" alt="image" data-base62-sha1="dp6y1p6s3DTmiYxFjTKYt9ExawF" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df2c683d504d19812c5f4d4f05c490847b862a9_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df2c683d504d19812c5f4d4f05c490847b862a9_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df2c683d504d19812c5f4d4f05c490847b862a9_2_1380x726.jpeg 2x" data-dominant-color="5E5F71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1011 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-12-03 16:01 UTC)

<p>I have had this bug but only a few times. Restarting Slicer always solved the issue. I couldn’t track it down though. I suggest saving the scene into MRB, restart Slicer, and load the scene.</p>

---

## Post #3 by @mitra (2024-12-03 16:12 UTC)

<p>Thank you for your reply, I already reloaded the scene several times, which did not solve the problem. I now also tried saving it into an .MRB file, and opened the .MRB scene, but it also did not solve the problem. Do you perhaps have any other solution to this problem? Something like creating a new project but reopening the Segmentations in there - if this is even possible?</p>

---

## Post #4 by @cpinter (2024-12-04 15:26 UTC)

<p>Maybe try loading the MRB in the latest preview version. If that does not solve the issue then if you can share the MRB we can take a look.</p>

---

## Post #5 by @mitra (2025-02-05 15:31 UTC)

<p>Thanks for the answer, I have been fiddling around with the file the past weeks and work has been really time consuming so its been a while but I couldn´t come up with a solution yet. If you´d still be up for having a look at it, it would really be much appreciated. Just let me know how we can get in contact?</p>

---

## Post #6 by @cpinter (2025-02-06 15:27 UTC)

<p>I think you could help most with:</p>
<ul>
<li>Downloading the 5.8 stable</li>
<li>Creating a scene using sample data that produces this issue when loading</li>
</ul>
<p>If you have a scene that you cannot publically share, you can send me a cloud drive link in private message, but I’m even busier nowadays than normal so not sure when I can take a look. If you manage to reproduce this in a way that can be shared, then anyone in the community will have the possibility to use it for fixing.<br>
It is also possible that 5.8 does not produce the issue any more…</p>

---

## Post #7 by @lassoan (2025-02-07 12:01 UTC)

<p>You can narrow down the issue by saving the scene in .mrml format - and all the nodes as additional data files. After this, restart Slicer and instead of loading the scene (.mrml file), load each data file one by one. If you see that after loading a specific file the application starts to misbehave then you known that something is wrong with that file and we can investigate it further, focusing on that single file.</p>

---
