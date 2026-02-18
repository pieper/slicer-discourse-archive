# SegmentationUnet

**Topic ID**: 25497
**Date**: 2022-09-30
**URL**: https://discourse.slicer.org/t/segmentationunet/25497

---

## Post #1 by @Isabella_Romero (2022-09-30 08:20 UTC)

<p>Hi,<br>
I am trying to automate the SegmentationUNet module with Python (using the logic and widget commands).<br>
I am trying to code the following buttons so that I can choose an input volume and prediction volume with python.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68758f216d2be3a4c799a0576e42aa899a901f15.png" data-download-href="/uploads/short-url/eU5wCv4Zf96bVvDQXDdvksk2Wgt.png?dl=1" title="Captura de pantalla 2022-09-30 a las 10.16.04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68758f216d2be3a4c799a0576e42aa899a901f15.png" alt="Captura de pantalla 2022-09-30 a las 10.16.04" data-base62-sha1="eU5wCv4Zf96bVvDQXDdvksk2Wgt" width="690" height="77" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2022-09-30 a las 10.16.04</span><span class="informations">1044×118 5.63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to set the following values for input Volume (image) and Prediction volume (Create new Volume as… and a name).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/036bb892c92553e57e4322adc84e21abe5f81c4e.png" data-download-href="/uploads/short-url/ugdRop2ZDVctsfZ8huSDfMkDuK.png?dl=1" title="Captura de pantalla 2022-09-30 a las 10.16.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036bb892c92553e57e4322adc84e21abe5f81c4e_2_690x245.png" alt="Captura de pantalla 2022-09-30 a las 10.16.13" data-base62-sha1="ugdRop2ZDVctsfZ8huSDfMkDuK" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036bb892c92553e57e4322adc84e21abe5f81c4e_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036bb892c92553e57e4322adc84e21abe5f81c4e_2_1035x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/036bb892c92553e57e4322adc84e21abe5f81c4e.png 2x" data-dominant-color="D8DDE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2022-09-30 a las 10.16.13</span><span class="informations">1046×372 59.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I found the following command in logic but it doesn’t work to set the input volume as desired:</p>
<p>setInputImage(self, inputImageNode)<br>
|      Sets input image node<br>
|      :param inputImageNode: vtkMRMLScalarVolumeNode<br>
|      :return: None</p>

---

## Post #2 by @Connor-Bowley (2022-10-03 12:41 UTC)

<p>In general, updating the logic doesn’t update the UI. If you are looking to update the UI, you can access the UI’s “Input Volume” <code>qMRMLNodeComboBox</code> using <code>widget.ui.inputSelector</code> (where <code>widget</code> is the widget object).</p>
<p>In general for Python modules, you can access the UI elements using the <code>.ui</code> section of the widget object. By looking at <code>SegmentationUNet.ui</code>, you can determine the names of the elements, like <a href="https://github.com/SlicerIGT/aigt/blob/66343f6b9c8c8fa6974d6af9297d03a83f3dcb64/SlicerExtension/LiveUltrasoundAi/SegmentationUNet/Resources/UI/SegmentationUNet.ui#L48" rel="noopener nofollow ugc">here</a>.</p>
<p>Here is a <a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html" rel="noopener nofollow ugc">reference</a> to <code>qMRMLNodeComboBox</code> so you can see how to set the node programmatically.</p>

---

## Post #3 by @Isabella_Romero (2022-10-04 07:03 UTC)

<p>Thank you so much for your answer. I am going to try it now and let you know how it goes.</p>

---
