---
topic_id: 12748
title: "Slicersalt 3 0 Release Summary And Changelog"
date: 2020-07-27
url: https://discourse.slicer.org/t/12748
---

# SlicerSALT 3.0 Release: Summary and Changelog

**Topic ID**: 12748
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/slicersalt-3-0-release-summary-and-changelog/12748

---

## Post #1 by @bpaniagua (2020-07-27 13:39 UTC)

<p>The SlicerSALT team is proud to announce that version 3.0 is <a href="http://salt.slicer.org/download">now available for download</a>. This release introduces new features as well as bug fixes for better performance and stability. The development of SlicerSALT is supported by the NIH National Institute of Biomedical Imaging Bioengineering <a href="https://projectreporter.nih.gov/project_info_description.cfm?aid=9741133&amp;icde=46482797&amp;ddparam=&amp;ddvalue=&amp;ddsub=&amp;cr=3&amp;csb=default&amp;cs=ASC&amp;pball=">R01EB021391</a> (Shape Analysis Toolbox for Medical Image Computing Projects).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://lh3.googleusercontent.com/v_UsqDukPzKRSICKUH5hPh5B4nG6iXTwIsJZxvNHcgu5bQb00E8Rbi8nhtdnznxUS410K95haLThsx2KoWY-ycCQxLcx-mrDZaPNdbvwJ48GYmFzp_AwjY0LUmi0SHkTFaUEQyUb" title="|624x336.00000000000006"><img src="https://lh3.googleusercontent.com/v_UsqDukPzKRSICKUH5hPh5B4nG6iXTwIsJZxvNHcgu5bQb00E8Rbi8nhtdnznxUS410K95haLThsx2KoWY-ycCQxLcx-mrDZaPNdbvwJ48GYmFzp_AwjY0LUmi0SHkTFaUEQyUb" alt="|624x336.00000000000006" width="690" height="371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">|624x336.00000000000006</span><span class="informations">1600×862</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg></div></a></div><br>
<em>Registration based correspondence module: a) Interface. The user only needs to provide a template object, a folder containing meshes of the target objects, and a folder to store the resulting meshes in. b) The resulting correspondent meshes for a group of mice femurs obtained from microCT, colored by point order. The consistency of the colors across cases shows that the meshes are in good correspondence. Thanks to <a href="https://www.niams.nih.gov/">NIAMS</a> grant 1R44AR074375 (PI. McCormick) for providing access to the data.</em></p>
<h1>Changelog</h1>
<h2>Features</h2>
<p>SPHARM-PDM Generator</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Incorporate population-wise correspondence improvements</p>
<p><a href="https://github.com/slicersalt/RegistrationBasedCorrespondence">Registration based correspondence module</a></p>
<p>Sample data</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add population-wise correspondence improvements module sample data</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add Covariance Significance Testing module sample data</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add skeletal representation module sample data</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add ShapeVariationAnalyzer module sample data</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Correct SPHARM-PDM sample data to match tutorial</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Script that now downloads and incorporates ShapeVariationAnalyzer sample data into the SlicerSALT scene</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Automatically populate the parameters of a module to match sample data when sample data is available</p>
<h2>Fixes</h2>
<p>Updates to the SALT module layouts to build with Qt5.15</p>
<p>Updates to the Covariance Significance Testing layout</p>
<p>Crash fixes and stability</p>
<p>Fixes to windows Fortran packaging</p>
<p>Updates to windows builds for Shape Population Viewer</p>
<p>Add observer that will clear the module when the scene is closed</p>
<h1><strong>Acknowledgements</strong></h1>
<ul>
<li>UNC
<ul>
<li>Martin Styner &amp; lab</li>
<li>Steve Pizer &amp; lab</li>
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
<li>David Allemang</li>
<li>Jean-Christophe Fillion-Robin</li>
<li>Sam Horvath</li>
</ul>
</li>
</ul>

---
