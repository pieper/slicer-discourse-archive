# Can MONAI Auto3dSeg use metal (MPS) on M series processors running MacOS?

**Topic ID**: 44305
**Date**: 2025-09-02
**URL**: https://discourse.slicer.org/t/can-monai-auto3dseg-use-metal-mps-on-m-series-processors-running-macos/44305

---

## Post #1 by @GeneRisi (2025-09-02 00:50 UTC)

<p>I am running Auto3dSeg on my MacBook Pro with M3 Pro and wondering whether there is something I need to do to enable use of MTL for inferencing?</p>
<p>Thank you.</p>
<p>Gene Risi</p>

---

## Post #2 by @jamesobutler (2025-09-02 12:35 UTC)

<p>The MPS (metal performance shaders) support will be possible once Slicer provides a native arm64 build for macOS as then the embedded python in Slicer will appropriately be an arm64 version that can use the arm64 macOS torch whls that provide the MPS support.</p>
<p>For now, macOS on Slicer must continue to use the intel x86_64 version that runs through the Rosetta 2 layer.</p>
<p>Once arm64 support is available we will post over on the following thread to provide an update:</p>
<aside class="quote" data-post="1" data-topic="35699">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/ba8739/48.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/build-3d-slicer-for-macos-arm64/35699">Build 3D Slicer for MacOS arm64?</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --style-square --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
    </div>
  </div>
  <blockquote>
    PyTorch has support for using the shaders in the M series chips, but to use it, one has to use the arm64 version of Python. Should a native (in this case, M3) build of Slicer3D be possible? If yes, where should I get the 5.15.2 Qt package (for MacOS arm64)? 
Thank you! 
Gene
  </blockquote>
</aside>


---

## Post #3 by @GeneRisi (2025-09-02 14:47 UTC)

<p>Hello James,</p>
<p>The version of PyTorch that is running in Slicer3d has the MPS backend available. I noticed that the source code for MONAI Auto3dSeg does not include any reference to “mps” (lots of references to CUDA) so I think the code will also need to recognize “mps” as an optional device. Is my assumption correct?</p>
<p>Thank you!</p>
<p>Gene Risi</p>

---

## Post #4 by @jamesobutler (2025-09-02 15:25 UTC)

<p>Yes if you have an Intel mac with amd GPU then torch can use the MPS. From my understanding, you have an Apple Silicon mac where the torch version I believe will not be able to use MPS with the graphics of Apple Silicon unless it is running an arm64 version (not an x86_64 version running through Rosetta 2).</p>

---

## Post #5 by @GeneRisi (2025-09-02 16:47 UTC)

<p>If it would be helpful, I could test that, if it would just make more work for you, I will wait.</p>
<p>Gene</p>

---
