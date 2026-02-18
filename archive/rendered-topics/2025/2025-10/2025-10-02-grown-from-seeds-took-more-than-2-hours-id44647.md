# Grown from seeds took more than 2 hours

**Topic ID**: 44647
**Date**: 2025-10-02
**URL**: https://discourse.slicer.org/t/grown-from-seeds-took-more-than-2-hours/44647

---

## Post #1 by @JaredAmudeo (2025-10-02 06:31 UTC)

<p>I work with high-resolution micro-CT scans of fossils, obtained with Skyscan 1272 and 1273 micro-CTs. Since the data comes as stacks of .png images, I use the <strong>Slice Morph</strong> extension to load them. Because of the condition of the fossils and the large number of elements I need to segment for later reconstruction in other software, I mainly use the <strong>“Grow from seeds”</strong> tool. It gives very good results and saves me a lot of time.</p>
<p>Performance has become extremely slow, even though I upgraded my setup. Normally, the scans I work with range from about 200 MB up to ~3.5 GB. At first, the initial segments only took about 2 minutes, but now the last one I did took more than 2 hours just for “Grow from seeds” to finish.</p>
<p>During those hours, I noticed that RAM usage went up to a maximum of ~55 GB. I also monitored CPU activity with Process Lasso and saw that cores 0, 9, and 11 had the highest load (around 20% each on average), while the others (1–8, 10, 12–15) stayed mostly at 0–1%. At one point, core 0 reached ~45%, while cores 9 and 11 peaked at 55% and 63%, respectively.</p>
<p><strong>Dataset information</strong><br>
I opened the dataset by loading the <code>.mrml</code> scene in Slicer. The main volume is stored as an <code>.nrrd</code> file, with a size of <strong>2.7 GB</strong>. Below are the relevant details:</p>
<ul>
<li>
<p><strong>File type:</strong> NRRD</p>
</li>
<li>
<p><strong>Dimensions:</strong> 1972 × 1084 × 1313</p>
</li>
<li>
<p><strong>Voxel spacing:</strong> 0.011 mm (isotropic, 11 μm per voxel)</p>
</li>
<li>
<p><strong>Voxel type:</strong> unsigned char (1 component)</p>
</li>
<li>
<p><strong>Volume bounds:</strong> X: 0–1971, Y: 0–1083, Z: 0–1312</p>
</li>
<li>
<p><strong>Resolution:</strong> ~11 μm per voxel</p>
</li>
<li>
<p><strong>Total size (on disk):</strong> 2.7 GB</p>
</li>
</ul>
<p><strong>Hardware setup</strong></p>
<ul>
<li>
<p>CPU: Ryzen 9 9950X3D (Zen 5)</p>
</li>
<li>
<p>RAM: 64 GB DDR5 @ 6000 MHz (EXPO enabled in BIOS)</p>
</li>
<li>
<p>Storage: NVMe SSD</p>
</li>
<li>
<p>OS: Windows 11 Pro</p>
</li>
<li>
<p>All cores, threads, and SMT are enabled.</p>
</li>
</ul>
<p><strong>What I’ve tried</strong></p>
<ul>
<li>
<p>Cropping: not possible, since there is no margin left in the region of interest.</p>
</li>
<li>
<p>Resampling to lower resolution: not acceptable, since I lose the little definition and contrast between bone structures.</p>
</li>
<li>
<p>Import with “half resolution”: sometimes reduces size, but too much detail is lost.</p>
</li>
<li>
<p>Alternative segmentation tools in Slicer: none of them have worked well for my case.</p>
</li>
</ul>
<p>Is there any way to significantly improve the processing time of “Grow from seeds” for datasets of this size, or could I be doing something wrong in my workflow?</p>
<p>I sincerely appreciate your time and your responses.</p>
<p>Jared Amudeo P.</p>

---

## Post #2 by @cpinter (2025-10-02 09:03 UTC)

<p>I don’t think you’re doing anything wrong in your workflow. Please note that your image is around 50-80 times larger than a normal CT (in terms of number of voxels). Also, from your description it seems to me that you are using most of the extent of the image for grow from seeds, which usually also does not occur with normal medical images (we segment a smaller part). So putting these two factors together, the two hours unfortunately seems understandable to me.</p>
<p>We have started moving some Segment editor effects on the GPU several years ago, but that line died away, because the direct motivation ceased to exist (the work with fractional labelmaps as I remember). If there is funding, I’m sure it is possible to improve Segment editor effects (even one by one) to use the GPU.</p>
<p>I think others will chime in with their points of view as well.</p>

