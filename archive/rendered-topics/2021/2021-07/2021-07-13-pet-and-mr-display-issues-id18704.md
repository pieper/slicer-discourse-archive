# PET and MR display issues

**Topic ID**: 18704
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/pet-and-mr-display-issues/18704

---

## Post #1 by @dougPorter (2021-07-13 18:37 UTC)

<p>Does anyone have issues displaying PET and MR series in Slicer. Try these and please let me know if you have any ideas on why this happens…</p>
<p><em>(link has been removed until it is confirmed that the images do not contain PHI)</em></p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2021-07-13 20:19 UTC)



---

## Post #3 by @lassoan (2021-07-13 21:04 UTC)

<p>The DICOM header specifies that the pixel values are signed (PixelRepresentation=1):</p>
<pre><code class="lang-auto">[0028,0002]	SamplesPerPixel	1	US	2
[0028,0004]	PhotometricInterpretation	MONOCHROME2	CS	12
[0028,0010]	Rows	128	US	2
[0028,0011]	Columns	128	US	2
[0028,0030]	PixelSpacing	[2] 5.46875, 5.46875	DS	16
[0028,0051]	CorrectedImage	[8] DECY, ATTN, SCAT, DTIM, RAN, DCAL, SLSENS, NORM	CS	40
[0028,0100]	BitsAllocated	16	US	2
[0028,0101]	BitsStored	15	US	2
[0028,0102]	HighBit	14	US	2
[0028,0103]	PixelRepresentation	1	US	2
[0028,0106]	SmallestImagePixelValue	0	SS	2
[0028,0107]	LargestImagePixelValue	32766	SS	2
[0028,1050]	WindowCenter	8438.388323078	DS	14
[0028,1051]	WindowWidth	16876.776646156	DS	16
[0028,1052]	RescaleIntercept	0	DS	2
[0028,1053]	RescaleSlope	0.453101	DS	8
[0028,2110]	LossyImageCompression	00	CS	2
</code></pre>
<p>To me, it seems that Slicer interprets the image correctly and image acquisition device created an incorrect DICOM header, but maybe there are some special cases that I’m not aware of.</p>
<p>Here is a sample image slice:</p>
<p><a href="https://1drv.ms/u/s!Arm_AFxB9yqHxeRDMH6PKINz6CbeQA?e=SjnUk8" class="onebox" target="_blank" rel="noopener">https://1drv.ms/u/s!Arm_AFxB9yqHxeRDMH6PKINz6CbeQA?e=SjnUk8</a></p>
<p>Slicer renders it like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be21e39156b2850e1a5a4069fb4ef105a50cc5e3.png" data-download-href="/uploads/short-url/r7ZkdvZIhzWxxYFpu4QJPMUHb5p.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be21e39156b2850e1a5a4069fb4ef105a50cc5e3_2_509x500.png" alt="image" data-base62-sha1="r7ZkdvZIhzWxxYFpu4QJPMUHb5p" width="509" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be21e39156b2850e1a5a4069fb4ef105a50cc5e3_2_509x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be21e39156b2850e1a5a4069fb4ef105a50cc5e3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be21e39156b2850e1a5a4069fb4ef105a50cc5e3.png 2x" data-dominant-color="858585"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">586×575 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>While it should look like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb790d78e95de835f1a2548c4a20925bc8d1386a.jpeg" data-download-href="/uploads/short-url/qKsDK7hpHgJGrggwFOMZaeddEpk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb790d78e95de835f1a2548c4a20925bc8d1386a_2_644x500.jpeg" alt="image" data-base62-sha1="qKsDK7hpHgJGrggwFOMZaeddEpk" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb790d78e95de835f1a2548c4a20925bc8d1386a_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb790d78e95de835f1a2548c4a20925bc8d1386a_2_966x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb790d78e95de835f1a2548c4a20925bc8d1386a.jpeg 2x" data-dominant-color="0B0B0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1212×940 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/issakomi">@issakomi</a> <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Do you have any insights?</p>

---

