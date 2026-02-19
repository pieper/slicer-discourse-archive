---
topic_id: 817
title: "How To Adjust The Distorted Image"
date: 2017-08-03
url: https://discourse.slicer.org/t/817
---

# How to adjust the distorted image?

**Topic ID**: 817
**Date**: 2017-08-03
**URL**: https://discourse.slicer.org/t/how-to-adjust-the-distorted-image/817

---

## Post #1 by @doc-xie (2017-08-03 17:15 UTC)

<p>Hi!<br>
After the data was loaded into 3D Slicer,the axinal and coronal view display normally,but the saggital view was distored.<br>
I cannot understand the reason about this problem,furthermore,whether it is possible the problem happened to axinal or<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7f5851babf6a95f9a0725a870a89da51ae691d2.jpeg" data-download-href="/uploads/short-url/swV2wqrWqrcwz1E1taerRv6FE54.jpg?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c7f5851babf6a95f9a0725a870a89da51ae691d2_2_690x249.jpg" alt="无标题" data-base62-sha1="swV2wqrWqrcwz1E1taerRv6FE54" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c7f5851babf6a95f9a0725a870a89da51ae691d2_2_690x249.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c7f5851babf6a95f9a0725a870a89da51ae691d2_2_1035x373.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7f5851babf6a95f9a0725a870a89da51ae691d2.jpeg 2x" data-dominant-color="333331"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">1365×493 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> coronal view and how to adjust the distorted image?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2017-08-03 17:29 UTC)

<p>Was the volume acquired with tilted gantry?</p>

---

## Post #3 by @doc-xie (2017-08-04 02:55 UTC)

<p>Sorry, I don’t know.The data of DICOM format was acquired through PACS (Picture archiving and communication system) and I have never met this problem before. So I consult with image doctor of our hospital, he have no idea about this too. The 3D Slicer is so powerful, so I think this problem could be solved with “reform” or “transform” module, but the result is failed.</p>

---

## Post #4 by @lassoan (2017-08-04 03:50 UTC)

<p>We should be able to address this in Slicer, but we need some more information.</p>
<p>Install the latest nightly version of Slicer and follow these steps to collect the necessary information:</p>
<ol>
<li>Open the DICOM popup</li>
<li>Select the CT image</li>
<li>Click <code>Metadata</code> button</li>
<li>Enter <code>tilt</code> in the search box</li>
<li>Click <code>Copy metadata</code> button</li>
<li>Paste the gantry tilt value in your response message here</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa60689d5a7c429f8b4c28823fc3bf6dd03967e.png" data-download-href="/uploads/short-url/olCSrfvFrZ2X6bkn0gDuDjhDDQi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa60689d5a7c429f8b4c28823fc3bf6dd03967e_2_647x500.png" alt="image" data-base62-sha1="olCSrfvFrZ2X6bkn0gDuDjhDDQi" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa60689d5a7c429f8b4c28823fc3bf6dd03967e_2_647x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa60689d5a7c429f8b4c28823fc3bf6dd03967e_2_970x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa60689d5a7c429f8b4c28823fc3bf6dd03967e_2_1294x1000.png 2x" data-dominant-color="D8D8DC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2361×1823 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @doc-xie (2017-08-05 01:23 UTC)

<p>The value of gantry tilt is 20.9,what should i do next?</p>

---

## Post #6 by @lassoan (2017-08-05 02:05 UTC)

<p>We are working on a solution, probably will be ready in 1-2 weeks. You can monitor the status here: <a href="https://issues.slicer.org/view.php?id=4409">https://issues.slicer.org/view.php?id=4409</a></p>
<p>If you need a solution now then you can use a DICOM converter that supports gantry-tilted images, for example <a href="https://github.com/dgobbi/vtk-dicom/wiki/dicomtonifti">dicomtonifti</a>. Download from here: <a href="https://github.com/dgobbi/vtk-dicom/releases">https://github.com/dgobbi/vtk-dicom/releases</a></p>

---

## Post #7 by @doc-xie (2017-08-05 14:32 UTC)

<p>Thank you very very much,professor lassoan!</p>

---

## Post #8 by @pieper (2017-10-12 20:09 UTC)

<p>I implemented a fix that should work for the gantry tilt data, but I don’t have a sharable dataset for testing.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/812" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/812" target="_blank">Cannot run newly installed Slicer 3</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:27" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:27" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I’ll try to acquire images of a phantom but if anyone has data they can share that would save the trouble.</p>
<p>For the record on discussion with colleagues we determined that a good phantom dataset for testing would include:</p>
<ul>
<li>a phantom with clearly marked up/down/left/right/front/back</li>
<li>data acquired prone and supine</li>
<li>slices acquired head first and foot first</li>
<li>data acquired with gantry tilt</li>
<li>data acquired with skips and/or variable table speed</li>
<li>use of different reconstructions (e.g. spiral data at 3mm and the same data at 5mm)</li>
<li>saved raw data for later reconstruction as needed</li>
</ul>
<p>If I’m able to time on a scanner and help from a tech I’ll try to acquire these and make them public on midas.</p>

---

## Post #9 by @doc-xie (2017-10-17 12:34 UTC)

<p>Hello Steve,I have the distorted image in dicom format.But how can I share the data with you?</p>

---

## Post #10 by @pieper (2017-10-17 13:41 UTC)

<p>Hi doc-xie -</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> was able to share some sample data with me for testing so after a few tweaks yesterday the new code linked above appears to be working.  It will be good for you to test it too with your data once we get it into a build of the application, which should be available in a day or two.</p>
<p>Best,<br>
Steve</p>

---

## Post #11 by @doc-xie (2017-10-17 14:28 UTC)

<p>Thanks Steve!<br>
I will be keeping eyes on your achievements all the time,the problem has confused me for a long time.<br>
Good luck!<br>
doc-xie!</p>

---

## Post #12 by @pieper (2017-10-17 15:59 UTC)

<p>Thanks for the encouragement!  <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:">  Yes, I’ve been wanting to fix gantry tilted volume handling in Slicer for a long time too.</p>
<p>Since the the code is still new and relatively untested, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a> and I decided not to include it in the 4.8 release but will put it in the Nightly build after the release builds are made.</p>
<p>Best,<br>
Steve</p>

---

## Post #13 by @pieper (2017-10-20 21:40 UTC)

<p>The pull request was merged today so it should show up in Nightly builds tomorrow.  Would be good to know if it works for your data <a class="mention" href="/u/doc-xie">@doc-xie</a>.  Have a great weekend <img src="https://emoji.discourse-cdn.com/twitter/sunny.png?v=5" title=":sunny:" class="emoji" alt=":sunny:"></p>

---

## Post #14 by @doc-xie (2017-10-22 14:31 UTC)

<p>Good job!Thanks you very much,Steve!<br>
Would you like tell the the details about the steps?In other words,what should I do after I setup the new Nightly builds or is there any extentions should be downloaded?<br>
Best wishes!<br>
doc-xie</p>

---

## Post #15 by @pieper (2017-10-22 23:34 UTC)

<p>Hi doc-xie -</p>
<p>No special steps should be required, just importing into the DICOM module and then if there’s a gantry tilt detected the loaded volume will be put inside of a grid transform that straightens it out.  Of course I’ve only tried this with a few datasets so let us know how it goes for you.</p>
<p>Best,<br>
Steve</p>

---

## Post #16 by @doc-xie (2017-10-23 14:00 UTC)

<p>Ok!Steve:smile:<br>
Another question,if the data is in .nii format,how to adjust the distorted image?<br>
Thanks!</p>

---

