---
topic_id: 8450
title: "Slicersalt 2 2 1 Release Summary And Changelog"
date: 2019-09-16
url: https://discourse.slicer.org/t/8450
---

# SlicerSALT 2.2.1 Release: Summary and Changelog

**Topic ID**: 8450
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/slicersalt-2-2-1-release-summary-and-changelog/8450

---

## Post #1 by @bpaniagua (2019-09-16 18:32 UTC)

<p>The SlicerSALT team is proud to announce that version 2.2.1 is <a href="http://salt.slicer.org/download">now available for download</a>. This release introduces new features in almost all of our modules as well as dozens of bug fixes for better performance and stability. The development of SlicerSALT is supported by the NIH National Institute of Biomedical Imaging Bioengineering <a href="https://projectreporter.nih.gov/project_info_description.cfm?aid=9741133&amp;icde=46482797&amp;ddparam=&amp;ddvalue=&amp;ddsub=&amp;cr=3&amp;csb=default&amp;cs=ASC&amp;pball=">R01EB021391</a> (Shape Analysis Toolbox for Medical Image Computing Projects).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/035c2d5a9b9078944a5f2d9538b7dde39f159af2.png" data-download-href="/uploads/short-url/tIV6BJ2GE0rXemMWLOSUqsLIlA.png?dl=1" title="25%20PM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035c2d5a9b9078944a5f2d9538b7dde39f159af2_2_690x391.png" alt="25%20PM" data-base62-sha1="tIV6BJ2GE0rXemMWLOSUqsLIlA" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035c2d5a9b9078944a5f2d9538b7dde39f159af2_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035c2d5a9b9078944a5f2d9538b7dde39f159af2_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035c2d5a9b9078944a5f2d9538b7dde39f159af2_2_1380x782.png 2x" data-dominant-color="C7C7DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">25%20PM</span><span class="informations">1680×953 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Improved population analysis module. It now allows to easily perform shape space exploration in all the main modes of variation within a population of geometries.</p>
<h1><a name="p-29683-changelog-1" class="anchor" href="#p-29683-changelog-1" aria-label="Heading link"></a><strong>Changelog</strong></h1>
<p><strong>Features</strong></p>
<ul>
<li>
<p>Python 3.0 support</p>
<ul>
<li>Improve all modules to support Python 3.x</li>
</ul>
</li>
<li>
<p>Improved jump-start with each SALT module</p>
<ul>
<li>We added tutorial tab to each module that allows automatically downloading and visualizing example data for each module, as well as loading the tutorial associated to the tool</li>
</ul>
</li>
<li>
<p><a href="https://blog.kitware.com/slicersalt-surface-toolbox-revamp/">Improved SurfaceToolbox with new filters</a></p>
</li>
<li>
<p>Shape Variation Analyzer</p>
<ul>
<li>Shape PCA browser</li>
<li>Shape PCA plots</li>
</ul>
</li>
<li>
<p>Data Importer</p>
<ul>
<li>Add support for automatically importing and visualizing freesurfer segmentations</li>
<li>Add support for selecting template geometry</li>
<li>Add scene observers so we can select which subject is used as template</li>
</ul>
</li>
<li>
<p>Shape statistics</p>
<ul>
<li>Improve GUI for a more streamlined use</li>
</ul>
</li>
<li>
<p>Skeletal representations</p>
<ul>
<li>Improve s-rep fitting mechanism to support initial fitting as well as adjustment or interpolation of the fit. The previous version included only an initializer and a viewer.</li>
</ul>
</li>
<li>
<p>Shape Population Viewer</p>
<ul>
<li>Improve user experience by integrating the shape population viewer within the SlicerSALT layout and by removing the disrupting pop-up.</li>
</ul>
</li>
<li>
<p>Improve extension integration</p>
<ul>
<li>Create a new architecture to obtain dependencies for each module in SlicerSALT. We have a system of mirrors of each original repository for each module. This allows to have a centralized and stable codebase for the methodology.</li>
</ul>
</li>
</ul>
<h2><a name="p-29683-fixes-2" class="anchor" href="#p-29683-fixes-2" aria-label="Heading link"></a><strong>Fixes</strong></h2>
<ul>
<li>
<p>Shape statistics crash fixes and stability</p>
</li>
<li>
<p>Data importer stability changes,</p>
<ul>
<li>
<p>Add observer that will clear the module when the scene is closed</p>
</li>
<li>
<p>Improve multi subject selection</p>
</li>
</ul>
</li>
<li>
<p>Shape Population viewer had bugs in the color customization that have now been fixed</p>
</li>
<li>
<p>Rename/re-categorize SlicerSALT modules <a href="https://github.com/Kitware/SlicerSALT/commit/531328bfc72c90fc08cac96212ac2a802c98f8aa">[commit]</a></p>
</li>
<li>
<p>Disable non-shape modules from Slicer that still remained in SlicerSALT 1.0.0</p>
</li>
<li>
<p>Rigid alignment module bug and stability fixes</p>
</li>
</ul>
<h1><a name="p-29683-acknowledgements-3" class="anchor" href="#p-29683-acknowledgements-3" aria-label="Heading link"></a><strong>Acknowledgements</strong></h1>
<ul>
<li>UNC
<ul>
<li>Martin Styner &amp; lab</li>
<li>Steve Pizer &amp; lab</li>
<li>Tengfei Li</li>
</ul>
</li>
<li>NYU Tandon School of Engineering
<ul>
<li>James Fishbaugh</li>
<li>Guido Gerig</li>
</ul>
</li>
<li>Kitware
<ul>
<li>Beatriz Paniagua</li>
<li>Jared Vicory</li>
<li>Jean-Christophe Fillion-Robin</li>
<li>Sam Horvath</li>
</ul>
</li>
</ul>

---

## Post #2 by @bpaniagua (2019-09-16 18:33 UTC)



---
