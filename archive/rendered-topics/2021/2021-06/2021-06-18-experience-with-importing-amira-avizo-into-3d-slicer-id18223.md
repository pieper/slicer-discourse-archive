---
topic_id: 18223
title: "Experience With Importing Amira Avizo Into 3D Slicer"
date: 2021-06-18
url: https://discourse.slicer.org/t/18223
---

# Experience with importing amira/avizo into 3D Slicer

**Topic ID**: 18223
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/experience-with-importing-amira-avizo-into-3d-slicer/18223

---

## Post #1 by @muratmaga (2021-06-18 22:49 UTC)

<p>I am curious if anyone on the forum has experience with importing Amira/Avizo files (particularly the segmentation) into Slicer one way or another.</p>
<p>Amira/Avizo has been used quite a lot in the biological sciences for 3D morphology and there a quite a few labs who want to wean themselves off and switch using Slicer/SlicerMorph, but are reluctant to do so, since they got quite a few datasets.</p>
<p>I have no experience with these two software, and in fact don’t exactly know what the distinctions between these two. Any input will be much appreciated.</p>

---

## Post #2 by @pieper (2021-06-19 14:14 UTC)

<p>I don’t have any direct experience either, but if people could post example datasets they want to work with, ideally with info about how they were generated (like a tutorial) we could investigate.</p>

---

## Post #3 by @MarkusHeller (2021-06-24 10:57 UTC)

<p>I have used both AMIRA/AVIZO since it’s beginnings and 3Dslicer more recently, and there certainly are ways to exchange data.</p>
<p>I am aware of and have used Fiji incl. the bio-format plugin (<a href="https://docs.openmicroscopy.org/bio-formats/6.6.1/supported-formats.html" class="inline-onebox" rel="noopener nofollow ugc">Supported Formats — Bio-Formats 6.6.1 documentation</a>) for the import of Amira data and the 3D IO plugin for export of MHD data (<a href="http://ij-plugins.sourceforge.net/plugins/3d-io/" class="inline-onebox" rel="noopener nofollow ugc">ij-plugins - IJ Plugins: 3D I/O</a>).</p>
<p>I have also looked into using direct export options of Avizo (a while back though) and seem to remember that e.g. the origin of a 3D image data set was ignored upon export.<br>
I am not 100% sure in how far interpretation of data (origin at the centre/edge of a pixel) is consistent across different software.</p>
<p>I very much agree that having a good understanding of how to best  exchange data between systems would be most helpful and I’d be happy to explore if our experience is of any use for what you have in mind here.</p>
<p>Best wishes,<br>
Markus</p>

---

## Post #4 by @muratmaga (2021-06-24 15:08 UTC)

<aside class="quote no-group" data-username="MarkusHeller" data-post="3" data-topic="18223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/markusheller/48/11046_2.png" class="avatar"> MarkusHeller:</div>
<blockquote>
<p>I am aware of and have used Fiji incl. the bio-format plugin (<a href="https://docs.openmicroscopy.org/bio-formats/6.6.1/supported-formats.html">Supported Formats — Bio-Formats 6.6.1 documentation</a>) for the import of Amira data and the 3D IO plugin for export of MHD data (<a href="http://ij-plugins.sourceforge.net/plugins/3d-io/">ij-plugins - IJ Plugins: 3D I/O</a>).</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/markusheller">@MarkusHeller</a>. I was thinking that BioFormats may support it, but not having an actual Avizo file, I wasn’t able to try.</p>
<aside class="quote no-group" data-username="MarkusHeller" data-post="3" data-topic="18223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/markusheller/48/11046_2.png" class="avatar"> MarkusHeller:</div>
<blockquote>
<p>I have also looked into using direct export options of Avizo (a while back though) and seem to remember that e.g. the origin of a 3D image data set was ignored upon export.</p>
</blockquote>
</aside>
<p>So as I understand Avizo-&gt;BioFormats-&gt;Slicer route preserves fidelity of the data (in terms of origins, offsets, directional matrix etc) better than exporting directly out of Avizo?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> I know there is a fundamental license incompatibility bioformats and Slicer. But this keeps coming up, and I am wondering what are our options to support BioFormats in Slicer (e.g., as an optional download like ffmpeg?). This doesn’t have to be in core Slicer, can be in SlicerMorph etc…</p>

---

## Post #5 by @pieper (2021-06-24 17:19 UTC)

<p>If people install the GPL parts themselves it shouldn’t be a problem.  We can’t distribute GPL code but we can make it easier for people to use it.</p>
<p>Would an interface to this package do the trick? <a href="https://pythonhosted.org/python-bioformats/" class="inline-onebox">python-bioformats: read and write life sciences image file formats — python-bioformats 0.0.0 documentation</a></p>

---

## Post #6 by @muratmaga (2021-06-24 17:51 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="18223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Would an interface to this package do the trick? <a href="https://pythonhosted.org/python-bioformats/">python-bioformats: read and write life sciences image file formats — python-bioformats 0.0.0 documentation </a></p>
</blockquote>
</aside>
<p>I was excited to see this thinking this might be native python, but looks like it still relies on having JRE installed on the computer. I have the feeling that default availability of JRE on a given personal computer is much less common nowadays (I sure didn’t have it until this morning until I tried the command line BFtools for the laptop I have been using for last three years).</p>
<p>Nevertheless, I think this might be a good start. Although I don’t know whether it might be any less work by simply asking people to install the command line tools + JRE (<a href="https://www.openmicroscopy.org/bio-formats/downloads/">https://www.openmicroscopy.org/bio-formats/downloads/</a>) and calling those under the hood.</p>

---

## Post #7 by @pieper (2021-06-24 18:20 UTC)

<p>Yes, I’d try not to rely on java or GPL’d code, but if that’s the easiest way for people to access their data they may be stuck with it.  There may be specific file formats we can read without resorting to these packages.</p>

---

## Post #8 by @lassoan (2021-06-24 19:03 UTC)

<p>ITK has added support for many file formats that we might not have exposed yet in Slicer. There is a good chance that we can find a format that Amira/avizo can directly write and ITK/VTK/etc. can read.</p>
<p>Note that we only need a “temporary” solution (for a few years), as there is a strong push in the entire biomedical imaging community towards a new modern open file format, such as OME-Zarr. OME, ITK, Slicer, napari, etc. are all on board.</p>

---

## Post #9 by @boud (2024-08-29 07:43 UTC)

<p>Dear all: Collaborators have been sharing Amira files with me. Before I ask them to convert the data themselves or spend time doing something that won’t work, I would like to have confirmation that 3D Slicer can indeed open Amira/Avizo files at this time. – Thank you!</p>

---

## Post #10 by @muratmaga (2024-08-29 16:59 UTC)

<p>Not sure there has been any change since the last post. I think using bioformats in ImageJ and exporting them as nrrd for Slicer is probably your safest option.</p>

---
