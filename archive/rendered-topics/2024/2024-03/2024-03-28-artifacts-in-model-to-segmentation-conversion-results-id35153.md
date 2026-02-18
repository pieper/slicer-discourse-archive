# Artifacts in model to segmentation conversion results

**Topic ID**: 35153
**Date**: 2024-03-28
**URL**: https://discourse.slicer.org/t/artifacts-in-model-to-segmentation-conversion-results/35153

---

## Post #1 by @Chuan (2024-03-28 13:58 UTC)

<p>Dear community,</p>
<p>I would like to report a problem which occurs when I convert my stl model to segmentation node in 3D slicer.<br>
Basically, what I have is a stl model, as shown in figure1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c0aae989c922789dc0a4aceca53ce73ceed6b9.png" data-download-href="/uploads/short-url/pvjMfuMAxR1CjF8sqcrMfDCFiXL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0aae989c922789dc0a4aceca53ce73ceed6b9_2_440x500.png" alt="image" data-base62-sha1="pvjMfuMAxR1CjF8sqcrMfDCFiXL" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0aae989c922789dc0a4aceca53ce73ceed6b9_2_440x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0aae989c922789dc0a4aceca53ce73ceed6b9_2_660x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0aae989c922789dc0a4aceca53ce73ceed6b9_2_880x1000.png 2x" data-dominant-color="9C9DC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1041×1181 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But when I convert this model to segmentation node in 3D slicer, you can see some extra lines occur in my segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8b72e14d77803097e43dd493ccbd757fb4e9c4d.png" data-download-href="/uploads/short-url/qm4jAnfS4GWoUDmFy9co0PAsXTf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8b72e14d77803097e43dd493ccbd757fb4e9c4d.png" alt="image" data-base62-sha1="qm4jAnfS4GWoUDmFy9co0PAsXTf" width="460" height="500" data-dominant-color="0A0602"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">494×536 4.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This will bring extra voxel (extra lines) in the future segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15033264035dd2d87624be766e25eac6950b538.png" data-download-href="/uploads/short-url/yqKTEC5F7O4dJ0wbixnfbrRBgc8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15033264035dd2d87624be766e25eac6950b538_2_399x500.png" alt="image" data-base62-sha1="yqKTEC5F7O4dJ0wbixnfbrRBgc8" width="399" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15033264035dd2d87624be766e25eac6950b538_2_399x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15033264035dd2d87624be766e25eac6950b538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15033264035dd2d87624be766e25eac6950b538.png 2x" data-dominant-color="9D9CC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">578×724 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried with version 4.10, 5.02, and 5.22. All of them has this problem.<br>
Does anyone also meet the similar problem before? I suspect there’s a bug in 3D Slicer.<br>
Welcome any kinds of discussion in advance!</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #2 by @pieper (2024-03-28 14:49 UTC)

<p>This kind of issue can happen when there are small triangles or other issues.  You can try increasing the resolution of the segmentation grid or slightly rotating and hardening the model before converting.</p>

---

## Post #3 by @Chuan (2024-03-31 11:08 UTC)

<p>Hi Pieper,</p>
<p>Thanks for your reply, do you know how to increase the resolution of the segmentation?</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #4 by @pieper (2024-03-31 15:42 UTC)

<p>You can change the geometry in the module:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options</a></p>

---

## Post #5 by @Chuan (2024-04-02 08:54 UTC)

<p>Hi Pieper,</p>
<p>Thanks, I have two follow-up questions. I tried to change the spacing here. But I am not sure which one I should change: the stl geo file or the segmentation node file after conversion?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89fbd1e06eef5f44fb2ad7a5e5a4c2fd057d6284.png" data-download-href="/uploads/short-url/jGEVXWXAVJZ9HJQmerPqPWrELIM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89fbd1e06eef5f44fb2ad7a5e5a4c2fd057d6284_2_690x309.png" alt="image" data-base62-sha1="jGEVXWXAVJZ9HJQmerPqPWrELIM" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89fbd1e06eef5f44fb2ad7a5e5a4c2fd057d6284_2_690x309.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89fbd1e06eef5f44fb2ad7a5e5a4c2fd057d6284.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89fbd1e06eef5f44fb2ad7a5e5a4c2fd057d6284.png 2x" data-dominant-color="E1E4E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">998×448 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried both, but unfortunately it didn’t solve my problem.<br>
I manually changed the spacing of the STL from 1mm to 0.5mm.<br>
Then I click ‘OK’, it showed one error ‘Source volume is not set as either the foreground or background’, and I got a blank output.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8070fbff2b3b8189e98cfaf8418618edbc6fca06.png" alt="image" data-base62-sha1="ikfbpFy9AmKKAC4nXVNNOfas6JE" width="501" height="347"><br>
Then I changed the oversampling factor from 1 to 1.5, 2 for the segmentation node.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bde650bf1fc18c96c7b28f76b9d0cce24d9005e7.png" alt="image" data-base62-sha1="r5VGNY4UKs9Mda8wXzgqeGgHkDZ" width="494" height="419"></p>
<p>But in the output I can still see those additional bars…<br>
Is my operation what you suggested? I am not sure if I did something wrong in this step.</p>
<p>Best regards,<br>
Siyuan</p>

---

## Post #6 by @pieper (2024-04-02 17:48 UTC)

<p>Hi -</p>
<p>Yes, you select the segmentation node and choose a higher resolution.  You may still get artifacts due to degenerate triangles on the input.  You may want to try different options in the SurfaceToolbox to clean up the mesh, or as I mentioned earlier it might help to slightly rotate the model with a transform (then harden it) and try rasterizing.  You can also inspect the model in the area where the conversion artifacts are, e.g. by turning on the edge visibility to see what’s going on.  In the worst case you might just manually clean up the artifacts with the segment editor.</p>

---

## Post #7 by @lassoan (2024-04-02 18:09 UTC)

<p>The bars are due to the input mesh is not watertight (there are some open, non-manifold, or intersecting surfaces).</p>
<p>Even if the input surfaces are not watertight, if all the model/slice intersections on axial slices are closed then you may avoid the bars (that’s why <a class="mention" href="/u/pieper">@pieper</a> suggested rotating your model). It may worth spending a little time with changing the orientation slightly, or by doing 90 degree rotations around various axes.</p>
<p>However, if that does not help then you need to either get watertight models or you can remove the bars manually in Segment Editor (e.g., using Scissors effect).</p>

---

## Post #8 by @dave3d (2024-04-02 19:14 UTC)

<p>If you pass your mesh through VTK’s cleanPolyData filter that ought to fix the degenerate triangles.  Here’s the documentation for the class:</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkCleanPolyData.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkCleanPolyData.html</a></p>

---
