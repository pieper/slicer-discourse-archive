---
topic_id: 40905
title: "Issues With Dentalsegmentator"
date: 2024-12-30
url: https://discourse.slicer.org/t/40905
---

# Issues with DentalSegmentator

**Topic ID**: 40905
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/issues-with-dentalsegmentator/40905

---

## Post #1 by @JuMaLe (2024-12-30 14:37 UTC)

<p>Hello to everybody! I tried to use DentalSegmentator but when I click on “Apply” the process get stock at the very beginning.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3990f69a96c41495c36ddf8065e8e5a7b0851682.png" data-download-href="/uploads/short-url/8dfNushopUfs5qF1qpvHMg5jXXk.png?dl=1" title="3D Slicer 5.7.0-2024-12-23 30_12_2024 11_29_33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3990f69a96c41495c36ddf8065e8e5a7b0851682_2_690x357.png" alt="3D Slicer 5.7.0-2024-12-23 30_12_2024 11_29_33" data-base62-sha1="8dfNushopUfs5qF1qpvHMg5jXXk" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3990f69a96c41495c36ddf8065e8e5a7b0851682_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3990f69a96c41495c36ddf8065e8e5a7b0851682_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3990f69a96c41495c36ddf8065e8e5a7b0851682.png 2x" data-dominant-color="DAD9D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer 5.7.0-2024-12-23 30_12_2024 11_29_33</span><span class="informations">1360×705 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3806dd49602ce4588610fe2b425af6ad4be71a81.png" data-download-href="/uploads/short-url/7ZDrBz16iEHfyyNDlkpazlvqsQV.png?dl=1" title="3D Slicer 5.7.0-2024-12-23 30_12_2024 11_29_50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3806dd49602ce4588610fe2b425af6ad4be71a81_2_690x357.png" alt="3D Slicer 5.7.0-2024-12-23 30_12_2024 11_29_50" data-base62-sha1="7ZDrBz16iEHfyyNDlkpazlvqsQV" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3806dd49602ce4588610fe2b425af6ad4be71a81_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3806dd49602ce4588610fe2b425af6ad4be71a81_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3806dd49602ce4588610fe2b425af6ad4be71a81.png 2x" data-dominant-color="DAD9D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer 5.7.0-2024-12-23 30_12_2024 11_29_50</span><span class="informations">1360×705 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>what I’m missing here?</p>

---

## Post #2 by @jamesobutler (2024-12-30 16:18 UTC)

<p>There is a known issue in a dependency of Dental Segmentator that has been problematic for about a month. The issue hasn’t been fixed as it is a third party developer that has been unresponsive to the reported bugs.</p>
<p>References to the dependency issue:</p>
<aside class="quote" data-post="1" data-topic="40793">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dr_drcadcam/48/78899_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dentalsegmentator-does-not-complete-on-slicer-5-7-0/40793">DentalSegmentator does not complete on Slicer 5.7.0</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Problem report for Slicer 5.7.0-2024-12-16 win-amd64: [please describe expected and actual behavior] 
[DEBUG][Qt] 18.12.2024 10:51:23  (unknown:0) - Session start time …: 20241218_105123 [DEBUG][Qt] 18.12.2024 10:51:23  (unknown:0) - Slicer version …: 5.7.0-2024-12-16 (revision 33157 / f711b40) win-amd64 - installed release [DEBUG][Qt]
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="40519">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dental-segmantator/40519">Dental segmantator</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I am trying the dental segmentator with the sample CBCT. During the package installation I got this error message. This is with the R33134 on Linux: 
Installing collected packages: connected-components-3d
Successfully installed connected-components-3d-3.21.0
ERROR: Ignored the following versions that require a different python version: 2.6.0 Requires-Python &lt;4,&gt;=3.10; 2.6.1 Requires-Python &lt;4,&gt;=3.10; 2.6.2 Requires-Python &lt;4,&gt;=3.10; 2.7.0 Requires-Python &lt;4,&gt;=3.10; 2.7.1 Requires-Python &lt;4,&gt;=3.1…
  </blockquote>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator/issues/21">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/21" target="_blank" rel="noopener nofollow ugc">github.com/gaudot/SlicerDentalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/21" target="_blank" rel="noopener nofollow ugc">DentalSegmentator doesnt work</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-26" data-time="17:49:37" data-timezone="UTC">05:49PM - 26 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/okoratum" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/83302553?v=4" class="onebox-avatar-inline" width="20" height="20">
          okoratum
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I was using 3D Slicer 5.7 2024-04-25 because it is the recommended version to wo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rk with blenderfordental software.

Today i tried to use dentalsegmentator and i get error of inference folder and doesnt segment.
So i uninstall the 3D Slicer completely and tried same version and lastest version and i get this error everytime, here is the log:

