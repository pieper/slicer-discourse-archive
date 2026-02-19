---
topic_id: 3464
title: "Dce Only A Portion Of Voxels Are Fit"
date: 2018-07-12
url: https://discourse.slicer.org/t/3464
---

# DCE: Only a portion of voxels are fit

**Topic ID**: 3464
**Date**: 2018-07-12
**URL**: https://discourse.slicer.org/t/dce-only-a-portion-of-voxels-are-fit/3464

---

## Post #1 by @bmb777 (2018-07-12 02:24 UTC)

<p>Using the PKmodeling extension once the dynamic contrast data has been fit and the individual voxel data visually assessed a portion of the voxels are not fit. This doesn’t appear to be related to noise or data quality. To show this I attached images from 2 voxels with similar concentration profiles with only 1 having been successfully fit by the extension. Is this a expected feature of this kind of analysis? Or should I expect all voxels to be successfully fit?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5146ed45c8fcbf0d87ad4e6386a1749d3efff106.jpeg" data-download-href="/uploads/short-url/bB0DnBzOsCwOZ9mJ420MyvwuSXQ.JPG?dl=1" title="fit" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5146ed45c8fcbf0d87ad4e6386a1749d3efff106_2_690x211.JPG" alt="fit" data-base62-sha1="bB0DnBzOsCwOZ9mJ420MyvwuSXQ" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5146ed45c8fcbf0d87ad4e6386a1749d3efff106_2_690x211.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5146ed45c8fcbf0d87ad4e6386a1749d3efff106.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5146ed45c8fcbf0d87ad4e6386a1749d3efff106.jpeg 2x" data-dominant-color="F7F3EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fit</span><span class="informations">753×231 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f7ceda02aa40f07cfad630b80c04c434ee8e403.jpeg" data-download-href="/uploads/short-url/dCJ142E8HFSrHQI2SoTaBPuIzBx.JPG?dl=1" title="notfit%20example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f7ceda02aa40f07cfad630b80c04c434ee8e403_2_690x218.JPG" alt="notfit%20example" data-base62-sha1="dCJ142E8HFSrHQI2SoTaBPuIzBx" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f7ceda02aa40f07cfad630b80c04c434ee8e403_2_690x218.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f7ceda02aa40f07cfad630b80c04c434ee8e403.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f7ceda02aa40f07cfad630b80c04c434ee8e403.jpeg 2x" data-dominant-color="F7F5F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">notfit%20example</span><span class="informations">765×242 19.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @fedorov (2018-07-12 16:35 UTC)

<p><a class="mention" href="/u/bmb777">@bmb777</a> thank you for investigating this and sharing your feedback!</p>
<p>It is hard to tell what went wrong in this case. As a general answer, no - you cannot expect all voxels to be fit. But I agree with you that from the look of it, this specific voxel you identified should probably work.</p>
<p>To investigate what happened, as the first step, you should toggle generation of the diagnostic image (see Advanced options). The diagnostic image will have an error code explaining why the fit failed, as described in the documentation: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling">https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling</a> (better formatted here for readability!). Unfortunately, there are many reasons why it could have failed …</p>
<blockquote>
<p>Output map with the optimizer diagnostics. The code is encoded in 2 hex numbers. Lower 4 bits encode the optimizer errors are as follows:</p>
<ul>
<li>0: OIOIOI – failure in leastsquares function</li>
<li>1: OIOIOI – lmdif dodgy input</li>
<li>2: converged to ftol</li>
<li>3: converged to xtol</li>
<li>4: converged nicely</li>
<li>5: converged via gtol</li>
<li>6: too many iterations</li>
<li>7: ftol is too small. no further reduction in the sum of squares is possible.</li>
<li>8: xtol is too small. no further improvement in the approximate solution x is possible.</li>
<li>9: gtol is too small. Fx is orthogonal to the columns of the jacobian to machine precision.</li>
<li>10: OIOIOI: unknown info code from lmder.</li>
<li>11: optimizer failed, but diagnostics string was not recognized.</li>
</ul>
<p>Upper 4 bits encode other non-optimizer errors or notifications:</p>
<ul>
<li>16 (0x10): Ktrans was clamped to [0…5].</li>
<li>32 (0x20): Ve was clamped to [0…1].</li>
<li>48 (0x30): BAT detection failed.</li>
<li>64 (0x40): BAT at the voxel was less than AIF BAT.</li>
</ul>
</blockquote>
<p>You can also see some illustrations in these PRs (of course, it will not look as colorful and pretty for the default color map assigned to the fit diagnostic map):</p>
<ul>
<li><a href="https://github.com/millerjv/PkModeling/pull/35" class="inline-onebox">ENH: add output of the optimizer diagnostics code by fedorov · Pull Request #35 · millerjv/PkModeling · GitHub</a></li>
</ul>
<p>Let us know what you find!</p>

