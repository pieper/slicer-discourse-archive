# PyTorch CUDA incompatibility with NVIDIA RTX 5070 Ti 

**Topic ID**: 43233
**Date**: 2025-06-05
**URL**: https://discourse.slicer.org/t/pytorch-cuda-incompatibility-with-nvidia-rtx-5070-ti/43233

---

## Post #1 by @rodrigot (2025-06-05 14:39 UTC)

<p>Hello everyone,</p>
<p>I’m currently using a 3D Slicer (version 5.9.0-2025-06-03) on Ubuntu Linux. I have an NVIDIA GeForce RTX 5070 Ti GPU installed.</p>
<p>When launching Slicer, I’m consistently seeing the following <code>UserWarning</code> in the Python Interactor:</p>
<hr>
<p>NVIDIA GeForce RTX 5070 Ti with CUDA capability sm_120 is not compatible with the current PyTorch installation.<br>
The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90.<br>
If you want to use the NVIDIA GeForce RTX 5070 Ti GPU with PyTorch, please check the instructions at <a href="https://pytorch.org/get-started/locally/" rel="noopener nofollow ugc">https://pytorch.org/get-started/locally/</a></p>
<hr>
<p>My understanding is that while Slicer detects my GPU, the PyTorch version bundled does not support the sm_120 (compute capability 12.0) architecture of my RTX 5070 Ti.</p>
<p>This means that Slicer modules are unable to access or utilize my GPU for accelerated processing, and consequently, will fall back to CPU execution, which is slower.</p>
<p>Is there anyone who can help resolve this issue so that the Slicer modules can run on this GPU?</p>
<p>Thank you so much.</p>

---

## Post #2 by @muratmaga (2025-06-05 15:22 UTC)

<p>As far as I can tell only 12.8 series support 5070Ti. So uninstall your pytorch (I assume you are using PyTorch utils?) restart slicer, then instead of automatic search for compatible versions, choose specifically cu12.8 and try again.</p>

---

## Post #3 by @Mark_Ryan (2025-06-07 22:51 UTC)

<p>Running on a 5090 - had to update Pytorch to 12.8 from within slicer python console. Around a 4 GB download so takes a while. SM_120 refers to the 50 series GPUs I believe, so 12.8 was the only supported version.</p>

---

## Post #4 by @jamesobutler (2025-06-09 15:18 UTC)

<p><a class="mention" href="/u/mark_ryan">@Mark_Ryan</a> You were successful with this on Windows? Or were you using a Linux distro? Rodrigo appears to be using Ubuntu 24.04 per:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8468">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8468" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8468" target="_blank" rel="noopener nofollow ugc">Request for PyTorch 2.7 Support in 3D Slicer for NVIDIA Blackwell GPUs</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-05" data-time="17:00:16" data-timezone="UTC">05:00PM - 05 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/rodrigoteixeira7" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/215039333?v=4" class="onebox-avatar-inline" width="20" height="20">
          rodrigoteixeira7
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Request for PyTorch 2.7 Support in 3D Slicer for NVIDIA Blackwell GPUs

System I<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nformation:
- GPU: NVIDIA GeForce RTX 5070 Ti
- Architecture: NVIDIA Blackwell
- OS: Linux Unbutu 24.04.2 LTS

PyTorch version 2.7 introduces support for the Blackwell architecture, which is required for compatibility with this GPU. Earlier versions of PyTorch (≤2.6) do not support it, resulting in the following error:
- “The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90.”

Unfortunately, the PyTorch version currently available in 3D Slicer is&nbsp;limited&nbsp;to&nbsp;2.6</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Mark_Ryan (2025-06-09 18:26 UTC)

<p>This was from within windows, but everything downloaded within python shell in Slicer. But I needed ChatGPT to get me that far, so can’t speak for the Linux thing.</p>

---

## Post #6 by @jamesobutler (2025-06-09 19:57 UTC)

<p>Ok thanks for the update. Yes, Rodrigo’s issues exists because of using the Slicer linux package which is currently built based on CentOS 7 and glibc 2.17 and there is not a Pytorch 2.7.x whl that is compatible with it.</p>
<p>Pytorch 2.6.0 for example has manylinux1 (CentOS 5 based, glibc 2.5) based whls which can be run by the Slicer linux package, however Pytorch 2.7.0 has manylinux_2_28 (glibc 2.28) based whls which is too new of a glibc to match what Slicer provides for the linux package.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/pypa/manylinux?tab=readme-ov-file#manylinux">
  <header class="source">

      <a href="https://github.com/pypa/manylinux?tab=readme-ov-file#manylinux" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/47fa758c30d1fd8958ab4bc4ffc2ab87/pypa/manylinux?tab=readme-ov-file#manylinux" class="thumbnail">

  <h3><a href="https://github.com/pypa/manylinux?tab=readme-ov-file#manylinux" target="_blank" rel="noopener nofollow ugc">GitHub - pypa/manylinux: Python wheels that work on any linux (almost)</a></h3>

    <p><span class="github-repo-description">Python wheels that work on any linux (almost)</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
