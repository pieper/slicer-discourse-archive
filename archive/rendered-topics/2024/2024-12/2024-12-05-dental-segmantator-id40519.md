# Dental segmantator

**Topic ID**: 40519
**Date**: 2024-12-05
**URL**: https://discourse.slicer.org/t/dental-segmantator/40519

---

## Post #1 by @muratmaga (2024-12-05 02:30 UTC)

<p>I am trying the dental segmentator with the sample CBCT. During the package installation I got this error message. This is with the R33134 on Linux:</p>
<pre><code class="lang-auto">Installing collected packages: connected-components-3d
Successfully installed connected-components-3d-3.21.0
ERROR: Ignored the following versions that require a different python version: 2.6.0 Requires-Python &lt;4,&gt;=3.10; 2.6.1 Requires-Python &lt;4,&gt;=3.10; 2.6.2 Requires-Python &lt;4,&gt;=3.10; 2.7.0 Requires-Python &lt;4,&gt;=3.10; 2.7.1 Requires-Python &lt;4,&gt;=3.10; 3.0.0b1 Requires-Python &gt;=3.10
ERROR: Could not find a version that satisfies the requirement blosc2&gt;=3.0.0b4 (from versions: 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9, 0.1.10, 0.2.0, 0.3.0, 0.3.1, 0.3.2, 0.4.0, 0.4.1, 0.5.1, 0.5.2, 0.6.1, 0.6.2, 0.6.3, 0.6.4, 0.6.5, 0.6.6, 2.0.0, 2.1.0, 2.1.1, 2.2.0, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 2.2.7, 2.2.8, 2.2.9, 2.3.0, 2.3.1, 2.3.2, 2.4.0, 2.5.0, 2.5.1)
ERROR: No matching distribution found for blosc2&gt;=3.0.0b4
</code></pre>

---

## Post #2 by @jamesobutler (2024-12-05 05:08 UTC)

<p>This seems to match existing report at which has some workarounds mentioned:</p>
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
          <img alt="okoratum" src="https://avatars.githubusercontent.com/u/83302553?v=4" class="onebox-avatar-inline" width="20" height="20">
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

<p>Where <code>acvl_utils</code> a dependency of nnUNet has a caused a dependency issue again. This time due to this commit:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/MIC-DKFZ/acvl_utils/commit/4cad0deb89dc97b6f4ecfdfd553b994bee076274">
  <header class="source">

      <a href="https://github.com/MIC-DKFZ/acvl_utils/commit/4cad0deb89dc97b6f4ecfdfd553b994bee076274" target="_blank" rel="noopener nofollow ugc">github.com/MIC-DKFZ/acvl_utils</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/MIC-DKFZ/acvl_utils/commit/4cad0deb89dc97b6f4ecfdfd553b994bee076274" target="_blank" rel="noopener nofollow ugc">bump version, add blosc2 dependency</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-11-12" data-time="11:45:44" data-timezone="UTC">11:45AM - 12 Nov 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/FabianIsensee" target="_blank" rel="noopener nofollow ugc">
          <img alt="FabianIsensee" src="https://avatars.githubusercontent.com/u/11302164?v=4" class="onebox-avatar-inline" width="20" height="20">
          FabianIsensee
        </a>
      </div>

      <div class="lines" title="changed 3 files with 24 additions and 2 deletions">
        <a href="https://github.com/MIC-DKFZ/acvl_utils/commit/4cad0deb89dc97b6f4ecfdfd553b994bee076274" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+24</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Appears to similarly impact TotalSegmentator which uses nnUNet.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/385#issuecomment-2486230801">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/385#issuecomment-2486230801" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/385#issuecomment-2486230801" target="_blank" rel="noopener nofollow ugc">ModuleNotFoundError: No module named 'blosc2'</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-07" data-time="22:41:29" data-timezone="UTC">10:41PM - 07 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/ASHISRAVINDRAN" target="_blank" rel="noopener nofollow ugc">
          <img alt="ASHISRAVINDRAN" src="https://avatars.githubusercontent.com/u/33703127?v=4" class="onebox-avatar-inline" width="20" height="20">
          ASHISRAVINDRAN
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hi @wasserth
I am from the MITK development team working to update TotalSegment<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ator to v2.4 for our upcoming release.
I am testing out installing TotalSegmentator via MITK and I see that TotalSegmentator has stopped working due to import errors.
Error log:

