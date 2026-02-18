# 3D model to segmentation

**Topic ID**: 5135
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/3d-model-to-segmentation/5135

---

## Post #1 by @muratmaga (2018-12-18 21:48 UTC)

<p>I would like to able to clean some 3D models from surface scanner. Currently, what I do is to import the model as a segmentation node, and then export the resultant segmentation node as a label map, which I use it as the master volume in the segment editor.</p>
<p>It seems to work. Would there be any downsides to this approach?</p>

---

## Post #2 by @lassoan (2018-12-18 21:57 UTC)

<p>This is a good approach. In recent nightly Slicer versions this process is streamlined:</p>
<ul>
<li>Drag-and-drop STL file to Slicer window and in Add data dialog, choose “Segmentation” in Description column (there is no need to load as model and then import to segmentation but you can directly load as segmentation)</li>
<li>Go to Segment Editor, click “Specify geometry” button (next to Master volume selector)</li>
<li>Choose current segmentation node as source geometry, set spacing values, click OK</li>
</ul>
<p>This automatically creates a blank master volume with the necessary size and chosen resolution so that you can edit the segmentation right away.</p>

---

## Post #3 by @muratmaga (2018-12-18 22:07 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. How recent is this? My nightly from 12/11 still shows only model/scalar overlay/volume as options in description column. My data is in ply format, not stl by the way.</p>

---

## Post #4 by @lassoan (2018-12-18 22:22 UTC)

<p>We have not enabled direct segmentation import for all surface mesh files. Probably ply you still have to load as model and then import to segmentation.</p>

---

## Post #5 by @muratmaga (2020-02-18 04:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> are you planning to enable importing segmentation from non-stl 3D model formats at all?</p>

---

## Post #6 by @lassoan (2020-02-18 04:36 UTC)

<p>We can import STL and OBJ. Would there be any other mesh file formats that you would like load directly as segmentation?</p>

---

## Post #7 by @muratmaga (2020-02-18 04:38 UTC)

<p>I think it would be good to have PLY and VTK. Particularly latter being the default format for 3D models in Slicer.</p>

---

## Post #8 by @jwalk (2020-06-13 01:25 UTC)

<p>Hello,<br>
I am trying to import a segmentation from one CT examination volume into a new, similar CT examination volume. When I attempt to do so, the segmentation and/or model that I import is located in a different location/ coordinate than the CT volume.</p>
<p>I would like to simply move and maybe rotate the 3d segmentation a little in order to superimpose it over the new CT exam volume.</p>
<p>I hope someone can help with this. Also happy to work together to figure it out over zoom.<br>
Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f177b01bb928f0a21fb74e2c5de9683fde9d58.jpeg" data-download-href="/uploads/short-url/5HlXIkO22gVBec3LJtF3ejYHe4w.jpeg?dl=1" title="scan" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f177b01bb928f0a21fb74e2c5de9683fde9d58_2_690x454.jpeg" alt="scan" data-base62-sha1="5HlXIkO22gVBec3LJtF3ejYHe4w" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f177b01bb928f0a21fb74e2c5de9683fde9d58_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f177b01bb928f0a21fb74e2c5de9683fde9d58_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f177b01bb928f0a21fb74e2c5de9683fde9d58_2_1380x908.jpeg 2x" data-dominant-color="9597BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scan</span><span class="informations">1528×1007 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @muratmaga (2020-06-13 02:12 UTC)

<p>Short answer is you can use <code>Transforms</code> module to create a blank transform, assign your segmentation to it, and the use the position sliders to manually align in 3D space. Registration might be an option too.</p>
<p>But, unless these are coming from the same subject, they probably won’t line up very well due to difference between individuals. You should be able to segment your volume with the existing segmentation tools quite effectively, so you don’t have to worry aligning another segmentation.</p>

---

## Post #10 by @lassoan (2020-06-13 04:27 UTC)

<p>Yes, probably landmark-based registration would get these aligned the fastest. If you use Fiducial registration wizard module (in SlicerIGT extension) then you can choose warping transform, which can deal with large differences.</p>
<p>What is your goal with the registration? Why don’t you segment the CT image instead?</p>

---

## Post #11 by @lassoan (2020-06-23 23:31 UTC)

<p>2 posts were split to a new topic: <a href="/t/image-is-not-aligned-with-segmentation/12190">Image is not aligned with segmentation</a></p>

---
