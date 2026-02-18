# Model (.VTK mesh) to Segment or Label Map for Remeshing

**Topic ID**: 15194
**Date**: 2020-12-23
**URL**: https://discourse.slicer.org/t/model-vtk-mesh-to-segment-or-label-map-for-remeshing/15194

---

## Post #1 by @Fluvio_Lobo (2020-12-23 03:05 UTC)

<p>Hello (and happy holidays to all),</p>
<p>Our group is using 3DSlicer to reconstruct DICOM-datasets, mesh them using the Segment Mesher module (and Cleaver), and running a simulation using FEBio <a href="https://discourse.slicer.org/t/meshing-self-intersecting-faces/13588"><em>(more here)</em></a>.</p>
<p>For some simulations, remeshing is done using tetgen externally.</p>
<p>We were wondering if it is possible to import a mesh (.VTK) as a model (with multiple materials) and reconstruct a segmentation or a label map that could then be re-meshed using the Segment Mesher module and Cleaver.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-12-23 03:31 UTC)

<p>Yes, sure, you can import each mesh (model node) as a segment into the segmentation node and do your workflow as usual.</p>
<p>If the mesh contains several closed surfaces, each with a different associated scalar value then you can use that scalar value to extract segments one by one, using vtkThreshold filter.</p>

---

## Post #3 by @Fluvio_Lobo (2020-12-29 20:16 UTC)

<p>Andras,</p>
<p>Thank you for your response. I think I may need some additional help though.<br>
This is what I have done;</p>
<ul>
<li>I imported the VTK model. Keep in mind that, in my case, the VTK is an a full volumetric mesh and follows the same 4.2 format exported by 3D Slicer.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d67de8224c0a032818370eb94bfdb09353be76.png" data-download-href="/uploads/short-url/leGd9Qo3vIwHmTiaF4bOBfwB9pc.png?dl=1" title="capture_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d67de8224c0a032818370eb94bfdb09353be76_2_690x373.png" alt="capture_1" data-base62-sha1="leGd9Qo3vIwHmTiaF4bOBfwB9pc" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d67de8224c0a032818370eb94bfdb09353be76_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d67de8224c0a032818370eb94bfdb09353be76_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d67de8224c0a032818370eb94bfdb09353be76_2_1380x746.png 2x" data-dominant-color="74747C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_1</span><span class="informations">1920×1040 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Then I run the VTK filter, using the Python terminal, to split the mesh into sub-meshes.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd0266ee4b3540730b97e14b096dbde13269f95e.png" data-download-href="/uploads/short-url/vx8FnrhnVAC7fKyBKyXrZ0brr9I.png?dl=1" title="capture_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd0266ee4b3540730b97e14b096dbde13269f95e_2_690x373.png" alt="capture_2" data-base62-sha1="vx8FnrhnVAC7fKyBKyXrZ0brr9I" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd0266ee4b3540730b97e14b096dbde13269f95e_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd0266ee4b3540730b97e14b096dbde13269f95e_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd0266ee4b3540730b97e14b096dbde13269f95e_2_1380x746.png 2x" data-dominant-color="AFAFB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_2</span><span class="informations">1920×1040 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Convert each sub-mesh or sub-model to a segmentation node</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1ba922db8598479e107c18150ff3778dc06f10a7.png" data-download-href="/uploads/short-url/3WHgnO8QdbdZTqm94bsRv2FDIHR.png?dl=1" title="capture_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba922db8598479e107c18150ff3778dc06f10a7_2_690x373.png" alt="capture_3" data-base62-sha1="3WHgnO8QdbdZTqm94bsRv2FDIHR" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba922db8598479e107c18150ff3778dc06f10a7_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba922db8598479e107c18150ff3778dc06f10a7_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1ba922db8598479e107c18150ff3778dc06f10a7_2_1380x746.png 2x" data-dominant-color="AFAEB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_3</span><span class="informations">1920×1040 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here I can mesh each segmentation, but not all of them combined. Is there a way of combining the segmentations? Or am I supposed to split the model after converting into a segmentation node?</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2020-12-30 05:38 UTC)

<p>You need to use at least the latest Slicer Stable Release to import a volumetric meshes into segmentation node.</p>

---

