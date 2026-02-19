---
topic_id: 1574
title: "Black Screen After Downloading Slicer"
date: 2017-12-01
url: https://discourse.slicer.org/t/1574
---

# Black screen after downloading Slicer

**Topic ID**: 1574
**Date**: 2017-12-01
**URL**: https://discourse.slicer.org/t/black-screen-after-downloading-slicer/1574

---

## Post #1 by @Souheil (2017-12-01 16:20 UTC)

<p>Operating system: Windows 7 Enterprise<br>
Slicer version: multiple versions latest 4.9.0<br>
Expected behavior:<br>
Actual behavior: Once slicer is downloaded the only screen that appears is a black screen and no actual ability to use software. I have attempted multiple different versions of splicer with similar outcome.</p>

---

## Post #2 by @ihnorton (2017-12-01 16:32 UTC)

<p>Is there a “Command Prompt” window with any messages? If so, could you please post a screenshot.</p>
<p>It would be helpful if you could try both the 4.8 and 4.6 release versions.</p>

---

## Post #3 by @Souheil (2017-12-01 18:09 UTC)

<p>Thanks for the reply. Below is the screenshot. No error messages</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e19edf20ed91d5b81c776888608035cac2cd422e.jpeg" data-download-href="/uploads/short-url/wbVOk589nU8gPQb6f6Qle6h26jY.jpg?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e19edf20ed91d5b81c776888608035cac2cd422e_2_690x431.jpg" alt="screenshot" data-base62-sha1="wbVOk589nU8gPQb6f6Qle6h26jY" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e19edf20ed91d5b81c776888608035cac2cd422e_2_690x431.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e19edf20ed91d5b81c776888608035cac2cd422e_2_1035x646.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e19edf20ed91d5b81c776888608035cac2cd422e.jpeg 2x" data-dominant-color="6F8AA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1242×776 42.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2017-12-01 18:15 UTC)

<p>Do you use 32-bit or 64-bit Windows 7? (<a href="https://support.microsoft.com/en-ca/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64">https://support.microsoft.com/en-ca/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64</a>)</p>

---

## Post #5 by @Souheil (2017-12-01 18:25 UTC)

<p>I use 32 bit workstation.</p>

---

## Post #6 by @lassoan (2017-12-01 18:41 UTC)

<p>All current Slicer versions are 64-bit software, which don’t run on 32-bit systems. We could still build 32-bit versions of Slicer but don’t do it anymore because the memory space is so limited on 32-bit systems that you would easily run out of memory when working with average-sized images.</p>
<p>What would you like to do with Slicer on your 32-bit computer?<br>
Do you have the option for upgrading the operating system to 64-bit?<br>
Do you have access to a newer computer?</p>

---

## Post #7 by @Souheil (2017-12-01 18:51 UTC)

<p>Thanks for the reply. Certainly can access a 64bit computer. Will circle back if run into problems again.</p>

---

## Post #8 by @JamesGalea (2018-06-18 19:03 UTC)

<p>See my post for this but essentially check if your video card is an integrated one and if so you need the latest Intel update. Most likely you will not be able to update so use my method below.</p>
<p>File link: <a href="https://downloadcenter.intel.com/product/88355" rel="nofollow noopener">https://downloadcenter.intel.com/product/88355</a></p>
<p>Quote:<br>
Version 4.9 brings much improvement and refinement with GPU rendering (Ray Casting) especially a Quality (Normal) option.  With Intel Integrated Graphics esp HD 520, there may be a problem with program running. This is easily sorted by installing the new May 2018 Intel update for integrated graphics. If your laptop or computer needs a specific driver and is unable to install the driver directly from Intel do as follows. Open the *.exe file using 7Zip or equivalent. Go to device manager, choose the video card, choose update driver, have my own driver, then choose the driver from the *.exe folder you have just unzipper. The file should end in *inf. Then restart 3D Slicer and that should be it.</p>

---

## Post #9 by @Soheil_Sabet (2018-12-16 11:53 UTC)

<p>Hi. I use a 64bit Windows 10 Enterprise version. I tried both 4.10 and 4.11 versions but still have the same problem and at start up I see only 4 black rectenangles.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d587d0de2c4651a0264b2ad26f200cc68a7d3c9a.png" data-download-href="/uploads/short-url/usYGuHXidDElUeGOj8bGInWT12i.png?dl=1" title="Slicer%20Problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d587d0de2c4651a0264b2ad26f200cc68a7d3c9a_2_690x295.png" alt="Slicer%20Problem" data-base62-sha1="usYGuHXidDElUeGOj8bGInWT12i" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d587d0de2c4651a0264b2ad26f200cc68a7d3c9a_2_690x295.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d587d0de2c4651a0264b2ad26f200cc68a7d3c9a_2_1035x442.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d587d0de2c4651a0264b2ad26f200cc68a7d3c9a_2_1380x590.png 2x" data-dominant-color="1D1D1C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer%20Problem</span><span class="informations">2560×1096 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2018-12-16 13:30 UTC)

<p>I’ve only seen this happening for very old, 2nd generation Intel chipsets and integrated graphics card. Can you tell us the brand/model of your computer or what CPU and graphics card do you have in it?</p>
<p>CPU and graphics card information is reported in <em>System information</em> application, in <em>System Summary</em> / <em>Processor</em> and  in <em>Components</em> / <em>Display</em> / <em>Adapter Description</em>.</p>

---

## Post #11 by @Soheil_Sabet (2018-12-16 13:43 UTC)

<p>The screenshot of my system info. is attached here…<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf7b3b6a8ffbc28035870ebc45de55fe689a25c.jpeg" data-download-href="/uploads/short-url/oorRSJfW6vCprYjEKX6lwx5jKDq.jpeg?dl=1" title="System%20info" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7b3b6a8ffbc28035870ebc45de55fe689a25c_2_492x500.jpeg" alt="System%20info" data-base62-sha1="oorRSJfW6vCprYjEKX6lwx5jKDq" width="492" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7b3b6a8ffbc28035870ebc45de55fe689a25c_2_492x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf7b3b6a8ffbc28035870ebc45de55fe689a25c_2_738x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf7b3b6a8ffbc28035870ebc45de55fe689a25c.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">System%20info</span><span class="informations">861×874 91.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48b24a6ff453653f58a9f994802faf2b0e475119.jpeg" data-download-href="/uploads/short-url/an6mzy8vnGeSzlRX76KDv6aiARz.jpeg?dl=1" title="Display%20Details" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48b24a6ff453653f58a9f994802faf2b0e475119_2_484x500.jpeg" alt="Display%20Details" data-base62-sha1="an6mzy8vnGeSzlRX76KDv6aiARz" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48b24a6ff453653f58a9f994802faf2b0e475119_2_484x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48b24a6ff453653f58a9f994802faf2b0e475119_2_726x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48b24a6ff453653f58a9f994802faf2b0e475119.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Display%20Details</span><span class="informations">825×851 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Soheil_Sabet (2018-12-16 13:45 UTC)

<p>Thanks alot Mr Lasso.</p>

---

## Post #13 by @lassoan (2018-12-16 13:59 UTC)

<p>This is a generation 2 Intel Core chipset. Current is generation 9. Integrated graphics capabilities of this chipset are insufficient to run Slicer-4.9 or later.</p>
<p>We had to drop support for very old/limited systems to allow using more recent graphics programming interfaces to get hugely improved performance on current hardware.</p>

---
