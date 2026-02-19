---
topic_id: 24593
title: "How To Save In Mat Format"
date: 2022-08-01
url: https://discourse.slicer.org/t/24593
---

# How to save in .mat format

**Topic ID**: 24593
**Date**: 2022-08-01
**URL**: https://discourse.slicer.org/t/how-to-save-in-mat-format/24593

---

## Post #1 by @akmal871026 (2022-08-01 16:16 UTC)

<p>Dear all,</p>
<p>Does anyone know how to save labeling images in slicer?</p>
<p>Let’s say labeled a tumor in the liver. then I want to save it in a logical/categorical data set (.mat)</p>
<p>because currently just have .nrrd format, then it cannot be open in matlab.</p>

---

## Post #2 by @pieper (2022-08-01 17:03 UTC)

<p>I don’t use matlab myself but I understand there is code available to open nrrd files in matlab.  It should be pretty trivial.</p>

---

## Post #3 by @lassoan (2022-08-02 10:19 UTC)

<p>You can use this Matlab nrrd reader to read segmentations (.seg.nrrd files) saved by Slicer:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m" target="_blank" rel="noopener">PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m</a></h4>


      <pre><code class="lang-m">function img = nrrdread(filename)
% Read image and metadata from a NRRD file (see http://teem.sourceforge.net/nrrd/format.html)
%   img = cli_imageread(filename) reads the image volume and associated metadata
%
%   img.pixelData: pixel data array
%   img.ijkToLpsTransform: pixel (IJK) to physical (LPS, assuming 'space' is 'left-posterior-superior')
%     coordinate system transformation, the origin of the IJK coordinate system is (1,1,1) to match Matlab matrix indexing
%   img.metaData: contains all the descriptive information in the image header
%   img.metaDataFieldNames: Contains full names of metadata fields that cannot be used as Matlab field names because they contains
%     special characters (space, dot, etc). Special characters in field names are replaced by underscore by default when the NRRD
%     file is read. Full field names are used when writing the image to NRRD file.
%
%  Supports reading of 3D and 4D volumes.
%
%   Current limitations/caveats:
%   * Block datatype is not supported.
%   * Only tested with "gzip" and "raw" file encodings.
%
% Partly based on the nrrdread.m function with copyright 2012 The MathWorks, Inc.

</code></pre>



  This file has been truncated. <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
