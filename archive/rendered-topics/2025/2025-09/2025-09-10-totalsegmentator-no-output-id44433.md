# TotalSegmentator No Output

**Topic ID**: 44433
**Date**: 2025-09-10
**URL**: https://discourse.slicer.org/t/totalsegmentator-no-output/44433

---

## Post #1 by @aceegreene (2025-09-10 16:09 UTC)

<p>Hi everyone -  I am trying to use totalsegmentator to segment an MRI image I have and seem to not be getting any results. There seem to be no errors in the module itself or in the Python console but once the processing is finished there is no segmentation and even the Show 3D button is grayed.</p>
<p>Things I have tried to troubleshoot the issue:</p>
<ul>
<li>I use a MacBook Air and successfully did the tutorial CTAbdomen Panoramix segmentation. I also monitored system usage using activity monitor during my MRI segmentation process and dont think I was running out of memory (though I could be wrong here).</li>
<li>I also uploaded the file to their website version in case my file/image quality was the problem and it gave me a segmentation but not of high enough quality so I wanted to try on Slicer.</li>
<li>I am checking the Fast option for now as I want to ensure it works before investing a longer time.</li>
</ul>
<p>Here is a transcript of Totalsegmentator’s processing script:</p>
<p>“Processing started</p>
<p>Writing input file to /private/var/folders/dn/rkh52q396l97m85_ts27_mm80000gn/T/Slicer-abc/__SlicerTemp__2025-09-10_10+54+07.300/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘/private/var/folders/dn/rkh52q396l97m85_ts27_mm80000gn/T/Slicer-abc/__SlicerTemp__2025-09-10_10+54+07.300/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/dn/rkh52q396l97m85_ts27_mm80000gn/T/Slicer-abc/__SlicerTemp__2025-09-10_10+54+07.300/segmentation’, ‘–ml’, ‘–task’, ‘total_mr’, ‘–fast’]</p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the `–roi_subset` option can help to reduce runtime.</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Using ‘fast’ option: resampling to lower resolution (3mm)</p>
<p>Resampling…</p>
<p>Resampled in 1.05s</p>
<p>Predicting…</p>
<p>Predicted in 21.04s</p>
<p>Resampling…</p>
<p>Saving segmentations…</p>
<p>Saved in 0.14s</p>
<p>Importing segmentation results…</p>
<p>Processing completed in 31.71 seconds</p>
<p>Cleaning up temporary folder…</p>
<p>Processing finished.”</p>
<p>Would love to hear people’s advice. Thank you!</p>

---

## Post #2 by @aceegreene (2025-09-12 14:41 UTC)

<p>Would really appreciate someone’s help with this. Thank you!</p>

---

## Post #3 by @muratmaga (2025-09-12 15:22 UTC)

<p>Can you provide the full log from Slicer?</p>
<p>Also can you check whether there the output file exists in the specified location:</p>
<aside class="quote no-group" data-username="aceegreene" data-post="1" data-topic="44433">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/6f9a4e/48.png" class="avatar"> aceegreene:</div>
<blockquote>
<p>‘/private/var/folders/dn/rkh52q396l97m85_ts27_mm80000gn/T/Slicer-abc/__SlicerTemp__2025-09-10_10+54+07.300/segmentation</p>
</blockquote>
</aside>

---

## Post #4 by @aceegreene (2025-09-13 00:08 UTC)

<aside class="quote no-group" data-username="aceegreene" data-post="1" data-topic="44433">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/6f9a4e/48.png" class="avatar"> aceegreene:</div>
<blockquote>
<p>/private/var/folders/dn/rkh52q396l97m85_ts27_mm80000gn/T/Slicer-abc/__SlicerTemp__2025-09-10_10+54+07.300/segmentation</p>
</blockquote>
</aside>
<p>Thank you for your response!</p>
<p>Here is a link for the log: <a href="https://drive.google.com/file/d/1oGLS8Z4ZTPfl-EYYPzcNWSzHg1G8AAS2/view?usp=share_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1oGLS8Z4ZTPfl-EYYPzcNWSzHg1G8AAS2/view?usp=share_link</a></p>
<p>That folder doesn’t exist anymore because Totalsegmentator clears the temporary folders it creates after its processing (at least that’s what it says in the progress panel in the module).</p>

---

## Post #5 by @muratmaga (2025-09-13 00:17 UTC)

<p>I don’t see anything unusual (apart from a warning about the DICOM geometry). So it is not clear why it is not importing the segmented object into the Slicer after the task is completed. One of the developers of the extension will need to chime in.</p>

---

## Post #6 by @aceegreene (2025-09-13 00:32 UTC)

<p>Got it, thank you for your time! What’s confusing me is their website tool gives an output but not the Slicer extension. It’s also a multivolume sequence and when I ran it on a specific echo it gave an output but it’s just a block-ish thing in the middle.</p>
<p>When I load the DICOM I do see this in the Python console: [Python] Geometric issues were found with 1 of the series. Please use caution. (which may be the warning about geometry you mentioned)</p>
<p>and these warnings in the DICOM loader:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23fa688aa91fb0fe9d5211c096218d9a8bd332c8.png" data-download-href="/uploads/short-url/58hcX4k9mMjU41hLv3Xlu594I1a.png?dl=1" title="Screenshot 2025-09-12 at 7.26.21 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23fa688aa91fb0fe9d5211c096218d9a8bd332c8_2_690x64.png" alt="Screenshot 2025-09-12 at 7.26.21 PM" data-base62-sha1="58hcX4k9mMjU41hLv3Xlu594I1a" width="690" height="64" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23fa688aa91fb0fe9d5211c096218d9a8bd332c8_2_690x64.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23fa688aa91fb0fe9d5211c096218d9a8bd332c8_2_1035x96.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23fa688aa91fb0fe9d5211c096218d9a8bd332c8_2_1380x128.png 2x" data-dominant-color="D7DCE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-09-12 at 7.26.21 PM</span><span class="informations">3418×318 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3692c12d4d986081f33fa1afd7004d55419585f.png" data-download-href="/uploads/short-url/uae4KnXupLNNLt7knGGK7on3NPF.png?dl=1" title="Screenshot 2025-09-12 at 7.26.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3692c12d4d986081f33fa1afd7004d55419585f_2_690x137.png" alt="Screenshot 2025-09-12 at 7.26.31 PM" data-base62-sha1="uae4KnXupLNNLt7knGGK7on3NPF" width="690" height="137" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3692c12d4d986081f33fa1afd7004d55419585f_2_690x137.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3692c12d4d986081f33fa1afd7004d55419585f_2_1035x205.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3692c12d4d986081f33fa1afd7004d55419585f_2_1380x274.png 2x" data-dominant-color="CDD1D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-09-12 at 7.26.31 PM</span><span class="informations">1912×380 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>not sure if it could be about that.</p>

---

## Post #7 by @aceegreene (2025-09-13 00:44 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/wasserth">@wasserth</a> would you be able to help troubleshoot this issue?</p>

---

## Post #8 by @aceegreene (2025-09-13 19:29 UTC)

<p>actually this got resolved by turning off fast mode and just letting it run full resolution. It gives a warning that it’ll run in 5-50 minutes but took like 2-3 minutes to process.</p>

---