## Post #5 by @Fluvio_Lobo (2020-12-30 16:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you! Turns out I had the newer version install but was opening 4.10 from the start window… <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>Here is the current working process;</p>
<ol>
<li>
<p>Import <strong>Volumetric Mesh</strong> as a <strong>Model</strong> <em>(‘Model_1’ in Figure 1 below)</em></p>
</li>
<li>
<p>Use the <strong>Python Interactor</strong> to separate the input <strong>Model</strong> into <strong>sub-meshes</strong> or <strong>separate models</strong> <em>('Model_1_# in Figure 1 below)</em></p>
</li>
<li>
<p>Right-click on either of the <strong>sub-meshes</strong> or <strong>separate models</strong> and <strong>Convert model to segmentation node…</strong> <em>(‘Model_1_<span class="hashtag-raw">#-segmentation</span>’ in Figure 1 below)</em></p>
</li>
<li>
<p>Repeat the previous step until all <strong>sub-meshes</strong> or <strong>separate models</strong> have been converted to <strong>segmentations</strong></p>
</li>
<li>
<p>Aggregate all of the segments in a single segmentation by simply dragging and dropping. Then, delete the empty segmentations. <em>(In Figure 1, the only segmentation left is ‘Model_1_<span class="hashtag-raw">#-segmentation</span>’ )</em></p>
</li>
<li>
<p>Finally, use the <strong>Segment Mesher</strong> module to generate a volumetric mesh from the new segmentation</p>
</li>
</ol>
<p>Figure 1;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40d9e04755f112778628b7a6708df65f79aa494d.png" data-download-href="/uploads/short-url/9fHm2rLnFlcU1mvjdNCzoJwYcWh.png?dl=1" title="capture_all" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40d9e04755f112778628b7a6708df65f79aa494d_2_690x373.png" alt="capture_all" data-base62-sha1="9fHm2rLnFlcU1mvjdNCzoJwYcWh" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40d9e04755f112778628b7a6708df65f79aa494d_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40d9e04755f112778628b7a6708df65f79aa494d_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40d9e04755f112778628b7a6708df65f79aa494d_2_1380x746.png 2x" data-dominant-color="323535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_all</span><span class="informations">1920×1040 90.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Fluvio_Lobo (2020-12-30 22:26 UTC)

<p>Here is something else I found…</p>
<p>When remeshing a <strong>segmentation</strong> created this way, there is no <strong>master volume</strong> associated with said <strong>segmentation</strong>, which may produce some weird artifacts in the Cleaver mesh. I know this is still a little bit of a preference/opinion of mine <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">, but you this example I posed here results in a mesh with a <strong>min dihedral angle = 1.75686</strong> (Figure 1)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ae96b9d812c3f51ae657d31039faf7f5ff20f6a.png" data-download-href="/uploads/short-url/aGHqSXSKWFOOdRgLbBzRx02NqQi.png?dl=1" title="capture_all_flurry" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae96b9d812c3f51ae657d31039faf7f5ff20f6a_2_690x373.png" alt="capture_all_flurry" data-base62-sha1="aGHqSXSKWFOOdRgLbBzRx02NqQi" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae96b9d812c3f51ae657d31039faf7f5ff20f6a_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae96b9d812c3f51ae657d31039faf7f5ff20f6a_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4ae96b9d812c3f51ae657d31039faf7f5ff20f6a_2_1380x746.png 2x" data-dominant-color="393E38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_all_flurry</span><span class="informations">1920×1040 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To avoid this, it is possible to;</p>
<ol>
<li>
<p>Import your <strong>Bounding Volume</strong> <em>(‘prone_median’ in Figure 1 and 2)</em></p>
</li>
<li>
<p>Create a <strong>NEW Segmentation</strong>, specifying the <strong>Master Volume</strong></p>
</li>
<li>
<p>Copy all of <strong>segments</strong> from the <strong>OLD Segmentation</strong> <em>(‘Model_1_#’ in Figure 1 and 2)</em></p>
</li>
<li>
<p>Create an equal number of <strong>NEW Segments</strong> and used the <strong>Logical Operator&gt;Copy</strong> function to copy each <strong>OLD</strong> into each <strong>NEW</strong> corresponding segment <em>(‘Segment_7,8,9’ in Figure 1 and 2)</em></p>
</li>
</ol>
<blockquote>
<p><strong>STEP 4</strong> <em>May be an overkill, but using the same segments did not work for me at first, so I just copied them and it worked</em></p>
</blockquote>
<ol start="5">
<li>Use <strong>Segment Mesher</strong> to generate a new volumetric mesh using <strong>Cleaver</strong> <em>(Figure 2)</em></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/657a8fb79c38a368593fda8ffffdf422b0668aef.png" data-download-href="/uploads/short-url/etIOhQpxZGDbEg859p1ae7W0he7.png?dl=1" title="capture_all_flat" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/657a8fb79c38a368593fda8ffffdf422b0668aef_2_690x373.png" alt="capture_all_flat" data-base62-sha1="etIOhQpxZGDbEg859p1ae7W0he7" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/657a8fb79c38a368593fda8ffffdf422b0668aef_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/657a8fb79c38a368593fda8ffffdf422b0668aef_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/657a8fb79c38a368593fda8ffffdf422b0668aef_2_1380x746.png 2x" data-dominant-color="3B4038"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_all_flat</span><span class="informations">1920×1040 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The resultant mesh had about <strong>1,000 more tets</strong>, but the <strong>min dihedral angle = 4.10604</strong>!!!</p>
<p>I hope people find this useful,</p>

---
