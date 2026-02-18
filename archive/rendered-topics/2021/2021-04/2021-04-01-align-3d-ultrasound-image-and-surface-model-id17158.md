# Align 3D ultrasound image and surface model

**Topic ID**: 17158
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/align-3d-ultrasound-image-and-surface-model/17158

---

## Post #1 by @sulaimanvesal (2021-04-01 05:34 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>It’s been a week that I am struggling with the new dataset that I received including ultrasound/MRI and their corresponding STL files. As I have mentioned earlier, I wrote the code and successfully combined STLs an exported to NRRD based on their corresponding MRI images. On the other hand, our STL files have been made for both Ultrasound and MRI.</p>
<p>However, similar to this issue, when I load US volumes and corresponding STLs, the STL files are totally off. I followed your recommendation to convert LPS/RPS for coordinate mismatch, but that didn’t help. Even, I tried to set the origin, pixel spacing and view direction of exported nrrd as US volume, but still the segmentation output is totally outside of the region.</p>
<p>The STL files have been generated couple of years ago with 3D slicer. I thought maybe that is the issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d06ee9c9b3cf309054c9b9a838fc5b6b226c369f.jpeg" data-download-href="/uploads/short-url/tJSWy7Ju8iLKvR6QgAMGOjHEiUT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d06ee9c9b3cf309054c9b9a838fc5b6b226c369f_2_642x500.jpeg" alt="image" data-base62-sha1="tJSWy7Ju8iLKvR6QgAMGOjHEiUT" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d06ee9c9b3cf309054c9b9a838fc5b6b226c369f_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d06ee9c9b3cf309054c9b9a838fc5b6b226c369f_2_963x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d06ee9c9b3cf309054c9b9a838fc5b6b226c369f.jpeg 2x" data-dominant-color="8A8BB5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1002×780 78.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @slicer365 (2021-04-01 05:50 UTC)

<p>In fact, there is a very simple method, you can adjust the model 180 degrees in Transform.IS colume</p>

---

## Post #3 by @sulaimanvesal (2021-04-01 05:54 UTC)

<p>I am quite new in 3D slicer, could you provide more details?<br>
I have a bunch of STL files and I need to add this functionality into my code.</p>
<p>Transoform.IS just rotate the model, it does not align the model to the volume. I just tried it.</p>

---

## Post #4 by @slicer365 (2021-04-01 06:23 UTC)

<p>You can try other transforms, adjust 180 degrees, the stl will be aligned with the volume. I’m not sure which mode is more suitable, but this kind of coordinate change is not 1 degree and 2 degrees, but 180 degrees, so it is easier to adjust</p>

---

## Post #5 by @muratmaga (2021-04-01 19:10 UTC)

<aside class="quote no-group" data-username="sulaimanvesal" data-post="1" data-topic="17158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sulaimanvesal/48/10463_2.png" class="avatar"> sulaimanvesal:</div>
<blockquote>
<p>The STL files have been generated couple of years ago with 3D slicer. I thought maybe that is the issue.</p>
</blockquote>
</aside>
<p>If these are old models, than the coordinate system is probably RAS. Drag and drop them into Slicer, in Load data dialog box, expand options and change the Coordinate System from default to RAS.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a3f112f2a9373458bd197de7d605ae6c0d4ab25.png" data-download-href="/uploads/short-url/8jgOsWhitbVAqEJNlxxyeJg1roh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a3f112f2a9373458bd197de7d605ae6c0d4ab25.png" alt="image" data-base62-sha1="8jgOsWhitbVAqEJNlxxyeJg1roh" width="690" height="411" data-dominant-color="2C2D2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">741×442 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @sulaimanvesal (2021-04-01 21:11 UTC)

<p>I have tried this method too but no success.</p>
<p>One question, do the models also store their origin/pixel-spacing information like normal volume?</p>
<p>When I export the STL file to nrrd segmentation output, I tried to set the origin and spacing the same as actual volume, with the hope that this enforces the alignment. However, the segmentation is still off the actual view.</p>
<h1>Input nodes</h1>
<pre><code>volumeNode   = slicer.util.loadVolume(usPath)
prostateNode = slicer.util.loadSegmentation(prosSegPath)

if usPath is not None:
    usNode = slicer.util.loadVolume(usPath)
    spacing = usNode.GetSpacing()
    origin = usNode.GetOrigin()

