# Load vtp files in slicer

**Topic ID**: 30442
**Date**: 2023-07-07
**URL**: https://discourse.slicer.org/t/load-vtp-files-in-slicer/30442

---

## Post #1 by @Kening_Zhang (2023-07-07 04:29 UTC)

<p>Dear developers,<br>
I want to load the output vtp files generated back to slicer, the code I write is as following:<br>
<span class="hashtag-raw">#Load</span> the generated anatomical tracts back into Slicer<br>
for file_name in os.listdir(AnatomicalTractsFolder):<br>
# Check whether the file extension is VTP<br>
if file_name.endswith(“.vtp”):<br>
# Build the full path of the file<br>
file_path = os.path.join(AnatomicalTractsFolder, file_name)<br>
# load vtp in slicer<br>
loaded_model_node = slicer.util.loadModel(file_path)<br>
However, it failed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0888c77dc581388f098897ef277c8a3ba9483542.png" data-download-href="/uploads/short-url/1duROwB2zgtdSOMkPUPeP9lgkz8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0888c77dc581388f098897ef277c8a3ba9483542_2_690x198.png" alt="image" data-base62-sha1="1duROwB2zgtdSOMkPUPeP9lgkz8" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0888c77dc581388f098897ef277c8a3ba9483542_2_690x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0888c77dc581388f098897ef277c8a3ba9483542_2_1035x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0888c77dc581388f098897ef277c8a3ba9483542.png 2x" data-dominant-color="DFDFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1140×328 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best wishes,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-07-07 13:48 UTC)

<p>It looks like that vtp file is empty.  Probably this is flagged as an error in VTK.  You can wrap your <code>loadModel</code> call in a try/except that the file didn’t load.</p>
<p>It is likely that older VTK versions silently accepted empty files but the I/O was reworked.  I ran into an issue like this when trying lo save empty files:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/issues/18059">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18059" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18059" target="_blank" rel="noopener">crash writing vtp with degenerate cells (new in vtk9) (#18059) · Issues · VTK...</a></h3>

  <p>Code that uses vtkXMLPolyDataWriter that previously worked with vtk8 started crashing with vtk9. We created a workaround to that in</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
