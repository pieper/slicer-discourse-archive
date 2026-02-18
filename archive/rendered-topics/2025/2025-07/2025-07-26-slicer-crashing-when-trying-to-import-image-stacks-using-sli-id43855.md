# Slicer crashing when trying to import image stacks using SlicerMorph

**Topic ID**: 43855
**Date**: 2025-07-26
**URL**: https://discourse.slicer.org/t/slicer-crashing-when-trying-to-import-image-stacks-using-slicermorph/43855

---

## Post #1 by @Russell_Engelman (2025-07-26 23:34 UTC)

<p><strong>Computer</strong> - Dell Precision 7710<br>
<strong>Software OS</strong> - Windows 10 Pro<br>
<strong>Total RAM</strong> - 64 gB<br>
<strong>CPU</strong> - Intel(R) Xeon(R) CPU E3-1505M v5 @ 2.80 gHz<br>
<strong>GPU</strong> - NVIDIA Quadro M3000M<br>
<strong>Slicer Version</strong> - Slicer 5.8.1</p>
<p>My version of Slicer is crashing whenever I try to open an image stack in it using the ImageStack function in SlicerMorph. What is really strange is that this is the same computer that was able to successfully open stacks using SlicerMorph <a href="https://discourse.slicer.org/t/segmentation-in-slicer-extremely-slow-when-using-the-scissors-tool-in-slice-view/41930/14">here</a>.</p>
<p>What happens is I will boot up 3D Slicer, open the ImageStack function, and when I go to browse for my files the window immediately hangs and the program crashes (will be updated with video when I get the chance). I tried with an earlier version of Slicer (Slicer 4.8) and the same error occurs. I checked to see if my versions of Slicer and SlicerMorph needed updating and even after this the program crashes in the same way. I am not sure what is going on, as my version of Slicer has not changed at all since the previous Support request where I showed SlicerMorph working properly.</p>

---

## Post #2 by @muratmaga (2025-07-27 00:07 UTC)

<p>Without the data or the log file from the crashed session, it is hard to tell what’s going on.</p>
<p>Did you try to use the “preview” quality to see if it is memory related?</p>

---

## Post #3 by @Russell_Engelman (2025-07-27 02:30 UTC)

<blockquote>
<p>Without the data or the log file from the crashed session, it is hard to tell what’s going on.</p>
<p>Did you try to use the “preview” quality to see if it is memory related?</p>
</blockquote>
<p>I couldn’t even get that far. The moment I tried to even open the file browser to select the files the program crashed (see video). I almost wonder if it has to do with some interaction with Windows in general because I haven’t changed anything on Slicer since the previous forum thread where it worked fine.</p>

---

## Post #4 by @Russell_Engelman (2025-07-27 02:30 UTC)

<p>For some reason I am unable to edit my post. Here is a link to a video documenting the issue.</p>
          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://www.dropbox.com/scl/fi/eameomw90rz4bggbvthj6/3D-Slicer-5.8.1-2025-07-26-19-19-06.mp4?rlkey=eao4nskk209gftc85j0qw6d6p&amp;dl=0">
              <a href="https://www.dropbox.com/scl/fi/eameomw90rz4bggbvthj6/3D-Slicer-5.8.1-2025-07-26-19-19-06.mp4?rlkey=eao4nskk209gftc85j0qw6d6p&amp;dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/scl/fi/eameomw90rz4bggbvthj6/3D-Slicer-5.8.1-2025-07-26-19-19-06.mp4?rlkey=eao4nskk209gftc85j0qw6d6p&amp;dl=0</a>
            </video>
          </div>


---

## Post #5 by @Russell_Engelman (2025-07-27 02:42 UTC)

<p>Unfortunately I just realized the screen recorder does not record pop ups for Windows 10.</p>
<p>More testing has found this issue is not just occurring with SlicerMorph. It also occurs if I try the basic open data option as well as the import DICOM option. Anything that involves the File Explorer seems to trigger it.</p>
<p>Is there any way to record and send the error log?</p>

