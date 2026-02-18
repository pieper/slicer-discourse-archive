# Different segmentation export function produce different results

**Topic ID**: 27279
**Date**: 2023-01-15
**URL**: https://discourse.slicer.org/t/different-segmentation-export-function-produce-different-results/27279

---

## Post #1 by @S_Arbabi (2023-01-15 15:53 UTC)

<p>Hi,</p>
<p>I have a segmentation node that I want to save on disk. In order to save it with saveNode, I need to convert it to a labelmap, but the way I convert it makes the result different:</p>
<p>here is how the segmentation looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4376e0a3d64c825566a120440ac26b53aa0ae04d.jpeg" data-download-href="/uploads/short-url/9COGqN5odpBsK8R1Ds3OPuN8htP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4376e0a3d64c825566a120440ac26b53aa0ae04d_2_671x500.jpeg" alt="image" data-base62-sha1="9COGqN5odpBsK8R1Ds3OPuN8htP" width="671" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4376e0a3d64c825566a120440ac26b53aa0ae04d_2_671x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4376e0a3d64c825566a120440ac26b53aa0ae04d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4376e0a3d64c825566a120440ac26b53aa0ae04d.jpeg 2x" data-dominant-color="1C1C1B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">722×538 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here are two different ways I convert the segmentation to labelmap and result of each:</p>
<ul>
<li>Using “ExportAllSegmentsToLabelmapNode”<br>
this way the labelmap <strong>is totally overlap with segmentation</strong>, and that’s what is desirable</li>
</ul>
<p>I run this in Interactor:</p>
<pre><code class="lang-auto">slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, lblmap, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)
</code></pre>
<p>here’s how it looks when I overlap to the segmentation shown above:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4bd143cac7d247170c455ce4b70386a34ea917.jpeg" data-download-href="/uploads/short-url/r9r9Lrks73kfn8DLi8KJ6eqmTRR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be4bd143cac7d247170c455ce4b70386a34ea917_2_690x464.jpeg" alt="image" data-base62-sha1="r9r9Lrks73kfn8DLi8KJ6eqmTRR" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be4bd143cac7d247170c455ce4b70386a34ea917_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4bd143cac7d247170c455ce4b70386a34ea917.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4bd143cac7d247170c455ce4b70386a34ea917.jpeg 2x" data-dominant-color="1C1C1C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">784×528 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and the other way is:</p>
<ul>
<li>Using “ExportVisibleSegmentsToLabelmapNode”<br>
this way the labelmap <strong>is not</strong> a full overlap with segmentation, and I don’t want this to happen, simply because it’s not true segmentation mask of all voxels.</li>
</ul>
<p>Here is the interactor code if I want to reproduce (here ref is the reference image node):</p>
<pre><code class="lang-auto">slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, lblmap, ref)
</code></pre>
<p>and here’s how it looks compared to original segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e78bff001a87d4f48151d3d37c1812ecaf2b0ad6.jpeg" data-download-href="/uploads/short-url/x2meCTsbaUvAUl8nitXQd8C5XH8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e78bff001a87d4f48151d3d37c1812ecaf2b0ad6_2_690x464.jpeg" alt="image" data-base62-sha1="x2meCTsbaUvAUl8nitXQd8C5XH8" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e78bff001a87d4f48151d3d37c1812ecaf2b0ad6_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e78bff001a87d4f48151d3d37c1812ecaf2b0ad6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e78bff001a87d4f48151d3d37c1812ecaf2b0ad6.jpeg 2x" data-dominant-color="1C1C1C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×540 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It’s not clear to me why converting segmentation to labelmap should produce different results, especially that the result is unrealistic when I provide the reference image to it (which I expected the other way around).</p>
<p>Still that would be fine if I could use it in my code, but when I save the generated (visually looking fine) labelmap, and then load it into slicer, it seems to have incorrect position, since I see nothing overlaying image. How should I handle this?</p>
<p>(Slicer version: 5.0.2 r30822 / a4420c3)</p>

---

## Post #2 by @S_Arbabi (2023-01-16 13:10 UTC)

<p>Hi, anyone has ideas on this? Ideas appreciated.</p>

---

## Post #3 by @lassoan (2023-01-16 21:56 UTC)

<p>A segmentation object can store the segmentation at different representations and resolutions. Usually the same geometry is used in all segments and that is the same as the segmentation’s reference geometry, but if you switched source volumes during segmentations then they may be different. It is up to you to choose what representation and resolution you would like to export.</p>
<p>If you export a labelmap representation then I would recommend to use <a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a1e4cd964c6b4c616a3c79968440b0f0d">any of the export methods</a> that take a <code>referenceVolumeNode</code> as input and set the reference volume to the geometry you need.</p>
<p>In your examples, you got different results, because of the reference geometry you specified in the <code>ref</code> node (probably you have just left some default geometry in it, with 1.0mm uniform spacing).</p>

---

## Post #4 by @S_Arbabi (2023-01-17 10:35 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>Thank you for your informative reply,<br>
I would like to elaborate a bit more on the context of this issue I’m facing, I hope this helps me get even more specific information.</p>
<p>I once had an image (img_original), that I previously transformed with a rigid transformation to create (img_transformed). Then I segmented a pathology area on this transformed image (pathology).</p>
<p>now I want to inverse transform the pathology, to overlay on the original image and save it on that. so I do it like this:</p>
<pre><code class="lang-auto">transformation.Inverse()
pathology.SetAndObserveTransformNodeID(transformation.GetID())
lblmap = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(pathology, lblmap, img_original)
</code></pre>
<p>doing so the segmentation (in red in image below) which was looking acceptable after applying inverse transformation on it, created the labelmap (in green) that looks somehow not a precise representation of the segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/166d77e84c78c6bf21f519145e52ecaf57587310.jpeg" data-download-href="/uploads/short-url/3cp2r1XVq4OY0quv9EOfFKLnaI8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/166d77e84c78c6bf21f519145e52ecaf57587310_2_690x354.jpeg" alt="image" data-base62-sha1="3cp2r1XVq4OY0quv9EOfFKLnaI8" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/166d77e84c78c6bf21f519145e52ecaf57587310_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/166d77e84c78c6bf21f519145e52ecaf57587310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/166d77e84c78c6bf21f519145e52ecaf57587310.jpeg 2x" data-dominant-color="252524"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">941×483 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As I am creating this to make my training set for next steps, I’m concerned about the discrepancy between the two. for instance, in the image above, the labelmap goes a bit inside tendon, that by definition can not be the pathology, and so this can provide wrong information to neural network in training later, I believe.</p>
<p>I appreciate any thoughts that can come helpful on any steps I tried to describe here.<br>
Thanks in advance</p>

---

## Post #5 by @lassoan (2023-01-17 14:46 UTC)

<p>If you harden a warping (not just rigid translation+rotation) transform on an image or segmentation  then there is some loss of details due to resampling. To compensate for this information loss, you can resample the original image to have 2x-3x smaller spacing and perform all operations (transformation, segmentation, etc.) on this higher-resolution image.</p>
<p>To keep the data size under control, it is also recommended to crop the image to the minimum necessary extent and use isotropic spacing. All these features - reducing spacing, resampling to isotropic spacing, cropping - are available at one place, in <code>Crop volume</code> module.</p>

---