---

## Post #3 by @mikebind (2025-10-02 17:36 UTC)

<p>I think the best approach will likely be to crop your image volume into several smaller pieces and run grow from seeds on each one, then merge them back together.  This may cause issues near block boundaries, but I think this is probably still your best bet, and you may be able to alleviate boundary issues by re-running grow from seeds near these regions (I can imagine a couple possibilities of how this could work, but am not sure which would work best in practice).   Grow from seeds is fundamentally a local operation, so cropping your image into blocks and running a quick grow from seeds on each block should basically work.  If your seed regions are so sparse that blocks might be missing a seed that they should have, then your even the full image grow from seed result probably won’t work very well.</p>

---

## Post #4 by @muratmaga (2025-10-02 17:44 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="1" data-topic="44647">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<ul>
<li>Resampling to lower resolution: not acceptable, since I lose the little definition and contrast between bone structures.</li>
<li>Import with “half resolution”: sometimes reduces size, but too much detail is lost.</li>
</ul>
</blockquote>
</aside>
<p>You are not doing anything wrong. These are your main options if you want to get results fasts. You can do the segmentation in half resolution version of your data, get your grow from the seed results fast (with the understanding that it may miss small detail). To fix the issues then you can resample your segmentaiton to the original resolution, and import the full resolution imagestack and fine tune your segmentation.</p>
<p>Alternatively, as suggested, split your full resolution data in 4 smaller volumes via CropVolume (make sure each subvolume overlaps a bit, maybe 40-50 voxels), and then run grow from the seeds independently and merge the segments label.</p>

---

## Post #5 by @JaredAmudeo (2025-10-02 18:18 UTC)

<p>Thank you all for your responses. I have a question about that methodology. For example, the dataset I am currently working on is a fragment of a dentary with 4 molars. Could I then crop those 4 teeth, segment them using GFS in the sub-volume, and then copy the finished segment to the segmentation of the main volume</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="44647">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>To fix the issues then you can resample your segmentaiton to the original resolution, and import the full resolution imagestack and fine tune your segmentation.</p>
</blockquote>
</aside>
<p>How can I resample the segmentation to the original resolution, just importing the imagestack?</p>

---

## Post #6 by @muratmaga (2025-10-02 18:43 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="5" data-topic="44647">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>Could I then crop those 4 teeth, segment them using GFS in the sub-volume, and then copy the finished segment to the segmentation of the main volume</p>
</blockquote>
</aside>
<p>Yes, as long as you crop them from the original volume, everything should line up after mergering.</p>
<aside class="quote no-group" data-username="JaredAmudeo" data-post="5" data-topic="44647">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>How can I resample the segmentation to the original resolution, just importing the imagestack?</p>
</blockquote>
</aside>
<p>You should use the oversampling feature of <code>Specify Segment Geometry</code> option of segment editor. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a></p>
<p>(ie., if you have done the segmentation in half-resolution volume, and transfer it to the full resolution version you need to oversample the existing segmentation by 2)</p>

---

## Post #7 by @pieper (2025-10-06 14:43 UTC)

<p><a class="mention" href="/u/jaredamudeo">@JaredAmudeo</a> if you have a cuda-enabled GPU (or you want to borrow one using <a href="https://morphocloud.org/">MorphoCloud</a>) you may want to give this experiment a try:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8767">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8767" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8767" target="_blank" rel="noopener">ENH: Add nvidia warp GPU grow cut</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>pieper:warp-growfromseeds</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-10-05" data-time="16:14:00" data-timezone="UTC">04:14PM - 05 Oct 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 322 additions and 28 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8767/files" target="_blank" rel="noopener">
            <span class="added">+322</span>
            <span class="removed">-28</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This adds a Warp GPU implementation of the underlyging GrowCut algorithm as an o<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8767" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ption if support is available (Warp with CUDA). If also offers a CPU version based on Warp, but this may be slower than the vtkITK version.

