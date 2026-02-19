---
topic_id: 45082
title: "Validation Request Visceral Fascia Segmentation From Ct Scan"
date: 2025-11-14
url: https://discourse.slicer.org/t/45082
---

# Validation Request: Visceral Fascia Segmentation from CT Scans 

**Topic ID**: 45082
**Date**: 2025-11-14
**URL**: https://discourse.slicer.org/t/validation-request-visceral-fascia-segmentation-from-ct-scans/45082

---

## Post #1 by @Charles_Chyna (2025-11-14 15:50 UTC)

<h2><a name="p-129867-greetings-everyone-1" class="anchor" href="#p-129867-greetings-everyone-1" aria-label="Heading link"></a>Greetings everyone,</h2>
<p>Before moving forward with a larger dataset, I would greatly appreciate expert feedback on my approach to the automated pipeline I’m developing for visceral fascia segmentation from abdominal CT scans.</p>
<p>Background: The visceral fascia, which is the fascial border enclosing internal organs and visceral fat in the abdominal cavity, needs to be automatically recognized and segmented. The objective is accurate (Dice &gt;0.75) and quick (&lt;2 min per patient) segmentation for clinical research.</p>
<p>Present Methodology: After segmenting the CT scan into different tissue types (skeletal muscle, visceral fat/organs, subcutaneous fat, and background), my pipeline extracts the visceral fascia boundary in the manner described below:</p>
<p>Separate the organ/visceral fat area (Label 3).<br>
To slightly reduce the area, use binary erosion with two iterations.<br>
Deduct the original mask from the eroded one: Visceral_region - eroded_region = fascia_boundary</p>
<p>This creates a thin boundary layer around the internal organs</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a530082b1f52e753566f87618712d8b24e26ec0e.jpeg" data-download-href="/uploads/short-url/nzjGOkqKbWfrCDERGvuDaBOkXCe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a530082b1f52e753566f87618712d8b24e26ec0e.jpeg" alt="image" data-base62-sha1="nzjGOkqKbWfrCDERGvuDaBOkXCe" width="690" height="388"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">690×388 61.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Analysis Objectives:</strong></p>
<p>The main goal is to analyze fascial volume and morphology in a population of young adults by automatically extracting and quantifying the visceral fascia boundary from abdominal CT scans.</p>
<p>Particular Data to Be Extracted:</p>
<p>Each patient’s visceral fascia boundary volume (cm³).<br>
Measurements of the thickness and surface area of the face.<br>
Fascia’s spatial distribution surrounding particular organ areas.<br>
Variability in fascial anatomy between patients.</p>
<p>Final Outcome:<br>
A fully automated, validated pipeline that produces CT scans with clinically acceptable accuracy (Dice &gt;0.75) in less than two minutes per patient</p>
<p>Visceral fascia 3D segmentation masks<br>
Quantitative measurements (surface area, volume)<br>
Visual depictions (2D slices, 3D surface renderings)</p>
<p><strong>Expert Questions:</strong></p>
<ul>
<li>
<p>Anatomical correctness: Is this definition of “visceral fascia” suitable for studies involving medical imaging? Is there another fascial layer I should be focusing on?</p>
</li>
<li>
<p>Methodology: Would edge detection algorithms (Sobel, Canny) or morphological gradient operators be better suited for boundary extraction, or is binary erosion (2 iterations) a better option?</p>
</li>
<li>
<p>Validation criteria: For fascia segmentation, what Dice coefficient threshold is deemed clinically acceptable? Should I be looking at any other metrics?</p>
</li>
<li>
<p>Clinical relevance: Should I be aware of any published literature references or established medical imaging standards for automated fascia segmentation?</p>
</li>
</ul>
<p><strong>Challenges:</strong></p>
<p>What I’ve attempted:<br>
used binary erosion (2 iterations) for boundary extraction after testing several fascia definitions (subcutaneous, deep, and visceral) and deciding on visceral fascia. successfully represented with accurate anatomical proportions in 3D Slicer.</p>
<p>What Prevents Advancement:</p>
<p>Anatomical uncertainty: Expert confirmation is required to determine whether the visceral fat boundary accurately depicts “visceral fascia” in a clinical setting.<br>
Data problems: only one patient processes successfully, while 19/20 patients fail with DICOM orientation errors.<br>
Lack of validation metrics: No ground truth for calculating the dice coefficient; unclear of acceptable alternatives<br>
Methodology question: Should I use different algorithms or is binary erosion the standard for medical fascia extraction?</p>

---

## Post #2 by @mikebind (2025-11-14 21:16 UTC)

<aside class="quote no-group" data-username="Charles_Chyna" data-post="1" data-topic="45082">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/charles_chyna/48/81431_2.png" class="avatar"> Charles_Chyna:</div>
<blockquote>
<p>Measurements of the thickness</p>
</blockquote>
</aside>
<p>Your methodology basically sets the thickness you will see, your fascia segment will be two voxels thick everywhere, because that is how you constructed it. I can’t weigh in on other aspects of your proposed methods since I don’t know much about fascia, but you definitely can’t learn anything about how thick the fascia layer is using the proposed methods.   Likewise, the volume of fascia is also not really something you are able to measure in this way; you will essentially be calculating the surface area of the organ/visceral fat segment and multiplying that times 2 voxels thick.  The surface area is something you are reasonably measuring, though, and might be of interest. You don’t need the fascia segment to calculate that though, you can just measure the surface area of the organ/visceral fat segment.  Also, note that medical imaging often has voxels are spaced differently in one direction than in another, so if you just use simple binary erosion, you will be taking different sized bites in different directions, and your fascia layer will be thicker in the directions where voxel spacing is thicker.  That’s definitely undesirable, so you should first resample the image to ensure isotropic voxel spacing so that “2-voxels thick” is the same thickness in each direction.</p>
<p>To validate your method, you will need some sort of ground truth to compare to, via Dice or any other method.  It’s hard to get around that if you want to be in any way quantitative. This usually involves creating (or finding elsewhere if you are very very lucky) a dataset of painstakingly manually created labeled data.</p>
<p>For your DICOM loading problems, you will need to solve those first.  People load CTs from DICOM into Slicer all the time without any issue, so it is not a capability problem on the Slicer side. Typically, loading issues arise from invalid DICOM headers, perhaps from an overzealous anonymization step?  I would suggest opening a separate question describing your loading problems and any error message information you see.  Try loading these images outside of your processing pipeline to see if the issue is perhaps in your loading code or in the images themselves.</p>

---
