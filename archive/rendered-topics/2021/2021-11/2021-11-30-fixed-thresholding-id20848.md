# Fixed thresholding

**Topic ID**: 20848
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/fixed-thresholding/20848

---

## Post #1 by @MPhilip (2021-11-30 18:25 UTC)

<p>Operating system:windows 10 enterprise<br>
Slicer version:Slicer 4.13.0-2021-10-25</p>
<p>I would like to know whether fixed thresholding can be implemented in 3Dslicer? To apply fixed thresholding SUVmax must be known and I guess PET parameters can be calculated using the extension PET standard uptake value computation. I am not quite sure about the input: PET Dicom volume path, input PET volume and input VOI volume which I read <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/petstandarduptakevaluecomputation.html" rel="noopener nofollow ugc">here</a>. The input VOI volume can be the GTV in RTSTRUCT or else how can I provide that? Also how to provide PET DICOM volume path?<br>
Could you please let me know what is the next step in applying a 40% fixed thresholding on the images, if that is possible in 3D slicer? I would like to know the workflow.</p>
<p>Thanks in advance</p>

---

## Post #2 by @pieper (2021-12-01 14:14 UTC)

<p>We don’t have a fixed procedure for that, but you can do it in two passes by first defining the general area you wan to measure with segmentation, then use Segment Statistics to get SUVmax, calculate the 40% manually, and then go back and use the result as a threshold to mask segmentation tools.  Then you an use Segment Statistics again to get vthe volume of the avidity.</p>

---

## Post #3 by @lassoan (2021-12-01 17:26 UTC)

<p><a class="mention" href="/u/mphilip">@MPhilip</a> if you need to do this for many cases then the process that <a class="mention" href="/u/pieper">@pieper</a> described can be easily automated using Python scripting. Let us know if you are interested and we can help you getting started.</p>

---

## Post #4 by @MPhilip (2021-12-01 17:39 UTC)

<p>Thank you for your suggestion. I have many cases and would like to automate them.<br>
It would be great if you could give some hints on how can I run the Python script on 3Dslicer, as I haven’t experimented using python script on 3d slicer.</p>

---

## Post #5 by @lassoan (2021-12-01 18:43 UTC)

<p>What input data do you have? Only the PET image or also some input points or segmentation (RTSTRUCT, DICOM Segmentation Object) that designate the region of interest?</p>
<p>What outputs do you need? Segmentation that contains a segment around each local maximum; and segment statistics computed on them (volume, mean/max SUV value, …)?</p>

---

## Post #6 by @MPhilip (2021-12-02 11:28 UTC)

<p>Thanks for your reply.</p>
<p>I have the PET image, CT image and the RTSTRUCT. Preferably I would use RTStruct.<br>
If I use the PET image, do I have to manually draw the ROI to determine the SUVmax to apply thresholding on the image?<br>
I would like the output to be: outlining the primary tumour and segment statistics computed on them.</p>

---
