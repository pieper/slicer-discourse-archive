# File Save Behavior Query: TIFF Files Auto-Selecting on Second Save

**Topic ID**: 34665
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/file-save-behavior-query-tiff-files-auto-selecting-on-second-save/34665

---

## Post #1 by @Aram_Harutyunyan (2024-03-03 03:16 UTC)

<p>I’ve encountered a unexpected behavior in an application running on <strong>Ubuntu 22.04</strong> , app version <strong>5.7.0-2024-02-29</strong> , and I’m trying to determine whether it’s a bug or an intended feature. The issue revolves around the process of saving files, specifically in the .tif/.tiff format, and how these files are selected (or not selected) during consecutive save attempts.</p>
<p><strong>Steps to Reproduce:</strong></p>
<ol>
<li>Download any sample data.</li>
<li>Press the “Save” button and choose to save the file in either <code>.tif</code> or <code>.tiff</code> format, then successfully save it.</li>
<li>Delete the saved file from the computer through the file manager.</li>
<li>Press the <code>"Save"</code> button again to save another file. By default, all previously saved files are not selected or “checked” until you hit the second <code>"Save"</code> button within the Save window.</li>
<li>At this point, without any user intervention, the application automatically selects or checks the <code>.tiff</code> file. But I did not get this problem with other file formats like <code>.nrrd</code> or <code>.mha</code></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5e9ade63a00360a5f18357f98b187c48ec3c30.jpeg" data-download-href="/uploads/short-url/xrkpVP2ysMOhjWHmrBA6N9oAEkU.jpeg?dl=1" title="1A" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea5e9ade63a00360a5f18357f98b187c48ec3c30_2_690x189.jpeg" alt="1A" data-base62-sha1="xrkpVP2ysMOhjWHmrBA6N9oAEkU" width="690" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea5e9ade63a00360a5f18357f98b187c48ec3c30_2_690x189.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea5e9ade63a00360a5f18357f98b187c48ec3c30_2_1035x283.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea5e9ade63a00360a5f18357f98b187c48ec3c30_2_1380x378.jpeg 2x" data-dominant-color="898494"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1A</span><span class="informations">1920×527 69.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5925afc54155dce5063c3f698a3e884c4f8a2e6b.jpeg" data-download-href="/uploads/short-url/cIDeL2ZsZUlWE19TVguwEnioZkv.jpeg?dl=1" title="2A" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5925afc54155dce5063c3f698a3e884c4f8a2e6b_2_690x190.jpeg" alt="2A" data-base62-sha1="cIDeL2ZsZUlWE19TVguwEnioZkv" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5925afc54155dce5063c3f698a3e884c4f8a2e6b_2_690x190.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5925afc54155dce5063c3f698a3e884c4f8a2e6b_2_1035x285.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5925afc54155dce5063c3f698a3e884c4f8a2e6b_2_1380x380.jpeg 2x" data-dominant-color="9692A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2A</span><span class="informations">1920×529 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d9e28a28eae2b3d3a917a755a049652eed00387.jpeg" alt="5" data-base62-sha1="b4DCmrtU8w2TiNe72KkUY9IY8zJ" width="355" height="118"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b81f0af18fd71299cf1ea6605bcf8e121584c48.jpeg" data-download-href="/uploads/short-url/fl3u3QBASVD32sIh2xmQsHuVV6U.jpeg?dl=1" title="3A" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b81f0af18fd71299cf1ea6605bcf8e121584c48_2_690x189.jpeg" alt="3A" data-base62-sha1="fl3u3QBASVD32sIh2xmQsHuVV6U" width="690" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b81f0af18fd71299cf1ea6605bcf8e121584c48_2_690x189.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b81f0af18fd71299cf1ea6605bcf8e121584c48_2_1035x283.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b81f0af18fd71299cf1ea6605bcf8e121584c48_2_1380x378.jpeg 2x" data-dominant-color="9694A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3A</span><span class="informations">1920×527 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f26b4cd99c7a28832426e982d3077c45e78fdd4.jpeg" data-download-href="/uploads/short-url/6J7mS275EgaN3JCfVWPHFSVb5mQ.jpeg?dl=1" title="8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f26b4cd99c7a28832426e982d3077c45e78fdd4_2_690x378.jpeg" alt="8" data-base62-sha1="6J7mS275EgaN3JCfVWPHFSVb5mQ" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f26b4cd99c7a28832426e982d3077c45e78fdd4_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f26b4cd99c7a28832426e982d3077c45e78fdd4_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f26b4cd99c7a28832426e982d3077c45e78fdd4.jpeg 2x" data-dominant-color="908E9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8</span><span class="informations">1280×703 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>NOTICE:</strong>  It’s worth noting that this issue might not occur on every attempt. Sometimes, it may be necessary to repeat the saving and deleting process 2-3 times to observe this problem.</p>
<p><strong>Expected Behavior:</strong> I would expect that upon attempting to save a file for the second time, no files would be automatically selected or checked, consistent with the behavior observed for other file formats.</p>
<p><strong>Actual Behavior:</strong> The application automatically selects or checks <code>.tiff</code> files on the second save attempt, diverging from the expected behavior.</p>
<p>Before I delve deeper into troubleshooting or reporting this as a bug, I wanted to reach out to this community to see if anyone else has experienced this issue or can confirm whether this is a known feature or a bug. This behavior seems to be specific to <code>.tiff</code> files, and I’m not sure <strong>yet</strong> why it’s occurring.</p>

---

## Post #2 by @pieper (2024-03-04 20:24 UTC)

<p>Hmm, that does sound odd.  I can’t reproduce it on a mac with 5.6.1.</p>
<p>You may already know this, but we discourage using tiff for volume data since you lose the spacing and orientation information.</p>

---

## Post #3 by @Aram_Harutyunyan (2024-03-05 08:15 UTC)

<p>Yes indeed, I know that we don’t have to save in <code>.TIFF</code> format if we are saving a 3D image. However, I thought that maybe this error could spread to other files too (Although I didn’t find the same error on other files yet). Maybe after I deal with the rest of the bugs/issues, I’ll delve into solving this one if it’s not a feature.</p>

---
