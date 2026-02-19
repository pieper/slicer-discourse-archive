---
topic_id: 361
title: "Trouble Getting The Real Spacing Of A Dicom Serie Using Vtki"
date: 2017-05-23
url: https://discourse.slicer.org/t/361
---

# Trouble getting the real spacing of a DICOM serie using vtkImageData

**Topic ID**: 361
**Date**: 2017-05-23
**URL**: https://discourse.slicer.org/t/trouble-getting-the-real-spacing-of-a-dicom-serie-using-vtkimagedata/361

---

## Post #1 by @sandra (2017-05-23 09:07 UTC)

<p>Operating system: Mac<br>
Slicer version: 4.6.2</p>
<p>Hi everyone !</p>
<p>I’m currently working on my loadable module and I would need to get the real spacing of a DICOM serie using vtkImageData. I explain:</p>
<p>the user loads a DICOM serie (using DICOM module) and selects the corresponding node in my module,<br>
then I do:</p>
<pre><code class="lang-cpp">vtkMRMLScalarVolumeNode* volumeNode = vtkMRMLScalarVolumeNode::SafeDownCast(d-&gt;volumeSelector-&gt;currentNode());
vtkImageData* image = volumeNode-&gt;GetImageData();
double spacing[3];
image-&gt;GetSpacing(spacing);
</code></pre>
<p>And I get <code>spacing=[1,1,1]</code><br>
But, when the DICOM serie is loaded, I can see in the “Volumes” module that the spacing is different (something like <code>[1.5 1.5 4]</code>).</p>
<p>How can I get the real spacing of the DICOM serie in my code (and not <code>[1 1 1]</code> ) ?</p>
<p>Thank you for your help,</p>
<p>Regards,<br>
Sandra.</p>

---

## Post #2 by @lassoan (2017-05-23 11:05 UTC)

<pre><code class="lang-cpp">volumeNode-&gt;GetSpacing(spacing);
</code></pre>
<p>Unfortunately, VTK cannot store axis directions, therefore IJK to RAS transformation (origin, spacing, axis directions) has to be stored outside <code>vtkImageData</code>, in the volume node. In <code>vtkImageData</code>, origin must be kept at <code>(0,0,0)</code>, spacing must be kept at <code>(1,1,1)</code>.</p>

---

## Post #3 by @sandra (2017-05-23 11:33 UTC)

<p>“volumeNode-&gt;GetSpacing(spacing);” : that will do for what I need, thank you for these information and for your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
