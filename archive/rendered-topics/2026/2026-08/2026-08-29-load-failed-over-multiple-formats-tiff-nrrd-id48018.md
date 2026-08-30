---
topic_id: 48018
title: "Load Failed over multiple formats (TIFF, NRRD)"
date: 2026-08-29
url: https://discourse.slicer.org/t/48018
last_bumped: 2026-08-30T05:30:07.350Z
---

# Load Failed over multiple formats (TIFF, NRRD)

**Topic ID**: 48018
**Date**: 2026-08-29
**URL**: https://discourse.slicer.org/t/load-failed-over-multiple-formats-tiff-nrrd/48018

---

## Post #1 by @asims (2026-08-29 23:45 UTC)

<p>Hi</p>
<p>I have an image stack to load which was provided to me as a series of TIFF files. These can be successfully opened in 3rd party tools such as ImageJ (Fiji) and GIMP. However there is a warning message about the description field:</p>
<blockquote>
<p>ASCII value for tag “ImageDescription” does not end in null byte</p>
</blockquote>
<p>In Slicer the tiff files could be opened as individual slices but not an image volume stack.</p>
<p>I tried exporting to NRRD from ImageJ.</p>
<p>Slicer would not load this NRRD file. The error messages are below. My next steps are to try to load the sequence.</p>
<p><code>Exception from vtkITK MegaMacro:</code><br>
<code>Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7f9c3d0) returned failure for request: vtkInformation (0x8a21af0)</code><br>
<code>vtkMRMLStorageNode::ReadData: Failed to read node images (vtkMRMLMultiVolumeNode1) from filename='&lt;path&gt;/images.nrrd'</code><br>
<code>vtkMRMLStorageNode::ReadData: Failed to read node images (vtkMRMLDiffusionWeightedVolumeNode1) from filename='&lt;path&gt;/images.nrrd'</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file '&lt;path&gt;/images.nrrd' failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of '&lt;path&gt;/images.nrrd' (first filename: '&lt;path&gt;/images.nrrd')</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file '&lt;path&gt;/images.nrrd' failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of '&lt;path&gt;/images.nrrd' (first filename: '&lt;path&gt;/images.nrrd')</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read '&lt;path&gt;/images.nrrd' file as a volume of type 'DiffusionTensorVolume'. Details: FileFormatError.</code><br>
<code>vtkMRMLStorageNode::ReadData: Failed to read node images (vtkMRMLDiffusionTensorVolumeNode1) from filename='&lt;path&gt;/images.nrrd'</code><br>
<code>ReadData: MRMLVolumeNode does not match file kind</code><br>
<code>vtkMRMLStorageNode::ReadData: Failed to read node images (vtkMRMLVectorVolumeNode1) from filename='&lt;path&gt;/images.nrrd'</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader</code><br>
<code>vtkMRMLStorageNode::ReadData: Failed to read node images (vtkMRMLVectorVolumeNode2) from filename='&lt;path&gt;/images.nrrd'</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file '&lt;path&gt;/images.nrrd' failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of '&lt;path&gt;/images.nrrd' (first filename: '&lt;path&gt;/images.nrrd')</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file '&lt;path&gt;/images.nrrd' failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of '&lt;path&gt;/images.nrrd' (first filename: '&lt;path&gt;/images.nrrd')</code><br>
<code>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read '&lt;path&gt;/images.nrrd' file as a volume of type 'Volume'. Details: FileFormatError.</code><br>
<code>vtkMRMLStorageNode::ReadData: Failed to read node images (vtkMRMLScalarVolumeNode1) from filename='&lt;path&gt;/images.nrrd'</code><br>
<code>static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection*) Errors occurred while loading nodes: "Error: Loading &lt;path&gt;/images.nrrd -  load failed.\n"</code></p>

---

## Post #2 by @muratmaga (2026-08-29 23:59 UTC)

<p>You didn’t tell us what kind of images these are and the data types (RGB, float etc) they contain. Also why are you trying to read the as sequence? If the images are sequentially ordered with suffixex (0001, 0002, so forth), all you have to do is to uncheck “Single File” option and read them as one file belonging to the same volume. Better yet, install the SlicerMorph extension and use the <code>ImageStacks</code> module in it to try to read the data.</p>
<p>I suspect fiji exported NRRD failed because it was saved in a data type slicer doesn’t expect or accept.</p>

---

## Post #3 by @asims (2026-08-30 00:08 UTC)

<p>I have since found out a little more. The NRRD image is approx 20GB. I am running on a system with over 60GB. On a previous read attempt, error messages regarding memory appeared. In this case other hanging processes from image conversion had used up the memory. With those processes terminated, Slicer successfully loads the file into memory but takes a long time about it.</p>
<p>This discussion can be closed. Seems like there might have been some issue with the TIFF volume not matching format. Conversion to NRRD has worked.</p>
<p>I think the dataset can probably be reduced. Bit depth if nothing else.</p>
<p>I came across the discussion here in 2024 that was helpful.</p>
<aside class="quote quote-modified" data-post="2" data-topic="38362">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/bad-performance-when-segmenting-11gb-micro-ct/38362/2">Bad performance when segmenting 11GB micro-CT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square "><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    There are many ways to improve the performance. But first you have to understand the memory usage during segmentation. If your volume is 11GB in size, during the segmentation (depending on the effect), Slicer may use 6-10 times more (so 60-100GB) transiently. That’s already at the limit of available memory on your computer. Adding another segment or five will increase even further. So while your computer is fairly powerful, your dataset is also quite big. 
There are many ways to deal with that. …
  </blockquote>
</aside>


---

## Post #4 by @asims (2026-08-30 00:33 UTC)

<p>Thank you for the reply.</p>
<p>For completeness to answer you questions, this is from a Micro CT:</p>
<ol>
<li>Image type 16bit unsigned integer grayscale</li>
<li>Images are sequentially ordered but not starting at zero. Single file was unchecked.</li>
<li>I did try SlicerMorph ImageStacks which allowed me to load as a preview, but not at higher resolution levels - now trying it again after clearing out the memory has worked. It maxed out the memory after reading all the files, but did work.</li>
</ol>
<p>I think the data can probably be safely downsampled a bit, both resolution and depth.</p>
<p>The TIFF read through the SlicerMorph module also returned the same warning about the ImageDescription not ending in a null byte.</p>
<p>Thanks again for the reply.</p>

---

## Post #5 by @muratmaga (2026-08-30 05:30 UTC)

<p>20GB imagestack is fairly big. You can use the various functionalities (such as downsampling or simply importing a specific region of the data at full resolution) with <code>ImageStacks</code>. If you are new to it, here is the tutorial for its functionality:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">Tutorials/ImageStacks at main · SlicerMorph/Tutorials</a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">main/ImageStacks</a></p>

  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
