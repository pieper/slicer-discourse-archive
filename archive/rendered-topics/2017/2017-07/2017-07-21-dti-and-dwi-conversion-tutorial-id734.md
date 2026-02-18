# DTI and DWI conversion tutorial

**Topic ID**: 734
**Date**: 2017-07-21
**URL**: https://discourse.slicer.org/t/dti-and-dwi-conversion-tutorial/734

---

## Post #1 by @iplneurosurgery (2017-07-21 05:15 UTC)

<p>Hi Sir,</p>
<p>We are using the slicer version of 4.6.2 and 4.7.0 in Windows 8. In DTI processing the input DWI volume which is downloaded from slicer dataset is supported in 4.6.2 and we are able to obtain the output in 4.6.2 but the same with 4.7.0 its processing till brain masking and exited with errors for the proceeding steps of estimation of tensor. With out datasets of DWI volume is also not processing in both the versions. We would like to have tutorial for converting the dataset into DWI volume and for processing DTI tractography. Can someone help us with a tutorial.</p>
<p>Thanks.</p>
<p>Suba</p>

---

## Post #2 by @ihnorton (2017-07-21 13:51 UTC)



---

## Post #3 by @ihnorton (2017-07-21 14:08 UTC)

<p>Hello – I made this post public since it’s of general interest.</p>
<p>I’ve just tested the masking -&gt; estimation workflow using the latest nightly download (2017-07-20) on Windows 10, and everything works as expected with the “DWIVolume” dataset from the Sample Data module.</p>
<p>Please post a copy of the Error Log (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report">instructions</a>).</p>

---

## Post #4 by @iplneurosurgery (2017-07-22 09:53 UTC)

<p>Hi Sir,</p>
<p>Good Evening. I have attached the screenshot of the DTI process completed with errors and error log using the Sample DWI volume dataset from slicer.</p>
<p>Let me know how to solve this issue.</p>
<p>Thanks</p>
<p>Suba</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d479c1a516a7349564f423ec6a7609e53bab0d86.jpg" data-download-href="/uploads/short-url/ujE5jklO38HThJW6Ovhb8aSmcqq.jpg?dl=1" title="dti.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d479c1a516a7349564f423ec6a7609e53bab0d86_2_690x375.jpg" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d479c1a516a7349564f423ec6a7609e53bab0d86_2_690x375.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d479c1a516a7349564f423ec6a7609e53bab0d86_2_1035x562.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d479c1a516a7349564f423ec6a7609e53bab0d86_2_1380x750.jpg 2x" data-dominant-color="7F7F8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dti.jpg</span><span class="informations">3840×2089 887 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5226ed9661c45b9265fec513831219c98a95aa50.PNG" data-download-href="/uploads/short-url/bIKyrHN7J0oSRXabE5qsknxkR3O.PNG?dl=1" title="error log.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5226ed9661c45b9265fec513831219c98a95aa50_2_690x228.PNG" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5226ed9661c45b9265fec513831219c98a95aa50_2_690x228.PNG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5226ed9661c45b9265fec513831219c98a95aa50_2_1035x342.PNG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5226ed9661c45b9265fec513831219c98a95aa50_2_1380x456.PNG 2x" data-dominant-color="E6E9F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error log.PNG</span><span class="informations">3840×1270 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @ljod (2017-07-22 10:32 UTC)

<p>Hello, this is the Warning log. Are there any errors if you click the tab at the top of the Log Messages window where it says Errors?</p>
<p>From the information in your image and from this log, the diffusion tensors and the mask have been successfully estimated (see log lines that say both completed without errors). Please let us know more information about which specific step or which specific module is not working for you.</p>

---

## Post #6 by @iplneurosurgery (2017-07-23 10:54 UTC)

<p>Hi Sir,</p>
<p>Good Evening. I am now able to process the DTI successfully with nightly build version. Thank you for your spontaneous reply and I am being grateful for your help. Good team work and all the best with success.</p>
<p>Thank you,</p>
<p>Suba</p>

---

## Post #7 by @lassoan (2017-08-15 16:41 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-get-number-of-points-in-a-model/874">How to get number of points in a model</a></p>

---
