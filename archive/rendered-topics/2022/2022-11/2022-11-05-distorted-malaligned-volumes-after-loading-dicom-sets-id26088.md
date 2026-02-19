---
topic_id: 26088
title: "Distorted Malaligned Volumes After Loading Dicom Sets"
date: 2022-11-05
url: https://discourse.slicer.org/t/26088
---

# Distorted & malaligned volumes after loading DICOM sets

**Topic ID**: 26088
**Date**: 2022-11-05
**URL**: https://discourse.slicer.org/t/distorted-malaligned-volumes-after-loading-dicom-sets/26088

---

## Post #1 by @MCM-Fischer (2022-11-05 23:34 UTC)

<p>Hello</p>
<p>I’ve got multiple DICOM datasets that are not properly loaded by Slicer.</p>
<p>The volumes are distorted and are incorrectly aligned to each other.<br>
The distortion is caused by an incorrect scaling along the superoinferior axis.</p>
<p>As comparison the same datasets were loaded using Mimics:<br>
Incorrect length of the bones in Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ecda1b8f449ebfa21a3e654c4afa56cf532e403.jpeg" alt="025_Slicer_Femur_Length" data-base62-sha1="dwFrF4rNqexKB19zNznNLQ933Mv" width="297" height="403"><br>
Same dataset in Mimics:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d77f4ee1d15675d0dd3b7d4aa37c0d513858b698.jpeg" alt="025_Mimics_Femur_Length" data-base62-sha1="uKnpzTygQsAp8q0bt4BuiINCg64" width="201" height="389"><br>
Incorrect relative position of volumes in Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54450c0f432ca5bd812fbb6b3febd348241fa60b.jpeg" alt="025_Slicer_Alignement" data-base62-sha1="c1u2uM3Yv4hrWwnI648RkhN7VF1" width="233" height="417"><br>
Same dataset in Mimics:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e8b18db138ef129d2204360822219716e11b471.jpeg" data-download-href="/uploads/short-url/24EHjVHAx5um8sfqSAgYcdIaYvL.jpeg?dl=1" title="025_Mimics_Alignement" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8b18db138ef129d2204360822219716e11b471_2_169x500.jpeg" alt="025_Mimics_Alignement" data-base62-sha1="24EHjVHAx5um8sfqSAgYcdIaYvL" width="169" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8b18db138ef129d2204360822219716e11b471_2_169x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8b18db138ef129d2204360822219716e11b471_2_253x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e8b18db138ef129d2204360822219716e11b471.jpeg 2x" data-dominant-color="7DCF62"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">025_Mimics_Alignement</span><span class="informations">260×768 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The anonymized DICOM Images can be downloaded here:<br>
<a href="https://bit.ly/3TalCrU" class="onebox" target="_blank" rel="noopener nofollow ugc">https://bit.ly/3TalCrU</a></p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2022-11-05 23:38 UTC)

<p>How did you load the images, with which Slicer version? Did you get any warning during loading?</p>
<p>You need to use the DICOM module to load DICOM images. If the image has variable spacing between slices then make sure acquisition geometry regularization is enabled (it is enabled by default in recent Slicer versions).</p>

---

## Post #3 by @MCM-Fischer (2022-11-06 08:24 UTC)

<p>Hi lassoan</p>
<p>I tried both the latest stable (5.0.3) and preview (5.1.0) release.</p>
<p>I did not get any warning in Slicer neither by pressing “Examine” nor “Load” in the DICOM module.<br>
(In Mimics there is a warning in the Log: “Warning: The files are not possible to import in strict mode”)</p>
<p>The acquisition geometry regularization in Slicer was not enabled in 5.1.0.<br>
I have switched it on now.</p>
<p>It seems to fix the distortion issue.<br>
However, the incorrect relative position of the volumes remains (foot and knee at the same position in the picture) and it also seems to introduce other problems:</p>
<ol>
<li>Offset between the volume and the volume rendering (see distance measurement in the picture).</li>
<li>Segmentation of the cortical bone is not possible anymore (see threshold range in the picture).</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/770817493dbefdb9ba9e8cb79000e2c59c6db4b1.jpeg" data-download-href="/uploads/short-url/gZ09xa0Y1tQAMTqK0WNUt0kdGVz.jpeg?dl=1" title="Segmentation_and_Offset_Issues" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770817493dbefdb9ba9e8cb79000e2c59c6db4b1_2_690x364.jpeg" alt="Segmentation_and_Offset_Issues" data-base62-sha1="gZ09xa0Y1tQAMTqK0WNUt0kdGVz" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770817493dbefdb9ba9e8cb79000e2c59c6db4b1_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770817493dbefdb9ba9e8cb79000e2c59c6db4b1_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770817493dbefdb9ba9e8cb79000e2c59c6db4b1_2_1380x728.jpeg 2x" data-dominant-color="7C7C7B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segmentation_and_Offset_Issues</span><span class="informations">1921×1016 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best regards</p>

