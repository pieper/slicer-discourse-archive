---
topic_id: 44765
title: "Probe Volume With Model Question"
date: 2025-10-14
url: https://discourse.slicer.org/t/44765
---

# Probe Volume with Model Question

**Topic ID**: 44765
**Date**: 2025-10-14
**URL**: https://discourse.slicer.org/t/probe-volume-with-model-question/44765

---

## Post #1 by @aceegreene (2025-10-14 21:33 UTC)

<p>Hi everyone - I am struggling to understand what the probe volume with model module in Slicer does. When probing a model with a volume that has scalar values assigned to its entire volume, are the values ultimately seen on the model surface a representation of just the corresponding voxels that intersect with the volume at those positions or does it also take into account values on the interior of the volume i.e. beneath the surface as well when estimating what to show on the surface of the model?</p>
<p>I am not a coder so didn’t really understand what the source code does so thought I’d ask here. Thank you!</p>

---

## Post #2 by @pieper (2025-10-14 21:48 UTC)

<p>It just looks up the pixel value at the location that corresponds with the location of each vertex of the model.  You can then manipulate the view of that information with the scalars feature of the Models module.</p>

---

## Post #3 by @aceegreene (2025-10-14 23:59 UTC)

<p>Thank you! I have a follow up question. I am trying to map T2* values from an MRI onto a model I created from a segmentation but if the module only generates surface values, then I am not sure of what utility that would be as I want data even from inside the volume. Is there a way to generate that?</p>
<p>As an aside, how are only surface values useful in other cases when using probe volume with model? I assumed you would need the volume’s internal data as well. Apologies if these are naive questions.</p>

---

## Post #4 by @pieper (2025-10-15 13:50 UTC)

<p>I’m not sure what you are trying to accomplish, but if you want a continuum mesh, you can use the SegmentMesher extension and then when you probe you will get the internal vertices too.</p>
<p>The module can be used for something like sampling an fMRI map on the surface of a subcortical structure or similar.</p>

---

## Post #5 by @aceegreene (2025-10-15 15:40 UTC)

<p>Thank you for that suggestion! I just tried using that extension with Cleaver but it unfortunately does not fully capture the details of my segmentation. Tetgen gives me an error saying command returns non-zero status.</p>
<p>I am working with a meniscus segmentation so need it to be fully replicated. Is that not possible with this tool? And is there an alternate way of completing this task after which I could import the file back as a solid model in Slicer to probe it with the volume?</p>
<p>Thanks!</p>

---

## Post #6 by @pieper (2025-10-15 16:12 UTC)

<p>yes, cleaver and tetgen often don’t behave well.  I tend to write python code to generate meshes using vtk which works well but there’s nothing packaged up for use.</p>
<p>There’s some experimental code here:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/pieper/SlicerSOFA/tree/main/Experiments">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/pieper/SlicerSOFA/tree/main/Experiments" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/pieper/SlicerSOFA/tree/main/Experiments" target="_blank" rel="noopener">SlicerSOFA/Experiments at main · pieper/SlicerSOFA</a></h3>


  <p><span class="label1">3D Slicer extension to enable simulations using the SOFA framework - pieper/SlicerSOFA</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @aceegreene (2025-10-15 17:05 UTC)

<p>Thank you for sharing this! Unfortunately I have no experience with coding. Is there something in the experimental codes that I could plug and play into Slicer’s python console to generate the mesh? Or any other way I could generate it (even if outside of Slicer)?</p>

---

## Post #8 by @pieper (2025-10-15 17:48 UTC)

<p>Meshing is a big complex topic, but gmsh is popular and you can easily move data back and forth once you get the hang of it.</p>

---

## Post #9 by @aceegreene (2025-10-15 22:03 UTC)

<p>Got it, I’ll try that. Thank you for your help!</p>

---

## Post #10 by @aceegreene (2025-10-20 13:57 UTC)

<p>Hi pieper. I was able to generate an accurate volumetric mesh from gmsh, thank you!</p>
<p>My ultimate goal is to 3d print this but it seems like there is no way to convert the volumetric vtk file to a volumetric printable format. Am I missing something or is there any other way to do this? Like using the volume directly to convert it to a printable format or something?</p>

---

## Post #11 by @pieper (2025-10-20 14:16 UTC)

<p>It depends on what your printer supports.  Mostly people use stl files for this, but they only provide surface structure.  More modern printers can accept bitmaps and the <a href="https://github.com/SlicerFab/SlicerFab">SlicerFab</a> extension can help with that, but it’s still not a common process so that extension is not really maintained.  I’m not sure it’s currently working.</p>

---

## Post #12 by @aceegreene (2025-10-20 15:20 UTC)

<p>I think the printer can support voxel level printing, I just can’t find a way to convert my volumetric mesh in 3D Slicer to a printable format that would contain internal scalar values. Do you know if any graphics or CAD softwares could do the conversion?</p>

---

## Post #13 by @pieper (2025-10-20 15:53 UTC)

<p>No, I don’t know of anything off the shelf that can do that.  But everything you need is in Slicer if you just do some scripting something like what is done in SlicerFab.</p>

---

## Post #14 by @aceegreene (2025-10-20 15:57 UTC)

<p>Got it, thanks so much!</p>

---
