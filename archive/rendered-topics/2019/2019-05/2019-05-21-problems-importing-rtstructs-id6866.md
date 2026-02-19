---
topic_id: 6866
title: "Problems Importing Rtstructs"
date: 2019-05-21
url: https://discourse.slicer.org/t/6866
---

# Problems importing RTStructs

**Topic ID**: 6866
**Date**: 2019-05-21
**URL**: https://discourse.slicer.org/t/problems-importing-rtstructs/6866

---

## Post #1 by @Alex_Vergara (2019-05-21 10:00 UTC)

<p>I have a serious problem while loading rtstructs. They are displayed correctly while loading as planar contours. So far so good:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e900b8dff05a5e4e9be002492466a4ee2e06135c.png" data-download-href="/uploads/short-url/xfeNsW57x4TjcJiMsvnBJvOOjj6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e900b8dff05a5e4e9be002492466a4ee2e06135c_2_373x499.png" alt="image" data-base62-sha1="xfeNsW57x4TjcJiMsvnBJvOOjj6" width="373" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e900b8dff05a5e4e9be002492466a4ee2e06135c_2_373x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e900b8dff05a5e4e9be002492466a4ee2e06135c_2_559x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e900b8dff05a5e4e9be002492466a4ee2e06135c.png 2x" data-dominant-color="F1F1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">574×769 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1fc49ec2ce8a880a22c9887c32257ea69adcc88.png" data-download-href="/uploads/short-url/ywHAZ9r5dX5En52nEDUXK1lBVDG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fc49ec2ce8a880a22c9887c32257ea69adcc88_2_345x235.png" alt="image" data-base62-sha1="ywHAZ9r5dX5En52nEDUXK1lBVDG" width="345" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fc49ec2ce8a880a22c9887c32257ea69adcc88_2_345x235.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fc49ec2ce8a880a22c9887c32257ea69adcc88_2_517x352.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fc49ec2ce8a880a22c9887c32257ea69adcc88_2_690x470.png 2x" data-dominant-color="8288BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×676 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I want to use the binary labelmap they are completely destroyed.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b391be4051567e8b3c0c2ee268a140849e0ad429.png" alt="image" data-base62-sha1="pCxIFDD2L5jOnR8MXr1AP393KaJ" width="430" height="164"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ee6c26a071e5253711e3c18c0a3f0f8f112e6f2.png" data-download-href="/uploads/short-url/i6CyMM748letkx0COxAQvAsk4Ho.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee6c26a071e5253711e3c18c0a3f0f8f112e6f2_2_345x235.png" alt="image" data-base62-sha1="i6CyMM748letkx0COxAQvAsk4Ho" width="345" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee6c26a071e5253711e3c18c0a3f0f8f112e6f2_2_345x235.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee6c26a071e5253711e3c18c0a3f0f8f112e6f2_2_517x352.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee6c26a071e5253711e3c18c0a3f0f8f112e6f2_2_690x470.png 2x" data-dominant-color="989AD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×677 22.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The segmentation has already defined a Master volume:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10865754cedeefcde4a949e7532afc8a020556f.png" alt="image" data-base62-sha1="rxE8Jm8lO5hP8jHJMGL9P31HDSD" width="576" height="310"></p>
<p>I don’t know what I am doing wrong here! I just couldn’t use the RTstructs. Help!!</p>

---

## Post #2 by @lassoan (2019-05-21 13:34 UTC)

<p>Maybe there is something wrong with the master volume. Try to seg labelmap geometry using an “Annotation ROI” as explained <a href="https://discourse.slicer.org/t/extend-roi-after-cropping-and-segmenting/6594/3">here</a>. If you still have issues the best would be if you could share the RTSTRUCT so that we can investigate.</p>

---

## Post #3 by @Alex_Vergara (2019-05-21 13:48 UTC)

<p>How do I share the files with you?</p>

---

## Post #4 by @lassoan (2019-05-21 13:49 UTC)

