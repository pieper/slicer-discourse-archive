---
topic_id: 31605
title: "Lungmask In Lung Ct Segmenter Eof Error"
date: 2023-09-07
url: https://discourse.slicer.org/t/31605
---

# LUNGMASK in Lung CT segmenter EOF error

**Topic ID**: 31605
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/lungmask-in-lung-ct-segmenter-eof-error/31605

---

## Post #1 by @BM167 (2023-09-07 14:52 UTC)

<p>Lung CT segmenter</p>
<p>I am trying to segment lung CT into lobes (Using lung mask LTRC lobes_231). Using slicer 5.4.0.</p>
<p>No matter how many times I reloaded lungmask file, there still seems to be a problem with a corruption of the file.</p>
<p>I have Pytorch (torch and torch vision properly installed (and reinstalled) using pytorch utilities) as well as CU118.</p>
<p>Python Console shows the following:</p>
<p>Any ideas?<br>
Thanks very much.</p>
<p>Lungmask version: 0.2.16<br>
[Python] Failed to compute results: unexpected EOF, expected 3373102 more bytes. The file might be corrupted.<br>
Traceback (most recent call last):<br>
File “C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/LungCTAnalyzer/lib/Slicer-5.4/qt-scripted-modules/LungCTSegmenter.py”, line 1002, in runProcessing<br>
self.logic.applySegmentation()<br>
File “C:/ProgramData/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/LungCTAnalyzer/lib/Slicer-5.4/qt-scripted-modules/LungCTSegmenter.py”, line 2374, in applySegmentation<br>
inferer = LMInferer(modelname=‘LTRCLobes’, fillmodel=‘R231’)<br>
File “C:\ProgramData\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\lungmask\mask.py”, line 119, in <strong>init</strong><br>
self.model = get_model(self.modelname, modelpath)<br>
File “C:\ProgramData\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\lungmask\mask.py”, line 50, in get_model<br>
state_dict = torch.hub.load_state_dict_from_url(<br>
File “C:\ProgramData\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\torch\hub.py”, line 750, in load_state_dict_from_url<br>
return torch.load(cached_file, map_location=map_location)<br>
File “C:\ProgramData\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\torch\serialization.py”, line 815, in load<br>
return _legacy_load(opened_file, map_location, pickle_module, **pickle_load_args)<br>
File “C:\ProgramData\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\torch\serialization.py”, line 1051, in _legacy_load<br>
typed_storage._untyped_storage._set_from_file(<br>
RuntimeError: unexpected EOF, expected 3373102 more bytes. The file might be corrupted.<br>
[VTK] Warning: In vtkMRMLSegmentationDisplayNode.cxx, line 295<br>
[VTK] vtkMRMLSegmentationDisplayNode (0000015A41082A30): vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=, return default</p>

---

## Post #2 by @rbumm (2023-09-08 06:36 UTC)

<p>Lungmask works well on our systems. That is what I get when I use the CT Chest demo dataset and 5.4.0 with lungmaskLCTRlobes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b01facf9408368adc3753d340b397d2c3ff8ac.jpeg" data-download-href="/uploads/short-url/c5brXahUF1ZKH1GwR32FBbwSxuQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b01facf9408368adc3753d340b397d2c3ff8ac_2_690x497.jpeg" alt="image" data-base62-sha1="c5brXahUF1ZKH1GwR32FBbwSxuQ" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b01facf9408368adc3753d340b397d2c3ff8ac_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b01facf9408368adc3753d340b397d2c3ff8ac_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b01facf9408368adc3753d340b397d2c3ff8ac.jpeg 2x" data-dominant-color="868387"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1321×952 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(Windows gaming laptop with an NVIDIA Geforce GTX 1060)</p>

---

## Post #3 by @rbumm (2023-09-08 06:42 UTC)

<p>My recommendation would be to delete everything and start from scratch again - Install 3D Slicer, Pytorch via the Pytorch extension, restart Slicer, and then install Lung CT Analyzer. Some files may be corrupted.</p>

---
