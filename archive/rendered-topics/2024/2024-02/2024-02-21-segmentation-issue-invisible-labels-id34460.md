# Segmentation issue - "invisible" labels

**Topic ID**: 34460
**Date**: 2024-02-21
**URL**: https://discourse.slicer.org/t/segmentation-issue-invisible-labels/34460

---

## Post #1 by @Dhartez (2024-02-21 22:15 UTC)

<p>Hi all,</p>
<p>sorry for semi-reposting (I initially thought this was a pyradiomics issue and therefore posted there, but now figured that it is a segmentation issue):</p>
<p>I am having a problem with importing CNN generated segmentations of two brain structures (bilaterally, so 4 segmentations / VOIs in total) on MRI.</p>
<p>When I load the MRI volume and the segmentation file, it looks good, only the light blue VOI isn’t fully recognized as a segmentation/label it seems:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f.jpeg" data-download-href="/uploads/short-url/lzju9q29sTdAIBwrJ5pPFS36VlR.jpeg?dl=1" title="Screen1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_690x298.jpeg" alt="Screen1" data-base62-sha1="lzju9q29sTdAIBwrJ5pPFS36VlR" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_690x298.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_1035x447.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972b96b2bd1ed0f59767d6f2e55b5b125f66e42f_2_1380x596.jpeg 2x" data-dominant-color="757477"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen1</span><span class="informations">1603×693 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I add it in the Segmentations module it looks fine:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3.jpeg" data-download-href="/uploads/short-url/58X4Tk7Wbb1Ts4kzPA3kmppox3R.jpeg?dl=1" title="Screen2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_690x395.jpeg" alt="Screen2" data-base62-sha1="58X4Tk7Wbb1Ts4kzPA3kmppox3R" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/240df37792f5e92a8eb0f0d31cfb825eeadc2ca3_2_1380x790.jpeg 2x" data-dominant-color="9E9FA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen2</span><span class="informations">1642×941 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, out of the four segmentations, I can only edit a single one (the brown one, seg 4), although all four are visible - any segmentation tool that I try on the other three will result in nothing - as if they were not there at all.</p>
<p>How can that be?</p>
<p>The volume and segmentation file are in the folder below (all deidentified of course):</p>
<p><a href="https://cloudius.meduniwien.ac.at/index.php/s/tRFmMXwUbacZE05" rel="noopener nofollow ugc">Link</a></p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2024-02-22 04:49 UTC)

<p>You can try upgrading to the current Slicer version (5.6.1) and make sure you save the segmentation into an image with integer type (unsigned char, short, etc).</p>

---

## Post #3 by @Dhartez (2024-02-22 14:40 UTC)

<p>Thanks - I tried the new version, but no change, still not editable.</p>
<p>In terms of saving, what option would that be (i.e. file extension)?</p>

---

## Post #4 by @lassoan (2024-02-22 14:44 UTC)

<p>To fix the loading issue, you can convert your numpy array to uint8 before writing to file. Like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/72abd51b670bf989f359632ab1e9e2841ed268ca/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py#L209">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/72abd51b670bf989f359632ab1e9e2841ed268ca/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py#L209" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/72abd51b670bf989f359632ab1e9e2841ed268ca/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py#L209" target="_blank" rel="noopener">lassoan/SlicerMONAIAuto3DSeg/blob/72abd51b670bf989f359632ab1e9e2841ed268ca/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py#L209</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="199" style="counter-reset: li-counter 198 ;">
          <li></li>
          <li></li>
          <li>    elif save_mode == 'brats23' or 'brats23' in config['bundle_root']: #special case brats</li>
          <li>        # convert 3 channel into 1 channel ints</li>
          <li>        p2 = 2 * seg.any(0).to(dtype=torch.uint8)</li>
          <li>        p2[seg[1:].any(0)] = 1</li>
          <li>        p2[seg[2]] = 3</li>
          <li>        seg = p2</li>
          <li>        print(f"Updated seg for brats23 {seg.shape}")</li>
          <li></li>
          <li class="selected">    seg = seg.cpu().numpy().astype(np.uint8)</li>
          <li></li>
          <li>    nib.save(nib.Nifti1Image(seg, affine = original_affine), result_file)</li>
          <li>    print(f'ALL DONE, result saved in {result_file}')</li>
          <li></li>
          <li>if __name__ == '__main__':</li>
          <li>  fire.Fire(main)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
