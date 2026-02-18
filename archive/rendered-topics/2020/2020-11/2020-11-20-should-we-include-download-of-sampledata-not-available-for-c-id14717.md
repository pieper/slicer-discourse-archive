# Should we include download of SampleData not available for commercial use?

**Topic ID**: 14717
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/should-we-include-download-of-sampledata-not-available-for-commercial-use/14717

---

## Post #1 by @jcfr (2020-11-20 20:41 UTC)

<p>In both Slicer or extensions, datasets with specific restrictions can be distributed.</p>
<p>For example, the <code>CTA abdomen (Panoramix)</code> dataset coming from <a href="http://www.osirix-viewer.com/resources/dicom-image-library/">Osirix DICOM image library</a> is available for download through the SampleData module interface but it is exclusively available for research and teaching. It is not possible,  to redistribute or sell it, or use it for commercial purposes.</p>
<p>While the <code>Acknowledgement</code> section is explicit about it. See screenshot below, I suggest we update the SampleData module to (1) display a warning when used click on the download button or (2) remove datasets that are not freely available for any purpose.</p>
<p>Thoughts ?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61ec9cc424604c7fb71df9e8a0087b79a9075545.png" alt="image" data-base62-sha1="dYhfLvkoaiPofWP1b6lBHaQbt7T" width="579" height="169"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08f4d48e85944c4d9055a4c004743277ca617755.png" alt="image" data-base62-sha1="1hemHUnyBDhIBDveuYnLCWd7za5" width="180" height="152"></p>

---

## Post #2 by @pieper (2020-11-20 20:43 UTC)

<p>Maybe better (easier) to just remove it?  We can also get sample data from TCIA, probably very similar but with fewer restrictions.</p>

---

## Post #3 by @jcfr (2020-11-20 21:13 UTC)

<p>Here is a pull request: <a href="https://github.com/Slicer/Slicer/pull/5311">https://github.com/Slicer/Slicer/pull/5311</a></p>
<p>Should we also remove these datasets:</p>
<ul>
<li>
<code>Panoramix.mrb</code> from <a href="https://github.com/Slicer/SlicerDataStore/releases/tag/SHA256">SlicerDataStore</a>
</li>
<li>
<code>Panoramix-cropped.nrrd</code> from <a href="https://github.com/Slicer/SlicerTestingData/releases">SlicerTestingData</a>
</li>
</ul>

---

## Post #4 by @pieper (2020-11-20 22:01 UTC)

<p>It looks like that volume is <a href="https://github.com/Slicer/Slicer/search?q=CTAAbdomenPanoramix">used in a couple tests</a> but it should pretty easy to swap in a different volume and update the tests.  One of the tests depends on the geometry of this volume, but we could just swap in dummy pixel data into the same header if we didn’t want to update the hard coded geometry data in the test.</p>

---
