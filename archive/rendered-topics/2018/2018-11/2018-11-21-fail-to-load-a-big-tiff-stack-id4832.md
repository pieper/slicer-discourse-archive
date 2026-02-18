# Fail to load a big tiff stack 

**Topic ID**: 4832
**Date**: 2018-11-21
**URL**: https://discourse.slicer.org/t/fail-to-load-a-big-tiff-stack/4832

---

## Post #1 by @cduque (2018-11-21 14:06 UTC)

<p>Hi There!</p>
<p>I wanted to load a stack of images stored in a single tiff file of microscopic data, but only the first image is loaded.<br>
The dataset is approximatly 5Gb and its dimensions are 2159x2560x548, the bit depth is 16 bit. If I resample the stack to have dimensions of 1000x1186x250 in Fiji, it manages to load it.</p>
<p>I am working in a workstations with Intel Core i7 <span class="mention">@3.6Ghz</span>, 128 GB RAM, Nvidia GTX 750 Ti, and Windows 10.</p>
<p>Do you have any idea how can I solve it?</p>
<p>Thanks a lot in advance and congrats for such great piece of software!</p>
<p>Best,</p>
<p>Carlos</p>

---

## Post #2 by @lassoan (2018-11-21 15:26 UTC)

<p>Consumer image file format (tiff, jpeg, png) support in VTK/ITK/Slicer is not as good as of research file formats.</p>
<p>Could you try saving in MetaImage (mha/mhd) or NRRD (nrrd/nhdr) format from Fiji and loading that into Slicer?</p>

---

## Post #3 by @muratmaga (2018-11-23 06:04 UTC)

<p>I am not sure if Slicer supports Z-stacks saved as a single TIFF file. You have sufficient RAM to load your data unreduced. As <a class="mention" href="/u/lassoan">@lassoan</a> suggested, try saving it as NRRD out of FIJI.</p>

---

## Post #4 by @cduque (2018-11-23 10:28 UTC)

