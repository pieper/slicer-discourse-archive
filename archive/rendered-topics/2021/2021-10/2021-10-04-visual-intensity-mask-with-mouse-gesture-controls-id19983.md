# Visual intensity mask with mouse gesture controls

**Topic ID**: 19983
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/visual-intensity-mask-with-mouse-gesture-controls/19983

---

## Post #1 by @joachim (2021-10-04 09:08 UTC)

<p>The intensity mask can be a useful feature when doing manual segmentation, especially for the <em>Draw</em> and <em>Erase</em> tool:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00db80511e0052ad9a81abad5f5835cda809576d.png" alt="intensitymask" data-base62-sha1="7Ahjn2ggK0N57x3iHieyAuacI5" width="437" height="115"></p>
<p>But in practice it is cumbersome: I have to look at values in <em>Data probe</em> and use this as a setting. I suggest a visual representation when intensity mask is on:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9bb310485abb268d6a60ce60618a8a6870f74df.png" data-download-href="/uploads/short-url/qv3o39ZKEJlXgQTXLbOsDD13O9h.png?dl=1" title="intensity" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9bb310485abb268d6a60ce60618a8a6870f74df_2_517x315.png" alt="intensity" data-base62-sha1="qv3o39ZKEJlXgQTXLbOsDD13O9h" width="517" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9bb310485abb268d6a60ce60618a8a6870f74df_2_517x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9bb310485abb268d6a60ce60618a8a6870f74df_2_775x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9bb310485abb268d6a60ce60618a8a6870f74df_2_1034x630.png 2x" data-dominant-color="5F5E5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">intensity</span><span class="informations">1973×1203 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This makes it easy to fill out contours in an efficent way since you can see if your intensity mask setting is good.</p>
<p>While a visual intensity mask will make these tools better, you will still have to set your intensity mask values in the toolbar. Therefore I suggest the following mouse gestures in a slice view window when intensity mask is on:</p>
<ul>
<li><strong>Ctrl</strong> + <strong>Left Drag</strong> : Change intensity mask minimum value. Update visual mask continuously. Keep tool cursor at same place so you can continue draw when you find your correct setting.</li>
<li><strong>Ctrl</strong> + <strong>Shift</strong> + <strong>Left Drag</strong> : Same as above but with fine precision increments like 1/10th of the above . This is how Blender does it.</li>
</ul>
<p>Is this a feature that can be added to Slicer? I would love this feature since manual segmentation is a craftmanship that can be exhausting.</p>

---

## Post #2 by @lassoan (2021-10-04 12:35 UTC)

<p>The preview is available in Threshold effect. You can also draw on the image to compute image intensity histogram of that region and specify the threshold range based on that histogram (either using min/mean/max values or by click-and-dragging the position markers in the histogram):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6363bf7681cb707ca8426eb8413e65e715b0840.jpeg" data-download-href="/uploads/short-url/pZV5WQmOer5kB7RlWIviDR53ECk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6363bf7681cb707ca8426eb8413e65e715b0840_2_607x500.jpeg" alt="image" data-base62-sha1="pZV5WQmOer5kB7RlWIviDR53ECk" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6363bf7681cb707ca8426eb8413e65e715b0840_2_607x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6363bf7681cb707ca8426eb8413e65e715b0840_2_910x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6363bf7681cb707ca8426eb8413e65e715b0840_2_1214x1000.jpeg 2x" data-dominant-color="4C514A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1580×1301 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the end, click “Use for masking” to set the range as “Editable intensity range”.</p>
<p>Is there any need that is not covered by these features?</p>

---

## Post #3 by @joachim (2021-10-04 13:13 UTC)

<p>Local histogram is a nice feature. But it is still cumbersome to set the intensity mask values by hand. I would really appreciate the above suggested feature. This way you can change the intensity mask value on the fly, adjusting it to your needs while you draw manually. Segmentation is a time consuming process especially if you need to take special care of the small details. An effective UI design with handy shortcuts really helps.</p>

