# How to set MONAI Label extension parameters in 3D Slicer

**Topic ID**: 24379
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/how-to-set-monai-label-extension-parameters-in-3d-slicer/24379

---

## Post #1 by @platanus (2022-07-19 01:11 UTC)

<p>Hello. All members of 3D-Slicer.</p>
<p>I have a question for setting option of MONAI Label extension.<br>
.<br>
I want to extract brain tumor using a DICOM(MRI) file in MONAI Label module.</p>
<p>When I conducted modeling in MONAI Label, The proess that extracts brain tumor using MONAI Label module in 3D-Slicer as follows.</p>
<ol>
<li>In the option of  MONAI Label server, I pressed green button.</li>
<li>In the option of Master Volume, I pressed ‘arrow’ green button.</li>
<li>In the option of Segment Editor, I added two segment, and then I extract brain tumor using ,Paint’ and  ‘Grow and Seeds’ effect,</li>
<li>At the bottom of Strategy option, I pressed the “Submit Label” button.</li>
<li>After selecting ‘deepedit’ model, I pressed ‘Train’ button.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a55daad9d07ce3c4fc101bc4c3b693d3b4990111.png" data-download-href="/uploads/short-url/nATsLTEd3dgbYsQBcnlpnmJVEsx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a55daad9d07ce3c4fc101bc4c3b693d3b4990111_2_541x500.png" alt="image" data-base62-sha1="nATsLTEd3dgbYsQBcnlpnmJVEsx" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a55daad9d07ce3c4fc101bc4c3b693d3b4990111_2_541x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a55daad9d07ce3c4fc101bc4c3b693d3b4990111_2_811x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a55daad9d07ce3c4fc101bc4c3b693d3b4990111.png 2x" data-dominant-color="EDF1F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×777 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, I occur some problem after conducting above process.</p>
<p>When I press ‘Train’ buttion, after selecting ‘segmentation’ model, Status option run. But Accuracy option didn’t run.</p>
<p>What should I do for extractiong brain tumor in MONAI Label module using a DICOM(MRI) file based on 3D-Slicer.</p>

---

## Post #2 by @rbumm (2022-07-19 12:51 UTC)

<p>There is a new and instructive  <a href="https://www.youtube.com/watch?v=3HTh2dqZqew&amp;t=95s">MONAI Label Training From Scratch video</a> available on YouTube that shows all the necessary training steps for a lung segmentation model. The workflow for brain tumors should be very similar.</p>
<p>Please notify us if questions remain.</p>

---

## Post #3 by @platanus (2022-07-27 10:30 UTC)

<p>Dear. <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>I tried to extract brain tumor referring for link that you had been shared.</p>
<p>I want to automatically extract brain tumor using MONAI Label with DICOM file of one patient. So I can’t let me train this DICOM file because I have only one DICOM dataset.</p>
<p>I conducted extraction process of brain tumor using MONAI Label in 3D-Slicer  refering for share link as follows.</p>
<ol>
<li>
<p>I conducted MONAI Label server pressing ’green button’ next to MONAI Label server item.</p>
</li>
<li>
<p>I also created Master Volume after pressing ’green allow button’.</p>
</li>
<li>
<p>I extracted brain tumor using ’Paint’ effect and ‘Grow from Seeds’ effect in Segment Editor option.</p>
</li>
<li>
<p>I pressed ’Submit Label’ button.</p>
</li>
<li>
<p>I selected segmentation in ‘model’ part that is under ‘Submit Label’ button, and then pressed ‘train’ button.</p>
</li>
</ol>
<p>Is that all?</p>
<p>Some brain tumor is hard to extract in NVIDIA AIAA module, so I want to exactly extract brain tumor using MONAI Label module.</p>
<p>When I conducted as process above, I thought I would rather use only Grow from Seed effect in segment editor module than use Segment editor(Grow from Seeds) option in MONAI Label module.</p>
<p>What I want to exactly is as follows.</p>
<ol>
<li>
<p>I want to exactly extract brain tumor that is hard to extract in NVIDIA AIAA module using Auto-Segmentation or other method(AI-Assisted Annotation) in MONAI Label.</p>
</li>
<li>
<p>Additionally, I want to find the solution that select ‘model’ type. I don’t know how to appear ‘model’ type in ‘Auto Segmentation’ and ‘SmartEdit/Deepgrow’ option.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46917d3f35dd7f41be46c626bbe8f8ddd0675387.png" alt="image" data-base62-sha1="a4h8cbEpy3z24QNKJIQEwA1e09V" width="587" height="177"></p>
</li>
</ol>
<p>Please, let me know how to solve the problems above.</p>
<p>Thank you for reading my writing.</p>

