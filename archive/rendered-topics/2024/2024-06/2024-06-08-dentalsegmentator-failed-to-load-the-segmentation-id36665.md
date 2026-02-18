# DentalSegmentator failed to load the segmentation

**Topic ID**: 36665
**Date**: 2024-06-08
**URL**: https://discourse.slicer.org/t/dentalsegmentator-failed-to-load-the-segmentation/36665

---

## Post #1 by @karim_mamdouh (2024-06-08 23:37 UTC)

<p>Failed to load the segmentation.</p>
<p>Check the inference folder content C:\Users\Khateeb\AppData\Local\Temp\Slicer-iPdxkt\output</p>
<p>Operating system: windous 10<br>
Slicer version:5.7 latest<br>
Expected behavior:dentatl segmentator extension<br>
Actual behavior:not working</p>

---

## Post #2 by @jamesobutler (2024-06-08 23:59 UTC)

<p>SlicerDentalSegmentator developers, <a class="mention" href="/u/gauthier">@Gauthier</a> <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a>, can you help with this issue?</p>
<p>Also see</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator/issues/8">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/8" target="_blank" rel="noopener nofollow ugc">github.com/gaudot/SlicerDentalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/8" target="_blank" rel="noopener nofollow ugc">Failed to load the segmentation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-06-02" data-time="03:51:26" data-timezone="UTC">03:51AM - 02 Jun 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/dentistfrankchen" target="_blank" rel="noopener nofollow ugc">
          <img alt="dentistfrankchen" src="https://avatars.githubusercontent.com/u/56914624?v=4" class="onebox-avatar-inline" width="20" height="20">
          dentistfrankchen
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Now I am using the 5.7.0 32881 3d slicer with EC2 ubuntu 22.04.
When I try usin<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">g the cpu version of  torch(2.2.1),everything works fine. However, when I use cu118 version, I get this error: failed to load the segmentation. Check ...
This seems to be error with SlicerNNUnet(with segmentationlogic.py)
Can you guys have a look?
Thank you.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Thibault_Pelletier (2024-06-10 06:29 UTC)

<p>Hi <a class="mention" href="/u/karim_mamdouh">@karim_mamdouh</a>,</p>
<p>Thank you for your interest in our extension.<br>
Just a note : please avoid posting the same issue in different topics.</p>
<p>As mentioned in another topic, could you give us the log content when you experience this error?</p>
<p>The logs can be found by pressing the (i) button next to the apply button</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/126a9c1c5b97dcaeeff9384f6f3fdcbea6332d5f.png" alt="image" data-base62-sha1="2CV0iWoY7dKEMQG4JboEHrMdWuX" width="601" height="124"></p>

---

## Post #4 by @Mikhail_Lovygin (2024-07-31 14:08 UTC)

