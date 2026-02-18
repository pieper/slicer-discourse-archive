# Segmentation problem with MRI (geometric issues)

**Topic ID**: 15899
**Date**: 2021-02-08
**URL**: https://discourse.slicer.org/t/segmentation-problem-with-mri-geometric-issues/15899

---

## Post #1 by @hao (2021-02-08 11:28 UTC)

<p>Hi, I tried to do segmentation with MRI serie, at import moment, slice give a message of "Geometric issue, images are not equally spaced). I have used transform option of dicom plugin configuartion. But each time I paint with “draw”, there are always the parasite image in the nexte slice.<br>
Can anyone help me?<br>
thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22b1b1290f43ff9ca2483440d2765bcc835f98b0.jpeg" data-download-href="/uploads/short-url/4WUW7rmlRfLOuA1Zmgb5yjF9fva.jpeg?dl=1" title="slicer_contourage_01.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22b1b1290f43ff9ca2483440d2765bcc835f98b0_2_545x499.jpeg" alt="slicer_contourage_01.PNG" data-base62-sha1="4WUW7rmlRfLOuA1Zmgb5yjF9fva" width="545" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22b1b1290f43ff9ca2483440d2765bcc835f98b0_2_545x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22b1b1290f43ff9ca2483440d2765bcc835f98b0_2_817x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22b1b1290f43ff9ca2483440d2765bcc835f98b0.jpeg 2x" data-dominant-color="44444A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_contourage_01.PNG</span><span class="informations">1075×985 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e2b06fdde59676f6d3b0f68eb2fe7032a1283e.jpeg" data-download-href="/uploads/short-url/lXkJpd0qWWD7FtNqurTQcEFlFIa.jpeg?dl=1" title="slicer_contourage_02.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99e2b06fdde59676f6d3b0f68eb2fe7032a1283e_2_549x500.jpeg" alt="slicer_contourage_02.PNG" data-base62-sha1="lXkJpd0qWWD7FtNqurTQcEFlFIa" width="549" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99e2b06fdde59676f6d3b0f68eb2fe7032a1283e_2_549x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99e2b06fdde59676f6d3b0f68eb2fe7032a1283e_2_823x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e2b06fdde59676f6d3b0f68eb2fe7032a1283e.jpeg 2x" data-dominant-color="45454B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_contourage_02.PNG</span><span class="informations">1085×987 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-02-08 15:46 UTC)

<aside class="quote no-group" data-username="hao" data-post="1" data-topic="15899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ea5d25/48.png" class="avatar"> hao:</div>
<blockquote>
<p>transform option of dicom plugin configuartion</p>
</blockquote>
</aside>
<p>This creates a nonlinear transform to correct the scan geometry, so you probably need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden this</a> before you do the segmentation.</p>

---

## Post #3 by @lassoan (2021-02-08 19:41 UTC)

<p>In addition to that, it may be possible that the volume axes are not aligned with default slice axes. You may just need to click the warning icon next to the segmentation node selector. See more information <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">here</a>.</p>

---

## Post #4 by @hao (2021-02-09 16:05 UTC)

