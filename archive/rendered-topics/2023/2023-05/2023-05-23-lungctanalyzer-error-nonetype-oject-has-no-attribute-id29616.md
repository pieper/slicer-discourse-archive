# LungCTAnalyzer error: NoneType oject has no attribute

**Topic ID**: 29616
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/lungctanalyzer-error-nonetype-oject-has-no-attribute/29616

---

## Post #1 by @Victor_Shahen (2023-05-23 22:12 UTC)

<p>Hi, I am using the Lung CT Segmenter add-on module and have had problems running it with imported CT data. Apologies, as I have never used the program before so please bear with me.</p>
<p>I am struggling to get the module to run on uploaded CT data. Here are the issues I’m encountering</p>
<ol>
<li>
<p>When I open the chest CT slices, two of the views are stretched/distorted and only one of the views has its proper dimensions.</p>
</li>
<li>
<p>When I started the module it displays this: Failed to start segmentation: ‘NoneType’ object has no attribute ‘AutoWindowLevelOff’</p>
</li>
<li>
<p>When I finished putting on the guide point on the CT slices, it displays this: Failed to compute results: ‘NoneType’ object has no attribute ‘activeEffect’</p>
</li>
</ol>
<p>My goal is just to be able to get 3D reconstructions of the lungs from CT.  Would really appreciate any help with this or if you could suggest alternative modules to use! Again apologies for having very little knowledge in this realm.</p>
<p>I installed it using the extension manager. I think it may be this: <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - rbumm/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.</a></p>

---

## Post #2 by @rbumm (2023-05-24 14:43 UTC)

<p>Please try the CTChest sample dataset first and let us here how it goes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d9dcfec46db9a47a008a5107bf62222312dbc49.png" alt="image" data-base62-sha1="hVfNhwVPuwm8XbOutsK6UH8kd6x" width="361" height="315"></p>

---
