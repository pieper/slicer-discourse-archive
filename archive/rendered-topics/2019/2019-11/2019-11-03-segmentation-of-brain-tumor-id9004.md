# Segmentation of brain Tumor

**Topic ID**: 9004
**Date**: 2019-11-03
**URL**: https://discourse.slicer.org/t/segmentation-of-brain-tumor/9004

---

## Post #1 by @mohammad_maskani (2019-11-03 13:09 UTC)

<p>hi<br>
I have problem with  brain tumor segment with Segment Editor module ,<br>
when  i saved my model and import the model file ,its not like my model !<br>
what is the problem ? how can i fix it ?<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3ce222c784f1d9272cb65af184c2d4aec6855e34.jpeg" alt="aft" data-base62-sha1="8GB8O6i3oLhkI70FldT5ag6I7JO" width="367" height="449"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/062213b4072867d89fac088d3623cd19d5a34939.jpeg" alt="bef" data-base62-sha1="SfSd8sgnA8Q6QARxft7OIXlCpb" width="408" height="474"></p>

---

## Post #2 by @lassoan (2019-11-03 13:33 UTC)

<p>You used the “Export to files” feature with “LPS” coordinate system.</p>
<p>LPS coordinate system is better for compatibility with other software (majority of medical image computing software nowadays assumes STL and OBJ files store LPS coordinates). Slicer uses RAS coordinate system.</p>
<p>If you load a model file with LPS coordinates then you  can transform it back to RAS as described <a href="https://discourse.slicer.org/t/dicom-and-vtk-file-orientation-issue/717/7">here</a>.</p>
<p>Overall, I would suggest to use export feature for creating files for other software (mesh editors, 3D printers, etc.). If you want to save data that you will load into Slicer, you can use File / Save.</p>

---

## Post #3 by @mohammad_maskani (2019-11-04 07:22 UTC)

<p>Thank you very much <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