---

## Post #4 by @pieper (2022-11-06 15:41 UTC)

<p>Thanks for sharing the anonymized data.  Try hardening the acquisition transform (switch to Transform hierarchy in the Data module and right click on the volume).  This will resample the volume to uniform slice spacing.  It seems to fix both your issues in my tests.</p>
<p>We don’t apply hardening automatically in case people want to control the resampling resolution but I’m thinking we should do more to alert people that some things won’t work when a transform is applied.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/596683994838c7fa4975599fe71ad4653a2cf985.jpeg" data-download-href="/uploads/short-url/cKS84AodJlUR4Tr8vgQLrUROw4d.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/596683994838c7fa4975599fe71ad4653a2cf985_2_199x500.jpeg" alt="image" data-base62-sha1="cKS84AodJlUR4Tr8vgQLrUROw4d" width="199" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/596683994838c7fa4975599fe71ad4653a2cf985_2_199x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/596683994838c7fa4975599fe71ad4653a2cf985_2_298x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/596683994838c7fa4975599fe71ad4653a2cf985_2_398x1000.jpeg 2x" data-dominant-color="8587B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">417×1046 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @MCM-Fischer (2022-11-06 16:51 UTC)

<p>Hi pieper</p>
<p>Great. That worked and solved the issues.</p>
<p>I now recognized that there actually is an warning in the Python console when loading the volumes:<br>
<em>^ Irregular volume geometry detected (maximum error of 459.5 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.</em><br>
<em>^ Irregular volume geometry detected (maximum error of 453.662 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.</em></p>
<p>I think this warning and maybe additional information should be presented to the user.</p>
<p>Thanks for your help<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de2fe8f52a7bc489e2791bb29df5574d3854dddf.jpeg" alt="Harden AGR" data-base62-sha1="vHyDZQBtDtqb6HtenA4NBm5wwxh" width="230" height="418"></p>

---

## Post #6 by @pieper (2022-11-06 18:08 UTC)

<aside class="quote no-group" data-username="MCM-Fischer" data-post="5" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcm-fischer/48/17190_2.png" class="avatar"> MCM-Fischer:</div>
<blockquote>
<p>I think this warning and maybe additional information should be presented to the user.</p>
</blockquote>
</aside>
<p>Yes, I agree.</p>
<p>Maybe we should put up a dialog any log messages were posted during loading.  An option could be to watch signals from the error model during the load process with this signal or similar.</p>
<p><code>slicer.app.errorLogModel().connect("entryAdded(ctkErrorLogLevel::LogLevel", self.trackError)</code></p>

---

## Post #7 by @lassoan (2022-11-06 22:38 UTC)

<p>I had a look at the images. They were loaded incorrectly because they had incorrect SOP Class UID (1.2.840.10008.5.1.4.1.1.7) = <code>Secondary Capture Image Storage</code>. Secondary capture essentially means screenshot, and they are generally not meant to be reconstructed into 3D volumes.</p>
<p>We try to make Slicer behave sensibly for corrupted input data, but DICOM images are so complex that it is impossible to prepare for all the possible ways how they can be messed up.</p>
<p>The limitation of volume rendering not taking into account warping transforms is documented, but it is not realistic to expect users to read the documentation. I’ve submitted an issue to make sure we address this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6648">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6648" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6648" target="_blank" rel="noopener">Warping transform is not taken into account in volume rendering</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-06" data-time="20:35:04" data-timezone="UTC">08:35PM - 06 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

It is [documented](https://slicer.readthedocs.io/en/latest/user_gu<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ide/modules/volumerendering.html#limitations) that "The volume must not be under a warping (affine or non-linear) transformation. To render a warped volume, the transform must be hardened on the volume.". However, we cannot expect users to know about this limitation.

## Environment
- Slicer version: Slicer-5.1.0-2022-11-06
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>We will also review our current choice of using a complex combination of ITK and Slicer for reading DICOM images. Probably we should implement volume rendering construction logic in a Python package. It could be a standalone package that could be used without Slicer, too (just relying on VTK and maybe ITK). <a class="mention" href="/u/pieper">@pieper</a> what do you think? Is there any promising Python package that does something similar that we could improve to fulfill all our needs?</p>

---

## Post #8 by @issakomi (2022-11-06 23:31 UTC)

<blockquote>
<p>I had a look at the images. They were loaded incorrectly because they had incorrect SOP Class UID (1.2.840.10008.5.1.4.1.1.7) = <code>Secondary Capture Image Storage</code>. Secondary capture essentially means screenshot, and they are generally not meant to be reconstructed into 3D volumes.</p>
</blockquote>
<p>Yes, this is often difficult. In fact <em>Secondary Capture Image Storage</em> doesn’t contain <em>Image Position Patient</em>, <em>Image Orientation Patient attributes</em>. But such images are not seldom, i have seen also similar Osirix exports. Many programs don’t read these attributes from SC files.</p>
<p>Here is also another problem<br>
MediaStorageSOPClassUID (0x0002, 0x0002 in image header) is different from SOPClassUID (0x0008, 0x0016).<br>
MediaStorageSOPClassUID is “DCMTK unknown”<br>
SOPClassUID is “Secondary Capture Image”<br>
It is clearly wrong.</p>
<pre><code class="lang-auto">dciodvfy 025/SMIR.Lower_limb.064Y.F.CT.564/SMIR.Lower_limb.064Y.F.CT.564.0.dcm

Error - MediaStorageSOPClassUID different from SOPClassUID
Warning - Value dubious for this VR - (0x0008,0x0090) PN Referring Physician's Name  PN [1] = &lt;unknown referring physician's name&gt; - Retired Person Name form
SCImage
Error - Missing attribute Type 2C Conditional Element=&lt;Laterality&gt; Module=&lt;GeneralSeries&gt;
Error - Missing attribute Type 2C Conditional Element=&lt;PatientOrientation&gt; Module=&lt;GeneralImage&gt;
Error - Missing attribute Type 1C Conditional Element=&lt;RescaleType&gt; Module=&lt;ModalityLUTMacro&gt;
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x0050) DS Slice Thickness 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x0060) DS KVP 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x0088) DS Spacing Between Slices 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x0090) DS Data Collection Diameter 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1100) DS Reconstruction Diameter 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1110) DS Distance Source to Detector 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1111) DS Distance Source to Patient 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1120) DS Gantry/Detector Tilt 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1130) DS Table Height 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1140) CS Rotation Direction 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1150) IS Exposure Time 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1151) IS X-Ray Tube Current 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1152) IS Exposure 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1160) SH Filter Type 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1170) IS Generator Power 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1190) DS Focal Spot(s) 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1210) SH Convolution Kernel 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x0032) DS Image Position (Patient) 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x0037) DS Image Orientation (Patient) 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x0052) UI Frame of Reference UID 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x1041) DS Slice Location 
Warning - Dicom dataset contains attributes not present in standard DICOM IOD - this is a Standard Extended SOP Class
</code></pre>
<p>The attributes are from <em>CT Image Storage</em>.</p>

