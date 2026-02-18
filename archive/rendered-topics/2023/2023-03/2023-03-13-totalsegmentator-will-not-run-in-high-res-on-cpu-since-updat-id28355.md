# TotalSegmentator will not run in High Res on CPU since updating to 5.2.2

**Topic ID**: 28355
**Date**: 2023-03-13
**URL**: https://discourse.slicer.org/t/totalsegmentator-will-not-run-in-high-res-on-cpu-since-updating-to-5-2-2/28355

---

## Post #1 by @Ds44 (2023-03-13 20:30 UTC)

<p>Hi all,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf72013709131f23e26b6162e2c76054a477ea8.png" alt="image" data-base62-sha1="dgpoebB2OFGDp2b0CBUDC8JZ1jy" width="676" height="132"></p>
<p>Since updating to 5.2.2, I have had trouble with TotalSegmenator. Currently, it will only segment in fast mode even if I click full resolution when prompted to choose. Before I updated it would segment in High Res if I selected with no issues.</p>
<p>Any ideas what the issue is?</p>
<p>Thanks,</p>
<p>David</p>

---

## Post #2 by @jamesobutler (2023-03-13 21:28 UTC)

<p>When running Total Segmentor for the first time was it successfully at downloading and installing PyTorch and the TotalSegmentor package? The specific issue you are observing appears to be the correct PyTorch version not being installed. The SlicerTotalSegmentor extension has some debugging techniques for this specific issue.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator#gpu-is-not-found">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator#gpu-is-not-found" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/bdbcd2ad81ff9aab5d2a6fb9507d02fd6b77afb1c0d57ff80598df13a6f2c04d/lassoan/SlicerTotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerTotalSegmentator#gpu-is-not-found" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body...</a></h3>

  <p>Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model - GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer usin...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Ds44 (2023-03-13 22:45 UTC)

<p>Hi, thanks for the reply.<br>
Yes, PyTorch and TotalSegmentator were installed successfully.<br>
I meant to include that I am running on CPU as I have integrated graphics so no gpu. I had some issues upgrading from 5.2.1 to 5.2.2. and I had to reinstall slicer and extensions. Since the upgrade, I I have had the issue. Before that, I had no issue getting a full res segmentation to run on my CPU in 45-50 minutes for the sample CT abdo panoramix dataset (the same one I am using now).</p>

---

## Post #4 by @richie (2023-04-07 18:17 UTC)

<p>hello,  i did a search and i get this.   But how exactly do I adjust the parameter.  Sorry if this is a newbie questions.    thanks</p>
<p>To adjust the threshold in TotalSegmenator, you can use the <code>similarity_threshold</code> parameter. This parameter controls the similarity threshold between two adjacent pixels to determine if they should be in the same segment or not.</p>
<p>By default, the similarity threshold is set to 20, which means that two pixels with a color difference of less than 20 will be considered part of the same segment. You can adjust this value to increase or decrease the segmentation detail.</p>

---
