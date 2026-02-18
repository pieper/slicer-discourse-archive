# Error with DWmodeling

**Topic ID**: 5423
**Date**: 2019-01-19
**URL**: https://discourse.slicer.org/t/error-with-dwmodeling/5423

---

## Post #1 by @happyle (2019-01-19 15:21 UTC)

<p>Operating system:win 10<br>
Slicer version:3Dslicer 4.11.0 2019-1-12<br>
Thank you <a class="mention" href="/u/fedorov">@fedorov</a>, i managed to get ADC maps using  DWI data from Philips, but it appeared to be “completed with error”.<br>
i had 40 dicom images contain 2 b-value(0,1000) for each slice of the brain. they were transfered into 2 nrrd file depended on b-value using 3dslicer, and were imported by multivolumeimporter<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b77c3b674f13247563313044a9ff8b3c33eaee4.png" data-download-href="/uploads/short-url/jTMXGrX5tEBngzjzejKkCDSGtQE.png?dl=1" title="%E5%9B%BE%E7%89%87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b77c3b674f13247563313044a9ff8b3c33eaee4.png" alt="%E5%9B%BE%E7%89%87" data-base62-sha1="jTMXGrX5tEBngzjzejKkCDSGtQE" width="690" height="396" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%9B%BE%E7%89%87</span><span class="informations">691×397 5.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
then i use DWmodeling as below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5868cd7cc8cc06bef8bef111edc98c6b3bfa9a34.png" data-download-href="/uploads/short-url/cC6ytIj1b00iAggIAl3Ucfeff5W.png?dl=1" title="%E5%9B%BE%E7%89%87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5868cd7cc8cc06bef8bef111edc98c6b3bfa9a34.png" alt="%E5%9B%BE%E7%89%87" data-base62-sha1="cC6ytIj1b00iAggIAl3Ucfeff5W" width="690" height="427" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%9B%BE%E7%89%87</span><span class="informations">814×504 6.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df1c2c89bd437eb3b3f55656f5e14f99e50bebbb.png" data-download-href="/uploads/short-url/vPIPYIGQhdGW3rJKMioCenK4Abx.png?dl=1" title="%E5%9B%BE%E7%89%87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df1c2c89bd437eb3b3f55656f5e14f99e50bebbb.png" alt="%E5%9B%BE%E7%89%87" data-base62-sha1="vPIPYIGQhdGW3rJKMioCenK4Abx" width="690" height="220" data-dominant-color="E6EEF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%9B%BE%E7%89%87</span><span class="informations">813×260 4.21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i wonder why it went wrong?<br>
in addition, if anything should be change in “Initialization”?</p>

---

## Post #2 by @fedorov (2019-01-19 17:08 UTC)

<p>Please expand the error log (the button to the right from the “Status” message, and post the error here.</p>
<p>About initialization, if you are not getting satisfactory fitting results, changing initialization might help, but I don’t have a good suggestion on the strategy of how those parameters should be adjusted. You will need to experiment with it. But in many cases this is not required.</p>

---

## Post #3 by @happyle (2019-01-21 16:09 UTC)

<p>Thank you <a class="mention" href="/u/fedorov">@fedorov</a>.<br>
the error log has been expanded and it was empty.<br>
but i found this after imported the data<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53864540d7ab2ce0b6f59523e3f6268384732049.png" data-download-href="/uploads/short-url/bUTiNVwebdN5BXkQbFNNIpatakN.png?dl=1" title="%E5%9B%BE%E7%89%87" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53864540d7ab2ce0b6f59523e3f6268384732049.png" alt="%E5%9B%BE%E7%89%87" data-base62-sha1="bUTiNVwebdN5BXkQbFNNIpatakN" width="690" height="390" data-dominant-color="F5EDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%9B%BE%E7%89%87</span><span class="informations">709×401 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
