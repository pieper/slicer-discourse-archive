# TotalSegmentator 'Failed to compute results'... 'returned non zero exit status'

**Topic ID**: 34433
**Date**: 2024-02-20
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status/34433

---

## Post #1 by @SHMMU (2024-02-20 18:46 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.6.0 &amp; 5.6.1<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3186e4226eb04634e4c858cf8188d5684c0323c.jpeg" data-download-href="/uploads/short-url/rPTrQYfPL8fcAwSCqW0VT3gri7W.jpeg?dl=1" title="thumbnail_IMG_5762" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3186e4226eb04634e4c858cf8188d5684c0323c_2_375x500.jpeg" alt="thumbnail_IMG_5762" data-base62-sha1="rPTrQYfPL8fcAwSCqW0VT3gri7W" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3186e4226eb04634e4c858cf8188d5684c0323c_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3186e4226eb04634e4c858cf8188d5684c0323c_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3186e4226eb04634e4c858cf8188d5684c0323c_2_750x1000.jpeg 2x" data-dominant-color="78716E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_IMG_5762</span><span class="informations">1440×1920 482 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have uninstalled, reinstalled different versions of 3D Slicer and the same error message keeps appearing. I am at a loss of what to do to get it working again. Any help would be very appreciated.</p>

---

## Post #2 by @lassoan (2024-02-20 19:00 UTC)

<p>TotalSegmentator can only segment CT images. Please retry the segmentation on a CT image as described in the <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#tutorial">tutorial</a>.</p>
<p><code>Error 120</code> is often caused by incorrect PyTorch installation. Reinstall the latest Slicer Stable Release (currently 5.6.1) in a new folder and install PyTorch manually as described <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/README.md#problem-error-popup-on-the-first-run-failed-to-compute-results--command--pythonslicer-totalsegmentatorexe--returned-non-zero-exit-status-120">here</a>.</p>
<p>What CPU and GPU do you have?</p>

---

## Post #3 by @jamesobutler (2024-02-20 23:56 UTC)

<p>Please see the following post regarding a required workaround even when using CT images. Note this may change as the various dependencies of the <code>TotalSegmentator</code> python package change.</p>
<aside class="quote quote-modified" data-post="11" data-topic="34434">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-failing-with-error-120/34434/11">Totalsegmentator failing with error 120</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Aha! So, it is not a too old package, but a too recent package. 
Unfortunately, developer of dynamic_network_architectures broke backward compatibility with a recent update. ResidualEncoderUNet package must be imported as from dynamic_network_architectures.architectures.residual_unet import ResidualEncoderUNet now, but since this change was snuck into a minor version update (0.2 to 0.4) developer of TotalSegmentator did not suspect anything bad would happen. 
As a workaround, you can downgrade d…
  </blockquote>
</aside>


---
