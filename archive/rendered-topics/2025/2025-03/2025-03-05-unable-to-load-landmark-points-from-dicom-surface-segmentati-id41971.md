---
topic_id: 41971
title: "Unable To Load Landmark Points From Dicom Surface Segmentati"
date: 2025-03-05
url: https://discourse.slicer.org/t/41971
---

# Unable to load landmark points from DICOM Surface Segmentation created by BrainLab Origin

**Topic ID**: 41971
**Date**: 2025-03-05
**URL**: https://discourse.slicer.org/t/unable-to-load-landmark-points-from-dicom-surface-segmentation-created-by-brainlab-origin/41971

---

## Post #1 by @Arber_Demi (2025-03-05 10:55 UTC)

<p>Hello everyone,</p>
<p>I’m trying to load some DICOM segmentation file, similar to <a href="https://discourse.slicer.org/t/unable-to-load-dicom-segmentation-file/15134">“Unable to load DICOM segmentation file”</a>. I am running into the same issue of not being able to load these files. The files do have reference images that I also have, with the correct UID references, but it makes no difference with loading. (I assume it would only matter for their positioning in any case)</p>
<p>However my problem seems to be one option mentioned by issakomi, where the SEG here has SOPClassUID = 1.2.840.10008.5.1.4.1.1.66.5</p>
<p>Is there any update since that topic that allows me to load these files without trying to fiddle with extra scripts? I already tried using the script that issakomi linked at the time, however I did not have any success. The actual data here is a couple of registration points coming from a registration pointer tracked by a Brainlab Curve system.</p>

---

## Post #2 by @pieper (2025-03-05 13:52 UTC)

<p>You can try with the latest Slicer release and if you still have issues it would be good for you to post data (but don’t post PHI) publicly together with exact descriptions of the software used to generate the files.</p>

---

## Post #3 by @Arber_Demi (2025-03-05 15:28 UTC)

<p>I tried with both 5.8.1 and the 5.9 preview, both have the same result as with 5.8 (doesn’t work). I have posted an edited version of the DICOM file <a href="https://drive.google.com/drive/folders/1BfOTYf9K9HUQezGOMoxq6ELp_nXllnob?usp=sharing" rel="noopener nofollow ugc">here</a>. I hope just one of them is enough (there are 7 points) to figure out how to make them load. If anything is wrong with the data I posted please let me know.</p>
<p>I have replaced possible remnants of sensitive data with “Assume this is correct” and other sample answers.</p>
<p>The data is obtained from the Brainlab Origin Software, I don’t really have the exact version of it but I will post when I get find out, although I think the data inside the DICOM might have some information about the version.</p>

---

## Post #4 by @pieper (2025-03-05 22:03 UTC)

<p>Okay, thanks for sharing that file.  This is a SurfaceSegmentationStorage, which has historically been very rare (I wrote a prototype reader 9 years ago and the topic has only come up once or twice since then, for example in the thread linked below.</p>
<p>It would be great if someone wants to dig this up again and make sure it works with the latest Slicer with some sharable data.</p>
<aside class="quote" data-post="1" data-topic="1125">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/df705f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-dicom-surface-segmentation-objects/1125">Load DICOM Surface Segmentation Objects</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Slicer version: 4.6.2 
Hi, 
I just wondered, if there is any possibility to load DICOM Surface Segmentation Objects, as described in the DICOM Supplement 132 with the 3D Slicer. 
Thank you in advance! <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13" title="slight_smile" alt="slight_smile" class="emoji"> 
Best regards 
Julia
  </blockquote>
</aside>


---

## Post #5 by @issakomi (2025-03-06 09:39 UTC)

<p>I have the <a href="https://gist.github.com/issakomi/29e48917e77201f2b73bfa5fe7b30451" rel="noopener nofollow ugc">script</a> to load SEG mesh, but it works with triangle meshes, <em>Triangle Point Index List</em> (deprecated) or <em>Long Triangle Point Index List</em> should be available. In your file it is empty, there is <em>Vertex Point Index List</em> (deprecated, <em>Long Vertex Point Index List</em> should be used). I think it is not a mesh, but a set of points (one point in your file), it is easy to read the points, but not yet sure how visualize.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6407c0701a2a01f08485ee69818903fc0b3515ba.png" data-download-href="/uploads/short-url/egUm0EnIf2ULgz686zHQsmrPed4.png?dl=1" title="s" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6407c0701a2a01f08485ee69818903fc0b3515ba_2_690x433.png" alt="s" data-base62-sha1="egUm0EnIf2ULgz686zHQsmrPed4" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6407c0701a2a01f08485ee69818903fc0b3515ba_2_690x433.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6407c0701a2a01f08485ee69818903fc0b3515ba.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6407c0701a2a01f08485ee69818903fc0b3515ba.png 2x" data-dominant-color="5C6168"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s</span><span class="informations">913×574 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @issakomi (2025-03-06 14:37 UTC)

<p>I have tried to modify the script to work with your data, s. <a href="https://gist.github.com/issakomi/93eaf61e928dfd82caa10c39a4a85ac9" rel="noopener nofollow ugc">here</a>. Probably the points could be visualized much better, also not sure about the file, but your can check. I have modified the file to have 5 points, with one point it is difficult to test. (Caution with LPS/RAS space, s. option in the script)</p>
<div class="youtube-onebox lazy-video-container" data-video-id="uthXeph6gJY" data-video-title="Test DICOM SEG with POINT representation" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=uthXeph6gJY" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/uthXeph6gJY/maxresdefault.jpg" title="Test DICOM SEG with POINT representation" width="690" height="388">
  </a>
</div>


---

## Post #7 by @Arber_Demi (2025-03-07 07:17 UTC)

<p>Thanks a lot for the work :]. I tried editting the script you posted before, but didn’t have much success myself, hopefully I understand it better now. I’ll test myself next week to see how I can implement it such that I can load the points into Slicer directly.</p>
<p>The actual data is 7 separate files, with 1 point each. My main goal is to just easily load the positions of the points in world coordinates, as afterwards I can change the visualization to Markup.</p>

