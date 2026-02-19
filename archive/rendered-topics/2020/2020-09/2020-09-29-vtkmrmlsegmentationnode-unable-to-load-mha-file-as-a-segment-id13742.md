---
topic_id: 13742
title: "Vtkmrmlsegmentationnode Unable To Load Mha File As A Segment"
date: 2020-09-29
url: https://discourse.slicer.org/t/13742
---

# [vtkMRMLSegmentationNode] Unable to load .mha file as a segmentation node

**Topic ID**: 13742
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/vtkmrmlsegmentationnode-unable-to-load-mha-file-as-a-segmentation-node/13742

---

## Post #1 by @strider_hunter (2020-09-29 10:07 UTC)

<ul>
<li>I have a file which is originally <em>.nrrd</em> but I convert it to <em>.mha</em> (for homogeneity purposes as I use other datasets as well)</li>
<li>I am able to load the <em>.nrrd</em> file using <em>slicer.util.loadSegmentation(pathMaskFile)</em>, but unable to do the same via the <em>.mha</em> file. The content/dimensions are the same, but the header formatting is of course different.<br>
** The error is in slicer\util.py", line 598, in loadNodeFromFile()</li>
<li>The headers of my files are in the image below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d6eee19cc5e86c5589cf5527ff0f060ed048ca.png" data-download-href="/uploads/short-url/7oAQgSpwlAxsLe75U9713UX5vqW.png?dl=1" title="nrrd_vs_mha_for_maskfile" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d6eee19cc5e86c5589cf5527ff0f060ed048ca_2_690x168.png" alt="nrrd_vs_mha_for_maskfile" data-base62-sha1="7oAQgSpwlAxsLe75U9713UX5vqW" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d6eee19cc5e86c5589cf5527ff0f060ed048ca_2_690x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d6eee19cc5e86c5589cf5527ff0f060ed048ca_2_1035x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d6eee19cc5e86c5589cf5527ff0f060ed048ca_2_1380x336.png 2x" data-dominant-color="302F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">nrrd_vs_mha_for_maskfile</span><span class="informations">1823×445 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>Is there any way to change the header of the <em>.mha</em> file so that it directly loads as a segmentation node ? I am also not able to do via the drag-and-drop UI option (image below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49caa05c7ecd61fd28eb908b60050be36f281973.png" data-download-href="/uploads/short-url/awMYMLckXiVv6CKKOpRSR3YeWP1.png?dl=1" title="mha_volume_only" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49caa05c7ecd61fd28eb908b60050be36f281973_2_690x124.png" alt="mha_volume_only" data-base62-sha1="awMYMLckXiVv6CKKOpRSR3YeWP1" width="690" height="124" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49caa05c7ecd61fd28eb908b60050be36f281973_2_690x124.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49caa05c7ecd61fd28eb908b60050be36f281973_2_1035x186.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49caa05c7ecd61fd28eb908b60050be36f281973_2_1380x248.png 2x" data-dominant-color="D8D9DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mha_volume_only</span><span class="informations">1421×256 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I can do so for a <em>.nrrd</em> file (image below)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57dd4eb0e1c0fef52c73b6a8d5ee87d24c15998e.png" data-download-href="/uploads/short-url/cxhGHOAIjZl1Hf22VyVY9dMUSo6.png?dl=1" title="nrrd_as_segmentationode" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dd4eb0e1c0fef52c73b6a8d5ee87d24c15998e_2_690x156.png" alt="nrrd_as_segmentationode" data-base62-sha1="cxhGHOAIjZl1Hf22VyVY9dMUSo6" width="690" height="156" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dd4eb0e1c0fef52c73b6a8d5ee87d24c15998e_2_690x156.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57dd4eb0e1c0fef52c73b6a8d5ee87d24c15998e_2_1035x234.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57dd4eb0e1c0fef52c73b6a8d5ee87d24c15998e.png 2x" data-dominant-color="D6D6D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">nrrd_as_segmentationode</span><span class="informations">1370×311 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The files are from an open dataset <a href="http://www.imagenglab.com/wiki/mediawiki/index.php?title=2015_MICCAI_Challenge" rel="noopener nofollow ugc">MICCAI2015</a></p>

---

## Post #2 by @strider_hunter (2020-09-29 10:28 UTC)

<ul>
<li>
<p>I just found <a href="https://github.com/Slicer/Slicer/blob/master/Docs/user_guide/modules/segmentations.md#import-an-existing-segmentation-from-volume-file" rel="noopener nofollow ugc">documentation</a> which states that only NRRD/NIFTI files can be directly loaded as segmentations. Is there a particular reason for this choice? Are there plans to add more file formats?</p>
</li>
<li>
<p>I was also able to find a python binding for <a href="https://github.com/Slicer/Slicer/search?q=%22Convert+labelmap+to+segmentation+node%22" rel="noopener nofollow ugc">“Convert labelmap to segmentation node”</a> from <a href="https://discourse.slicer.org/t/how-to-automatically-convert-a-labelmap-volume-to-a-segmentation-node-upon-loading-labelmap-volume/9931/8">the slicer forum</a></p>
</li>
</ul>
<pre><code class="lang-python">tmp = slicer.util.loadLabelVolume(pathMaskFile)
mask = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(tmp, mask)
slicer.mrmlScene.RemoveNode(tmp)
</code></pre>

---

## Post #3 by @lassoan (2020-09-29 12:23 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="2" data-topic="13742">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>NRRD/NIFTI files can be directly loaded as segmentations. Is there a particular reason for this choice? Are there plans to add more file formats?</p>
</blockquote>
</aside>
<p>We encourage users to use NRRD format for segmentation storage (as it allows simple storage of additional metadata). Nifti is widely used by the neuroimaging community and many people requested support for it, so we enabled it, too. We don’t plan to add direct support for any other formats, as you it just takes two clicks or 2-3 lines of Python code to convert a labelmap volume to segmentation.</p>
<p>Metaimage (mha) format capabilities are almost identical to NRRD, but it has a huge limitation: 4D data support in metaimage is not robust. You cannot specify meaning of each dimension, which means that it cannot store overlapping segmentations or time sequences reliably. Its format also specifies a few exotic features (such as multi-file headers), which are not commonly implemented, and image orientation definition is somewhat misleading.</p>
<p>You can extend/customize almost anything using Python or C++ plugins. If you want to add import/export of any file formats as any node type then you can do it by specifying a file reader for it (just an extra class in your Python scripted module, about 10-20 lines, see <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">example</a>).</p>

---
