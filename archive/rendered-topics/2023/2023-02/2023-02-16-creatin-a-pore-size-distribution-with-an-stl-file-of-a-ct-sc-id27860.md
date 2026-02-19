---
topic_id: 27860
title: "Creatin A Pore Size Distribution With An Stl File Of A Ct Sc"
date: 2023-02-16
url: https://discourse.slicer.org/t/27860
---

# Creatin a Pore Size Distribution with an .stl file of a CT Scan of a tensile specimen

**Topic ID**: 27860
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/creatin-a-pore-size-distribution-with-an-stl-file-of-a-ct-scan-of-a-tensile-specimen/27860

---

## Post #1 by @thorbenjt (2023-02-16 11:56 UTC)

<p>Hello there,</p>
<p>I am trying to isolate the pores in my .stl file of a tensile specimen. I figured, that i have to load the data as a “segmentation” into 3D Slicer. I also figured, how to change the amount of slices, such that i could mark every pore per hand. But that would take forever. So i tried out the “treshold” feature, but this doesn’t work. First, i cant change the treshould values and second, 3D Slicer seems to not be able to recognice the part at all. Instead of marking a part of the slice in the 4 sceens on the left, the hole screen is blinking in the predefined colour of the segmentation.<br>
Sadly, i cant upload the .stl file …<br>
I am using Mac OS Ventura 13.1 on a Macbook Air M2<br>
I would appreciate it very much, if someone could assist me with this problem.<br>
Here is a screenshot of my screen, when i use the treshold feauture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9060192f1d8d8ae549e1c751216559fcc710e2bb.png" data-download-href="/uploads/short-url/kBcE1xXpCSMHtHx9LzExNjin9ID.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9060192f1d8d8ae549e1c751216559fcc710e2bb_2_578x500.png" alt="image" data-base62-sha1="kBcE1xXpCSMHtHx9LzExNjin9ID" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9060192f1d8d8ae549e1c751216559fcc710e2bb_2_578x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9060192f1d8d8ae549e1c751216559fcc710e2bb_2_867x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9060192f1d8d8ae549e1c751216559fcc710e2bb_2_1156x1000.png 2x" data-dominant-color="B5A78A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1956×1690 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @thorbenjt (2023-02-16 14:06 UTC)

<p>Ok, i made progress. I scliced the .stl file into .tiff images and loaded them into Slicer. Now, the treshold values works really well with the part. But i cant change the treshold values, such that i only can select the pores…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72b582d43a94d5cc5e4705c6ac1b3bede0f8ae5e.jpeg" data-download-href="/uploads/short-url/gmLjFyVlGWddYDRsiSodwzc1Xvo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72b582d43a94d5cc5e4705c6ac1b3bede0f8ae5e_2_690x431.jpeg" alt="image" data-base62-sha1="gmLjFyVlGWddYDRsiSodwzc1Xvo" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72b582d43a94d5cc5e4705c6ac1b3bede0f8ae5e_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72b582d43a94d5cc5e4705c6ac1b3bede0f8ae5e_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72b582d43a94d5cc5e4705c6ac1b3bede0f8ae5e_2_1380x862.jpeg 2x" data-dominant-color="40403F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @mikebind (2023-02-16 23:15 UTC)

<p>You should be able to type values into the “Threshold Range” or to move the ends of the slider just below those numbers to change the threshold range. What happens when you try to do that?</p>

---

## Post #4 by @thorbenjt (2023-02-17 07:36 UTC)

<p>That’s exactly what i have tried and it worked out just fine. With the “island” effect, i created a segment for each pore. Then i looked into the statistics of the segments, e.g. volume, an found at, that the dimensions are not right.<br>
Assuming, all pores are sphere-like pores, the volume-data leads to a mean radius of 2mm. But the thinnest part of the tensile specimen, the gauge-section, is just 1mm in diamater.<br>
I checked the dimensions and found out, that the dimensions are 100x bigger, as they should be.</p>
<p>Regarding my first try, loading the .stl file into 3D Slicer as a segmentation, there was no such problem. But the treshold effect did not work.<br>
Is there a solution, to make the treshold effect work, such that i dont have to worry about the dimensions?</p>

---

## Post #5 by @thorbenjt (2023-02-17 08:19 UTC)

