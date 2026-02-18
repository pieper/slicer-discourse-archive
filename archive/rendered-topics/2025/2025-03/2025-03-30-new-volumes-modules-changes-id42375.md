# New volumes modules changes

**Topic ID**: 42375
**Date**: 2025-03-30
**URL**: https://discourse.slicer.org/t/new-volumes-modules-changes/42375

---

## Post #1 by @muratmaga (2025-03-30 20:10 UTC)

<p>With the new changes introduced to the <code>Volumes</code> module that allow to invert the LUT, and map the selected LUT to historgram, I am finding making 3D renderings in the Slicer became much easier and faster.</p>
<p>I start with the Synchronize to Volumes option, prepare my baseline visualization, and then uncheck it to make make tweaks to the transfer function. I find this easier to obtain good results and trying to create from scratch or use begin with one of the presets for my datasets. I also like the ability to see the histogram with the color ramp in the Volumes, which was lacking in the Volume Rendering.</p>
<p>If you are not aware of it, this is what Volumes module look like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e02934181ba61eca2ad1563efc9cd23ce05ad77.jpeg" data-download-href="/uploads/short-url/1ZWcwmajjbcOhXyiura86Me9uN9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e02934181ba61eca2ad1563efc9cd23ce05ad77_2_446x500.jpeg" alt="image" data-base62-sha1="1ZWcwmajjbcOhXyiura86Me9uN9" width="446" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e02934181ba61eca2ad1563efc9cd23ce05ad77_2_446x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e02934181ba61eca2ad1563efc9cd23ce05ad77_2_669x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e02934181ba61eca2ad1563efc9cd23ce05ad77_2_892x1000.jpeg 2x" data-dominant-color="CCCBD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">931×1043 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The only issue I have found so far with the changes that Color Legend is not visible in the 3D view (even if it is explicitly specified. It works fine in 2D views).</p>
<p>Coupled with Shadows feature (and with Slicermorph’s HiResScreenCapture), I think the results are pretty good.</p>
<p>Thanks again for everyone making these features available. <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/oothomas">@oothomas</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30d711feca8a3c180faf4e68843641a2396bd9ac.jpeg" data-download-href="/uploads/short-url/6Y3HGkIDE9Owz5jeTGkfhOEtEVC.jpeg?dl=1" title="bee" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30d711feca8a3c180faf4e68843641a2396bd9ac_2_612x500.jpeg" alt="bee" data-base62-sha1="6Y3HGkIDE9Owz5jeTGkfhOEtEVC" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30d711feca8a3c180faf4e68843641a2396bd9ac_2_612x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30d711feca8a3c180faf4e68843641a2396bd9ac_2_918x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30d711feca8a3c180faf4e68843641a2396bd9ac_2_1224x1000.jpeg 2x" data-dominant-color="330E05"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bee</span><span class="informations">1920×1567 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(ok looks like Discourse downsampling rendering for some reason, when I drag and drop. You can find the full resolution here: <a href="https://github.com/muratmaga/random_things/blob/main/bee.png" class="inline-onebox" rel="noopener nofollow ugc">random_things/bee.png at main · muratmaga/random_things · GitHub</a>. It should be 4348x3548)</p>

---

## Post #2 by @muratmaga (2025-04-01 03:50 UTC)

<p>It also made making striking animations easier as well:</p>          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://raw.githubusercontent.com/muratmaga/random_things/refs/heads/main/bee_movie.mp4">
              <a href="https://raw.githubusercontent.com/muratmaga/random_things/refs/heads/main/bee_movie.mp4" rel="noopener nofollow ugc">https://raw.githubusercontent.com/muratmaga/random_things/refs/heads/main/bee_movie.mp4</a>
            </video>
          </div>


---

## Post #3 by @pieper (2025-04-01 12:50 UTC)

<p>Nice movie!  It doesn’t play in the browser for me unfortunately but I could download and play it locally.</p>
<p>Here’s an H.264 version in case that works better for anyone.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/16tPRlNnY1cA_0Z-woRn-NwCx2YFEGrJR/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/16tPRlNnY1cA_0Z-woRn-NwCx2YFEGrJR/view?usp=sharing" target="_blank" rel="noopener">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/16tPRlNnY1cA_0Z-woRn-NwCx2YFEGrJR/view?usp=sharing" target="_blank" rel="noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/16tPRlNnY1cA_0Z-woRn-NwCx2YFEGrJR/view?usp=sharing" target="_blank" rel="noopener">bee_movie-H.264.mov</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
