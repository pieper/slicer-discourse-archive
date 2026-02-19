---
topic_id: 34559
title: "Reslice The Volume With Plane Positioned By Several Referenc"
date: 2024-02-27
url: https://discourse.slicer.org/t/34559
---

# Reslice the volume with plane positioned by several reference points

**Topic ID**: 34559
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/reslice-the-volume-with-plane-positioned-by-several-reference-points/34559

---

## Post #1 by @UH_Cho (2024-02-27 03:58 UTC)

<p>Is it possible to set several reference points on the volume to form a specific plane, use that plane to reorient the volume, and then reslice and export the result?</p>
<p>I am an orthodontist researching the cranio-maxillofacial area.</p>
<p>I am planning to conduct a study using CT volume data. Due to the nature of orthodontic analysis, it is necessary to reorient the volume based on a specific 2D plane composed of several fiducial points (landmarks).</p>
<p>Depending on the case, two planes may be used as a reference. For example, a specific plane composed of several landmarks is reoriented parallel to the horizontal plane, and then sequentially reoriented so that a specific landmark matches the midsagittal plane.</p>
<p>After the reorientation process, for subsequent work, it is necessary to transform the volume itself according to the plane, reslice it, and export it.</p>
<p>Several commercial programs developed for orthodontic analysis support the functions mentioned above, but unfortunately, they do not support the function to export the work content to a more universal file format. Moreover, it seems that there is no program that can reslice the reoriented volume. Therefore, it is impossible to conduct analysis and research in conjunction with other software.</p>
<p>I would like to inquire if such work is possible using 3D Slicer.</p>

---

## Post #2 by @pieper (2024-02-27 19:53 UTC)

<p>I don’t know if there’s anything quite like that now, but it could be added with some python scripting if it’s not there already in one of these modules:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/DCBIA-OrthoLab">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/DCBIA-OrthoLab" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <img width="280" height="280" src="https://avatars.githubusercontent.com/u/11340280?s=280&amp;v=4" class="thumbnail onebox-avatar">

<h3><a href="https://github.com/DCBIA-OrthoLab" target="_blank" rel="noopener">DCBIA-OrthoLab</a></h3>

  <p>Dental and Craniofacial Bionetwork for Image Analysis (DCBIA) - DCBIA-OrthoLab</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2024-02-28 05:02 UTC)

<p>You can position a markup plane by placing multiple markup points (Markups module → Plane settings → “Three points” or “Plane fit”). You can then get the transformation  from the markup plane and create a transform from it (this requires a few lines of Python code). Finally, you can apply the transform to a ROI markup and use <code>Crop volume</code> module with this ROI to resample the volume.</p>
<p>What you describe also sounds vey similar to the <a href="https://slicer.readthedocs.io/en/5.0/user_guide/modules/acpctransform.html">ACPC transform module</a>.Maybe you could slightly modify that module to do what you need.</p>

---

## Post #5 by @UH_Cho (2024-03-06 08:25 UTC)

<p>Thank you for your prompt reply. I appreciate your assistance.</p>
<p>I will need to investigate whether such functionality exists in the module. However, do you happen to know of any Python scripts that can perform such a function?</p>

---

## Post #6 by @UH_Cho (2024-03-06 08:32 UTC)

<p>Thank you for your support. I appreciate your assistance.</p>
<p>As you suggested, I was able to successfully make the specified plane using  the markup module.  but I am still unsure how to proceed at this stage. I am seeking guidance on how to best implement the desired functionality.</p>
<p>Could you please advise me on which Python code I could utilize to achieve this goal? I would be grateful for any recommendations on relevant Python libraries or modules that could facilitate this process.</p>
<p>I am eager to learn and progress in this area, and any guidance you can provide would be immensely helpful. Thank you in advance for your time and consideration.</p>

---
