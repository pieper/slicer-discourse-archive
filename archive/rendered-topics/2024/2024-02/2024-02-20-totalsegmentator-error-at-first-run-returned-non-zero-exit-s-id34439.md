---
topic_id: 34439
title: "Totalsegmentator Error At First Run Returned Non Zero Exit S"
date: 2024-02-20
url: https://discourse.slicer.org/t/34439
---

# TotalSegmentator error at first run: returned non-zero exit status 120.

**Topic ID**: 34439
**Date**: 2024-02-20
**URL**: https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-returned-non-zero-exit-status-120/34439

---

## Post #1 by @Rolling (2024-02-20 23:22 UTC)

<p>Dear all</p>
<p>I tried to use the TotalSegmentator in 3D slicer, but I got an error：<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74934427f10cffbcb05400fca1c25e51f1e1277a.png" data-download-href="/uploads/short-url/gDgTZdY6UmKcMYZxh2vtwhHkj7c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74934427f10cffbcb05400fca1c25e51f1e1277a_2_690x142.png" alt="image" data-base62-sha1="gDgTZdY6UmKcMYZxh2vtwhHkj7c" width="690" height="142" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74934427f10cffbcb05400fca1c25e51f1e1277a_2_690x142.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74934427f10cffbcb05400fca1c25e51f1e1277a_2_1035x213.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74934427f10cffbcb05400fca1c25e51f1e1277a_2_1380x284.png 2x" data-dominant-color="E5E5E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1660×343 64.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Failed to compute results.</p>
<p>Traceback (most recent call last):<br>
File “E:\3D Slicer\Slicer 5.6.1\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “E:/3D Slicer/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 292, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “E:/3D Slicer/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 967, in process<br>
self.logProcessOutput(proc)<br>
File “E:/3D Slicer/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 787, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘E:/3D Slicer/Slicer 5.6.1/bin/…/bin\PythonSlicer.EXE’, ‘E:\3D Slicer\Slicer 5.6.1\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/xrnyy/AppData/Local/Temp/Slicer/__SlicerTemp__2024-02-20_22+51+14.310/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/xrnyy/AppData/Local/Temp/Slicer/__SlicerTemp__2024-02-20_22+51+14.310/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Then the error reported under the “Apply” button :</p>
<p>Processing started<br>
Writing input file to C:/Users/xrnyy/AppData/Local/Temp/Slicer/__SlicerTemp__2024-02-20_22+51+14.310/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/xrnyy/AppData/Local/Temp/Slicer/__SlicerTemp__2024-02-20_22+51+14.310/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/xrnyy/AppData/Local/Temp/Slicer/__SlicerTemp__2024-02-20_22+51+14.310/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
Traceback (most recent call last):<br>
File “E:\3D Slicer\Slicer 5.6.1\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return _run_code(code, main_globals, None,<br>
File “E:\3D Slicer\Slicer 5.6.1\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "E:\3D Slicer\Slicer 5.6.1\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “E:\3D Slicer\Slicer 5.6.1\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 127, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “E:\3D Slicer\Slicer 5.6.1\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 77, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
File “E:\3D Slicer\Slicer 5.6.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 23, in <br>
from nnunetv2.inference.predict_from_raw_data import predict_from_raw_data<br>
ModuleNotFoundError: No module named ‘nnunetv2’<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000002840C2953A0&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Thank you very much for the support!</p>

---

## Post #2 by @jamesobutler (2024-02-20 23:55 UTC)

<p>Please see the following post regarding a required workaround. Note this may change as the various dependencies of the <code>TotalSegmentator</code> python package change.</p>
<aside class="quote quote-modified" data-post="11" data-topic="34434">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-failing-with-error-120/34434/11">Totalsegmentator failing with error 120</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Aha! So, it is not a too old package, but a too recent package. 
Unfortunately, developer of dynamic_network_architectures broke backward compatibility with a recent update. ResidualEncoderUNet package must be imported as from dynamic_network_architectures.architectures.residual_unet import ResidualEncoderUNet now, but since this change was snuck into a minor version update (0.2 to 0.4) developer of TotalSegmentator did not suspect anything bad would happen. 
As a workaround, you can downgrade d…
  </blockquote>
</aside>


---
