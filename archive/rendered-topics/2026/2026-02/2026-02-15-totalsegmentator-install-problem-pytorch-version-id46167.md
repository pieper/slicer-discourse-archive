# TotalSegmentator install problem - pytorch version?

**Topic ID**: 46167
**Date**: 2026-02-15
**URL**: https://discourse.slicer.org/t/totalsegmentator-install-problem-pytorch-version/46167

---

## Post #1 by @mhopeng (2026-02-15 19:00 UTC)

<p>Hello, I’ve tried to install TotalSegmentator on two macOS systems. When I try to run the sample data set, I get an error that seems to be related to the PyTorch version:</p>
<p>ImportError: cannot import name ‘GradScaler’ from ‘torch’ (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/_<em>init</em>_.py)</p>
<p>A google search suggests that this is a problem with the PyTorch version. The PyTorch installation appears to be managed by a Slicer extension. Is there a version mismatch, or am I on the wrong track here?</p>

---

## Post #2 by @jamesobutler (2026-02-15 19:30 UTC)

<p>The following about downgrading the nnunetv2 version may help:</p>
<aside class="quote quote-modified" data-post="3" data-topic="45200">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/version-5-10-0-error-in-total-segmentator/45200/3">Version 5.10.0, error in total segmentator</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    This appears to be an issue introduced by NNunetv2 developers. This package is a dependency of TotalSegmentator. 
A possible workaround is to open the NNunet Slicer module which is used for installing versions of the package. Choose to install nnunetv2&lt;2.6 as it seems like the nnunetv2 2.6.0 version introduced this error that requires torch 2.6.0 and later for the CPU version of GradScaler. 
Unfortunately, on macOS Slicer factory builds are still x86_64 builds with no native arm64 build. The lat…
  </blockquote>
</aside>


---