---

## Post #9 by @lassoan (2022-11-07 04:03 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Maybe we should put up a dialog any log messages were posted during loading.</p>
</blockquote>
</aside>
<p>We do this already, but we only report errors that Slicer finds. ITK reader does not provide any warnings or errors, it just silently fails - reporting (1,1,1) spacing and (0,0,0) origin if it cannot determine the correct value. This is a quite serious limitation of ITK’s DICOM reader. Slicer checks consistency of the image geometry based on <code>Image Position Patient</code> and <code>Image Orientation Patient tags</code> and reports to the user if something seems wrong. However, in this case the values in these fields were correct but the problem was that these were not the fields that were supposed to be used (due to the incorrect SOP class UID). Since ITK does not report any issues and Slicer did not detect any issues, no errors were displayed to the user. When acquisition geometry regularization was enabled then Slicer detected that ITK’s image geometry looks incorrect and it took over, but this is usually not an error case (that’s how things supposed to work), so this is not reported to the user as a problem.</p>
<p>So, it was an unfortunate, unusual way of messing up a DICOM image, that got through our current error detection mechanisms. Enabling acquisition geometry regularization by default would have helped. I thought it is enabled by default in current Slicer version, but apparently not, so I’ve submitted a pull request to change the default - see:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6649">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6649" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6649" target="_blank" rel="noopener">ENH: Regularize acquisition geometry by default for DICOM image loading</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:dicom-regularize-acq-geom-by-default</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-07" data-time="04:02:26" data-timezone="UTC">04:02AM - 07 Nov 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 6 additions and 4 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6649/files" target="_blank" rel="noopener">
            <span class="added">+6</span>
            <span class="removed">-4</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Image acquisition geometry regularization has proven to work well over the past <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6649" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">several years (it allows loading unusual image geometries correctly and does not seem to result in extra complications), therefore it makes sense to enable it by default.