---

## Post #4 by @rbumm (2022-07-28 19:16 UTC)

<p>Dear <a class="mention" href="/u/platanus">@platanus</a>,</p>
<p>Please run your NVIDIA Control Panel, go → help and -&gt;system information and post the results here.</p>
<p>Thank you.</p>

---

## Post #5 by @platanus (2022-07-29 00:38 UTC)

<p>Thank you for answering <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>System Information is as following.</p>
<p>NVIDIA System Information Report Generation Date: 07/29/2022 08:40:50<br>
System Name: KRK</p>
<p>[display]<br>
Operating System: Windows 10 Home, 64-bit<br>
DirectX Version: 12.0<br>
GPU Processor: NVIDIA GeForce RTX 3070 Laptop GPU<br>
Driver Version: 471.51<br>
Driver Type: DCH<br>
Direct3D feature level: 12_1<br>
CUDA Core: 5120<br>
Resizable BAR Yes<br>
Max-Q technology 3rd generation<br>
Dynamic Boost 2.0 Yes<br>
WhisperMode 2.0 Yes<br>
Advanced Optimus No<br>
Maximum graphics performance 100 W<br>
Core clock: 1290 MHz<br>
Memory data rate: 12.00 Gbps<br>
Memory interface: 256-bit<br>
Memory bandwidth: 384.06 GB/s<br>
Total available graphics memory: 16079 MB<br>
Dedicated video memory: 8192 MB GDDR6<br>
System video memory: 0 MB<br>
Shared system memory: 7887 MB<br>
Video BIOS Version: 94.04.4F.00.19<br>
IRQ: Not used<br>
Bus: PCI Express x8 Gen3<br>
Device Id: 10DE 249D 20141A58<br>
Part number: 4735 0010</p>
<p>[Component]</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>nvui.dll</th>
<th></th>
<th>8.17.14.7151</th>
<th></th>
<th>NVIDIA User Experience Driver Component</th>
</tr>
</thead>
<tbody>
<tr>
<td>nvxdplcy.dll</td>
<td></td>
<td>8.17.14.7151</td>
<td></td>
<td>NVIDIA User Experience Driver Component</td>
</tr>
<tr>
<td>nvxdbat.dll</td>
<td></td>
<td>8.17.14.7151</td>
<td></td>
<td>NVIDIA User Experience Driver Component</td>
</tr>
<tr>
<td>nvxdapix.dll</td>
<td></td>
<td>8.17.14.7151</td>
<td></td>
<td>NVIDIA User Experience Driver Component</td>
</tr>
<tr>
<td>NVCPL.DLL</td>
<td></td>
<td>8.17.14.7151</td>
<td></td>
<td>NVIDIA User Experience Driver Component</td>
</tr>
<tr>
<td>nvCplUIR.dll</td>
<td></td>
<td>8.1.940.0</td>
<td></td>
<td>NVIDIA Control Panel</td>
</tr>
<tr>
<td>nvCplUI.exe</td>
<td></td>
<td>8.1.940.0</td>
<td></td>
<td>NVIDIA Control Panel</td>
</tr>
<tr>
<td>nvWSSR.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Workstation Server</td>
</tr>
<tr>
<td>nvWSS.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Workstation Server</td>
</tr>
<tr>
<td>nvViTvSR.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Video Server</td>
</tr>
<tr>
<td>nvViTvS.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Video Server</td>
</tr>
<tr>
<td>nvLicensingS.dll</td>
<td></td>
<td>6.14.14.7151</td>
<td></td>
<td>NVIDIA Licensing Server</td>
</tr>
<tr>
<td>nvDispSR.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Display Server</td>
</tr>
<tr>
<td>nvDispS.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Display Server</td>
</tr>
<tr>
<td>nvDevToolSR.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA Licensing Server</td>
</tr>
<tr>
<td>nvDevToolS.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA 3D Settings Server</td>
</tr>
<tr>
<td>PhysX</td>
<td></td>
<td>09.20.0221</td>
<td></td>
<td>NVIDIA PhysX</td>
</tr>
<tr>
<td>NVCUDA64.DLL</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA CUDA 11.4.101 driver</td>
</tr>
<tr>
<td>nvGameSR.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA 3D Settings Server</td>
</tr>
<tr>
<td>nvGameS.dll</td>
<td></td>
<td>30.0.14.7151</td>
<td></td>
<td>NVIDIA 3D Settings Server</td>
</tr>
</tbody>
</table>
</div>

