---
topic_id: 32783
title: "Large Data Set Not Enough Memory Slicer Crashes"
date: 2023-11-13
url: https://discourse.slicer.org/t/32783
---

# Large data set, not enough memory, Slicer crashes

**Topic ID**: 32783
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/large-data-set-not-enough-memory-slicer-crashes/32783

---

## Post #1 by @Susan_Marriott (2023-11-13 17:50 UTC)

<p>Operating system: MacOS<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior: crashes<br>
I have data sets of 3000+ images derived from CT scans of rocks containing trace fossils.  I am trying to find out what the architecture of the trace fossils is inside the rocks. Slicer crashes before I get very far.  I presume this is because of the size of the data set.  Is there any way round this?</p>

---

## Post #2 by @pieper (2023-11-13 18:33 UTC)

<p>Probably the easiest is to rent a virtual machine with lots of memory.  Any of the cloud computing vendors can provide such machines by the hour.  I don’t think you would want to shrink the data or you would lose detail.</p>

---

## Post #3 by @lassoan (2023-11-13 21:42 UTC)

<p>If you want to ensure that you don’t run out of memory then I would recommend to have 10x more memory space than the size of your data set. If your image is 3000 slices, each slice 2048x2048, 16 bits per voxel then the data size is about 25GB, so you would want 250GB memory space if you want to work with your entire data at full resolution. If all this memory is RAM then it may be expensive, if it is just disk space then it is very slow.</p>
<p>Renting a big virtual machine by the hour is a viable option.</p>
<p>However, often the region of interest is significantly smaller than the entire image. Even if the region is 1/3 the size along each axis, it would mean a size reduction of 27x, which means that you reduced your data size to 1GB, which a machine with even as low as 16GB RAM could handle.</p>
<p>You can use Image Stacks module (in SlicerMorph extension) to load the image at low resolution, specify the region of interest, and load only that part at full resolution.</p>

---

## Post #4 by @muratmaga (2023-11-14 06:04 UTC)

<p>ImageStacks is perfect for this task. Load your dataset in preview resolution. Set various ROIs for your trace fossils, and then import only those ROIs as separate subvolumes at full resolution. See the tutorial here:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener">//github.com/SlicerMorph/Tutorials/tree/main/ImageStacks</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @pieper (2023-11-14 13:36 UTC)

<p>One thing to note is that if your source data is in dicom then often the Slicer dicom module is requred for sorting.  ImageStacks relies on the filenames to sort, which may be okay but it depends on your data.</p>

---

## Post #6 by @Susan_Marriott (2023-11-15 17:20 UTC)

<p>Thanks for the reply and the link to the tutorial.  I’ll see if I can use ImageStacks sa you suggest. Otherwise I might have to rent some time on a virtual machine.</p>

---
