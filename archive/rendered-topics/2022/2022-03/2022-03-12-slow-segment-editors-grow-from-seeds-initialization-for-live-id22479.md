# slow segment-editor's grow-from-seeds initialization for liver segmentation

**Topic ID**: 22479
**Date**: 2022-03-12
**URL**: https://discourse.slicer.org/t/slow-segment-editors-grow-from-seeds-initialization-for-liver-segmentation/22479

---

## Post #1 by @hju (2022-03-12 22:08 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.13.0-2021-12-21, 4.11.20210226<br>
Expected behavior: faster performance<br>
Actual behavior:<br>
I’m trying to use Segment Editor’s Grow-From-Seeds to segment liver on abdominal CT. I found the initialization step can take 4-5min, for both stable and preview release Windows versions, which is longer than I expected. I saw it took around 1 min when others doing similar operations on similar images on <strong>Linux</strong>.</p>
<p>Could you test it on your side if you have access to a Windows machine? Is the grow-from-seeds always slower with Windows version? Any tips to improve the performance? Thanks!</p>
<p>I recorded a short video to show what I did</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1XguFomtvGMqvZanI5-q2PKBagBZH3pGl/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1XguFomtvGMqvZanI5-q2PKBagBZH3pGl/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1XguFomtvGMqvZanI5-q2PKBagBZH3pGl/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1XguFomtvGMqvZanI5-q2PKBagBZH3pGl/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">slicer-20220312_105538-Meeting Recording.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The image I used in the video</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1Y2ZOU9rFMhyZ4_jKWJ2oIPIuqCC6ndYX/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1Y2ZOU9rFMhyZ4_jKWJ2oIPIuqCC6ndYX/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1Y2ZOU9rFMhyZ4_jKWJ2oIPIuqCC6ndYX/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1Y2ZOU9rFMhyZ4_jKWJ2oIPIuqCC6ndYX/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">liver_102.nii.gz</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2022-03-12 23:28 UTC)

<p>I was able to reproduce the slow (4-minute) “Grow from seeds” initialization on this image. <strong>By somewhat optimizing the image for liver segmentation, I reduced the computation time to 5 seconds!</strong></p>
<ul>
<li>This image has “float” voxels, which makes computation slower. <strong>Use the “Cast scalar volume” to convert it to “short” type</strong>. CT images are usually are natively stored in “short” voxel type, so no information is lost - if any - should be negligible.</li>
<li>The image is fairly high resolution (0.7mm voxel size). This resolution is important for segmenting small and thin structures, but unnecessary for a large, bulky structure such as the liver. <strong>Use Crop volume module to crop the the image size to the minimum necessary size (about 1cm margin around the liver) to save memory, set Spacing scale to 2.0x (or even 3.0x), and enable “Isotropic spacing”</strong> (this image is already close to isotropic, but since we resample it anyway, we can easily make it completely isotropic).</li>
</ul>

---

## Post #3 by @hju (2022-03-13 23:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot!<br>
It works for me! Around 5 seconds!</p>
<p>One question: Does painting more seeds always lead to slower <code>initialization</code>?</p>

---

## Post #4 by @lassoan (2022-03-14 02:30 UTC)

<p>Amount of seeds does not matter, just the bounding box of the painted regions. Grow from seeds only fills within the region where the seeds are defined in (extended by some margin) and the larger the region the longer the computation takes.</p>

---

## Post #5 by @hju (2022-03-14 02:46 UTC)

<p>Many thanks! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
