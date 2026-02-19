---
topic_id: 3217
title: "Citing Slicer Modules Extensions"
date: 2018-06-18
url: https://discourse.slicer.org/t/3217
---

# Citing Slicer modules/extensions

**Topic ID**: 3217
**Date**: 2018-06-18
**URL**: https://discourse.slicer.org/t/citing-slicer-modules-extensions/3217

---

## Post #1 by @muratmaga (2018-06-18 17:14 UTC)

<p>When I use Slicer in a publication, I have been citing this paper.</p>
<p>Kikinis R, Pieper SD, Vosburgh KG. 2014. 3D Slicer: A Platform for Subject-Specific Image Analysis, Visualization, and Clinical Support. In: Intraoperative Imaging and Image-Guided Therapy. Springer, New York, NY. p 277–289. Available from: <a href="https://link.springer.com/chapter/10.1007/978-1-4614-7657-3_19" class="inline-onebox">3D Slicer: A Platform for Subject-Specific Image Analysis, Visualization, and Clinical Support | SpringerLink</a></p>
<p>However, there are many extensions and other functionalities that are not part of the core, where citing only this paper is not appropriate to acknowledge their contributions. I also noticed that acknowledgement sections of modules usually does not necessarily provide a citation, beyond a URL to documentation, which is under help.</p>
<p>What I had in mind is something similar to R citation function. e.g. for a non-peer reviewed contribution:</p>
<blockquote>
<p>citation(‘Hotelling’)</p>
</blockquote>
<p>To cite package ‘Hotelling’ in publications use:</p>
<p>James M. Curran (2013). Hotelling: Hotelling’s T-squared test and variants. R package version<br>
1.0-2. <a href="https://CRAN.R-project.org/package=Hotelling" class="inline-onebox">CRAN - Package Hotelling</a></p>
<p>A BibTeX entry for LaTeX users is</p>
<p><span class="mention">@Manual</span>{,<br>
title = {Hotelling: Hotelling’s T-squared test and variants},<br>
author = {James M. Curran},<br>
year = {2013},<br>
note = {R package version 1.0-2},<br>
url = {<a href="https://CRAN.R-project.org/package=Hotelling" class="inline-onebox">CRAN - Package Hotelling</a>},<br>
}</p>
<p>or  a peer-reviewed paper example</p>
<blockquote>
<p>citation(‘geomorph’)</p>
</blockquote>
<p>To cite package ‘geomorph’ in a publication use:</p>
<p>Adams, D.C., and E. Otarola-Castillo. 2013. geomorph: an R package for the collection and analysis<br>
of geometric morphometric shape data. Methods in Ecology and Evolution. 4:393-399.</p>
<p>A BibTeX entry for LaTeX users is</p>
<p><span class="mention">@Article</span>{,<br>
title = {geomorph: an R package for the collection and analysis of geometric morphometric shape data},<br>
author = {D.C. Adams and E. Otarola-Castillo},<br>
journal = {Methods in Ecology and Evolution},<br>
year = {2013},<br>
volume = {4},<br>
pages = {393-399},<br>
}</p>
<p>As geomorph is evolving quickly, you may want to cite also its version number (found with<br>
‘library(help = geomorph)’).</p>

---

## Post #2 by @dokay1 (2022-07-28 18:36 UTC)

<p>Is there a citation I could use for the level tracing tool in 3D Slicer?</p>

---

## Post #3 by @pieper (2022-07-28 18:45 UTC)

<p>I don’t believe there was ever a publication about that tool.  Citing the Slicer reference and pointing to the files in the repo would probably be good practice if you are going for reproducibility (also note the version of Slicer).</p>
<p>Here’s one of the files that describes the implementation: <a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkITK/itkLevelTracingImageFilter.h" class="inline-onebox">Slicer/itkLevelTracingImageFilter.h at main · Slicer/Slicer · GitHub</a></p>

---
