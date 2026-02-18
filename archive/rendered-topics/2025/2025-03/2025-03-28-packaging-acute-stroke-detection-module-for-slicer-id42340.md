# Packaging Acute Stroke Detection Module for Slicer

**Topic ID**: 42340
**Date**: 2025-03-28
**URL**: https://discourse.slicer.org/t/packaging-acute-stroke-detection-module-for-slicer/42340

---

## Post #1 by @software (2025-03-28 05:13 UTC)

<p><strong>Repository:</strong> <a href="https://github.com/Chin-Fu-Liu/Acute-stroke_Detection_Segmentation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Chin-Fu-Liu/Acute-stroke_Detection_Segmentation</a></p>
<p><strong>Problem:</strong> I want to package the Acute Stroke Detection and Segmentation (ADS) module for 3D Slicer with pre-trained models.</p>
<p><strong>Specific Challenges:</strong></p>
<ul>
<li>Including pre-trained deep learning models in the Slicer extension</li>
<li>Managing specific Python library dependencies (TensorFlow, h5py, etc.)</li>
<li>Ensuring the module works across different systems</li>
</ul>
<p><strong>Key Questions:</strong></p>
<ol>
<li>What’s the recommended way to include machine learning models in a Slicer extension?</li>
<li>How can I handle complex Python dependencies within Slicer?</li>
<li>What’s the best practice for cross-platform module packaging?</li>
</ol>
<p>Seeking guidance from experienced Slicer developers on creating a distributable, self-contained extension for this ADS tool.</p>

---

## Post #2 by @pieper (2025-03-28 14:23 UTC)

<p>Thanks for your interest in making this tool available in Slicer.  It looks like a valuable tool.  Here are some high-level answers and some comments.</p>
<p>There are many examples to look at (TotalSegmentator, Auto3DSeg, MHub, etc) so you can see that there is not yet one clear suggested architecture.  But porting your model to run inside one of those already supported frameworks could be the easiest option.  For example, retraining with MONAI Auto3DSeg would let you simply publish the model and weights.  I see you use tensorflow, which you might be able to make work, but most of the community use PyTorch, so adapting to that path would make development and maintenance easier.</p>
<p>Also I see that your model is GPL licensed.  We discourage this for many reasons (you can search the forum archives for threads on this topic).  If you absolutely must retain the GPL license, it may prevent you from using some of the distribution methods I mentioned above.</p>
<p>If you end up using GPL for any code you distribute please put a clear disclaimer of this at the top of the readme so that others don’t accidentally incorporate any of your code as this would cause problems for everyone.</p>

---

## Post #3 by @software (2025-04-08 09:54 UTC)

<p><strong>First of all, thank you, sir!</strong><br>
What is the best and easiest way to integrate it?<br>
If I want to do it, how should I proceed? Is it a straightforward process?<br>
Also, I don’t fully understand the GPL license—could you please explain what it means and whether it affects integration?</p>

---

## Post #4 by @pieper (2025-04-08 13:05 UTC)

<p>I’m not sure I can add much beyond what I said before.  There are plenty of examples that you can look at.</p>
<p>Regarding GPL, it’s a problem for many of us that even looking at GPL code could put you at risk of someone claiming you need to apply that license to all your work.  Again, it’s a well discussed topic so you can look up the arguments on all sides.</p>

---
