---
topic_id: 17466
title: "Segmentation Of Facial Nerve"
date: 2021-05-05
url: https://discourse.slicer.org/t/17466
---

# Segmentation of facial nerve

**Topic ID**: 17466
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/segmentation-of-facial-nerve/17466

---

## Post #1 by @Balkis_elkhouni (2021-05-05 12:29 UTC)

<p>Hello<br>
I’m not familiar with this segmentation tool and I’m trying to perform an extra cranial facial nerve segmentation on MRI 3D T2W sequences. Can some one help me with the steps to follow to obtain a linear segmentation?</p>

---

## Post #2 by @lassoan (2021-05-21 18:29 UTC)

<p>Probably the easiest way of segmenting facial nerves is to use “Draw tube” effect (provided by SegmentEditorExtraEffects extension) in Segment Editor module. If you don’t need segmentation, but you just want to mark a curve then you can simply <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#place-new-markups">place a curve</a>.</p>

---

## Post #3 by @Balkis_elkhouni (2021-06-08 15:58 UTC)

<p>Thanks a lot, I succeeded with these extensions in segmenting the facial nerve.<br>
My study actually consists of comparing the segmentation of extra cranial facial nerve made by a junior radiologist and a senior radiologist specialized in head and neck.<br>
I have issues when using the RT slicer module to compute haudsorff distance and Dice coefficient. The program always shuts down when trying to compute it or returns zero for all metrics.<br>
I also want to ask if it s possible to compare stored segmentations later when needed.</p>

---

## Post #4 by @lassoan (2021-06-08 17:43 UTC)

<p>Dice coefficient is not applicable to thin or long structures. Hausdorff distance only gives information on the position of the largest deviation, so it does not give you very detailed information either.</p>
<p>If you only need to compare the centerline curve of the nerve (no need to compare radius) then you can write a short Python code snippet that computes detailed statistics (such as mean max error, and 50th, 75th, 95th percentiles; errors in different segments of the nerve, …).</p>
<p>The script could first resample the assessed curve at equal distances (using <code>ResampleCurveWorld</code> method) and then for each control point position get the distance from the ground truth curve (using <code>GetClosestPointPositionAlongCurveWorld</code> method), and add all the distances into a numpy array. You can then use <code>mean</code> and <code>max</code> numpy functions to get the mean error, and <code>percentile</code> numpy function to get percentiles. Probably about 15 lines of Python code in total.</p>

---

## Post #5 by @Balkis_elkhouni (2021-06-08 22:06 UTC)

<p>Thanks for your time and patience. I’ll try to find someone to write the script since it 's too complicated for me. Meanwhile can you check this article ? They used exactely the same technique and coefficient I mentionned using 3d slicer." MR Imaging of the Extracranial Facial Nerve with the CISS Sequence" J.P. Guenette, 2019</p>

---

## Post #6 by @lassoan (2021-06-09 05:10 UTC)

<aside class="quote no-group" data-username="Balkis_elkhouni" data-post="5" data-topic="17466">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/balkis_elkhouni/48/8607_2.png" class="avatar"> Balkis_elkhouni:</div>
<blockquote>
<p>MR Imaging of the Extracranial Facial Nerve with the CISS Sequence" J.P. Guenette, 2019</p>
</blockquote>
</aside>
<p>Regardless of this paper passing peer review, Dice Coefficient metric is not suitable for comparing thin tubular objects. Average Hausdorff distance is meaningful, it is just not very sensitive metric. In addition to average, higher percentiles and/or computing the average for parts of the nerve would have been more informative.</p>
<aside class="quote no-group" data-username="Balkis_elkhouni" data-post="3" data-topic="17466">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/balkis_elkhouni/48/8607_2.png" class="avatar"> Balkis_elkhouni:</div>
<blockquote>
<p>I have issues when using the RT slicer module to compute haudsorff distance and Dice coefficient. The program always shuts down when trying to compute it or returns zero for all metrics.</p>
</blockquote>
</aside>
<p>I’ve just tested Segment Comparison module in Slicer-4.11.20210226 on Windows and it worked well. What Slicer version did you use? Can you attach a screenshot of your Segment Comparison module? Do you see any error message in the application log? (you can open the log of the previous session in menu: Help / Report a bug)</p>