---

## Post #6 by @rbumm (2022-07-29 10:48 UTC)

<p>This seems to be great hardware to use MonaiLabel.</p>
<p>To address some of the questions above:</p>
<p>Question: Why does nothing show up under “Auto Segmentation” after you connected to ML server and trained?<br>
Answer: There was a recent <a href="https://github.com/Project-MONAI/MONAILabel/issues/852#">issue/bug</a> when using 3D Slicer 5.0.2 and the MonaiLabel extension.</p>
<p>(1) please make sure that you use 3D Slicer 5.0.3 stable for your next tests.<br>
(2) Start 3D Slicer 5.0.3 stable and install the MonaiLabel extension again.<br>
(3) Restart Slicer.</p>
<p>Please report back if that does not solve your problem.</p>
<p>Question:</p>
<aside class="quote no-group" data-username="platanus" data-post="3" data-topic="24379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecb155/48.png" class="avatar"> platanus:</div>
<blockquote>
<p>I want to automatically extract brain tumor using MONAI Label with DICOM file of one patient. So I can’t let me train this DICOM file because I have only one DICOM dataset.</p>
</blockquote>
</aside>
<p>Answer:<br>
You will need to train a machine learning model with many labeled volumes to have acceptable results. At least 3-5 different volumes (patients) are needed, you would need to label them one by one, then start the MonaiLabel training process.<br>
If you want to do your brain tumor segmentation <strong>on one dataset only</strong> I would recommend using 3D Slicers Segment Editor - no need to involve AI</p>

---

## Post #7 by @platanus (2022-07-30 08:25 UTC)

<p>Thank you for answering details. <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Now, I’m using 3D-Slicer 5.1.2 preview version.</p>
<p>Should I install 5.0.3 stable version for using Auto Segmentation in MONAI Label?</p>
<p>Anyway… As you let me know above, I installed 3D-Slicer 5.0.3 stable version. After reopening 3D-Slicer, I tried to extract brain tumor using MONAI Label.</p>
<p>The reason that I try to run Auto Segmentation in MONAI Label is because I’d like to exactly extract brain tumor in one volume  using AI-Assisted Annotation.</p>
<p>Brain tumor can exactly extract  in one volume  using Grow from Seeds effect in Segment Editor module and NVIDIA AIAA. But there is brain tumor hard to extract in one volume using Segment Editor and NVIDIA AIAA modules.</p>
<p>I didn’t solve problem as following yet.<br>
<span class="hashtag">#1</span><br>
Although you recommended that I need to use Segment Editor of 3D-Slicer when I use only one volume, I’d like to run  using Auto-Segmentation(Inference mode) or SmartEdit/Deepgrow options(Inference mode) in MONAI Label.<br>
Please, let me know how to extract brain tumor using Auto-Segmentation and SmartEdit/Deepgrow in MONAI Label module.</p>
<p><span class="hashtag">#2</span><br>
I installed 3D-Slicer 5.0.3 version and ran MONAI Label module after reopening 3D-Slicer, but it doesn’t show up nothing in ‘Model’ item, ‘run’ button, ‘Label’ item and ‘Update’ button of Auto-Segmentation option and SmartEdit/Deepgrow option in MONAI Label module.<br>
And I have question  regarding run of MONAI Label server for extracting brain tumor.</p>
<p><span class="hashtag">#3</span><br>
When I run MONAI server, I input command “monailabel start_server --app apps/radiology --studies datasets/Task02_57453299_VS --conf models deepedit”.<br>
Is it right to do this?</p>
<p>Thank you for always helping me.</p>

---

## Post #8 by @rbumm (2022-07-30 12:27 UTC)

