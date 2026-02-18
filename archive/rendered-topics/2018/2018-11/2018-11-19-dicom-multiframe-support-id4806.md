# DICOM multiframe support

**Topic ID**: 4806
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/dicom-multiframe-support/4806

---

## Post #1 by @pieper (2018-11-19 15:58 UTC)

<p>This thread contains a link to a dicom multiframe object David Clunie created.  <a class="mention" href="/u/fedorov">@fedorov</a> reports that it doesn’t load correctly in Slicer.</p>
<p><a href="https://groups.google.com/forum/?utm_medium=email&amp;utm_source=footer#!msg/dicom4qi/BD9i2lUklvU/TN_gRgSFBgAJ" class="onebox" target="_blank">https://groups.google.com/forum/?utm_medium=email&amp;utm_source=footer#!msg/dicom4qi/BD9i2lUklvU/TN_gRgSFBgAJ</a></p>
<p>My thinking is that we should write a DICOMMultframePlugin that detects the multiframe SOPClassUIDs and loads them directly, probably using pydicom and custom logic that detects volume geometry (or MultiVolume / Sequence geometry).  Ideally the core logic of this sorting should be independent of Slicer it can be re-used in other pydicom applications.  The Plugin would be a thin wrapper on this logic.</p>

---

## Post #2 by @fedorov (2018-11-19 16:08 UTC)

<p>Would it be a complete heresy to bundle <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> and use that for conversion?</p>
<p>Alternatively, we should look if we can perhaps reuse plastimatch, already bundled in SlicerRT, at least as an alternative parsing strategy. I did try it for this specific multiframe dataset, and I could not figure out quickly how to make it work, but maybe we should just check with <a class="mention" href="/u/gcsharp">@gcsharp</a>.</p>
<p>I am just not convinced it is a good investment of effort to reimplement this functionality (and to assemble a good test dataset).</p>

---

## Post #3 by @pieper (2018-11-19 16:31 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Would it be a complete heresy to bundle <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> and use that for conversion?</p>
</blockquote>
</aside>
<p>That would be great actually - it looks like the license if compatible.  We could start by adding this as an extension and then if it works well make it part of the Slicer distribution.  From what I can tell the <a href="https://github.com/rordenlab/dcm2niix/blob/master/license.txt">dcm2niix license</a> is compatible.</p>
<p>As an aside, I also like the look of the <a href="https://www.mccauslandcenter.sc.edu/mricrogl/">MIRcroGL renderer</a> - could make an interesting extension tool.</p>

---

## Post #4 by @lassoan (2018-11-19 17:00 UTC)

<p>Is it a simple 3D volume? Shouldn’t we report the error to ITK developers and ask them to fix multiframe support? It should not be difficult.</p>

---

## Post #5 by @fedorov (2018-11-19 18:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Shouldn’t we report the error to ITK developers and ask them to fix multiframe support? It should not be difficult.</p>
</blockquote>
</aside>
<p>I think I already reported some of those on Jira, this issue came up before, but now that ITK Jira is gone, no way to confirm…</p>
<p>Based on a discussion here: <a href="https://discourse.slicer.org/t/slicer-dicom-scalar-volume-plugin-relies-on-old-gdcm-why-do-we-not-use-dcmtk/354/24" class="inline-onebox">Slicer DICOM Scalar volume plugin relies on (old) GDCM: why do we not use DCMTK? - #24 by pieper</a>, looks like the “home” for ITK DICOM development is <a href="https://github.com/KitwareMedical/ITKDICOM" class="inline-onebox">GitHub - KitwareMedical/ITKDICOM: Better support for DICOM in ITK.</a>, but I do not see a lot of activity there, and there are issues open since 2017. Not clear if ITK community prioritized DICOM support over many competing interests. I am sure something like “deep learning in ITK” would be much higher on the list! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @pieper (2018-11-19 18:55 UTC)

<p>I would be happy with any of these solutions (pydicom, dcm2niix, ITK or others) - whatever works well and is maintained and has a compatible license.</p>
<p>Ideally the DICOMPlugin layer of Slicer shouldn’t contain any of the actual logic, just adaptors to turn a well defined set of DICOM data into the corresponding Slicer (MRML) objects.</p>

