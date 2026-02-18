# Virtual reality controller to split segments/Labelling

**Topic ID**: 5751
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/virtual-reality-controller-to-split-segments-labelling/5751

---

## Post #1 by @sarvpriya1985 (2019-02-13 01:31 UTC)

<p>Hi,<br>
I have few questions regarding Virtual display.<br>
I am using HP mixed reality headset to see segmented structures in virtual reality. For now I am using headset as a way to slice (split) segments to see internal anatomy. But that sometimes is not useful as the moment you want to see it from different angle you have to rotate the model and then it is no longer sliced.</p>
<ol>
<li>Is there a way I can use one controller to just slice a segment and use another to zoom, pan or rotate.</li>
<li>Also , when I check the video with pedicle screw insertion, the screw is being handled with one controller and can be moved with ease.<br>
Is there a way I can split the segmented model using the controller and move them apart just by dragging (my model has several segments).</li>
<li>LABELLING- I wish to label parts of segmented model so that other persons seeing the scene on monitor understands what is being shown. I tried placing fiducial markers and renaming them, but they keep hiding when the model is rotated. Is there any module by which the labelling of structures remain fixed.</li>
</ol>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @cpinter (2019-02-13 14:14 UTC)

<ol>
<li>I believe if you grab the “slice anchor” with one controller and the volume in the other, then you can move the two independently (it is not zoom and pan and rotate, but essentially the same). I actually haven’t tested this yet so let us know if it doesn’t work.</li>
<li>You can move one node at a time, and segments in a segmentation belong in one node. YOu can “split” them by exporting the segmentation to a model hierarchy (right-click segmentation in Data module). Then you can move the segments independently. After you’re done you can import them back to another segmentation in the Segmentations module</li>
<li>If you start moving the models in VR, an interaction transform node is created for each model. To sync movement of a fiducial and the model, you can apply the interaction transform of the model to the fiducial. Again, haven’t tested this specifically.</li>
</ol>
<p>Best,<br>
csaba</p>

---
