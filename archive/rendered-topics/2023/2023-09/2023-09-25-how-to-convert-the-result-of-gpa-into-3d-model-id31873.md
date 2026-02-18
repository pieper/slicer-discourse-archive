# How to convert the result of GPA into 3D model?

**Topic ID**: 31873
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/how-to-convert-the-result-of-gpa-into-3d-model/31873

---

## Post #1 by @zariliusra (2023-09-25 02:06 UTC)

<p>Hi, please give some advice. I’ve got the point cloud from the GPA module of SlicerMorph, but then get lost about how to turn it into a 3D model in vtk/stl/ply.</p>

---

## Post #2 by @muratmaga (2023-09-25 03:27 UTC)

<p>You need a reference model with the same set of landmarks, and GPA module will turn that into the mean shape of your study. usually the sample closest the mean is used as the reference. Then, you can use the interactive visualization tab of the GPA module, and switch to 3D model visualization</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4894c531e521c08797fa05f76e48aa0473b9b55d.jpeg" data-download-href="/uploads/short-url/am57eNNc2YYaTrMpVu8o4rUJkGF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4894c531e521c08797fa05f76e48aa0473b9b55d_2_690x233.jpeg" alt="image" data-base62-sha1="am57eNNc2YYaTrMpVu8o4rUJkGF" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4894c531e521c08797fa05f76e48aa0473b9b55d_2_690x233.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4894c531e521c08797fa05f76e48aa0473b9b55d_2_1035x349.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4894c531e521c08797fa05f76e48aa0473b9b55d_2_1380x466.jpeg 2x" data-dominant-color="B2B1CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3550×1202 645 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to export that as a new model, simply go to <code>Data</code> module, right-click on the <code>PCA_Warped Volume</code>  and choose <code>export to file</code>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc0d7f6f15fce1667499810e5ae91cf62262b5d5.png" data-download-href="/uploads/short-url/t78k12my4ouLfjN9sNNgvWyXEih.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc0d7f6f15fce1667499810e5ae91cf62262b5d5_2_689x367.png" alt="image" data-base62-sha1="t78k12my4ouLfjN9sNNgvWyXEih" width="689" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc0d7f6f15fce1667499810e5ae91cf62262b5d5_2_689x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc0d7f6f15fce1667499810e5ae91cf62262b5d5_2_1033x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc0d7f6f15fce1667499810e5ae91cf62262b5d5.png 2x" data-dominant-color="EEF1F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1374×732 91.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If your goal is to visualize the consensus (mean) shape, you should do this before touching any of the PC sliders, which will deform the model based on the PC coefficients.</p>

---

## Post #3 by @zariliusra (2023-09-25 12:20 UTC)

<p>Thank you very much, Prof. It works!</p>

---
