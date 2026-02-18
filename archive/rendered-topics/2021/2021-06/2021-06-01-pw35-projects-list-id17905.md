# PW35 Projects List

**Topic ID**: 17905
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/pw35-projects-list/17905

---

## Post #1 by @Sam_Horvath (2021-06-01 14:48 UTC)

<p>Hi all</p>
<p>This will be our master topic for PW35 projects.  Please post a reply to this topic with the project(s) you are considering.  Or, feel free to create a standalone topic for your project in the ProjectWeek section, and link to it here.</p>
<p>Thanks,</p>
<p>Sam</p>

---

## Post #2 by @Sam_Horvath (2021-06-01 14:49 UTC)



---

## Post #3 by @curtislisle (2021-06-01 15:13 UTC)

<p>I am planning to attend PW35 and will be working on a project entitled: “Registration of Time Series data for Deep Learning”.  I have a longitudinal dataset of patients who have been treated for lung cancer.  They returned periodically for several follow-up scans to see if any cancer has returned.  I propose to (1) use Plastimatch or other techniques to first register and measure the time sequence of a patient’s scans, and then (2) to prepare the 4D (3D + time) dataset for annotation and deep learning-based learning.</p>

---

## Post #4 by @Fernando (2021-06-01 15:48 UTC)

<p>Hi all,</p>
<p>Apart from supporting the <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc"><code>MONAILabel</code></a> team, I would like to work on more generic and lower-level compatibility issues between <a href="https://pytorch.org/" rel="noopener nofollow ugc">PyTorch</a> and Slicer.</p>
<p>Basically, I imagine the following scenario: a user has trained a deep learning segmentation model using PyTorch (and possibly <a href="https://torchio.readthedocs.io/" rel="noopener nofollow ugc">TorchIO</a>, <a href="https://monai.io/" rel="noopener nofollow ugc">MONAI</a> or <a href="https://colab.research.google.com/github/fepegar/torchio-notebooks/blob/main/notebooks/TorchIO_MONAI_PyTorch_Lightning.ipynb" rel="noopener nofollow ugc">both</a>). They want users (e.g., clinicians) to be able to use the model on their own data, without the need to code. The best solution is probably to contribute an extension. (I am in this situation, with <a href="https://github.com/fepegar/resseg" rel="noopener nofollow ugc"><code>resseg</code></a> and its corresponding extension <a href="https://github.com/fepegar/SlicerEPISURG" rel="noopener nofollow ugc"><code>SlicerEPISURG</code></a>).</p>
<p>Three issues I would like to address:</p>
<ol>
<li>How to install PyTorch inside Slicer. The main question is whether to install a version with GPU support and, if it does, which version of the CUDA toolkit to install. I did a bit of work on this during the development of the <a href="https://github.com/fepegar/SlicerTorchIO" rel="noopener nofollow ugc"><code>SlicerTorchIO</code></a> extension.</li>
<li>How to handle the necessary conversion of Slicer nodes (e.g. <code>vtkMRMLScalarNode</code>) to  PyTorch objects (e.g. <code>torch.Tensor</code>). A few additions to <code>slicer.util</code> might help here.</li>
<li>Possibly, contributing a full tutorial with a toy example using a publicly available dataset such as TorchIO’s <a href="https://torchio.readthedocs.io/datasets.html#ixitiny" rel="noopener nofollow ugc"><code>IXITiny</code></a> or a dataset from the <a href="http://medicaldecathlon.com/" rel="noopener nofollow ugc">Medical Segmentation Decathlon</a>*</li>
</ol>
<p>If someone is interested in this stuff, please let me know and let’s work together!</p>
<p>Some related projects that are probably worth looking at are <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DeepInfer" rel="noopener nofollow ugc">DeepInfer</a> and <a href="https://github.com/faustomilletari/TOMAAT-Slicer" rel="noopener nofollow ugc">TOMAAT</a>.</p>
<p>*Many images from the Medical Decathlon cannot be easily read by Slicer due to their 4D shape. This can maybe be addressed within the <code>MONAILabel</code> projects – <a class="mention" href="/u/diazandr3s">@diazandr3s</a>, <a class="mention" href="/u/sachidanandalle">@SachidanandAlle</a></p>

---

## Post #5 by @diazandr3s (2021-06-01 20:22 UTC)

<p>These are great topics <a class="mention" href="/u/fernando">@Fernando</a>. We can use MONAILabel to train those deep learning segmentation models you mentioned. Happy to help with this.<br>
I’d also like to echo the issue we had when loading multimodality images in Slicer (Modality, Height, Width, Depth). MONAILabel will benefit from this as it allows the development of <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps" rel="noopener nofollow ugc">Apps</a> that manage multimodality images. So far we have Apps that work on single modality images only.<br>
Another project I’m really interested in is the development of the OHIF plugin for MONAILabel. If anyone would like to contribute on any of these, please don’t hesitate to reach out <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @curtislisle (2021-06-03 13:54 UTC)

