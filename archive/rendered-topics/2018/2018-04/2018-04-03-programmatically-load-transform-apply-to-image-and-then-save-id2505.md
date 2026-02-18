# Programmatically load transform apply to image and then save

**Topic ID**: 2505
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/programmatically-load-transform-apply-to-image-and-then-save/2505

---

## Post #1 by @kayarre (2018-04-03 18:48 UTC)

<p>I  am trying to automate parts of my workflow in Slicer, (  my mental model wants something like VMTK or the CLI where I can break the operations into smaller steps and add and rearrange as needed)</p>
<p>I have figured out how to read in a .h5 transform and and image volume with python commands but it is not clear how to apply the transform to the image volume and save or “harden” transformed image to be subsequently processed with Brainsfit.</p>
<p>i have been reading through<br>
[<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms</a>] (Transforms docs)</p>
<p>but it is more confusing than helpful</p>

---

## Post #2 by @kayarre (2018-04-03 19:01 UTC)

<p>This worked for me:</p>
<p>[success, dsa] = slicer.util.loadVolume(r’./image_vols/DSA.nrrd’, returnNode=True)<br>
<span class="hashtag">#relative</span> paths seem to not work with transforms, filed on a bug on that.<br>
[success, dss2post_trans]  = slicer.util.loadTransform(r’/home/sansomk/caseFiles/mri/VWI_proj/case4/registration/dsa2post_man_LT.h5’, returnNode=True)<br>
dsa.SetAndObserveTransformNodeID(dsa2post_trans.GetID())<br>
slicer.vtkSlicerTransformLogic().hardenTransform(dsa)<br>
slicer.util.saveNode(dsa, “./registration/dsa2post_man_trans.nrrd”)</p>
<p>I haven’t tried this outside of the python interactor, but ideally I would be able to execute this without the slicer gui, I assume this is possible but I am don’t know how.</p>

---

## Post #3 by @lassoan (2018-04-03 22:13 UTC)

<p>This post should help: <a href="https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863">Slicer batch processing question (--no-main-window --python-script)</a></p>
<p>If you still have questions then let us know.</p>

---