<p>If no one has a solution including me  i will just devide the radii by a factor of 100.</p>

---

## Post #6 by @mikebind (2023-02-17 18:02 UTC)

<p>I think .tiff images may not have dimensions included, and with no dimensional information, Slicer may assume that each voxel is a cubic 1 mm.   If you know what the true voxel dimensions should be, you can enter them directly using the “Volumes” module, just open the “Volume Information” section, and enter the correct voxel dimensions.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d1d299f05f16907a1de8d58bee544871e520829.png" alt="image" data-base62-sha1="8IDBAoD1pQL6hyPtNuAN0qAnsRr" width="575" height="407"></p>
<p>If this is a one-off analysis, the procedure you’ve worked out is fine.  If you will be doing this over and over again, then it will be more efficient to skip the tiff slicing step.  You can load your STL, create an image volume which contains that same region in 3D space (at a voxel resolution of your choosing), create a segmentation based on that image volume, create a segment in that segmentation which corresponds to your part by importing from the STL model as the surface representation of the segment, and carry out your processing from there.  It sounds like a lot of steps, but if you have some programming experience you could fully automate all of these steps fairly easily into a python Slicer module.  That’s really only worth it if you have many of these to do, since it will take some time invested to implement, but if you see yourself doing similar sorts of processing in the future, learning how to do automate a workflow like this in Slicer could be well worth your time.</p>

---

## Post #7 by @tsehrhardt (2023-02-18 13:45 UTC)

<p>This should work just importing the STL as a segmentation as you did. When you go to threshold the pores or basically everything that is not your STL, select “Outside all Segments” as the editable area.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf80c188f80046ec3e845bcffe175cb3e9d2c4bd.jpeg" data-download-href="/uploads/short-url/tBEH4W4kWAqHoqll5ToEcZESUvH.jpeg?dl=1" title="2023-02-18_8-41-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf80c188f80046ec3e845bcffe175cb3e9d2c4bd_2_690x377.jpeg" alt="2023-02-18_8-41-29" data-base62-sha1="tBEH4W4kWAqHoqll5ToEcZESUvH" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf80c188f80046ec3e845bcffe175cb3e9d2c4bd_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf80c188f80046ec3e845bcffe175cb3e9d2c4bd_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf80c188f80046ec3e845bcffe175cb3e9d2c4bd_2_1380x754.jpeg 2x" data-dominant-color="B4B1B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_8-41-29</span><span class="informations">1920×1050 90.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then you can use the Islands tool to Remove the “box” which is outside your STL (assuming the pores do not connect to the outside.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b2c6fa767e6ad2cae15bcd29c03aaa0a41ee97.jpeg" data-download-href="/uploads/short-url/zcou97423WckpQGcbOVNdSOO0Fp.jpeg?dl=1" title="2023-02-18_8-39-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b2c6fa767e6ad2cae15bcd29c03aaa0a41ee97_2_690x377.jpeg" alt="2023-02-18_8-39-11" data-base62-sha1="zcou97423WckpQGcbOVNdSOO0Fp" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b2c6fa767e6ad2cae15bcd29c03aaa0a41ee97_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b2c6fa767e6ad2cae15bcd29c03aaa0a41ee97_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b2c6fa767e6ad2cae15bcd29c03aaa0a41ee97_2_1380x754.jpeg 2x" data-dominant-color="A09FA6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_8-39-11</span><span class="informations">1920×1050 95.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You should then be left with the inside pores that do not connect to the outside.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df154c91be964e01a697cf854c0c874c57576826.jpeg" data-download-href="/uploads/short-url/vPu6L4hYxoLKevWifNO1WnWQKhM.jpeg?dl=1" title="2023-02-18_8-39-33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df154c91be964e01a697cf854c0c874c57576826_2_690x377.jpeg" alt="2023-02-18_8-39-33" data-base62-sha1="vPu6L4hYxoLKevWifNO1WnWQKhM" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df154c91be964e01a697cf854c0c874c57576826_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df154c91be964e01a697cf854c0c874c57576826_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df154c91be964e01a697cf854c0c874c57576826_2_1380x754.jpeg 2x" data-dominant-color="9394A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_8-39-33</span><span class="informations">1920×1050 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