---

## Post #3 by @bmb777 (2018-07-14 17:32 UTC)

<p>Thank you for providing the diagnostic codes. However, I may be misunderstanding the interpretation of the output diagnostics, as the value at the pixels that are not fit but appear as if the should has a diagnostic code of 50, which isn’t provided as a error in the numbers above. Is there something I am misunderstanding?</p>

---

## Post #4 by @fedorov (2018-07-16 14:43 UTC)

<p>If you have 50, this means 48 (BAT failure) + 2 (converged to ftol).</p>
<p>You can try using <code>UseConstantBAT</code> mode in the advanced options, and set it to 7 (the frame number corresponding to the initial sharp uptake of contrast, based on the curves you share earlier).</p>
<p>Although, looking at the curve, I do not see why BAT detection would fail there. Would be good to investigate this. If you can share a sample dataset, please submit an issue and attach the dataset here: <a href="https://github.com/QIICR/PkModeling/issues/new">https://github.com/QIICR/PkModeling/issues/new</a>.</p>

---

## Post #5 by @bmb777 (2018-07-19 01:20 UTC)

<p>For that particular fit I had selected the constant batch option and set it to 7.<br>
I am currently doing a fairly intensive DCE data analysis for a conference next week. I’ll submit a sample dataset with the issue mentioned once that is completed.</p>
<p>Thanks for the information.</p>

---

## Post #6 by @fedorov (2018-07-19 03:42 UTC)

<p>Did I understand correctly - when you set BAT to 7 fit works for the affected voxels?</p>
<p>Whenever you have time to respond. Good luck with the submission!</p>

---

## Post #7 by @bmb777 (2018-07-19 15:21 UTC)

<p>No, the fits I attached in post one above were obtained using a constant BAT.  One of the reasons I was confused why the software returned a diagnostic code of failure to calculate a BAT.</p>
<p>As a secondary question, is the AUC parameter calculated based of the PK fits or the raw converted concentration versus time data? For example in the above scenario will the C v. T profile that was not fit for a voxel return a AUC value of 0 due to the failed fit?</p>

---

## Post #8 by @fedorov (2018-07-23 14:42 UTC)

<p>Sorry for the delayed reply, I know you are working on a deadline, but I was away Thu-Fri.</p>
<p>Yes, indeed AUC is calculated for the fitted signal and also relies on BAT for aligning the AIF and signal curves. Just since I had to find this to answer your question, AUC is calculated in this line: <a href="https://github.com/QIICR/PkModeling/blob/master/CLI/itkConcentrationToQuantitativeImageFilter.hxx#L394">https://github.com/QIICR/PkModeling/blob/master/CLI/itkConcentrationToQuantitativeImageFilter.hxx#L394</a>. and <code>shiftedVectorVoxel</code> is the fitted vector shifted to compensate for the BAT delay: <a href="https://github.com/QIICR/PkModeling/blob/master/CLI/itkConcentrationToQuantitativeImageFilter.hxx#L342">https://github.com/QIICR/PkModeling/blob/master/CLI/itkConcentrationToQuantitativeImageFilter.hxx#L342</a>.</p>
<p>Hope this helps.</p>

---
