# After ImportModelToSegmentationNode some segments are cubical

**Topic ID**: 29684
**Date**: 2023-05-27
**URL**: https://discourse.slicer.org/t/after-importmodeltosegmentationnode-some-segments-are-cubical/29684

---

## Post #1 by @xxxiNAIxxx (2023-05-27 03:44 UTC)

<p>Hi.<br>
I have a few stl files and want to create one multilabel for monai train. I write python-script and it works (<a href="https://gist.github.com/xxxiNAIxxx/544be2f1ef2ad63a44fd38d43ab54760" class="inline-onebox" rel="noopener nofollow ugc">gist:544be2f1ef2ad63a44fd38d43ab54760 · GitHub</a>)<br>
In general, it loads all stl in cycle and imports to segmentation:</p>
<pre><code class="lang-python">def load_avalible_labels(labels_stl_path, segmentationNode):
    for label in labels_stl_path:
        modelNode = slicer.modules.models.logic().AddModel(label)
        slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode, segmentationNode)
        slicer.mrmlScene.RemoveNode(modelNode)
</code></pre>
<p>then fill, save and so on…</p>
<p>But! Some segments are “cubical”, some are normal:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af60aa878bd6ea5faa383c33431806fd82df213.jpeg" data-download-href="/uploads/short-url/8pAPLWJZCAKpyF4xD1X5LrZ8YIb.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af60aa878bd6ea5faa383c33431806fd82df213_2_690x214.jpeg" alt="1" data-base62-sha1="8pAPLWJZCAKpyF4xD1X5LrZ8YIb" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af60aa878bd6ea5faa383c33431806fd82df213_2_690x214.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af60aa878bd6ea5faa383c33431806fd82df213_2_1035x321.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af60aa878bd6ea5faa383c33431806fd82df213_2_1380x428.jpeg 2x" data-dominant-color="3C3C44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×596 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
stl-files are same, I mean, if open all files in a slicer as model they are smooth.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6375a27d99fbd1898d55794bc903bf8d9e873c78.png" alt="2" data-base62-sha1="ebRiElBdsWzHi0npzUv7ePGeUZ2" width="256" height="210"><br>
If I convert them manually (model&gt;segmentation node), segments are smooth too.</p>
<p>So… could someone help?</p>

---

## Post #2 by @lassoan (2023-05-28 12:16 UTC)

<p>If you start editing a segmentation then its source (a.k.a. master) representation is changed to “binary labelmap”. A binary labelmap is made up of voxels that you can see when you zoom in. If you find the default resolution insufficient the you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">increase it</a>.</p>

---

## Post #3 by @xxxiNAIxxx (2023-05-29 20:11 UTC)

<p>Thank you!<br>
Problem was in that</p>

---
