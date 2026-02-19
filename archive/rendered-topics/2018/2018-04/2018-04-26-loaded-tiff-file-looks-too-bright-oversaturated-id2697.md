---
topic_id: 2697
title: "Loaded Tiff File Looks Too Bright Oversaturated"
date: 2018-04-26
url: https://discourse.slicer.org/t/2697
---

# Loaded tiff file looks too bright/oversaturated

**Topic ID**: 2697
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/loaded-tiff-file-looks-too-bright-oversaturated/2697

---

## Post #1 by @romip (2018-04-26 11:55 UTC)

<p>Hi Everyone,</p>
<p>Probably a silly question, but I am struggling to open my CLSM images.</p>
<p>I couldn’t open my original file (.lsm) so I converted the stack to images using imagej (save as → Image sequence), but something weird happens. I have two stacks - each for each channel/color, when I open one of them in Slicer it looks just fine, but the other one looks completely wrong. However, when I open the problematic one in ImageJ or even in the Windows Photo viewer it looks just fine.<br>
The image in Slicer looks over saturated to the point that it barely matches the original. Anyone has encountered this problem before? I am attaching a picture for better understanding of the problem.</p>
<p>Thanks in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7ad64cab83634986ff45c394c9680241a520475.jpeg" data-download-href="/uploads/short-url/zl3qD6MiGiGa0lvQnBUEFHcCvHv.jpeg?dl=1" title="Untitled-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ad64cab83634986ff45c394c9680241a520475_2_690x327.jpeg" alt="Untitled-1" data-base62-sha1="zl3qD6MiGiGa0lvQnBUEFHcCvHv" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ad64cab83634986ff45c394c9680241a520475_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ad64cab83634986ff45c394c9680241a520475_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7ad64cab83634986ff45c394c9680241a520475_2_1380x654.jpeg 2x" data-dominant-color="AF7B96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled-1</span><span class="informations">2404×1142 567 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-04-26 21:29 UTC)

<p>Ddid you try adjusting the window/level using the left mouse button (or the volumes module)?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/Volumes" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/Volumes</a></p>

---

## Post #3 by @Jacob_Mccleary (2019-08-07 21:04 UTC)

<p>I had the same issue with some .tiff files. I switched my LUT from green to grey in ImageJ and it solved the problem.</p>

---
