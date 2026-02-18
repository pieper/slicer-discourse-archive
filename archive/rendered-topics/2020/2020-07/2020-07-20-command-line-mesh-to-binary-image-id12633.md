# Command Line - Mesh to binary image

**Topic ID**: 12633
**Date**: 2020-07-20
**URL**: https://discourse.slicer.org/t/command-line-mesh-to-binary-image/12633

---

## Post #1 by @Kevin_Eddinger (2020-07-20 02:04 UTC)

<p>Hi everyone,</p>
<p>I have a .OBJ mesh that I would like to convert into a binary segmentation DICOM or NIFTI image. The easiest way for me to do it now is to drag the model into Slicer and change the dropdown from ‘model’ to ‘segmentation.’ This produces a nearly perfect result that I can then export.</p>
<p>Is there a way to recreate this functionality from the command line to automate the process?</p>
<p>Thanks<br>
Kevin</p>

---

## Post #2 by @lassoan (2020-07-20 02:16 UTC)

<p>You can find examples for all the commonly needed operations in the script repository:</p>
<ul>
<li>read node from file (replace <code>readVolume</code> by <code>readSegmentation</code>): <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file</a>
</li>
<li>export to labelmap and save to file: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node</a>
</li>
</ul>

---

## Post #3 by @ptsii (2021-07-31 16:44 UTC)

<p>Can you elaborate on how this is done?  I can successfully drag my .obj mesh into Slicer, and I see it rendered in one of 4 windows on the right side of the Slicer window, but I don’t see any dropdown that say “segmentation”…  I see “segmentations”, but then what?</p>

---

## Post #4 by @lassoan (2021-07-31 22:10 UTC)

<p>The dropdown menu where you can choose to load the .obj file as segmentation is in the “Description” column the “Add data” window (the window that appears when you drag-and-drop a file to the Slicer application window).</p>

---

## Post #5 by @ptsii (2021-07-31 23:09 UTC)

<p>OK, I can see the object in the upper right slicer window - I believe this is where I was before.  How does one save this selected object out now as a 3D volume in .nii format?</p>

---

## Post #6 by @lassoan (2021-07-31 23:13 UTC)

<aside class="quote no-group" data-username="ptsii" data-post="5" data-topic="12633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/848f3c/48.png" class="avatar"> ptsii:</div>
<blockquote>
<p>How does one save this selected object out now as a 3D volume in .nii format?</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">Segmentations module documentation</a> on how to export a segmentation into labelmap volume file.</p>
<p>Note that usage of NIFTI file format is strongly discouraged, because it has many issues. Only use it for storing brain images, because for those images compatibility the BIDS ecosystem outweighs the disadvantages of using such a problematic file format.</p>

---

## Post #7 by @ptsii (2021-07-31 23:36 UTC)

<p>Beautiful - thanks for pointing me in the right direction!</p>
<p>Most of my work involves neuro-imaging tools, hence my interest in NIFTI.  What are the limitations of NIFTI from your perspective, out of curiosity?</p>

---

## Post #8 by @pieper (2021-08-01 14:04 UTC)

<aside class="quote no-group" data-username="ptsii" data-post="7" data-topic="12633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/848f3c/48.png" class="avatar"> ptsii:</div>
<blockquote>
<p>What are the limitations of NIFTI from your perspective, out of curiosity?</p>
</blockquote>
</aside>
<p>Search for nifti on this forum and you’ll find lots of examples of interoperability problems due to unclear assumptions about the use of qform/sform by various packages, no definitive standard for the meaning of 4D data, and other issues.  Nifti was a big improvement over the img/hdr conventions that used to be common in neuroimaging but it’s disappointing that left/right flip questions still come up on neuroimaging forums after all these years.</p>
<p><a href="https://discourse.slicer.org/search?q=nifti%20flip">https://discourse.slicer.org/search?q=nifti%20flip</a></p>

---

## Post #9 by @ptsii (2021-08-01 15:10 UTC)

<p>Thanks!  I have enough to do already without searching a forum for NIFTI issues, so thanks for summarizing.  I’ve run into the L/R-flipped issue with .img/.hdr before, but not with NIFTI. The packages I use must interpret L/R in the same way: I have a gold-standard image which I use in my processing pipelines to check for this. So its good to know it can still be an issue.</p>

---

## Post #10 by @ptsii (2021-08-01 15:43 UTC)

<p>In case it is useful to others in the future, here is a recipe:</p>
<ol>
<li>
<p>Translate mesh into .obj format<br>
To use Slicer for the transformation, you need to have the mesh in .obj format. You can use Meshlab to translate some other common mesh formats (e.g., .ply) Load the file into Meshlab, and then “Export mesh as…” from File menu, and choose “Alias Wavefront Object (*.obj)” as the file type.</p>
</li>
<li>
<p>Use Slicer to transform mesh to volume</p>
</li>
</ol>
<ul>
<li>start the Slicer app</li>
<li>drag the mesh file and drop it into the Slicer main window (a sub-window will open titled: “Add data into the scene”)</li>
<li>in the “Add data into the scene” window, select “segmentation” from the dropdown menu in the Description portion (far right), then select “OK”. The object should show up in the upper right Slicer sub-window.</li>
<li>choose “Segmentations” from the Modules dropdown menu. This will change the options in the left-most part of the Slicer window (under the 3D Slicer icon)</li>
<li>in the “Representations” section (one of the new set of options that appeared as part of “Segmentations”), select “create” in the “Binary labelmap” line</li>
<li>in the “Export to files” section (also part of “Segmentations”, but below the “Representations” subsection), select the following:</li>
<li>NIFTI under the “File format” dropdown menu
<ul>
<li>choose the “Destination folder” for the exported .nii file</li>
<li>optional: select a reference volume that you want to save this new object into (e.g., that has the voxel size etc. that you prefer). If you don’t choose anything here, then it defaults to the size of the object (which you’ll need to pad later - easy to do)</li>
<li>choose “Export”. This should create an .nii file in the “Destination folder”, with the same basic name as the mesh .obj file you started with. This should be loadable in, e.g., ITKSNAP where you can check if it did the right thing.</li>
</ul>
</li>
</ul>
<ol start="3">
<li>The resulting image space will be exactly the size of the maximal dimensions of the mesh object. This can be a problem if you want to register images with certain other software packages.  You can pad this image using ImageMath (part of ANTS tools) or the iMath function in the ANTsR package in R</li>
</ol>

---