## Post #4 by @pieper (2021-07-13 21:19 UTC)

<p>Hi <a class="mention" href="/u/dougporter">@dougPorter</a> -</p>
<p>I agree Slicer appears to be interpreting the pixel values according to the header.</p>
<p>Can you doublecheck that these files are representative of the files you need to support?  I hope these are not like your real clinical images, because they have several inconsistencies as <a class="mention" href="/u/lassoan">@lassoan</a> points out.  My guess is that these are some kind of old research files that were made by a non-standard process so they have errors that wouldn’t occur with real data.  (Some vendors aren’t perfect in their dicom data, but these are particularly bad).</p>
<p>For example when I run <a href="http://dclunie.com/dicom3tools/dciodvfy.html">this standard validation tool</a> there are many red flags.</p>
<pre><code class="lang-auto">% dciodvfy /tmp/TestImages/PET/0.dcm 
Warning - Retired attribute - (0x0032,0x1000) DA Scheduled Study Start Date 
Warning - Retired attribute - (0x0032,0x1001) TM Scheduled Study Start Time 
Warning - Retired attribute - (0x0032,0x1050) DA Study Completion Date 
Warning - Retired attribute - (0x0032,0x1051) TM Study Completion Time 
Warning - Dicom dataset contains retired attributes
PETImage
Error - Missing attribute Type 1 Required Element=&lt;FileMetaInformationGroupLength&gt; Module=&lt;FileMetaInformation&gt;
Warning - is only permitted to be empty when actually unknown; should be absent (not empty) if an unpaired body part, and have a value if a paired body part - attribute &lt;Laterality&gt;
Error - May not be present when PatientOrientationCodeSequence is present - attribute &lt;PatientPosition&gt;
Warning - Unrecognized defined term &lt;SLSENS&gt; for value 7 of attribute &lt;Corrected Image&gt;
Warning - Coding Scheme Designator is deprecated - attribute &lt;CodingSchemeDesignator&gt; = &lt;SNM3&gt;
Warning - Coding Scheme Designator is deprecated - attribute &lt;CodingSchemeDesignator&gt; = &lt;SNM3&gt;
Warning - Coding Scheme Designator is deprecated - attribute &lt;CodingSchemeDesignator&gt; = &lt;SNM3&gt;
Warning - Coding Scheme Designator is deprecated - attribute &lt;CodingSchemeDesignator&gt; = &lt;SNM3&gt;
Error - Missing attribute Type 1 Required Element=&lt;FrameOfReferenceUID&gt; Module=&lt;FrameOfReference&gt;
Error - Unrecognized enumerated value &lt;0xf&gt; for value 1 of attribute &lt;Bits Stored&gt;
Error - Unrecognized enumerated value &lt;0xe&gt; for value 1 of attribute &lt;High Bit&gt;
Error - Attribute present when condition unsatisfied (which may not be present otherwise) Type 1C Conditional Element=&lt;TriggerTime&gt; Module=&lt;PETImage&gt;
Error - Attribute present when condition unsatisfied (which may not be present otherwise) Type 1C Conditional Element=&lt;FrameTime&gt; Module=&lt;PETImage&gt;
Warning - Coding Scheme Designator is deprecated - attribute &lt;CodingSchemeDesignator&gt; = &lt;SRT&gt;
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1000) DA Scheduled Study Start Date 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1001) TM Scheduled Study Start Time 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1032) PN Requesting Physician 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1050) DA Study Completion Date 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1051) TM Study Completion Time 
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x0100) SH Code Value 
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x0102) SH Coding Scheme Designator 
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x0104) LO Code Meaning 
Warning - Attribute is not present in standard DICOM IOD - (0x0054,0x0412) SQ Patient Orientation Modifier Code Sequence 
Warning - Dicom dataset contains attributes not present in standard DICOM IOD - this is a Standard Extended SOP Class
</code></pre>
<p>and</p>
<pre><code class="lang-auto">% dciodvfy /tmp/TestImages/MR/0.dcm
Warning - Retired attribute - (0x0008,0x0040) US Data Set Type 
Warning - Retired attribute - (0x0008,0x0041) LO Data Set Subtype 
Warning - Retired attribute - (0x0032,0x1000) DA Scheduled Study Start Date 
Warning - Retired attribute - (0x0032,0x1001) TM Scheduled Study Start Time 
Warning - Retired attribute - (0x0032,0x1050) DA Study Completion Date 
Warning - Retired attribute - (0x0032,0x1051) TM Study Completion Time 
Warning - Dicom dataset contains retired attributes
MRImage
Error - Missing attribute Type 1 Required Element=&lt;FileMetaInformationGroupLength&gt; Module=&lt;FileMetaInformation&gt;
Warning - is only permitted to be empty when actually unknown; should be absent (not empty) if an unpaired body part, and have a value if a paired body part - attribute &lt;Laterality&gt;
Error - Missing attribute Type 1 Required Element=&lt;FrameOfReferenceUID&gt; Module=&lt;FrameOfReference&gt;
Warning - Unrecognized defined term &lt;FAST_GEMS&gt; for value 1 of attribute &lt;Scan Options&gt;
Error - Attribute present when condition unsatisfied (which may not be present otherwise) Type 2C Conditional Element=&lt;InversionTime&gt; Module=&lt;MRImage&gt;
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x0040) US Data Set Type 
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x0041) LO Data Set Subtype 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x9056) SH Stack ID 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x9057) UL In-Stack Position Number 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1000) DA Scheduled Study Start Date 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1001) TM Scheduled Study Start Time 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1032) PN Requesting Physician 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1050) DA Study Completion Date 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1051) TM Study Completion Time 
Warning - Attribute is not present in standard DICOM IOD - (0x0040,0x0242) SH Performed Station Name 
Warning - Attribute is not present in standard DICOM IOD - (0x0040,0x0243) SH Performed Location 
Warning - Dicom dataset contains attributes not present in standard DICOM IOD - this is a Standard Extended SOP Class
</code></pre>

