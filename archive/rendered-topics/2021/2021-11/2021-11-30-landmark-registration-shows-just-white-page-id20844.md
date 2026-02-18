# Landmark registration shows just white page

**Topic ID**: 20844
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/landmark-registration-shows-just-white-page/20844

---

## Post #1 by @lolamartinalonso (2021-11-30 14:25 UTC)

<p>Operating system:64 bit<br>
Slicer version:4.11.20210226<br>
Expected behavior:<br>
Actual behavior:</p>
<p>When I click on Landmark registration I am getting this type of error that the page appears white, and I cannot click anywhere.</p>
<p>I do not know why is it occurring now because I have used so many times before this volume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/391abadc76bf3e8d87982c3257897012213338ab.png" data-download-href="/uploads/short-url/89au26CiXG9T4VN9vTgaF4hCymL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391abadc76bf3e8d87982c3257897012213338ab_2_690x373.png" alt="image" data-base62-sha1="89au26CiXG9T4VN9vTgaF4hCymL" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391abadc76bf3e8d87982c3257897012213338ab_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391abadc76bf3e8d87982c3257897012213338ab_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/391abadc76bf3e8d87982c3257897012213338ab_2_1380x746.png 2x" data-dominant-color="FDFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-11-30 14:34 UTC)

<p>Hmm, can you share the error log?</p>

---

## Post #3 by @lolamartinalonso (2021-11-30 14:38 UTC)

<p>Any error log appears, it´s like only this volume is not working. If I click in all the other modules, it works properly.</p>
<p>I have restarted the computer but the same. I´ll try to re-install it.</p>

---

## Post #4 by @pieper (2021-11-30 14:41 UTC)

<p>Here’s how to look in the error log:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report</a></p>

---

## Post #5 by @lolamartinalonso (2021-11-30 14:47 UTC)

<p>Oh, I understand; here it is the error log:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/515b96d2b6711afcabffdd9a9e00d12867f4a456.png" data-download-href="/uploads/short-url/bBIU2PeCFQaUCA8p7mZfEqX2BIW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/515b96d2b6711afcabffdd9a9e00d12867f4a456_2_690x373.png" alt="image" data-base62-sha1="bBIU2PeCFQaUCA8p7mZfEqX2BIW" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/515b96d2b6711afcabffdd9a9e00d12867f4a456_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/515b96d2b6711afcabffdd9a9e00d12867f4a456_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/515b96d2b6711afcabffdd9a9e00d12867f4a456_2_1380x746.png 2x" data-dominant-color="F0F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1038 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2021-11-30 14:51 UTC)

<p>Yes, that’s the error log and it shows where the failure happens but it’s not clear why.  Can you try the latest SlicerPreview version?  If this is specific to a given volume or you can otherwise give step-by-step details about how to reproduce the error we can look into it.</p>

---

## Post #7 by @lolamartinalonso (2021-12-01 07:33 UTC)

<p>I have tried with the SlicerPreview Version and it is still happening the same. The steps that I follow are these ones:</p>
<p>I click on Add Data and I upload two .mha volumes</p>
<p>When they are uploaded I am able to see all the slices and the misalignment between them.</p>
<p>Then I go to Registration and I click on Landmark Registration. And a popup says to  pick the volume to register, so I click on them on the fixed volume and moving volume and when I click on Apply is when the right part of the page appears in white.</p>
<p>But I am able to see all the other volumes, and to click in all parts, except the options of the Landmark Registration where I have to add Landmarks and select the refinement etc.</p>
<p>Does anyone have an idea of what is happening?</p>
<p>Thanks</p>

---

## Post #8 by @pieper (2021-12-01 13:49 UTC)

<p>Do you get the same behavior if you use the sample data?  E.g. the pre-post dental surgery CBCT scans are a good test case.  Perhaps there’s something different about your mha files?  Can you share them or describe them?</p>

---

## Post #9 by @lolamartinalonso (2021-12-02 12:35 UTC)

<p>The problem is solved!</p>
<p>The day I started having the error, I was trying to change some parameters by clicking on the slice spacing button that is on the screen of each view of the volume.</p>
<p>Today I have clicked on View and then to Restore to default and the Landmark Registration is working properly.</p>
<p>I think that maybe this was the triggering point of this error.</p>
<p>Hope this can help to others.</p>
<p>Thanks for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8166eeeb1259dd50e0d9df927de84541feaa856a.jpeg" data-download-href="/uploads/short-url/isK7T00jO2klzqzh3VGhmGxf4sW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8166eeeb1259dd50e0d9df927de84541feaa856a_2_690x383.jpeg" alt="image" data-base62-sha1="isK7T00jO2klzqzh3VGhmGxf4sW" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8166eeeb1259dd50e0d9df927de84541feaa856a_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8166eeeb1259dd50e0d9df927de84541feaa856a_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8166eeeb1259dd50e0d9df927de84541feaa856a_2_1380x766.jpeg 2x" data-dominant-color="9A9998"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1066 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
