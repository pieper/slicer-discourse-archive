---
topic_id: 29541
title: "Cant Open S Certain Dicom File"
date: 2023-05-19
url: https://discourse.slicer.org/t/29541
---

# Can't open s certain dicom file

**Topic ID**: 29541
**Date**: 2023-05-19
**URL**: https://discourse.slicer.org/t/cant-open-s-certain-dicom-file/29541

---

## Post #1 by @mohammed_alshakhas (2023-05-19 17:24 UTC)

<p>this is the second time it occurred , a dicom file get uploaded yet couldn’t open it . tried reload it again and again and just cant open</p>
<p>notice this error this time whenever opening slicer as well</p>
<p>b’E: cannot create network: 0006:031c TCP Initialization Error: Address already in use\n’</p>
<p>anyway to help with this ?</p>

---

## Post #2 by @pieper (2023-05-19 17:45 UTC)

<p>That indicates another program is using a network port.  If you can’t find the program and kill it by hand probably just rebooting your computer is the easiest.</p>

---

## Post #3 by @mohammed_alshakhas (2023-05-19 17:53 UTC)

<p>i did reset to default and changed the database location and it worked.</p>
<p>another annoying thing was that that file I couldn’t open and couldn’t delete it.</p>

---

## Post #4 by @pieper (2023-05-19 17:56 UTC)

<p>Hard to say.  If you can replicate the issue with specific steps using public data then maybe someone can help you out.</p>

---

## Post #5 by @mohammed_alshakhas (2023-05-19 18:47 UTC)

<p>it is not  a big deal , just wanted to know if there is obvious solution without having to reset the setting</p>

---

## Post #6 by @lassoan (2023-05-21 03:48 UTC)

<p>It seems that you run multiple Slicer executables at the same time, which use the same resources (network ports, database files, etc). This leads to inability to delete the database (the file is open in anther instance) inability to start another listening server on the same port (you can probably ignore this error, as the other instance receives any sent DICOM data), etc. The easiest way to resolve any potential problems is to run only one Slicer instance at a time.</p>

---

## Post #7 by @mohammed_alshakhas (2023-05-21 15:26 UTC)

<p>im not sure what do you mean by single slicer instance !</p>
<p>i tried to select my previous folder for Dicom data and the issue came back again.</p>
<p>two patient appeared and I couldn’t open or delete the data</p>

---

## Post #8 by @lassoan (2023-05-22 00:25 UTC)

<p>Do you get any error messages on screen?<br>
Do you see any error messages in the application log?<br>
In DICOM module / DICOM database settings, does “Remove unavailable data sets” remove the non-loadable patients?</p>

---

## Post #9 by @mohammed_alshakhas (2023-05-22 10:31 UTC)

<p>i didn’t get any error on the screen, it only opens the empty file, and nothing loaded. no patient name or study name.</p>
<p>remove unavailable data set doesn’t change anything</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db7aa2a255c9b3c6e40afa287a2559e297601e62.jpeg" data-download-href="/uploads/short-url/vjBjhbZxQFZQDdpGsYMqwCOBTSW.jpeg?dl=1" title="Screenshot 2023-05-22 at 13.39.42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db7aa2a255c9b3c6e40afa287a2559e297601e62_2_690x448.jpeg" alt="Screenshot 2023-05-22 at 13.39.42" data-base62-sha1="vjBjhbZxQFZQDdpGsYMqwCOBTSW" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db7aa2a255c9b3c6e40afa287a2559e297601e62_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db7aa2a255c9b3c6e40afa287a2559e297601e62_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db7aa2a255c9b3c6e40afa287a2559e297601e62_2_1380x896.jpeg 2x" data-dominant-color="313336"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-22 at 13.39.42</span><span class="informations">1920×1247 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2023-05-23 11:10 UTC)

<p>You get errors for farming to load jpeg images. Do you also have DICOM filter in that folder?</p>
<p>Also, the folder looks like some virtual network drive and its path is very long - both can be problematic.</p>

---