---

## Post #5 by @dougPorter (2021-07-13 21:35 UTC)

<p>OK, I’ll get some more recent images. QREADS and RDICOM apps may be more tolerable of invalid DICOM elements. I’ll let you know.</p>

---

## Post #6 by @dougPorter (2021-07-13 22:47 UTC)

<p>Darn it! Still there for image done today</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d4c52cab0fd62c4858abc3f42692a5f1d73cc31.png" alt="image" data-base62-sha1="8KgEaicSdpCBTmk4BImlNe14tIB" width="206" height="406"></p>
<p>What in the header do you think might be causing the problem?</p>
<p>Thanks</p>

---

## Post #7 by @pieper (2021-07-14 00:18 UTC)

<p>Hmm, that’s bad.  Can you describe what vendor and processing pathway that is?  We’ve worked with tons of PET data over the year with no issues like that.</p>
<p>Can you try running the tool I linked above (<a href="http://dclunie.com/dicom3tools/dciodvfy.html" class="inline-onebox">DICOM Validator - dciodvfy</a>) and see if you get the same errors with the new data?</p>

---

## Post #8 by @lassoan (2021-07-14 00:43 UTC)

<p>The problem is that <code>PixelRepresentation</code> is set to 1, which means that the value is signed.</p>
<p>Could you check the source code of QREADS how it decides to read the voxel value as signed or unsigned short? For example, I saw another viewer checked the minimum pixel value tag and it set the value to unsigned if was &gt;=0. It looked like an ugly workaround but if this is applied in many viewers then we may consider doing this, too.</p>
<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> what would you recommend?</p>

---

## Post #9 by @issakomi (2021-07-14 14:17 UTC)