## Post #17 by @pieper (2017-10-23 14:19 UTC)

<p>Ah, sorry, the solution I implemented only work with DICOM because that’s where the original image geometry information is available.  I’m not sure there is a good solution for nii files unless you know the gantry tilt angle and can manually construct a shear matrix to correct it.</p>
<p>-Steve</p>

---

## Post #18 by @doc-xie (2017-10-23 14:23 UTC)

<p>Thanks for your quick answer!<br>
But where can I find the gantry tilt in the menu?Is it in the Metadata,and I shoul search it with word"tilt" ?<br>
Best,<br>
doc-xie!</p>

---

## Post #19 by @doc-xie (2017-10-23 14:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95291887cc3988728f3d888b3929b1acd501917b.png" data-download-href="/uploads/short-url/lhxbOf1VrbWBjGJqyUcLVYwdJ7Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95291887cc3988728f3d888b3929b1acd501917b_2_690x387.png" alt="image" data-base62-sha1="lhxbOf1VrbWBjGJqyUcLVYwdJ7Z" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95291887cc3988728f3d888b3929b1acd501917b_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95291887cc3988728f3d888b3929b1acd501917b_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95291887cc3988728f3d888b3929b1acd501917b.png 2x" data-dominant-color="F4F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The value of the gantry tilt has not been shown in the interface!</p>

---

## Post #20 by @doc-xie (2017-10-23 14:27 UTC)

<p>This is the original image of the volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13d97186b0c9829c44dc72504728ee742c92361d.png" data-download-href="/uploads/short-url/2PAWqBLUwrlEsgGSNvLVpK8VPU9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13d97186b0c9829c44dc72504728ee742c92361d_2_690x387.png" alt="image" data-base62-sha1="2PAWqBLUwrlEsgGSNvLVpK8VPU9" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13d97186b0c9829c44dc72504728ee742c92361d_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13d97186b0c9829c44dc72504728ee742c92361d_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13d97186b0c9829c44dc72504728ee742c92361d.png 2x" data-dominant-color="ACAEBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @lassoan (2017-10-23 14:50 UTC)

<p>For nii files I think you should just resample the image, for example using Crop volume module.</p>

---

## Post #22 by @pieper (2017-10-23 17:35 UTC)

<p>Hi doc-xie -</p>
<p>If you have the original dicom, you can look for the Gantry Tilt header (0018,1120) but it’s not a required tag so your data may not have it [1].  If you know the tilt you can make linear transform to correct the shear.  If you don’t know the tilt exactly you could probably estimate visually, maybe by looking at the table.  Do you know how do this?  If not we can give instructions.</p>
<p>The solution I added to the DICOM module looks at the image positions at each slice, which are required by the standard, and creates a nonlinear transform that fixes the tilt and also handles a few other situations like missing slices.  But it really only works on the original DICOM objects, not on data that’s been converted to nifti.</p>
<p>Best,<br>
Steve</p>
<p>[1] <a href="http://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.8.2">http://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.8.2</a></p>

---

## Post #23 by @lassoan (2017-10-23 19:02 UTC)

<p><a class="mention" href="/u/doc-xie">@doc-xie</a> Do you have a nifti file that has shear in its image header?</p>

---

## Post #24 by @doc-xie (2017-10-24 01:17 UTC)

<p>Thanks a lot,Professor Steve!<br>
I am so sorry,after I transform the .nii file to original format,the data have not the Gantry Tilt and I do not know how to recognize it.<br>
Would you like give me the instructions?<br>
Otherwise,the link you give me can not be opened correctly.<br>
Best,<br>
Doc-xie</p>

---

## Post #25 by @doc-xie (2017-10-24 01:20 UTC)

<p>Yes,Professor Lassoan!<br>
My distored images have not be adjusted correctly,so the problem confused me for a long time.<br>
I can send the data to you if need,<br>
Thanks!<br>
Doc-xie</p>

---

## Post #26 by @lassoan (2017-10-24 01:23 UTC)

<p>If you have old data that you imported earlier versions of Slicer or other software that cannot handle gantry tilt then there is not much you can do. Probably you have to discard the nii files and go back and reimport them from DICOM and probably resample the volume if you need the volume on a rectilinear grid.</p>

---

## Post #27 by @doc-xie (2017-10-24 03:54 UTC)

<p>Thanks a lot,Professor Lassoan!<br>
After I import the original data,the value of the Gantry Tilt is 20.9. So what we know from this is the data transformed from .nii file can not be used again,especially to be adjusted for disformation. About the Gantry Tilt,what should I do in the next?<br>
Best wishes!<br>
Doc-xie</p>

---

## Post #28 by @lassoan (2017-10-24 13:06 UTC)

<p>The Gantry Tilt angle DICOM tag is for display purposes only. Accurate slice positions are defined by the slice position and axis directions DICOM tags. You may be able to compute an approximate transformation matrix from the Gantry Tilt tag, but it won’t be completely accurate (angle is rounded to one decimal, so you may get up to a few pixel error) and you may need some experimentation to get the rotation axis and direction right. Therefore, I would recommend to re-import the images from DICOM with a recent nightly version of Slicer (that computes the accurate image acquisition transformation matrix).</p>

---

## Post #29 by @doc-xie (2017-10-24 13:37 UTC)

<p>Thanks you very much!<br>
The version of 3D Slicer I used is new Nightly(2017-10-22),need I download some extensions for this transformation?<br>
If I finish adjustment with Transform module,which value should to be corrected?<br>
Would you like show me the specific steps because I am a new learner?<img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"><img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"><br>
Best,<br>
doc-xie</p>

---

## Post #30 by @pieper (2017-10-24 17:21 UTC)

<p>Hi doc-xie -</p>
<p>The gantry tilt is a shear transform along the scan axis, which can be described with an off-diagonal entry in an otherwise identity linear transform.  I just tried this on the case Andras shared with me, so it should work for your case too.  I confirmed that at least visually this gives identical results to the DICOM-based approach (using the image position and orientation tags) that is in the current Nightly builds.</p>
<p>The basic steps are:</p>
<ol>
<li>calculate the sine of the tilt angle.  In my case, tag 0018,1120 was -8.5, so in the python console I typed:</li>
</ol>
<pre><code class="lang-auto">import math
math.sin(math.radians(-8.5))
</code></pre>
<p>which gave the answer -0.14780941112961063</p>
<ol start="2">
<li>
<p>In the transforms module I created a linear transform and applied it to the CT</p>
</li>
<li>
<p>in the second row of the third column I changed the number from 0 to -.15</p>
</li>
</ol>
<p>And it looks good.</p>
<p>The rationale for this from a linear algebra point of view is that the second row third column controls how the Anterior coordinate changes as a function of the Superior direction.  Here it’s saying that for each mm increment anteriorly, the image data should be shifted back by .15 mm.</p>
<p>Visually, here is the volume without the transform:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fc75fd76b781a7eab8f6c4df63c4768f72a5ca7.jpeg" data-download-href="/uploads/short-url/4x7Xtg77Ssc8lKOZmyztzY9Vbgj.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1fc75fd76b781a7eab8f6c4df63c4768f72a5ca7_2_690x478.jpg" alt="image" data-base62-sha1="4x7Xtg77Ssc8lKOZmyztzY9Vbgj" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1fc75fd76b781a7eab8f6c4df63c4768f72a5ca7_2_690x478.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1fc75fd76b781a7eab8f6c4df63c4768f72a5ca7_2_1035x717.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1fc75fd76b781a7eab8f6c4df63c4768f72a5ca7_2_1380x956.jpg 2x" data-dominant-color="A6A6AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1654×1148 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here it is with the transform:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84a11fcfd5144755bab38fe4e4a5dc0e71488c69.png" data-download-href="/uploads/short-url/iViesAOvYZIjnQOHTvzSDK4YIKR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84a11fcfd5144755bab38fe4e4a5dc0e71488c69_2_690x475.png" alt="image" data-base62-sha1="iViesAOvYZIjnQOHTvzSDK4YIKR" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84a11fcfd5144755bab38fe4e4a5dc0e71488c69_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84a11fcfd5144755bab38fe4e4a5dc0e71488c69_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84a11fcfd5144755bab38fe4e4a5dc0e71488c69_2_1380x950.png 2x" data-dominant-color="A5A5AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1663×1145 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And for reference here is the same data loaded in the Nightly build where the transform came from the DICOM directly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/084c9b20cf20181d435586000b06468d811dd7a6.jpeg" data-download-href="/uploads/short-url/1bpWJpauGkIj3KE3Smu0KtT9FNs.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/084c9b20cf20181d435586000b06468d811dd7a6_2_690x454.jpg" alt="image" data-base62-sha1="1bpWJpauGkIj3KE3Smu0KtT9FNs" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/084c9b20cf20181d435586000b06468d811dd7a6_2_690x454.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/084c9b20cf20181d435586000b06468d811dd7a6_2_1035x681.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/084c9b20cf20181d435586000b06468d811dd7a6_2_1380x908.jpg 2x" data-dominant-color="A7A7AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1700×1119 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Let me know if this doesn’t work for you - we want to get all these coordinate mappings correct!</p>
<p>Best,<br>
Steve</p>

