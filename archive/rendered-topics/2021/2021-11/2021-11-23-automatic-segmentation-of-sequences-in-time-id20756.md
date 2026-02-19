---
topic_id: 20756
title: "Automatic Segmentation Of Sequences In Time"
date: 2021-11-23
url: https://discourse.slicer.org/t/20756
---

# Automatic segmentation of sequences in time

**Topic ID**: 20756
**Date**: 2021-11-23
**URL**: https://discourse.slicer.org/t/automatic-segmentation-of-sequences-in-time/20756

---

## Post #1 by @Francesca_Pittoni (2021-11-23 18:08 UTC)

<p>Hi everyone!</p>
<p>I imported a 4D TAC scan (10 timeframes) in “volume sequence”, I created a segmentation node, segmenting the first timeframe (aorta) and created a new sequence, setting the correct proxy node.</p>
<p>So, I was wondering if there is a way to make the segmentation in the other time frames “follow the CT intensity map” (a sort of segment registration), so as to obtain all 10 timeframes automatically segmented starting only from the segmentation of the first timeframe (adjusting then manually in case of errors).</p>
<p>Thank you all</p>

---

## Post #2 by @lassoan (2021-11-23 19:32 UTC)

<p>Yes, you can compute displacement across the time sequence using Sequence registration module. It computes a transform sequence that you can apply to the segmentation.</p>

---

## Post #3 by @lassoan (2021-11-24 03:20 UTC)

<p>I’ve added a video tutorial for this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="qVgXdXEEVFU" data-video-title="Create an animated 4D surface model by segmenting a single 3D frame" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=qVgXdXEEVFU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/qVgXdXEEVFU/maxresdefault.jpg" title="Create an animated 4D surface model by segmenting a single 3D frame" width="" height="">
  </a>
</div>


---

## Post #5 by @Francesca_Pittoni (2021-11-24 10:30 UTC)

<p>Thank you so much!!</p>
<p>I followed all the steps, but when I click on “Register”, nothing seems to happen. I attach an image of what I see: the mouse icon is not in the form of a wheel but of a pointer, so it seems to have finished the operation when in reality nothing has happened …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80a48bb8c90b8448226bc168e024294404c05e10.png" data-download-href="/uploads/short-url/im1ExKXsmKymL41roiUiyszvRgA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a48bb8c90b8448226bc168e024294404c05e10_2_690x367.png" alt="image" data-base62-sha1="im1ExKXsmKymL41roiUiyszvRgA" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a48bb8c90b8448226bc168e024294404c05e10_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a48bb8c90b8448226bc168e024294404c05e10_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a48bb8c90b8448226bc168e024294404c05e10_2_1380x734.png 2x" data-dominant-color="A4A9AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1922×1025 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-11-24 13:35 UTC)

<p>Please try with the latest Slicer Preview Release and let us know if you run into any issues.</p>

---

## Post #7 by @Francesca_Pittoni (2021-11-24 15:11 UTC)

<p>I downloaded the latest Preview Release (24/11/2021), however I have the same problem…<br>
Compared to before, the mouse icon for a few seconds was in the form of a wheel, but then immediately becomed a pointer, with the operation not performed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b92057991beba2efbc6689b541f42bffb8fae0eb.png" data-download-href="/uploads/short-url/qpHCJRtCH5Eq4CGzsNm5p2yqqfh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92057991beba2efbc6689b541f42bffb8fae0eb_2_690x369.png" alt="image" data-base62-sha1="qpHCJRtCH5Eq4CGzsNm5p2yqqfh" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92057991beba2efbc6689b541f42bffb8fae0eb_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92057991beba2efbc6689b541f42bffb8fae0eb_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92057991beba2efbc6689b541f42bffb8fae0eb_2_1380x738.png 2x" data-dominant-color="A4A9AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1029 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2021-11-24 15:12 UTC)

<p>Do you see any error messages in the application log?</p>
<p>Does everything work well with the sample data set as shown in the tutorial video?</p>

---

## Post #9 by @Francesca_Pittoni (2021-11-24 15:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b53f36bb4bfc145f51638a6a61c993c53a1955a.png" data-download-href="/uploads/short-url/1Cd7cabtqgzcIIW8DN6z0clbk8y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b53f36bb4bfc145f51638a6a61c993c53a1955a_2_690x354.png" alt="image" data-base62-sha1="1Cd7cabtqgzcIIW8DN6z0clbk8y" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b53f36bb4bfc145f51638a6a61c993c53a1955a_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b53f36bb4bfc145f51638a6a61c993c53a1955a_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b53f36bb4bfc145f51638a6a61c993c53a1955a_2_1380x708.png 2x" data-dominant-color="CBCCCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×987 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The same happens with the sample data set, and here is the Python window</p>