---

## Post #7 by @Balkis_elkhouni (2021-06-11 10:21 UTC)

<p>I see, I’m trying to create a python code and I’ll keep you updated.<br>
I had previousely downloaded Dicom supports easily. Since yesterday any DICOM file is downloaded in fragments and  therefore not suitable for segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d645c0d5da6bf00f108379cd53f5c159ef5bf2c2.png" data-download-href="/uploads/short-url/uzxCI0PN6XSguaCps72kH39VYf8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d645c0d5da6bf00f108379cd53f5c159ef5bf2c2_2_690x431.png" alt="image" data-base62-sha1="uzxCI0PN6XSguaCps72kH39VYf8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d645c0d5da6bf00f108379cd53f5c159ef5bf2c2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d645c0d5da6bf00f108379cd53f5c159ef5bf2c2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d645c0d5da6bf00f108379cd53f5c159ef5bf2c2_2_1380x862.png 2x" data-dominant-color="6B6B73"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @Balkis_elkhouni (2021-06-22 16:28 UTC)

<p>Hello! I tried to use DICOM patcher to group the splitted series but it didnt work. I also tried to export them as NRDD files but with no results either. Do you please have a solution with this issue ?</p>

---

## Post #9 by @lassoan (2021-06-22 18:37 UTC)

<p>This happens because according to the header in the DICOM files, each slice has different orientation. Does the data set comes straight from the scanner or somebody tried to anonymize it?</p>
<p>You can try loading the data set with the latest Slicer Preview Release and you can also try the advanced loading options in the DICOM module.</p>

---

## Post #10 by @Balkis_elkhouni (2021-06-22 19:17 UTC)

<p>I did try the latest preview version with the same result. What should I use in the advanced loading options ?</p>

---

## Post #11 by @lassoan (2021-06-23 02:07 UTC)

<p>When you check “Advanced” checkbox then you will be offered a number of ways to load the selected data set. Select all of them and then see if any of those are usable.</p>
<p>If you cannot find a way to load your data then you may share it with us (make sure that the data is anonymized; upload it somewhere and post the link here) so that we can have a look.</p>

---

## Post #12 by @Balkis_elkhouni (2021-07-17 17:41 UTC)

<p>There was a missing slice in the downloaded document that generated an error.<br>
When segmenting the facial nerve using the draw tube effect, I couldnt separate the different segments. The first point in the segmentation always starts from the last point of the previous one. do you have an idea how to avoid that ?</p>

---

## Post #13 by @lassoan (2021-07-17 20:18 UTC)

<p>You need d tocreate a separate segment for each branch of the nerve. You can later combine them into a single segment, if needed.</p>

---

## Post #14 by @Balkis_elkhouni (2021-07-18 20:38 UTC)

<p>So I cant create the segmentations of two branches of a main trunk in the same segmentation group?  I’m sending you a screen shot.<br>
If no how can I combine them later?<br>
Thanks again !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68da5061376706757933800b05c655d69b1842c5.jpeg" data-download-href="/uploads/short-url/eXzokGJb3DUeZxMa2716KawcTBj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68da5061376706757933800b05c655d69b1842c5_2_690x431.jpeg" alt="image" data-base62-sha1="eXzokGJb3DUeZxMa2716KawcTBj" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68da5061376706757933800b05c655d69b1842c5_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68da5061376706757933800b05c655d69b1842c5_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68da5061376706757933800b05c655d69b1842c5_2_1380x862.jpeg 2x" data-dominant-color="76777E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 369 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2021-07-19 00:04 UTC)

<p>Yes, you can combine them very easily in the end. The simplest is to use masking settings / editable region → inside all segments, then fill the entire volume using Logical operators effect’s / Fill method (or Scissors or Threshold effect).</p>

---