<p>Hello there!<br>
Recently I have installed Slicer 5.7.0-2024-06-01 as well as the DentalSegmentation extension and tried to use it on sample data available through Slicer (CBCTDentalSurgery). However I encountered the same problem as Karim did: “Failed to load segmentation”.<br>
<a class="mention" href="/u/gauthier">@Gauthier</a> <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a>, I’d be grateful for any help as this extension seems to do a great job in dental segmentation.</p>
<p>OS: Win10<br>
Slicer: Slicer 5.7.0-2024-06-01</p>
<p>The following is the log results:</p>
<blockquote>
<p>Blockquote<br>
2024/07/31 16:56:02.797 :: nnUNet is already installed (2.5.1) and compatible with requested version (nnunetv2).<br>
2024/07/31 16:56:11.852 :: Transferring volume to nnUNet in C:/Users/Михалыч/AppData/Local/Temp/Slicer-GbtAsy<br>
2024/07/31 16:56:14.722 :: Starting nnUNet with the following parameters:<br>
2024/07/31 16:56:14.722 ::<br>
2024/07/31 16:56:14.722 :: C:\ProgramData\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/Михалыч/AppData/Local/Temp/Slicer-GbtAsy/input -o C:/Users/Михалыч/AppData/Local/Temp/Slicer-GbtAsy/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cpu -chk checkpoint_final.pth --disable_tta<br>
2024/07/31 16:56:14.722 ::<br>
2024/07/31 16:56:14.722 :: JSON parameters :<br>
2024/07/31 16:56:14.722 :: {<br>
2024/07/31 16:56:14.722 ::     “folds”: “0”,<br>
2024/07/31 16:56:14.722 ::     “device”: “cuda”,<br>
2024/07/31 16:56:14.722 ::     “stepSize”: 0.5,<br>
2024/07/31 16:56:14.722 ::     “disableTta”: true,<br>
2024/07/31 16:56:14.722 ::     “nProcessPreprocessing”: 1,<br>
2024/07/31 16:56:14.722 ::     “nProcessSegmentationExport”: 1,<br>
2024/07/31 16:56:14.722 ::     “checkPointName”: “”,<br>
2024/07/31 16:56:14.722 ::     “modelPath”: {<br>
2024/07/31 16:56:14.722 ::         "<em>path": “C:\ProgramData\slicer.org\Slicer 5.7.0-2024-06-01\slicer.org\Extensions-32886\DentalSegmentator\lib\Slicer-5.7\qt-scripted-modules\Resources\ML”<br>
2024/07/31 16:56:14.722 ::     }<br>
2024/07/31 16:56:14.722 :: }<br>
2024/07/31 16:56:14.727 :: nnUNet preprocessing…<br>
2024/07/31 16:56:22.286 :: C:\ProgramData\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py:84: FutureWarning: You are using <code>torch.load</code> with <code>weights_only=False</code> (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See <a href="https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models" class="inline-onebox" rel="noopener nofollow ugc">pytorch/SECURITY.md at main · pytorch/pytorch · GitHub</a> for more details). In a future release, the default value for <code>weights_only</code> will be flipped to <code>True</code>. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via <code>torch.serialization.add_safe_globals</code>. We recommend you start setting <code>weights_only=True</code> for any use case where you don’t have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.<br>
2024/07/31 16:56:22.286 ::   checkpoint = torch.load(join(model_training_output_dir, f’fold</em>{f}', checkpoint_name),<br>
2024/07/31 16:56:24.111 :: C:\ProgramData\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\nnunetv2\utilities\plans_handling\plans_handler.py:37: UserWarning: Detected old nnU-Net plans format. Attempting to reconstruct network architecture parameters. If this fails, rerun nnUNetv2_plan_experiment for your dataset. If you use a custom architecture, please downgrade nnU-Net to the version you implemented this or update your implementation + plans.<br>
2024/07/31 16:56:24.111 ::   warnings.warn("Detected old nnU-Net plans format. Attempting to reconstruct network architecture "<br>
2024/07/31 16:56:35.836 :: Process SpawnProcess-16:<br>
2024/07/31 16:56:35.849 :: Traceback (most recent call last):<br>
2024/07/31 16:56:35.849 ::   File “C:\ProgramData\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
2024/07/31 16:56:36.016 :: #######################################################################<br>
2024/07/31 16:56:36.016 :: Please cite the following paper when using nnU-Net:<br>
2024/07/31 16:56:36.016 :: Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., &amp; Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.<br>
2024/07/31 16:56:36.016 :: #######################################################################<br>
2024/07/31 16:56:36.016 ::<br>
2024/07/31 16:56:36.016 :: perform_everything_on_device=True is only supported for cuda devices! Setting this to False<br>
2024/07/31 16:56:36.016 :: There are 1 cases in the source folder<br>
2024/07/31 16:56:36.016 :: I am process 0 out of 1 (max process ID is 0, we start counting with 0!)<br>
2024/07/31 16:56:36.016 :: There are 1 cases that I would like to predict<br>
2024/07/31 16:56:37.892 :: Loading inference results…<br>
2024/07/31 17:02:45.830 :: Error loading results :<br>
2024/07/31 17:02:45.830 :: Failed to load the segmentation.<br>
2024/07/31 17:02:45.830 :: Check the inference folder content C:\Users\Михалыч\AppData\Local\Temp\Slicer-GbtAsy\output</p>
</blockquote>

---
