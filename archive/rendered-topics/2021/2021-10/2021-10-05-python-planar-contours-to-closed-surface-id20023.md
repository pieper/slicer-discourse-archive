# Python Planar Contours to Closed Surface

**Topic ID**: 20023
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/python-planar-contours-to-closed-surface/20023

---

## Post #1 by @darcymason (2021-10-05 13:36 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.11</p>
<p>Hi,</p>
<p>I’m looking to convert RTSTRUCT contours to STL files in a Python script.<br>
If there is a simple robust path someone can point to, then great, otherwise what I have seen<br>
that looks promising is from <a href="https://discourse.vtk.org/t/mesh-from-contours/896/4" rel="noopener nofollow ugc">a 2019 discussion</a> pointing to a conversion rule class in SlicerRT.<br>
(<a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx" rel="noopener nofollow ugc">Link to the code</a>).</p>
<p>I’m quite new to Slicer and Python connections to it (and conversion rules), and I’m not sure how to find Python binding names.  Looking for something like <code>vtkPlanarContourToClosedSurfaceConversionRule</code>, I don’t see anything in the Python interactor autocomplete that mentions PlanarContour, but perhaps I have not found the right ‘path’ to get to it. I’ve tried mainly through <code>slicer.xxx</code> and <code>slicer.modules.dicomrtimportexport.xxx</code>.  There are several similar conversion rules available from the slicer object, e.g. <code>slicer.vtkBinaryLabelmapToClosedSurfaceConversionRule</code>.  Does the rule need to be registered somehow, or is it not available in current releases?</p>
<p>I’ve tried in Slicer 4.11 and in preview 4.13, both on Windows with SlicerRT extension installed.</p>
<p>Thanks in advance for any help</p>

---

## Post #2 by @cpinter (2021-10-05 13:45 UTC)

<p>I suggest you take a look at this script. The only thing you need to change is that instead of binary labelmaps you want to convert into closed surface and instead of nrrd you want to save to STL.</p>
<p><a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" class="onebox" target="_blank" rel="noopener">https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py</a></p>

---

## Post #3 by @pieper (2021-10-05 14:00 UTC)

<p>BTW, welcome <a class="mention" href="/u/darcymason">@darcymason</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>
<p>As an aside you’ll see that a lot of the dicom infrastructure in Slicer assumes you are working in Slicer’s python which historically was different from regular python.  But these days we’ve been able to re-sync things so that most pip packages ‘just work’ in Slicer.  This makes us think we might refactor Slicer dicom code for more general purpose use, but we haven’t put the work in for that yet.</p>

---

## Post #4 by @darcymason (2021-10-05 15:00 UTC)

<p>Thanks for the quick replies, and for the welcome, <a class="mention" href="/u/pieper">@pieper</a>   <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group quote-modified" data-username="cpinter" data-post="2" data-topic="20023" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I suggest you take a look at this script. The only thing you need to change is that instead of binary labelmaps you want to convert into closed surface and instead of nrrd you want to save to STL.</p>
<p><a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/BatchProcessing/BatchStructureSetConversion.py at master · SlicerRt/SlicerRT · GitHub</a></p>
</blockquote>
</aside>
<p>I had seen that before but got stuck on the conversion rule seen in the discussion I linked, but per your suggestion, it seems I could use <code>segNode.CreateClosedSurfaceRepresentation()</code>.  It appears there are no arguments to the function, so is there a way I could specify the particular rule (or does that happen to point to the one I’m interested in)?  And … a quick pointer to how to adjust settings prior (e.g. smoothing) would be very helpful.</p>
<p>Thanks again</p>

---
