# Inquiry Regarding Measurement of Functional Tumor Volume in Breast using 3D Slicer

**Topic ID**: 31188
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/inquiry-regarding-measurement-of-functional-tumor-volume-in-breast-using-3d-slicer/31188

---

## Post #1 by @thomas_su (2023-08-17 05:53 UTC)

<p>Dear 3D Slicer Community,<br>
Currently, I am delving into the realm of measuring Functional Tumor Volume (FTV) in breast tumors, along with parameters like Percentage of Enhancement (PE) and Signal Enhancement Ratio (SER). As an avid user of 3D Slicer, I am intrigued to know if there exists a suitable module or method within 3D Slicer that could aid me in accurately measuring these parameters.<br>
Given the complexity of breast tumor analysis and the specific focus on functional aspects, I would greatly appreciate any insights, guidance, or suggestions from the experienced members of this community. If there are any existing tools, extensions, or workflows within 3D Slicer that can assist in this process, I would be keen to learn more about them. Additionally, if there are any recommended best practices or resources related to measuring FTV, PE, and SER in the context of breast tumors, I would be very interested in exploring them.<br>
Thank you in advance for your time and expertise. Your input would undoubtedly contribute to the advancement of my research endeavors. I look forward to engaging in discussions and learning from the collective knowledge of this community.</p>

---

## Post #2 by @pieper (2023-08-17 17:35 UTC)

<p>There are several PET related extensions (type PET in the search bar of the extension dialog) but I don’t know if they cover what you are looking for.  Most of them have references to papers about how they can be used.</p>

---

## Post #3 by @thomas_su (2023-08-18 05:03 UTC)

<p>Thank you very much.<br>
Actually, I was looking for a module for breast MRI. However, I will try to research some PET-related modules. Perhaps there are some solutions.</p>

---

## Post #4 by @pieper (2023-08-18 12:36 UTC)

<aside class="quote no-group" data-username="thomas_su" data-post="3" data-topic="31188">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thomas_su/48/67176_2.png" class="avatar"> thomas_su:</div>
<blockquote>
<p>looking for a module for breast MRI</p>
</blockquote>
</aside>
<p>Ah, I see - I assume this is time series data then, and there’s a lot of infrastructure for plotting and analyzing volume sequences (e.g. for prostate) that you may find useful, but maybe more development required for specific uses in the breast.</p>

---
