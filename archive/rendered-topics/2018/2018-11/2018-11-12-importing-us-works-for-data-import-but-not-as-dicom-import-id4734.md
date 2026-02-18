# Importing US works for data import but not as dicom import?

**Topic ID**: 4734
**Date**: 2018-11-12
**URL**: https://discourse.slicer.org/t/importing-us-works-for-data-import-but-not-as-dicom-import/4734

---

## Post #1 by @EricWilson (2018-11-12 19:09 UTC)

<p>I would like to understand why this doesn’t work. I have an ultrasound scan stored as a dicom file. I have followed the thread of a <a href="https://discourse.slicer.org/t/reference-image-in-series-does-not-contain-geometry-information-please-use-caution/3790">very similar case involving ultrasound</a> but it gives the same error after installing the Slicer Heart extension.</p>
<p>if i instead import it as data, it has no issues and can be manipulated as expected.</p>
<p>it would be easiest to work with if i could import this as dicom data, and it looks like it should be possible. If anyone can tell me how to load this through dicom it would be much appreciated.</p>
<p>not sure that it will help, but here is the dicom import log:<br>
Imported a DICOM directory, checking for extensions</p>
<p>Warning in DICOM plugin Scalar Volume when examining loadable 1: Unnamed Series: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution.</p>
<p>Loading with imageIOName: GDCM</p>
<p>Could not read scalar volume using GDCM approach. Error is: FileFormatError</p>
<p>Loading with imageIOName: DCMTK</p>
<p>Could not read scalar volume using DCMTK approach. Error is: FileFormatError</p>
<p>Could not load: 1: Unnamed Series as a Scalar Volume</p>

---

## Post #2 by @lassoan (2018-11-12 19:33 UTC)

<p>If you load the DICOM file using “Add data” dialog then it’ll basically ignore all metadata and load the entire image stack as a 3D volume using ITK library’s DICOM reader directly.</p>
<p>If you import the file into the DICOM database and load using the DICOM volume, then there is a much more sophisticated mechanism, which inspects the file content, evaluates many different ways have the data set can be interpreted, performs consistency checks, etc.</p>
<p>Your data set does not seem to fit any of the profiles currently offered by the more sophisticated and reliable DICOM file loading mechanism. Based on “FileFormatError” message, the data set may have some low-level data encoding error (maybe due to trivial things, such as international characters, or maybe due to corruption caused by anonymization). To investigate this, we would an example data set. The data set must not contain any patient identifiable information; should preferably taken of some test object or animal case.</p>

---

## Post #3 by @EricWilson (2018-11-12 21:05 UTC)

<p>ok, I’ll give you the sample i’m working with. It was anonymized before I got it, so that should be fine. I have also attempted to run it through the dicom patcher module with the same result.</p>
<p>here is a link the original anonymized data:<br>
<a href="https://spheregen-my.sharepoint.com/:u:/p/eric_wilson/EUh5viAuSEVDrCrgFkqLp9IB6h6vtzMLFqtOIdynlr4jJw?e=H457C3" class="onebox" target="_blank" rel="nofollow noopener">https://spheregen-my.sharepoint.com/:u:/p/eric_wilson/EUh5viAuSEVDrCrgFkqLp9IB6h6vtzMLFqtOIdynlr4jJw?e=H457C3</a></p>

---

## Post #4 by @pieper (2018-11-13 18:16 UTC)

<p>Hi <a class="mention" href="/u/ericwilson">@EricWilson</a> -</p>
<p>Thanks for sharing the example data.   It’s a mutliframe ultrasound image and it looks pretty standard, but it’s not something Slicer currently supports via the DICOM module.</p>
<p>I’ve written <a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L279-L375">a custom script</a> for a similar dataset in the past, and that could be used as a start point for making a dedicated plugin.</p>
<p>The issue is that most of these datasets will be ultrasound cine and not volumes (and usually there’s no way to tell automatically).  We should probably give the user the option of loading either a scalar volume or a sequence when this type of data is loaded through the dicom module.</p>
<p>-Steve</p>

---

## Post #5 by @EricWilson (2018-11-13 20:13 UTC)

<p>thanks for the information and the code. I should be able to make a solution with this.</p>

---

## Post #6 by @pieper (2018-11-14 14:59 UTC)

<aside class="quote no-group" data-username="EricWilson" data-post="5" data-topic="4734" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ericwilson/48/1513_2.png" class="avatar"> EricWilson:</div>
<blockquote>
<p>thanks for the information and the code. I should be able to make a solution with this.</p>
</blockquote>
</aside>
<p>Super - post back if you come up with anything that could be of general use for people with this kind of data.</p>

---

## Post #7 by @sonjapejcic (2019-03-04 19:11 UTC)

<p><a class="mention" href="/u/ericwilson">@EricWilson</a>, did you ever manage to make up a solution for this? I am also hoping to load US cines.</p>

---

## Post #8 by @jamesobutler (2019-03-04 19:17 UTC)

<p><a class="mention" href="/u/sonjapejcic">@sonjapejcic</a> US cines can be loaded if they are in the format of Nrrd(Nhdr+raw) or MHA(mhd+raw) using the <a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/Sequences" rel="nofollow noopener">Sequences</a> extension which can be downloaded and installed from the Extension manager.</p>

---

## Post #9 by @EricWilson (2019-03-04 19:51 UTC)

<p>hopefully <a class="mention" href="/u/jamesobutler">@jamesobutler</a>’s  response helps. the data set wasn’t really in the format we were looking for, so development working with US was stopped until we can get access to the relevant format.</p>

---