```
Traceback (most recent call last):
  File "&lt;frozen runpy&gt;", line 198, in _run_module_as_main
  File "&lt;frozen runpy&gt;", line 88, in _run_code
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 138, in main
    totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\totalsegmentator\python_api.py", line 126, in totalsegmentator
    from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\totalsegmentator\nnunet.py", line 30, in &lt;module&gt;
    from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 22, in &lt;module&gt;
    from nnunetv2.inference.data_iterators import PreprocessAdapterFromNpy, preprocessing_iterator_fromfiles, \
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\nnunetv2\inference\data_iterators.py", line 12, in &lt;module&gt;
    from nnunetv2.preprocessing.preprocessors.default_preprocessor import DefaultPreprocessor
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\nnunetv2\preprocessing\preprocessors\default_preprocessor.py", line 25, in &lt;module&gt;
    from nnunetv2.preprocessing.cropping.cropping import crop_to_nonzero
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\nnunetv2\preprocessing\cropping\cropping.py", line 5, in &lt;module&gt;
    from acvl_utils.cropping_and_padding.bounding_boxes import get_bbox_from_mask, crop_to_bbox, bounding_box_to_slice
  File "C:\DKFZ\TotalSegmentator_work\.venv_7Nov\Lib\site-packages\acvl_utils\cropping_and_padding\bounding_boxes.py", line 5, in &lt;module&gt;
    import blosc2
ModuleNotFoundError: No module named 'blosc2'
```
Merely pip installing `blosc2` leads to even more import errors. 
It would be great if you can take a look.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2024-12-05 05:22 UTC)

<p>I’ve submitted an issue to <code>acvl_utils</code> to work to fix the dependency issue.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/MIC-DKFZ/acvl_utils/issues/4">
  <header class="source">

      <a href="https://github.com/MIC-DKFZ/acvl_utils/issues/4" target="_blank" rel="noopener nofollow ugc">github.com/MIC-DKFZ/acvl_utils</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/MIC-DKFZ/acvl_utils/issues/4" target="_blank" rel="noopener nofollow ugc">Install unable to find blosc2 dependency for Python 3.9</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-12-05" data-time="05:20:14" data-timezone="UTC">05:20AM - 05 Dec 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">@FabianIsensee The introduction of blosc2 and the version specified in https://g<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ithub.com/MIC-DKFZ/acvl_utils/commit/4cad0deb89dc97b6f4ecfdfd553b994bee076274 does not have support for Python 3.9 even though nnUNet specifies it supports Python 3.9.

At minimum could you update this package to explicitly state the `python_requires` in setup.py so that pip can better manage dependencies? See https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py#L123 

See how this has impacted TotalSegmentator again as mentioned at https://github.com/wasserth/TotalSegmentator/issues/385#issuecomment-2486230801.

Example of dependency handling failing at time of install.
```
ERROR: Ignored the following versions that require a different python version: 2.6.0 Requires-Python &lt;4,&gt;=3.10; 2.6.1 Requires-Python &lt;4,&gt;=3.10; 2.6.2 Requires-Python &lt;4,&gt;=3.10; 2.7.0 Requires-Python &lt;4,&gt;=3.10; 2.7.1 Requires-Python &lt;4,&gt;=3.10; 3.0.0b1 Requires-Python &gt;=3.10
ERROR: Could not find a version that satisfies the requirement blosc2&gt;=3.0.0b4 (from versions: 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.1.9, 0.1.10, 0.2.0, 0.3.0, 0.3.1, 0.3.2, 0.4.0, 0.4.1, 0.5.1, 0.5.2, 0.6.1, 0.6.2, 0.6.3, 0.6.4, 0.6.5, 0.6.6, 2.0.0, 2.1.0, 2.1.1, 2.2.0, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 2.2.7, 2.2.8, 2.2.9, 2.3.0, 2.3.1, 2.3.2, 2.4.0, 2.5.0, 2.5.1)
ERROR: No matching distribution found for blosc2&gt;=3.0.0b4
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
