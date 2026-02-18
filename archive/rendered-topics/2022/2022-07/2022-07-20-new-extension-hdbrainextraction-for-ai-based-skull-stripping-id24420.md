# New extension: HDBrainExtraction for AI-based skull stripping

**Topic ID**: 24420
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/new-extension-hdbrainextraction-for-ai-based-skull-stripping/24420

---

## Post #1 by @lassoan (2022-07-20 20:50 UTC)

<p>A new AI-based tool - <a href="https://github.com/lassoan/SlicerHDBrainExtraction#hdbrainextraction">HDBrainExtracion extension</a> - is added to 3D Slicer for skull stripping (blanking out region outside the brain in MRI images). The model is trained on a large set of images and proven to be more robust than many other similar tools.</p>
<p><img src="https://github.com/lassoan/SlicerHDBrainExtraction/raw/main/Screenshot01.jpg" alt="" width="690" height="360"></p>
<p>The extension is built by packaging the <a href="https://github.com/MIC-DKFZ/HD-BET">HD-BET model provided by DKFZ (Heidelberg, Germany)</a>. This extension can serve as a good example for others who intend to distribute their AI models via 3D Slicer.</p>

---

## Post #2 by @rbumm (2022-07-21 07:09 UTC)

<p>This is a very instructive and well-written extension, thank you <a class="mention" href="/u/lassoan">@lassoan</a>. Do you have any information on how HD-BET trained their skull stripping model in detail? The cited paper remains a bit unclear here. It would be interesting to have similar tissue stripping AI-based modules for other organs.</p>

---

## Post #3 by @lassoan (2022-07-21 07:48 UTC)

<p>I don’t have any more information other than what they described in their paper. You may contact the authors at the email provided in the paper or by submitting an issue in <a href="https://github.com/MIC-DKFZ/HD-BET/">their GitHub repository</a> for more details.</p>

---

## Post #4 by @rbumm (2022-07-21 13:02 UTC)

<p>Short feedback: Works great on a Windows 11 GTX 1060 laptop, but I needed to start Slicer in Admin mode to install the PyTorch extension upon the first run. Processing took about 5 min to complete (Device=auto), so it is probably not using the GPU yet.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8201fa619796b74817ed93e90f265ee6ba2eb97c.png" data-download-href="/uploads/short-url/iy6jaeDd3mhnj62AHVNCUbBHMWo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8201fa619796b74817ed93e90f265ee6ba2eb97c_2_690x372.png" alt="image" data-base62-sha1="iy6jaeDd3mhnj62AHVNCUbBHMWo" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8201fa619796b74817ed93e90f265ee6ba2eb97c_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8201fa619796b74817ed93e90f265ee6ba2eb97c_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8201fa619796b74817ed93e90f265ee6ba2eb97c.png 2x" data-dominant-color="9C9C9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1358×734 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2022-07-22 06:11 UTC)

<p>Thanks for the feedback. What indicated that installing as admin user was necessary?</p>
<p>I’ve noticed that failed Pytorch installs may prevent proper installation. You may consider trying to reinstall Slicer from scratch (deleting the Slicer install folder completely) to see if it makes Slicer’s pytorch find the GPU.</p>
<p>Also make sure that in your NVIDIA settings Slicer is configured to use the GPU.</p>

---

## Post #6 by @rbumm (2022-07-22 06:29 UTC)

<p>I install HDBrainExtraction, it asks to install PyTorch too,  I agree, then I restart and run the extension the first time and get:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9d9e2d89e5ccfb3f1ee07229935a76307d13052.jpeg" data-download-href="/uploads/short-url/xmK4j2rvVR66o6KTO3T4atfNK5s.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d9e2d89e5ccfb3f1ee07229935a76307d13052_2_690x378.jpeg" alt="image" data-base62-sha1="xmK4j2rvVR66o6KTO3T4atfNK5s" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d9e2d89e5ccfb3f1ee07229935a76307d13052_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d9e2d89e5ccfb3f1ee07229935a76307d13052_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d9e2d89e5ccfb3f1ee07229935a76307d13052_2_1380x756.jpeg 2x" data-dominant-color="919196"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1607×882 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @rbumm (2022-07-22 06:42 UTC)