<p>thank you lassoan and steve pieper,<br>
I think my problem is mainly due of the non-aligned volume axe. it is resolved by click the botton beside the segmentation as indicated by the article.<br>
I have succefully transform all of the segmentation of 2nd CT scan after an important changement morphologique. it’s really fantastique and amazing. I think that we can use 3D slicer for routine traitement.<br>
before registation, 1er scan vs 2er scan, the segmentations are based on 1er scan<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd.png" data-download-href="/uploads/short-url/5mdOGEYSXYtidOAJ5P2mCSXerH7.png?dl=1" title="Screenshot from 2021-02-09 15-45-05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_690x373.png" alt="Screenshot from 2021-02-09 15-45-05" data-base62-sha1="5mdOGEYSXYtidOAJ5P2mCSXerH7" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258df625d82e57e51193605d1968f52d74862cdd_2_1380x746.png 2x" data-dominant-color="616363"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 15-45-05</span><span class="informations">1876×1015 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
two scans without segmentations<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f65e3e1510cdbcdc771ad70bc5e98360904ebaa.jpeg" data-download-href="/uploads/short-url/mK6dq3qmDlAb65NPDzlwmx2KD46.jpeg?dl=1" title="Screenshot from 2021-02-09 15-46-44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f65e3e1510cdbcdc771ad70bc5e98360904ebaa_2_690x488.jpeg" alt="Screenshot from 2021-02-09 15-46-44" data-base62-sha1="mK6dq3qmDlAb65NPDzlwmx2KD46" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f65e3e1510cdbcdc771ad70bc5e98360904ebaa_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f65e3e1510cdbcdc771ad70bc5e98360904ebaa_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f65e3e1510cdbcdc771ad70bc5e98360904ebaa.jpeg 2x" data-dominant-color="2D2D2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 15-46-44</span><span class="informations">1377×975 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After rigid segmentation (General registration brain)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0007049304c52c1d8a973985fb6a1a3a5863da79.jpeg" data-download-href="/uploads/short-url/f2dhxlheNKTvTCgdmnkaxw5FD.jpeg?dl=1" title="Screenshot from 2021-02-09 15-54-10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0007049304c52c1d8a973985fb6a1a3a5863da79_2_690x498.jpeg" alt="Screenshot from 2021-02-09 15-54-10" data-base62-sha1="f2dhxlheNKTvTCgdmnkaxw5FD" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0007049304c52c1d8a973985fb6a1a3a5863da79_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0007049304c52c1d8a973985fb6a1a3a5863da79_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0007049304c52c1d8a973985fb6a1a3a5863da79.jpeg 2x" data-dominant-color="313132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 15-54-10</span><span class="informations">1318×952 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After Bspine segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0818018b6c352fd7a595d869126f46bacdb45bfd.jpeg" data-download-href="/uploads/short-url/19BfEqK9Py9fPjCyc3lGNZfDWnH.jpeg?dl=1" title="Screenshot from 2021-02-09 16-06-09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818018b6c352fd7a595d869126f46bacdb45bfd_2_690x485.jpeg" alt="Screenshot from 2021-02-09 16-06-09" data-base62-sha1="19BfEqK9Py9fPjCyc3lGNZfDWnH" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818018b6c352fd7a595d869126f46bacdb45bfd_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818018b6c352fd7a595d869126f46bacdb45bfd_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0818018b6c352fd7a595d869126f46bacdb45bfd.jpeg 2x" data-dominant-color="222123"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 16-06-09</span><span class="informations">1328×934 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the segmentation before application of transform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/576d25cba0b81251024912f3dafddbb54bb04226.jpeg" data-download-href="/uploads/short-url/ctpo2bBDJv45iLewUUYp9jLlppc.jpeg?dl=1" title="Screenshot from 2021-02-09 16-08-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/576d25cba0b81251024912f3dafddbb54bb04226_2_686x499.jpeg" alt="Screenshot from 2021-02-09 16-08-21" data-base62-sha1="ctpo2bBDJv45iLewUUYp9jLlppc" width="686" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/576d25cba0b81251024912f3dafddbb54bb04226_2_686x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/576d25cba0b81251024912f3dafddbb54bb04226_2_1029x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/576d25cba0b81251024912f3dafddbb54bb04226.jpeg 2x" data-dominant-color="343832"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 16-08-21</span><span class="informations">1300×947 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the final position and transformation of the segmentations<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95ca2324d56372da580e47c82d00ccd7ab374a3d.jpeg" data-download-href="/uploads/short-url/ln6dExsOqcTAq8qI5gu4GNfurH7.jpeg?dl=1" title="Screenshot from 2021-02-09 16-11-32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ca2324d56372da580e47c82d00ccd7ab374a3d_2_690x490.jpeg" alt="Screenshot from 2021-02-09 16-11-32" data-base62-sha1="ln6dExsOqcTAq8qI5gu4GNfurH7" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ca2324d56372da580e47c82d00ccd7ab374a3d_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95ca2324d56372da580e47c82d00ccd7ab374a3d_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95ca2324d56372da580e47c82d00ccd7ab374a3d.jpeg 2x" data-dominant-color="2F332D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-02-09 16-11-32</span><span class="informations">1321×940 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-02-09 16:40 UTC)

<p>This looks awesome, thanks for sharing!</p>
<p>It would be nice if you could post a few sentences (and maybe 1-2 nice images) in a new topic in <a href="https://discourse.slicer.org/c/community/success-stories/29">“Success stories”</a> category describing who you are and how 3D Slicer and the community helped you to achieve what you needed. It would help us securing more grant funding to further improve Slicer. Thank you!</p>
<aside class="onebox category-onebox" style="box-shadow: -5px 0px #92278F;">
  <article class="onebox-body category-onebox-body">
    <h3>
      <a class="badge-wrapper bullet" href="/c/community/success-stories/29">
          <span class="badge-category-bg" style="background-color: #92278F"></span>
        <span class="clear-badge"><span>Success stories</span></span>
      </a>
    </h3>
      <div>
        <span class="description">
          <p>This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos.</p>
        </span>
      </div>
  </article>
  <div class="clearfix"></div>
</aside>


---

## Post #6 by @hao (2021-02-09 17:42 UTC)

<p>OK, i will do it as soon as possible.<br>
thank you</p>

---
