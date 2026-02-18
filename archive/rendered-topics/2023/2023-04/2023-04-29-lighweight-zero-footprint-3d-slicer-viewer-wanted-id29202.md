# Lighweight "zero footprint" 3D Slicer viewer wanted

**Topic ID**: 29202
**Date**: 2023-04-29
**URL**: https://discourse.slicer.org/t/lighweight-zero-footprint-3d-slicer-viewer-wanted/29202

---

## Post #1 by @rbumm (2023-04-29 03:56 UTC)

<p>For day clinical work it would be awesome (maybe wrong word - required)  to have a lightweight, streamlined, fast, optimized, pretty,  small  preferable HTLM-5 or gradio based 3D  SLicer viewed available, which does nothing but</p>
<ul>
<li>display of slices ,</li>
<li>threedview and tables,</li>
<li>basic cropping,</li>
<li>windowing,</li>
<li>measurements,</li>
<li>labels</li>
<li>tables</li>
<li>GPU requirements should be minimal and be orientated at available PACS browsers</li>
</ul>
<p>This reader should be FDA-approved.</p>
<p>It should be callable in a Chromium browser, HTML5 or gradio based, and should accept arguments such as passing data files or patient IDs, etc to enable the call from HIS systems. A threedview would be mandatory. MPR would be great. Cine would be mandatory. Saving videos ffmpeg videos or screenshots too. It must be highly configurable, should offer themes,  in all aspects and keyboard shortcuts.<br>
No Python or Python console.</p>
<p>It should be updated only once a year and the update should be fully automatic.</p>
<p>No extensions.</p>
<p>It should offer speech-to-text transcription with one of the more spread llm and the ability to build up a ChatGPT connection if API key is provided into a password or settings field.<br>
Mainly a pure display tool for DCM, nrrd, mrb, glTF, obj, stl 3D data formats.<br>
Segmentation list box with on off checkboxes.</p>
<p>Things to avoid: Docker, Jupyter etc. Too complicated to setup and maintain in a hospital.<br>
It should support user authentication and user action logging.<br>
It should be passable with data folders with just a few DLLs.</p>
<p>Best<br>
r.</p>

---

## Post #2 by @pll_llq (2023-04-29 10:53 UTC)

<p>Looks like this is what <a href="https://viewer.ohif.org/" rel="noopener nofollow ugc">ohif</a> is meant to be.</p>
<p>I don’t know if there are means in slicer to satisfy the browser/html5 requirement</p>

---

## Post #3 by @pieper (2023-04-29 13:10 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a> - yes, <a class="mention" href="/u/pll_llq">@pll_llq</a> is correct, OHIF is an effort in that direction.  Several of us in the Slicer community also work with OHIF and use it in various projects.  For example the viewer integrated in the <a href="https://portal.imaging.datacommons.cancer.gov/">Imaging Data Commons</a> is based on OHIF.</p>
<p>Regarding FDA approval, OHIF is a lot like Slicer in the sense that it’s an open source platform that can be used to make commercial products.  There are several systems that make use of OHIF already, but one that may address your interests is <a href="https://flexview.ai/">FlexView</a>.</p>

---

## Post #4 by @rbumm (2023-04-29 15:37 UTC)

<p>Does OHIF have a 3D display that can be rotated in all axes? Did not see one, but there might be an extension …</p>

---

## Post #5 by @pieper (2023-04-29 16:26 UTC)

<p><a href="https://v3-docs.ohif.org/">OHIF version 3</a> (try the <a href="https://v3-demo.ohif.org/">demo here</a>) has been in development for a while now and has some very good 3D features.  It is based on <a href="https://kitware.github.io/vtk-js/index.html">vtk.js</a>, the javascript version of the C++ VTK that we use in Slicer, and OHIF v3 is extensible so new features can be exposed, like <a href="https://v3-demo.ohif.org/tmtv?StudyInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.7009.2403.871108593056125491804754960339">this MIP PET/CT example</a>.  Both Kitware’s <a href="https://kitware.github.io/glance/">Glance</a> and <a href="https://github.com/Kitware/VolView">VolView</a>  use vtk.js as well, so there’s a lot of synergy and features that are in any of the systems can in principle be migrated to any of the others with enough effort.  They all have different goals so their user interfaces differ, and I think that of these FlexView is the one that is closest to what you are looking for (FDA cleared and supported for clinical use, but there may be others).</p>
<p>There’s more about OHIF in this paper: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7259879/" class="inline-onebox">Open Health Imaging Foundation Viewer: An Extensible Open-Source Framework for Building Web-Based Imaging Applications to Support Cancer Research - PMC</a></p>
<p>One goal for me and others has been to use DICOM objects to enable standards-based interoperability between Slicer and OHIF.</p>

---

## Post #6 by @lassoan (2023-04-30 13:06 UTC)

<p>You describe almost exactly what a radiology image viewer web application is. It is a very popular product category, which is slowly replacing desktop viewers, as web viewer capabilities expand, they are more mobile friendly, can leverage web technology stacks, and easier for IT departments to manage. There are hundreds of commercial systems offering such solutions (all PACS vendors and many other companies) and there are 5-10 open-source projects with similar goals. There may be just a very few specific requirements that are unlikely to be fulfilled (e.g., update limited to once a year, research/consumer file support in a clinical system, FDA approval for a community-supported project).</p>
<p>Slicer is in a different product category. It is an “advanced workstation”. It offers more features and has more resource needs and does not have be that mobile (no need for all the features in a phone).</p>
<p>I expect that the line between these two product categories will get more and more blurry in the coming years, because web applications will get more capabilities, desktop applications will become more web-friendly and web browser catches up to desktop operating systems. However, they fulfill quite different set of needs, so probably both will remain distinct categories for a good while.</p>

---