<p>This exception was solved by applying this commit</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/fepegar/SlicerPyTorch/commit/b1f33d6527509a607576e544cf225a67bcabe437">
  <header class="source">

      <a href="https://github.com/fepegar/SlicerPyTorch/commit/b1f33d6527509a607576e544cf225a67bcabe437" target="_blank" rel="noopener">github.com/fepegar/SlicerPyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fepegar/SlicerPyTorch/commit/b1f33d6527509a607576e544cf225a67bcabe437" target="_blank" rel="noopener">Add upper bound for light-the-torch requirement</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-06-18" data-time="14:30:13" data-timezone="UTC">02:30PM - 18 Jun 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/fepegar" target="_blank" rel="noopener">
          <img alt="fepegar" src="https://avatars.githubusercontent.com/u/12688084?v=4" class="onebox-avatar-inline" width="20" height="20">
          fepegar
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/fepegar/SlicerPyTorch/commit/b1f33d6527509a607576e544cf225a67bcabe437" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The used functionality is removed in newer versions: https://github.com/pmeier/l<span class="show-more-container"><a href="https://github.com/fepegar/SlicerPyTorch/commit/b1f33d6527509a607576e544cf225a67bcabe437" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ight-the-torch/issues/41#issuecomment-1155279506</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>to the PyTorch utility module. Then the install runs normally, but unfortunately, it does not detect CUDA yet on my two systems. Using Slicer in Admin mode was mandatory, otherwise, the PyTorch Util was throwing exceptions.</p>

---

## Post #8 by @rbumm (2022-07-22 07:06 UTC)

<p>Very good performance on my desktop (RTX 3070 Ti): 20 s rendering time</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7698eee6d77201617e9166263b8787a519e3dee6.jpeg" data-download-href="/uploads/short-url/gV9ZXHWYurjptERZ4SvX4p9hXYa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7698eee6d77201617e9166263b8787a519e3dee6_2_690x365.jpeg" alt="image" data-base62-sha1="gV9ZXHWYurjptERZ4SvX4p9hXYa" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7698eee6d77201617e9166263b8787a519e3dee6_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7698eee6d77201617e9166263b8787a519e3dee6_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7698eee6d77201617e9166263b8787a519e3dee6.jpeg 2x" data-dominant-color="3D3D47"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1211×642 93.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>CUDA seems to be available on that system.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3185f88f7067ae863b473132695a481bd3accce1.png" alt="image" data-base62-sha1="746qvaJIHif70U1ac3kS6Klr9mN" width="224" height="95"></p>

---

## Post #9 by @lassoan (2022-07-22 07:38 UTC)

<p>Thanks for the additional information.</p>
<p>If you encounter any issues then always try to update the extensions in the latest Slicer Stable Release, or install the latest Slicer Preview Release (extension updates are not available for preview releases).</p>

---

## Post #10 by @Gonzalo_Rojas_Costa (2022-07-22 14:31 UTC)

<p>HDBrainExtraction is useful for non-volumetric T1 images?</p>

---

## Post #11 by @lassoan (2022-07-23 05:26 UTC)

<p>I would expect that the module only works for images that contains many slices and cover the full brain, but you can try it on síngle-slice images, too.</p>
<p>If you find that it does not work then you can train a new network specifically for síngle-slice images. You should be able to automatically generate training data from full-brain data sets.</p>

---

## Post #12 by @spichardo (2022-07-29 00:13 UTC)

<p>This is great… do you know if there is a way to hack the Pytorch installation to swap it to use the Metal-backend that is now available for M1/M2 processors?</p>

---

## Post #13 by @lassoan (2022-07-29 05:53 UTC)

<p>Wet use <a href="https://pypi.org/project/light-the-torch/">light-the-torch</a> to install pytorch. Check out its documentation for ARM architecture compatibility. Note that Slicer runs on ARM macs through Rosetta emulation, which might complicate things a bit further.</p>

---

## Post #15 by @lassoan (2022-12-30 01:12 UTC)

<p>Let’s see if you get more information if you run the installation from the Windows terminal. Exit Slicer and run this command in the Command Prompt:</p>
<blockquote>
<p>“%localappdata%\NA-MIC\Slicer 5.2.1\bin\PythonSlicer.exe” -m pip install git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators</p>
</blockquote>

---

## Post #17 by @Tobias (2024-01-02 07:31 UTC)

<p>This works very well! I was just wondering if it is possible to generate a mask with higher resolution?</p>

---

## Post #18 by @lassoan (2024-01-02 18:00 UTC)

<p>You can get higher-resolution segmentation if you use a GPU. In CPU mode the resolution is automatically reduced to keep the computation time lower.</p>

---