<p>Upload to dropbox/onedrive/google drive and post the link.</p>

---

## Post #5 by @Alex_Vergara (2019-05-21 14:04 UTC)

<p>Here are the files, let me know if you can get them<br>
<a href="https://1drv.ms/f/s!AkKpgfpFgNdvk3bkDvNqyB7ofguq" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/f/s!AkKpgfpFgNdvk3bkDvNqyB7ofguq</a></p>
<p>One folder is the CT, and the other are the RTSTRUCT</p>

---

## Post #6 by @cpinter (2019-05-21 19:10 UTC)

<p>I loaded it to the latest version, and although it looks like the closed surface is alright, the triangulation is actually faulty:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa2422ee4002997bc73bb27ce4d30b90090a27ca.png" data-download-href="/uploads/short-url/oh8AHunNWf7Aj8tFTufwywTKq7M.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2422ee4002997bc73bb27ce4d30b90090a27ca_2_406x500.png" alt="image" data-base62-sha1="oh8AHunNWf7Aj8tFTufwywTKq7M" width="406" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2422ee4002997bc73bb27ce4d30b90090a27ca_2_406x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2422ee4002997bc73bb27ce4d30b90090a27ca_2_609x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa2422ee4002997bc73bb27ce4d30b90090a27ca.png 2x" data-dominant-color="56707A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">684×842 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Moreover it seems like a systematic issue, as if the contours are not saved the way we have seen from the planning systems we encountered (which is most of them, as SlicerRT is used since 2012 and this is the first time I’m seeing something like this - similarly to the fact that each structure is in its own structure set object, which is also unusual).</p>
<p>The contours themselves seem to be alright to me, see<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f88cddca6a912e990788c2ffec1f6c8dbb93ec2.png" data-download-href="/uploads/short-url/6MvxDVTD3yOOynMtsx2UEPAZ8f8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f88cddca6a912e990788c2ffec1f6c8dbb93ec2.png" alt="image" data-base62-sha1="6MvxDVTD3yOOynMtsx2UEPAZ8f8" width="575" height="500" data-dominant-color="001111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">634×551 3.79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe it’s as easy as an inverse direction of defining the contours as usual. Maybe <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can take a look into it (once he’s back from vacation).</p>

---

## Post #7 by @fedorov (2019-05-21 23:33 UTC)

<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> would be interesting if using <code>plastimatch convert</code> to discretize those contours has the same problem. Can you try that?</p>
<p><a href="http://plastimatch.org/plastimatch.html" class="onebox" target="_blank" rel="nofollow noopener">http://plastimatch.org/plastimatch.html</a></p>

---

## Post #8 by @lassoan (2019-05-22 03:01 UTC)

<p>I’ve checked the data set and the problem is that each contour is listed 5 times (see [3006,0050] ContourData fields in the metadata browser). Although each duplicate contour refers to a different image series (via ContourImageSequence), I’m not sure if it is valid to dump all these duplicate contours in one sequence, as there is no way a third-party software could know how it is supposed to interpret these duplicate contours.</p>
<p>Maybe <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can implement a workaround in Slicer that will deal with this very unusual and potentially invalid data representation. In the meantime, you might check with your software provider if they have a new version of their software where this issue is fixed; or maybe you can make some configuration or workflow changes that would prevent exporting of the same contour several times within the same ContourSequence.</p>

---

## Post #9 by @Alex_Vergara (2019-05-22 07:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a><br>
The software provider is Dosisoft, the planning system that exported the RTStructs is planetDose. This is a standard exportation of an already defined segmentation used for dosimetry. The repetitions is because we require one segmentation per time point (5). So you can just take the first one on each structure which is the most relevant. I don’t know a simple workaround to handle this case. But anyways, Slicer shall be able to detect the repeated structures and ask to import them all or just one, in each RTSTRUCT file. In any case, I will ask Dosisoft if there is a way to export only one segment per structure.</p>

---

## Post #10 by @Alex_Vergara (2019-05-22 08:25 UTC)