2024/11/26 19:41:35.182 :: Start nnUNet install with requirements : nnunetv2
2024/11/26 19:41:35.187 :: - Installing pandas...
2024/11/26 19:41:42.688 :: - Installing pillow&lt;10.1...
2024/11/26 19:41:47.118 :: - Installing nnunetv2 --no-deps...
2024/11/26 19:41:48.244 :: - Installing acvl-utils&lt;0.3,&gt;=0.2 --no-deps...
2024/11/26 19:41:48.964 :: - Installing batchgenerators --no-deps...
2024/11/26 19:41:49.915 :: - Installing scikit-image --no-deps...
2024/11/26 19:41:51.590 :: - Installing networkx&gt;=2.8 --no-deps...
2024/11/26 19:41:53.860 :: - Installing imageio&gt;=2.33 --no-deps...
2024/11/26 19:41:54.776 :: - Installing tifffile&gt;=2022.8.12 --no-deps...
2024/11/26 19:41:55.791 :: - Installing lazy-loader&gt;=0.4 --no-deps...
2024/11/26 19:41:56.504 :: - Installing scikit-learn --no-deps...
2024/11/26 19:41:59.316 :: - Installing joblib&gt;=1.2.0 --no-deps...
2024/11/26 19:42:00.224 :: - Installing threadpoolctl&gt;=3.1.0 --no-deps...
2024/11/26 19:42:01.059 :: - Installing future --no-deps...
2024/11/26 19:42:02.205 :: - Installing unittest2 --no-deps...
2024/11/26 19:42:03.207 :: - Installing argparse --no-deps...
2024/11/26 19:42:04.062 :: - Installing traceback2 --no-deps...
2024/11/26 19:42:04.816 :: - Installing linecache2 --no-deps...
2024/11/26 19:42:05.546 :: - Installing connected-components-3d --no-deps...
2024/11/26 19:42:06.328 :: - Installing blosc2&gt;=3.0.0b4 --no-deps...
2024/11/26 19:42:07.080 :: Install returned non-zero exit status : Command '['C:/Users/PC/AppData/Local/slicer.org/Slicer 5.7.0-2024-11-25/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'blosc2&gt;=3.0.0b4', '--no-deps']' returned non-zero exit status 1.. Attempting to continue...
2024/11/26 19:42:07.085 :: Error occurred during install : blosc2

I pressed apply again in hope it will fix itself and i am stuck at download model weights for a while.

I restarted the app and installed pytorch compatible with my gpu in pytorchutils extension and run the extension again and then i got different error, here is the log:

2024/11/26 20:01:45.238 :: nnUNet is already installed (2.5.1) and compatible with requested version (nnunetv2).
2024/11/26 20:01:48.296 :: Transferring volume to nnUNet in C:/Users/PC/AppData/Local/Temp/Slicer-RuOTvc
2024/11/26 20:02:06.380 :: Starting nnUNet with the following parameters:
2024/11/26 20:02:06.380 :: 
2024/11/26 20:02:06.380 :: C:\Users\PC\AppData\Local\slicer.org\Slicer 5.7.0-2024-11-25\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/PC/AppData/Local/Temp/Slicer-RuOTvc/input -o C:/Users/PC/AppData/Local/Temp/Slicer-RuOTvc/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta
2024/11/26 20:02:06.380 :: 
2024/11/26 20:02:06.380 :: JSON parameters :
2024/11/26 20:02:06.380 :: {
2024/11/26 20:02:06.380 ::     "folds": "0",
2024/11/26 20:02:06.380 ::     "device": "cuda",
2024/11/26 20:02:06.380 ::     "stepSize": 0.5,
2024/11/26 20:02:06.380 ::     "disableTta": true,
2024/11/26 20:02:06.380 ::     "nProcessPreprocessing": 1,
2024/11/26 20:02:06.380 ::     "nProcessSegmentationExport": 1,
2024/11/26 20:02:06.380 ::     "checkPointName": "",
2024/11/26 20:02:06.380 ::     "modelPath": {
2024/11/26 20:02:06.380 ::         "_path": "C:\\Users\\PC\\AppData\\Local\\slicer.org\\Slicer 5.7.0-2024-11-25\\slicer.org\\Extensions-33123\\DentalSegmentator\\lib\\Slicer-5.7\\qt-scripted-modules\\Resources\\ML"
2024/11/26 20:02:06.380 ::     }
2024/11/26 20:02:06.380 :: }
2024/11/26 20:02:06.405 :: nnUNet preprocessing...
2024/11/26 20:02:08.233 :: Traceback (most recent call last):
2024/11/26 20:02:08.233 ::   File "C:\Users\PC\AppData\Local\slicer.org\Slicer 5.7.0-2024-11-25\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
2024/11/26 20:02:08.234 :: return _run_code(code, main_globals, None,
2024/11/26 20:02:08.234 ::   File "C:\Users\PC\AppData\Local\slicer.org\Slicer 5.7.0-2024-11-25\lib\Python\Lib\runpy.py", line 87, in _run_code
2024/11/26 20:02:08.234 ::     exec(code, run_globals)
2024/11/26 20:02:08.234 ::   File "C:\Users\PC\AppData\Local\slicer.org\Slicer 5.7.0-2024-11-25\lib\Python\Scripts\nnUNetv2_predict.exe\__main__.py", line 4, in &lt;module&gt;
2024/11/26 20:02:08.234 ::   File "C:\Users\PC\AppData\Local\slicer.org\Slicer 5.7.0-2024-11-25\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 18, in &lt;module&gt;
2024/11/26 20:02:08.234 ::     from tqdm import tqdm
2024/11/26 20:02:08.234 :: ModuleNotFoundError: No module named 'tqdm'
2024/11/26 20:02:08.469 :: Loading inference results...
2024/11/26 20:02:10.316 :: Error loading results :
2024/11/26 20:02:10.316 :: Failed to load the segmentation.
2024/11/26 20:02:10.316 :: Something went wrong during the nnUNet processing.
2024/11/26 20:02:10.316 :: Please check the logs for potential errors and contact the library maintainers.

My PC Specs:

Windows 11
Ryzen 7 7700X
32GB Ram
RTX 4070</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
