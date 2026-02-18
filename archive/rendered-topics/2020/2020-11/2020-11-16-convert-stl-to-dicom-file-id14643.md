# Convert stl to DICOM file

**Topic ID**: 14643
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/convert-stl-to-dicom-file/14643

---

## Post #1 by @archery (2020-11-16 17:57 UTC)

<p>Hello,<br>
I was using 4.10.2 to convert stl to DICOM. However, after update to 4.11.2 I could not fund functionality. Can anyone help me with this?<br>
Thank you,<br>
Amy</p>

---

## Post #2 by @lassoan (2020-11-16 18:43 UTC)

<p>See step-by-step instructions for DICOM export here <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database</a></p>
<p>If you have any specific questions then let us know.</p>

---

## Post #3 by @archery (2020-11-16 17:52 UTC)

<p>Can you please share the tip? Thank you!</p>

---

## Post #4 by @archery (2020-11-16 19:38 UTC)

<p>Thank you for sharing. The file I need to convert is a stl file and when I follow the instruction (right-click to “Export to DICOM”) there is no option to select the export type in the bottom left of the export dialog. I need to convert the stl file to an RT structure set. Do you mind giving me more guidance?<br>
Thank you,<br>
Amy</p>

---

## Post #5 by @lassoan (2020-11-16 19:40 UTC)

<p>You need to convert it to segmentation first. You also need the associated CT image - RT structure sets cannot be generated and interpreted without a referenced CT.</p>

---

## Post #6 by @archery (2020-11-16 20:17 UTC)

<p>How do I create an associated CT image? Do I import one to the software? How do I make them associated? in 4.10.2, I only need to do “Mesh to Lable Map” and then I can export it as a DICOM file.<br>
Thank you again for your help!</p>

---

## Post #7 by @lassoan (2020-11-16 21:36 UTC)

<p>I assumed you already have a CT image that the STL model was derived from. You can of course create a fake CT for it, but to tell if it is the right answer, we would need to know what you would like to achieve at the end.</p>
<p>What is the overall goal of your project? Why do you need to convert STL file to DICOM RT structure set?</p>

---

## Post #8 by @archery (2020-11-16 22:09 UTC)

<p>I use a 3D camera to capture the patient’s body contour which was truncated by CT (limited CT FOV). With the 3D captured body contour we can make up for the missing information. I want to import the 3D scan as an RT-struture to the TPS and fill up the missing tissue with the water.<br>
Thank you!</p>

---

## Post #9 by @archery (2020-11-16 23:04 UTC)

<p>or… can it be converted to a “CT scan”?  I think it was working in that way in the old version?<br>
Or… is there any chance I can download the 4.10.2?</p>

---

## Post #10 by @lassoan (2020-11-16 23:12 UTC)

<p>You can load the CT, expand it using Crop volume module and a ROI, register it to the surface scan, and use Mask volume effect (provided by SegmentEditorExtraEffects extension) to fill the region inside the surface scan with 0 HU. You can then export this modified CT to DICOM and use it in your treatment planning system. I don’t think there is a need to export DICOM RT structure sets.</p>

---

## Post #11 by @archery (2020-11-16 23:24 UTC)

<p>Do I have to load the CT? Can I just convert the stl to DICOM? I can register them in the TPS.<br>
Thank you!</p>

---

## Post #12 by @collamaf (2021-12-21 09:31 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> ,<br>
I am dealing with a task much similar to the one of <a class="mention" href="/u/archery">@archery</a> .<br>
I would like to ask you which is in your opinion the best/most efficient way to “register the CT to the surface scan”.<br>
I am having some good results with the module “ModelRegistration” of IGT, that however works between models, and thus requires to convert somehow the whole CT to a model (I managed to do it via semi automatic segmentation of the whole CT).<br>
Do you have any better suggestion?<br>
Thanks!</p>

---

## Post #13 by @lassoan (2021-12-22 05:05 UTC)

<p>For quick registration you can use register the CT to the surface scan based on 4-6 matching landmark points, using Fiducial registration wizard module in SlicerIGT extension.</p>
<p>You might improve registration further by creating a skin surface model from the CT using Segment Editor, extract relevant surface parts using Dynamic modeler module’s “Select by points” tool, and then use “Model registration” module to compute the registration. This requires clicking around in a couple of modules, but if you need to do this regularly then the process can be automated using Python scripting.</p>

