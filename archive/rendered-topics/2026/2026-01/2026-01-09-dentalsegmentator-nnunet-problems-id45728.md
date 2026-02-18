# DentalSegmentator / nnUNet problems

**Topic ID**: 45728
**Date**: 2026-01-09
**URL**: https://discourse.slicer.org/t/dentalsegmentator-nnunet-problems/45728

---

## Post #1 by @Aiden (2026-01-09 20:45 UTC)

<p>I’m having troubles with DentalSegmentator.</p>
<p>3D Slicer 5.10.0</p>
<p>The log:</p>
<pre><code class="lang-auto">2026/01/09 16:28:19.241 :: Start nnUNet install with requirements : nnunetv2

2026/01/09 16:28:19.280 :: - Installing nnunetv2 --no-deps...

2026/01/09 16:28:20.152 :: - Installing acvl-utils&lt;0.3,&gt;=0.2.3 --no-deps...

2026/01/09 16:28:20.797 :: - Installing batchgenerators --no-deps...

2026/01/09 16:28:21.471 :: - Installing scikit-image --no-deps...

2026/01/09 16:28:22.708 :: - Installing networkx&gt;=3.0 --no-deps...

2026/01/09 16:28:24.741 :: - Installing imageio!=2.35.0,&gt;=2.33 --no-deps...

2026/01/09 16:28:25.673 :: - Installing tifffile&gt;=2022.8.12 --no-deps...

2026/01/09 16:28:26.624 :: - Installing lazy-loader&gt;=0.4 --no-deps...

2026/01/09 16:28:27.257 :: - Installing scikit-learn --no-deps...

2026/01/09 16:28:30.490 :: - Installing joblib&gt;=1.3.0 --no-deps...

2026/01/09 16:28:31.342 :: - Installing threadpoolctl&gt;=3.2.0 --no-deps...

2026/01/09 16:28:32.032 :: - Installing future --no-deps...

2026/01/09 16:28:33.048 :: - Installing pandas --no-deps...

2026/01/09 16:28:39.524 :: - Installing pytz&gt;=2020.1 --no-deps...

2026/01/09 16:28:40.498 :: - Installing tzdata&gt;=2022.7 --no-deps...

2026/01/09 16:28:41.296 :: - Installing unittest2 --no-deps...

2026/01/09 16:28:42.123 :: - Installing argparse --no-deps...

2026/01/09 16:28:42.771 :: - Installing traceback2 --no-deps...

2026/01/09 16:28:43.422 :: - Installing linecache2 --no-deps...

2026/01/09 16:28:44.108 :: - Installing connected-components-3d --no-deps...

2026/01/09 16:28:45.016 :: - Installing blosc2&gt;=3.0.0b4 --no-deps...

2026/01/09 16:28:46.027 :: - Installing ndindex --no-deps...

2026/01/09 16:28:46.870 :: - Installing msgpack --no-deps...

2026/01/09 16:28:47.632 :: - Installing platformdirs --no-deps...

2026/01/09 16:28:48.302 :: - Installing numexpr&gt;=2.14.1 --no-deps...

2026/01/09 16:28:49.147 :: - Installing py-cpuinfo --no-deps...

2026/01/09 16:28:49.795 :: - Installing dynamic-network-architectures&lt;0.5,&gt;=0.4.1 --no-deps...

2026/01/09 16:28:50.504 :: - Installing timm --no-deps...

2026/01/09 16:28:52.209 :: - Installing pyyaml --no-deps...

2026/01/09 16:28:52.982 :: - Installing huggingface_hub --no-deps...

2026/01/09 16:28:54.416 :: - Installing filelock --no-deps...

2026/01/09 16:28:55.094 :: - Installing fsspec&gt;=2023.5.0 --no-deps...

2026/01/09 16:28:56.339 :: - Installing hf-xet&lt;2.0.0,&gt;=1.2.0 --no-deps...

2026/01/09 16:28:57.376 :: - Installing httpx&lt;1,&gt;=0.23.0 --no-deps...

2026/01/09 16:28:58.164 :: - Installing anyio --no-deps...

2026/01/09 16:28:59.029 :: - Installing httpcore==1.* --no-deps...

2026/01/09 16:28:59.757 :: - Installing h11&gt;=0.16 --no-deps...

