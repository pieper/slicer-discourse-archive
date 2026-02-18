# Problem with vmtkimagevesselenhancement to improve CT lung images and detect fissures locations?

**Topic ID**: 13022
**Date**: 2020-08-16
**URL**: https://discourse.slicer.org/t/problem-with-vmtkimagevesselenhancement-to-improve-ct-lung-images-and-detect-fissures-locations/13022

---

## Post #1 by @shahrokh (2020-08-16 11:54 UTC)

<p>Hello Dear Developers and Users</p>
<p>I want to segment lung lobes using “Intractive Lobe Segmentation” module. As mentioned in the manual of “<a href="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf" rel="noopener nofollow ugc">Interactive Lobe segmentation</a>”, I must place 2 fiducials on each of left and right obliques and right horizontal fissures in 2 or 3 different slices.</p>
<p>As seen in the following images, the quality of the slices is not enough that I can be easily detected the fissures.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6390908013680fc9ee86973c1e09d836d249ed65.jpeg" data-download-href="/uploads/short-url/ecMZQlD7SqoDIb15SukbCPlaeax.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6390908013680fc9ee86973c1e09d836d249ed65_2_598x499.jpeg" alt="Screenshot" data-base62-sha1="ecMZQlD7SqoDIb15SukbCPlaeax" width="598" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6390908013680fc9ee86973c1e09d836d249ed65_2_598x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6390908013680fc9ee86973c1e09d836d249ed65_2_897x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6390908013680fc9ee86973c1e09d836d249ed65.jpeg 2x" data-dominant-color="3B3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1113×930 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>According to the articles, I noticed that I can apply <strong>Frangi filte</strong>r using <strong>vmtkimagevesselenhancement</strong> to improve images quality.</p>
<p>For doing it, I do the following steps:</p>
<p>1- Convert DICOM files to mha file.</p>
<p>2- Execute vmtkimagevesselenhancement with the following arguments:</p>
<blockquote>
<p>vmtkimagevesselenhancement -ifile CT.mha -method frangi -alpha 0.5 -beta 0.5 -gamma 0.5 -ofile frangi.nrrd</p>
</blockquote>
<p>Everything seems to be right and I do not get error message but I do not get any output file. I do not know the reason for this. Should this filter be applied to coronal slices?</p>
<p>Please guide me or suggest me pipeline to do it.<br>
Thanks for your help.<br>
Shahrokh.</p>

---

## Post #2 by @lassoan (2020-08-16 14:46 UTC)

<p>I don’t find VMTK pypes useful, as Python scripts are already simple enough, and adding one more layer of abstraction does not simplify things much, and makes it harder to figure out what’s happening (or if something does not work - why something is not happening).</p>
<p>I would recommend to either use VMTK <code>vtkvmtkVesselnessMeasureImageFilter</code> directly in Python, or even better, use “Vesselness Filtering” module that has a convenient graphical user interface for this filter.</p>
<p>Also note that Slicer’s segmentation tools have been greatly improved since development of  CIP. You can probably separate segments by Segment Editor effects in Slicer core and SegmentEditorExtraEffects extension. For example, Surface cut effect could be useful to separate lobes.</p>

---

## Post #3 by @shahrokh (2020-08-17 12:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>use VMTK <code>vtkvmtkVesselnessMeasureImageFilter</code> directly in Python</p>
</blockquote>
</aside>
<p>Dear Andras</p>
<p>Thanks a lot for your guidance.</p>
<p>Sorry…</p>
<p>Maybe I should not mentioned my problem about vmtkimagevesselenhancement.</p>
<p>I want to enhance CT chest images to help in the detection of fissures and then locate fiducials on the fissure in the module of “Interactive Lobe Segmentation”.</p>
<p>As you told me, I get SlicerCIP4-10-2-linux and follow steps mentioned in <a href="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf" rel="noopener nofollow ugc">Interactive Lobe segmentation</a>. On the sixth page of this file, it is mentioned that “when filtering is ”on” a new frame opens up”. As you can see in the figure below, I do not have this new frame. Why?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f16ef5374e5c2875dba11e6a3328353951c2ae.png" data-download-href="/uploads/short-url/qfeE2z2G9eSuT82NfKw1Gae6AI6.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f16ef5374e5c2875dba11e6a3328353951c2ae_2_690x388.png" alt="error" data-base62-sha1="qfeE2z2G9eSuT82NfKw1Gae6AI6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f16ef5374e5c2875dba11e6a3328353951c2ae_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f16ef5374e5c2875dba11e6a3328353951c2ae_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f16ef5374e5c2875dba11e6a3328353951c2ae_2_1380x776.png 2x" data-dominant-color="7D7C7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×1080 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, you have also recommended that “use VMTK <code>vtkvmtkVesselnessMeasureImageFilter</code> directly in Python”. Where can I find the content about “Python-wrapped C++ classes” in VMTK?</p>
<p>Best regards.</p>
<p>Shahrokh</p>

---

## Post #4 by @lassoan (2020-08-17 16:11 UTC)

<p>I’ve tried Frangi vessel enhancement on chest CTs and it did not help much, so I would not recommend to use it. Maybe if the image quality is very good then it further improves visibility, but then you may not need it at all.</p>
<p>Interactive lobe segmentation displayed filtering settings on Windows in both Slicer-4.10.2 an Slicer-4.11. In Slicer-4.11 I had to make some fixes for the CIP extension to work, which should be available in the extension index tomorrow. If you have further questions about CIP lung lobe segmentation then create a new topic for it.</p>

---

## Post #5 by @shahrokh (2020-08-18 10:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="13022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Interactive lobe segmentation</p>
</blockquote>
</aside>
<p>Dear Andras<br>
Thanks a lot for your checking Frangi filter on chet Cts.</p>
<p>I check filtering options in “Interactive lobe segmentation” module in SlicerCIP (SlicerCIP4-10-2) on Windows (Windows 7 Enterprise, Service Pack 1) and Linux (Ubuntu 18.04.4 LTS). Unfortunately, I do not have this option. As mentioned you, I create new topic on SlicerCIP community with titled by “<a href="https://discourse.slicer.org/t/incomplete-options-in-slicercip-slicercip4-10-2-on-windows-windows-7-enterprise-service-pack-1-and-linux-ubuntu-18-04-4-lts/13067">Incomplete options in SlicerCIP (SlicerCIP4-10-2) on Windows (Windows 7 Enterprise, Service Pack 1) and Linux (Ubuntu 18.04.4 LTS)</a>”</p>

---

## Post #6 by @lassoan (2020-08-18 14:01 UTC)

<p>A post was merged into an existing topic: <a href="/t/incomplete-options-in-slicercip-slicercip4-10-2-on-windows-windows-7-enterprise-service-pack-1-and-linux-ubuntu-18-04-4-lts/13067/2">Incomplete options in SlicerCIP (SlicerCIP4-10-2) on Windows (Windows 7 Enterprise, Service Pack 1) and Linux (Ubuntu 18.04.4 LTS)</a></p>

---
