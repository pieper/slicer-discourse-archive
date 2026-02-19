---
topic_id: 2050
title: "Nrrdwrite M Of 2D Image"
date: 2018-02-07
url: https://discourse.slicer.org/t/2050
---

# Nrrdwrite.m of 2d image

**Topic ID**: 2050
**Date**: 2018-02-07
**URL**: https://discourse.slicer.org/t/nrrdwrite-m-of-2d-image/2050

---

## Post #1 by @gcsharp (2018-02-07 20:47 UTC)

<p>Hi, I’m trying to use nrrdwrite.m to create nrrds, but it doesn’t work on 2D images.  Does anyone know if/how in Octave I can convert these to 3D images with one voxel in the 3rd dimension?</p>
<p>Alternatively, I can submit a patch to nrrdwrite, if such an interpretation is desirable.</p>

---

## Post #2 by @pieper (2018-02-07 21:03 UTC)

<p>I think they will need to be one slice 3d nrrd files.</p>

---

## Post #3 by @lassoan (2018-02-07 21:59 UTC)

<p>I’ve updated this nrrdwrite function to be able to save 2D image (as single-slice 3D volume):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" target="_blank" rel="nofollow noopener">PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m</a></h4>
<pre><code class="lang-m">function nrrdwrite(outputFilename, img)
% Write image and metadata to a NRRD file (see http://teem.sourceforge.net/nrrd/format.html)
%   img.pixelData: pixel data array
%   img.ijkToLpsTransform: pixel (IJK) to physical (LPS, assuming 'space' is 'left-posterior-superior')
%     coordinate system transformation, the origin of the IJK coordinate system is (1,1,1) to match Matlab matrix indexing
%   img.metaData: Contains all the descriptive information in the image header. The following fields are ignored:
%     sizes: computed to match size of img.pixelData
%     type: computed to match type of img.pixelData
%     kinds: computed to match dimension of img.pixelData
%     dimension: computed to match dimension of img.pixelData
%     space_directions: ignored if img.ijkToLpsTransform is defined
%     space_origin: ignored if img.ijkToLpsTransform is defined
%   img.metaData: Contains the list of full NRRD field names for each
%     metaData field name. All fields should be listed here that have a
%     special character in their name (such as dot or space).
%   img.metaDataFieldNames: Contains full names of metadata fields that cannot be used as Matlab field names because they contains
%     special characters (space, dot, etc). Full field names are used for determining the field name to be used in the NRRD file
%     from the Matlab metadata field name.
%
% Supports writing of 3D and 4D volumes.
</code></pre>

  This file has been truncated. <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @gcsharp (2018-02-07 22:57 UTC)

<p>Works great.  Thanks!</p>
<p>I suggest a tiny little change: line 76 would benefit from a semi-colon!</p>

---

## Post #5 by @lassoan (2018-02-10 20:13 UTC)

<p>Thank you, I’ve fixed it.</p>

---
