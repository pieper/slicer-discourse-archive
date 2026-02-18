# RTstruct not showing contour

**Topic ID**: 1926
**Date**: 2018-01-24
**URL**: https://discourse.slicer.org/t/rtstruct-not-showing-contour/1926

---

## Post #1 by @mmtg (2018-01-24 21:12 UTC)

<p>Hi everyone,</p>
<p>I am using the segmentations module in 3DSlicer v 4.8.0. I have contours that were made in MIM and I am exporting the RTStruct to 3DSlicer. One of the contours is rather small and when I load it into 3DSlicer, it doesn’t show the contour that I can see in MIM. I don’t know why this is and am confident it’s not in exporting the file from MIM as I have other contours that work just fine.</p>
<p>Let me know what I need figure this out, thanks!</p>

---

## Post #2 by @gcsharp (2018-01-24 22:16 UTC)

<p>Hi mmtg,</p>
<p>I can’t think of any obvious reason.</p>
<p>Is there any error in the error log?</p>
<p>Is an (apparently empty) segment created?</p>
<p>Would you be able to anonymize and share the data?</p>
<p>Greg</p>

---

## Post #3 by @mmtg (2018-01-25 18:53 UTC)

<p>Hi, sorry I am not ignoring your response. I am making sure I have the ethics to send anonymized data. If I were to supply just the RTstruct, would that be helpful (if I can’t send the CT it was generated on)?</p>

---

## Post #4 by @lassoan (2018-01-25 19:06 UTC)

<p>Yes, absolutely. Getting the RT struct should be enough.</p>

---

## Post #5 by @mmtg (2018-01-25 21:01 UTC)

<p>I can send the anonymized RTStruct at this point (still waiting for lead PI on ethics of anonymized CT). Who should I send it to? I’d rather not post a link here.</p>

---

## Post #6 by @cpinter (2018-01-25 21:16 UTC)

<p>You can send it to me: <a href="mailto:csaba.pinter@queensu.ca">csaba.pinter@queensu.ca</a>. I’m a SlicerRT developer, just as Andras and Greg who answered before. Please make sure that the anonymized dataset produces the samme issue as the original. Thanks!</p>

---

## Post #7 by @cpinter (2018-01-27 14:57 UTC)

<p><a class="mention" href="/u/mmtg">@mmtg</a> Thanks for the data! However I don’t think it is suitable for debugging your issue.</p>
<ul>
<li>The only ROI in the dataset you sent me seems to contain less information than what is enough to calculate the spacing between the contours in itself (see error message “Input polydata has less than two cells! Unable to calculate spacing” - in general it is good practice to look at the log when anything unexpected happens and try to figure out the issue from there, but at least send it to us)</li>
<li>Usually the RTSTRUCT comes with a CT, which SlicerRT uses as additional information to determine the spacing. However you only sent the RTSTRUCT, so reading it in happens in a different way than if the CT is also available</li>
</ul>
<p>Can you please give us more information?</p>
<ul>
<li>What does “rather small” mean for your contours? How many slices do they span?</li>
<li>Do you segment a CT? If so, do you export it as well?</li>
<li>Please send us a dataset that you actually segmented in MIM (and exported ideally along with the CT), and also send us a screenshot what it supposed to look like</li>
</ul>
<p>Thanks!</p>

---

## Post #8 by @mmtg (2018-01-27 16:53 UTC)

<p>Hi thanks for taking a look.</p>
<p>In this case the contour only spanned 1 slice and, on the original CT is probably about 30 voxels or so… Just from memory. One problem is that I think MIM tends to interpolate the volumes heavily and so I am wondering if the coordinates specified don’t actually correspond to any physical space in the original CT… But again that’s just a guess and I am naive in how this works.</p>
<p>The CT is segmented and exported with the RT struct. Both are loaded at the same time.</p>
<p>I will attempt to use one of the sample data sets in Slicer, export to MIM, contour a small volume, and then re-import to slicer to see if I can recreate it. Unfortunately the main PI on this case is away from email and I haven’t got a response about sending the anonymized CT data.</p>
<p>I will hopefully be able to do this monday morning. Thanks for your time so far.</p>

---

## Post #9 by @cpinter (2018-01-27 19:01 UTC)

<aside class="quote no-group" data-username="mmtg" data-post="8" data-topic="1926">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5e925/48.png" class="avatar"> mmtg:</div>
<blockquote>
<p>Both are loaded at the same time</p>
</blockquote>
</aside>
<p>In that case please send the anatomical volume too, because loading the RTSTRUCT alone yields a different result.</p>
<p>It’s a good idea to start from a sample dataset to work around patient confidentiality issues. Thanks!</p>

