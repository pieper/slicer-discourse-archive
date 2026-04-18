---
topic_id: 46771
title: "Multiple Segments Into 1 3D Print"
date: 2026-04-17
url: https://discourse.slicer.org/t/46771
---

# Multiple Segments into 1 3D print

**Topic ID**: 46771
**Date**: 2026-04-17
**URL**: https://discourse.slicer.org/t/multiple-segments-into-1-3d-print/46771

---

## Post #1 by @Riley_Maurath (2026-04-17 13:51 UTC)

<p>I currently have 3 segments created in the 3D slicer and I am wanting to export them to be 3D printed. The issue I am running into are that the models are inside of each other and I am wanting to print them inside of each other using different transparent filaments. Is there a way that keeps the positioning of the three segments but also keeps them separate so they can be assigned different filaments to print? I am using the PrusaSlicer with an MMU3.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5111608632da1f582eb94789ad5bcc6f0ab3211.jpeg" data-download-href="/uploads/short-url/uoSj5GQod59NNEvZ2myuwWhwxIl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5111608632da1f582eb94789ad5bcc6f0ab3211.jpeg" alt="image" data-base62-sha1="uoSj5GQod59NNEvZ2myuwWhwxIl" width="502" height="462"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">502×462 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-04-18 00:11 UTC)

<p>You can do this quite easily by following the steps below.</p>
<h2><a name="p-133254-in-3d-slicer-1" class="anchor" href="#p-133254-in-3d-slicer-1" aria-label="Heading link"></a>In 3D Slicer</h2>
<p>It takes just a few clicks to export a multimaterial 3D-printable model from Segment Editor module:</p>
<ul>
<li>click the menu button of the green arrow button</li>
<li>click “Export to files”</li>
<li>select “File format” → STL</li>
<li>click “Export” (you will get an STL file for each segment)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a36f272ab7f5e8dd76b511fa4851438c77fe318d.png" data-download-href="/uploads/short-url/njNYfTILXYPqNHlqy8PHbe6mqJf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36f272ab7f5e8dd76b511fa4851438c77fe318d_2_690x494.png" alt="image" data-base62-sha1="njNYfTILXYPqNHlqy8PHbe6mqJf" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36f272ab7f5e8dd76b511fa4851438c77fe318d_2_690x494.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36f272ab7f5e8dd76b511fa4851438c77fe318d_2_1035x741.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36f272ab7f5e8dd76b511fa4851438c77fe318d_2_1380x988.png 2x" data-dominant-color="C0C1BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1980×1418 491 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Tip: To avoid any potential artifacts at segment boundaries, allow your segments overlap (e.g., make the tumor overlap with the brain, instead of cutting a hole in the brain where the tumor is) when you are creating your segmentation. If you get your segmentation from MONAIAuto3DSeg or other tool that creates holes instead of overlaps, then you can use “Logical operators” effect in Segment Editor to fill in those holes.</p>
<h2><a name="p-133254-in-3d-printing-slicer-application-2" class="anchor" href="#p-133254-in-3d-printing-slicer-application-2" aria-label="Heading link"></a>In 3D printing slicer application</h2>
<p>Then in your 3D printing slicer application, load all the meshes at once and set different printing settings for each mesh.</p>
<p>For example, in Cura:</p>
<ul>
<li>By default, Cura does not respect position of the models it loads (it drops everything on the build plate), so you need to go through a few extra steps to avoid this:
<ul>
<li>in menu: Preferences / Configure Cura / Automatically drop models to the build plate → uncheck</li>
<li>load all the STL files at once</li>
<li>select all the models (Ctrl-A)</li>
<li>in menu: Edit / Merge models (this brings all the models in their correct positions)</li>
<li>in menu: Edit / Ungroup models (this makes models independently editable again, but their correct position is preserved - they are not dropped to the build plate again)</li>
</ul>
</li>
<li>Specify printing settings independently for each model:
<ul>
<li>click “Per Model Settings”</li>
<li>click “Select settings” and adjust any printing parameters you like</li>
</ul>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a4e42fcae546daa7a3f694351e7fff500f100dc.png" data-download-href="/uploads/short-url/cSSE7NK0RvPFToQ3NzQcAuM9ieU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a4e42fcae546daa7a3f694351e7fff500f100dc_2_334x500.png" alt="image" data-base62-sha1="cSSE7NK0RvPFToQ3NzQcAuM9ieU" width="334" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a4e42fcae546daa7a3f694351e7fff500f100dc_2_334x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a4e42fcae546daa7a3f694351e7fff500f100dc_2_501x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a4e42fcae546daa7a3f694351e7fff500f100dc_2_668x1000.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">864×1293 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can see the different infill, pattern, filament, etc. differences in the slicing preview:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93a8527edc27022c6bc8b9d40bd98a7a1e68d676.jpeg" data-download-href="/uploads/short-url/l4eOEcrkv4ve96U0OgiBNFl8heu.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93a8527edc27022c6bc8b9d40bd98a7a1e68d676_2_690x375.jpeg" alt="image" data-base62-sha1="l4eOEcrkv4ve96U0OgiBNFl8heu" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93a8527edc27022c6bc8b9d40bd98a7a1e68d676_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93a8527edc27022c6bc8b9d40bd98a7a1e68d676_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93a8527edc27022c6bc8b9d40bd98a7a1e68d676_2_1380x750.jpeg 2x" data-dominant-color="DCC79B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1044 665 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
