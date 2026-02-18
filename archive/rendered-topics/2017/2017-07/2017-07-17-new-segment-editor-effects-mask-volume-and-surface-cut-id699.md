# New segment editor effects: Mask volume and Surface cut

**Topic ID**: 699
**Date**: 2017-07-17
**URL**: https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699

---

## Post #1 by @lassoan (2017-07-17 13:30 UTC)

<p>See short demo video of the new “Mask volume” and “Surface cut” Segment editor effects here:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>These effects were developed by <strong>Kyle Macneil</strong> (Med-i Lab, Queen’s University; SPL, Brigham and Women’s Hospital), with help from <a class="mention" href="/u/lassoan">@lassoan</a>  and <a class="mention" href="/u/fedorov">@fedorov</a> . Thank you for your contribution!</p>
<p>Mask volume: Blanks out a segment or surrounding area in a volumetric image. Useful for quick removal of unwanted objects (such as CT table) or showing only a selected organ. It can also be used for creating a binary mask for registration, bias correction, etc. This effect essentially makes “Mask scalar volume” module functionality available conveniently in Segment editor.</p>
<p>Surface cut: Creates a surface from a set of points placed at the boundary of a structure in multiple views. The surface then can be used to create a segment or added or removed from an existing segment. The surface can be edited in slice and 3D views in real-time. Useful for quick approximate segmentation of structures with mostly convex shape. This effect essentially makes “Markups to model” module functionality available conveniently in Segment editor.</p>
<p>Available in <strong>latest nightly build</strong> in <strong>SegmentEditorExtraEffects extension</strong>.</p>
<p>Feedback and suggestions are welcome.</p>

---

## Post #2 by @Fernando (2017-07-18 20:56 UTC)

<p>They are awesome, thank you!</p>

---

## Post #3 by @xackey (2018-01-06 05:40 UTC)

<p>Thank you for this nice tool!<br>
But, I noticed that masked image and segmentation did not become same shape. They are slightly different shape as shown in the attached image below.<br>
Is is bug?<br>
Could you give me any suggestion?</p>

---

## Post #4 by @xackey (2018-01-06 05:41 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d61d4cb545999008b0e66a93a5a740a47beda5dc.jpeg" data-download-href="/uploads/short-url/uy8X4OYWDLZ8B3CHXP6y44XXvoU.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61d4cb545999008b0e66a93a5a740a47beda5dc_2_690x388.jpg" alt="image" data-base62-sha1="uy8X4OYWDLZ8B3CHXP6y44XXvoU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61d4cb545999008b0e66a93a5a740a47beda5dc_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61d4cb545999008b0e66a93a5a740a47beda5dc_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61d4cb545999008b0e66a93a5a740a47beda5dc_2_1380x776.jpg 2x" data-dominant-color="DADCD9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-01-06 06:29 UTC)

<p>Yes, the mask is somewhat smoothed, see more information in this <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues/6">bug report</a>. It is in easy fix, we just did not get to it yet, because the difference is so little that it is even hard to notice.</p>
<p>Is this causing significant error for you?<br>
Are you a developer, would you be interested trying to fix it?</p>

---

## Post #6 by @xackey (2018-01-06 10:24 UTC)

<p>Yes, I am very interested in fix.<br>
I am Japanese radiologist in university hospital. I want to evaluate CT density histogram of lung nodule, but I don’t know how to do this by 3D slicer (Do you know this?).<br>
So, as an alternative way, I want to analyze masked images using ImageJ software. But if masked images and segmentation are different, histogram will be different.</p>

---

## Post #7 by @timeanddoctor (2018-01-06 10:47 UTC)

<p>I have also confused by this bug. Thanks!</p>

---

## Post #8 by @lassoan (2018-01-07 03:58 UTC)

<p>I’ve updated mask volume effect to use the segment’s binary labelmap representation instead of closed surface representation, so now it should work as you expected. The update is available if you reinstall Slicer or SegmentEditorExtraEffects extension on Jan 7 or later.</p>

---

## Post #9 by @Saima (2020-01-23 04:30 UTC)

<p>Hi Andras,<br>
I am using surface cut but it do not make a surface rather it only makes a surface for only working slice. How it automatically selects all slices. is there any key to use with it.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #10 by @lassoan (2020-01-23 11:24 UTC)

<p>Scissors effect affect all slices. Do you mean that you would like to cut all <em>segments</em> at once?</p>

---

## Post #11 by @Saima (2020-01-24 05:45 UTC)

<p>I want to select all segments using the surfacecut tool to have a surface but I am unable to do it as described in the video for surface cut for segmenting heart. the surface cut tool only selects the portion of segment using fiducials in the working slice.</p>

---

## Post #12 by @Saima (2020-01-24 06:46 UTC)

<p>Thanks andras i figured out what i was doing wrong. the segment needs to be selected in red window and in greean and yellow as well. then it creates a surface in 3d.</p>

---

## Post #13 by @Hasan_Imanli (2021-01-29 13:36 UTC)

<p>Hi Andras,</p>
<p>This seems to be very helpful tool, although it does not appear on my Slicer 3D (V 4.11.20200930, installed on Mac Pro macOS Big Sur).</p>
<p>Do you know how to fix it?</p>
<p>Thank you in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bfeadfe73886f2d0b07863dd82ad26384b08ab8.jpeg" data-download-href="/uploads/short-url/8yJONQGHPv4DgwEo1E4tR1RkAR2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bfeadfe73886f2d0b07863dd82ad26384b08ab8_2_690x152.jpeg" alt="image" data-base62-sha1="8yJONQGHPv4DgwEo1E4tR1RkAR2" width="690" height="152" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bfeadfe73886f2d0b07863dd82ad26384b08ab8_2_690x152.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bfeadfe73886f2d0b07863dd82ad26384b08ab8_2_1035x228.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bfeadfe73886f2d0b07863dd82ad26384b08ab8.jpeg 2x" data-dominant-color="E2E4E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1180×260 58.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @lassoan (2021-01-29 15:09 UTC)

<p>See above - these effects are provided by <strong>SegmentEditorExtraEffects extension</strong> .</p>

---

## Post #15 by @Hasan_Imanli (2021-01-29 16:33 UTC)

<p>Excellent, found it. Thank you so much</p>

---

## Post #16 by @labakoum_badr-eddine (2023-01-10 00:14 UTC)

<p>please what is the name of the surface cut model on the extension manager<br>
I have already installed the model Markups to model but I did not find in the segment editor part of the application</p>

---

## Post #17 by @lassoan (2023-01-11 04:13 UTC)

<p>Surface cut effect will show up in Segment Editor module after you install SegmentEditorExtraEffects extension.</p>

---

## Post #18 by @labakoum_badr-eddine (2023-01-12 16:04 UTC)

<p>yes it’s true I uninstalled it and I install it and it works very well</p>

---