---

## Post #31 by @pieper (2017-10-24 17:37 UTC)

<p>Follow up: comparing closely between the gantry tilt shear matrix method described above and the dicom image position/orientation method from the nightly I still see some residual differences (possibly the kinds of errors Andras mentioined).  I’m pretty sure the dicom method in the Nightly is correct but be very careful making any measurements on gantry tilted data.</p>

---

## Post #32 by @doc-xie (2017-10-26 07:26 UTC)

<p>Thank you for your detailed introduction,I will try it.<br>
Best wishes!<br>
Doc-xie!</p>

---

## Post #33 by @doc-xie (2017-10-28 14:02 UTC)

<p>The problem has been solved successfully with your advice!<br>
Thanks a lot!<br>
Have a good weekend!<br>
Doc-die.</p>

---

## Post #34 by @doc-xie (2017-11-08 02:40 UTC)

<p>Hello,Steve!<br>
A very intresting problem about the transform module.<br>
When I check a normal brain CT scan(Fig 1),<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f27b3b00f4373da3b07620191bef98f121af2875.jpeg" data-download-href="/uploads/short-url/yB5zdamxlElD6kepx6GSC5hmrQN.jpg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f27b3b00f4373da3b07620191bef98f121af2875_2_690x492.jpg" alt="1" data-base62-sha1="yB5zdamxlElD6kepx6GSC5hmrQN" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f27b3b00f4373da3b07620191bef98f121af2875_2_690x492.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f27b3b00f4373da3b07620191bef98f121af2875_2_1035x738.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f27b3b00f4373da3b07620191bef98f121af2875_2_1380x984.jpg 2x" data-dominant-color="A4A3B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1576×1125 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
the gantry tilt is 24.6(Fig 2)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23eb065b53c8c62a7267803bfd2ca2ec05984cb1.jpeg" data-download-href="/uploads/short-url/57KfuoNUNaiqq2I0fq2vls9dXKV.jpg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23eb065b53c8c62a7267803bfd2ca2ec05984cb1_2_680x500.jpg" alt="2" data-base62-sha1="57KfuoNUNaiqq2I0fq2vls9dXKV" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23eb065b53c8c62a7267803bfd2ca2ec05984cb1_2_680x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23eb065b53c8c62a7267803bfd2ca2ec05984cb1_2_1020x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23eb065b53c8c62a7267803bfd2ca2ec05984cb1_2_1360x1000.jpg 2x" data-dominant-color="C5C6C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1576×1158 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>,<br>
so after i changed the Transform Matrix,the coronal view displayed unnormally and the 3D view distored obviously(Fig 3).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/318567e03a49ff149646d9ed2f26bddeb7ddc639.jpeg" data-download-href="/uploads/short-url/745dqyrEW25ObFD3eZr3KvTiDzz.jpg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/318567e03a49ff149646d9ed2f26bddeb7ddc639_2_681x500.jpg" alt="3" data-base62-sha1="745dqyrEW25ObFD3eZr3KvTiDzz" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/318567e03a49ff149646d9ed2f26bddeb7ddc639_2_681x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/318567e03a49ff149646d9ed2f26bddeb7ddc639_2_1021x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/318567e03a49ff149646d9ed2f26bddeb7ddc639_2_1362x1000.jpg 2x" data-dominant-color="A2A3B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1579×1158 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
What is the reason about this and whether the Value of the GantryDetectorTilt is right?<br>
Best wished!<br>
Doc-xie</p>

---

## Post #35 by @lassoan (2017-11-08 14:52 UTC)

<p>As we explained before, GantryDetectionTilt field indicates that the image was acquired with gantry tilt, but it is not to be used for determining the image geometry. For example, it may be possible that the CT scanner saves the image as a Cartesian volume. The image transformation mechanism that is available in recent nightly versions does not use GantryDetectionTilt field and should handle all cases correctly regardless the volume is saved as a sheared or a Cartesian volume.</p>

---

## Post #36 by @doc-xie (2017-11-09 03:21 UTC)

<p>Thaks,Professor Lassoan.<br>
But how to estimate the deformation degree of the volume and how to adjust the distorted image in recent nightly version  correctly?<br>
Doc-xie</p>

---

## Post #37 by @pieper (2017-11-09 11:56 UTC)

<p>Hi Doc-xie -</p>
<p>Did you try importing and loading the dicom files through the dicom module?  This should automatically create the nonlinear transform based on the per-slice geometry.  It would be good know if this works for your data - it is a much simpler process.</p>
<p>Best,<br>
Steve</p>

---

## Post #38 by @doc-xie (2017-11-10 08:03 UTC)

<p>Thanks a lot!<br>
What I want to know is whether I should check every Gantry tilt of every volume in order to estimate the deformation degreee,or the value of the Gantry tilt can be shown automatically?Another question,does the value of the Gantry tilt should be adjusted for the reconstruction correctly?<br>
Best wishes!<br>
Doc xie</p>

---

## Post #39 by @laura_rodriguez (2017-11-10 10:04 UTC)