---

## Post #14 by @collamaf (2021-12-28 08:14 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> , thanks very much for the tips! I will go through them and eventually let you know in this post!<br>
Have a nice new year!</p>

---

## Post #15 by @Mena_Mikhail (2023-06-07 15:17 UTC)

<p>hi,<br>
i’m trying to take an STL model from a dicom CT skull, modify it and return it as a dicom file so i can use it in navigation. The idea is to load it onto the navigation and register it to the old CT, however when i’m stuck as the exported file has no images<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/281972d02e48506d7451fb29a6130c51a6c90719.png" data-download-href="/uploads/short-url/5IJCyN8MFTDR69crBdOhthF0Lpv.png?dl=1" title="Screenshot 2023-06-07 181710" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/281972d02e48506d7451fb29a6130c51a6c90719_2_690x372.png" alt="Screenshot 2023-06-07 181710" data-base62-sha1="5IJCyN8MFTDR69crBdOhthF0Lpv" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/281972d02e48506d7451fb29a6130c51a6c90719_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/281972d02e48506d7451fb29a6130c51a6c90719_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/281972d02e48506d7451fb29a6130c51a6c90719_2_1380x744.png 2x" data-dominant-color="2E3133"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-07 181710</span><span class="informations">1916×1034 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @Mena_Mikhail (2023-06-07 15:30 UTC)

<p>it worked by filling the mask with 1000 HU, but the cuts are grainy<br>
any advise<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3d3ac9f2b310ed1a4d2226eefc8011ef3bb48d9.png" data-download-href="/uploads/short-url/nnhkWsbqRy5RcS22PnZfLdCQ2Pn.png?dl=1" title="Screenshot 2023-06-07 183036" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d3ac9f2b310ed1a4d2226eefc8011ef3bb48d9_2_690x354.png" alt="Screenshot 2023-06-07 183036" data-base62-sha1="nnhkWsbqRy5RcS22PnZfLdCQ2Pn" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d3ac9f2b310ed1a4d2226eefc8011ef3bb48d9_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d3ac9f2b310ed1a4d2226eefc8011ef3bb48d9_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3d3ac9f2b310ed1a4d2226eefc8011ef3bb48d9_2_1380x708.png 2x" data-dominant-color="2F3235"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-07 183036</span><span class="informations">1894×972 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @BlakeSlicer (2023-11-02 02:34 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I am trying to do something similar to <a class="mention" href="/u/archery">@archery</a>. I would like to convert a STL file containing a segmentation of a bone back to a DICOM file similar to a CT scan for use in other software which deals with DICOM files. Is this possible? Thanks!</p>

---

## Post #18 by @lassoan (2023-11-02 03:01 UTC)

<aside class="quote no-group" data-username="Mena_Mikhail" data-post="16" data-topic="14643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mena_mikhail/48/66321_2.png" class="avatar"> Mena_Mikhail:</div>
<blockquote>
<p>it worked by filling the mask with 1000 HU, but the cuts are grainy<br>
any advise</p>
</blockquote>
</aside>
<p>You can use the “Soft edge” option in “Mask volume” effect to make the edges smooth.</p>
<aside class="quote no-group" data-username="BlakeSlicer" data-post="17" data-topic="14643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e274bd/48.png" class="avatar"> BlakeSlicer:</div>
<blockquote>
<p>I would like to convert a STL file containing a segmentation of a bone back to a DICOM file similar to a CT scan for use in other software which deals with DICOM files. Is this possible?</p>
</blockquote>
</aside>
<p>Yes, sure. See this topic:</p>
<aside class="quote" data-post="1" data-topic="32524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e274bd/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/stl-file-to-fake-ct-scan-dicom/32524">STL file to fake CT scan/DICOM?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have a STL of a segmented bone. I would like to convert the STL back to a CT scan as a DICOM to be used in another software which processes images. 
I’ve imported the STL files as a segmentation and can now scroll though the slices of the STL part as if it was a CT scan. 
Can I save these slices as DICOM?
  </blockquote>
</aside>


---

## Post #19 by @lassoan (2025-09-20 22:17 UTC)

<p>A post was split to a new topic: <a href="/t/read-ge-vol-files/44539">Read GE .vol files</a></p>

---
