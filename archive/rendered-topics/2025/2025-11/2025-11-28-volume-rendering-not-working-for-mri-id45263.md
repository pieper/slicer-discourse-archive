# Volume Rendering not working for MRI

**Topic ID**: 45263
**Date**: 2025-11-28
**URL**: https://discourse.slicer.org/t/volume-rendering-not-working-for-mri/45263

---

## Post #1 by @Maleia_Tye (2025-11-28 07:38 UTC)

<p>As the title says, I’m not getting a 3D Volume rendering with an MRI.</p>
<p>Preface: I’m able to get a 3D Volume view for a CT scan, this seems to only be impacting an MRI.</p>
<p>Probably additional helpful information: My project is to turn my MRI scan into a 3D print. I’ve been following a guide at <a href="https://www.youtube.com/watch?v=ToIkOpDVfpw" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=ToIkOpDVfpw</a> and <a href="https://www.youtube.com/watch?v=SOk3QtgDOIc" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=SOk3QtgDOIc</a>; and when that wasn’t working out, I checked out this video for the first portion of this guide <a href="https://www.youtube.com/watch?v=k1WIpwV-8lE" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=k1WIpwV-8lE</a>. I’ve also googled this but “3D Slicer MRI not Volume Rendering” did not come up with any solutions, the top result from 2023 has many complications or differences that I’m not using.</p>
<p>My 3D Slicer version is 5.10.0, Windows 11, AMD CPU/GPU, 64GB of RAM. Using DICOM files from the .iso file from my hospital (additional information, the CT Scan is also from the same hospital).</p>
<p>My steps have been: 1) Import the DICOM files from the disc, 2) Examine &amp; Load, [Important: It does not spit out any error messages on this step. It has thrown error messages before when I was figuring out how to get a CT Scan going][the MRI scan images show up normally] 3) Go to the Volume Rendering drop-down option. 4) Click on the hide/show eye icon. Nothing happens.</p>
<p>I’ve tried “Fit to Volume”, I’ve tried “Center View” on the box that should have the 3D Render. The ROI box shows up right in the middle of the window. I’ve tried every different preset. When I was doing the CT Scan, sometimes I had to check the Crop Enable/Disable box to get it to work, that has not made a difference. I’ve tried messing around with the color ranges on the Advances/Scalar Opacity &amp; Scalar Color Mapping. I’ve tried all three types of rendering (GPU, CPU, and Multi-Volume). I’ve tried the “Shift” slider. I’ve tried “Synchronize with Volumes Module”. And lastly, I’ve tried uninstalling and reinstalling the program.</p>
<p>I’m at a complete loss. Is there anything else I can try? Because the one alternative program that I’ve managed to make any progress on, can only do one series at a time, (and I assume it’s because of that) the 3D model comes out in too poor of resolution to work with, along with some other issues.</p>
<p>Thank you for reading my post, I know it was long, but I’ve been trying everything I can think of before posting.</p>

---

## Post #2 by @Maleia_Tye (2025-11-28 16:49 UTC)

<p>Sorry, some additional info I forgot to include, my CPU gets pretty pegged on task manager, and I hear the fans going crazy, when I’m going into the Volume Rendering screen for the CT Scan; but when I’m trying to do it for the MRI, there’s no increase of the CPU load. So it’s definitely not trying / not just taking forever to render it.</p>

---

## Post #3 by @pieper (2025-11-29 19:36 UTC)

<p>One suggestion: look in the Volumes module at the Volume Information section and compare the CT to the MR.  Volume Rendering works with Scalar volumes, and it’s possible the MR data you loaded is something else, like a Vector volume that won’t render directly.  If you find differences you don’t understand, post screenshots of the Volume Information and people may be able to make suggestions.</p>

---

## Post #4 by @Maleia_Tye (2025-11-29 20:31 UTC)

<p>Okay, I wrote a whole lot out, the volume type is Scalar. However, I managed to make progress on accident! While I was in the Volumes view that you were pointing me to, I decided to try a “Center Volume” button that I hadn’t seen previously. And it must be different than the other center/fit buttons in the Volume Rendering screen, because now all the 3D models for the MRI show up how I was expecting them to!</p>
<p>Anyway, thank you a ton, even if it wasn’t direct help. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
