# Export multiple individual segment .stl files from one segmented nii.gz file using python script

**Topic ID**: 15687
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/export-multiple-individual-segment-stl-files-from-one-segmented-nii-gz-file-using-python-script/15687

---

## Post #1 by @Mingxiao_Tu (2021-01-27 03:36 UTC)

<p>Hi there,</p>
<p>I am currently new to 3dslicer and I have questions about how to perform a specific task using the python script code for 3d slicer.</p>
<p>The segmented file (nii.gz) can be exported into individual ‘.stl’ files based on different segments using the 3Dslicer software. However I am about to integrate this function into my own python code. Could anyone please give me some tips on where I should look at or even start? Thank you very much.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e03890a85d5381c3a9c8c34755d7992519c29891.png" data-download-href="/uploads/short-url/vZy8TxNrOcnpz1bxEiJJdjHG1IB.png?dl=1" title="new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03890a85d5381c3a9c8c34755d7992519c29891_2_690x210.png" alt="new" data-base62-sha1="vZy8TxNrOcnpz1bxEiJJdjHG1IB" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03890a85d5381c3a9c8c34755d7992519c29891_2_690x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03890a85d5381c3a9c8c34755d7992519c29891_2_1035x315.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03890a85d5381c3a9c8c34755d7992519c29891_2_1380x420.png 2x" data-dominant-color="F7F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new</span><span class="informations">1504×459 34.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-01-27 03:39 UTC)

<p>See examples how to do this in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #3 by @Mingxiao_Tu (2021-01-27 03:46 UTC)

<p>Hi, thank you very much for the link. It is indeed helpful. However I also noticed that in the 3DSlicer we could export segments into ‘.stl’, ‘.obj’ or ‘nrrd’ files, could the python script allow the user to choose which output format?</p>

---

## Post #4 by @lassoan (2021-01-27 04:06 UTC)

<p>Yes, you can save segmentations to all these formats. You can find more examples in this forum, for example:</p>
<aside class="quote quote-modified" data-post="7" data-topic="10802">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/exporting-segment-as-obj-through-python/10802/7">Exporting Segment as OBJ through Python</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    To get help on how to use a method, use help method in the Python interactor: 
&gt;&gt;&gt; help(slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles)
Help on method_descriptor:

ExportSegmentsClosedSurfaceRepresentationToFiles(...)
    V.ExportSegmentsClosedSurfaceRepresentationToFiles(string,
        vtkMRMLSegmentationNode, vtkStringArray, string, bool, float,
        bool) -&gt; bool
    C++: static bool ExportSegmentsClosedSurfaceRepresentationToFiles(
        std::…
  </blockquote>
</aside>


---