<p>Hi everyone,</p>
<p>I am pretty new working with 3D slicer, but I use to work with Mimics (I was using it since 2005), so please be patient…</p>
<p>I have a lot of distorsion with my dicom data, I can see perfectly well in axial view but the image is complete distorted in sagittal and coronal view, it is like some kind of unit problem. But I do not know how to fix it. There is no tilt in effect. They seem to be very wide… I was having a look to the dicom parameters but they look ok to me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d3eb96cde37f82ed16e41e0bca906af0a75c257.jpeg" data-download-href="/uploads/short-url/8JNvJQId4UZbgjPTvOf6MkXfQwf.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3d3eb96cde37f82ed16e41e0bca906af0a75c257_2_687x500.jpg" alt="image" data-base62-sha1="8JNvJQId4UZbgjPTvOf6MkXfQwf" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3d3eb96cde37f82ed16e41e0bca906af0a75c257_2_687x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3d3eb96cde37f82ed16e41e0bca906af0a75c257_2_1030x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3d3eb96cde37f82ed16e41e0bca906af0a75c257_2_1374x1000.jpg 2x" data-dominant-color="292932"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1428×1039 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I hope you can help me</p>
<p>These are the DICOM image parameters</p>
<p>Study Date: 20100801<br>
Acquisition Date: 20100801<br>
Image Date: 20100801<br>
Study Time: 103821<br>
Acquisition Time: 104048<br>
Image Time: 104050.398998<br>
Accession Number: 0006050<br>
Modality: CT<br>
Manufacturer: Philips<br>
Institution Name: APHP.Pitie PrGRENIER<br>
Institution Address: PARIS 13<br>
Refering Physician’s Name: DR HUYNH<br>
Station Name: HOST-200029<br>
Study Description: <br>
Series Description: OS<br>
Institutional Dept. Name: RADIOLOGIE<br>
Manufacturer’s Model Name: iCT 128<br>
Patient Name: MEMBRE SUP^ANCIEN<br>
Patient Date of Birth: 20000101<br>
Patient Sex: O<br>
Scan Options: HELIX<br>
Slice Thickness: 1.00<br>
KVP: 140<br>
Spacing Between Slices: 0.5<br>
Data Collection Diameter: 500<br>
Software Version: 3.0.1<br>
Protocol Name: EPAULE/Orthoped<br>
Reconstruction Diameter: 269<br>
Gantry/Detector Tilt: 0<br>
Table Height: 51.000000<br>
Rotation Direction: CW<br>
X-ray Tube Current: 99<br>
Exposure: 351<br>
Filter Type: F<br>
Convolution Kernel: F<br>
Patient Position: HFS<br>
Study Instance UID: 1.2.840.113704.1.111.3252.1280651812.6<br>
Series Instance UID: 1.2.276.0.45.45.2.51.3.23084206062387.20131211.112340001<br>
Study ID: 7185<br>
Series Number: 2<br>
Image Number: 0<br>
Image Position Patient: -100.174\111.531\214.8<br>
Image Orientation Patient: 1\0\0\0\1\0<br>
Frame of Reference UID: 1.2.840.113704.1.111.3040.1280651919.3<br>
Slice Location: 5.80<br>
Photometric Interpretation: MONOCHROME2<br>
Pixel Spacing: 0.35026\0.35026<br>
Window Center: 00600\00600<br>
Window Width: 02000\02000</p>
<p>It should have to be something like this other image I am sending to you. Can you see the difference? Bone are thinner</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6bfe91d9f404ac3a497f1e333ea1d287531a57.jpeg" data-download-href="/uploads/short-url/xrN6vNQxUDGHmneTOUSBlvZiZhB.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ea6bfe91d9f404ac3a497f1e333ea1d287531a57_2_341x499.jpg" alt="image" data-base62-sha1="xrN6vNQxUDGHmneTOUSBlvZiZhB" width="341" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ea6bfe91d9f404ac3a497f1e333ea1d287531a57_2_341x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ea6bfe91d9f404ac3a497f1e333ea1d287531a57_2_511x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6bfe91d9f404ac3a497f1e333ea1d287531a57.jpeg 2x" data-dominant-color="343417"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">647×947 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I can fix this “little” things and I would like to teach my students who to work with 3dslicer.</p>

---

## Post #40 by @doc-xie (2017-11-10 13:14 UTC)

<p>Hello!<br>
The problem is the same with me.The value of the Gantry/Detector Tilt is 0,but the image is distorted,    what is the reason about this?    How to estimate the deformation degree?<br>
If we want to adjust the distorted image,which value can be referenced to?<br>
Best wishes!<br>
Doc-xie</p>

---

## Post #41 by @pieper (2017-11-11 18:01 UTC)

<p><a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> is is possible you could share these files for debugging?  Or if you want to debug yourself, you could try loading the data into the DICOM database and then going into advanced mode and looking at the metadata.  As you scroll through the slices you can look at the ImagePositionPatient and see how it is changing and compare this to the slice spacing shown for the loaded volume in the Volumes module.  You could also change the spacing to find out what value matches the Mimics view.  Also you could check the error logs for any diagnostic information.</p>

---

## Post #42 by @pieper (2017-11-11 18:03 UTC)

<p><a class="mention" href="/u/doc-xie">@doc-xie</a> importing through the DICOM module in the current nightly should autocorrect the gantry tilt if the files are like the examples I have here (the ones I posted earlier in this thread).  If neither that nor the manual shear technique are working on other data then I’m not sure what else to suggest…</p>

---

## Post #43 by @lassoan (2017-11-11 19:24 UTC)

<p>You can  now also filter for tags and copy value of all frames at once. It would help us a lot if you could copy-paste here value of <code>Image Position Patient</code> tag for all frames.</p>

---

## Post #44 by @laura_rodriguez (2017-11-13 15:46 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> it looks to be everything ok in medata about the patient position…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b69e9085aeae242546f3db201f0e7c6dfab943a7.png" data-download-href="/uploads/short-url/q3wCBcBRH7gQ1aC08K2kaq8eQDl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b69e9085aeae242546f3db201f0e7c6dfab943a7_2_690x441.png" alt="image" data-base62-sha1="q3wCBcBRH7gQ1aC08K2kaq8eQDl" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b69e9085aeae242546f3db201f0e7c6dfab943a7_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b69e9085aeae242546f3db201f0e7c6dfab943a7_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b69e9085aeae242546f3db201f0e7c6dfab943a7.png 2x" data-dominant-color="EFEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1102×705 80 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See this one too</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0b5ea2553a02ec068efdf0d14dba55f60dc24c6.png" data-download-href="/uploads/short-url/w3SHCXbBIWxB5SyakulJZinY1b8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b5ea2553a02ec068efdf0d14dba55f60dc24c6_2_690x431.png" alt="image" data-base62-sha1="w3SHCXbBIWxB5SyakulJZinY1b8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b5ea2553a02ec068efdf0d14dba55f60dc24c6_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b5ea2553a02ec068efdf0d14dba55f60dc24c6_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0b5ea2553a02ec068efdf0d14dba55f60dc24c6.png 2x" data-dominant-color="EEEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1121×701 94.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You are saying that I can change the paramaters, can you explain me how?</p>

---

## Post #45 by @lassoan (2017-11-13 15:54 UTC)

<p>You can view/adjust voxel size in <code>Volumes</code> module: <code>Volume information</code> section, <code>Image Spacing</code> values.</p>

---

## Post #46 by @lassoan (2017-11-13 15:56 UTC)

<p><a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> Could you please enter <code>ImagePositionPatient</code> into the <code>Search...</code> box, click <code>Copy all files metadata</code> button (it copies all ImagePositionPatient values to the clipboard), and paste the clipboard content here? We could then double-check that all position values are correct.</p>

---

## Post #47 by @laura_rodriguez (2017-11-13 17:24 UTC)

<p>It does not me allow to send you the complete file because i have to many files…</p>
<p>Can I send you in another way? Thank you</p>
<p>L</p>

---

## Post #48 by @lassoan (2017-11-13 17:32 UTC)

<p>If you follow my instructions above (enter filter criteria in search box and click copy all files metadata), field values are copied to the clipboard. Then, you can just paste the clipboard content here. There are no files involved.</p>

---

## Post #49 by @laura_rodriguez (2017-11-13 17:50 UTC)

<p>Neither, this is what the app is telling me:</p>
<p>Body is limited to 36500 characters; you entered 81668.</p>

---

## Post #50 by @lassoan (2017-11-13 17:52 UTC)