<p>As you can see there is no output even when plastimatch says it is OK</p>
<pre><code class="lang-bash">E15AVG:RTStruct_20181114151700455_Liveralltimes alex$ plastimatch convert --input RS.1er_Tx.1.3.6.1.4.1.33868.20181114151634.7910670.dcm --output-img RS.1er_Tx.nrrd --output-type float
Found RTSTUCT, UID=1.3.6.1.4.1.33868.20181114151700.69827
Found DCM_ReferencedFrameOfReferenceSequence!
Found DCM_RTReferencedStudySequence!
Trying to load rt structure set.
Adding structure (3), Liver - R
Structure 3 has color 0\205\209
PIH is:
Origin = -137.1192 -71.1401 -35.0000
Size = 512 512 30
Spacing = 0.3733 0.3733 5.0000
Direction = 1.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 1.0000
Rt_study_warp: Convert ss_img to cxt.
Rt_study_warp: Apply dicom_dir.
Rt_study_warp: Set geometry from PIH.
Rt_study_warp: Set rasterization geometry.
rast_dim = 512 512 30
rast_offset = -137.119 -71.1401 -35
rast_spacing = 0.373258 0.373258 5
Rt_study_warp: warp and save ss.
Warp_and_save_ss: save_ss_img
Finished!
E15AVG:RTStruct_20181114151700455_Liveralltimes alex$ ls
RS.1er_Tx.1.3.6.1.4.1.33868.20181114151634.7910670.dcm
RS.1er_Tx.1.3.6.1.4.1.33868.20181114151634.7910670.dcm.ig.img.hdr
</code></pre>

---

## Post #11 by @gcsharp (2019-05-22 13:49 UTC)

<blockquote>
<p>I’m not sure if it is valid to dump all these duplicate contours in one sequence</p>
</blockquote>
<p>Valid, but semantically unclear.  Separate ROI for each timepoint would be a better choice.</p>
<blockquote>
<p>So you can just take the first one on each structure which is the most relevant.</p>
</blockquote>
<p>Unfortunately it’s not that simple.  At a given Z coordinate, you may have a single contour, or multiple contours.  If it is a single contour, how does one know it belongs to the first, or the second, or the nth version of the structure?  If the Referenced SOP Instance UID were used correctly, one could potentially analyze the referenced images and figure this out.  But the in the RTSTRUCT you have shared, the multiple contours at a given Z coordinate reference the same CT slice.</p>
<p><code>plastimatch convert --input RS.1er_Tx.1.3.6.1.4.1.33868.20181114151634.7910670.dcm --output-img RS.1er_Tx.nrrd --output-type float</code></p>
<p>Plastimatch will interpret this as the union of all contours by default.  If that is acceptable, I suggest the below syntax.</p>
<p><code>plastimatch convert --input rtstruct-file.dcm --referenced-ct DICOM/ --output-prefix structures</code></p>

---

## Post #12 by @Alex_Vergara (2019-05-22 16:16 UTC)

<p>That worked, well sort off! It created a labelmap:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf6dee8dd686789e337d521b831225250a33ea99.png" data-download-href="/uploads/short-url/tB0mAkiKjmlUXGPGynTzUsnffCN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf6dee8dd686789e337d521b831225250a33ea99_2_439x375.png" alt="image" data-base62-sha1="tB0mAkiKjmlUXGPGynTzUsnffCN" width="439" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf6dee8dd686789e337d521b831225250a33ea99_2_439x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf6dee8dd686789e337d521b831225250a33ea99_2_658x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf6dee8dd686789e337d521b831225250a33ea99_2_878x750.png 2x" data-dominant-color="181815"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">991×845 99.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But trying to convert to Segments raises an error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/466fff6ca81f32e30a5266de61dc0b774a89ace4.png" alt="image" data-base62-sha1="a37nndwtXlfT5I53PxmBUYDedE0" width="573" height="432"><br>
Thanks anyway, I think I am closer to the truth now.</p>
<p>Edit: Deleting the previous segmentation and creating a new empty one solved the problem!<br>
That plastimatch line is indeed the solution, would be nice to have it in Slicer by default!</p>