On informaal testing the Warp/CUDA version appears to be much faster than the vtkITK version.  Results appear to be identical.  Performance will vary based on GPU used.

This code was ported from an earlier implementation based on OpenCL:

https://github.com/pieper/SlicerCL/blob/3d04661ef7f225edf00292a92088db902787a016/GrowCutCL/GrowCutCL.cl.in

The Warp version and changes to the GrowFromSeeds effect were implemented with the help of Google Gemini.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The python file in the PR is just a drop-in replacement for the corresponding file in a Slicer distribution.</p>

---

## Post #8 by @JaredAmudeo (2025-10-06 14:51 UTC)

<p>Definitely! I have a RTX 5090, it should go well</p>
<p>I’m out of town for a week, but once I’m back I’ll give it a try and see how it goes. Thank you so much!</p>

---

## Post #9 by @JaredAmudeo (2025-10-18 20:18 UTC)

<p>Hello, good day! I just tried this method and it’s wonderful. I haven’t quantified it on multiple datasets yet, but in the one I’m currently working on, it reduced the initialization time by just a few seconds. I only have one issue, which occurs when updating. Whether the auto-update option is enabled or disabled, after correcting the seeds and seeing the loading icon, the updates don’t apply. When I click apply, the previous results remain. How could I fix this? I’m using Slicer 5.8.1. Thank you very much in advance!</p>
<p>Image 1 before correcting seeds</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad8e899894253e9c7c4d7b193cd42954a79cba0.png" data-download-href="/uploads/short-url/1xXuX0oAalpsgpzUcimpCWDSeZy.png?dl=1" title="Captura de pantalla 2025-10-18 171613" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad8e899894253e9c7c4d7b193cd42954a79cba0_2_472x500.png" alt="Captura de pantalla 2025-10-18 171613" data-base62-sha1="1xXuX0oAalpsgpzUcimpCWDSeZy" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad8e899894253e9c7c4d7b193cd42954a79cba0_2_472x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad8e899894253e9c7c4d7b193cd42954a79cba0_2_708x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad8e899894253e9c7c4d7b193cd42954a79cba0.png 2x" data-dominant-color="4F494A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-10-18 171613</span><span class="informations">755×799 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image 2 after painting over the seeds</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce2e85b17e1efbeb71d506631bb31fdfbe3a1be1.png" data-download-href="/uploads/short-url/tpY20maJYeB4vqmmmDigYKxJI9r.png?dl=1" title="Captura de pantalla 2025-10-18 171706" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2e85b17e1efbeb71d506631bb31fdfbe3a1be1_2_454x499.png" alt="Captura de pantalla 2025-10-18 171706" data-base62-sha1="tpY20maJYeB4vqmmmDigYKxJI9r" width="454" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2e85b17e1efbeb71d506631bb31fdfbe3a1be1_2_454x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2e85b17e1efbeb71d506631bb31fdfbe3a1be1_2_681x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce2e85b17e1efbeb71d506631bb31fdfbe3a1be1.png 2x" data-dominant-color="504A4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-10-18 171706</span><span class="informations">721×794 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image 3 after apply</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c049496864238fcf28016ddcda84b08b28c264a.png" data-download-href="/uploads/short-url/3ZRbke0Ny5QWwZ6KylhDMQVjCrM.png?dl=1" title="Captura de pantalla 2025-10-18 171744" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c049496864238fcf28016ddcda84b08b28c264a_2_472x499.png" alt="Captura de pantalla 2025-10-18 171744" data-base62-sha1="3ZRbke0Ny5QWwZ6KylhDMQVjCrM" width="472" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c049496864238fcf28016ddcda84b08b28c264a_2_472x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c049496864238fcf28016ddcda84b08b28c264a_2_708x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c049496864238fcf28016ddcda84b08b28c264a.png 2x" data-dominant-color="382132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-10-18 171744</span><span class="informations">800×846 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @mikebind (2025-10-18 21:58 UTC)

<p>Check your masking settings.  Sometimes a change isn’t made because the masking settings prevent a change your are trying to make from taking effect.</p>
<p>It also seems a little odd that it looks like your segments overlap in image 2.  If a voxel is marked as a seed for two different segments, only one of those will win (I think it’s the one lower on the segment list, but I’m not totally certain about that).</p>
<p>Lastly, if it’s not either of those, perhaps make sure you update the preview segmentation before applying.  If you have modified the seeds, but not updated the preview, it’s possible that clicking the “Apply” button just transfers the existing preview segmentation to the real segmentation without updating it first.</p>

