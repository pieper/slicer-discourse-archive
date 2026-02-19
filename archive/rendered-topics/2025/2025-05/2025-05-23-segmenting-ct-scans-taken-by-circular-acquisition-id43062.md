---
topic_id: 43062
title: "Segmenting Ct Scans Taken By Circular Acquisition"
date: 2025-05-23
url: https://discourse.slicer.org/t/43062
---

# Segmenting CT scans taken by circular acquisition

**Topic ID**: 43062
**Date**: 2025-05-23
**URL**: https://discourse.slicer.org/t/segmenting-ct-scans-taken-by-circular-acquisition/43062

---

## Post #1 by @sldamico131 (2025-05-23 11:11 UTC)

<p>Operating system: mac OS Sequoia<br>
Slicer version: 5.8.1<br>
I am trying to segment the ossicles in a seal skull. The CT scans were taken I believe using circular acquisition. When I load them into slicer, there are no slices. Instead, in the axial plane, I can just rotate the skull, and in the sagittal plane, the scans are mirrored. In the coronal plane is just a strange spiral. I can visualize the ossicles in the scans in the axial plane, but any attempt to segment them just leads to a large circle. Is there a way that I can segment these properly?</p>

---

## Post #2 by @muratmaga (2025-05-23 15:04 UTC)

<p>Those are not the cross-sections, but the shadow image acquired at the detector. You will need the reconstructed cross-section images. Please read this to get familiar with CT</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/microCT/README.md#what-is-microct-imaging">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/microCT/README.md#what-is-microct-imaging" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/microCT/README.md#what-is-microct-imaging" target="_blank" rel="noopener nofollow ugc">microCT/README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/main/microCT/README.md#what-is-microct-imaging" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md"># What is microCT imaging? 

MicroCT imaging, short for micro-computed tomography, is a technique that uses X-rays to create detailed 3D images of objects. It works by taking many 2D X-ray images, called projection images, of an object from different angles and then combining them using a process called reconstruction to form a 3D virtual histology of the object. This method is non-destructive, meaning the object being scanned remains intact. 
## Comparison to Medical Imaging
MicroCT imaging is similar to medical CT (computed tomography) scans used in hospitals, but there are some significant differences. Both use X-rays and reconstruction to create 3D images. 
The term "microCT" does not originate from its frequent use in scanning small objects, but rather from the difference in the beam diameter, which is also referred to as the "spot size", and resolution range compared to medical CT (computed tomography). In microCT, the X-ray beam and detector are optimized to achieve extremely high resolutions, often in the micrometer (µm) range, which is why "micro" is part of the name. This capability enables microCT to reveal incredibly fine details in scanned objects.

In contrast, medical CT uses a larger spot size and broader X-ray beam to image larger objects, such as human organs or entire body sections. Medical CT is designed for speed and efficiency when scanning large volumes, prioritizing to reduce the harm to the patient due to the effects of ionizing radition on cellular structure over ultra-fine resolution. The typical resolution in medical CT is in the millimeter range—sufficient for diagnosing conditions like tumors or fractures but unable to capture the microscopic features that microCT excels at revealing.

The smaller beam diameter or spot size in microCT systems provides the ability to focus on tiny details, making it ideal for research applications like analyzing bone microstructure, studying the internal anatomy of small organisms, or examining the porosity of materials. However, the trade-off is that microCT has a much smaller field of view, longer scan times, and may not be suitable for imaging larger specimens efficiently. Medical CT scans are used for diagnosing diseases in humans, while microCT is often used in research, engineering, and studying biological specimens.

## Projection (Shadow) Images
Shadow, or projection, images in microCT imaging are the 2D X-ray images that are captured during the scanning process. They are formed when an X-ray beam passes through the object being scanned and creates a pattern of varying intensities on the detector. These patterns resemble shadows because they display the silhouette and internal structure of the object, depending on how much the X-rays are absorbed—or attenuated—by different parts of the material.

 &lt;figure&gt;
  &lt;img src="./projection.png" alt="projection images"&gt;
  &lt;figcaption&gt;&lt;b&gt;Fig.1 X-ray projection images vs Cross-sectional images.&lt;/b&gt; Three images on the left are examples of projection image taken by the scanner at various angles during the scanning. These projection images are then mathematically reconstructed into cross-sectional images shown on the right (hence the name tomography). It is these cross-sectional images that we can go through in program like 3D Slicer and visualize as a virtual 3D object.   &lt;/figcaption&gt;
&lt;/figure&gt; 


</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/microCT/README.md#what-is-microct-imaging" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