<p>I will be interested in attending a breakout session or other project meetings to discuss integrating Slicer with deep learning systems.  I am personally leaning toward having the deep learning server outside of Slicer instead of performing the training/prediction inside Slicer using Slicer’s Python interpreter.  I believe others in the community have some examples we can learn from.  From my first impressions, the MONAILabel architecture looks promising for hosting deep learnig models.</p>

---

## Post #7 by @Ron (2021-06-04 23:14 UTC)

<p>I would like to propose a project for establishing (more initial steps I suppose) entitled: “development of a deep learning segmentation approach for spines with metastatic disease" as part of an NIH grant project for the development of risk of fracture prediction in cancer patients.<br>
However, I am not a programmer! I have 50 labeled CT data sets for lumbar and/or thoracic as well as full spine columns for patients at baseline. For a good # of patients, we have 3 and 6m follow-up CT.  These are not yet labeled.  I can try and label these data sets if this would be of help for model development. Indeed it would be great to get some help/advice regarding how to speed up the segmentation for the labeling and extraction of volume information from the masks. The segmented volumes are needed for the analytical and computational modeling pipeline as part of a collaboration with MIT.<br>
Ultimately the study patient cohort will contain 450 patients for which CT imaging is tightly standardized, as much as we can in a clinical environment across departments, with baseline and longitudinal follow up at 3, 6 9, and 12M.<br>
I am looking forward to seeing what can be done, as I have several additional novel projects regarding imaging (CT, MRI) of this cohort that will greatly benefit from a deep learning approach. I am happy to be fully committed to the project in whatever capacity useful for the project.<br>
Ron</p>

---

## Post #8 by @pieper (2021-06-07 20:04 UTC)

<p>I’m interested in following up on work from <a href="https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/Slicer_in_Cloud_Environments/">last project week</a> and <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/OHIFSlicerBridge/">the one before that</a> to launch Slicer instances on-demand in cloud environments (optionally GPU accelerated for ML.  The idea would be that one could browse studies and view images in OHIF, and then launch Slicer on the same dataset to access any of the tools and extensions it can provide, ultimately storing back segmentations or other results back to the original or another server.</p>

---

## Post #9 by @simonoxen (2021-06-08 10:33 UTC)

<p>I’m interested developing a module combining different resources (imaging, electrophysiology, atlases) to get a live feedback during Deep Brain Stimulation surgery. The idea is to communicate with devices SDK to get the current location of micro electrodes and their recordings. From here, different visualisations can be implemented in Slicer.</p>
<p>I’m also interested in image registration - currently working on adding ANTs registration in Slicer and a  module capable of manually fixing small misalignments from the non-linear registration warp.</p>

---

## Post #10 by @cpinter (2021-06-08 12:26 UTC)

<p>My plan is to move forward the VTK9 compatibility of the SlicerVirtualReality extension, and in case it is achieved, continue by integrating in-VR UI widgets in said extension. For reference see project page from <a href="https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerVR/">last project week</a>.</p>
<p>Update: the <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SlicerVR/">project page</a> is ready.</p>

---

## Post #11 by @RafaelPalomar (2021-06-08 14:15 UTC)

<p>I’m planning to continue our liver surgery planning platform from <a href="https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerLiverAnalysis/" rel="noopener nofollow ugc">last project week</a>. I’ll be joined by <a class="mention" href="/u/dalbenziog">@dalbenzioG</a> (OUS), Ole V. Solberg (SINTEF) and Geir A. Tangen (SINTEF)</p>

---

## Post #12 by @diazandr3s (2021-06-18 10:19 UTC)

<p>Hi <a class="mention" href="/u/Ron">@Ron</a> let’s create a MONAILabel App for this use case. Happy to help! Are you registered for the Slicer Week Workshop?</p>

---

## Post #13 by @Neha_Goyal (2021-06-18 14:07 UTC)

<p>Hi Curtis,</p>
<p>I have worked on image registration with EM images using deep learning model. I am interested in your project and would like to work with you.</p>

---

## Post #14 by @Ron (2021-06-18 15:19 UTC)