## Post #16 by @Balkis_elkhouni (2021-08-02 16:11 UTC)

<p>Is there any method to obtain the lentgh of a segmented branch in mm ?</p>

---

## Post #17 by @lassoan (2021-08-03 12:06 UTC)

<p>You can extract branches from your segmented tree as a curve node using SlicerVMTK extension. You can enable length measurement for the curve in Markups module.</p>

---

## Post #18 by @Balkis_elkhouni (2021-08-04 17:38 UTC)

<p>Thank you. Is it accurate for segmentations done with the draw tube extension too( piecewise linear) ?</p>

---

## Post #19 by @lassoan (2021-08-04 18:44 UTC)

<p>Draw tube extension can create arbitrary curves, not just piecewise linear. Of course, an analytic curve must be represented in a computer as a set of linear segments for processing and display, but those segments can be as fine resolution as needed.</p>

---

## Post #20 by @Balkis_elkhouni (2021-08-09 14:32 UTC)

<p>I have a problem in extracting the centerline curve with the VMTK module.<br>
It shows a message error " Failed to compute results; VMTK Library is not found"<br>
Can you take a look to these screen shots?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc55977386988a0e1ce88f197e6feb44cdd7f876.jpeg" data-download-href="/uploads/short-url/t9CMyoSa8FTvTL4qOjtEQ9NpDYG.jpeg?dl=1" title="Screen Shot 2021-08-09 at 2.07.01 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc55977386988a0e1ce88f197e6feb44cdd7f876_2_689x360.jpeg" alt="Screen Shot 2021-08-09 at 2.07.01 PM" data-base62-sha1="t9CMyoSa8FTvTL4qOjtEQ9NpDYG" width="689" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc55977386988a0e1ce88f197e6feb44cdd7f876_2_689x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc55977386988a0e1ce88f197e6feb44cdd7f876_2_1033x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc55977386988a0e1ce88f197e6feb44cdd7f876_2_1378x720.jpeg 2x" data-dominant-color="393941"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-09 at 2.07.01 PM</span><span class="informations">5116×2670 880 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbb897963f06505df1de9617d56f73080751b555.jpeg" data-download-href="/uploads/short-url/t4cpCPW91tQrLGNDPbWM4u0wDuR.jpeg?dl=1" title="Screen Shot 2021-08-09 at 1.36.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbb897963f06505df1de9617d56f73080751b555_2_690x392.jpeg" alt="Screen Shot 2021-08-09 at 1.36.15 PM" data-base62-sha1="t4cpCPW91tQrLGNDPbWM4u0wDuR" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbb897963f06505df1de9617d56f73080751b555_2_690x392.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbb897963f06505df1de9617d56f73080751b555_2_1035x588.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbb897963f06505df1de9617d56f73080751b555_2_1380x784.jpeg 2x" data-dominant-color="383736"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-09 at 1.36.15 PM</span><span class="informations">4644×2640 723 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #21 by @lassoan (2021-08-09 19:11 UTC)

<p>Thank you for reporting. This is due to an error that was made when VMTK toolkit was updated to work with most recent version of VTK. You can track resolution of the error here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/37">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">VMTK gone missing recently in Slicer-4.11.20210226</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="19:08:54" data-timezone="UTC">07:08PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The extension installation package does not contain VMTK binaries, only the Slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er module .py files.

It seems that the recent upgrade to VTK9 broke packaging for VTK-8.2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #22 by @rdp1970 (2023-03-21 10:45 UTC)

<p>Hi,<br>
I’m also interested in segmenting the facial nerve on MRI.<br>
What was eventually your method and result?</p>

---

## Post #23 by @lassoan (2023-03-27 03:09 UTC)

<p>Manual segmentation is quite straightforward, but it may take several minutes.</p>
<p>If you want fully automatic segmentation then you can train a deep learning segmentation model, similarly to how <a class="mention" href="/u/cpinter">@cpinter</a>’s group did at the last Slicer project week (see their <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/TeethSegmentation/">project page</a>).</p>

---
