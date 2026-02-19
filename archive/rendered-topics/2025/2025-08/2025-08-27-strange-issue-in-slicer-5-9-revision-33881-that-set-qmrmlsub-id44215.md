---
topic_id: 44215
title: "Strange Issue In Slicer 5 9 Revision 33881 That Set Qmrmlsub"
date: 2025-08-27
url: https://discourse.slicer.org/t/44215
---

# Strange issue in Slicer 5.9 (revision 33881) that set qMRMLSubjectHierarchyComboBox to None

**Topic ID**: 44215
**Date**: 2025-08-27
**URL**: https://discourse.slicer.org/t/strange-issue-in-slicer-5-9-revision-33881-that-set-qmrmlsubjecthierarchycombobox-to-none/44215

---

## Post #1 by @chz31 (2025-08-27 07:02 UTC)

<p>Hi,</p>
<p>I encountered a weird issue. I made a customized extension for surgical plate registration that runs well in Slicer 5.8.1 across platforms.</p>
<p>However, in the most recent Slicer 5.9 (revision 33881), whenever I ran a button linked to a simple <a href="https://github.com/chz31/SlicerOrbitSurgerySim/blob/9cb83b2d38affc637d219b909de1675f0f96a872/plateRegistration/plateRegistration.py#L661C2-L721C55" rel="noopener nofollow ugc">fiducial rigid registration function</a> <code>onInitialRegistrationPushButton</code> (line 661), all the nodes in <code>qMRMLSubjectHierarchyComboBox</code> were set to None and I got ‘<code>NoneType</code>’ error since they are also connected to the parameter node.</p>
<p>There is no line in that function (<a href="https://github.com/chz31/SlicerOrbitSurgerySim/blob/9cb83b2d38affc637d219b909de1675f0f96a872/plateRegistration/plateRegistration.py#L661C2-L721C55" rel="noopener nofollow ugc">link to the script</a>) that set up those comboBoxes to None. The only lines relevant to the combo boxes are (see above hyperlink to the full script):</p>
<pre><code class="lang-auto">self.ui.inputOrbitModelSelector.enabled = False
self.ui.orbitFiducialSelector.enabled = False
self.ui.plateModelSelector.enabled = False
self.ui.plateFiducialSelector.enabled = False
</code></pre>
<p>However, I don’t think these are relevant. Even if I commented them out, all those comboBoxes are still set to None.</p>
<p>I tested on Windows and Mac, and the issue persists. I will test it on Linux soon.</p>
<p>To reproduce, download the <a href="https://github.com/chz31/SlicerOrbitSurgerySim" rel="noopener nofollow ugc">repository</a>and use Extension Wizard to load it to Slicer 5.9 (revision 33881). Switch to ‘plateRegistration’ module.</p>
<p>Download the sample data: <a href="https://github.com/chz31/orbitSurgeySim_sampleData/blob/main/plateRegistrationSampleData.zip" class="inline-onebox" rel="noopener nofollow ugc">orbitSurgeySim_sampleData/plateRegistrationSampleData.zip at main · chz31/orbitSurgeySim_sampleData · GitHub</a></p>
<p>Drag the files into Slicer and populate the qMRMLSubjectHierarchyComboboxes, then click the ‘Initial Registration’ button.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8644d7176c0a366293095926759eceac06b93d68.png" data-download-href="/uploads/short-url/j9Ntaz9HAZzsfPFOHKpj325mtyo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8644d7176c0a366293095926759eceac06b93d68.png" alt="image" data-base62-sha1="j9Ntaz9HAZzsfPFOHKpj325mtyo" width="517" height="200" data-dominant-color="F4F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">787×305 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df5fdeabc0d01d64f382ded26f7932f763bdb537.png" data-download-href="/uploads/short-url/vS3SjrLralTbESOQmHtknr1al39.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df5fdeabc0d01d64f382ded26f7932f763bdb537.png" alt="image" data-base62-sha1="vS3SjrLralTbESOQmHtknr1al39" width="690" height="310" data-dominant-color="F5F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">816×367 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If it runs well, it should simply disable the qMRMLSubjectHiearchyComboBoxes without setting it to None:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44afd9d09ffa7c1ed194cc9c970a7e02c485c93c.png" data-download-href="/uploads/short-url/9NDe3lqMJBelgPPD7izpBZzBEPq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44afd9d09ffa7c1ed194cc9c970a7e02c485c93c_2_517x94.png" alt="image" data-base62-sha1="9NDe3lqMJBelgPPD7izpBZzBEPq" width="517" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44afd9d09ffa7c1ed194cc9c970a7e02c485c93c_2_517x94.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44afd9d09ffa7c1ed194cc9c970a7e02c485c93c_2_775x141.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44afd9d09ffa7c1ed194cc9c970a7e02c485c93c.png 2x" data-dominant-color="F6F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">782×143 11.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @chz31 (2025-08-27 20:42 UTC)

<p>I found a version of Slicer 5.9.0 in my Linux computer built in 07-25. Interestingly, there was no such issue of automatically setting the qMRMLSubjectHierarchyComboBox to None.</p>

---