---

## Post #6 by @muratmaga (2025-07-27 02:43 UTC)

<p>Your video does not play on my end. Upload to the cloud and share the link.</p>
<p>Also is the folder you are loading data from being synced to cloud (like onedrive or icloud)…</p>

---

## Post #7 by @Russell_Engelman (2025-07-27 02:49 UTC)

<blockquote>
<p>Your video does not play on my end. Upload to the cloud and share the link.</p>
</blockquote>
<p>I did. I copy-pasted the link and it loaded into the forum as a video. For some reason it won’t run on the machine I am on now as well even though it ran on the machine I uploaded it from. I will see if there is something I can do to fix it.</p>
<blockquote>
<p>Also is the folder you are loading data from being synced to cloud (like onedrive or icloud)</p>
</blockquote>
<p>No. It doesn’t matter what folder I select the program crashes. Even if I select an internal folder like Documents or Pictures.</p>

---

## Post #8 by @Russell_Engelman (2025-07-27 03:00 UTC)

<p>I tried running sfc /scannow as an administrator in case corrupted drivers were responsible as well as reinstalling Slicer. No success.</p>

---

## Post #9 by @muratmaga (2025-07-27 03:45 UTC)

<p>Did you look into the log file contents from those crashes? It may have some pointers.</p>

---

## Post #10 by @Russell_Engelman (2025-07-27 03:46 UTC)

<p>Here are screenshots showing this in case the video does not properly load.</p>
<p>Screen just before error occurs. Note this is very early in workflow.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbe3a6f4a55730d59c21256aa789af74f6b7c239.jpeg" data-download-href="/uploads/short-url/t5GFtJRSbZMH28C0YbvsaYrzKwF.jpeg?dl=1" title="Error 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3a6f4a55730d59c21256aa789af74f6b7c239_2_690x388.jpeg" alt="Error 1" data-base62-sha1="t5GFtJRSbZMH28C0YbvsaYrzKwF" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3a6f4a55730d59c21256aa789af74f6b7c239_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3a6f4a55730d59c21256aa789af74f6b7c239_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3a6f4a55730d59c21256aa789af74f6b7c239_2_1380x776.jpeg 2x" data-dominant-color="939299"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error 1</span><span class="informations">1920×1080 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Selecting “add data”, program stalls for a few seconds and then crashes with the following error message. Note that icons also appear to be corrupted.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edd570c8018418bbd05ad778f4288a796e6f92bc.jpeg" data-download-href="/uploads/short-url/xVYsc8mvm85pvBy8aMK4OiMyAwY.jpeg?dl=1" title="Error 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edd570c8018418bbd05ad778f4288a796e6f92bc_2_690x388.jpeg" alt="Error 2" data-base62-sha1="xVYsc8mvm85pvBy8aMK4OiMyAwY" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edd570c8018418bbd05ad778f4288a796e6f92bc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edd570c8018418bbd05ad778f4288a796e6f92bc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edd570c8018418bbd05ad778f4288a796e6f92bc_2_1380x776.jpeg 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error 2</span><span class="informations">1920×1080 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @muratmaga (2025-07-27 04:25 UTC)

<p>After Slicer crashes, launch it again. Go to Help-&gt;Report a bug, and then choose the <strong>2nd</strong> (not the top one) entry from the top and cop <strong>all</strong> entries in the that log file and paste it here.</p>

---

## Post #12 by @lassoan (2025-07-27 06:39 UTC)

<p>It looks like a Windows system configuration problem and not something specific to Slicer. You can try File/Open in other software to confirm.</p>
<p>Such error is usually caused by misbehaving mapped drives (that are no longer available or implemented incorrectly). Maybe unmapping the “Echinosorex” and “Media 000…” drives will fix the issue. A workaround is to not use the file open dialog but drag-and-drop files from Windows Explorer to the Slicer application window.</p>

---