<p>I see, the info is too long. Then please copy into notepad or word, save the file to dropbox (or onedrive, or google drive) and paste here the link to the file. Thanks!</p>

---

## Post #51 by @laura_rodriguez (2017-11-13 17:57 UTC)

<p><a href="https://drive.google.com/open?id=1UKJOAO7wYRQ27sQIBuT1oUBALbRB9E0x" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1UKJOAO7wYRQ27sQIBuT1oUBALbRB9E0x</a></p>

---

## Post #52 by @lassoan (2017-11-13 18:14 UTC)

<p>Thank you. The file shows that distance between all neighbor slices are 0.5mm. What are the 3 Image Spacing values in Volumes module / Volume information section?</p>

---

## Post #53 by @laura_rodriguez (2017-11-13 18:50 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2b6c8c84c9a2f7a621314a15e533d3c2b7f0776.png" data-download-href="/uploads/short-url/yD9a0uDpCf0J73YqX0T9vcT1Z1s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2b6c8c84c9a2f7a621314a15e533d3c2b7f0776.png" alt="image" data-base62-sha1="yD9a0uDpCf0J73YqX0T9vcT1Z1s" width="399" height="500" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">551×690 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #54 by @lassoan (2017-11-13 19:04 UTC)

<p>Correct values would be 0.35026, 0.35026, 0.5.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Do you know what could cause seeing 1,1,1 spacing, while the slice position seems to be correct and pixel spacing tag is present?</p>
<p><a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> Could you share the DICOM files and post the link here? (make sure data is anonymized, if belongs to patients)</p>

---

## Post #55 by @pieper (2017-11-13 19:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> no, I’n not sure why that would be happening but I would like to figure it out.  The slice thickness is set to be 1mm, but the spacing is clearly 0.5mm.</p>
<p><a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> it really would help to have a look at the data.  If you can’t share it publicly with a link on the forum perhaps you could share it privately with me and <a class="mention" href="/u/lassoan">@lassoan</a>.  Also do you know if this data was processed in any way or did it come straight from a scanner?</p>

---

## Post #56 by @doc-xie (2017-11-14 07:51 UTC)

<p>Hello,Professor Lassoan!<br>
How can you get the values(0.35026,0.35026,0.5) basing the Image Spacing(1mm,1mm,1mm) and what should do in the next in order to correct the images?<br>
Thanks a lot!<br>
Doc-xie</p>

---

## Post #57 by @lassoan (2017-11-14 15:43 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="56" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>How can you get the values(0.35026,0.35026,0.5)</p>
</blockquote>
</aside>
<p>0.35026, 0.35026 values come from Pixel Spacing tag (I could see it in the screenshots).</p>
<p>0.5 is computed from values in Image Position Patient tags (slice position difference between neighbor slices).</p>

---

## Post #58 by @lassoan (2017-11-14 15:44 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="56" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>what should do in the next in order to correct the images?</p>
</blockquote>
</aside>
<p>If you can share the data set then we can make sure that Slicer loads it correctly.</p>

---

## Post #59 by @laura_rodriguez (2017-11-14 16:22 UTC)

<p>Ok, it is working now, Changing the values, thank you very much for this. I will continue “playing with the software”</p>
<p>I cannot share the data with you through here, because they are highly confidential. sorry. I do not have problems in sharing a partial part. if that can work to you</p>

---

## Post #60 by @lassoan (2017-11-14 16:37 UTC)

<p>Getting 3-5 neighbor slices would probably be enough (you can choose frames that are almost empty, as for the testing we only need the DICOM tags).</p>

---

## Post #61 by @laura_rodriguez (2017-11-14 16:46 UTC)

<p>Here you have, thank you</p>
<p><a href="https://drive.google.com/open?id=1GiTakTBuGFdb-joN_IesZxVAQMM9NiW-" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1GiTakTBuGFdb-joN_IesZxVAQMM9NiW-</a></p>

---

## Post #62 by @pieper (2017-11-14 17:34 UTC)

<p>Thank you <a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a>, this is helpful.</p>
<p>The underlying issue appears to be that GDCM does not recognize the private class UID and issues a warning:</p>
<pre><code class="lang-auto">Warning: In /Users/pieper/slicer4/latest/Slicer-superbuild/ITKv4/Modules/ThirdParty/GDCM/src/gdcm/Source/DataStructureAndEncodingDefinition/gdcmFileMetaInformation.cxx, line 874, function gdcm::MediaStorage gdcm::FileMetaInformation::GetMediaStorage() const
Media Storage Class UID: 1.2.276.0.7230010.3.1.0.1
</code></pre>
<p>Searching for that class UID leads to this issue: <a href="https://sourceforge.net/p/gdcm/feature-requests/15/">https://sourceforge.net/p/gdcm/feature-requests/15/</a></p>
<p>Which indicates this data was somehow manipulated and re-saved using DCMTK.</p>
<p>So as a workaround for this data <a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> you can go to the Slicer’s Edit menu and pick application settings and then in the  DICOM page set “DICOM reader approach” to be DCMTK.  I just confirmed that this loads with the correct spacings.</p>
<p>As another option I loaded with a recent version of Slicer (post 4.8) that includes the “Acquisition Transform” feature (the one described above to correct gantry tilt) using GDCM it loads with spacing 1,1,1 but the transform reassuringly actually gives the exact same image, which is a good confirmation of that approach.</p>
<p>Getting back to the original issue, the current default mode is “GDCM with DCMTK fallback” which is meant to handle the case where GDCM fails to load at all, e.g. by throwing an exception.  Here it just prints a warning and then incorrectly loads.  It seems to me that ignoring the image spacing should be a GDCM failure and not just a warning.</p>

---

## Post #63 by @laura_rodriguez (2017-11-14 17:57 UTC)

<p>Thank you, I will try all that and tell you</p>

---

## Post #64 by @pieper (2017-11-14 18:06 UTC)