---

## Post #4 by @lassoan (2021-10-04 14:05 UTC)

<p>I can see how a preview of a thresholded paint stroke could look nice and it would make intensity range adjustment easier. However, implementation workload of this feature would be significant and its use for medical image segmentation would be quite limited. The reason for limited use is that threshold value should not be adjusted for individual paint strokes, and not even for slices, because that would result in inconsistent (dependent on slice orientation, display settings, operator, etc.) and noisy segmentation (due to neighbor slices being segmented independently). Instead, there are two main approaches that are typically followed:</p>
<ul>
<li>If there is a good global threshold value for an entire structure then use Threshold effect (with a few extra clicks, reproducible threshold value setting, for example as a mid-point between two histogram peaks) to determine that threshold value and use that consistently throughout the segmentation.</li>
<li>If there is no threshold that works well across the entire structure then the solution is not to manually alter the threshold, but let “Grow from seeds” (or Watershed, Fast marching, etc.) method determine the optimal threshold value for each voxel, in 3D, based on the inputs you give and all the local intensity variations of the underlying image.</li>
</ul>
<p>What structures are you segmenting on what kind of images?<br>
How do you segment them now?</p>

---

## Post #5 by @joachim (2021-10-06 08:59 UTC)

<p>I can see that implementing this feature could be time consuming. This was just a suggestion for something I would find handy.</p>
<p>The problem with interpolation between layers could be a problem. But manual drawing is worse. Manual drawing often creates a mesh looking like stairs. Drawing with an intensity mask (manually between slices (or sphere brush?)) will probably create a smoother interpolation just like thresholding.</p>
<p>I’ve been working with models of congenital heart diseases where the CT images of the small patients often are diffuse because of radiation concerns for children. This often creates the need for manual post drawing. I also been segmenting orbita fractures where the details often must be enhanced with manual drawing (<a href="https://discourse.slicer.org/t/enhancing-orbital-walls-with-unsharp-mask-filtering/8440/9">I know about this post</a>). I often find it easier/effective to go through the segmentation slice by slice to fix it. Here is how I would use my suggested effect for orbitas (pink color to clearify):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6599ffdfd65151bf8d3adfb96e868638f24e3552.png" data-download-href="/uploads/short-url/euOalJ0cenYeOtBkM9Z6UodiweK.png?dl=1" title="segmentintensity" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6599ffdfd65151bf8d3adfb96e868638f24e3552.png" alt="segmentintensity" data-base62-sha1="euOalJ0cenYeOtBkM9Z6UodiweK" width="690" height="398" data-dominant-color="4F524E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentintensity</span><span class="informations">1968×1137 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-10-06 12:26 UTC)

<aside class="quote no-group" data-username="joachim" data-post="5" data-topic="19983">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Manual drawing often creates a mesh looking like stairs. Drawing with an intensity mask (manually between slices (or sphere brush?)) will probably create a smoother interpolation just like thresholding.</p>
</blockquote>
</aside>
<p>Exactly! You must work with the same threshold value across the entire structure (not change the threshold value slice by slice) if you want to avoid staircasing. This is why a tool that would make it easy to change the threshold value between slices based on visual feedback would not be useful (because it would introduce staircasing). You can set an editable intensity range and then use Paint with a large sphere brush, or use Scissors or Surface cut to quickly segment your region of interest, then disable thresholding and go slice by slice to fix small errors.</p>
<p>If a single global threshold value does not work well then “Grow from seeds” effect is more appropriate, as it relies on local intensity changes in 3D (not just slice by slice).</p>
<p>If you segment very thin structures (orbital wall, heart valve leaflets or septum) then due to partial volume effect and noise the structure may disappear (become indistinguishable from the surrounding tissue). In these cases it can be easier to segment the cavity or the structures on both sides of the membrane and then create the thin boundary structure using Hollow effect.</p>

---
