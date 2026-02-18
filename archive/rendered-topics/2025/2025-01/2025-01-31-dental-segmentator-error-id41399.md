# Dental Segmentator Error

**Topic ID**: 41399
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/dental-segmentator-error/41399

---

## Post #1 by @mraihan (2025-01-31 11:27 UTC)

<p>Hi,</p>
<p>I am unable to use the Dental Segmentator module. I am using slicer 5.8, Pytorch version is 2.6.0 + cu118. I have tried manually downloading the weights and adding it to the Recources/ML folder. However, I am still getting the following error in the log:</p>
<p>2025/01/30 09:50:19.665 :: nnUNet is already installed (2.5.1) and compatible with requested version (nnunetv2).<br>
2025/01/30 09:50:24.325 :: Transferring volume to nnUNet in C:/Users//AppData/Local/Temp/2/Slicer-OCVZwp<br>
2025/01/30 09:50:30.096 :: Starting nnUNet with the following parameters:<br>
2025/01/30 09:50:30.096 ::<br>
2025/01/30 09:50:30.096 :: C:\Users\Slicer 5.8.0\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users//AppData/Local/Temp/2/Slicer-OCVZwp/input -o C:/Users//AppData/Local/Temp/2/Slicer-OCVZwp/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta<br>
2025/01/30 09:50:30.096 ::<br>
2025/01/30 09:50:30.096 :: JSON parameters :<br>
2025/01/30 09:50:30.096 :: {<br>
2025/01/30 09:50:30.096 ::     “folds”: “0”,<br>
2025/01/30 09:50:30.096 ::     “device”: “cuda”,<br>
2025/01/30 09:50:30.096 ::     “stepSize”: 0.5,<br>
2025/01/30 09:50:30.096 ::     “disableTta”: true,<br>
2025/01/30 09:50:30.096 ::     “nProcessPreprocessing”: 1,<br>
2025/01/30 09:50:30.096 ::     “nProcessSegmentationExport”: 1,<br>
2025/01/30 09:50:30.096 ::     “checkPointName”: “”,<br>
2025/01/30 09:50:30.096 ::     “modelPath”: {<br>
2025/01/30 09:50:30.096 ::         “_path”: “C:\Users\Slicer 5.8.0\slicer.org\Extensions-33216\DentalSegmentator\lib\Slicer-5.8\qt-scripted-modules\Resources\ML”<br>
2025/01/30 09:50:30.096 ::     }<br>
2025/01/30 09:50:30.096 :: }<br>
2025/01/30 09:50:30.137 :: nnUNet preprocessing…<br>
2025/01/30 09:50:33.686 :: Traceback (most recent call last):<br>
2025/01/30 09:50:33.686 ::   File “C:\Users\Slicer 5.8.0\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
2025/01/30 09:50:33.781 :: return <em>run_code(code, main_globals, None,<br>
2025/01/30 09:50:33.781 ::   File “C:\Users\Slicer 5.8.0\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
2025/01/30 09:50:33.781 ::     exec(code, run_globals)<br>
2025/01/30 09:50:33.781 ::   File "C:\Users\Slicer 5.8.0\lib\Python\Scripts\nnUNetv2_predict.exe_<em>main</em></em>.py", line 7, in <br>
2025/01/30 09:50:33.781 ::   File “C:\Users\Slicer 5.8.0\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 861, in predict_entry_point<br>
2025/01/30 09:50:33.781 ::     predictor.initialize_from_trained_model_folder(<br>
2025/01/30 09:50:33.781 ::   File “C:\Users\Slicer 5.8.0\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 84, in initialize_from_trained_model_folder<br>
2025/01/30 09:50:33.781 ::     checkpoint = torch.load(join(model_training_output_dir, f’fold</em>{f}', checkpoint_name),<br>
2025/01/30 09:50:33.781 ::   File “C:\Users\Slicer 5.8.0\lib\Python\Lib\site-packages\torch\serialization.py”, line 1470, in load<br>
2025/01/30 09:50:33.781 ::     raise pickle.UnpicklingError(_get_wo_message(str(e))) from None<br>
2025/01/30 09:50:33.781 :: _pickle.UnpicklingError: Weights only load failed. This file can still be loaded, to do so you have two options, e[1mdo those steps only if you trust the source of the checkpointe[0m.<br>
2025/01/30 09:50:33.781 :: 	(1) In PyTorch 2.6, we changed the default value of the <code>weights_only</code> argument in <code>torch.load</code> from <code>False</code> to <code>True</code>. Re-running <code>torch.load</code> with <code>weights_only</code> set to <code>False</code> will likely succeed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.<br>
2025/01/30 09:50:33.781 :: 	(2) Alternatively, to load with <code>weights_only=True</code> please check the recommended steps in the following error message.<br>
2025/01/30 09:50:33.781 :: 	WeightsUnpickler error: Unsupported global: GLOBAL numpy.core.multiarray.scalar was not an allowed global by default. Please use <code>torch.serialization.add_safe_globals([scalar])</code> or the <code>torch.serialization.safe_globals([scalar])</code> context manager to allowlist this global if you trust this class/function.<br>
2025/01/30 09:50:33.781 ::<br>
2025/01/30 09:50:33.781 :: Check the documentation of torch.load to learn more about types accepted by default with weights_only <a href="https://pytorch.org/docs/stable/generated/torch.load.html" class="inline-onebox" rel="noopener nofollow ugc">torch.load — PyTorch 2.6 documentation</a>.<br>
2025/01/30 09:50:33.781 ::<br>
2025/01/30 09:50:33.781 :: #######################################################################<br>
2025/01/30 09:50:33.781 :: Please cite the following paper when using nnU-Net:<br>
2025/01/30 09:50:33.781 :: Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., &amp; Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.<br>
2025/01/30 09:50:33.781 :: #######################################################################<br>
2025/01/30 09:50:34.073 :: Loading inference results…<br>
2025/01/30 09:50:36.366 :: Error loading results :<br>
2025/01/30 09:50:36.366 :: Failed to load the segmentation.<br>
2025/01/30 09:50:36.366 :: Something went wrong during the nnUNet processing.<br>
2025/01/30 09:50:36.366 :: Please check the logs for potential errors and contact the library maintainers."</p>
<p>Could someone please look into the issue and recommend some possible workarounds?</p>

---

## Post #2 by @Thibault_Pelletier (2025-01-31 15:20 UTC)

<p>Hi <a class="mention" href="/u/mraihan">@mraihan</a>,</p>
<p>Looking at the error message, the PyTorch version 2.6 seems to be incompatible with the current version of the model / loading settings of nnU-Net.</p>
<p>You can manually downgrade the installed PyTorch version by using the <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">Slicer PyTorch extension</a> and installing the 2.5 version.</p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @mraihan (2025-01-31 18:15 UTC)

<p>Thanks, Thibault. It worked!</p>
<p>Regards,<br>
Raihan</p>

---

## Post #4 by @priskus (2025-02-05 16:11 UTC)

<p>Please, tell, how to install another version of Torch than automatic. I am trying to type different version in the field “Torch version requirement” But all the time I got errors:<br>
ERROR: No matching distribution found for torch2.5.0<br>
ERROR: Could not find a version that satisfies the requirement torch2.5.1 (from versions: none)<br>
ERROR: No matching distribution found for torch2.5.1<br>
ERROR: Could not find a version that satisfies the requirement torch2.5.1 (from versions: none)<br>
ERROR: No matching distribution found for torch2.5.1<br>
ERROR: Could not find a version that satisfies the requirement torch2.4.1 (from versions: none)<br>
ERROR: No matching distribution found for torch2.4.1<br>
ERROR: Could not find a version that satisfies the requirement torch2.4.0 (from versions: none)<br>
ERROR: No matching distribution found for torch2.4.0<br>
ERROR: Could not find a version that satisfies the requirement torch2.3.1 (from versions: none)<br>
ERROR: No matching distribution found for torch2.3.1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0f244001afa91e760f52cc9a564013c557fb157.png" data-download-href="/uploads/short-url/pfl5mxNMLTVvavifrZaa5MhKlFR.png?dl=1" title="изображение" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0f244001afa91e760f52cc9a564013c557fb157.png" alt="изображение" data-base62-sha1="pfl5mxNMLTVvavifrZaa5MhKlFR" width="457" height="159"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">изображение</span><span class="informations">457×159 2.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mraihan (2025-02-05 16:40 UTC)

<p>are you trying to install PyTorch for DentalSegmentator? You can uninstall the PyTorch extension and DentalSegmentator automatically installs the required library on its first usage (including the required PyTorch version). That worked for me.</p>

---

## Post #6 by @Thibault_Pelletier (2025-02-05 16:46 UTC)

<p>If you want to install a specific version, you need to specify it using “PyPi” syntaxe :</p>
<p>Using “&lt;2.6” should force the install to the latest torch version before 2.6</p>
<p>For 2.5.1, you should use “==2.5.1”</p>

---

## Post #7 by @Thibault_Pelletier (2025-02-05 16:49 UTC)

<p>Just a follow up on this problem, the issue is currently being tracked in the nnUNet repository to change how the nnUNet loads its weights : <a href="https://github.com/MIC-DKFZ/nnUNet/issues/2681" class="inline-onebox" rel="noopener nofollow ugc">PyTorch 2.6 has changed the default value of `weights_only` to `True`, breaking the loading of some `nnunetv2` models · Issue #2681 · MIC-DKFZ/nnUNet · GitHub</a></p>

---

## Post #8 by @jamesobutler (2025-02-05 18:58 UTC)

<p>The nnUNetv2 developer issued a fix and created a new release. Install the latest to use PyTorch 2.6. Also note that torchvision 0.21.0 is specifically compatible with PyTorch 2.6.0. See <a href="https://github.com/pytorch/vision?tab=readme-ov-file#installation" rel="noopener nofollow ugc">this table</a> for more info.</p>
<aside class="quote quote-modified" data-post="2" data-topic="41493">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/pytorch-2-6-seems-to-break-totalsegmentor/41493/2">PyTorch 2.6 seems to break TotalSegmentor </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The developer of nnUNetv2 (a dependency of TotalSegmentator) issued a fix earlier today. Please try going to the “nnUNet” module in Slicer and specifying to install nnUNet &gt;=2.5.2. 
Let us know how it goes for you! 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfbc59a338afec4e952b92e18e5e147a7c425d5.png" data-download-href="/uploads/short-url/hPECKV9NnJCZuYpehgnleYGg3FX.png?dl=1" title="{15F668A2-77BE-4F91-B30C-35B2D0AF80C6}" rel="noopener nofollow ugc">[{15F668A2-77BE-4F91-B30C-35B2D0AF80C6}]</a>
  </blockquote>
</aside>


---

## Post #9 by @yijie3091 (2025-05-11 13:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e69a361e99e0d0642353932c88d661c48bc0994.png" data-download-href="/uploads/short-url/6CAi8ffdlHa0jyJMGY08rAfgHSA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e69a361e99e0d0642353932c88d661c48bc0994.png" alt="image" data-base62-sha1="6CAi8ffdlHa0jyJMGY08rAfgHSA" width="690" height="181" data-dominant-color="EFEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×280 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd7b2532a88bbd6b9076a4559407a7038351cbc.png" data-download-href="/uploads/short-url/479uOlbI6Aq21EJNEdqD03Bh5jC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd7b2532a88bbd6b9076a4559407a7038351cbc_2_450x500.png" alt="image" data-base62-sha1="479uOlbI6Aq21EJNEdqD03Bh5jC" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd7b2532a88bbd6b9076a4559407a7038351cbc_2_450x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd7b2532a88bbd6b9076a4559407a7038351cbc_2_675x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd7b2532a88bbd6b9076a4559407a7038351cbc_2_900x1000.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">991×1099 48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbedb425416080501938e5cf11f460e9a93b1b69.png" data-download-href="/uploads/short-url/vnzQjJnmMbTlw4vsvAuvL5ePHMR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbedb425416080501938e5cf11f460e9a93b1b69.png" alt="image" data-base62-sha1="vnzQjJnmMbTlw4vsvAuvL5ePHMR" width="690" height="331" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1014×487 8.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
dear professor,when i download this“dentalsegmentator” extension，some questions above appeaer，how can i solve with them？</p>

---

## Post #10 by @Thibault_Pelletier (2025-05-14 06:20 UTC)

<p>Hi <a class="mention" href="/u/yijie3091">@yijie3091</a>,</p>
<p>As pointed out by the message, the weight download failed because your internet connection was down.</p>
<p>To troubleshoot this, please follow the instructions here : <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights" class="inline-onebox" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</a></p>
<p>You will need to unzip the weight files in the correct folder and create a <code>download_info.json</code> file in the ML folder.</p>
<p>Best,<br>
Thibault</p>

---

## Post #11 by @yijie3091 (2025-05-14 07:47 UTC)

<p>I have downloaded the zip files，but I can not<br>
find the weight file，even I do not have the LM folder.In addition ，my windows do not have GPU.</p>
<p>Thibault Pelletier via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;于2025年5月14日 周三14:20写道：</p>

---

## Post #12 by @Thibault_Pelletier (2025-05-14 10:59 UTC)

<p>Hi <a class="mention" href="/u/yijie3091">@yijie3091</a>,</p>
<p>As written in the <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights" rel="noopener nofollow ugc">troubleshooting section</a>, you need to :</p>
<ul>
<li>Create a ML folder in the Resources folder</li>
<li>Download and unzip the <a href="https://github.com/gaudot/SlicerDentalSegmentator/releases/download/v1.0.0-alpha/Dataset111_453CT_v100.zip" rel="noopener nofollow ugc">Dataset111_453CT_v100.zip</a> file in the ML folder</li>
<li>Create a download_info.json file in the ML folder with the following content : {“download_url”: “<a href="https://github.com/gaudot/SlicerDentalSegmentator/releases/download/v1.0.0-alpha/Dataset111_453CT_v100.zip" rel="noopener nofollow ugc">https://github.com/gaudot/SlicerDentalSegmentator/releases/download/v1.0.0-alpha/Dataset111_453CT_v100.zip</a>”}</li>
</ul>
<p>If everything works well, you should have the following file accessible :<br>
C:\Users\&lt;user_name&gt;\AppData\Local\slicer.org\Slicer 5.8.1\slicer.org\Extensions-33241\DentalSegmentator\lib\Slicer-5.8\qt-scripted-modules\Resources\ML\Dataset111_453CT\nnUNetTrainer__nnUNetPlans__3d_fullres\dataset.json</p>
<p>Best,<br>
Thibault</p>

---

## Post #13 by @yijie3091 (2025-05-18 14:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c4db2f08746621b7a5065ef993999d76c372c.jpeg" data-download-href="/uploads/short-url/flpGFxnXsIB1ywknsV0siBD4ffu.jpeg?dl=1" title="IMG_6248.jpeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8c4db2f08746621b7a5065ef993999d76c372c_2_666x500.jpeg" data-base62-sha1="flpGFxnXsIB1ywknsV0siBD4ffu" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8c4db2f08746621b7a5065ef993999d76c372c_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8c4db2f08746621b7a5065ef993999d76c372c_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8c4db2f08746621b7a5065ef993999d76c372c_2_1332x1000.jpeg 2x" data-dominant-color="A2A1A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_6248.jpeg</span><span class="informations">4032×3024 3.82 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have followed your instructions step by step，but it seems have a problem.How can i solve with it？</p>
<p>Thibault Pelletier via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;于2025年5月14日 周三18:59写道：</p>

---

## Post #14 by @Thibault_Pelletier (2025-05-20 07:36 UTC)

<p>Hi <a class="mention" href="/u/yijie3091">@yijie3091</a>,</p>
<p>Please don’t take pictures of you screen in the future and instead copy / paste the contents of the error messages and python console when providing context for your issues.</p>
<p>Regarding the issue itself, it’s indicating that the “dataset.json” file is missing in the python console. This indicates that your ML file tree is still not correct.</p>
<p>Your Resources folder should contain the following file structure :</p>
<pre><code class="lang-auto">+---Icons
|       DentalSegmentator.png
|       DentalSegmentator_full_icon.png
|       info.png
|       loading.gif
|       start_icon.png
|       
\---ML
    |   Dataset111_453CT_v100.zip
    |   download_info.json
    |   
    \---Dataset111_453CT
        \---nnUNetTrainer__nnUNetPlans__3d_fullres
            |   dataset.json
            |   plans.json
            |   
            \---fold_0
                    checkpoint_final.pth
</code></pre>
<p>FYI  you can print your file structure on windows using the command prompt and the <code>tree /F /A</code> command.</p>
<p>Best,<br>
Thibault</p>

---

## Post #15 by @leoniea (2025-06-11 12:36 UTC)

<p>Hello, I tried to use the Dentalsegmentator and have set the folder of Resources correctly, but it seems like the nnunet cannot work at all. I have following errors:</p>
<pre><code class="lang-auto">[Qt] void __cdecl qMRMLSegmentEditorWidget::setSourceVolumeNode(class vtkMRMLNode *)  failed: need to set segment editor and segmentation nodes first
[Python] Failed to load the segmentation.
[Python] Something went wrong during the nnUNet processing.
[Python] Please check the logs for potential errors and contact the library maintainers.
</code></pre>
<p>I have no idea I cannot install the pytorch with specific version like 2.5.1, only could be installed with 2.7.1, which is the latest one. When I tried to install Pytorch by pip, it would be stuck for a while and no reaction afterwards. Using the latest version would be ny effect that lead to such error?</p>
<p>Best,<br>
Leoniea</p>

---

## Post #16 by @Thibault_Pelletier (2025-06-11 13:34 UTC)

<p>Hi <a class="mention" href="/u/leoniea">@leoniea</a>,</p>
<p>Thank you for your message. Your problem is very likely due to the pytorch version. This version is not yet supported by Slicer (see <a href="https://github.com/Slicer/Slicer/issues/8468" rel="noopener nofollow ugc">related issue for more information</a>).</p>
<p>Could you detail what you mean by:</p>
<blockquote>
<p>I cannot install the pytorch with specific version like 2.5.1</p>
</blockquote>
<p>Installing specific versions of pytorch should be possible through the PyTorch module.</p>
<p>Best,<br>
Thibault</p>

---

## Post #17 by @leoniea (2025-06-11 14:57 UTC)

<p>hi thanks for your reply! Yeah I mean since the Pytorch will be installed automatically in version 2.7 when I directly click the “install” button, hence I tried to install it via “pip install torch==2.5.1…” in the python console of Slicer, but the installation process is always problemaitc and getting stuck during the process. I don’t know why but using other’s latop can handle this issue. Kind of weird. So is there any solution except using the “pip”?<br>
Thanks in advance!</p>
<p>Best<br>
Leoniea</p>

---

## Post #18 by @Thibault_Pelletier (2025-06-13 05:15 UTC)

<p>If you install pytorch first then the extension will not try to install it again.<br>
Installing PyTorch can be done using the dedicated PyTorch extension in the extension manager.</p>
<p>You can find more information on the <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">SlicerPyTorch Github</a>.</p>

---

## Post #19 by @Josh_Chow (2025-08-14 05:29 UTC)

<p>How do I create a “download_info.json” file?</p>
<p>Also, my DentalSegmentator folder only has “lib” and “share” folders. So I created a “Resources” folder and a “ML” folder inside that. I unzipped the “SlicerDentalSegmentator-main” in the ML folder and placed the “Dataset111_453CT_v100.zip” in there. Is that the correct thing to do?</p>

---

## Post #20 by @Thibault_Pelletier (2025-08-19 05:56 UTC)

<p>Hi <a class="mention" href="/u/josh_chow">@Josh_Chow</a>,</p>
<p>The latest version of the dental segmentator now doesn’t require a .json file anymore.</p>
<p>You can update the extension using the check for updates / update button in the extensions manager.</p>
<p>To know where to create the ML folder, you can check the extension path in the module finder. The path should look like : `C:/Users/Thibault/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/DentalSegmentator/lib/Slicer-5.8/qt-scripted-modules/DentalSegmentator.py`</p>
<p>The resources folder will be located in the same folder :<br>
`C:/Users/Thibault/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/DentalSegmentator/lib/Slicer-5.8/qt-scripted-modules/Resources`</p>
<p>In the Resources folder, create a ML folder and unzip the weight files there.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d64e4e3109e1f45771a3c05e120d4641fcc6d86.jpeg" data-download-href="/uploads/short-url/dkcziy9SbrUXYQi5KEeFOH1Pkl8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64e4e3109e1f45771a3c05e120d4641fcc6d86_2_617x500.jpeg" alt="image" data-base62-sha1="dkcziy9SbrUXYQi5KEeFOH1Pkl8" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64e4e3109e1f45771a3c05e120d4641fcc6d86_2_617x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d64e4e3109e1f45771a3c05e120d4641fcc6d86_2_925x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d64e4e3109e1f45771a3c05e120d4641fcc6d86.jpeg 2x" data-dominant-color="EAEAF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">961×778 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e611b227c9c518fba20691dbe510f9d1b77948b4.png" data-download-href="/uploads/short-url/wPhJm1yRuCXeK2YvGvAw6wFhIeo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e611b227c9c518fba20691dbe510f9d1b77948b4.png" alt="image" data-base62-sha1="wPhJm1yRuCXeK2YvGvAw6wFhIeo" width="542" height="362"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">542×362 69.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