See the most recent related discussion at https://discourse.slicer.org/t/distorted-malaligned-volumes-after-loading-dicom-sets/26088/8

It is probably safe to include this in Slicer-5.2 stable, but waiting until Slicer-5.3 preview should not be a problem either (then we could integrate it along with a fix for https://github.com/Slicer/Slicer/issues/6648).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @pieper (2022-11-07 21:23 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Maybe we should put up a dialog any log messages were posted during loading.</p>
</blockquote>
</aside>
<p>We do this already, but we only report errors that Slicer finds.</p>
</blockquote>
</aside>
<p>With 5.0.3 and my local build the message only comes up in the python console as <a class="mention" href="/u/mcm-fischer">@MCM-Fischer</a> reported.  The message comes via <code>logging.warning</code> from the scalar volume plugin, so it shows up in the console and the error log but there’s no dialog box in this case.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably we should implement volume rendering construction logic in a Python package. It could be a standalone package that could be used without Slicer, too (just relying on VTK and maybe ITK). <a class="mention" href="/u/pieper">@pieper</a> what do you think? Is there any promising Python package that does something similar that we could improve to fulfill all our needs?</p>
</blockquote>
</aside>
<p>Yes, I started down that path when I added the option to use either <code>gdcm</code> or <code>dcmtk</code> in the reader based on some experience we had with them behaving differently in their ability to handle certain datasets.  We could add another path there to a pydicom-based parser.  There are some other packages like <code>dicomstack</code> and some extensions that were being worked on <a href="https://github.com/matthew-brett/czi-nibabel">in <code>nibabel</code></a>.</p>
<p>I think yes, we should try to factor out all the Slicer dicom parsing into python packages for general purpose use.  Our dicom plugins can then depend on those and can add a layer to create the MRML representations of the parsed objects.</p>

---

## Post #11 by @lassoan (2022-11-08 02:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>With 5.0.3 and my local build the message only comes up in the python console as <a class="mention" href="/u/mcm-fischer">@MCM-Fischer</a> reported. The message comes via <code>logging.warning</code> from the scalar volume plugin, so it shows up in the console and the error log but there’s no dialog box in this case.</p>
</blockquote>
</aside>
<p>Yes, only those errors are displayed in a popup that <em>Slicer</em> detects. Slicer only detects inconsistencies of <code>Image Position Patient</code> and <code>Image Orientation Patient</code> values, and in this case these values were consistent, only the incorrect SOP class UID prevented ITK from using them. Unfortunately, ITK does not provide any warnings or errors.</p>
<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We could add another path there to a pydicom-based parser. There are some other packages like <code>dicomstack</code> and some extensions that were being worked on <a href="https://github.com/matthew-brett/czi-nibabel">in <code>nibabel</code></a>.</p>
</blockquote>
</aside>
<p>You are right that probably there is no single toolkit that can handle all types of data sets. There is no single person, or even group, who would be aware of all details, error cases, ways how various device manufacturers messed up their implementations, etc. for all kinds of data sets, ranging from brain diffusion imaging to 4D cardiac ultrasound. Instead, we should choose a few high-quality implementations that cover all use cases.</p>
<p>In addition to DCMTK, GDCM, nibabel, and dcmtk, there is also <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> and <a href="http://dgobbi.github.io/vtk-dicom/">vtkDICOM</a>.</p>

---

## Post #12 by @issakomi (2022-11-08 05:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="26088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer only detects inconsistencies of <code>Image Position Patient</code> and <code>Image Orientation Patient</code> values, and in this case these values were consistent, only the incorrect SOP class UID prevented ITK from using them. Unfortunately, ITK does not provide any warnings or errors.</p>
</blockquote>
</aside>
<p>This behavior is caused by GDCM. GDCM refuses to process <em>Image Position Patient Patient</em> and <em>Image Orientation Patient</em> for <em>Secondary Capture Image Storage</em>.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L732">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L732" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L732" target="_blank" rel="noopener nofollow ugc">InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L732</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="722" style="counter-reset: li-counter 721 ;">
          <li>        dircos[3] = 0;</li>
          <li>        dircos[4] = 1;</li>
          <li>        dircos[5] = 0;</li>
          <li>        }</li>
          <li>      return dircos;</li>
          <li>      }</li>
          <li>    }</li>
          <li>  }</li>
          <li></li>
          <li>dircos.resize( 6 );</li>
          <li class="selected">if( ms == MediaStorage::SecondaryCaptureImageStorage || !GetDirectionCosinesFromDataSet(ds, dircos) )</li>
          <li>  {</li>
          <li>  dircos[0] = 1;</li>
          <li>  dircos[1] = 0;</li>
          <li>  dircos[2] = 0;</li>
          <li>  dircos[3] = 0;</li>
          <li>  dircos[4] = 1;</li>
          <li>  dircos[5] = 0;</li>
          <li>  }</li>
          <li></li>
          <li>assert( dircos.size() == 6 );</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L580">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L580" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L580" target="_blank" rel="noopener nofollow ugc">InsightSoftwareConsortium/ITK/blob/dca4a36dde8dc4b45efff4ef7df411e7010d0163/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L580</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="570" style="counter-reset: li-counter 569 ;">
          <li>      }</li>
          <li>    }</li>
          <li>  ori.resize( 3 );</li>
          <li>  gdcmWarningMacro( "Could not find Origin" );</li>
          <li>  return ori;</li>
          <li>  }</li>
          <li>ori.resize( 3 );</li>
          <li></li>
          <li>// else</li>
          <li>const Tag timagepositionpatient(0x0020, 0x0032);</li>
          <li class="selected">if( ms != MediaStorage::SecondaryCaptureImageStorage &amp;&amp; ds.FindDataElement( timagepositionpatient ) )</li>
          <li>  {</li>
          <li>  const DataElement&amp; de = ds.GetDataElement( timagepositionpatient );</li>
          <li>  Attribute&lt;0x0020,0x0032&gt; at = {{0,0,0}}; // default value if empty</li>
          <li>  at.SetFromDataElement( de );</li>
          <li>  for( unsigned int i = 0; i &lt; at.GetNumberOfValues(); ++i )</li>
          <li>    {</li>
          <li>    ori[i] = at.GetValue(i);</li>
          <li>    }</li>
          <li>  }</li>
          <li>else</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also spacing is not taken from 0x0028, 0x0030 for SC, if i remember correctly.</p>

---

## Post #13 by @Davide_Punzo (2023-11-13 08:38 UTC)

<p>SIDE NOTE: Support for regularization transform hardening in DICOM Scalar plugin has been added. See <a href="https://discourse.slicer.org/t/enh-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">link</a>.</p>

---
