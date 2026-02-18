# 3D Slicer Extension: Is it required to have an API key to contribute an extension?

**Topic ID**: 1256
**Date**: 2017-10-20
**URL**: https://discourse.slicer.org/t/3d-slicer-extension-is-it-required-to-have-an-api-key-to-contribute-an-extension/1256

---

## Post #1 by @algohary (2017-10-20 17:28 UTC)

<p>Hi,</p>
<p>I am trying to upload a Slicer plugin (Radiomics plugin, Collage, that I developed at Case Western Reserve University) to the Extension Serve. I am contacting you regarding gaining access. I use my email and API key but with no success. If was wondering if you can help with some directions.</p>
<p>Thanks,<br>
Ahmad Algohary<br>
PhD Candidate, BME<br>
Case Western Reserve University</p>

---

## Post #2 by @fedorov (2017-10-21 01:09 UTC)

<p><a class="mention" href="/u/algohary">@algohary</a> API key is not required to contribute the extension. You only need it “if you want to upload test data to MIDAS or troubleshoot extension upload problems”, as you can read in the instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions</a></p>
<p>In most cases it is not needed. Do you have a Slicer extension that is functional and works on your computer? Do you have a pointer to the public source code repository for that extension?</p>
<p>If this is a set of specific radiomics features, you could consider contributing it to the <a href="http://pyradiomics.readthedocs.io/en/latest/">pyradiomics</a> instead of making a new extension. This way your set of features will automatically become accessible from the SlicerRadiomics extension. If you share the pointers to your source code and what exactly you want to accomplish, it would be easier to help you.</p>

---
