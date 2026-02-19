---
topic_id: 17428
title: "Cranial And Caudal Directions Are Opposite When Loading Sequ"
date: 2021-05-04
url: https://discourse.slicer.org/t/17428
---

# Cranial and caudal directions are opposite when loading sequence of DICOM images

**Topic ID**: 17428
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/cranial-and-caudal-directions-are-opposite-when-loading-sequence-of-dicom-images/17428

---

## Post #1 by @xackey (2021-05-04 01:43 UTC)

<p>Hi.<br>
When loading sequence of DICOM images (“Load Data”&lt;&lt;Chose File(s) to Add"), loading order of files is different between version 4.10.2 and nightly version (4.13.0). I think version 4.10.2 is correct, but caudal and cranial directions are opposite in nightly version.</p>
<p>Can you solve this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9e602080c8cb3f1f384988246ab116dfee6b4d.jpeg" data-download-href="/uploads/short-url/fm2pfyBWiIxTWs4v487ccXRjQFT.jpeg?dl=1" title="fig1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b9e602080c8cb3f1f384988246ab116dfee6b4d_2_689x290.jpeg" alt="fig1" data-base62-sha1="fm2pfyBWiIxTWs4v487ccXRjQFT" width="689" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b9e602080c8cb3f1f384988246ab116dfee6b4d_2_689x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b9e602080c8cb3f1f384988246ab116dfee6b4d_2_1033x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9e602080c8cb3f1f384988246ab116dfee6b4d.jpeg 2x" data-dominant-color="64645F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig1</span><span class="informations">1148×484 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b3cb88bb76051a29a7d179c6f2fb3df289d9409.jpeg" data-download-href="/uploads/short-url/hAcP0FucZigv8oxREbtvAez47pf.jpeg?dl=1" title="fig2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b3cb88bb76051a29a7d179c6f2fb3df289d9409_2_690x287.jpeg" alt="fig2" data-base62-sha1="hAcP0FucZigv8oxREbtvAez47pf" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b3cb88bb76051a29a7d179c6f2fb3df289d9409_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b3cb88bb76051a29a7d179c6f2fb3df289d9409_2_1035x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b3cb88bb76051a29a7d179c6f2fb3df289d9409.jpeg 2x" data-dominant-color="555550"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig2</span><span class="informations">1162×485 93.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-05-04 13:06 UTC)

<p>What kind of scanner are these from?  Did you load with the DICOM module or the load data dialog?</p>
<p>Is there any chance you can share data that reproduces this issue?</p>

---

## Post #3 by @issakomi (2021-05-04 16:27 UTC)

<p>Probably the same (it is about how to sort slices if IPP/IOP is not available)</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1587" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1587" target="_blank" rel="noopener nofollow ugc">Some DICOM volumes are loaded flipped along Z axis in ITK-v5.1rc01</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-02-02" data-time="18:11:47" data-timezone="UTC">06:11PM - 02 Feb 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:Bug</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### Description

Some volumes are flipped along their Z axis (ordering of slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">es is inverted). Other axes are not inverted, so it is not a rotation but a mirroring along one axis. It worked well in the previous ITK 5 release.

![image](https://user-images.githubusercontent.com/307929/73612832-5d9e1c80-45bd-11ea-9fcf-996f745d2c9e.png)

### Steps to Reproduce

Load the DICOM volume using ITK-5.0 and ITK-5.1rc01 and compare them in a sagittal view.

### Expected behavior

They should look the same.

### Actual behavior

There is a flip along the IS axis.

### Reproducibility

I can provide an anonymized data set on request but it is not for public sharing.

### Versions

ITK-v5.1rc01

### Environment

Windows, Visual Studio 2015</span></p>
  </div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @xackey (2021-05-04 21:15 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a><br>
Yes! This is the same problem.</p>

---

## Post #5 by @xackey (2021-05-05 00:36 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<ol>
<li>The CT scanner is from Siemens, but the same problem happened on Toshiba CT. So, this problem is not related to the kind of CT scanner.</li>
<li>I used “Load Data” (not “Load DICOM Data”). But when I loaded images using “Load DICOM Data”, image orientation (z direction) became correct.</li>
<li>When I renamed the DICOM files in reverse order (i.e., change from 1, 2, 3, 4 to 4, 3, 2, 1), ordering of slices was inverted (changed from inverted view to correct view).  So, maybe this problem is related to loading order of image files.</li>
</ol>

---

## Post #6 by @pieper (2021-05-05 22:28 UTC)

<p><a class="mention" href="/u/xackey">@xackey</a>, does the Slicer DICOM module warn you about geometry issues with this data?</p>
<p>If it’s really the case that ITK is using the file name rather than the Image Position Patient tags in the dicom header to sort the images this is a terrible regression.  I haven’t really thought about it since the discussion on the ITK issue tracker last summer, but I’m really surprised this hasn’t been fixed.  <a class="mention" href="/u/lassoan">@lassoan</a> what do you think?</p>

---

## Post #7 by @issakomi (2021-05-06 00:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="17428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If it’s really the case that ITK is using the file name rather than the Image Position Patient tags in the dicom header to sort the images this is a terrible regression.</p>
</blockquote>
</aside>
<p>In GDCM <em>IPP/IOP</em> ordering is the first choice (there is also an option for user-derined ordering, but is unused), if it fails then <em>Image Number</em> tag is used, if it fails too then file names. The change was to use <em>Image Number</em>. There is a link to GDCM commit in ITK issue discussion above.</p>
<p>S. <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/0de9cfe31d42b4a5640e2baae494e99eccdcf347/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmSerieHelper.cxx#L430" rel="noopener nofollow ugc">gdcmSerieHelper.cxx</a></p>

---

## Post #8 by @lassoan (2021-05-06 01:38 UTC)

<p>I could not reproduce the flipping issue by specifying a single DICOM file for ITK. Slicer’s frame sorter works well, too. The problem only occurs when somebody uses the “Add data” dialog in Slicer to load DICOM data - it somehow uses the ITK DICOM reader in an incorrect way.</p>
<p>I’ve never really understood how DICOM loading via “Add data” dialog is supposed to work and why it is so complex. I think the best would be to remove this loading method, as it has many other limitations anyway.</p>

---

## Post #9 by @xackey (2021-05-06 02:39 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<blockquote>
<blockquote>
<p>does the Slicer DICOM module warn you about geometry issues with this data?<br>
→Do you mean viewing a “Error log”? I show a log after loading the DICOM files.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c51c7dccddec8eeee5b00d1b9aa3f2d84c0e94d.jpeg" data-download-href="/uploads/short-url/1KYWwNa4w49jDIpOvDJnF2UbTEp.jpeg?dl=1" title="log" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c51c7dccddec8eeee5b00d1b9aa3f2d84c0e94d_2_690x424.jpeg" alt="log" data-base62-sha1="1KYWwNa4w49jDIpOvDJnF2UbTEp" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c51c7dccddec8eeee5b00d1b9aa3f2d84c0e94d_2_690x424.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c51c7dccddec8eeee5b00d1b9aa3f2d84c0e94d_2_1035x636.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c51c7dccddec8eeee5b00d1b9aa3f2d84c0e94d.jpeg 2x" data-dominant-color="ECECF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">log</span><span class="informations">1156×712 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
</blockquote>
<p>If this problem can be resolved by changing application settings of 3D Slicer, could you tell me how to do it.<br>
Thank you!</p>

---

## Post #10 by @xackey (2021-05-06 09:57 UTC)

<p>I tried public DICOM images, but I have the same result; version 4.10.2 is correct view, but 4.13.0 is flipped.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8e689afd78be1d6ad2494794c5d5f2c6be6e54b.jpeg" data-download-href="/uploads/short-url/sFfpZ948RcyRL23Ah0YzQqfJ1uX.jpeg?dl=1" title="Fig3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8e689afd78be1d6ad2494794c5d5f2c6be6e54b_2_690x297.jpeg" alt="Fig3" data-base62-sha1="sFfpZ948RcyRL23Ah0YzQqfJ1uX" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8e689afd78be1d6ad2494794c5d5f2c6be6e54b_2_690x297.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8e689afd78be1d6ad2494794c5d5f2c6be6e54b_2_1035x445.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8e689afd78be1d6ad2494794c5d5f2c6be6e54b_2_1380x594.jpeg 2x" data-dominant-color="878785"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig3</span><span class="informations">1654×714 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I attached the link of the DICOM images below. Could you check whether the issue will be reproduced?</p>
<p><a href="https://drive.google.com/drive/folders/14s0U2WJyVQ0u-Ni5U8ulet0Yy0fAccZc?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/14s0U2WJyVQ0u-Ni5U8ulet0Yy0fAccZc?usp=sharing</a></p>

---

## Post #11 by @issakomi (2021-05-06 18:11 UTC)

<p>I could not reproduce the problem in Slicer (and in my app too).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c5d427e407568378dd5ec20245ce59268a46fce.jpeg" data-download-href="/uploads/short-url/db5JAGCaCE9wyryRiXm9bxVb0my.jpeg?dl=1" title="Screenshot at 2021-05-06 20-04-56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d427e407568378dd5ec20245ce59268a46fce_2_517x362.jpeg" alt="Screenshot at 2021-05-06 20-04-56" data-base62-sha1="db5JAGCaCE9wyryRiXm9bxVb0my" width="517" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d427e407568378dd5ec20245ce59268a46fce_2_517x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d427e407568378dd5ec20245ce59268a46fce_2_775x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d427e407568378dd5ec20245ce59268a46fce_2_1034x724.jpeg 2x" data-dominant-color="B4B3B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2021-05-06 20-04-56</span><span class="informations">1151×807 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Edit:</p>
<p><a class="mention" href="/u/xackey">@xackey</a></p>
<p>Oops, i have reproduced, in fact, with “Load Data” dialog (select a folder)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de632dca7193bbc3f42876053664e2a1716dee2d.png" data-download-href="/uploads/short-url/vJkugBbcmvOGeYH6bjr4AqfhJ9z.png?dl=1" title="Screenshot at 2021-05-06 20-30-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de632dca7193bbc3f42876053664e2a1716dee2d_2_517x366.png" alt="Screenshot at 2021-05-06 20-30-20" data-base62-sha1="vJkugBbcmvOGeYH6bjr4AqfhJ9z" width="517" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de632dca7193bbc3f42876053664e2a1716dee2d_2_517x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de632dca7193bbc3f42876053664e2a1716dee2d_2_775x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de632dca7193bbc3f42876053664e2a1716dee2d_2_1034x732.png 2x" data-dominant-color="B3B2B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2021-05-06 20-30-20</span><span class="informations">1130×802 363 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @pieper (2021-05-06 19:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="17428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think the best would be to remove this loading method, as it has many other limitations anyway.</p>
</blockquote>
</aside>
<p>Yes, I think now (as part of slicer5) we stop letting people load dicom via that legacy Add Data code.  For now I would at least way we should consider it ill-advised.</p>
<p>I’d still argue this must be a regression in ITK because the dataset that reproduces the issue <em>does</em> have valid ImagePostiionPatient values that Slicer is able to parse, but for some reason the newer ITK ignores in favor of using the filenames.  Very odd.</p>

---

## Post #13 by @xackey (2021-05-06 22:51 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a><br>
Thank you for trying.<br>
Version 4.10.2 has no such issue even when choosing “Load Data” dialog.<br>
I think there is something difference in data loading systems between version 4.10.2 and 4.13.0.</p>

---

## Post #14 by @issakomi (2021-05-07 08:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="17428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’d still argue this must be a regression in ITK</p>
</blockquote>
</aside>
<p>This ITK example - <a href="https://itk.org/ITKExamples/src/IO/GDCM/ReadDICOMSeriesAndWrite3DImage/Documentation.html" rel="noopener nofollow ugc">ReadDICOMSeriesAndWrite3DImage</a> works fine, sorted by IPP as expected. I have tried C++ version with ITK master and above data set, result - <em>nrrd</em> file - is correct. <a href="https://drive.google.com/file/d/1aWd_liUnb6ladsU8afm12ZrNxqUPlz7G/view?usp=sharing" rel="noopener nofollow ugc">Here</a> is this example with cmake and data set shared above.</p>
<p>I have also compared <em>vtkITKArchetypeImageSeriesReader.cxx</em> from <a href="https://drive.google.com/file/d/1sWyKERmISARtTdFIQ-VTuKzq_dLOfT80/view?usp=sharing" rel="noopener nofollow ugc">4.10.2</a> and from <a href="https://drive.google.com/file/d/1yxWxpm_UrloCnYuHGnL8EiHpqM3skfGD/view?usp=sharing" rel="noopener nofollow ugc">master</a>, they are very different. 100+ lines were changed, specially parts related to DICOM were updated.</p>
<p>I am still not sure what the problem is. I am building Slicer, may be i shall find the source of the problem and report.</p>

---

## Post #15 by @pieper (2021-05-07 12:13 UTC)

<p>Thanks very much for your help with this <a class="mention" href="/u/issakomi">@issakomi</a> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #16 by @lassoan (2021-05-07 13:51 UTC)

<p>I can confirm that ITK examples work well, that’s why I did not ask ITK developers to investigate this change in behavior. There is something special about how Slicer uses ITK’s DICOM reader, and considering how complex that code part is, it is quite possible that Slicer does not use the API correctly.</p>

---

## Post #17 by @issakomi (2021-05-07 13:52 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> You’re welcome.</p>
<p>Highly likely the problem is in <em>vtkITKArchetypeImageSeriesReader.cxx</em>, i have  built Slicer <em>master</em> and have done very quick and dirty port of that file (and .h file) from 4.10.2 (only added things related to new <em>VoxelVectorType</em>). And there is no flip. I shall try to find out what exactly is the issue, but it can take several days, and confirm if it will work.<br>
Here is tiny (20 s) video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="f0uDJ4CUhDo" data-video-title="Test" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=f0uDJ4CUhDo" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/f0uDJ4CUhDo/maxresdefault.jpg" title="Test" width="" height="">
  </a>
</div>


---

## Post #18 by @issakomi (2021-05-08 20:36 UTC)

<p>This bug is in Slicer since <a href="https://github.com/Slicer/Slicer/commit/cbaaa0182974352736b0567cc0eeaff49813d578" rel="noopener nofollow ugc">commit</a> 12 Jan 2020. New function <a href="https://github.com/Slicer/Slicer/blob/6a9cb52eb1a93b031c7388ee5688a28a709fa7b4/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L206" rel="noopener nofollow ugc">itk::ImageIOBase::Pointer vtkITKArchetypeImageSeriesReader::GetImageIO</a> was added. In the function a list of files is <a href="https://github.com/Slicer/Slicer/blob/6a9cb52eb1a93b031c7388ee5688a28a709fa7b4/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L230" rel="noopener nofollow ugc">assembled</a> before check for DICOM IO. And <a href="https://github.com/Slicer/Slicer/blob/6a9cb52eb1a93b031c7388ee5688a28a709fa7b4/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L384" rel="noopener nofollow ugc">later</a>, in <em>vtkITKArchetypeImageSeriesReader::RequestInformation</em>, the <a href="https://github.com/Slicer/Slicer/blob/6a9cb52eb1a93b031c7388ee5688a28a709fa7b4/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L412" rel="noopener nofollow ugc">point</a>, where itk::GDCMSeriesFileNames is called, is not reached.<br>
<code>// if user already set up FileNames, we do not try to find candidate files if ( this-&gt;GetNumberOfFileNames() &gt; 0 )</code></p>

---

## Post #19 by @pieper (2021-05-08 20:53 UTC)

<p>Nice detective work!</p>
<p>This sounds fixable, but we should still consider removing the option to load dicom via that class.  That archetype series code is so hard to maintain and it surely needs a redesign after so many years of patching.</p>

---

## Post #21 by @lassoan (2021-05-10 01:03 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a>, thanks a lot for this investigation!</p>
<p>It seems that we have 3 slice sorting implementations:</p>
<ul>
<li>GDCM: probably robust but most likely it only supports simple cases (e.g., cannot handle 4D volumes with variable spacing)</li>
<li>vtkITKArchetypeImageSeriesReader: very basic implementation, not robust and currently broken. It can be fixed with <a href="https://github.com/Slicer/Slicer/commit/3c92804fa88ca19a6867d518181aef51b31d330d">these changes</a>, but it would require much more work.</li>
<li>DICOMScalarVolumePlugin (and other plugins for 2D+t, 3D+t, etc.): can handle very complex cases. It uses vtkITKArchetypeImageSeriesReader to load a file list.</li>
</ul>
<p>Potential next steps:</p>
<ul>
<li>We should remove the sorter in vtkITKArchetypeImageSeriesReader to reduce redundancy and maintenance workload.</li>
<li>We should also simplify and fix vtkITKArchetypeImageSeriesReader and all subclasses to make errors such as this one easier to avoid in the future. Probably merge all subclasses (vtkITKArchetypeDiffusionTensorImageReaderFile, vtkITKArchetypeImageSeriesReader, vtkITKArchetypeImageSeriesScalarReader, vtkITKArchetypeImageSeriesVectorReaderFile, vtkITKArchetypeImageSeriesVectorReaderSeries) in a single class replace macros by templated functions, etc.</li>
<li>To reduce chance of use errors, we should probably redirect users to the DICOM module for loading DICOM data. Maybe the image reader plugin could detect DICOM data sets and import them to the DICOM database.</li>
</ul>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/fedorov">@fedorov</a> What do you think?</p>

---

## Post #22 by @cpinter (2021-05-10 12:00 UTC)

<p>Each of the steps you listed makes complete sense to me. After many such queries I think it is high time we detect DICOM loading and only allow it via the browser. Also it would be great simplifying the vtkITKArchetypeImageSeriesReader adjacent code.</p>

---

## Post #23 by @pieper (2021-05-10 12:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="17428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably merge all subclasses (vtkITKArchetypeDiffusionTensorImageReaderFile, vtkITKArchetypeImageSeriesReader, vtkITKArchetypeImageSeriesScalarReader, vtkITKArchetypeImageSeriesVectorReaderFile, vtkITKArchetypeImageSeriesVectorReaderSeries)</p>
</blockquote>
</aside>
<p>One historical note: a lot of the logic in these classes is split out because all the template instantiations led to memory issue in old compilers.</p>

---

## Post #24 by @xackey (2021-07-09 23:00 UTC)

<p>Hi.<br>
The issue has not been fixed yet in the latest 3D slicer (4.13.0).<br>
Could you tell me the current status?<br>
Thank you for your help.</p>

---

## Post #25 by @jamesobutler (2021-07-10 01:44 UTC)

<p>DICOM loading using the Load Data Dialog (which is typically used for loading all other files in Slicer) is planned to be disabled. See <a href="https://github.com/Slicer/Slicer/issues/5726" class="inline-onebox" rel="noopener nofollow ugc">Disable DICOM import from "Add data" dialog · Issue #5726 · Slicer/Slicer · GitHub</a>.</p>
<p>You should load DICOM data using the DICOM module. See more details at <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#data-loading-and-saving" class="inline-onebox" rel="noopener nofollow ugc">Data Loading and Saving — 3D Slicer documentation</a>.</p>

---
