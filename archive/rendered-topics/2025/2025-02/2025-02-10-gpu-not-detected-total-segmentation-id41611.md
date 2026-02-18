# GPU not detected Total Segmentation

**Topic ID**: 41611
**Date**: 2025-02-10
**URL**: https://discourse.slicer.org/t/gpu-not-detected-total-segmentation/41611

---

## Post #1 by @Caterina (2025-02-10 20:38 UTC)

<p>Dear support,<br>
I’m using TotalSegmentator on a desktop pc with the following hardware features:<br>
Processore: 3,2 GHz Intel Xeon W 16 core<br>
Scheda video: AMD Radeon Pro Vega II 32 GB<br>
Ram: 384 GB 2933 MHz DDR4<br>
Mac OS:  Sequoia 15.1.1 (24B91).</p>
<p>No gpu was detected when we apply totalSegmentation. We have two questions about this question:</p>
<ol>
<li>There is a way to use our GPU or to fix this issue in MacOs environment?</li>
<li>We have a desktop pc with the same features in a Windows environment. Is there a simpler solution for this environment?<br>
Thanks</li>
</ol>

---

## Post #2 by @jamesobutler (2025-02-10 21:06 UTC)

<p><a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator</a> appears to have added the option for MPS where your Mac Pro AMD Radeon Pro Vega II card supports the <a href="https://pytorch.org/docs/stable/notes/mps.html" rel="noopener nofollow ugc">mps</a> backend for PyTorch.</p>
<p>It does seem to be a bit on the untested and new side as the following place in the readme hasn’t been updated to reflect the mps option although you can see that <code>--device</code> does allow the “mps” option.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/README.md?plain=1#L106">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/README.md?plain=1#L106" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/README.md?plain=1#L106" target="_blank" rel="noopener nofollow ugc">README.md?plain=1</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/README.md?plain=1#L106" rel="noopener nofollow ugc"><code>7bceedf0e</code></a>
</div>



    <pre class="onebox"><code class="lang-md?plain=1">
      <ol class="start lines" start="96" style="counter-reset: li-counter 95 ;">
          <li>```</li>
          <li>TotalSegmentator -i ct.nii.gz -o segmentations -ta &lt;task_name&gt;</li>
          <li>```</li>
          <li></li>
          <li>Confused by all the structures and tasks? Check [this](https://backend.totalsegmentator.com/find-task/) to search through available structures and tasks.</li>
          <li></li>
          <li>The mapping from label ID to class name can be found [here](https://github.com/wasserth/TotalSegmentator/blob/master/totalsegmentator/map_to_binary.py).</li>
          <li></li>
          <li></li>
          <li>### Advanced settings</li>
          <li class="selected">* `--device`: Choose `cpu` or `gpu` or `gpu:X (e.g., gpu:1 -&gt; cuda:1)`</li>
          <li>* `--fast`: For faster runtime and less memory requirements use this option. It will run a lower resolution model (3mm instead of 1.5mm).</li>
          <li>* `--roi_subset`: Takes a space-separated list of class names (e.g. `spleen colon brain`) and only predicts those classes. Saves a lot of runtime and memory. Might be less accurate especially for small classes (e.g. prostate).</li>
          <li>* `--preview`: This will generate a 3D rendering of all classes, giving you a quick overview if the segmentation worked and where it failed (see `preview.png` in output directory).</li>
          <li>* `--ml`: This will save one nifti file containing all labels instead of one file for each class. Saves runtime during saving of nifti files. (see [here](https://github.com/wasserth/TotalSegmentator#class-details) for index to class name mapping).</li>
          <li>* `--statistics`: This will generate a file `statistics.json` with volume (in mm³) and mean intensity of each class.</li>
          <li>* `--radiomics`: This will generate a file `statistics_radiomics.json` with the radiomics features of each class. You have to install pyradiomics to use this (`pip install pyradiomics`).</li>
          <li></li>
          <li></li>
          <li>### Other commands</li>
          <li>If you want to know which contrast phase a CT image is you can use the following command (requires `pip install xgboost`). More details can be found [here](resources/contrast_phase_prediction.md):</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubblob" data-onebox-src="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/totalsegmentator/bin/TotalSegmentator.py#L115-L119">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/totalsegmentator/bin/TotalSegmentator.py#L115-L119" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/totalsegmentator/bin/TotalSegmentator.py#L115-L119" target="_blank" rel="noopener nofollow ugc">totalsegmentator/bin/TotalSegmentator.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/wasserth/TotalSegmentator/blob/7bceedf0e0f3f1e4a419c9592ee1e4dc960e73bd/totalsegmentator/bin/TotalSegmentator.py#L115-L119" rel="noopener nofollow ugc"><code>7bceedf0e</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="115" style="counter-reset: li-counter 114 ;">
          <li># "mps" is for apple silicon; the latest pytorch nightly version supports 3D Conv but not ConvTranspose3D which is</li>
          <li># also needed by nnU-Net. So "mps" not working for now.</li>
          <li># https://github.com/pytorch/pytorch/issues/77818</li>
          <li>parser.add_argument("-d",'--device', type=validate_device_type, default="gpu",</li>
          <li>                    help="Device type: 'gpu', 'cpu', 'mps', or 'gpu:X' where X is an integer representing the GPU device ID.")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The SlicerTotalSegmentator utilizes the TotalSegmentator python package, but will need to be updated to handle the MPS option as right now if it doesn’t detect a CUDA compatible GPU it will use CPU. See the following code that would need to be updated.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/c9dc3cf479a6463d3d17ca40b66de18156d06247/TotalSegmentator/TotalSegmentator.py#L952">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/c9dc3cf479a6463d3d17ca40b66de18156d06247/TotalSegmentator/TotalSegmentator.py#L952" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/c9dc3cf479a6463d3d17ca40b66de18156d06247/TotalSegmentator/TotalSegmentator.py#L952" target="_blank" rel="noopener nofollow ugc">TotalSegmentator/TotalSegmentator.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/c9dc3cf479a6463d3d17ca40b66de18156d06247/TotalSegmentator/TotalSegmentator.py#L952" rel="noopener nofollow ugc"><code>c9dc3cf47</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="942" style="counter-reset: li-counter 941 ;">
          <li>tempFolder = slicer.util.tempDirectory()</li>
          <li></li>
          <li>inputFile = tempFolder+"/total-segmentator-input.nii"</li>
          <li>outputSegmentationFolder = tempFolder + "/segmentation"</li>
          <li># print (outputSegmentationFolder)</li>
          <li>outputSegmentationFile = tempFolder + "/segmentation.nii"</li>
          <li></li>
          <li># Recommend the user to switch to fast mode if no GPU or not enough memory is available</li>
          <li>import torch</li>
          <li></li>
          <li class="selected">cuda = torch.cuda if torch.backends.cuda.is_built() and torch.cuda.is_available() else None</li>
          <li></li>
          <li>if not fast and not cuda and interactive:</li>
          <li></li>
          <li>    import ctk</li>
          <li>    import qt</li>
          <li>    mbox = ctk.ctkMessageBox(slicer.util.mainWindow())</li>
          <li>    mbox.text = "No GPU is detected. Switch to 'fast' mode to get low-resolution result in a few minutes or compute full-resolution result which may take 5 to 50 minutes (depending on computer configuration)?"</li>
          <li>    mbox.addButton("Fast (~2 minutes)", qt.QMessageBox.AcceptRole)</li>
          <li>    mbox.addButton("Full-resolution (~5 to 50 minutes)", qt.QMessageBox.RejectRole)</li>
          <li>    # Windows 10 peek feature in taskbar shows all hidden but not destroyed windows</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It appears that the MPS backend for PyTorch originally came out for PyTorch 2 with fixes and improvements over time. Since you are on an Intel Mac, you will be stuck on PyTorch 2.2.x as the latest since developers dropped support for it and were instead only going to support macOS on Apple Silicon.</p>
<p>Would you be willing to complete the code changes for SlicerTotalSegmentator and update the documentation for the TotalSegmentator package for your MPS use case? A majority of Slicer users are on Windows, so there has been less of a need for macOS specific tasks. Alternatively, a Windows machine with a CUDA enabled driver would be the easiest environment to immediately begin using.</p>

---

## Post #3 by @Caterina (2025-02-11 14:23 UTC)

<p>Thanks a lot for reply. Considering the case of desktop pc with the mentioned hardware features, it is possible to use our GPU with an emulator or other alternative that enables to detect Cuda-compatible GPU and to perform total segmentator with default CONFIGURATION ( NO FORCE CPU)?<br>
THANKS</p>

---

## Post #4 by @jamesobutler (2025-02-12 04:18 UTC)

<p>You could probably use your GPU if you switched from macOS to Linux and then used the ROCm variant of PyTorch, but you are going down the even more less commonly used pathway.</p>
<p>PyTorch is heavily focused on Nvidia GPUs or using the MPS backend on macOS.</p>

---