<p>I also think there is an issue with <em>bits stored</em> and <em>pixel representation</em>. Look, in PET series - <em>bits stored</em> are 15, <em>pixel representation</em> 1 (signed) and values up to 32767, it is wrong, either <em>bits stored</em> should be 16 or <em>pixel representation</em> 0 (unsigned). Signed is valid for <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_8.2.html#table_8.2.1-2" rel="noopener nofollow ugc">JPEG Lossless Transfer Syntaxes</a>, but here is probably not required, no negative values, there were several bugs with processing of signed JPEG compressed data (actually in Slicer - no problem), so safer to avoid, if not required, IMHO.<br>
In MR series <em>bits stored</em> vary from frame to frame 5-12 and <em>pixel representation</em> is also signed, i didn’t check values, but probably there is the same error.</p>

---

## Post #10 by @issakomi (2021-07-14 14:51 UTC)

<p>I have tried to modify <em>bits stored/high bit</em> values (16/15) and left pixel representation signed, the data is not modified, of course, only above attributes. Seems that Slicer can load series.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/10CTVTcY403xpMnne6sNVZ5sHn1wSDgte/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/10CTVTcY403xpMnne6sNVZ5sHn1wSDgte/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/10CTVTcY403xpMnne6sNVZ5sHn1wSDgte/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/10CTVTcY403xpMnne6sNVZ5sHn1wSDgte/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">TestImages_corrected.tar.gz</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @pieper (2021-07-14 14:53 UTC)

<p>Thanks for checking <a class="mention" href="/u/issakomi">@issakomi</a> - if this is a common enough pattern we could consider adding it to the DICOMPatcher.  I’m still curious how these are being created as it would be better to fix at the source rather than in Slicer.</p>

---

## Post #12 by @dougPorter (2021-07-14 15:21 UTC)