---

## Post #11 by @pieper (2025-10-19 13:24 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> thanks for the suggestions.  I think to clarify though I believe <a class="mention" href="/u/jaredamudeo">@JaredAmudeo</a> was referring to the experimental GPU version linked above, which doesn’t support masking operations.  And also as <a class="mention" href="/u/lassoan">@lassoan</a> reported in the PR thread, the update doesn’t work yet either.</p>
<p>So the GPU GrowCut still needs work for sure, but it sounds from <a class="mention" href="/u/jaredamudeo">@JaredAmudeo</a> 's enthusiasm it’s still a valid direction to pursue.</p>
<p>Andras and I discussed this at a <a href="https://discourse.slicer.org/c/community/hangout/20/l/latest">Slicer dev meeting</a> (Tuesday’s at 10 eastern, open to anyone who wants to join) and were awaiting feedback to think about priorities.  We have both been very impressed with nnInteractive, and wondered if putting more effort into Grow From Seeds vs simplifying the process of running nnInteractive servers is a better investment.  It’s possible we need both.</p>
<p>Jared, did you try nnInteractive on your data?</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> do you have any feedback from the SlicerMorph community on what tools are working best for them when segmenting high res scans?</p>

---

## Post #12 by @JaredAmudeo (2025-10-19 16:18 UTC)

<p>Thank you very much for your reply. Sure, the issue I’m having is with the experimental version using the GPU.</p>
<p>I’m asking out of ignorance, to fix that, would I need to work directly with the .py file, or is it something much more complex?</p>
<p>Regarding nnInteractive, I tried using it once with an RTX 4070 Ti Super, but I could never get it to work. I would like to try it again but my question is, it would be similar to Grown froom seeds in it’s experimental GPU version, faster, slower?</p>

---

## Post #13 by @pieper (2025-10-19 16:33 UTC)

<p>Thanks for the extra info <a class="mention" href="/u/jaredamudeo">@JaredAmudeo</a>.</p>
<p>Fixing the update mode, and even adding the masking should all be doable with the GPU version just by tweaking the python file, and probably can be done with a chatbot.   Since the basic GPU algorithm is working I think the missing features would be just a matter of a few lines of python.</p>
<p>For context, I wrote the GPU growcut in OpenCL about 10 years ago and integrated it with the older Editor module, but never bothered to port it over.  But your post made me look at it again since it’s a simple algorithm and I have been playing around with Warp for another project.  Using gemini, the port from OpenCL to warp worked on the very first try, so used gemini to get the current draft PR in about an hour or two.</p>
<p>As for nnInteractive, it’s a totally different approach.  It may not actually work on large volumes but I’m sure that depends on many factors like GPU memory etc.  I know I saw it fail on a 10GB card but then work on a 20GB card for a clinical CT so I imagine that a very high res scan would need significant GPU memory.</p>

---

## Post #14 by @JaredAmudeo (2025-10-19 17:54 UTC)

<p>I’ve tried doing it with the help of an AI for the code, but I haven’t been able to get it to work haha. What I did was download the entire GrowCutCL folder and add it to 3D Slicer through another additional module path. I’m not sure if that has anything to do with it.</p>
<p>To understand, could I achieve a port with AI assistance? Sorry for my ignorance, I know very little about this topic.</p>

---

## Post #15 by @pieper (2025-10-20 15:17 UTC)

<p>You wouldn’t need to use the GrowCutCL code, since the core algorithm has already been ported.  The part that very different between the old Editor version and the current Segment Editor version is the way the incremental updates are handled, so that’s the part that really needs to be re-implemented the way the current GrowFromSeeds effect is implemented.  Also the old CL version didn’t have the masking option at all, so that needs to be added.</p>
<p>I’m not sure how easy it will be to get the AI to implement these things.  It may also depend on what AI is used.  Some people have been saying that the latest Claude Code is really good as many tasks.  Perhaps by checking out the the branch for the pull request and then also pasting in this discourse thread it would know what to do.  Or maybe you need to break it down step-by-step.</p>

---
