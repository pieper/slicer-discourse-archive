# Export volume (or segment?) to stl file with python

**Topic ID**: 25111
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/export-volume-or-segment-to-stl-file-with-python/25111

---

## Post #1 by @Mike_Flanigan (2022-09-05 22:51 UTC)

<p>Hi there,<br>
Currently I’ve been working on automating a work flow in python that goes like the following:</p>
<ol>
<li>Load CT scans (as .tiffs)</li>
<li>Create a segmentation and threshold to identify air in the scans</li>
<li>Automate a mouse click in a known location and use the “Remove selected island” feature</li>
<li>Apply the “Keep largest island” feature</li>
<li>Calculate and report statistics</li>
</ol>
<p>I’d like to add a 6th step that saves the final resulting volume as an STL file so users could easily open up a visual artifact at a later date to make sure that the script worked as intended, but I’m struggling to get the Segmentation Export Widget (or the ExportNode) syntax to work in python.</p>
<p>If anyone could provide an example of calling a/that function to export a volume/segment as an STL I’d really appreciate it!</p>

---

## Post #2 by @ungi (2022-09-06 14:58 UTC)

<p>Hi, segmentation nodes cannot be saved as STL directly. You need to first export the segmentation to model node: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a><br>
Then, model nodes can be saved as STL files.</p>

---

## Post #3 by @Sunderlandkyl (2022-09-06 15:13 UTC)

<p>You can use the vtkSlicerSegmentationsModuleLogic::ExportSegmentsClosedSurfaceRepresentationToFiles function to export the segmentation to stl:<br>
<a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a4b5328985b2d98cbbc93a5b2ae7fde6b" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a4b5328985b2d98cbbc93a5b2ae7fde6b</a></p>

---

## Post #4 by @Mike_Flanigan (2022-09-21 02:18 UTC)

<p>This post ended up providing enough of a solution framework for me to figure it out.</p><aside class="quote" data-post="4" data-topic="24850">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/tips-for-getting-started-loading-and-batch-segmenting-files-with-slicer-in-python/24850/4">Tips for getting started loading and batch segmenting files with Slicer in python?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Check this script example for running island tool and exporitng the segmentation and writing to the disk:
  </blockquote>
</aside>


---