---

## Post #8 by @pieper (2018-11-19 19:37 UTC)

<p><a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> - agreed, it’s a messy business!  In Slicer we allow multiple plugins to evaluate the data and offer different reader options for the user to select from (each with a “confidence” so the user can just choose the highest confidence by default).  But it’s an imperfect mapping so we are always looking for ways to improve things.</p>

---

## Post #9 by @thewtex (2018-11-19 20:32 UTC)

<aside class="quote no-group quote-modified" data-username="fedorov" data-post="5" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<blockquote>
<p>Shouldn’t we report the error to ITK developers and ask them to fix multiframe support? It should not be difficult.</p>
</blockquote>
<p>I think I already reported some of those on Jira, this issue came up before, but now that ITK Jira is gone, no way to confirm…</p>
</blockquote>
</aside>
<p>ITK’s Jira Issue Tracker is dead. Long live <a href="https://github.com/InsightSoftwareConsortium/ITK/issues" rel="noopener nofollow ugc">ITK’s GitHub Issue Tracker</a>! <img src="https://emoji.discourse-cdn.com/twitter/crown.png?v=12" title=":crown:" class="emoji" alt=":crown:" loading="lazy" width="20" height="20"></p>
<p>If there are issues with ITK’s reading of multi-frame DICOM files, please report it there. To the best of my knowledge, reading multi-frame DICOM volumes works well.</p>
<p>The old <a href="https://insightsoftwareconsortium.atlassian.net/projects/ITK/issues/ITK-3546?filter=allopenissues" rel="noopener nofollow ugc">Jira issue tracker</a> is still available – if there is a relevant issue that you find important, please migrate them to the GitHub issue tracker.</p>
<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Not clear if ITK community prioritized DICOM support over many competing interests. I am sure something like “deep learning in ITK” would be much higher on the list! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>Deep learning is wonderful, and ITK helps apply deep learning methods to medical imaging data. To perform deep learning on medical imaging data, we definitely need good DICOM support!</p>

---

## Post #11 by @fedorov (2018-11-19 22:47 UTC)