<p>Dear Andras and muratmaga, thank you very much for your reply.</p>
<p>Fiji can indeed save as  MetaImage or NRRD, so I will try that. Thanks for the advice!</p>
<p>On the other hand, Slicer seems to support Z-stacks save as a single TIFF file, since it has no problem in loading my dataset when resampled to reduce the number of sections. Maybe it is a problem of the amount of sections - who knows.</p>
<p>One more comment to Andras, many microscopes output their images in OME-TIFF, which I think should not be considerer a “consumer image file format”. I am not aware of how big is the amount of microscopist users of Slicer, but maybe it could be super useful if Slicer has support to Bio-formats (<a href="https://www.openmicroscopy.org/bio-formats/" rel="nofollow noopener">https://www.openmicroscopy.org/bio-formats/</a>).</p>
<p>Thanks and have a nice weekend!</p>

---

## Post #5 by @lassoan (2018-11-23 12:46 UTC)

<p>Thanks for the additional information. With standardization efforts such as OME, file formats such as TIFF may become a standard file format for microscopy. To achieve that, vendors would need to coordinate between each other and retire the ridiculous number of other file format variants.</p>
<p>Current microscopy situation looks like radiology image file formats before DICOM standard was mandated. Do you know how widely DICOM format is used by microscopy community?</p>
<p>Bio-formats could be added as an extension to Slicer, but it would be better if there was one or few widely use file formats that the microscopy community would use and we could then add support for those in Slicer (probably through ITK).</p>

---

## Post #6 by @pieper (2018-11-23 12:59 UTC)

<p>We did look at adding OME to Slicer in the past, but the GPL license is a problem.</p>

---

## Post #7 by @cduque (2018-11-23 14:45 UTC)

<p>It is indeed a very complex situation, in my opinion. There is the attempt of OME to bring all the formats together, but then every microscope company has its own format: Leica has .lif, Zeiss has .czi, Abberior has .msr, etc. On the other side, there are also some preference of formats among the analyst community, like .hdf5.</p>
<p>To my knowledge, I know no microscopy system that uses DICOM.</p>

---

## Post #8 by @pieper (2018-11-23 15:06 UTC)

<p>Microscopy is a big field with a lot of different use cases.</p>
<p>Most related to Slicer’s core uses is pathology imaging.  Even here the vendors have many competing proprietary systems, but there is a workable DICOM standard for pathology slide imaging and <a href="http://www.jpathinformatics.org/article.asp?issn=2153-3539;year=2018;volume=9;issue=1;spage=37;epage=37;aulast=Herrmann;type=0">it has a lot of advantages</a>.</p>

---

## Post #9 by @muratmaga (2018-11-25 23:06 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> can you comment on the license problem? So all Slicer extensions has to be BSD license or only the core as distributed by Kitware?</p>
<p>Pathology is the immediate link to the microscopy and Slicer, but there are many 3D fluorescent imaging users in developmental biology world that can benefit from the core visualization and segmentation functionalities of the Slicer.</p>

---

## Post #10 by @cduque (2018-11-25 23:26 UTC)

<p>And not only in developmental biology. I work in auditory neuroscience and it is great not only for visualization but also for segmentation and for creating volumes and surfaces out of histological stacks. I really think the amount of users from other disciplines will increase sooner than later (at least I am recommending it to anyone who needs to reconstruct anything in 3D)</p>

---

## Post #11 by @lassoan (2018-11-26 00:30 UTC)

<p>Software with restrictive and viral licenses is not allowed in Slicer core or in any of the libraries that Slicer core uses.</p>
<p>You can use GPL code in extensions, as long as you clearly communicate that in the extension description and documentation. However, many people will not even touch software with such license, so this solution can only be considered a partial, temporary solution.</p>
<p>I understand that this temporary solution would be a relief for many users, so if you can spend time on making it available then it is great. I think the microscopy community should also come up with a few recommended open standard formats and push the vendors (and open-source toolkit and application developers) to support those.</p>

---

## Post #12 by @muratmaga (2018-11-26 02:46 UTC)

<p>Thanks Andras. Good to know about license issues. I can understand why a company like Kitware may want nothing do with GPL, but why would a user not use an extension if it is based on GPL?</p>
<p>I don’t do microscopy myself, but my impression of the field has been such that they are not big into data exchange (since the assumption is you should be able to replicate the experiment, the critical piece of information is the protocol, not the image). But with more quantitative studies and move towards that reproducibility that may change.</p>
<p>I am not sure if we can take on the OME as a project, but we will sure discuss it…</p>

---

## Post #13 by @lassoan (2018-11-26 05:00 UTC)

<p>For high-level components that can be easily replace by alternatives of they are not critical (e.g, just make things more convenient), using restrictive license is acceptable.</p>
<p>However, if you invest significant amount of time into developing new software tools or processing workflows then you don’t want to depend on any third-party component that would restrict how you can use and distribute the result of your own work. Even if you don’t mind sharing all your source code and refrain from all commercial activities, your potential users and collaborators may reject your work because of this.</p>

---

## Post #14 by @ihnorton (2018-11-26 14:56 UTC)

<p>I haven’t used it myself, but ITK does have optional support for Bio-Formats already, via <a href="https://itk.org/Doxygen/html/classitk_1_1SCIFIOImageIO.html" rel="nofollow noopener">SCIFIO</a>.</p>
<p>Alternatively, there is an LGPL-licensed, clean-reimplementation reader library called <a href="https://openslide.org/" rel="nofollow noopener">OpenSlide</a>, which may be supported (to some extent) via a new <a href="https://github.com/InsightSoftwareConsortium/ITKIOOpenSlide" rel="nofollow noopener">ITK remote module</a>. OpenSlide supports many common formats, but unfortunately, as far as I understand, their funding lapsed/developers left/etc., and none of the commercial users or other community has really picked up the slack – so it is only minimally maintained right now. In particular, they do not have support for modern Zeiss format (CZI) which is a significant limitation. (Bio-Formats does, via a Zeiss-contributed, GPL-licensed reader implementation).</p>

---
