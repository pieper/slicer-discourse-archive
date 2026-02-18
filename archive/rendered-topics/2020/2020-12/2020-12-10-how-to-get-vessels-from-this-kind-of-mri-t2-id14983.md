# How to get vessels from this kind of MRI T2

**Topic ID**: 14983
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/how-to-get-vessels-from-this-kind-of-mri-t2/14983

---

## Post #1 by @slicer365 (2020-12-10 11:15 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb51784ed2d68f4380f4fdb516bbcdfed97074e0.jpeg" alt="捕获" data-base62-sha1="xzIKKQVTHE2EJfGZReOpAbHNHEY" width="286" height="246"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11d4110a9d1ac0efe885fa0dc445402834a0fd6.jpeg" alt="捕获2" data-base62-sha1="yoZKjXxdCuTPS8VGsTGzYr6zb14" width="262" height="246"><br>
As you can see in this image, we can clearly see the many blood vessels inside, the black ones wrapped in white, I want to know how to get the black blood vessels from the white ones. I used a threshold, but it will calculate the other black brain tissue around it. Since we can distinguish blood vessels from images, there must be a way to segment them. Or is there a way to divide the white area and the black part in the white area?</p>

---

## Post #2 by @lassoan (2020-12-12 06:33 UTC)

<p>You can use Local threshold effect (provided by SegmentEditorExtraEffects extension), as it allows restricting thresholding into a single structure. You can define a box-shaped region of interest, intensity range, and minimum bridge diameter to prevent the vessel to be connected to other dark areas.</p>
<p>If you can share an example dataset (upload the anonymized data somewhere and post the link here) then we can give more specific advice.</p>

---

## Post #3 by @slicer365 (2020-12-13 00:15 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://wws.lanzous.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://wws.lanzous.com/iAtHcjb54od" target="_blank" rel="noopener nofollow ugc">wws.lanzous.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://wws.lanzous.com/iAtHcjb54od" target="_blank" rel="noopener nofollow ugc">T2 Data.rar - 蓝奏云</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This is the data，I hope u can help me test it ,get vessels from it.The black in white is vessel.</p>

---

## Post #4 by @chir.set (2020-12-13 08:18 UTC)

<p>Tried your data in vain, no usable result could be obtained. Intensities of blood vessels of the Willis circle do not distinguish much from surrounding structures. It’s segmenting vessels without contrast media. Specialized OEM software may perform better. Expert advice from Slicer devs may be of better help. Best would be to perform an object oriented CT scan with contrast. Good luck.</p>

---

## Post #5 by @lassoan (2020-12-13 20:37 UTC)

<p>Would it be enough to segment those parts of the vessels where it is surrounded by bright region? If that’s enough then the segmentation is feasible, but quite tedious.</p>
<p>Overview of steps:</p>
<ul>
<li>Use Cast Scalar Volume module to change the scalar type of the volume to <code>short</code>. Floating-point scalar type multiplies unnecessary extra memory need and computation time.</li>
<li>Use Crop Volume module to resample the volume to have isotropic spacing by enabling “isotropic spacing” option (and if you are interested in a smaller region then also crop)</li>
<li>Segment the bright regions by thresholding (1000 to maximum)</li>
<li>Fill internal holes by applying Margin effect in <code>grow</code> mode by 4mm, then shrink by 4mm back to the original region size</li>
<li>This segment will be used to limit further operations to dark regions that are enclosed in bright surroundings, so rename it to “mask”, hide it, and in masking section set: Editable area → mask, Modify other segments → Overwrite visible.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb251440f4254784270289fe3232ba1872f4448.jpeg" data-download-href="/uploads/short-url/fNgz2icWU53YASq1oEMhcpBMALC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb251440f4254784270289fe3232ba1872f4448_2_690x441.jpeg" alt="image" data-base62-sha1="fNgz2icWU53YASq1oEMhcpBMALC" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb251440f4254784270289fe3232ba1872f4448_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb251440f4254784270289fe3232ba1872f4448_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb251440f4254784270289fe3232ba1872f4448_2_1380x882.jpeg 2x" data-dominant-color="A1A3A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 476 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>Create two new segments: <code>vessels</code> and <code>other</code>
</li>
<li>Go to Paint effect, in masking section, enable <code>Editable intensity range</code> and set range to 0 to 600, to restrict painting to dark regions (where vessels are)</li>
<li>Paint scribbles in vessels that you want to segment in all three planes</li>
<li>Go to “Grow from seeds” effect, click “Initialize”, and just below that button click “Show 3D” button (next to “result” label)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b17f49d5c55243d44370ccdc92b2cb29bb59df.jpeg" data-download-href="/uploads/short-url/odaYFx4QgUB6sprBjajCZtV7Hht.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b17f49d5c55243d44370ccdc92b2cb29bb59df_2_690x418.jpeg" alt="image" data-base62-sha1="odaYFx4QgUB6sprBjajCZtV7Hht" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b17f49d5c55243d44370ccdc92b2cb29bb59df_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b17f49d5c55243d44370ccdc92b2cb29bb59df_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b17f49d5c55243d44370ccdc92b2cb29bb59df_2_1380x836.jpeg 2x" data-dominant-color="B3B2B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1367 518 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And this is where things start to become tedious: you need to keep painting scribbles with “vessel” segment inside vessels and “other” segment outside vessels, until you segmented all vessels of interest and excluded all other regions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7e161ae904d53401420ad35cacab13ba905935.jpeg" data-download-href="/uploads/short-url/hCsRN8bIV9HLfLvVIK9V2y6eAoB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b7e161ae904d53401420ad35cacab13ba905935_2_690x441.jpeg" alt="image" data-base62-sha1="hCsRN8bIV9HLfLvVIK9V2y6eAoB" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b7e161ae904d53401420ad35cacab13ba905935_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b7e161ae904d53401420ad35cacab13ba905935_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b7e161ae904d53401420ad35cacab13ba905935_2_1380x882.jpeg 2x" data-dominant-color="A4A7AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 618 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When you are finished, click Apply in “Grow from seeds effect” and hide the “other” segment. I’ve spent about 10 minutes with this and got this far:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9286a4ac61a2048f6a201bc6c49a3a19e22f0197.jpeg" data-download-href="/uploads/short-url/kUebjDW2tFUGRKbxc6ipL7rGiiP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9286a4ac61a2048f6a201bc6c49a3a19e22f0197_2_690x418.jpeg" alt="image" data-base62-sha1="kUebjDW2tFUGRKbxc6ipL7rGiiP" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9286a4ac61a2048f6a201bc6c49a3a19e22f0197_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9286a4ac61a2048f6a201bc6c49a3a19e22f0197_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9286a4ac61a2048f6a201bc6c49a3a19e22f0197_2_1380x836.jpeg 2x" data-dominant-color="A5A4A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1367 552 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you just want to segment specific vessels then this may be feasible, but to get a complete vessel tree would take so much time that it would not worth the effort. I agree with <a class="mention" href="/u/chir.set">@chir.set</a> that a scan with contrast material seems like a better approach, as it would provide full vessel tree and segmentation would not be so difficult.</p>

---

## Post #6 by @slicer365 (2020-12-14 11:55 UTC)

<p>Thank you ,professor,u provide me a good way ，Thank you very much!</p>

---
