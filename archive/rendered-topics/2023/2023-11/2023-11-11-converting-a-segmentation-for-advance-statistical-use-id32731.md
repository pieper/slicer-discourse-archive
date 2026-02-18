# Converting a segmentation for advance statistical use

**Topic ID**: 32731
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/converting-a-segmentation-for-advance-statistical-use/32731

---

## Post #1 by @Carson_smith (2023-11-11 01:03 UTC)

<p>Currently I am using CT scans of fish to segment their spines. I am using grow from seeds to get the best resolution and most full 3D rendering of it. Once I am able to segment the spine I am looking to do a statistical analysis of the segmentation to look for bone morphometrics and bone texture analysis. I have been able to use segment statistics, but want to go in more details with other statistical modules.</p>
<p>When using Bone Morphometry features: It will not allow me to choose an input volume to allow the module to run on my segmentation. I do not understand if I need to export my segmentation to a volume or how to go about that process.</p>
<p>When using the extension, Bone Texture: It will allow me to input my scan but will not allow me to input any segmentation. This hults me from being able to compute texture maps or the texture feature set. I am unsure if I need to export or do something after I have segmented the spine to allow for this.</p>
<p>My ultimate goal is to look for differences in bone densities for multiple CT scans of fish that have been treated with oil and have run a multi-generational population testing. Although the machine used for running these CT scans is not at the best quality, I am still able to upload the DICOM files.</p>
<p>If anyone could upload a link or give me some insight to a better workflow to achieve this goal, that would be much appreciated.</p>

---

## Post #2 by @jamieawren (2023-11-28 18:25 UTC)

<p>Hi,</p>
<p>I ran into a similar problem. You have to first convert the Segments into a binary label map. I typically do this by going to the Data module and right-clicking on a segment and selecting “export visible segments to binary label map”. Just make sure that you only have the individual segment you have selected visible, otherwise, all segments will be exported.</p>

---

## Post #3 by @muratmaga (2023-11-28 18:34 UTC)

<p>Are these scans calibrated to known phantoms? Are the values in HU? If not, all you can do is to look at the relative bone density (or bone volume fraction).</p>
<p>In Bone Texture extension, there is an option to provide input segmentation. Are you saying this is not working?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f27c877819551c45c9ed8ebdf62818b62a088f.png" data-download-href="/uploads/short-url/jfNvmtlsZS8zGqbnwVhA7CQjAqb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86f27c877819551c45c9ed8ebdf62818b62a088f.png" alt="image" data-base62-sha1="jfNvmtlsZS8zGqbnwVhA7CQjAqb" width="670" height="500" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">859×641 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2023-11-28 18:37 UTC)

<p>It appears that Bone Texture extensione expects a labelmap instead of segmentation. If you export your segmentation to labelmap it should work</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/bpaniagua">@bpaniagua</a> can you correct the wording on the UI? This is confusing for users. You should probably replace <code>Input Segmentation</code> with <code>Input labelmap</code>.</p>

---
