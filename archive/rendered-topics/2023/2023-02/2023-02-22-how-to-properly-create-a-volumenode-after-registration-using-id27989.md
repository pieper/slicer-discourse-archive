---
topic_id: 27989
title: "How To Properly Create A Volumenode After Registration Using"
date: 2023-02-22
url: https://discourse.slicer.org/t/27989
---

# How to properly create a volumeNode after registration using SITK ?

**Topic ID**: 27989
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/how-to-properly-create-a-volumenode-after-registration-using-sitk/27989

---

## Post #1 by @Mwoon (2023-02-22 22:30 UTC)

<p>The question is basic, but I don’t know what is failing.<br>
Here is the code :</p>
<pre><code class="lang-auto">resampled = sitk.Resample(moving_image, fixed_image, final_transform, sitk.sitkLinear, 0.0, moving_image.GetPixelID())
volume = self.sitk_to_vtk(resampled)
self.transfer_volume_metadate(volume, volume)
self.add_volume(volume)

    def transfer_volume_metadate(self, original_volume, moved_volume) -&gt; None:
        spacing =  original_volume.GetSpacing()
        origin =  original_volume.GetOrigin()
        ijk_to_ras_direction_matrix = vtk.vtkMatrix4x4()
        original_volume.GetIJKToRASDirectionMatrix(ijk_to_ras_direction_matrix)

        # Apply the metadata to the target volume.
        moved_volume.SetSpacing(spacing)
        moved_volume.SetOrigin(origin)
        moved_volume.SetIJKToRASDirectionMatrix(ijk_to_ras_direction_matrix)

    def add_volume(self, volume) -&gt; None:
        volume.SetName(self.volume_name_edit.text)
        mrmlScene.AddNode(volume)
        slicer.util.setSliceViewerLayers(volume, fit=True)
</code></pre>
<p>Here is what I obtain with those parameters :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecef19489b65c1c15e0ae91eceb302109dc51e0d.jpeg" data-download-href="/uploads/short-url/xO0WSTJKTHyKz5N1I4GJpvLlnDn.jpeg?dl=1" title="first_registration.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecef19489b65c1c15e0ae91eceb302109dc51e0d_2_690x243.jpeg" alt="first_registration.PNG" data-base62-sha1="xO0WSTJKTHyKz5N1I4GJpvLlnDn" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecef19489b65c1c15e0ae91eceb302109dc51e0d_2_690x243.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecef19489b65c1c15e0ae91eceb302109dc51e0d_2_1035x364.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecef19489b65c1c15e0ae91eceb302109dc51e0d_2_1380x486.jpeg 2x" data-dominant-color="888786"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">first_registration.PNG</span><span class="informations">1895×668 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The stopping condition is :</p>
<pre><code class="lang-auto">Optimizer stop condition: GradientDescentOptimizerv4Template: Convergence checker passed at iteration 38.
 Iteration: 38
 Metric value: -0.40111932866211414
</code></pre>
<p>If I change in the function transfer_metadata the first parameter by fixedImageData, I obtain something more coherent<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/877dafef05b1be08780bb1cc766c002c9e1f5701.jpeg" data-download-href="/uploads/short-url/jkBK0WQHYESRqgguVAEpInlFiFz.jpeg?dl=1" title="second_registration.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877dafef05b1be08780bb1cc766c002c9e1f5701_2_690x238.jpeg" alt="second_registration.PNG" data-base62-sha1="jkBK0WQHYESRqgguVAEpInlFiFz" width="690" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877dafef05b1be08780bb1cc766c002c9e1f5701_2_690x238.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877dafef05b1be08780bb1cc766c002c9e1f5701_2_1035x357.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877dafef05b1be08780bb1cc766c002c9e1f5701_2_1380x476.jpeg 2x" data-dominant-color="868685"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">second_registration.PNG</span><span class="informations">1903×658 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a5b4b5e741d6b16a49ad50d2dbc8a291f4b70b7.jpeg" data-download-href="/uploads/short-url/aBMVFD1Enw9xlFV2oMfl0M8AKh1.jpeg?dl=1" title="second_registration_with_fixed_image.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a5b4b5e741d6b16a49ad50d2dbc8a291f4b70b7_2_690x249.jpeg" alt="second_registration_with_fixed_image.PNG" data-base62-sha1="aBMVFD1Enw9xlFV2oMfl0M8AKh1" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a5b4b5e741d6b16a49ad50d2dbc8a291f4b70b7_2_690x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a5b4b5e741d6b16a49ad50d2dbc8a291f4b70b7_2_1035x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a5b4b5e741d6b16a49ad50d2dbc8a291f4b70b7_2_1380x498.jpeg 2x" data-dominant-color="8B8B8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">second_registration_with_fixed_image.PNG</span><span class="informations">1920×695 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">Optimizer stop condition: GradientDescentOptimizerv4Template: Convergence checker passed at iteration 72.
 Iteration: 72
 Metric value: -0.40737172935316895
</code></pre>
<p>Well, I don’t know which one is the correct way to construct the final registered volume, and from the registration something is happening, it stops before 100 steps.<br>
Any kind heart to help me with this ?</p>

---