2026/01/09 16:29:00.402 :: - Installing shellingham --no-deps...

2026/01/09 16:29:01.058 :: - Installing tqdm&gt;=4.42.1 --no-deps...

2026/01/09 16:29:01.811 :: - Installing typer-slim --no-deps...

2026/01/09 16:29:02.559 :: - Installing click&gt;=8.0.0 --no-deps...

2026/01/09 16:29:03.422 :: - Installing safetensors --no-deps...

2026/01/09 16:29:04.323 :: - Installing einops --no-deps...

2026/01/09 16:29:05.062 :: - Installing graphviz --no-deps...

2026/01/09 16:29:05.774 :: - Installing nibabel --no-deps...

2026/01/09 16:29:07.017 :: - Installing matplotlib --no-deps...

2026/01/09 16:29:09.733 :: - Installing contourpy&gt;=1.0.1 --no-deps...

2026/01/09 16:29:10.556 :: - Installing cycler&gt;=0.10 --no-deps...

2026/01/09 16:29:11.222 :: - Installing fonttools&gt;=4.22.0 --no-deps...

2026/01/09 16:29:13.174 :: - Installing kiwisolver&gt;=1.3.1 --no-deps...

2026/01/09 16:29:14.164 :: - Installing seaborn --no-deps...

2026/01/09 16:29:15.420 :: - Installing imagecodecs --no-deps...

2026/01/09 16:29:16.928 :: - Installing yacs --no-deps...

2026/01/09 16:29:17.890 :: - Installing batchgeneratorsv2&gt;=0.3.0 --no-deps...

2026/01/09 16:29:18.850 :: - Installing fft-conv-pytorch --no-deps...

2026/01/09 16:29:19.577 :: PyTorch Python package is required. Installing... (it may take several minutes)

2026/01/09 16:29:48.294 :: nnUNet installation completed successfully.

2026/01/09 16:29:48.311 :: Downloading model weights...

2026/01/09 16:29:57.551 :: Transferring volume to nnUNet in /tmp/Slicer-eSDRuj

2026/01/09 16:30:11.062 :: Starting nnUNet with the following parameters:

2026/01/09 16:30:11.062 ::

2026/01/09 16:30:11.062 :: /home/user/Slicer-5.10.0-linux-amd64/lib/Python/bin/nnUNetv2_predict -i /tmp/Slicer-eSDRuj/input -o /tmp/Slicer-eSDRuj/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cpu -chk checkpoint_final.pth --disable_tta

2026/01/09 16:30:11.062 ::

2026/01/09 16:30:11.062 :: JSON parameters :

2026/01/09 16:30:11.062 :: {

2026/01/09 16:30:11.062 :: "folds": "0",

2026/01/09 16:30:11.062 :: "device": "cpu",

2026/01/09 16:30:11.062 :: "stepSize": 0.5,

2026/01/09 16:30:11.062 :: "disableTta": true,

2026/01/09 16:30:11.062 :: "nProcessPreprocessing": 1,

2026/01/09 16:30:11.062 :: "nProcessSegmentationExport": 1,

2026/01/09 16:30:11.062 :: "checkPointName": "",

2026/01/09 16:30:11.062 :: "modelPath": {

2026/01/09 16:30:11.062 :: "_path": "/home/user/Slicer-5.10.0-linux-amd64/slicer.org/Extensions-34045/DentalSegmentator/lib/Slicer-5.10/qt-scripted-modules/Resources/ML"

2026/01/09 16:30:11.062 :: }

2026/01/09 16:30:11.062 :: }

2026/01/09 16:30:12.469 :: nnUNet preprocessing...

2026/01/09 16:30:16.804 :: /home/user/Slicer-5.10.0-linux-amd64/lib/Python/lib/python3.12/site-packages/nnunetv2/utilities/plans_handling/plans_handler.py:37: UserWarning: Detected old nnU-Net plans format. Attempting to reconstruct network architecture parameters. If this fails, rerun nnUNetv2_plan_experiment for your dataset. If you use a custom architecture, please downgrade nnU-Net to the version you implemented this or update your implementation + plans.

