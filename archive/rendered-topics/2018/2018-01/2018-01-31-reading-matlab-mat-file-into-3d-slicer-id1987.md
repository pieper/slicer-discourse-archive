# Reading Matlab mat file into 3D Slicer

**Topic ID**: 1987
**Date**: 2018-01-31
**URL**: https://discourse.slicer.org/t/reading-matlab-mat-file-into-3d-slicer/1987

---

## Post #1 by @marasov (2018-01-31 15:51 UTC)

<p>Hello!<br>
I made several X-ray images of a metal ball of different density from different angles.<br>
Then I applied CBCT reconstruction to them and got a *.mat file.<br>
<a href="https://www.mathworks.com/matlabcentral/fileexchange/35548-3d-cone-beam-ct--cbct--projection-backprojection-fdk--iterative-reconstruction-matlab-examples" rel="nofollow noopener">3D Cone beam CT (CBCT) projection backprojection FDK, iterative reconstruction Matlab examples</a><br>
How can I transfer the received data to a 3D Slicer to render the object and get a 3D model?<br>
Thank you all in advance!</p>

---

## Post #2 by @lassoan (2018-01-31 16:13 UTC)

<p>Probably the easiest is to save the reconstructed image as a standard NRRD image file.</p>
<p>There is a Matlab writer for NRRD image files here:</p>
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

<p>If you want to run Matlab code directly from Slicer, then you can use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension</a>.</p>

---

## Post #3 by @alireza (2018-08-09 19:39 UTC)

<p>Thank you Andras,<br>
Is it possible to give pixel spacing information too? Where should I put that information?</p>

---

## Post #4 by @lassoan (2018-08-09 22:15 UTC)

<p><code>img.ijkToLpsTransform</code> transform specifies IJK voxel coordinates to LPS anatomical coordinates transform. Pixel spacing is the norm of the columns of the top-left 3x3 submatrix. If volume is axis-aligned then spacing values are in the diagonal of the top-left 3x3 submatrix.</p>

---

## Post #5 by @Chicago_Girl (2022-04-23 23:54 UTC)

<p>I have a 2D matrix and I wanna make it to nrrd but this function doesnt work.<br>
The reason that I want to change it to nrrd is I want enforce the module that I’ve written on Slicer on this matrix.</p>

---

## Post #6 by @lassoan (2022-04-24 03:51 UTC)

<p>I’ve just tested the <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrwrite.m script</a> and it works perfectly for 2D images. For example:</p>
<pre data-code-wrap="matlab"><code class="lang-matlab">a=eye(30)
img.pixelData=a
nrrdwrite("c:/tmp/test.nrrd", img)
</code></pre>
<p>Creates an image like this:</p>
<pre data-code-wrap="txt"><code class="lang-txt">NRRD0005
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: double
space: left-posterior-superior
dimension: 3 
sizes: 30  30   1
space directions: (1,0,0) (0,1,0) (0,0,1)
kinds: domain domain domain
endian: little
encoding: raw
...
</code></pre>
<p>It gets loaded into Slicer correctly:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/649a7e3eb8d05f3be6d1a6feeeff2633c5a7e44f.png" alt="image" data-base62-sha1="elYKjMdx2UcogUUgSw30JDajvPh" width="661" height="460"></p>
<p>Note that others may have created scripts called <code>nrrdwrite.m</code> and <code>nrrdread.m</code> and those scripts may or may not work correctly. Make sure you use the scripts that we developed and made available <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/">in the Slicer Matlab Bridge repository</a>.</p>

---
