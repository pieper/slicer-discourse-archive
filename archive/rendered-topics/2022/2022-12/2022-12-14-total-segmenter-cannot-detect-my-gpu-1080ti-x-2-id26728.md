# Total Segmenter cannot detect my GPU (1080ti x 2)

**Topic ID**: 26728
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/total-segmenter-cannot-detect-my-gpu-1080ti-x-2/26728

---

## Post #1 by @scottcollins3d (2022-12-14 15:36 UTC)

<p>On my setup, the Total Segmenter extension is telling me that it cannot detect my GPU (1080ti x 2). Can you point me to where there may be settings to detect my graphics card?</p>
<p>Operating system: Windows 10<br>
Slicer version: 5.2.1<br>
Expected behavior: detect gpu<br>
Actual behavior: cannot detect gpu</p>

---

## Post #2 by @lassoan (2022-12-14 15:45 UTC)

<p>You need to install CUDA that is compatible with PyTorch, which is <a href="https://pytorch.org/get-started/locally/">currently on your platform</a> is CUDA 11.6 or 11.7.</p>
<p>If you did not have CUDA installed or an incompatible version was installed when you first set up TotalSegmentator then the CPU version of pytorch was installed.</p>
<p>You need to force installation of the GPU version using the install command on the pytorch website, which is currently (use cu116/cu117 according to your installed CUDA version):</p>
<pre data-code-wrap="txt"><code class="lang-plaintext">"%localappdata%\NA-MIC\Slicer 5.2.1\bin\PythonSlicer.exe" -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116 --force-reinstall
</code></pre>
<p>If this forced reinstallation does not work then maybe you can try to uninstall torch, torchvision, torchaudio then install again; but probably the easiest is to remove Slicer-5.2 and reinstall.</p>

---

## Post #3 by @scottcollins3d (2022-12-14 16:21 UTC)

<p>Thank you. I installed cuda after installing v5.2.1 and the Total Segmenter extension. I believe I should have installed cuda first. GPU is being detected now.</p>

---

## Post #4 by @Luca (2023-06-05 14:19 UTC)

<p>hello, can you please tell me how to run the code line that you posted, to solve problems in detecting GPU with total segmentator? thank you</p>

---

## Post #5 by @lassoan (2023-06-05 15:26 UTC)

<p>I’ve submitted a pull request to make it easier to select pytorch version in PyTorch Utils module. Hopefully it will be merged today or tomorrow. You can track its status here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/fepegar/SlicerPyTorch/pull/11">
  <header class="source">

      <a href="https://github.com/fepegar/SlicerPyTorch/pull/11" target="_blank" rel="noopener">github.com/fepegar/SlicerPyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/fepegar/SlicerPyTorch/pull/11" target="_blank" rel="noopener">Allow specifying pytorch version for installation</a>
      </h4>

    <div class="branches">
      <code>fepegar:main</code> ← <code>lassoan:configurable-torch-version</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-05" data-time="15:23:07" data-timezone="UTC">03:23PM - 05 Jun 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 36 additions and 13 deletions">
          <a href="https://github.com/fepegar/SlicerPyTorch/pull/11/files" target="_blank" rel="noopener">
            <span class="added">+36</span>
            <span class="removed">-13</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The main motivation for this is that on some computers when installing PyTorch w<span class="show-more-container"><a href="https://github.com/fepegar/SlicerPyTorch/pull/11" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ith default options, a very old version (1.8.1) is installed. The new API and GUI allows specifying a requirement (e.g., "&gt;=1.12" or "&gt;=2").

While this does not address the question of why old version is installed by default, it allows modules to automatically install correct pytorch version and allows users to manually specify a version, if effectively fixes #9</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You need to use the lateset Slicer Stable Release or latest Slicer Preview Release to get the update (the update is available automatically in the Extensions Manager the day after the pull request is merged).</p>

---
