# Error when running MONAI Auto3DSeg (cannot import name ‘MetaKeys’ from ‘monai.utils’)

**Topic ID**: 35738
**Date**: 2024-04-25
**URL**: https://discourse.slicer.org/t/error-when-running-monai-auto3dseg-cannot-import-name-metakeys-from-monai-utils/35738

---

## Post #1 by @davidngqk88 (2024-04-25 14:21 UTC)

<p>Am testing it on some abdominal CT datasets now.</p>
<p>am getting errors saying<br>
ImportError: cannot import name ‘MetaKeys’ from ‘monai.utils’<br>
‘Processing failed with return code 1’<br>
after it attempts to create the segmentations.</p>
<p>What is error code 1?</p>

---

## Post #2 by @lassoan (2024-04-25 14:49 UTC)

<p>The non-zero error code just means that the processing failed. The error message indicates that your MONAI package installation is corrupted (or you manually installed some very old version of MONAI).</p>
<p>Could you please open the <code>Advanced</code> section, click the <code>Get Python package information</code> button, and copy here the contents of the textbox?</p>
<p>Have you installed Anaconda on your computer? On Windows, it can overwrite lot of system settings on your computer that may break other Python environments, so if you have Anaconda installed then you may try temporarily renaming the top-level Anaconda installation folder, restart Slicer, and retry the segmentation.</p>

---

## Post #3 by @davidngqk88 (2024-04-25 14:52 UTC)

<p>here it is. I dont have anaconda installed.</p>
<p>Name: monai</p>
<p>Version: 0.9.0</p>
<p>Summary: AI Toolkit for Healthcare Imaging</p>
<p>Home-page: <a href="https://monai.io/" rel="noopener nofollow ugc">https://monai.io/</a></p>
<p>Author: MONAI Consortium</p>
<p>Author-email: <a href="mailto:monai.contact@gmail.com">monai.contact@gmail.com</a></p>
<p>License: Apache License 2.0</p>
<p>Location: c:\users\XXX\appdata\local\slicer.org\slicer 5.6.1\lib\python\lib\site-packages</p>
<p>Requires: numpy, torch</p>
<p>Required-by:</p>

---

## Post #4 by @diazandr3s (2024-04-25 16:00 UTC)

<p>Hi <a class="mention" href="/u/davidngqk88">@davidngqk88</a>,</p>
<p>This is strange.<br>
I’d suggest you download the latest Preview Slicer and do a clean installation of the MONAI Auto3DSeg extension.</p>
<p>Please let us know,</p>

---

## Post #5 by @lassoan (2024-04-25 18:45 UTC)

<p>Yes, MONAI Auto3DSeg is only supported with the latest Slicer Stable Release and latest Slicer Preview Release. Your Slicer version is 5.6.1 (the current stable is 5.6.2), so your Slicer has not been receiving any of the extension updates for a good while and your MONAI Auto3DSeg extension is an early prototype version.</p>

---

## Post #6 by @MGoryawala (2025-07-09 16:37 UTC)

<p>Hi All,</p>
<p>Wondering if this issue was resolved.</p>
<h2><a name="p-126630-getting-a-similar-error-while-running-the-brain-tumor-segmentation-brats-gli-module-1" class="anchor" href="#p-126630-getting-a-similar-error-while-running-the-brain-tumor-segmentation-brats-gli-module-1" aria-label="Heading link"></a>Getting a similar error while running the Brain Tumor Segmentation (BRATS) GLI module.</h2>
<p>Initializing</p>
<p>Segmenting</p>
<p>Process Started</p>
<p><code>apex.normalization.InstanceNorm3dNVFuser</code> is not installed properly, use nn.InstanceNorm3d instead.</p>
<p>Model epoch 176 metric 0.9485230445861816</p>
<h2><a name="p-126630-processing-failed-with-error-code-1-please-check-logs-for-further-information-2" class="anchor" href="#p-126630-processing-failed-with-error-code-1-please-check-logs-for-further-information-2" aria-label="Heading link"></a>Processing failed with error code [1]. Please check logs for further information.</h2>
<h2><a name="p-126630-the-python-package-information-is-3" class="anchor" href="#p-126630-the-python-package-information-is-3" aria-label="Heading link"></a>The Python Package information is:</h2>
<p>Name: monai</p>
<p>Version: 1.5.0</p>
<p>Summary: AI Toolkit for Healthcare Imaging</p>
<p>Home-page: <a href="https://monai.io/" rel="noopener nofollow ugc">https://monai.io/</a></p>
<p>Author: MONAI Consortium</p>
<p>Author-email: <a href="mailto:monai.contact@gmail.com">monai.contact@gmail.com</a></p>
<p>License: Apache License 2.0</p>
<p>Location: c:\users\xxxxx\appdata\local\slicer.org\slicer 5.8.1\lib\python\lib\site-packages</p>
<p>Requires: numpy, torch</p>
<h2><a name="p-126630-required-by-4" class="anchor" href="#p-126630-required-by-4" aria-label="Heading link"></a>Required-by:</h2>
<p>My slicer version details are:</p>
<p>Slicer</p>
<p>5.8.1 r33241 / 11eaf62</p>

---
