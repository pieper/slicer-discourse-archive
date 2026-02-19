---
topic_id: 14573
title: "Exporting Matlab Data For Gel Dosimetry"
date: 2020-11-12
url: https://discourse.slicer.org/t/14573
---

# Exporting MATLAB data for gel dosimetry

**Topic ID**: 14573
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/exporting-matlab-data-for-gel-dosimetry/14573

---

## Post #1 by @SmHoop (2020-11-12 19:11 UTC)

<p>Hi there,</p>
<p>I am running an in-house MATLAB program to reconstruct optical CT files. The only options this program has to save the reconstructions are “save as type: All MATLAB files” or “export cube” which generates a .raw file. I am trying to use the Gel Dosimetry slicelet and the tutorial calls for a .VFF file (and the slicelet itself says “Load optical CT files from VFF, NRRD, etc.”. I have everything else for the slicelet to run (Normal CT image, struct, planned dose from Eclipse, etc.) but I am struggling with how to possibly import my actual reconstructed, irradiated scan.</p>
<p>Does anyone out there have experience with this?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-11-12 19:12 UTC)

<p>You can save the image matrix in Matlab as a nrrd file, for example using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m</a>.</p>

---

## Post #3 by @SmHoop (2020-11-12 19:31 UTC)

<p>Thank you for the response!</p>
<p>I’m not sure how to utilize this function however. The .mat file that is saved is a 1x1 struct . I tried to set the “img” argument equal to this struct (in the workspace) but I got an error of “Reference to non-existent field ‘pixelData’.” My Matlab knowledge is extremely slim and this is all new territory for me, am I even using this function correctly?</p>

---

## Post #4 by @lassoan (2020-11-12 20:37 UTC)

<p>Usage instructions are described in great details in the function’s documentation:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m#L2-L49">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m#L2-L49" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m#L2-L49" target="_blank" rel="noopener">PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m#L2-L49</a></h4>



    <pre class="onebox"><code class="lang-m">
      <ol class="start lines" start="2" style="counter-reset: li-counter 1 ;">
          <li>% Write image and metadata to a NRRD file (see http://teem.sourceforge.net/nrrd/format.html)
</li>
          <li>%   img.pixelData: pixel data array
</li>
          <li>%   img.ijkToLpsTransform: pixel (IJK) to physical (LPS, assuming 'space' is 'left-posterior-superior')
</li>
          <li>%     coordinate system transformation, the origin of the IJK coordinate system is (1,1,1) to match Matlab matrix indexing
</li>
          <li>%   img.metaData: Contains all the descriptive information in the image header. The following fields are ignored:
</li>
          <li>%     sizes: computed to match size of img.pixelData
</li>
          <li>%     type: computed to match type of img.pixelData
</li>
          <li>%     kinds: computed to match dimension of img.pixelData
</li>
          <li>%     dimension: computed to match dimension of img.pixelData
</li>
          <li>%     space_directions: ignored if img.ijkToLpsTransform is defined
</li>
          <li>%     space_origin: ignored if img.ijkToLpsTransform is defined
</li>
          <li>%   img.metaData: Contains the list of full NRRD field names for each
</li>
          <li>%     metaData field name. All fields should be listed here that have a
</li>
          <li>%     special character in their name (such as dot or space).
</li>
          <li>%   img.metaDataFieldNames: Contains full names of metadata fields that cannot be used as Matlab field names because they contains
</li>
          <li>%     special characters (space, dot, etc). Full field names are used for determining the field name to be used in the NRRD file
</li>
          <li>%     from the Matlab metadata field name.
</li>
          <li>%
</li>
          <li>% Supports writing of 3D and 4D volumes.
</li>
          <li>% 2D pixelData is written as single-slice 3D volume.
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m#L2-L49" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="SmHoop" data-post="3" data-topic="14573">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f6c823/48.png" class="avatar"> SmHoop:</div>
<blockquote>
<p>My Matlab knowledge is extremely slim and this is all new territory for me</p>
</blockquote>
</aside>
<p>Matlab is on a steep decline. Instead of investing time into learning it, you might consider using existing sophisticated image reconstruction solutions implemented in C++ and available in Python, for example <a href="https://www.openrtk.org/">RTK</a> (Python package: <a href="https://pypi.org/project/itk-rtk/">itk-rtk</a>).</p>

---

## Post #5 by @SmHoop (2020-12-14 18:40 UTC)

<p>Hello,</p>
<p>I’ve tried to make this work with what I can export using this custom GUI built in Matlab (basically a 3D matrix, .mat file) but I’ve had no success. Instead, I’ve written the .mat out to a dicom and am attempting to use this as the measured/calibration data in the gel dosimetry slicelet. It seems to be working so far, is there any reason a non dicom should be used?</p>
<p>Thank you!</p>

---