2026/01/09 16:30:16.804 :: warnings.warn("Detected old nnU-Net plans format. Attempting to reconstruct network architecture "

2026/01/09 16:30:18.304 :: #######################################################################

2026/01/09 16:30:18.304 :: Please cite the following paper when using nnU-Net:

2026/01/09 16:30:18.304 :: Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., &amp; Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

2026/01/09 16:30:18.304 :: #######################################################################

2026/01/09 16:30:18.304 ::

2026/01/09 16:30:18.304 :: perform_everything_on_device=True is only supported for cuda devices! Setting this to False

2026/01/09 16:30:18.538 :: There are 1 cases in the source folder

2026/01/09 16:30:18.538 :: I am processing 0 out of 1 (max process ID is 0, we start counting with 0!)

2026/01/09 16:30:18.538 :: There are 1 cases that I would like to predict

2026/01/09 16:31:10.971 :: Traceback (most recent call last):

2026/01/09 16:31:10.971 :: File "/home/user/Slicer-5.10.0-linux-amd64/lib/Python/bin/nnUNetv2_predict", line 8, in &lt;module&gt;

2026/01/09 16:31:14.232 :: Loading inference results...

2026/01/09 16:31:17.081 :: Error loading results :

2026/01/09 16:31:17.081 :: Failed to load the segmentation.

2026/01/09 16:31:17.081 :: Something went wrong during the nnUNet processing.

2026/01/09 16:31:17.081 :: Please check the logs for potential errors and contact the library maintainers.
</code></pre>

---

## Post #2 by @Aiden (2026-01-09 22:49 UTC)

<p>I tried to remove as many 3D Slicer related files from my computer and re installed it along with DentalSegmentator. Now my issue is that it says this infinitely:</p>
<p><code>nnUNet is already installed (2.6.2) and compatible with requested version (nnunetv2).</code></p>

---

## Post #3 by @amyers (2026-01-12 13:19 UTC)

<p>You have another nnUNet installation on your system, probably python is my guess. Are you using nnUNet for anything else? If not, these steps should clear up your problem:</p>
<ol>
<li>From The Extensions Manager, Uninstall Dental Segmentator, NNUNet, and any other Segmentator Extensions.</li>
<li>Close 3D Slicer</li>
<li>Then open Powershell as admin and run the command: python -m pip uninstall nnunet.</li>
<li>Run:  Find-Package -Name nnunet</li>
<li>If nothing shows up for nnunet packages, re-install Dental Segmentator and try again.</li>
</ol>

---

## Post #4 by @Romulo_Alfaro (2026-01-12 15:35 UTC)

<p>Has anyone tried this and had it work? I couldn’t fix it and had to revert to the previous version of Slicer, 5.8.</p>

---

## Post #5 by @lassoan (2026-01-12 17:08 UTC)

<p>It works well for me on Windows:</p>
<pre><code class="lang-auto">2026/01/12 11:55:45.742 :: nnUNet is already installed (2.6.2) and compatible with requested version (nnunetv2).
2026/01/12 11:55:45.750 :: Downloading model weights...
2026/01/12 11:56:03.416 :: Transferring volume to nnUNet in C:/Users/andra/AppData/Local/Temp/Slicer-daAwew
2026/01/12 11:56:04.283 :: Starting nnUNet with the following parameters:
2026/01/12 11:56:04.283 :: 
2026/01/12 11:56:04.283 :: C:\Users\andra\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/andra/AppData/Local/Temp/Slicer-daAwew/input -o C:/Users/andra/AppData/Local/Temp/Slicer-daAwew/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta
2026/01/12 11:56:04.283 :: 
2026/01/12 11:56:04.283 :: JSON parameters :
2026/01/12 11:56:04.283 :: {
2026/01/12 11:56:04.283 ::     "folds": "0",
2026/01/12 11:56:04.283 ::     "device": "cuda",
2026/01/12 11:56:04.283 ::     "stepSize": 0.5,
2026/01/12 11:56:04.283 ::     "disableTta": true,
2026/01/12 11:56:04.283 ::     "nProcessPreprocessing": 1,
2026/01/12 11:56:04.283 ::     "nProcessSegmentationExport": 1,
2026/01/12 11:56:04.283 ::     "checkPointName": "",
2026/01/12 11:56:04.283 ::     "modelPath": {
2026/01/12 11:56:04.283 ::         "_path": "C:\\Users\\andra\\AppData\\Local\\slicer.org\\3D Slicer 5.10.0\\slicer.org\\Extensions-34045\\DentalSegmentator\\lib\\Slicer-5.10\\qt-scripted-modules\\Resources\\ML"
2026/01/12 11:56:04.283 ::     }
2026/01/12 11:56:04.283 :: }
2026/01/12 11:56:04.312 :: nnUNet preprocessing...
2026/01/12 11:56:19.029 :: C:\Users\andra\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\nnunetv2\utilities\plans_handling\plans_handler.py:37: UserWarning: Detected old nnU-Net plans format. Attempting to reconstruct network architecture parameters. If this fails, rerun nnUNetv2_plan_experiment for your dataset. If you use a custom architecture, please downgrade nnU-Net to the version you implemented this or update your implementation + plans.
2026/01/12 11:56:19.029 ::   warnings.warn("Detected old nnU-Net plans format. Attempting to reconstruct network architecture "
2026/01/12 11:57:07.486 :: #######################################################################
2026/01/12 11:57:07.486 :: Please cite the following paper when using nnU-Net:
2026/01/12 11:57:07.486 :: Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., &amp; Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.
2026/01/12 11:57:07.486 :: #######################################################################
2026/01/12 11:57:07.486 :: 
2026/01/12 11:57:07.486 :: There are 1 cases in the source folder
2026/01/12 11:57:07.486 :: I am processing 0 out of 1 (max process ID is 0, we start counting with 0!)
2026/01/12 11:57:07.486 :: There are 1 cases that I would like to predict
2026/01/12 11:57:07.486 :: 
2026/01/12 11:57:07.486 :: Predicting volume:
2026/01/12 11:57:07.486 :: perform_everything_on_device: True
2026/01/12 11:57:07.486 :: 0%|          | 0/210 [00:00&lt;?, ?it/s]
2026/01/12 11:57:08.566 :: 0%|          | 1/210 [00:01&lt;03:45,  1.08s/it]
2026/01/12 11:57:08.790 :: 1%|          | 2/210 [00:01&lt;01:59,  1.74it/s]
2026/01/12 11:57:09.119 :: 1%|1         | 3/210 [00:01&lt;01:35,  2.16it/s]
2026/01/12 11:57:09.261 :: 2%|1         | 4/210 [00:01&lt;01:09,  2.97it/s]
...
2026/01/12 11:57:36.607 :: 99%|#########8| 207/210 [00:29&lt;00:00,  7.33it/s]
2026/01/12 11:57:36.742 :: 99%|#########9| 208/210 [00:29&lt;00:00,  7.37it/s]
2026/01/12 11:57:36.882 :: 100%|#########9| 209/210 [00:29&lt;00:00,  7.30it/s]
2026/01/12 11:57:37.009 :: 100%|##########| 210/210 [00:29&lt;00:00,  7.47it/s]
2026/01/12 11:57:37.009 :: 100%|##########| 210/210 [00:29&lt;00:00,  7.11it/s]
2026/01/12 11:57:55.780 :: sending off prediction to background worker for resampling and export
2026/01/12 11:57:55.780 :: done with volume
2026/01/12 11:57:56.939 :: Loading inference results...
2026/01/12 11:57:58.427 :: Post processing results...
2026/01/12 11:57:58.438 :: Remove small voxels for Maxilla &amp; Upper Skull...
2026/01/12 11:57:59.833 :: Remove small voxels for Mandible...
2026/01/12 11:58:00.758 :: Remove small voxels for Upper Teeth...
2026/01/12 11:58:01.539 :: Remove small voxels for Lower Teeth...
2026/01/12 11:58:02.298 :: Post processing done.
2026/01/12 11:58:02.346 :: Inference ended successfully.
</code></pre>
<p>One difference I see is that you get this message:</p>
<blockquote>
<p>2026/01/09 16:30:18.304 :: perform_everything_on_device=True is only supported for cuda devices! Setting this to False</p>
</blockquote>
<p>What nnUnet version do you have installed (you can find it in nnUNet module in Slicer in the “nnUNet Install” section)?<br>
What GPU do you have?<br>
Does segmentation work if you select “Device” → “cpu” in the module?</p>

---
