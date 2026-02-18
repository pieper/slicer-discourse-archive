# ADC values on a DWI scan

**Topic ID**: 1352
**Date**: 2017-11-02
**URL**: https://discourse.slicer.org/t/adc-values-on-a-dwi-scan/1352

---

## Post #1 by @faraz1368 (2017-11-02 15:17 UTC)

<p>Hi,<br>
I wanted to know if it is possible to load a DWI scan into slicer, draw a ROI and find the ADC values (in 10-6 mm2/s) (average and a distribution curve) corresponding to that ROI.</p>
<p>Thank you for your responses<br>
Faraz</p>
<p>Slicer version:4.9.0 (nightly)<br>
operating system: Windows 7</p>

---

## Post #2 by @happyle (2017-11-02 15:30 UTC)

<p>it can be done on Firevoxel(<a href="https://wp.nyu.edu/firevoxel/" rel="nofollow noopener">https://wp.nyu.edu/firevoxel/</a>),i wonder if 3Dslicer can do this too:grin:</p>

---

## Post #3 by @fedorov (2017-11-02 16:58 UTC)

<p>If your DWI data can be parsed as a MultiVolume from DICOM Browser (it must be in DICOM to try that), you can next try DWModeling module from the SlicerProstate extension to fit various models to the data: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWModeling">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWModeling</a></p>

---

## Post #4 by @ihnorton (2017-11-02 23:55 UTC)

<p>If you have raw DWI you can use DWIConverter to load, then SlicerDMRI <code>Diffusion Tensor Estimation</code> and <code>DiffusionScalarMaps</code> to calculate an ADC volume; then use Segment Editor to draw ROI and LabelStatistics to measure. I’m not sure if this workflow is in any tutorials but I’ll check and send a link or some screenshot instructions tomorrow.</p>

---

## Post #5 by @lassoan (2017-11-03 16:11 UTC)

<p>Just a small addition to <a class="mention" href="/u/ihnorton">@ihnorton</a>’s recommendation: in this workflow, it is easier to use <code>Segment Statistics</code> module instead of <code>Label Statistics</code> module. (<code>Label Statistics</code> module requires labelmap volume as input, so you would first need to export segmentation to a labelmap volume.)</p>

---

## Post #6 by @happyle (2017-11-07 09:38 UTC)

<p>failed and still don’t know how to do ,looking forward to the screenshot:grin:</p>

---

## Post #7 by @ihnorton (2017-11-07 19:49 UTC)

<p>Ok, we don’t have a complete workflow tutorial for this, yet, but here are the steps and link to documentation for each step.</p>
<ol start="0">
<li>Please <a href="http://download.slicer.org">download the latest Slicer nightly</a> and install SlicerDMRI extension: <a href="http://dmri.slicer.org/download/" class="inline-onebox">Download</a></li>
<li>Please follow the <a href="https://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Training#Slicer4_Diffusion_Tensor_Imaging_Tutorial">DTI tutorial</a> for instructions to load data and estimate a tensor volume from raw DWI data.</li>
<li>Around page 47 is scalar calculation, and you can instead follow the next screenshot to calculate Mean Diffusivity (ADC):</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/412a35d08a20c47862ad421b46396c2e0a4abf21.png" alt="image" data-base62-sha1="9ittaLQ6Oy0H5jCpaVYM6hiAR7X" width="489" height="464"></p>
<ol start="3">
<li>
<p>Then use the <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor</a> to create regions of interest.</p>
</li>
<li>
<p>Then follow this video to use the Segment Statistics module as Andras suggested:</p>
</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="fM_rxfDTRi0" data-video-title="Segment statistics - new module in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fM_rxfDTRi0" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fM_rxfDTRi0/maxresdefault.jpg" title="Segment statistics - new module in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #8 by @Joejoe (2018-10-21 14:17 UTC)

<p>How about DWI images of other organs, like the breasts. I have dwi data of breast with b values of 0, 800, 1400, 2000. Can I calculate the ADC value from the trace DICOM files in 3D slicer? or better, use a DKI model to obtain diffusity and kurtosis scalar map.</p>

---

## Post #9 by @fedorov (2018-10-21 17:51 UTC)

<p>You can fit DWI data using the DWModeling module of the SlicerProstate extension.</p>

---

## Post #10 by @Mgi (2021-04-21 23:36 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a> ! I am using the Slicer version 4.11.20200930 on Windows 10. I want to calculate the ADC values from breast DWI images. I used the DWModeling module but I can not see the results, Could you share to me a tutorial, please? or tell me How I can see the results?</p>

---

## Post #11 by @fedorov (2021-04-22 15:11 UTC)

<p>The question from <a class="mention" href="/u/mgi">@Mgi</a> is being discussed in a separate thread here: <a href="https://discourse.slicer.org/t/calculate-the-adc-for-different-b-values-in-breast-dwi-images/17241" class="inline-onebox">Calculate the ADC for different b values in Breast DWI images</a>.</p>

---

## Post #12 by @Mgi (2021-04-23 21:09 UTC)

<p>Hi <a class="mention" href="/u/joejoe">@Joejoe</a> ! Could you solve this problem?</p>

---
