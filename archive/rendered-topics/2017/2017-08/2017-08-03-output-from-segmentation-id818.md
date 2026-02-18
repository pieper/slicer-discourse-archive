# Output from segmentation

**Topic ID**: 818
**Date**: 2017-08-03
**URL**: https://discourse.slicer.org/t/output-from-segmentation/818

---

## Post #1 by @Kang_Wang (2017-08-03 17:47 UTC)

<pre><code class="lang-auto">Operating system  : Mac OS 
Slicer version    : 4.62
Expected behavior :
Actual behavior   : image volume mismatch
</code></pre>
<p>Hi,</p>
<p>I am new the 3D slicer, basically i use segmentation editor to create manual segmentation and then save the segmentation as the default .nrrd file.</p>
<p>However, the segmentation file has different dimension than the original raw data file, it loads fine on 3D slicer, but i am wondering how can i create a segmentation file that has the SAME dimension as the original data file (i.e. like the labelvolume you save from just editor).</p>
<p>I tried export it to labelvolume but doesn’t work.</p>
<p>Any help will be great, thanx</p>

---

## Post #2 by @cpinter (2017-08-03 18:02 UTC)

<p>If you export the segmentation into a labelmap in the Segmentations module with your anatomical volume set as the reference (Export/Import, Advanced section), then save the labelmap as nrrd, then they will have the same dimensions. However, you’ll lose information if the segments overlap.</p>
<p>What is the reason you want it to have the same dimensions? Maybe you can do the following steps in Slicer as well, not having to do the export like this.</p>

---

## Post #3 by @lassoan (2017-08-03 18:41 UTC)

<p>You probably need to use a recent nightly version of Slicer for this. I think 4.6.2 does not have the option of setting the reference volume (and the nightly has many other fixes and improvements).</p>

---

## Post #4 by @Kang_Wang (2017-08-03 21:19 UTC)

<p>Thanks for the quit reply Csaba =D.  Maybe there is an easier way to do this.  I mainly want the manual segmentation label to have the same dimension as the input images because i am preparing ground truth for collaborators who are developing segmentation algorithm.  That is the easiest way i can see to provide the ground truth to them.  If there is a better way like some information in the header i can use so they can align the segment volume and raw image volume together in python, i will be happy to use that advise as well.  Thanks in advance.</p>

---

## Post #5 by @Kang_Wang (2017-08-03 21:21 UTC)

<p>Andras, also thanx for the tip, please see below- again if there is a better way to do this please let me know since i am very new to slicer.  Essentially how do i align two 3D data matrix with different size i guess.  Thanx</p>

---

## Post #6 by @cpinter (2017-08-03 21:35 UTC)

<p>If you want simpler, then you can export DICOM. Unfortunately the DICOM SEG exporter is currently broke, but very close to fixing, see <a href="https://github.com/QIICR/QuantitativeReporting/issues/140">https://github.com/QIICR/QuantitativeReporting/issues/140</a></p>
<p>Exporting the segmentation to the labelmap takes around 8 clicks additinally to the few hundred you made when doing the segmentation. I think it is still much simpler than coming up with an elaborate workaround. If you want to make it quicker you can always write a python script that does that for you.</p>

---
