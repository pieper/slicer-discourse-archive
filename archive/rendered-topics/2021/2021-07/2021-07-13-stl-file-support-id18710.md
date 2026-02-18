# STL file support

**Topic ID**: 18710
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/stl-file-support/18710

---

## Post #1 by @landerson (2021-07-13 21:05 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11<br>
Expected behavior: Load STL file as a 3D model<br>
Actual behavior: No 3D model was produced. The STL file does not seem to be corrupted (I am able to open it on Meshlab)</p>

---

## Post #2 by @lassoan (2021-07-13 21:08 UTC)

<p>The 3D view’s field of view is centered to the origin by default. If you load a model file and you don’t see it then click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">“Center 3D view” button</a>. If you still not see the model then you may need to zoom using right-click-and-drag (or by hitting the <code>r</code> key).</p>

---

## Post #3 by @landerson (2021-07-13 21:10 UTC)

<p>The model doesn’t show up at all, I’ve tried centering it in addition to zooming in/out</p>

---

## Post #4 by @lassoan (2021-07-14 01:26 UTC)

<p>Can you upload the misbehaving STL file somewhere and post the link here?</p>

---

## Post #5 by @landerson (2021-07-14 14:32 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1OVaU15JeERrAGhAkjbadyaN4O0t41UJT/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1OVaU15JeERrAGhAkjbadyaN4O0t41UJT/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1OVaU15JeERrAGhAkjbadyaN4O0t41UJT/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1OVaU15JeERrAGhAkjbadyaN4O0t41UJT/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Segmentation_Segment_1.stl</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here is the link. I also talked to a co-worker and they suggested that there might be a path error since I moved the files around.</p>

---

## Post #6 by @lassoan (2021-07-14 21:08 UTC)

<p>When you saved this file, you have set size scaling factor to 0.005. It means that the diameter of your model is now 0.04mm. You need to do a lot of zooming in to see it. In recent Slicer Preview Releases we automatically zoom the view to fit the first loaded model, so you won’t have trouble finding it.</p>
<p>Scaling feature was added to segmentation export so that at the very end of all your processing you can write a surface mesh file that uses a different distance unit (for example, some software use meter as coordinate system unit). But if you intend to use these files in Slicer then keep scaling factor at 1.0.</p>

---

## Post #7 by @landerson (2021-07-14 21:31 UTC)

<p>Ok, is there a way to retroactively do that in the STL file or would I need to change the scale size from the MRML file</p>

---

## Post #8 by @lassoan (2021-07-14 21:44 UTC)

<p>You can load the STL file and scale it back to its original size using Surface toolbox.</p>
<p>But in general the best is to save the segmentation in its native format (usually .seg.nrrd, because you create them from images). If you need a surface mesh then you can just load the segmentation file and store it in any format you need. STL is not good for storing segmentations, because conversion to editable (binary labelmap) representation is a lossy operation and there are many other inconveniences (you need a separate file for each segment, there is no standard way of specifying coordinate system unit or axis directions, you can only store very limited amount of metadata, etc.).</p>

---