# Write segmentation to labelmap volume node with a geometry that matches the volume node
labelmapVolumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(prostateNode, labelmapVolumeNode1, volumeNode)

labelmapVolumeNode1.SetOrigin(origin)
labelmapVolumeNode1.SetSpacing(spacing)</code></pre>

---

## Post #7 by @lassoan (2021-04-02 00:09 UTC)

<p>Do you have the MRML scene? There may be transforms in the scene that you need to apply.</p>
<p>If you know which version was used to save this scene then please check if that version loads it correctly. (all previous releases are available on the Slicer download page)</p>

---

## Post #8 by @sulaimanvesal (2021-04-05 02:23 UTC)

<p>Hi Lassoan,</p>
<p>Unfortunately I don’t have MRML scene files. I did some more investigations. If I load first the stl file, it will be in the center of the view window, and then I load the volume (US image). It will be out of the scene but If I press the “Center Volume” button from Volumes tab, both STL model and volume are align together. Even though the direction of STL is not fully match, but I can set that. Now, If I do the reverse and first load the volume and then STL file, I can not have this alignment neither in Python code nor in Slicer window.</p>
<p>Any idea, how to set the US volume always to the center?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5812e42544e678f5a43f2042452bbdb90fb978f4.png" data-download-href="/uploads/short-url/cz8utGVyoqwB30f6wbB2DaKqbly.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5812e42544e678f5a43f2042452bbdb90fb978f4_2_530x500.png" alt="image" data-base62-sha1="cz8utGVyoqwB30f6wbB2DaKqbly" width="530" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5812e42544e678f5a43f2042452bbdb90fb978f4_2_530x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5812e42544e678f5a43f2042452bbdb90fb978f4_2_795x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5812e42544e678f5a43f2042452bbdb90fb978f4.png 2x" data-dominant-color="9B9DCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1040×980 25.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2582e539495b04859ef0cc8347625bb6a5416fba.jpeg" data-download-href="/uploads/short-url/5lQ6J9aMC1jErRq62gIkdEakOQq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2582e539495b04859ef0cc8347625bb6a5416fba_2_488x500.jpeg" alt="image" data-base62-sha1="5lQ6J9aMC1jErRq62gIkdEakOQq" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2582e539495b04859ef0cc8347625bb6a5416fba_2_488x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2582e539495b04859ef0cc8347625bb6a5416fba_2_732x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2582e539495b04859ef0cc8347625bb6a5416fba.jpeg 2x" data-dominant-color="8081A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">816×836 73.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c7f6fc562c3f7d61382c90c756210929596f861.png" data-download-href="/uploads/short-url/mkrw3zumRWjpgLImyp9kq4MKbQd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c7f6fc562c3f7d61382c90c756210929596f861.png" alt="image" data-base62-sha1="mkrw3zumRWjpgLImyp9kq4MKbQd" width="690" height="386" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×628 31.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/019488f5b301ccf35648ace5698b76d51823e0b5.jpeg" data-download-href="/uploads/short-url/dYI9Qk8pXO0lswnxYJ7CBCgLrL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/019488f5b301ccf35648ace5698b76d51823e0b5_2_631x500.jpeg" alt="image" data-base62-sha1="dYI9Qk8pXO0lswnxYJ7CBCgLrL" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/019488f5b301ccf35648ace5698b76d51823e0b5_2_631x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/019488f5b301ccf35648ace5698b76d51823e0b5_2_946x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/019488f5b301ccf35648ace5698b76d51823e0b5.jpeg 2x" data-dominant-color="7F80A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1106×876 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7a743e6bae2602a7df12df79dbded3c6fa7c21c.png" data-download-href="/uploads/short-url/sudnBzukvPFHINATWDYHvdRHQvO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a743e6bae2602a7df12df79dbded3c6fa7c21c_2_637x500.png" alt="image" data-base62-sha1="sudnBzukvPFHINATWDYHvdRHQvO" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a743e6bae2602a7df12df79dbded3c6fa7c21c_2_637x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a743e6bae2602a7df12df79dbded3c6fa7c21c_2_955x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7a743e6bae2602a7df12df79dbded3c6fa7c21c.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1114×874 39.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-04-18 19:47 UTC)

<p>Where do these model files coming from? What coordinate system the point positions are defined in (what is the origin and axis directions)?</p>

---