<p><a class="mention" href="/u/thewtex">@thewtex</a> thanks for the response!</p>
<p>I thought it is probably not very helpful if I submit an issue demonstrating the problem in Slicer, since there are potentially other sources of error, so I wanted to reproduce the problem with ITK.</p>
<p>I googled for “itk read dicom series”, and came across the python example here: <a href="https://itk.org/ITKExamples/src/IO/GDCM/ReadDICOMSeriesAndWrite3DImage/Documentation.html">https://itk.org/ITKExamples/src/IO/GDCM/ReadDICOMSeriesAndWrite3DImage/Documentation.html</a>.</p>
<p>However, when I run this example (after adding <code>import sys</code>) on the dataset referenced from the thread mentioned in the initial post (the dataset itself is available here: <a href="https://www.dropbox.com/s/re37n46wvktez5c/mf.dcm.bz2">https://www.dropbox.com/s/re37n46wvktez5c/mf.dcm.bz2</a>), I get the error below:</p>
<pre><code class="lang-nohighlight">WARNING: In /Users/kitware/Dashboards/ITK/ITKPythonPackage/standalone-build/ITK-source/Modules/IO/GDCM/src/itkGDCMSeriesFileNames.cxx, line 109
GDCMSeriesFileNames (0x7fe8869d7bb0): No Series were found

No DICOMs in: .
</code></pre>
<p>Looks like this DICOM file is not even recognized as DICOM by ITK <code>GDCMSeriesFileNames</code>.</p>
<p>Checking it with <a href="https://support.dcmtk.org/docs/dcmdump.html"><code>dcmdump</code></a>, it is clearly a valid DICOM file (and it comes from David Clunie).</p>
<pre><code class="lang-nohighlight">$ dcmdump mf.dcm|more                                                                                                2.3.6

# Dicom-File-Format

# Dicom-Meta-Information-Header
# Used TransferSyntax: Little Endian Explicit
(0002,0000) UL 214                                      #   4, 1 FileMetaInformationGroupLength
(0002,0001) OB 00\01                                    #   2, 1 FileMetaInformationVersion
(0002,0002) UI =LegacyConvertedEnhancedMRImageStorage   #  28, 1 MediaStorageSOPClassUID
(0002,0003) UI [1.3.6.1.4.1.5962.99.1.7321.1421.1542625430036.1.1.1.2.1] #  56, 1 MediaStorageSOPInstanceUID
(0002,0010) UI =LittleEndianExplicit                    #  20, 1 TransferSyntaxUID
(0002,0012) UI [1.3.6.1.4.1.5962.99.2]                  #  22, 1 ImplementationClassUID
(0002,0013) SH [PIXELMEDJAVA001]                        #  16, 1 ImplementationVersionName
(0002,0016) AE [OURAETITLE]                             #  10, 1 SourceApplicationEntityTitle

# Dicom-Data-Set
# Used TransferSyntax: Little Endian Explicit
(0008,0008) CS [ORIGINAL\PRIMARY\M\NONE]                #  24, 4 ImageType
(0008,0012) DA [20181119]                               #   8, 1 InstanceCreationDate
(0008,0013) TM [060350.036]                             #  10, 1 InstanceCreationTime
(0008,0016) UI =LegacyConvertedEnhancedMRImageStorage   #  28, 1 SOPClassUID
(0008,0018) UI [1.3.6.1.4.1.5962.99.1.7321.1421.1542625430036.1.1.1.2.1] #  56, 1 SOPInstanceUID
(0008,0020) DA [19991231]                               #   8, 1 StudyDate
(0008,0021) DA [19991231]                               #   8, 1 SeriesDate
(0008,0023) DA [19991231]                               #   8, 1 ContentDate
</code></pre>
<p>Is <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.71.html">LegacyConvertedEnhancedMRImageStorage</a> IOD expected to be supported by ITK?</p>
<p>Is there another example you can point me to that is recommended that I can use to reproduce the problem and report the issue?</p>

---

## Post #12 by @fedorov (2018-11-19 22:50 UTC)

<p>Forgot to mention, I have itk-4.13.1.post1 installed with pip on mac 10.14.1.</p>

---

## Post #14 by @fedorov (2018-11-19 23:08 UTC)

<p><a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> sounds good, thanks. But to me this means that <em>de facto</em> reading multiframe DICOM, at least of this specific type, is not supported in ITK as of today. <a class="mention" href="/u/thewtex">@thewtex</a> please let me know if I am missing something, or if I should try something different.</p>
<p>cc: <a class="mention" href="/u/dzenanz">@dzenanz</a> - I see you authored the python sample code that I’ve been using for testing.</p>

---

## Post #16 by @thewtex (2018-11-20 02:02 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I thought it is probably not very helpful if I submit an issue demonstrating the problem in Slicer, since there are potentially other sources of error, so I wanted to reproduce the problem with ITK.</p>
</blockquote>
</aside>
<p>Thank you <a class="mention" href="/u/fedorov">@fedorov</a> !</p>
<aside class="quote no-group quote-modified" data-username="fedorov" data-post="11" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I googled for “itk read dicom series”, and came across the python example here: <a href="https://itk.org/ITKExamples/src/IO/GDCM/ReadDICOMSeriesAndWrite3DImage/Documentation.html" class="inline-onebox" rel="noopener nofollow ugc">Read DICOM Series and Write 3D Image — v5.4.0</a>.</p>
</blockquote>
</aside>
<p>This is for reading the more cumbersome series distributed over multiple files.</p>
<p>For a multi-frame DICOM, we can just use:</p>
<pre><code class="lang-auto">import itk
image = itk.imread('mf.dcm')
</code></pre>
<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>However, when I run this example (after adding <code>import sys</code> ) on the dataset referenced from the thread mentioned in the initial post (the dataset itself is available here: <a href="https://www.dropbox.com/s/re37n46wvktez5c/mf.dcm.bz2" rel="noopener nofollow ugc">https://www.dropbox.com/s/re37n46wvktez5c/mf.dcm.bz2 </a>),</p>
</blockquote>
</aside>
<p>I tried the above with the given image, and it reads in a head volume content fine. However, the origin and spacing are not populated.</p>
<aside class="quote no-group quote-post-not-found" data-username="Mihail_Isakov" data-post="13" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9adbd/48.png" class="avatar"> Mihail_Isakov:</div>
<blockquote>
<p>Legacy Converted Enhanced was partially supported, this commit added more support (spacing, origin, etc.), probably not yet in ITK.</p>
<p><a href="https://github.com/malaterre/GDCM/commit/38fff78cbe6f2065e22dfea32b406e016665c5f5" rel="noopener nofollow ugc">github.com/malaterre/GDCM </a></p>
<p><a href="https://github.com/malaterre" rel="noopener nofollow ugc"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/e/ed41d5165e8a83a031690a53f6db16b8cdf57e4b.png" alt="malaterre" width="90" height="90"> </a></p>
<h4><a href="https://github.com/malaterre/GDCM/commit/38fff78cbe6f2065e22dfea32b406e016665c5f5" rel="noopener nofollow ugc">Merge pull request #55 from issakomi/legacy_enh2</a></h4>
<p>Spacing and other. attr. for Legacy, Breast Tomo</p>
<p>by <a href="https://github.com/malaterre" rel="noopener nofollow ugc">malaterre</a> on <a href="https://github.com/malaterre/GDCM/commit/38fff78cbe6f2065e22dfea32b406e016665c5f5" rel="noopener nofollow ugc">06:50AM - 20 Aug 18 UTC</a></p>
<p>changed <strong>3 files</strong> with <strong>70 additions</strong> and <strong>14 deletions</strong> .</p>
</blockquote>
</aside>
<p>Very nice <a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> ! I will try updating ITK’s GDCM, and I will report back on the resulting origin / spacing…</p>

---

## Post #17 by @fedorov (2018-11-20 02:16 UTC)

<aside class="quote no-group quote-modified" data-username="thewtex" data-post="16" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thewtex/48/32_2.png" class="avatar"> thewtex:</div>
<blockquote>
<blockquote>
<p>I tried the above with the given image, and it reads in a head volume content fine. However, the origin and spacing are not populated.</p>
</blockquote>
</blockquote>
</aside>
<p>Thanks – this is consistent with what we observe in Slicer, so the problem is reproduced. Should I create an issue so we could follow on the updates?</p>

---

## Post #19 by @thewtex (2018-11-20 02:36 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="17" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Thanks – this is consistent with what we observe in Slicer, so the problem is reproduced. Should I create an issue so we could follow on the updates?</p>
</blockquote>
</aside>
<p>Good – yes, an issue would be helpful to collect information and track progress.</p>

---

## Post #20 by @thewtex (2018-11-20 03:28 UTC)

<aside class="quote no-group quote-post-not-found" data-username="Mihail_Isakov" data-post="18" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9adbd/48.png" class="avatar"> Mihail_Isakov:</div>
<blockquote>
<p>There are more issues, but enough written today <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Sorry for many posts.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> thanks for your contributions. These variations can be challenging, but working together on them collectively disarms the challenge.</p>
<p>Your fix in GDCM indeed fixed the issue with the provided dataset:</p>
<pre><code class="lang-auto"> RequestedRegion:
   Dimension: 3
   Index: [0, 0, 0]
   Size: [256, 256, 128]
 Spacing: [1, 1, 1.33]
 Origin: [-83.2177, -123.869, 159.934]
 Direction:
4.37571e-31 -1e-16 1
0.976296 -0.21644 -2.1644e-17
-0.21644 -0.976296 -9.76296e-17
</code></pre>
<p>Pull request is here: <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/208" class="inline-onebox" rel="noopener nofollow ugc">Update GDCM to 2018-11-05 release branch by thewtex · Pull Request #208 · InsightSoftwareConsortium/ITK · GitHub</a></p>

---

## Post #21 by @fedorov (2018-11-20 15:56 UTC)

<aside class="quote no-group quote-post-not-found" data-username="Mihail_Isakov" data-post="18" data-topic="4806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9adbd/48.png" class="avatar"> Mihail_Isakov:</div>
<blockquote>
<p>they <em>always</em> have In-Stack Position Number in reversed order, e.g.<br>
Stack ID / In-Stack Position Number<br>
1 / 121<br>
1 / 120<br>
1 / 119<br>
1 / 118<br>
etc.<br>
Not sure it is a bug, sometimes it is correct, sometimes definitely not. Where take the origin? 1st frame, last frame? GDCM takes always first. Per standard in Legacy Converted dimension organisation is optional, so if there is no dimension organisation - i ignore In-Stack Position Number, load frames one by one (as GDCM returns) and do own validation. If it fails, mark image as non-uniform and disable orientation letters.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> what makes you believe you can rely on in-stack position number for volumetric reconstruction of the geometry?  I think those positions can only be useful for visualizing the frames to the user, and one should always sort individual frames geometrically to reconstruct the volume and calculate the origin.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a> <a class="mention" href="/u/malaterre">@malaterre</a> does ITK/GDCM sort frames of enhanced objects using shared/per frame geometry information as part of volume reconstruction?</p>

---

## Post #24 by @pieper (2018-11-21 13:47 UTC)

<p><a href="https://github.com/InsightSoftwareConsortium/ITK/pull/208#issuecomment-440659486">This post on the ITK issue tracker</a> contends that the multiframe file is left/right flipped - is that true?</p>

---

## Post #26 by @Mihail_Isakov (2018-11-21 14:29 UTC)

<p>Here is same image exported as classic series, no problem, if individual slices sorted by IPP/IOP. It is then ASL (in ITK terminology)</p>
<p><a href="https://drive.google.com/file/d/1mGZYywLseaipcG-SnJJOjll32xxR7T2Q/view?usp=sharing" rel="nofollow noopener">Classic series</a></p>

---

## Post #27 by @fedorov (2018-11-21 14:53 UTC)

<p>For the sake of completeness, here’s the link to the original MR series that David Clunie converted into the multiframe instance referenced in the original post: <a href="https://www.dropbox.com/s/8m7ugu4cmw83fvd/dicoms-anon.zip?dl=0">https://www.dropbox.com/s/8m7ugu4cmw83fvd/dicoms-anon.zip?dl=0</a></p>

---

## Post #28 by @Mihail_Isakov (2018-11-21 15:03 UTC)

<p>Yes, it confirms. Try to open multi-frame and classic series in volume rendering or compare Z-directions thru calculations. Flipped. Didn’t you say frames should be sorted?</p>

---

## Post #29 by @fedorov (2018-11-21 15:20 UTC)

<p><a class="mention" href="/u/mihail_isakov">@Mihail_Isakov</a> I do not have any experience with or access to the tool you are using, or to its source code, and I didn’t investigate the content of those files. All I know is that if I use established open source tools that I trust, I do not see inconsistency in how images show up in Slicer. I would be very surprised if dcm2niix didn’t sort frames, and that’s what I used to load the multiframe image into Slicer.</p>
<p>I won’t have time to debug this any time soon. But I also won’t take a screenshot from an unknown tool as a proof that data encoding by David Clunie is incorrect</p>

---

## Post #31 by @fedorov (2018-11-21 16:02 UTC)

<p>As explained in the link mentioned in the first post of this topic, Slicer is not able to properly load this multiframe directly. I used dcm2niix to make a NIfTI first, which I then loaded into Slicer. The whole reason this topic started is because Slicer cannot (at least, not always) directly and correctly load multiframe DICOM images.</p>

---

## Post #33 by @Chris_Rorden (2019-01-03 22:49 UTC)

<p>The latest development version of <a href="https://github.com/rordenlab/dcm2niix/issues/252" rel="nofollow noopener">dcm2niix allows programs like Slicer to request files for conversion</a>. In addition, dcm2niix could also be extended to create NRRD files instead of NIfTI files. In my experience, DWIconvert is typically very robust. However, for situations like multi-frame it might be nice to have an alternative mechanism.</p>
<p>The simplest NRRD implementation would be to convert files very similar to NIfTI: with space being stored in the first three dimensions and the fourth used for time (fMRI) or diffusion direction (DWI). The gradient direction in NRRD seems a bit simpler than the FSL bvecs, so it seems that would be more direct.</p>
<p>This would take a bit of development effort, so if the Slicer community is happy with just using dcm2niix for NIfTI, I can understand.</p>

---

## Post #34 by @fedorov (2019-01-03 23:09 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> thank you for the followup, and for adding the feature!</p>
<p>I think <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> are the right people to contribute their input on this topic.</p>

---