<p>Looking at this a bit more, it’s clear that these are pretty non-standard files.</p>
<p>Running <span class="mention">@dclunie</span>’s verifier points out that the file is internally inconsistent.</p>
<pre><code class="lang-auto">$ dciodvfy /tmp/3dslicer\ test/Ferrassie\ 1-MbsSup.0135.dcm
...
Error - Media Storage SOP Class UID different from SOP Class UID
...
</code></pre>
<p>The media class is the DCMTK private class while the image SOP class is Secondary Capture.  Because of this GDCM looks for spacing in tag 0x0018,0x2010 while the file actually has it in 0x0028,0x0030.</p>
<p>I guess the best for you <a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> might be to look into the history of these files and see if any of the DICOM information can be relied on.  If not maybe save them in a less ambiguous way, either as fixed DICOM or maybe in nrrd or similar format.</p>
<p>For the record some of the related GDCM code is linked below.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmPixmapReader.cxx#L72-L170" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmPixmapReader.cxx#L72-L170" target="_blank" rel="nofollow noopener">Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmPixmapReader.cxx#L72-L170</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="72" style="counter-reset: li-counter 71 ;">
<li>bool res = false;</li>
<li>/* Does it really make sense to check for Media Storage SOP Class UID?</li>
<li> * I need then to check consistency with 0008 0016 Instance SOP Class UID</li>
<li> * ... I don't think there is an end.</li>
<li> * I'd rather go the old way check a bunch of tags (From Image Plane</li>
<li> * Module).</li>
<li> */</li>
<li>MediaStorage ms = header.GetMediaStorage();</li>
<li>bool isImage = MediaStorage::IsImage( ms );</li>
<li>if( isImage )</li>
<li>  {</li>
<li>  // I cannot leave this here, since ELSCINT1 / LOSSLESS RICE declares CT Image Storage,</li>
<li>  // when in fact this is a private Media Storage (no Pixel Data element)</li>
<li>  //assert( ds.FindDataElement( Tag(0x7fe0,0x0010 ) ) );</li>
<li>  assert( ts != TransferSyntax::TS_END &amp;&amp; ms != MediaStorage::MS_END );</li>
<li>  // Good it's the easy case. It's declared as an Image:</li>
<li>  //PixelData-&gt;SetCompressionFromTransferSyntax( ts );</li>
<li>  res = ReadImage(ms);</li>
<li>  }</li>
<li>//else if( ms == MediaStorage::MRSpectroscopyStorage )</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmPixmapReader.cxx#L72-L170" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1219" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1219" target="_blank" rel="nofollow noopener">Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1219</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1209" style="counter-reset: li-counter 1208 ;">
<li>    // -&gt; (0018,1063) DS [76.000000]                              #  10, 1 FrameTime</li>
<li>
</li>
<li>    gdcmWarningMacro( "No spacing value found" );</li>
<li>    sp.push_back( 1.0 );</li>
<li>    sp.push_back( 1.0 );</li>
<li>    sp.push_back( 1.0 );</li>
<li>    return sp;</li>
<li>    }</li>
<li>  }</li>
<li>
</li>
<li class="selected">Tag spacingtag = GetSpacingTagFromMediaStorage(ms);</li>
<li>if( spacingtag != Tag(0xffff,0xffff) &amp;&amp; ds.FindDataElement( spacingtag ) &amp;&amp; !ds.GetDataElement( spacingtag ).IsEmpty() )</li>
<li>  {</li>
<li>  const DataElement&amp; de = ds.GetDataElement( spacingtag );</li>
<li>  const Global &amp;g = GlobalInstance;</li>
<li>  const Dicts &amp;dicts = g.GetDicts();</li>
<li>  const DictEntry &amp;entry = dicts.GetDictEntry(de.GetTag());</li>
<li>  const VR &amp; vr = entry.GetVR();</li>
<li>  assert( vr.Compatible( de.GetVR() ) );</li>
<li>  switch(vr)</li>
<li>    {</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1048-L1056" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1048-L1056" target="_blank" rel="nofollow noopener">Slicer/ITK/blob/slicer-v4.12.0-2017-05-09-2d63918/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1048-L1056</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1048" style="counter-reset: li-counter 1047 ;">
<li>case MediaStorage::SecondaryCaptureImageStorage:</li>
<li>case MediaStorage::MultiframeSingleBitSecondaryCaptureImageStorage:</li>
<li>case MediaStorage::MultiframeGrayscaleByteSecondaryCaptureImageStorage:</li>
<li>case MediaStorage::MultiframeGrayscaleWordSecondaryCaptureImageStorage:</li>
<li>case MediaStorage::MultiframeTrueColorSecondaryCaptureImageStorage:</li>
<li>  // See PS 3.3-2008. Table C.8-25 SC IMAGE MODULE ATTRIBUTES</li>
<li>  // and Table C.8-25b SC MULTI-FRAME IMAGE MODULE ATTRIBUTES</li>
<li>  t = Tag(0x0018,0x2010);</li>
<li>  break;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #65 by @lassoan (2017-11-14 19:56 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Should we add dclunie’s verifier to Slicer? We could launch it from DICOM patcher or the DICOM importer or browser.</p>
<p><a class="mention" href="/u/laura_rodriguez">@laura_rodriguez</a> Let us know if you figure out what’s the origin of these files. If they are produced by a commercial software then we may add a rule to our DICOM patcher module to fix it up.</p>

---

## Post #66 by @pieper (2017-11-14 20:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="65" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> Should we add dclunie’s verifier to Slicer? We could launch it from DICOM patcher or the DICOM importer or browser.</p>
</blockquote>
</aside>
<p>That’s an interesting idea - here’s the info on the tool <a href="http://www.dclunie.com/dicom3tools/dciodvfy.html" class="inline-onebox">DICOM Validator - dciodvfy</a></p>
<p>It’s part of David’s older C++ toolkit but all his newer work is in Java (but I don’t think he has anything comparable to dciodvfy in that and we wouldn’t want a Java dependency).  But I do like the idea of giving users more options for how to work with troublesome data since it happens fairly often.</p>

---

## Post #67 by @fedorov (2017-11-14 22:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="65" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> Should we add dclunie’s verifier to Slicer? We could launch it from DICOM patcher or the DICOM importer or browser.</p>
</blockquote>
</aside>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="66" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>That’s an interesting idea - here’s the info on the tool <a href="http://www.dclunie.com/dicom3tools/dciodvfy.html" class="inline-onebox">DICOM Validator - dciodvfy</a></p>
</blockquote>
</aside>
<p>This would be great!</p>
<p>I don’t think there is a replacement in the Java tools for dciodvfy.</p>
<p>Note that dicom3tools is not cmake-fied, it relies on ‘nmake’. Another challenge is that by intent the project is not a “two-way open source”. David makes the source code available for everyone’s use, but whatever changes you do to the source code (e.g., cmake-fy it), will not be integrated into David’s master, so the process will require a lot of maintenance.</p>
<p>A practical workaround could be to use dciodvfy from a docker container (we already have a precedent for docker prerequisite in an extension).</p>

---

## Post #68 by @pieper (2017-11-14 23:39 UTC)

<p>I like the idea of dciodvfy in a docker as a debugging utility.  But installing docker is still a bit of a hurdle.</p>

---

## Post #69 by @fedorov (2017-11-15 21:48 UTC)

<aside class="quote no-group" data-username="pieper" data-post="68" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But installing docker is still a bit of a hurdle.</p>
</blockquote>
</aside>
<p>Agreed!</p>
<p>I remember being criticized when I made a similar comment in the past! <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #70 by @laura_rodriguez (2017-11-17 08:13 UTC)

<p>Sorry for the delay in the my answer, but I had to lecture these two days.</p>
<p>I think they were modified by avizo:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a0d28caecc2e88f5a6e68a17d5d50794a3f382.png" alt="image" data-base62-sha1="uc9j1jGRkmrgvyRt7dzMWUrnfwe" width="669" height="345"></p>
<p>Thank you</p>
<p>L</p>

---

## Post #71 by @doc-xie (2017-12-15 03:37 UTC)

<p>Hello,Steve!<br>
A new problem with the distorted image. After I load the DICOM data into the software,the image was distorted even if with the software of 4.9 version,and the value of the Gantrytilt can not be found in the metadata.<br>
I cannot find the reason and solve the problem.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65cba93281e340faf7c8d6b847df50f06091a985.jpeg" data-download-href="/uploads/short-url/ewwz5QVg8Aj4ibfcFYn0zmTlEpf.jpg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65cba93281e340faf7c8d6b847df50f06091a985_2_690x480.jpg" alt="1" data-base62-sha1="ewwz5QVg8Aj4ibfcFYn0zmTlEpf" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65cba93281e340faf7c8d6b847df50f06091a985_2_690x480.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65cba93281e340faf7c8d6b847df50f06091a985_2_1035x720.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65cba93281e340faf7c8d6b847df50f06091a985_2_1380x960.jpg 2x" data-dominant-color="A4A3B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1581×1100 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/267495c8dee1b8bf6c582c97f814b7b1797a4c88.jpeg" data-download-href="/uploads/short-url/5ubVqFLHJQz7pkKPJc5WJA1kCMw.jpg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/267495c8dee1b8bf6c582c97f814b7b1797a4c88_2_682x500.jpg" alt="2" data-base62-sha1="5ubVqFLHJQz7pkKPJc5WJA1kCMw" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/267495c8dee1b8bf6c582c97f814b7b1797a4c88_2_682x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/267495c8dee1b8bf6c582c97f814b7b1797a4c88_2_1023x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/267495c8dee1b8bf6c582c97f814b7b1797a4c88_2_1364x1000.jpg 2x" data-dominant-color="F8F8F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1573×1153 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best wishes!<br>
doc-xie</p>

---

## Post #72 by @lassoan (2017-12-16 20:33 UTC)

<p>Please try with today’s nightly build. If does not work with default settings, check “Advanced” checkbox and try each loadable.</p>
<p>If none of these are enough then run it through DICOM Patcher module, import it again (if you don’t generate new IDs then you have to delete the previously imported items from the DICOM browser), and see if you can load it (with default or advanced settings).</p>
<p>If none of these work, then use the original CT, that was not manipulated by Avizo, or try an updated version of Avizo - hopefully they have figured out they exported invalid DICOM files and fixed their problem. If you can process a non-confidential data set the same way then we can create an error report from that that you can send to Avizo.</p>

---

## Post #73 by @doc-xie (2017-12-21 08:54 UTC)

<p>Thanks very much, Professor Lassoan!<br>
The distorted images were adjusted normally after loaded the DICOM files into the newly version 3D Slicer.But as for the data I used before(Aug 4),the images have not any changes,should I correct it with the value of the GantryTilt like before?<br>
Best wishes!<br>
doc-xie</p>

---

## Post #74 by @lassoan (2017-12-21 13:56 UTC)

<p>I would recommend to use the latest version of Slicer (and re-process any data that you processed with earlier version of Slicer). Don’t use GantryTilt value - it is for informational purposes only, not for processing your volumes. If you need to process the volumes then I would suggest to resample them on a rectilinear grid using Crop Volume module.</p>

---

## Post #75 by @doc-xie (2018-02-08 16:05 UTC)

<p>Hello,professor Lassoan!<br>
Another distorted image need to be corrected!<br>
The results of the volume rendering did not accord with the yellow slice<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7caf761d5f5bfe810875ebbdc1c109e09c2d7871.jpeg" data-download-href="/uploads/short-url/hN1866AtSNJXc1RKYV8AN8TE0sV.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7caf761d5f5bfe810875ebbdc1c109e09c2d7871_2_450x500.jpeg" alt="Screenshot" data-base62-sha1="hN1866AtSNJXc1RKYV8AN8TE0sV" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7caf761d5f5bfe810875ebbdc1c109e09c2d7871_2_450x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7caf761d5f5bfe810875ebbdc1c109e09c2d7871_2_675x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7caf761d5f5bfe810875ebbdc1c109e09c2d7871_2_900x1000.jpeg 2x" data-dominant-color="A4A6A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">942×1045 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
Even if I reconstructed the skull with Editor module,the results was the same as before<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d93aa60c2962b1099ec1a10ec5a93faae5b9a7.jpeg" data-download-href="/uploads/short-url/76YO32SpAaLOk1e5HFItszXHkfZ.jpeg?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31d93aa60c2962b1099ec1a10ec5a93faae5b9a7_2_684x500.jpeg" alt="Screenshot_3" data-base62-sha1="76YO32SpAaLOk1e5HFItszXHkfZ" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31d93aa60c2962b1099ec1a10ec5a93faae5b9a7_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d93aa60c2962b1099ec1a10ec5a93faae5b9a7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d93aa60c2962b1099ec1a10ec5a93faae5b9a7.jpeg 2x" data-dominant-color="787E7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">942×688 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
So,how to evaluate the tilt degree of this volume and correct the imaging!<br>
Have a goog weekend!<br>
Doc-xie.</p>

---

## Post #77 by @lassoan (2019-06-10 13:45 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="75" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>The results of the volume rendering did not accord with the yellow slice</p>
</blockquote>
</aside>
<p>Volume rendering cannot apply non-linear transforms on-the-fly. You need to harden the non-linear transform in order to take it into account for volume rendering.</p>

---

## Post #78 by @Sharada (2021-09-06 16:10 UTC)

<p>Hi Steve,</p>
<p>I have been trying to understand the gantry tilt problem too. Thank you for this detailed explanation here, but according to my understanding, the shear correction should be applied in the z-direction and is the tangent of the shear. <a href="https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pone.0110408/1/pone.0110408.s003.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&amp;X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210906%2Fauto%2Fstorage%2Fgoog4_request&amp;X-Goog-Date=20210906T160656Z&amp;X-Goog-Expires=86400&amp;X-Goog-SignedHeaders=host&amp;X-Goog-Signature=42648e085803114fc87484fd14576913cc0f598eb618703dae52a5d51602c714cdf9804ec1dc4f11c563fcd0cadd0d0b5e8f52a66b076f984280a8716cbc1d26c08ee641ef00c61d812e3fa81041c4908c1751480799671597e4be529c94ac8da9d8e8bce3a1795c53ff517ea0681200b1abe439d8f8131c97575bef385e3e77d1fa7c32a9ae8ca67be27f88d8a996909cee6680df26b8edd8ae3562d6932bfe14bd8ffad0ac9c1647b9d240f065ed4b57aacc73fe5f7df93103528dd6ed0fc68dc8770e3ab562d7464af01840e3c2de66dc015033f279fa709049c67394fbd6aed2c857465d899d3377fe79c0bf33e951d4e2679825a50e926f4afd2d675ee7" rel="noopener nofollow ugc">This supplement</a> describes it better.</p>
<p>I understand that the idea is to move the superior coordinate as a function of the anterior coordinate, but I am not able to consolidate the transform you specify to what the article describes. Could you please comment on this?</p>
<p>Thank you,<br>
Sharada</p>

---

## Post #79 by @pieper (2021-09-07 17:32 UTC)

<p>I’m afraid the link you provided has expired - maybe you can repost?</p>
<p>In any event yes, you could represent gantry tilt as a shear transform, with a non-zero element in the off-diagonal of a linear transform as described in some of the earlier posts in this thread.</p>
<p>But it’s easier and more general to enable the geometry correction in the DICOM page of the Application Settings (<a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">described here</a>).</p>

---

## Post #80 by @Sharada (2021-09-07 17:54 UTC)

<p>Hi Steve,<br>
Thank you for your response. I made some progress.</p>
<p>The link has expired for some reason, but here’s a screenshot from it:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158b4f6e19725751bc43a55def4812c2e9033103.png" data-download-href="/uploads/short-url/34AuRpbB6UgB7jzfD7201nlAfGb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/158b4f6e19725751bc43a55def4812c2e9033103_2_690x312.png" alt="image" data-base62-sha1="34AuRpbB6UgB7jzfD7201nlAfGb" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/158b4f6e19725751bc43a55def4812c2e9033103_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/158b4f6e19725751bc43a55def4812c2e9033103_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/158b4f6e19725751bc43a55def4812c2e9033103_2_1380x624.png 2x" data-dominant-color="F3F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1411×639 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I see that in an earlier explanation you had sin(gantry_tilt) in T(2,3) instead of the transformation described here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c58f49790bb00b6cbcd121379245d999526332d.png" data-download-href="/uploads/short-url/hK1N8iE8SbsrS3dKZ3F9Vh6i8aN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c58f49790bb00b6cbcd121379245d999526332d_2_627x500.png" alt="image" data-base62-sha1="hK1N8iE8SbsrS3dKZ3F9Vh6i8aN" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c58f49790bb00b6cbcd121379245d999526332d_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c58f49790bb00b6cbcd121379245d999526332d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c58f49790bb00b6cbcd121379245d999526332d.png 2x" data-dominant-color="E6E5E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">756×602 58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure how/why it is different from the one described in the screenshot. Can you please explain?</p>
<p>I also had a similar question - when obliquely acquired sagittal images are loaded, Slicer visualizes the geometry correctly. But is there a way to re-slice the volume such that the geometry is the normal sagittal orientation? ([[0,0-1],[1,0,0],[0,-1,0]]). Please let me know!</p>
<p>Best,<br>
Sharada</p>

---

## Post #81 by @pieper (2021-09-07 20:48 UTC)

<aside class="quote no-group" data-username="Sharada" data-post="80" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>I am not sure how/why it is different from the one described in the screenshot. Can you please explain?</p>
</blockquote>
</aside>
<p>I’d suggestion going with the <code>s*tan(alpha)</code> formula if that’s been published and validated.  My post was just an experiment that looked correct but didn’t take slice spacing into account and maybe it just looked close.</p>
<p>But as I pointed out, we use a different method in Slicer that handles both gantry tilt and variable slice spacing since both are very common.  I’m pretty confident in this nonlinear transform approach so I’d suggest that rather than trying to work out the matrix.</p>
<aside class="quote no-group" data-username="Sharada" data-post="80" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>I also had a similar question - when obliquely acquired sagittal images are loaded, Slicer visualizes the geometry correctly. But is there a way to re-slice the volume such that the geometry is the normal sagittal orientation? ([[0,0-1],[1,0,0],[0,-1,0]]). Please let me know!</p>
</blockquote>
</aside>
<p>Yes, Slicer takes into account the acquisition orientation (see <a href="https://www.slicer.org/wiki/Coordinate_systems">here for more details</a>).  You can always resample to a different grid if you want, for example with the Resample Scalar/Vector/DWI Volume module, but it’s usually better to leave them in the native space to avoid lossy resampling.</p>

---

## Post #82 by @Sharada (2021-09-07 22:01 UTC)

<p>Thank you, that makes sense. The reason I am having to resample is I need to make anatomical measurements on the mid-sagittal plane. And with oblique sagittal images, the true MSP (perfectly aligned to the patient coordinates) spans over multiple slices. This makes my annotation task hard. That’s why I figured resampling to [[0,0,-1],[1,0,0],[0,-1,0]] might work and I can make my annotations on one slice. Just wondering - are there any methods I could use in Slicer to help with this?</p>

---

## Post #83 by @pieper (2021-09-07 22:04 UTC)

<p>Maybe the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html">ACPC module</a> would work for your purposes.</p>

---

## Post #84 by @Sharada (2021-09-07 22:20 UTC)

<p>Thank you, that will definitely help. The only issue is that I am working with CT images and as the soft resolution is not very great, marking the AC and PC is going to be a challenge. I will try it out nevertheless.</p>
<p>Best,<br>
Sharada</p>

---

## Post #85 by @lassoan (2021-09-08 02:58 UTC)

<p>The AC-PC line is optional. You can just place points on the mid-sagittal plane and the ACPC module will compute the transform that you need.</p>

---

## Post #86 by @Sharada (2021-09-08 16:33 UTC)

<p>Hi Andras,</p>
<p>Thank you for that tip. I did my best at locating AC and PC with the axial volume, and also tried only with the midline points like you suggested. The results match pretty closely, but there are a few differences (Gray is With AC-PC, Cyan is without it). The computed transforms are also slightly different, but I believe it is not a matter of concern for the accuracy of further image processing. What do you think?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd99d553e2782584dfc48c3cc9ce3327bae3a46f.jpeg" data-download-href="/uploads/short-url/r3hPlQxfpwr8ZIbs1ESFNkccZR5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd99d553e2782584dfc48c3cc9ce3327bae3a46f_2_652x500.jpeg" alt="image" data-base62-sha1="r3hPlQxfpwr8ZIbs1ESFNkccZR5" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd99d553e2782584dfc48c3cc9ce3327bae3a46f_2_652x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd99d553e2782584dfc48c3cc9ce3327bae3a46f_2_978x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd99d553e2782584dfc48c3cc9ce3327bae3a46f.jpeg 2x" data-dominant-color="4B6975"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1093×837 65.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also have a follow-up:<br>
With a sagittal volume, the AC PC is better identifiable. I computed the transform using the AC-PC module for alignment and applied it to the Axial volume instead. Both these volumes were acquired for the same study. With this, the alignment seems off, especially in the coronal view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d29b2997a431f5b3d9b4b04060a60d8dfa5d89b.jpeg" data-download-href="/uploads/short-url/b0C6kei5oA7jbRLu7PTX4FtNrzd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d29b2997a431f5b3d9b4b04060a60d8dfa5d89b_2_609x500.jpeg" alt="image" data-base62-sha1="b0C6kei5oA7jbRLu7PTX4FtNrzd" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d29b2997a431f5b3d9b4b04060a60d8dfa5d89b_2_609x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d29b2997a431f5b3d9b4b04060a60d8dfa5d89b_2_913x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d29b2997a431f5b3d9b4b04060a60d8dfa5d89b.jpeg 2x" data-dominant-color="656C72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">955×784 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I suspect it is because Slicer is not taking into account the Sagittal acquisition transform which is:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb85cb10aa25e85234eafd10c35f3c09cc0c226c.png" alt="image" data-base62-sha1="xBwR5hJC670vsQdkS20nROG6QDW" width="650" height="136"></p>
<p>This volume is obviously an oblique acquisition. I might be wrong with my theory but please let me know if you have any insight here.</p>
<p>Thanks again for all your help and advice with this!</p>
<p>-Sharada</p>

---

## Post #87 by @lassoan (2021-09-08 17:02 UTC)

<p>If you only specify AC-PC line then the volume is rotated so that the line will be in an axial plane. However, you still need to drop points on the mid-sagittal plane if you want to fix rotation around the AP axis.</p>

---

## Post #88 by @Sharada (2021-09-08 17:47 UTC)

<p>I see, that makes perfect sense. Sorry if I worded my questions unclearly before, but I wanted to know:</p>
<ol>
<li>If there’s a difference between just specifying the midline (5 points) versus midline + AC PC line. Visually, there is not much difference - as seen in my earlier screenshot. The computed transforms are different, but very close.</li>
<li>When I load an oblique sagittal image, I don’t see an acquisition transform created. Does Slicer automatically account for this like it handles gantry tilt?</li>
</ol>
<p>Thanks,<br>
Sharada</p>

---

## Post #89 by @lassoan (2021-09-08 18:05 UTC)

<aside class="quote no-group" data-username="Sharada" data-post="88" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>If there’s a difference between just specifying the midline (5 points) versus midline + AC PC line. Visually, there is not much difference - as seen in my earlier screenshot. The computed transforms are different, but very close.</p>
</blockquote>
</aside>
<p>AC-PC line is only used for rotating the volume so that the AC-PC line becomes “horizontal” (in an axial plane).</p>
<aside class="quote no-group" data-username="Sharada" data-post="88" data-topic="817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>When I load an oblique sagittal image, I don’t see an acquisition transform created. Does Slicer automatically account for this like it handles gantry tilt?</p>
</blockquote>
</aside>
<p>An oblique image can be represented in a volume node. Acquisition transform is only created if the image geometry is not a simple rectilinear grid with orthogonal axes (such as a volume acquired with tilted gantry or with non-uniform space between slices).</p>

---
