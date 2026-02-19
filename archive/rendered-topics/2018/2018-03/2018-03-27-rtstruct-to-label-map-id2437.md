---
topic_id: 2437
title: "Rtstruct To Label Map"
date: 2018-03-27
url: https://discourse.slicer.org/t/2437
---

# RTstruct to Label map

**Topic ID**: 2437
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/rtstruct-to-label-map/2437

---

## Post #1 by @alain (2018-03-27 12:34 UTC)

<p>Hi,</p>
<p>I have 200 dicom datapoints that contain a image and a RTstruct for the segmentations. I need to convert all RTstructs to Label volumes (maps) and can do this with the segmentations module. However, I have to perform every step manually and I am thus looking for a way to do it batch-wise. Since the segmentations module does not have a CLI, I was wondering if there is another solution that would allow me to access the module without the GUI.</p>
<p>Best regards,<br>
Alain</p>

---

## Post #2 by @cpinter (2018-03-27 14:38 UTC)

<p>This batch processing script does exactly what you want</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">SlicerRT/BatchProcessing at master · SlicerRt/SlicerRT</a></h3>

  <p><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">master/BatchProcessing</a></p>

  <p><span class="label1">Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>See readme file for details.</p>

---
