# Feature: Custom library to extract radiomic features at specific angle

**Topic ID**: 32819
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/feature-custom-library-to-extract-radiomic-features-at-specific-angle/32819

---

## Post #1 by @Mohanad_Arafe (2023-11-14 20:20 UTC)

<p>Hello everyone,</p>
<p>In my research, I am using PyRadiomics to extract radiomic features at specific angles (2D for now) &amp; distance. Therefore, I implemented a small library that helps you do so. Here is an example of how to use it:</p>
<pre><code class="lang-auto">from RadiomicsHelper import RadiomicsHelper
import SimpleITK as sitk

helper = RadiomicsHelper(image, mask, binCount=32, distance=[1])

# Get index of all 2D angles
angles = helper.getAngleIndex()
print(angles)
&gt;&gt; {135: 1, 90: 4, 45: 7, 0: 10}

# Get contrast value at 45 degrees
helper.getContrastFeatureValue(angles[45])
&gt;&gt; 23.42705042892648

# Get correlation value at 135 degrees
helper.getCorrelationFeatureValue(angles[135])
&gt;&gt; 0.543999809502995
</code></pre>
<p>If this seems something of interest or worthy of a PR, please do let me know and we can discuss.</p>
<p>Thank you,<br>
Mohanad</p>
<p>Github: mohanadarafe</p>

---
