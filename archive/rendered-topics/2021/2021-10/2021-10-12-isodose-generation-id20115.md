---
topic_id: 20115
title: "Isodose Generation"
date: 2021-10-12
url: https://discourse.slicer.org/t/20115
---

# Isodose Generation

**Topic ID**: 20115
**Date**: 2021-10-12
**URL**: https://discourse.slicer.org/t/isodose-generation/20115

---

## Post #1 by @Cody_Xie (2021-10-12 13:12 UTC)

<p>Hi all,</p>
<p>I would like to create <strong>isodose</strong> and the <strong>color bar</strong>. I followed the isodose tutorial (<a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_Isodose.pptx" class="inline-onebox" rel="noopener nofollow ugc">SlicerRtDoc/tutorials/SlicerRT_Tutorial_Isodose.pptx at master · SlicerRt/SlicerRtDoc · GitHub</a>). However, in the Isodose feature I could only edit the number of iso levels, but <strong>cannot change</strong> the <strong>color</strong>, <strong>dose</strong> and <strong>Opacity</strong> for each level by double clicking (please see the picture below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31da5b85ed46b23b09a25429cdddf898fcaec8f1.jpeg" data-download-href="/uploads/short-url/771dWnvOW8VLQ50cvpVKIx3f31f.jpeg?dl=1" title="Isodose_Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31da5b85ed46b23b09a25429cdddf898fcaec8f1_2_690x369.jpeg" alt="Isodose_Slicer" data-base62-sha1="771dWnvOW8VLQ50cvpVKIx3f31f" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31da5b85ed46b23b09a25429cdddf898fcaec8f1_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31da5b85ed46b23b09a25429cdddf898fcaec8f1_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31da5b85ed46b23b09a25429cdddf898fcaec8f1_2_1380x738.jpeg 2x" data-dominant-color="91A290"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Isodose_Slicer</span><span class="informations">1920×1028 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/423949c62aa04f393cc82421f1c655250e35f409.png" data-download-href="/uploads/short-url/9rQfEgcpXW1iJ1a0HV65TiujSVr.png?dl=1" title="Isodose_Slicer_Instruction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/423949c62aa04f393cc82421f1c655250e35f409_2_665x500.png" alt="Isodose_Slicer_Instruction" data-base62-sha1="9rQfEgcpXW1iJ1a0HV65TiujSVr" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/423949c62aa04f393cc82421f1c655250e35f409_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/423949c62aa04f393cc82421f1c655250e35f409_2_997x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/423949c62aa04f393cc82421f1c655250e35f409_2_1330x1000.png 2x" data-dominant-color="E2CECE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Isodose_Slicer_Instruction</span><span class="informations">1412×1061 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you give me some help? Thank you so much!</p>

---

## Post #2 by @lassoan (2021-10-13 04:31 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is there a reason why the color table entries are editable only if “Relative isolevels of dose” option is enabled in Isodose module?</p>

---

## Post #3 by @Cody_Xie (2021-10-13 07:03 UTC)

<p>Hi Andrass, thank you co much for your reply! And yes, that’s exactly the problem I have. The color table is only editable if “Relative isolevels of dose” option is checked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/651982637c810a78efd0dee47f168a6f538b847b.jpeg" data-download-href="/uploads/short-url/eqmSr2VOhGmw3Vh0oC5kUGJERuj.jpeg?dl=1" title="Isodose_" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/651982637c810a78efd0dee47f168a6f538b847b_2_690x369.jpeg" alt="Isodose_" data-base62-sha1="eqmSr2VOhGmw3Vh0oC5kUGJERuj" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/651982637c810a78efd0dee47f168a6f538b847b_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/651982637c810a78efd0dee47f168a6f538b847b_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/651982637c810a78efd0dee47f168a6f538b847b_2_1380x738.jpeg 2x" data-dominant-color="9F99AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Isodose_</span><span class="informations">1920×1028 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> I appreciate any help from your side!</p>

---

## Post #4 by @Mik (2021-10-13 07:23 UTC)

<p>I think the problem is not only in “Isodose” module. You can’t modify that color table in the “Colors” module as well. “Isodose_ColorTable_Relative” can be edited, but “Isodose_ColorTable_Default” is blocked for editing.</p>

---

## Post #5 by @Mik (2021-10-13 08:56 UTC)

<p><a class="mention" href="/u/cody_xie">@Cody_Xie</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>The problem in that part of <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx#L98-L107" rel="noopener nofollow ugc">code</a>.</p>
<p>Logic loads default  (absolute dose) color table, and creates relative dose color table, if both color table are created without loading, both absolute and relative doses are available for editing.</p>
<p>Possible solution</p>
<pre><code class="lang-auto">//---------------------------------------------------------------------------
void vtkSlicerIsodoseModuleLogic::SetMRMLSceneInternal(vtkMRMLScene* newScene)
{
  vtkNew&lt;vtkIntArray&gt; events;
  events-&gt;InsertNextValue(vtkMRMLScene::NodeAddedEvent);
  events-&gt;InsertNextValue(vtkMRMLScene::NodeRemovedEvent);
  events-&gt;InsertNextValue(vtkMRMLScene::EndCloseEvent);
  events-&gt;InsertNextValue(vtkMRMLScene::EndBatchProcessEvent);
  this-&gt;SetAndObserveMRMLSceneEvents(newScene, events.GetPointer());

    // Create isodose color tables
    vtkSlicerIsodoseModuleLogic::CreateDefaultDoseColorTable(newScene);
    vtkSlicerIsodoseModuleLogic::CreateRelativeDoseColorTable(newScene);
}
</code></pre>

---

## Post #6 by @Cody_Xie (2021-10-13 10:29 UTC)

<p>Hi Mik,</p>
<p>many thanks for pointing it out!</p>
<p>Besides, may I know if you have the similar problem when you create isodose surfaces? The dose will be enlarged after clicking “Create isodose surfaces”. I posted a new topic here <a href="https://discourse.slicer.org/t/dose-will-be-distorted-when-creating-isodose-surfaces/20129" class="inline-onebox">Dose will be distorted when creating isodose surfaces</a></p>
<p>Thank you so much!</p>

---

## Post #7 by @cpinter (2021-10-13 10:55 UTC)

<p>Good catch <a class="mention" href="/u/mik">@Mik</a> ! This issue with color tables that they are not editable sometimes has been around for a good while, but I wasn’t aware that it affected one of the isodose color tables. If it’s not easy to make it editable then a workaround could be added that creates a new editable one and copies the colors from the loaded one.</p>

---

## Post #8 by @Mik (2021-10-13 11:24 UTC)

<p>I will try to look at that bug.</p>

---

## Post #10 by @Cody_Xie (2021-10-13 11:30 UTC)

<p>Thank yo so much Mik! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #11 by @Cody_Xie (2021-10-20 12:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> Hello Andras and Csaba, may I know why I cannot download and install the Preview Release Slicer (built by 2021-10-20)? The size of the .zip file looks wrong. Thank you so much!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d44115045fa521bb97ea87c194e692b061d3141.png" data-download-href="/uploads/short-url/b1wBai7ruWgEbAsN7CDeBnSiGuB.png?dl=1" title="Slicer_Properties" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d44115045fa521bb97ea87c194e692b061d3141.png" alt="Slicer_Properties" data-base62-sha1="b1wBai7ruWgEbAsN7CDeBnSiGuB" width="385" height="500" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Properties</span><span class="informations">484×628 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73accb6b53f855b3bbd485848fe62989f46d78cb.png" data-download-href="/uploads/short-url/gvj7qESMrTRtIi6nO0scVcchK0r.png?dl=1" title="Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73accb6b53f855b3bbd485848fe62989f46d78cb.png" alt="Error" data-base62-sha1="gvj7qESMrTRtIi6nO0scVcchK0r" width="690" height="383" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error</span><span class="informations">790×439 8.15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2021-10-20 14:42 UTC)

<p>There was a download server failure yesterday - see here for details and workaround: <a href="https://discourse.slicer.org/t/slicer-preview-release-package-for-windows-failed-to-upload/20264" class="inline-onebox">Slicer Preview Release package for Windows failed to upload</a></p>

---

## Post #13 by @Cody_Xie (2021-10-20 17:52 UTC)

<p>Thank you so much Andras! It works fine now</p>

---
