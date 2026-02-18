# Exporting segmentation as 2D image stack

**Topic ID**: 40975
**Date**: 2025-01-07
**URL**: https://discourse.slicer.org/t/exporting-segmentation-as-2d-image-stack/40975

---

## Post #1 by @sulli419 (2025-01-07 01:07 UTC)

<p>Hello,</p>
<p>I am looking for a way to get my segments out of 3D slicer and into a stack of 2D binary images (say TIF). Is this possible?  Naively, it seems possible because Slicer already displays the series of 2D images I want (the segment as I move down the sections of the Z axis).  How to export this?</p>
<p>I followed your instructions for exporting an .stl file and this works great for 3D printing and display, but I cannot find software that can convert this .stl file to a 2D image series.</p>
<p>Thanks</p>
<p>p.s., I am a beginner to slicer but finding it quite nifty.  Thanks for providing so many tools!</p>

---

## Post #2 by @muratmaga (2025-01-07 01:24 UTC)

<p>Since  2D  formats do not preserve such critical imaging metadata about image spacing, orientation and geometry, slicer does not allow 3D volumes to be exported as 2D image sequences. Saving 3D volumes as 2D image series will result in data loss.</p>
<p>Why do you need to export 2D binary masks? What is your use case? perhaps it is doable within Slicer?</p>
<p>If you must, you can export your segmentation as a label map and then save it as a NRRD file, which you can open Fiji/ImageJ, and then save it as 2D image sequence.</p>

---

## Post #3 by @pieper (2025-01-07 13:23 UTC)

<p>Or if you really just want the pictures you can use the Screen Capture module.</p>

---

## Post #4 by @sulli419 (2025-01-07 22:18 UTC)

<p>Thanks.  muratmaga’s suggestion worked great.  In case anyone else is also new here, this is what I did:<br>
After creating segments in Slicer, I opened the module “Data”.  I made sure only the segment I wanted as a 2D image stack was visible.  I then right clicked this segment and selected “export visible segments to binary labelmap” (the .nrrd file).  FIJI/ImageJ was able to open this file as an image stack and resave as a TIF with no problems.<br>
Cheers</p>

---

## Post #5 by @muratmaga (2025-01-07 22:37 UTC)

<p>Yes, that’s possible but not encouraged.</p>
<p>You now lost all the information about the spacing of your scan, possible offset (if your dataset is cropped), and will be having a hard time bringing it back anything you derived from it to Slicer and reliably compare to the original data.</p>
<p>This may or may not be an issue for you, but I am adding this comment for posterity for future users who might be considering using this.</p>

---

## Post #6 by @sulli419 (2025-01-07 22:40 UTC)

<p>Thanks for the warning.  I might come back to this post if I encounter issues.  I suppose this relates to my next question: If I generate a stack of 2D binary images/masks as a TIF in different software, what is the best way to bring them into Slicer as segments?</p>

---

## Post #7 by @muratmaga (2025-01-07 23:25 UTC)

<p>You can use SlicerMorph’s ImageStacks to import any 2D sequence into Slicer.</p>
<p>You can then go to Volumes module and convert the scalar volume to labelmap.</p>

---

## Post #8 by @sulli419 (2025-01-08 21:39 UTC)

<p>Thanks, this also seemed to work.  I didn’t use SlicerMorph (still trying to understand when and when not to).  I just directly dragged into slicer the TIF stack that contained the series of 2D masks.  In the Volume module I corrected for the voxel distortion (as you warned me about), and here I also converted to labelmap (as suggested, see image).  To make Slicer see the labelmap as a segment I went to the Data module, right clicked the recently created labelmap, and selected “convert labelmap to segment node”.  I didn’t test, but the goal is that all the tools in Segment Editor will now work on this imported segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62945be2beb1d32cf6ccadbce9c37597ae0d867e.jpeg" data-download-href="/uploads/short-url/e44Ehe1gnVb71ygpgIyHYUrmBL8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62945be2beb1d32cf6ccadbce9c37597ae0d867e.jpeg" alt="image" data-base62-sha1="e44Ehe1gnVb71ygpgIyHYUrmBL8" width="358" height="500" data-dominant-color="3C3C3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">379×528 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
