---
topic_id: 39792
title: "Struggling With Multi Phase Dce Mri Segmentation Issues With"
date: 2024-10-22
url: https://discourse.slicer.org/t/39792
---

# Struggling with Multi-Phase DCE-MRI Segmentation: Issues with 3D Slicer Viewing and DICOM Reconstruction

**Topic ID**: 39792
**Date**: 2024-10-22
**URL**: https://discourse.slicer.org/t/struggling-with-multi-phase-dce-mri-segmentation-issues-with-3d-slicer-viewing-and-dicom-reconstruction/39792

---

## Post #1 by @Luo_Dr (2024-10-22 08:20 UTC)

<p><strong>Issue Summary:</strong></p>
<p>I’m working with a dynamic contrast-enhanced abdominal MRI dataset, with 320 slices divided into 4 phases (non-contrast, arterial, portal venous, delayed). The goal is to separate these phases and generate corresponding DICOM files that can be correctly loaded and viewed in 3D Slicer.</p>
<h3><a name="p-118595-problem-1" class="anchor" href="#p-118595-problem-1" aria-label="Heading link"></a>Problem:</h3>
<ol>
<li><strong>DICOM Files Segmentation</strong>: The original file has all 4 phases combined, and I need to split them into individual phases, each containing 80 slices.</li>
<li><strong>DICOM Viewer Issues</strong>: After splitting the phases, the resulting DICOM files can be opened, but they do not behave as expected:</li>
</ol>
<ul>
<li><strong>Inconsistent Browsing</strong>: In viewers like MicroDICOM, scrolling through slices is not smooth, and slices have to be clicked manually.</li>
<li><strong>3D Slicer Errors</strong>: While importing into 3D Slicer, the following warning appears:<br>
3.“Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly.”*Moreover, the reconstructed files seem to contain slices from multiple phases.</li>
</ul>
<h3><a name="p-118595-methods-attempted-2" class="anchor" href="#p-118595-methods-attempted-2" aria-label="Heading link"></a>Methods Attempted:</h3>
<ol>
<li><strong>Original Dataset Processing</strong>: We extracted pixel data from the DICOM file and attempted to split the phases based on temporal indices using Python (<code>pydicom</code>). We ensured proper metadata such as <code>SeriesInstanceUID</code>, <code>SliceThickness</code>, <code>SpacingBetweenSlices</code>, <code>PixelRepresentation</code>, <code>BitsAllocated</code>, etc., are copied or set correctly.</li>
<li><strong>File Reconstruction</strong>: The pixel data was successfully split into the four phases, but the reconstructed files had problems:</li>
</ol>
<ul>
<li>Incorrect browsing behavior in DICOM viewers.</li>
<li>In 3D Slicer, the loading was problematic, and slices were not displayed correctly.</li>
</ul>
<ol start="3">
<li><strong>Pixel Data Metadata</strong>: Ensured that the pixel data metadata (<code>BitsAllocated: 16</code>, <code>BitsStored: 12</code>, <code>High Bit: 11</code>, and <code>PixelRepresentation: 0</code>) matched the original DICOM file.</li>
</ol>
<p>Despite these efforts, 3D Slicer still throws the geometry-related warning and does not display the images correctly.</p>
<h3><a name="p-118595-request-for-help-3" class="anchor" href="#p-118595-request-for-help-3" aria-label="Heading link"></a>Request for Help:</h3>
<p>I am looking for guidance on:</p>
<ol>
<li>Correctly splitting multi-phase DICOM files for smooth scrolling in viewers like 3D Slicer.</li>
<li>Fixing metadata or geometry issues that may be causing the error in 3D Slicer.</li>
</ol>

---

## Post #2 by @Luo_Dr (2024-10-22 08:49 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1QO9pDjhhnVIQvzbJeO0Lu2HVlO_5e3de/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1QO9pDjhhnVIQvzbJeO0Lu2HVlO_5e3de/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1QO9pDjhhnVIQvzbJeO0Lu2HVlO_5e3de/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1QO9pDjhhnVIQvzbJeO0Lu2HVlO_5e3de/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">1.0_anon.dcm</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @pieper (2024-12-04 21:48 UTC)

<p>Hi.-</p>
<p>Thanks for sharing this data.  Unfortunately it’s not a format that we typically see and I don’t know of any tools that will automatically recognize the sequence of volumes.  Also there are lots of Philips private tags, so some of the key metadata needed to understand the acquisition may be hard to extract or may need to be filled in from out-of-band sources (i.e. not from the header).</p>
<p>That said, probably with a little python scripting you could extract the frames into reasonable volumes.  You would want to look at the <code>DimensionOrganizationSequence</code> and then the <code>SharedFunctionalGroupsSequence</code> and <code>PerFrameFunctionalGroupsSequence</code> to get the correct image geometry and timing information.</p>

---