<p>Dear Andres and Curtis</p>
<p>I am very grateful that you are willing to help me with this project. Andres, Curtis, and I have been talking over the last two weeks about the project and Curtis has been trying to help me install Linux mint on a rather recalcitrant Lenovo P620. We are hoping to have it ready for the project week. As to patient data sets, I am hoping to put at least 4. I am having issues with the BI regarding putting more of the data online.</p>
<p>As I have stated, I am not a programmer or an imaging expert. Thus I cannot offer any help in this regard. However, I am more than happy to collaborate. I have attached reference that relate directly to the spine. I have more comprehensive PDF from that workshop, but its 7MB and I got a error message from discorse. I am happy to have a meeting (zoom?)with all of us to plan the week. For my end, I aim to become a better slicer user. Currently, to segment, a spine takes two days ( partially, still having problems encompassing the full volume!)</p>
<p>As to registration, I think I am. I am getting emails regarding the week. How can I confirm?</p>
<p>I have never worked with GitHub. Curtis kindly offered to put the project description on the site.</p>
<p>I very much look forward to working with you both. R</p>
<p>(Attachment Coarse to Fine Vertebrae Localization and Segmentation with Spatial Configuration-Net and U-Net.pdf is missing)</p>

---

## Post #15 by @curtislisle (2021-06-18 18:41 UTC)

<p><a class="mention" href="/u/neha_goyal">@Neha_Goyal</a>:</p>
<p>Dear Neha, thank you for your interest in this registration project.  I will ask my collaborators about sharing some sample data with you, and I look forward to discussing this problem further.  I have access to deep learning hardware, so I can run tests during the project week.  Thanks again for your interest.</p>
<p>Curtis</p>

---

## Post #16 by @Neha_Goyal (2021-06-20 17:14 UTC)

<p>Hello Curtis,</p>
<p>Thank you. Please let me know when you and the team are available to discuss more.<br>
Also if you could share project meeting link for every Tuesday with me?</p>
<p>Regards,<br>
Neha</p>

---

## Post #17 by @mau_igna_06 (2021-06-22 13:09 UTC)

<p>I’m interested in helping new developers give support to more kinds of planar osteotomies surgeries for virtual surgical planning and patient-specific guides. Also improving the current <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" rel="noopener nofollow ugc">mandibular reconstruction module</a> to support dental implants planning and (if there is time) finish the <a href="https://github.com/mauigna06/SlicerDeformityCorrectionOsteotomyPlanner" rel="noopener nofollow ugc">long-bone deformity correction module</a>.<br>
More info <a href="https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/PlanarOsteotomiesVSPAndSurgicalGuides" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #18 by @HINeurosurgeon (2021-06-26 15:48 UTC)

<p>I am a clinician and trying to bring a miniaturized version of a simple image guidance system for cranial procedures to the bedside using facial features for registration for simplicity.</p>
<p>I am currently trying to use a Microsoft azure camera linked to a tablet or laptop. The challenge has been in obtaining registration using the camera.</p>
<p>Once this step is obtained, we would like to try to use a different fiducial (perhaps a QR code) to track the instrument that needs to be navigated.</p>

---

## Post #19 by @lassoan (2021-06-26 17:41 UTC)

<p>There are several groups at the project week who have been working on this topic. We have been using ArUco makers, flexible marker patterns, surface mesh acquired by Intel RealSense camera, etc.</p>
<p>We have a <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/MarkerlessTrackingWithRGBDCamerasForLowCostNeuronavigation/">very closely related project</a> during this project week. It would be great if you could join.</p>

---

## Post #20 by @RebeccaHisey (2021-06-28 13:19 UTC)

<p>Hi <a class="mention" href="/u/fernando">@Fernando</a> I have some similar experience working on this problem except using Tensorflow/Keras instead of Pytorch. I’m happy to discuss the approach that we’ve taken and potentially see if we can  to make these projects work together seamlessly! If you want to take a look at what I’ve done so far it can be found here: <a href="https://github.com/SlicerIGT/aigt/tree/master/DeepLearnLive" class="inline-onebox" rel="noopener nofollow ugc">aigt/DeepLearnLive at master · SlicerIGT/aigt · GitHub</a></p>

---

## Post #21 by @Fernando (2021-06-28 13:21 UTC)

<p>Thanks, Rebecca. I added you to the <a href="https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/PyTorchIntegration#key-investigators" rel="noopener nofollow ugc">investigators list</a>. I haven’t found you on the Discord group. The breakout session is today at 8 PM UTC (4 PM EST). It would be great if you (and <a class="mention" href="/u/ungi">@ungi</a>? who I haven’t found on Discord either) could join and share your experience.</p>

---

## Post #22 by @Aditiy.aiyer (2022-10-19 04:42 UTC)

<p>Hello,<br>
I am a 4th year Integrated MTech Bioengineering student. I am currently doing an internship in which I have to make 3d models using CT and MRI scans. I am also interested in your project. Would like to know about your idea and would also like to help with the same.<br>
Thank you!</p>

---