---

## Post #10 by @lassoan (2021-11-24 15:31 UTC)

<p>Thank you, the log is very useful. What exact Windows version do you use?</p>

---

## Post #11 by @Francesca_Pittoni (2021-11-24 15:38 UTC)

<p>| Edition | Windows 10 Home |<br>
| Version | 20H2 |<br>
| Installation date: | 13/04/2021 |<br>
| OS Build | 19042.1348 |<br>
| Experience | Windows Feature Experience Pack 120.2212.3920.0 |<br>
System type: 64-bit operating system, x64-based processor</p>
<p>Thank you for everything you are doing, I really appreciate</p>

---

## Post #12 by @lassoan (2021-11-24 16:13 UTC)

<p>Is your system locale set to English?</p>

---

## Post #13 by @Francesca_Pittoni (2021-11-24 16:19 UTC)

<p>No, it’s in Italian, I translated the info tags I wrote before!</p>

---

## Post #14 by @lassoan (2021-11-24 16:20 UTC)

<p>As a workaround, you can temporarily switch your system locale to English, but I’m working on a proper solution.</p>

---

## Post #15 by @Francesca_Pittoni (2021-11-24 16:54 UTC)

<p>I update you on what I’ve done.<br>
I switched my system locale to English, and now the operation is effectively completed for all 10 time frames.<br>
However I don’t get any results (only an error), and the Python script is this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c04871d007b0af8765c01e60ce3ace696e85455f.png" data-download-href="/uploads/short-url/rr0SWgcKhdZDxmPPJ5vQTBjktC7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c04871d007b0af8765c01e60ce3ace696e85455f_2_690x354.png" alt="image" data-base62-sha1="rr0SWgcKhdZDxmPPJ5vQTBjktC7" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c04871d007b0af8765c01e60ce3ace696e85455f_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c04871d007b0af8765c01e60ce3ace696e85455f_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c04871d007b0af8765c01e60ce3ace696e85455f_2_1380x708.png 2x" data-dominant-color="D4D6D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×987 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lassoan (2021-11-24 16:56 UTC)

<p>You need to choose a different output for volume sequence and transform sequence (it is OK to choose only one and leave the other None).</p>

---

## Post #17 by @Francesca_Pittoni (2021-11-24 17:08 UTC)

<p>Sorry, you’re right.<br>
However correcting this, I still get the error regarding the “returnNode argument”, so then scrolling through the timeframes the segmentation does not change …<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a603f11c493bc173f3467c6b15aa2dbbed590ffa.png" data-download-href="/uploads/short-url/nGDHJIRUtHNM9hZgCzA6SRF24mS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a603f11c493bc173f3467c6b15aa2dbbed590ffa_2_690x369.png" alt="image" data-base62-sha1="nGDHJIRUtHNM9hZgCzA6SRF24mS" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a603f11c493bc173f3467c6b15aa2dbbed590ffa_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a603f11c493bc173f3467c6b15aa2dbbed590ffa_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a603f11c493bc173f3467c6b15aa2dbbed590ffa_2_1380x738.png 2x" data-dominant-color="B7BBBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1027 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @lassoan (2021-11-24 17:10 UTC)

<p>The message is just a warning, you can safely ignore it.</p>
<p>You need to apply the transform to the segmentation as it is explained in the tutorial video. Selection of the transform is done in a popup window and unfortunately the screen recording software did not capture the popup, but it is described in the video at 1:21 in the subtitles where to right-click in Data module and what to select.</p>

---

## Post #19 by @lassoan (2021-11-24 18:16 UTC)

<p><a class="mention" href="/u/francesca_pittoni">@Francesca_Pittoni</a> would you mind trying if replacing content of this file <code>c:\Users\frapi\AppData\Local\NA-MIC\Slicer 4.13.0-2021-11-24\NA-MIC\Extensions-30427\SlicerElastix\lib\Slicer-4.13\qt-scripted-modules\Elastix.py</code> with this content of <a href="https://raw.githubusercontent.com/lassoan/SlicerElastix/master/Elastix/Elastix.py">this file</a> makes it possible to run the registration even when your system locale is set to Italian?</p>

---

## Post #20 by @Francesca_Pittoni (2021-11-24 19:33 UTC)

<p>Thank you very much, now everything works (in English)!</p>
<p>I only have two final questions:<br>
Can I change the segmentation of a timeframe without affecting the others?<br>
And to export the STLs of the timeframes individually, to different files, do I have to go to the “segmentation” module?</p>
<p>Now I’ll try to run it in Italian and I’ll let you know about it</p>

---
