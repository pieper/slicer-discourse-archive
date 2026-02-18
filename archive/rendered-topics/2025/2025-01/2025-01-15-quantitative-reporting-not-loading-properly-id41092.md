# Quantitative reporting not loading properly

**Topic ID**: 41092
**Date**: 2025-01-15
**URL**: https://discourse.slicer.org/t/quantitative-reporting-not-loading-properly/41092

---

## Post #1 by @daniele_rimini (2025-01-15 12:26 UTC)

<p>Good morning,</p>
<p>I have installed the “Quantitative reporting” extension to analyze the PET segments.</p>
<p>However, when I load the extension, the interface doesn’t show any field (Test area, Segmentions).</p>
<p>I got the following error from the console:<br>
ITK] WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478<br>
[ITK] ImageSeriesReader (0000023188D82060): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.007<br>
Traceback (most recent call last):<br>
File “C:/Users/drimini/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/QuantitativeReporting/lib/Slicer-5.6/qt-scripted-modules/QuantitativeReporting.py”, line 77, in enter<br>
if self.measurementReportSelector.currentNode():<br>
AttributeError: ‘QuantitativeReportingWidget’ object has no attribute ‘measurementReportSelector’</p>
<p>I am using the latest version of Slicer.</p>
<p>Thank you for your help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b8635bcdd728cc58fa2dcfea2ba01441255dd9c.png" data-download-href="/uploads/short-url/1DWNkeO2WWKk8KotyKkIOuwWB4w.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b8635bcdd728cc58fa2dcfea2ba01441255dd9c_2_690x377.png" alt="Capture" data-base62-sha1="1DWNkeO2WWKk8KotyKkIOuwWB4w" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b8635bcdd728cc58fa2dcfea2ba01441255dd9c_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b8635bcdd728cc58fa2dcfea2ba01441255dd9c_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b8635bcdd728cc58fa2dcfea2ba01441255dd9c_2_1380x754.png 2x" data-dominant-color="78777D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">2560×1400 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