<p>OK, so for instance, in the following case…</p>
<pre><code class="lang-auto">0028,0100]     BitsAllocated  16 `
[0028,0101]    BitsStored     15 
[0028,0102]    HighBit 14 
[0028,0103]    PixelRepresentation    1 
[0028,0106]    SmallestImagePixelValue        0     
[0028,0107]    LargestImagePixelValue 32766
[0028,1050]    WindowCenter   8438.388323078 
[0028,1051]    WindowWidth    16876.776646156
[0028,1052]    RescaleIntercept       0  
[0028,1053]    RescaleSlope   0.453101
</code></pre>
<pre><code>I won't allow my module to run if this condition is present...
</code></pre>
<pre><code class="lang-auto">       if ( BitsStored &lt; 16 or HighBit &lt; 15 or PixelRepresentation &gt; 0) 
          Then Do Not Display
</code></pre>
<p>Also, what if the RescaleSlope were 1.0? Would that make a difference?</p>
<p>Also, does the DICOM standard indicate that the PixelRepresentation applies only to the pixel values before applying the RescaleSlope? I know the W/L is post.</p>
<p>Thanks</p>

---

## Post #13 by @dougPorter (2021-07-14 15:52 UTC)

<aside class="quote no-group" data-username="dougPorter" data-post="1" data-topic="18704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dougporter/48/10927_2.png" class="avatar"> dougPorter:</div>
<blockquote>
<p>link has been removed until it is confirmed that the images do not contain PHI)</p>
</blockquote>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/0nsybbzmahsm5lt/AADKMcS7ZR1vUtzvJYIxsTPwa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/0nsybbzmahsm5lt/AADKMcS7ZR1vUtzvJYIxsTPwa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-folder-dropbox-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/sh/0nsybbzmahsm5lt/AADKMcS7ZR1vUtzvJYIxsTPwa?dl=0" target="_blank" rel="noopener nofollow ugc">TestImages</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>These images have been cleared for PHI. They can be made public. Thanks.</p>

---

## Post #15 by @dougPorter (2021-07-14 18:28 UTC)

<aside class="quote no-group quote-post-not-found" data-username="issakomi" data-post="14" data-topic="18704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>Maybe correct the buggy files by setting <em>Pixel Representation</em> to 0 (if possible) or adjust <em>Bits Stored</em> (in particular case highly likely bits stored == bits allocated will not harm, i guess, high bit is always = bits stored - 1) or both. Ideally the bug will be fixed where it happens.</p>
</blockquote>
</aside>
<p>That might be possible to do as we create the DICOM files for the module but may cause too long of a delay in launching the module. We’ll consider that.</p>
<aside class="quote no-group quote-post-not-found" data-username="issakomi" data-post="14" data-topic="18704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<blockquote>
<p>does the DICOM standard indicate that the PixelRepresentation applies only to the pixel values before applying the RescaleSlope?</p>
</blockquote>
<p>Yes, before.</p>
</blockquote>
</aside>
<p>I wonder if the correct way to think about this is …</p>
<pre><code> if (SmallestImagePixelValue &gt; 0 and PixelRepresentation  = 1)  then bad DICOM.
</code></pre>
<p>They seem contradictory. What do you think?</p>
<p>Thanks</p>

---

## Post #16 by @dougPorter (2021-07-14 19:47 UTC)

<p>Interesting: Here is the display from Slicer version 4.5.0-1 running on a Mac:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02866265f8ec4dd8abe1d762f8554d78ccc95103.jpeg" data-download-href="/uploads/short-url/mkS4rd1snuNEpmJuR9YGDm6jVp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02866265f8ec4dd8abe1d762f8554d78ccc95103_2_666x500.jpeg" alt="image" data-base62-sha1="mkS4rd1snuNEpmJuR9YGDm6jVp" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02866265f8ec4dd8abe1d762f8554d78ccc95103_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02866265f8ec4dd8abe1d762f8554d78ccc95103_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02866265f8ec4dd8abe1d762f8554d78ccc95103.jpeg 2x" data-dominant-color="ADAEBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1044×783 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So, at some point Slicer displayed it. Probably assumed high bit = 15 and Bits Stored 16.</p>

---

## Post #17 by @dougPorter (2021-07-14 19:57 UTC)

<p>With the help of someone more knowledgeable than I about our images, I learned that the corresponding images in long term storage are correct. This was changed at some point in the process of compression and decompression only for the purpose of displaying in our host app that creates DCMs and launches the Slicer module. I think I understand now what’s happening and I’ll keep you posted on my solution.</p>
<p>Thanks you so much!</p>

---

## Post #18 by @lassoan (2021-07-15 19:23 UTC)

<p>I’ve checked the images and the problem is not with zeroing. The file stores values between 0-32767, which can be represented on 15 bits if unsigned. Disabling unused bit zeroing will not fix the issue, the numbers will be still negative.</p>
<p>Only the PixelRepresentation value is incorrect. If I edit the DICOM file to set the pixel representation to 0 then the image appears correctly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/354fedd6d2cc0d5c0c40dcad5dd839c35e6b5229.png" data-download-href="/uploads/short-url/7BCyijVDQQhLm07x5fDW0Uei77b.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/354fedd6d2cc0d5c0c40dcad5dd839c35e6b5229.png" alt="image" data-base62-sha1="7BCyijVDQQhLm07x5fDW0Uei77b" width="636" height="500" data-dominant-color="171313"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">773×607 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/dougporter">@dougPorter</a> there are two things you could do to help moving forward:</p>
<ol>
<li>
<p>Ask on the ITK forum what could have changed in ITK between current version and about 2 years ago that changes the appearance of these images.</p>
</li>
<li>
<p>Check in your QREADS software how it decides to interpret voxel values as signed/unsigned.</p>
</li>
</ol>

---

## Post #20 by @dougPorter (2021-07-16 18:21 UTC)

<p>We will find a way to fix this on our end.</p>
<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="18704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Only the PixelRepresentation value is incorrect. If I edit the DICOM file to set the pixel representation to 0 then the image appears correctly</p>
</blockquote>
</aside>
<p>Is there a way to change header elements in the Python script prior to displaying so that the change can take effect? Just curious. Not proposing as a solution, but just a general dev question.</p>
<p>Thanks</p>

---

## Post #21 by @pieper (2021-07-16 18:25 UTC)

<p>Yes, have a look at the DICOMPatcher module which does that kind of operation.</p>

---
