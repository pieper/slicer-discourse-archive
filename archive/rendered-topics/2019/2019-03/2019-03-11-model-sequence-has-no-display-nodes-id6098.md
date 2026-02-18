# Model Sequence has no display nodes

**Topic ID**: 6098
**Date**: 2019-03-11
**URL**: https://discourse.slicer.org/t/model-sequence-has-no-display-nodes/6098

---

## Post #1 by @GerryG (2019-03-11 05:03 UTC)

<p>Operating system: Linux Ubuntu 18.10<br>
Slicer version: 4.10.1</p>
<p>I have created a Sequence from a number of vtkUnstructuredGrid models and get the below error when I try to play in in Sequence Browser:<br>
virtual QColor qSlicerSubjectHierarchyModelsPlugin::getDisplayColor(vtkIdType, QMap&lt;int, QVariant&gt;&amp;) const : No display node for model</p>
<p>The models can be seen in the 3D viewer when viewed as a model although I can’t get a slice view either.<br>
I’m sure this is something trivial that I have misunderstood.<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2019-03-11 05:05 UTC)

<aside class="quote no-group" data-username="GerryG" data-post="1" data-topic="6098">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/a698b9/48.png" class="avatar"> GerryG:</div>
<blockquote>
<p>I have created a Sequence from a number of vtkUnstructuredGrid models</p>
</blockquote>
</aside>
<p>How did you create the models?<br>
Did you create display nodes for the models as well?<br>
Did you put the display nodes in a sequence or just created a single display node and associated with the model sequence’s proxy node?</p>

---

## Post #3 by @GerryG (2019-03-11 05:27 UTC)

<p>The models are a series of .vtu files. one for each time increment. They contain point data connected by cells and some scalars.<br>
Looking in the Data Module each ModelNode has a hidden associated DisplayNode. These are not something I actively created beyond importing the .vtu files. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23354533f093428978fd4dd7f5ae4717eacd417f.png" data-download-href="/uploads/short-url/51sQeZ5SzKLHwPnpYPpqZziuw7Z.png?dl=1" title="Screenshot%20from%202019-03-11%2013-23-37" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23354533f093428978fd4dd7f5ae4717eacd417f_2_690x388.png" alt="Screenshot%20from%202019-03-11%2013-23-37" data-base62-sha1="51sQeZ5SzKLHwPnpYPpqZziuw7Z" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23354533f093428978fd4dd7f5ae4717eacd417f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23354533f093428978fd4dd7f5ae4717eacd417f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23354533f093428978fd4dd7f5ae4717eacd417f_2_1380x776.png 2x" data-dominant-color="898997"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-03-11%2013-23-37</span><span class="informations">1920×1080 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
When creating the sequence the only option for importable nodes are the ModelNodes.<br>
How would I go about creating a DisplayNode?</p>

---