---

## Post #13 by @Alex_Vergara (2019-05-22 16:21 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="11" data-topic="6866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>plastimatch convert --input rtstruct-file.dcm --referenced-ct DICOM/ --output-prefix structures</p>
</blockquote>
</aside>
<p>This is the solution</p>

---

## Post #14 by @lassoan (2019-05-22 20:05 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="11" data-topic="6866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Valid, but semantically unclear. Separate ROI for each timepoint would be a better choice.</p>
</blockquote>
</aside>
<p>I agree, I checked the DICOM standard and it is not explicitly forbidden to insert redundant/contradicting contours. Nevertheless, I’m quite sure that this dumping of contours from various sequences into a single structure can only be interpreted by dosisoft’s own software. There is no way other software could know that if the contour refers to different images then they should be interpreted as separate contours.</p>
<p>In case of this specific data set, all the repeated contours are exactly the same, so by Plastimatch computing of the union it produces correct results. But of course this will break as soon as the contours are not the same in all repetitions.</p>
<p>To not pollute our DICOM importers with various vendor-specific workarounds, we usually address this kind of DICOM content issues by adding new rules to Slicer’s DICOM patcher module. So, if dosisoft is not willing to change their ways then we can add a new DICOM patcher rule (split segments if an RTSTRUCT produced by dosisoft refer multiple image series in the same structure).</p>
<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> Please report this issue to dosisoft. They are probably aware that they have cut some corners but they should also know that it is hurting their users.</p>

---

## Post #15 by @ylcnkzy (2021-08-27 08:31 UTC)

<p>Hello, I have the same issue with my data. Is it possible to make a video and share it? I really couldn’t solve the problem. I have the complete RTstruct data (with several annotations for Lung, Heart, etc.). I can visualize it in the DICOM database of the slicer, but that’s all. I cannot open it and use it for segmentation. Any idea? or Recommendation?</p>
<p>Thanks in Advance!</p>

---

## Post #16 by @lassoan (2021-08-27 22:24 UTC)

<p>Is your structure set generated by dosisoft software?</p>

---

## Post #17 by @ylcnkzy (2021-08-30 08:30 UTC)

<p>Hi Lassoan, Thanks for the quick reply. It says that " Electa`s XiO® proton therapy treatment". The software is XiO when we check RTSTRUCT data via MatLab. I can visualize the RTSTRUCT file via MITK software, but not the 3D slicer.</p>
<p>Best,</p>

---

## Post #18 by @lassoan (2021-08-30 13:00 UTC)

<p>Can you upload an anonymized data set somewhere and post the link here?</p>

---

## Post #19 by @ylcnkzy (2021-08-31 09:01 UTC)

<p>Hi Lassoan,</p>
<p>It seems like I have solved the issue. It seems like I was missing with <strong>SlicerRT Extension</strong>. After I added the extension, it started working like a charm (attached).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/360292d05e3e507746f070938682573b5d89bbcb.jpeg" data-download-href="/uploads/short-url/7HNipZKpkkjcu6Hu9Xc26GrzdEf.jpeg?dl=1" title="Slicer-RTSTRUCT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/360292d05e3e507746f070938682573b5d89bbcb_2_690x364.jpeg" alt="Slicer-RTSTRUCT" data-base62-sha1="7HNipZKpkkjcu6Hu9Xc26GrzdEf" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/360292d05e3e507746f070938682573b5d89bbcb_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/360292d05e3e507746f070938682573b5d89bbcb_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/360292d05e3e507746f070938682573b5d89bbcb.jpeg 2x" data-dominant-color="222022"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-RTSTRUCT</span><span class="informations">1275×673 62.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can also extract the volumetric analysis, etc.</p>
<p>Thank you very much for all.!</p>

---
