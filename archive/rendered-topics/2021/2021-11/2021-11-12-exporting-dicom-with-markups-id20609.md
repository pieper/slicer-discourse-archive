---
topic_id: 20609
title: "Exporting Dicom With Markups"
date: 2021-11-12
url: https://discourse.slicer.org/t/20609
---

# Exporting DICOM with Markups

**Topic ID**: 20609
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/exporting-dicom-with-markups/20609

---

## Post #1 by @neuralnet (2021-11-12 23:23 UTC)

<p>Hi all,</p>
<p>I have a volume that I have marked up with several fiducial points that are clinically useful. I hope to export this back out to DICOM, including the markups (ideally these markups would be visible even in another DICOM viewer).</p>
<p>Is this possible? I know it’s not ideal, but it would be helpful to clinicians with DICOM viewers but not 3D slicer installed.</p>

---

## Post #2 by @lassoan (2021-11-13 17:16 UTC)

<p>What DICOM viewers do you use? What kind of annotations it can display: DICOM segmentation objects, structured reports (with what templates), just secondary captures (screenshots), …? What kind of findings would you like to store?</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/pieper">@pieper</a> As far as I remember you have implemented some fiducial saving/loading for QICCR. What exactly are supported now? What annotations does the OHIF viewer support now? We should at least add reading and writing of those annotations in Slicer, too.</p>

---

## Post #3 by @pieper (2021-11-13 17:27 UTC)

<p>Currently Slicer can read the line annotations we made for <a href="https://www.crowds-cure.org/">Crowds Cure</a> from the SR files <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=33948774">in TCIA</a>.  <a class="mention" href="/u/fedorov">@fedorov</a> and I have been talking about expanding read/write support both in Slicer and OHIF but haven’t got a concrete timeline in mind.  I don’t recall that we ever did fiducials.</p>
<p>For <a class="mention" href="/u/neuralnet">@neuralnet</a>’s question, I think adding SC export from the Screen Capture module would be the most widely compatible solution.  The DICOM Scene Export makes an SC and puts the MRB in a private tag, but it would be possible to modify this and just export the SC, possibly with multiple frames.</p>

---

## Post #4 by @fedorov (2021-11-13 17:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="20609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I think adding SC export from the Screen Capture module would be the most widely compatible solution</p>
</blockquote>
</aside>
<p>I agree this is the most practical and reliable solution to make sure the result can be visualized with a broad range of DICOM viewers. But I am also wondering if longer term we could come up with a solution that exports such markup into a structured report that could reference that SC series, so that we could maybe achieve both semantically rich, machine-readable standard compatible representation in SR with the lowest denominator SC to support visualization. Maybe <a class="mention" href="/u/david_clunie">@David_Clunie</a> has thoughts if that would be the ideal solution?</p>

---

## Post #5 by @lassoan (2021-11-14 20:39 UTC)

<p>I would assume that you can save image data in the Pixel Data element of the stuctured report information object that all DICOM viewer could show, even those that don’t know anything about structures reports.</p>
<p>Are there any example DICOM files containing annotations created by OHIF viewer? If we had those then it would be quite easy to implement the same in Slicer.</p>
<p>Are there any online OHIF viewer demos that can create and import annotations?</p>

---

## Post #6 by @pieper (2021-11-14 21:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="20609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are there any online OHIF viewer demos that can create and import annotations?</p>
</blockquote>
</aside>
<p><a href="https://github.com/dcmjs-org/dcmjs">This dcmjs demo</a> should work at least for length measurements.</p>
<p><a href="https://dcmjs.netlify.app/cornerstonedicomsr/" class="onebox" target="_blank" rel="noopener">https://dcmjs.netlify.app/cornerstonedicomsr/</a></p>
<p>The SRs should be like the ones from crowds-cure in TCIA, but maybe they are different a bit.  Unfortunately without also loading the referenced image the SR won’t load correctly in the current QR extension.</p>
<p>This demo is not OHIF proper but it’s the basis for what’s going into OHIF.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="20609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would assume that you can save image data in the Pixel Data element of the stuctured report information object that all DICOM viewer could show, even those that don’t know anything about structures reports.</p>
</blockquote>
</aside>
<p>This might work but it would be non-standard.  None of the SR types include the Image Pixel or Image Plane modules; I believe it’s legal to add them but I suspect anything that reads reports wouldn’t expect to find them.  SC with burned in numbers  (e.g. bitmaps) is the least common denominator in terms of likely wide compatibility.  A multiframe SC has been around long enough and is generated often enough that most viewers support it.</p>
<p>So basically yes, all this needs work and since there are so few clinical systems that use these standards there hasn’t been a big push or pull to get things working well.  Also the DICOM standard focuses on <em>planar</em> annotations (and even getting those correct is complex), which is a vanishingly small subset of our typical Markups use cases.  SEG is proving much more valuable in general.  Still, we do intend to do measurement SRs for IDC at some point.</p>

---

## Post #7 by @neuralnet (2021-11-14 22:19 UTC)

<p>Hi Dr. Lasso,</p>
<p>Thank you so much for your response. Our current DICOM viewer is the hosptial PACS viewer Philips ISite. I believe that it can display the following formats: XML/REC, PAR/REC, DICOM (classic and enhanced), NifTI (1, 2 and FSL). I am not sure if it can display screenshots that are not in DICOM format, but it would be lovely if I could convert the screenshots into DICOM format, which could be pushed to our PACS server. Would it be possible to get screenshots from transverse, sagittal, and coronal planes to save as one volume that could be represented in a DICOM files? Apologies if my understanding is rudimentary.</p>
<p>Thank you all for your guidance!</p>

---

## Post #8 by @neuralnet (2021-11-14 22:22 UTC)

<p>Hi Dr. Lasso,</p>
<p>I would love to implement this solution, saving the markers as Pixel Data. Is there any way you could direct me towards a resource to learn this? Thank you so much</p>

---

## Post #9 by @neuralnet (2021-11-14 22:24 UTC)

<p>Hi Dr. <a class="mention" href="/u/pieper">@pieper</a> and Dr. <a class="mention" href="/u/fedorov">@fedorov</a> ,</p>
<p>Thank you so much for all of your help with this and your suggestions for future tools. I cannot tell you how lucky the medical and research communities are to have such a team working on this powerful, free software. We appreciate you!</p>

---

## Post #10 by @neuralnet (2021-11-14 22:28 UTC)

<p>The findings we would like to represent are points within the volume that represent electrode locations. For example, I’d like to mark the electrode locations from a post-op CT onto the pre-op MRI (already achieving this with coregistration followed by markup), but would also like to export this information as a “volume” so that clinicians can view a copy of the pre-op MRI with this additional information in our PACS viewer. Thank you!</p>

---

## Post #11 by @lassoan (2021-11-16 03:43 UTC)

<p>If you want to go beyond viewing 2D screenshots then you need to check what DICOM information objects your iSite viewer can display. This should be specified in the DICOM conformance statement of the software. I did a quick search and only found this page, which lists software software released 5-15 years ago: <a href="https://www.philips.ca/healthcare/resources/support-documentation/ihe-pacs-systemsandwebviewing" class="inline-onebox">Philips Healthcare | IHE - PACS Systems and Web Viewing</a></p>
<p>What Philips iSite version do you use? What is the exact name and version of the viewer application?</p>

---
