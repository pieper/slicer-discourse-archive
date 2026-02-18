# Volume Model has Black box around it

**Topic ID**: 4054
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/volume-model-has-black-box-around-it/4054

---

## Post #1 by @Jay (2018-09-10 19:51 UTC)

<p>Operating system: Windows 7<br>
Slicer version:Nightly Build 2018-09-08<br>
Expected behavior: I’m trying to use the scissors and mask volume tools to erase the table a patient’s scan was taken on. I’m following this video: <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" rel="nofollow noopener">https://www.youtube.com/watch?v=xZwyW6SaoM4</a>. I would like my rendered volume to show just the sections of anatomy and not the black “background”<br>
Actual behavior: My rendered volume has a black box surrounding the anatomy of interest. I’m assuming it’s the empty space from the scan being rendered. How do I remove this? For instance, in the above video, the scan shows the head only being rendered.</p>

---

## Post #2 by @cpinter (2018-09-10 20:07 UTC)

<p>Are you saying that the volume appears as a black box in volume rendering?<br>
If yes, then you’ll probably need to change the preset and adjust the shift to get a proper 3D visualization of your volume. There are presets for different kinds of CTs and MRIs etc. What modality is your volume?</p>

---

## Post #3 by @Jay (2018-09-10 20:26 UTC)

<p>It’s a CT image. When I change over to CT-SoftTissue, the surrounding box turns grey instead of black. I’ve attached the image to help clarify<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a773b7509308a70c724bae509d533157a42002.png" data-download-href="/uploads/short-url/9WbI0hpqQPMRw3nB6ZcqVYei7jY.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a773b7509308a70c724bae509d533157a42002_2_650x500.png" alt="Untitled" data-base62-sha1="9WbI0hpqQPMRw3nB6ZcqVYei7jY" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a773b7509308a70c724bae509d533157a42002_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a773b7509308a70c724bae509d533157a42002.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a773b7509308a70c724bae509d533157a42002.png 2x" data-dominant-color="8688AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">671×516 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2018-09-10 20:42 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="4054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>adjust the shift</p>
</blockquote>
</aside>
<p>Have you tried this?</p>

---

## Post #5 by @Jay (2018-09-11 11:43 UTC)

<p>Yes. Adjusting the shift enough to remove it removes some of the soft tissue I’m after as well</p>
<p>This is my original preset and shift<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0a429a7d60fcfad88f7f925b06e1515d665763a.jpeg" data-download-href="/uploads/short-url/pcDKBUEzKj84hkZkKjRgKygYlDk.jpeg?dl=1" title="%231" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0a429a7d60fcfad88f7f925b06e1515d665763a_2_636x500.jpeg" alt="%231" data-base62-sha1="pcDKBUEzKj84hkZkKjRgKygYlDk" width="636" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0a429a7d60fcfad88f7f925b06e1515d665763a_2_636x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0a429a7d60fcfad88f7f925b06e1515d665763a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0a429a7d60fcfad88f7f925b06e1515d665763a.jpeg 2x" data-dominant-color="898BB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%231</span><span class="informations">670×526 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I’m happy with this as a starting point and there is nothing surrounding it. But I want to try to remove the table before moving on to tougher segmentation is when I get the gray box all of a sudden<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b14a78f01317b03209de779a1d0e5a16ec0f82d9.jpeg" data-download-href="/uploads/short-url/pio4g07XuegGba5VXIfWWW7zUP7.jpeg?dl=1" title="%232" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b14a78f01317b03209de779a1d0e5a16ec0f82d9_2_649x500.jpeg" alt="%232" data-base62-sha1="pio4g07XuegGba5VXIfWWW7zUP7" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b14a78f01317b03209de779a1d0e5a16ec0f82d9_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b14a78f01317b03209de779a1d0e5a16ec0f82d9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b14a78f01317b03209de779a1d0e5a16ec0f82d9.jpeg 2x" data-dominant-color="757686"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%232</span><span class="informations">674×519 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is the same volume with the same preset just after the scissors and masking tool. I’m not sure what other approaches to use to easily crop out</p>

---

## Post #6 by @cpinter (2018-09-11 12:42 UTC)

<p>You probably mask to the value of 0, which for a CT basically means water. You need to mask it to be -1000, which is more or less air.</p>

---

## Post #7 by @Jay (2018-09-11 13:55 UTC)

<p>You’re right; changing this masking value was my oversight. Thank you Mr. Pinter!</p>

---