<aside class="quote no-group quote-modified" data-username="platanus" data-post="7" data-topic="24379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecb155/48.png" class="avatar"> platanus:</div>
<blockquote>
<p>Please, let me know how to extract brain tumors using Auto-Segmentation and SmartEdit/Deepgrow in the MONAI Label module.</p>
</blockquote>
</aside>
<p>Please understand that for using auto-segmentation there are only two options here.</p>
<p>(1) You will need somebody who provides a working MonaiLabel brain tumor segmentation model to you. I (probably we) can not help here yet.</p>
<p>or</p>
<p>(2) you would need to train a MonaiLabel model <strong>yourself</strong> using <strong>many</strong> brain tumor volumes (50-100 patients minimum) with a steep learning curve and unclear outcome. I would not recommend you to do this for your special problem. Use Slicers conventional segment editor for the task and wait for a MonaiLabel brain tumor segmentation model to be published in the near future.</p>
<p>Of course, in the meantime, you can experiment with MonaiLabel.</p>
<aside class="quote no-group quote-modified" data-username="platanus" data-post="7" data-topic="24379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecb155/48.png" class="avatar"> platanus:</div>
<blockquote>
<p>I installed 3D-Slicer 5.0.3 version and ran MONAI Label module after reopening 3D-Slicer but it doesn’t show up nothing …</p>
</blockquote>
</aside>
<p>Did you start the server first ?</p>
<aside class="quote no-group" data-username="platanus" data-post="7" data-topic="24379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecb155/48.png" class="avatar"> platanus:</div>
<blockquote>
<p>When I run MONAI server, I input command “monailabel start_server --app apps/radiology --studies datasets/Task02_57453299_VS --conf models deepedit”.<br>
Is it right to do this?</p>
</blockquote>
</aside>
<p>The command line looks ok, where did you get the <code>Task02_57453299_VS</code> parameter from, and what happens if you issue that command? Please post a screenshot of the result or the output of the command.</p>

---

## Post #9 by @platanus (2022-07-31 05:01 UTC)

<p>Yon mean that It is not easy for me to run Auto Segmentation in MONAI Label based on 3D-Slicer.</p>
<p>Task02_57453299_VS is a folder included one volume(DICOM file).</p>
<p>When I input command “monailabel start_server --app apps/radiology --studies datasets/Task02_57453299_VS --conf models deepedit”, it occurrs result as following.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6b84c46a2b8c97bdef1916dd8175834b1eede30.png" data-download-href="/uploads/short-url/uDv2bnEVVfhed55uTwHLEen2fV6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6b84c46a2b8c97bdef1916dd8175834b1eede30.png" alt="image" data-base62-sha1="uDv2bnEVVfhed55uTwHLEen2fV6" width="690" height="479" data-dominant-color="0D1E0C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1387×963 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @rbumm (2022-07-31 05:54 UTC)

<p>MonaiLabel will not read your  DICOM data directly from a folder.</p>
<p>Enter the following command:</p>
<p><code>monailabel datasets</code></p>
<p>and you will get something like:</p>
<pre><code class="lang-auto">Using PYTHONPATH=C:\Users\yourname\MONAILabel;
Available Datasets are:
----------------------------------------------------
  Task01_BrainTumour            : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task01_BrainTumour.tar
  Task02_Heart                  : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task02_Heart.tar
  Task03_Liver                  : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task03_Liver.tar
  Task04_Hippocampus            : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task04_Hippocampus.tar
  Task05_Prostate               : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task05_Prostate.tar
  Task06_Lung                   : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task06_Lung.tar
  Task07_Pancreas               : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task07_Pancreas.tar
  Task08_HepaticVessel          : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task08_HepaticVessel.tar
  Task09_Spleen                 : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task09_Spleen.tar
  Task10_Colon                  : https://msd-for-monai.s3-us-west-2.amazonaws.com/Task10_Colon.tar 
</code></pre>
<p>Then download the Task01_BrainTumor dataset with:</p>
<p><code>monailabel datasets --download --name Task01_BrainTumour --output datasets </code></p>
<p>This will download the mentioned dataset to your harddrive.</p>
<p>Then you could run</p>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/Task01_BrainTumour --conf models deepedit 
</code></pre>
<p>Start 3D Slicer, connect to MonaiLabel in the extension,<br>
just press the green button:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3308e725d62fff4e36484e6e35864bcb131ec9ae.png" alt="image" data-base62-sha1="7htqnhUTU1fEAvwELNpvI14AyUm" width="487" height="42"><br>
and your fields will be populated. Press “Next Sample” to load the first volume.</p>
<p>Please do all this and report back. You should see one of the brain tumor volumes from the Task01 dataset in 3D Slicer. It is not your volume. It is one of the downloaded series.</p>

