# dentalsegmentator Failed to load the segmentation, Something went wrong during the nnUNet processing.

**Topic ID**: 40682
**Date**: 2024-12-13
**URL**: https://discourse.slicer.org/t/dentalsegmentator-failed-to-load-the-segmentation-something-went-wrong-during-the-nnunet-processing/40682

---

## Post #1 by @g.alh (2024-12-13 15:47 UTC)

<p>I need help with this error I couldn’t figure it out regarding dentalsegmenttor</p>
<p>2024/12/13 17:49:45.935 :: nnUNet is already installed (2.5.1) and compatible with requested version (nnunetv2).<br>
2024/12/13 17:49:59.535 :: Transferring volume to nnUNet in C:/Users/hp/AppData/Local/Temp/Slicer-Mqpbvj<br>
2024/12/13 17:51:05.788 :: Starting nnUNet with the following parameters:<br>
2024/12/13 17:51:05.788 ::<br>
2024/12/13 17:51:05.788 :: C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/hp/AppData/Local/Temp/Slicer-Mqpbvj/input -o C:/Users/hp/AppData/Local/Temp/Slicer-Mqpbvj/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cpu -chk checkpoint_final.pth --disable_tta<br>
2024/12/13 17:51:05.788 ::<br>
2024/12/13 17:51:05.788 :: JSON parameters :<br>
2024/12/13 17:51:05.788 :: {<br>
2024/12/13 17:51:05.788 ::     “folds”: “0”,<br>
2024/12/13 17:51:05.788 ::     “device”: “cpu”,<br>
2024/12/13 17:51:05.788 ::     “stepSize”: 0.5,<br>
2024/12/13 17:51:05.788 ::     “disableTta”: true,<br>
2024/12/13 17:51:05.788 ::     “nProcessPreprocessing”: 1,<br>
2024/12/13 17:51:05.788 ::     “nProcessSegmentationExport”: 1,<br>
2024/12/13 17:51:05.788 ::     “checkPointName”: “”,<br>
2024/12/13 17:51:05.788 ::     “modelPath”: {<br>
2024/12/13 17:51:05.788 ::         “_path”: “C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\slicer.org\Extensions-33077\DentalSegmentator\lib\Slicer-5.7\qt-scripted-modules\Resources\ML”<br>
2024/12/13 17:51:05.788 ::     }<br>
2024/12/13 17:51:05.788 :: }<br>
2024/12/13 17:51:05.894 :: nnUNet preprocessing…<br>
2024/12/13 17:51:08.519 :: Traceback (most recent call last):<br>
2024/12/13 17:51:08.519 ::   File “C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
2024/12/13 17:51:08.520 :: return _run_code(code, main_globals, None,<br>
2024/12/13 17:51:08.520 ::   File “C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
2024/12/13 17:51:08.520 ::     exec(code, run_globals)<br>
2024/12/13 17:51:08.520 ::   File "C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\lib\Python\Scripts\nnUNetv2_predict.exe_<em>main</em></em>.py", line 4, in <br>
2024/12/13 17:51:08.520 ::   File “C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 12, in <br>
2024/12/13 17:51:08.520 ::     from batchgenerators.dataloading.multi_threaded_augmenter import MultiThreadedAugmenter<br>
2024/12/13 17:51:08.520 ::   File “C:\Users\hp\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-28\lib\Python\Lib\site-packages\batchgenerators\dataloading\multi_threaded_augmenter.py”, line 26, in <br>
2024/12/13 17:51:08.545 :: from threadpoolctl import threadpool_limits<br>
2024/12/13 17:51:08.545 :: ModuleNotFoundError: No module named ‘threadpoolctl’<br>
2024/12/13 17:51:08.740 :: Loading inference results…<br>
2024/12/13 17:51:31.644 :: Error loading results :<br>
2024/12/13 17:51:31.644 :: Failed to load the segmentation.<br>
2024/12/13 17:51:31.644 :: Something went wrong during the nnUNet processing.<br>
2024/12/13 17:51:31.644 :: Please check the logs for potential errors and contact the library maintainers.</p>

---

## Post #2 by @lassoan (2024-12-13 15:58 UTC)

<p>It seems that it is the same issue as this:</p>
<aside class="quote quote-modified" data-post="1" data-topic="38452">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/8797f3/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentor-showing-missing-threadpoolctl-module/38452">Totalsegmentor showing missing threadpoolctl module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    hello community. 
I have updated my slicer version to version 5.6.2 and that seems to have broken Total Segmentor. I am getting a failed to compute results with non-zero exit status 1 with the following logs. 
it looks like a python module threadpoolctl is missing. My python is rudimentary, is there a way to install this manually and get total segmentor to reference it correctly? 
Processing started
Writing input file to C:/Users/XXXX/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-20_05+05+47.1…
  </blockquote>
</aside>

<p>The solution is described there.</p>

---