---

## Post #11 by @cpinter (2018-01-29 20:29 UTC)

<p>Thanks for the new data! I was able to determine the problem. It’s that due to the single-sliceness of the segmentation the contours-&gt;surface conversion algorithm is unable to do the “end-capping” step properly, because when it fails to calculate the contour thickness, it defaults to 0mm. So end-capping is done with 0mm thickness, and so while it is done, the surface will remain completely flat (see screenshot; the wireframe shows the end-capping).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38c5ff2d337d14f3fa23c476a13f3a08e40be62d.png" alt="image" data-base62-sha1="86eWyE9tUVdmwTfeBTn5e6wwN0F" width="368" height="344"></p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> will do a fix that sets a default slice thickness to the conversion algorithm for cases like this.</p>
<p>In the meantime you can probably fall back to the “ribbon” method, I’ll provide you a script shortly if I manage to make it work.</p>

---

## Post #12 by @cpinter (2018-01-29 21:19 UTC)

<p>The ribbon method yields a segment that looks nicer and that allows labelmaps to be created. The segment’s volume was calculated to be 0.209cc, which is about half of what you said it is in MIM. This makes complete sense if we consider interpolation (i.e. the aforementioned end-capping, which is performed in this scenario as well), instead of the raw ribbon method.</p>
<p>I had to do one fix in the ribbon converter as well. It required at least two cells in the polydata, but I don’t know why so I decreased it to one (<a class="mention" href="/u/lassoan">@lassoan</a> any ideas?) and now it works well. You’ll be able to try it with tomorrow’s nightly. Also you’ll need to disable the direct conversion that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is fixing now. You can do it by entering this in the python interactor before loading the data, or adding this to .slicerrc.py. However this is a temporary workaround in case you’re in a rush.</p>
<pre><code>f=slicer.vtkSegmentationConverterFactory()
f.DisableConverterRule('Planar contour', 'Closed surface')
</code></pre>
<p>It will look like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9886070986932b1d2364e4f6c6d0033c5e13957.jpeg" data-download-href="/uploads/short-url/qtiw6rbKwA7Y1SFPEgFEeIA5uIv.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9886070986932b1d2364e4f6c6d0033c5e13957_2_532x500.jpg" alt="image" data-base62-sha1="qtiw6rbKwA7Y1SFPEgFEeIA5uIv" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9886070986932b1d2364e4f6c6d0033c5e13957_2_532x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9886070986932b1d2364e4f6c6d0033c5e13957_2_798x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9886070986932b1d2364e4f6c6d0033c5e13957.jpeg 2x" data-dominant-color="A9A5B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×810 80.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2018-01-29 21:23 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="1926">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>It required at least two cells in the polydata, but I don’t know why</p>
</blockquote>
</aside>
<p>I guess 2 contours were required so that we can compute slice thickness, but it is better to compute thickness from the CT image anyway.</p>

---

## Post #14 by @cpinter (2018-01-29 21:26 UTC)

<p>Makes sense. Also the slice thickness calculator function has been significantly improved, so it can calculate it multiple ways. The 2 cell restriction shouldn’t be needed I think. Thanks!</p>

---

## Post #15 by @mmtg (2018-01-29 21:38 UTC)

<p>Thanks very much for this! I will install the nightly - hopefully my script to batch convert these RTStructs into binaries still works. Glad this worked out!</p>

---

## Post #16 by @Sunderlandkyl (2018-01-29 21:58 UTC)

<p>The underlying issue has been fixed (Slice thickness now defaults to image slice spacing instead of 0.0).</p>
<p>You should be able to use the default conversions tomorrow in the next nightly, without needing the workaround that Csaba posted.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe4f2359c6783e99b417b3fd3e5b256a48c86a2c.jpeg" data-download-href="/uploads/short-url/AhIPsMc2J4hkKiRRdWFX4pj0Ubi.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe4f2359c6783e99b417b3fd3e5b256a48c86a2c_2_690x499.jpg" alt="image" data-base62-sha1="AhIPsMc2J4hkKiRRdWFX4pj0Ubi" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe4f2359c6783e99b417b3fd3e5b256a48c86a2c_2_690x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe4f2359c6783e99b417b3fd3e5b256a48c86a2c_2_1035x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe4f2359c6783e99b417b3fd3e5b256a48c86a2c.jpeg 2x" data-dominant-color="ABA7B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1255×909 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