---

## Post #8 by @lassoan (2025-03-07 13:09 UTC)

<p>Storing a single point in a <code>SurfaceSegmentationStorage</code> is a very unusual choice. Segmentation is intended to store 3D shapes, hence the name “Surface…” (a single point is not a surface). The much more common <code>SegmentationStorage</code> representation stores 3D shapes, too.</p>
<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> is this kind of use of surface segmentation valid or we should ask the vendor to stop exporting data objects like this and stick to the usual measurements storage instead (Structured Report with TID 1500)?</p>

---

## Post #9 by @David_Clunie (2025-03-07 13:41 UTC)

<p>If the single points are registration landmark points (fiducials), there is a specific IOD for that, the <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.40.html" rel="noopener nofollow ugc">Spatial Fiducials IOD</a>, which defines fiducials in either 3D (frame of reference relative) or 2D (image pixel data relative) space. Fiducials do not have to be points, but they can be - see <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.21.2.html#sect_C.21.2.1.1" rel="noopener nofollow ugc">Shape Type</a>.</p>
<p>I would not recommend using SR or the surface segmentation objects for this.</p>

---

## Post #10 by @lassoan (2025-03-09 21:38 UTC)

<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> thanks a lot for your response, it is very useful!</p>
<p><a class="mention" href="/u/arber_demi">@Arber_Demi</a></p>
<p>Please contact BrainLab engineers and clarify this: Did they really save registration landmark positions in a Surface Segmentation IOD? What was their rationale? What would be a timeline for the fix?</p>
<p>If it turns out that this is indeed an inappropriate use of Surface Segmentation IOD then I would rather not make Slicer legitimize it (and waste time with implementing some temporary solution that later need to be replaced). But of course if your project cannot afford to wait for correct solution then you can go and add a very simple Python scripted DICOM plugin that recognizes these odd DICOM objects and creates markups from them. You would implement something like <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py">the structured report plugin</a> but much simpler, because you would just need to read a single point per instance (you would not need to ready many markups and you would not need to be able to read a proper Surface Segmentation IOD). If you implement this then you can submit it to a related extension, such as <a href="https://github.com/SlicerIGT/SlicerIGT">SlicerIGT</a> to make it easily available without adding a new Slicer extension.</p>

---

## Post #11 by @Arber_Demi (2025-03-10 15:46 UTC)

<p>I will contact someone at Brainlab today, hopefully will get some response before end of the week.</p>
<p>I plan to make a quick reader this week to load the data I am working with, however after that I will look into making that an addition for SlicerIGT. Will update as soon as I have something new, thanks again for all the help.</p>

---

## Post #12 by @Arber_Demi (2025-03-11 09:32 UTC)

<p>This does indeed work just fine. After having a proper look at what was going on in the code, I realised that I really just missunderstood where the data for the points was being extracted from in the DICOM file. The DICOM viewer only shows the X value (no Y or Z), however through the code I can see that Y and Z are also in the <code>PointCoordinatesData</code> attribute. At the moment I am just loading the coordinates through that, and adding the points into a <code>MarkupFiducial</code>. Thank you again for the script <a class="mention" href="/u/issakomi">@issakomi</a> .</p>
<p>If I get a response from Brainlab about the issue, I will post an update here, however for now I will continue using this, and in the weekend try to find where in <code>SlicerIGT</code> I can add a code snippet to handle this specific DICOM file edge case. Thank you all for the help :].</p>

---
