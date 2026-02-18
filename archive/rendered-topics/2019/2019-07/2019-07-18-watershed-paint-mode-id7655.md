# Watershed paint mode

**Topic ID**: 7655
**Date**: 2019-07-18
**URL**: https://discourse.slicer.org/t/watershed-paint-mode/7655

---

## Post #1 by @the3dslicerdude (2019-07-18 12:13 UTC)

<p>Hi everyone</p>
<p>I noticed a feature in another software where it seems as though they use watershed filters to speed up the painting process. If that’s not already a feature, I definitely think it would be a time saver.</p>
<p>I apologize if I got the terms wrong since I’m quite new to 3d segmentation.</p>
<aside class="onebox twitterstatus">
  <header class="source">
      <a href="https://twitter.com/OrsDragonfly3D/status/1105571703604822016" target="_blank" rel="nofollow noopener">twitter.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://pbs.twimg.com/tweet_video_thumb/D1fHeRAWoAcCKmG.jpg" class="thumbnail onebox-avatar" width="60" height="60">
<h4>
  <a href="https://twitter.com/OrsDragonfly3D/status/1105571703604822016" target="_blank" rel="nofollow noopener">
    ORS Dragonfly Software (OrsDragonfly3D)
  </a>
</h4>

<div class="tweet">Smart grid in Dragonfly. You can paint really fast! https://t.co/HwG2417hia
</div>

<div class="date">
  <a href="https://twitter.com/OrsDragonfly3D/status/1105571703604822016" target="_blank" rel="nofollow noopener">1:50 PM - 12 Mar 2019</a>
    <span class="like">
      <svg viewbox="0 0 512 512" width="14px" height="16px" aria-hidden="true">
        <path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"></path>
      </svg> 13
    </span>
    <span class="retweet">
      <svg viewbox="0 0 640 512" width="14px" height="16px" aria-hidden="true">
        <path d="M629.657 343.598L528.971 444.284c-9.373 9.372-24.568 9.372-33.941 0L394.343 343.598c-9.373-9.373-9.373-24.569 0-33.941l10.823-10.823c9.562-9.562 25.133-9.34 34.419.492L480 342.118V160H292.451a24.005 24.005 0 0 1-16.971-7.029l-16-16C244.361 121.851 255.069 96 276.451 96H520c13.255 0 24 10.745 24 24v222.118l40.416-42.792c9.285-9.831 24.856-10.054 34.419-.492l10.823 10.823c9.372 9.372 9.372 24.569-.001 33.941zm-265.138 15.431A23.999 23.999 0 0 0 347.548 352H160V169.881l40.416 42.792c9.286 9.831 24.856 10.054 34.419.491l10.822-10.822c9.373-9.373 9.373-24.569 0-33.941L144.971 67.716c-9.373-9.373-24.569-9.373-33.941 0L10.343 168.402c-9.373 9.373-9.373 24.569 0 33.941l10.822 10.822c9.562 9.562 25.133 9.34 34.419-.491L96 169.881V392c0 13.255 10.745 24 24 24h243.549c21.382 0 32.09-25.851 16.971-40.971l-16.001-16z"></path>
      </svg> 3
    </span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2019-07-18 14:04 UTC)

<p>I agree that it looks cool, so I’ve reproduced something like this with the <a href="https://www.insight-journal.org/browse/publication/92">Watershed algorithm that Slicer uses</a>). The result was completely disappointing. The method is useless, especially for segmenting in 3D.</p>
<p>Issues:</p>
<ol>
<li>
<p>In 3D, you cannot make good decisions about which cell to add/remove by looking at a single slice. You need to inspect each cell in 3D, in orthogonal slices, to decide if it should be added or not. This would require several seconds for each cell.</p>
</li>
<li>
<p>With large cell sizes you cannot segment accurately. You can see in their demo video that even in 2D the cells are often too coarse and you cannot separate structures that normally would be trivial to segment (e.g., using Grow from seeds or Watershed effects in Slicer). With small sizes, it becomes tedious to fill in the entire structure.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa6e9f0b8ac4748660604ed57b71511b3af9a35.jpeg" data-download-href="/uploads/short-url/yc3J3jcuV9DPSQ6QeoIbjMiCqj3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa6e9f0b8ac4748660604ed57b71511b3af9a35_2_560x500.jpeg" alt="image" data-base62-sha1="yc3J3jcuV9DPSQ6QeoIbjMiCqj3" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa6e9f0b8ac4748660604ed57b71511b3af9a35_2_560x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa6e9f0b8ac4748660604ed57b71511b3af9a35.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa6e9f0b8ac4748660604ed57b71511b3af9a35.jpeg 2x" data-dominant-color="92909C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">596×532 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2403f4cda1931f3e00e41bb728fb83ad51b94e28.jpeg" alt="image" data-base62-sha1="58BFeZn29mlaVAsfTeggVl2abLG" width="528" height="435"></p>
<ol start="3">
<li>In 3D, you need to review and fill in <em>every slice</em>. You cannot skip slices, as most often neighbor slices have a number of holes that you need to review and fill in. In the best case, when segmenting a very simple shape on a single slice at unrealistically low resolution takes 10 seconds (see demo video), but with more realistic shape and resolution it would probably take half minute or a minute. Segmentation of a single structure that spans 50-100 slices could take an hour or so. The same structure would be segmented in a few minutes using tools in Slicer (assuming the structure has reasonable contrast, which is a requirement for the demoed tool).</li>
</ol>
<p>I can imagine that there are very few special cases when the tool shown in the demo may be usable, but it would be impractical for most segmentation problems. Therefore, I do not think it is worth the time to implement and maintain such segmentation tool in Slicer.</p>

---
