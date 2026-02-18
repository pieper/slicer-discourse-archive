# Elastix registration toolbox is now available in Slicer

**Topic ID**: 165
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165

---

## Post #1 by @lassoan (2017-04-21 15:22 UTC)

<p><a href="http://elastix.isi.uu.nl/">Elastix</a> is a very powerful registration toolbox with lots of advantages over stock ITK registration tools - it has many more metrics, transformation methods, constraints, optimizers, and it comes with a large registration parameter set database, which contains optimized settings for a wide range of registration tasks.</p>
<p>This toolbox is now available in Slicer, through the SlicerElastix extension, in the latest nightly builds.</p>
<p>Even the default settings work really well for simple (same patient, same modality) and difficult cases (different modality, different field of view, even different patient), as shown in this 1-minute demo video here: <a href="https://youtu.be/cU0pWhn0-3o">https://youtu.be/cU0pWhn0-3o</a></p>
<p>Limitations: Masking will be available in tomorrow’s nightly build.  Multi-label, landmark, 4D volumes, and multi-metric inputs are not supported yet (can be added quite easily if the community needs it). Parameter set editing is manual (edit files in a directory).</p>
<p>Any feedback and suggestions are welcome.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16590a1afb6681e927f0d51513511d2bc2b058c0.jpeg" data-download-href="/uploads/short-url/3bHgLY6N02iAjvsCMogS32ECSS4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16590a1afb6681e927f0d51513511d2bc2b058c0_2_690x441.jpeg" alt="image" data-base62-sha1="3bHgLY6N02iAjvsCMogS32ECSS4" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16590a1afb6681e927f0d51513511d2bc2b058c0_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16590a1afb6681e927f0d51513511d2bc2b058c0_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16590a1afb6681e927f0d51513511d2bc2b058c0_2_1380x882.jpeg 2x" data-dominant-color="5E5F4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3000×1920 1.12 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2017-04-21 20:46 UTC)

<p>7 posts were split to a new topic: <a href="/t/elastix-registration-returns-with-failure/170">Elastix registration returns with failure</a></p>

---

## Post #3 by @cpinter (2017-04-24 13:55 UTC)

<p>This is great! The simplicity of the module makes it even more promising than BRAINS! Maybe this is the kind of news that would be worth adding to the Announcements category.</p>

---

## Post #4 by @brhoom (2017-04-27 19:07 UTC)

<p>Looks great. Elastix is one of the best registration tools. I can not find it in the extension manager, do I miss something?<br>
Quick question. did you integrate elastix within Slicer? or do you run elastix in the background? I think the first option is better as writing/reading the images from/to the hdd is time consuming.<br>
best!</p>

---

## Post #5 by @brhoom (2017-04-27 19:21 UTC)

<p>found it. I had to download the nightly build. I alsof found out that you use it in the background. It would be great if there is a cooperation between Slicer and elastix group to integrate it with-in Slicer in the future. I have some ideas to enhance the extension, I will try to contribute them soon. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @lassoan (2017-04-27 19:29 UTC)

<p>Time for reading/writing uncompressed binary files is negligible (compared to registration or resampling time), even for very large files. Generating the resampled output and displacement field are time-consuming, so that deserves some attention.</p>
<ol>
<li>I think the resampled output volume is generated twice (once by elastix, at the end of each registration phase; once by transformix at the end - these are redundant).</li>
<li>We could avoid id completely by changing Elastix to write ITK-compatible transforms or implement Elastix transform readers in SlicerElastix.</li>
</ol>
<p>Contributions are welcome!</p>

---

## Post #7 by @ihnorton (2017-04-27 21:04 UTC)

<p>2 posts were split to a new topic: <a href="/t/announcements-category-traffic/218">Announcements category traffic?</a></p>

---

## Post #8 by @lassoan (2017-11-18 05:22 UTC)

<p>A post was split to a new topic: <a href="/t/elastix-registration-returns-with-error-status/1485">Elastix registration returns with error status</a></p>

---

## Post #9 by @lassoan (2019-02-08 17:03 UTC)

<p>A post was split to a new topic: <a href="/t/model-to-image-registration/5696">Model to image registration</a></p>

---

## Post #10 by @lassoan (2019-07-02 19:13 UTC)

<p>A post was split to a new topic: <a href="/t/abdominal-ct-registration-using-elastix/7387">Abdominal CT registration using Elastix</a></p>

---

## Post #11 by @lassoan (2020-02-11 14:05 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-add-multi-metric-inputs-function-to-slicerelastix/10202">How to add multi-metric inputs function to SlicerElastix?</a></p>

---

## Post #12 by @HodaGH (2021-04-14 16:20 UTC)

<p>Hello,</p>
<p>I would like to use Simplex optimizer in Elastix but it gives an error that it’s not installed. Is it possible to include it?</p>
<p>Thank you.</p>

---

## Post #13 by @lassoan (2021-04-14 16:26 UTC)

<p>We build Elastix with default build options. If something is not enabled by default then probably there is a good reason for it (e.g., that algorithm does not perform well or its usage is discouraged for other reasons).</p>
<p>Probably simplex optimizer is not included by default because it is a very basic optimizer. It may be sufficient for very easy problems, but better quality optimizers are available (that can find more accurate results, faster). You can ask on the SimpleITK forum/mailing list to confirm and if you learn that there is good motivation to use simplex method then let us know and we’ll change the Elastix build options.</p>
<p>In the meantime, you can configure Elastix module in Slicer (in Advanced section) to use an elastix executable that you download from the Elastix website or you build yourself.</p>

---