---

## Post #11 by @platanus (2022-07-31 08:25 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thank you for answering my question.</p>
<p>I simply wanted to compare brain tumor extraction results using Segment Editor(Grow from Seeds) and NVIDIA AIAA using clinical DICOM data as shown in the figure below.</p>
<p>So I first extracted the brain tumor using NVIDIA AIAA. However, there was a brain tumor that NVIDIA could not extract, so I posted a question on the 3D-Slicer Forum.</p>
<p>When I extract brain tumor using Segment Editor(Grow from Seeds), brain tumor extracts well.<br>
but I should compare Segment Editor and NVIDIA AIAA(other AIAA).</p>
<p>First image is to use option of Auto-Segmentation in NVIDIA AIAA.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecf8105026c084e247f08244916a12268f8c38e0.jpeg" data-download-href="/uploads/short-url/xOk9JTF44jPerrjc8lBsb3UcnRK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecf8105026c084e247f08244916a12268f8c38e0_2_690x374.jpeg" alt="image" data-base62-sha1="xOk9JTF44jPerrjc8lBsb3UcnRK" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecf8105026c084e247f08244916a12268f8c38e0_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecf8105026c084e247f08244916a12268f8c38e0_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecf8105026c084e247f08244916a12268f8c38e0.jpeg 2x" data-dominant-color="5F656D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1071×581 70.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Second image is to use option of Segment from boundary point(DExtr3D).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ab80e8ec3dd10844610b4d835f3b8f45af6dfe6.jpeg" data-download-href="/uploads/short-url/fe4X12EcQqoWLF10zsQlyQwILFs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab80e8ec3dd10844610b4d835f3b8f45af6dfe6_2_689x328.jpeg" alt="image" data-base62-sha1="fe4X12EcQqoWLF10zsQlyQwILFs" width="689" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab80e8ec3dd10844610b4d835f3b8f45af6dfe6_2_689x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab80e8ec3dd10844610b4d835f3b8f45af6dfe6_2_1033x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ab80e8ec3dd10844610b4d835f3b8f45af6dfe6.jpeg 2x" data-dominant-color="575957"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1374×655 94.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/pieper">@pieper</a> mentioned MONAI Label to solve my <a href="https://discourse.slicer.org/t/do-you-know-how-to-exactly-extract-brain-tumor-using-nvidia-module/24153">problem</a>.</p>
<p>So, I had tried to run MONAI Label for extracting brain tumor.</p>
<p>Although you have helped a lot, it is not easy to extract brain tumor of the figure above using MONAI Label.</p>
<p>I don’t have to use the MONAI Label to extract brain tumor.</p>
<p>I should extract brain tumor using AIAA method such as pre-trained Auto Segmentation or Segment from boundary point(DExtr3D) included in NVIDIA AIAA.</p>
<p>If brain tumor of above figure don’t extract using pre-trained Auto Segmentation or DeeEdit/DeepGrow included in  MONAI Label, can you suggest alterative other AIAA method?</p>
<p>I should compare Segment Editor module and NVIDIA AIAA(or other AIAA)  module after extracting brain tumor of figure above.</p>

---

## Post #12 by @rbumm (2022-07-31 09:53 UTC)

<aside class="quote no-group" data-username="platanus" data-post="11" data-topic="24379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecb155/48.png" class="avatar"> platanus:</div>
<blockquote>
<p>can you suggest alterative other AIAA method</p>
</blockquote>
</aside>
<p>No, I can not suggest an alternate AIAA method.</p>

---

## Post #13 by @platanus (2022-08-04 06:20 UTC)

<p>Thank you for helping me <a class="mention" href="/u/rbumm">@rbumm</a>.</p>

---

## Post #14 by @deboshree_roy (2022-10-25 12:46 UTC)

<p><span class="mention">@rbunn</span> I have been stuck in a similar situation and I hope you will be able to guide me through this<br>
I have my own pre-trained model (.pth file) that I is tested and shown to give good results<br>
On loading the same model in 3D Slicer to conf → deepedit.py and editing the labels, I expect a well defined result when I run Auto-segment module.</p>
<p>But the results are completely off the track. Can you please help me on how to go about this ?</p>

---
