---
topic_id: 27504
title: "Novice Guidance For Using Monai Label To Create An Automatic"
date: 2023-01-27
url: https://discourse.slicer.org/t/27504
---

# Novice Guidance for Using MONAI Label to Create an Automatic Segmentation App

**Topic ID**: 27504
**Date**: 2023-01-27
**URL**: https://discourse.slicer.org/t/novice-guidance-for-using-monai-label-to-create-an-automatic-segmentation-app/27504

---

## Post #1 by @JacobD (2023-01-27 15:35 UTC)

<p>I attended the recent MONAI Label Workshop, and with a background of sports medicine/orthopaedics research, I am new to this concept and do not have a strong background in computer programming. I am familiar with 3D Slicer, however, and I am looking for additional assistance or resources to help guide my learning.</p>
<p>Essentially, the goal is to create a MONAI Label app that automatically segments the bones of the shoulder joint, primarily, to display a visualization of glenohumeral bone loss to assist with research, analysis, and surgical planning. I have manually segmented several shoulder MRIs, and I am looking to use this work to contribute to a learning model, for efficiency purposes.</p>
<p>Currently, listed are some of the resources that have been helpful in progressing this idea, however, there are some limitations and questions that I was hoping to find clarification for.</p>
<p>Resources:</p>
<p>-Steps for Running a MONAI Label server: <a href="http://github.com/Project-MONAI/MONAILabel#installation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a><br>
-MONAI Label Bootcamp: <a href="https://docs.google.com/presentation/d/19YWH7J-WBGl9MLfrd8eybJ_Bhwio7lXQjsM8EKcOOhk/edit?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel_MONAI_Bootcamp_Sept_2021 - Google Slides</a><br>
-MONAI Label-Training from Scratch: <a href="http://youtube.com/watch?v=3HTh2dqZqew" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label - Training from Scratch - YouTube</a></p>
<p>Limitations/Questions:</p>
<p>-My current computer is a MacBook Pro. As, to my understanding, a Windows or Linux system is required for MONAI Label, what are my options? Would running Windows or Linux on a Mac be sufficient, or would a specific computer be required? Is the purpose of using AWS AppStream to connect to a server capable of this process, if a local network is not available?<br>
-Using Python: Attempting to follow the installation process, the message ‘SyntaxError: invalid syntax’ is listed when entering any of the information into 3D Slicer. Is this because it is being entered on a Mac, or is it simply being entered incorrectly?</p>
<p>Please feel free to let me know if any other information is requested. Thanks!</p>

---

## Post #2 by @pieper (2023-01-27 15:46 UTC)

<p>Hi -</p>
<p>It sounds like you are on the right track but yes, there are several details to work out.  Maybe a good approach would be to sign up for next week’s <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/">project week</a> (you can join online, but you’d need to be able to invest some time) and either sign up for a project similar to your plans or create your own page with details (ideally some sample data) and probably people with similar interests can help you sort out some of these details.</p>

---

## Post #3 by @rbumm (2023-01-28 13:16 UTC)

<aside class="quote no-group" data-username="JacobD" data-post="1" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>-My current computer is a MacBook Pro. As, to my understanding, a Windows or Linux system is required for MONAI Label, what are my options?</p>
</blockquote>
</aside>
<p>You can run 3D Slicer and the MONAILabel extension on a Macbook Pro, but should be running the MONAILabel server on a system with CUDA and GPU processing avalable which will make processing, inference (show the results of your trained model in a new dataset) and training itself faster.</p>
<aside class="quote no-group" data-username="JacobD" data-post="1" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>Would running Windows or Linux on a Mac be sufficient, or would a specific computer be required?</p>
</blockquote>
</aside>
<p>A specific computer acting as your MONAILabel Server would be required. See above.</p>
<aside class="quote no-group" data-username="JacobD" data-post="1" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>Is the purpose of using AWS AppStream to connect to a server capable of this process, if a local network is not available?</p>
</blockquote>
</aside>
<p>Yes. But any other CUDA-enabled system in your network will also work.</p>
<aside class="quote no-group" data-username="JacobD" data-post="1" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>Using Python: Attempting to follow the installation process, the message ‘SyntaxError: invalid syntax’ is listed when entering any of the information</p>
</blockquote>
</aside>
<p>Where exactly do you enter the information you are referring to?</p>

---

## Post #4 by @JacobD (2023-02-02 22:38 UTC)

<p>Thank you both for the suggestions and information. I am not able to participate in project week, however, I am following some of the posts from Discord to help educate myself and continue learning.</p>
<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Where exactly do you enter the information you are referring to?</p>
</blockquote>
</aside>
<p>Regarding the question, the information is entered in the Python Console window in 3D Slicer, or the IDLE Shell that was downloaded. Following the <a href="https://github.com/Project-MONAI/MONAILabel#installation" rel="noopener nofollow ugc">installation guide</a>, for example, the message ‘SyntaxError: invalid syntax’ is displayed when ‘pip install monailabel -U’ is entered.</p>

---

## Post #5 by @rbumm (2023-02-04 12:46 UTC)

<p>The steps for setting up MONAILabel on a Mac are as follows:</p>
<ol>
<li>Install the MONAILabel extension in Slicer</li>
<li>Connect to a MONAILabel server</li>
</ol>
<p>Note: The “pip install MONAILabel -U” command should be entered on the system where you want to install the MONAILabel server. The server should have CUDA and a NVIDIA GPU and be reachable over the network. This could be a Google Cloud computer, an AWS EC2 or Appstream instance, or any other server of your choice.</p>

---

## Post #6 by @JacobD (2023-02-08 15:05 UTC)

<p>Thank you. The MONAILabel extension is installed in Slicer, however, I do not seem to be understanding how to connect to a server. When entering the “pip install MONAILabel -U” command on the desired system, an error message appears.</p>
<blockquote>
<p>ERROR: Cannot install monailabel==0.4.0, monailabel==0.4.1, monailabel==0.4.2, monailabel==0.5.0, monailabel==0.5.1, monailabel==0.5.2 and monailabel==0.6.0 because these package versions have conflicting dependencies.</p>
<p>The conflict is caused by:<br>
monailabel 0.6.0 depends on torch&gt;=1.7<br>
monailabel 0.5.2 depends on torch&gt;=1.7<br>
monailabel 0.5.1 depends on torch&gt;=1.7<br>
monailabel 0.5.0 depends on torch&gt;=1.7<br>
monailabel 0.4.2 depends on torch&gt;=1.7<br>
monailabel 0.4.1 depends on torch&gt;=1.7<br>
monailabel 0.4.0 depends on torch&gt;=1.7</p>
<p>To fix this you could try to:</p>
<ol>
<li>loosen the range of package versions you’ve specified</li>
<li>remove package versions to allow pip attempt to solve the dependency conflict</li>
</ol>
<p>ERROR: ResolutionImpossible: for help visit <a href="https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts" class="inline-onebox" rel="noopener nofollow ugc">Dependency Resolution - pip documentation v24.0.dev0</a></p>
</blockquote>
<p>I do not understand what the error is, or how to apply the suggested solutions to the entered information. Please feel free to let me know if any assistance or suggestions regarding a solution is available, or if it should be directed differently.</p>
<p>The system I am using may not be ideal regarding the previously mentioned requirements, however, my understanding is that the server should be able to be established, and that the processing and functionality would be slower. If the message displayed is a result of incompatibility, please feel free to let me know as well.</p>
<p>I appreciate the assistance!</p>

---

## Post #7 by @rbumm (2023-02-08 15:43 UTC)

<p>You will need to</p>
<pre><code class="lang-auto">python -m pip install --upgrade pip setuptools wheel
</code></pre>
<p>and</p>
<pre><code class="lang-auto">pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu114
</code></pre>
<p>on your system first. <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">Here</a> is a full installation guide for Windows 11.</p>

---

## Post #8 by @JacobD (2023-02-13 16:43 UTC)

<p>Thank you. The Python version installed was outdated, so after resolving that, by following the installation guide, a server was able to be started.</p>
<p>Now that I understand the process of starting a MONAILabel server, the goal is to create an app that automatically segments the humerus, clavicle, and scapula, utilizing a stored repository of previously segmented MRI scans. It appears that the best way to achieve this goal is to follow the <a href="https://www.youtube.com/watch?v=3HTh2dqZqew" rel="noopener nofollow ugc">MONAILabel-Training from Scratch</a> video, loading the mentioned MRI dataset in place of the lung dataset used in the video, and training a model based off of those segmentations.</p>
<p>Please feel free to let me know if this plan is missing any steps, if any information is being overlooked, or if any other resources or directions may be valuable.</p>
<p>Thank you!</p>

---

## Post #9 by @JacobD (2023-03-02 14:29 UTC)

<p>Hello!</p>
<p>I wanted to reach out with some questions that I thought of as I am learning this process. I am not able to actually attempt the process yet due to unavailable resources, so I am attempting to map out a plan. I apologize if any of the questions would be easily solved after attempting the process.</p>
<ul>
<li>
<p>Based on my goal of using previously segmented images to train a model, is the ‘segmentation’ model the best model to utilize? If not, why would the DeepGrow or DeepEdit be chosen alternatively?</p>
</li>
<li>
<p>When preparing the dataset, will multiple multi-label .mrb files suffice if stored in a folder together, or is there a different format that they should be stored as?</p>
</li>
<li>
<p>As part of the stored segmentations, a background segment has already been established prior to loading onto the MONAI Label module. Can that simply be added as a label when adjusting the labels of the model in the ‘configs’ folder?</p>
</li>
<li>
<p>As the seeds would have already been added when the files are loaded, and the ‘grow from seeds’ function has been initialized and applied, as these files are previously segmented, can that be submitted to the server to train the model?</p>
</li>
<li>
<p>When the label is ‘submitted to the server,’ how secure is that? Would the data have the potential to be accessible by an outside source in any way?</p>
</li>
</ul>
<p>Thank you for any answers or assistance in helping me learn this information!</p>

---

## Post #10 by @rbumm (2023-03-02 17:42 UTC)

<p>Very good questions, <a class="mention" href="/u/jacobd">@JacobD</a>. We will try to answer them step by step, hopefully with the help of <a class="mention" href="/u/diazandr3s">@diazandr3s</a> and <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>Last question first:</p>
<aside class="quote no-group" data-username="JacobD" data-post="9" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>When the label is ‘submitted to the server,’ how secure is that? Would the data have the potential to be accessible by an outside source in any way?</p>
</blockquote>
</aside>
<p>If you run the server and 3D Slicer with the MONAILabel extension on the same computer: No, that data will not be accessible by an outside source as long as you do not open specific ports in the firewall.</p>

---

## Post #11 by @rbumm (2023-03-02 18:01 UTC)

<aside class="quote no-group" data-username="JacobD" data-post="9" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>Based on my goal of using previously segmented images to train a model, is the ‘segmentation’ model the best model to utilize? If not, why would the DeepGrow or DeepEdit be chosen alternatively?</p>
</blockquote>
</aside>
<p>I am not associated with the MonaiLabel development team but glad to help, if possible. Did my lung segmentation training exercise with the “segmentation” model after starting with DeepEdit and the results were not convincing.</p>
<p>You would need to edit the segmentation.py config file on your system <a href="https://github.com/Project-MONAI/MONAILabel/blob/5d2ae1fbb770040ef1e428b8e7b0312c6bbead75/sample-apps/radiology/lib/configs/segmentation.py#L37">here</a> and add the labels that exactly match the ones you are gonna use.</p>
<aside class="quote no-group" data-username="JacobD" data-post="9" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>When preparing the dataset, will multiple multi-label .mrb files suffice if stored in a folder together, or is there a different format that they should be stored as?</p>
</blockquote>
</aside>
<p>My workflow was: Open the dataset in 3D Slicer, make a segmentation with MONAILabel segmentation tools or Slicer tools, then “submit to the server” and save it locally as well for backup.<br>
Did this for 5-7 segmentation, train, and after that already got a relatively good inference on the next loaded dataset.  Around 20 labeled datasets and several hours (better days) of training are the low limit for getting good inference.</p>
<p>Most AI tools work with NIFTI (*.nii.gz) format and this is the format in which the MONAILabel server will store your labels in its dataset directory.</p>
<aside class="quote no-group" data-username="JacobD" data-post="9" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>As part of the stored segmentations, a background segment has already been established prior to loading onto the MONAI Label module. Can that simply be added as a label when adjusting the labels of the model in the ‘configs’ folder?</p>
</blockquote>
</aside>
<p>Do not understand this, please post an image</p>
<aside class="quote no-group" data-username="JacobD" data-post="9" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>As the seeds would have already been added when the files are loaded, and the ‘grow from seeds’ function has been initialized and applied, as these files are previously segmented, can that be submitted to the server to train the model?</p>
</blockquote>
</aside>
<p>Yes.</p>
<p>Hope that helps …</p>

---

## Post #12 by @JacobD (2023-03-03 19:34 UTC)

<p>Thank you, that information is very helpful.</p>
<p>I attempted to edit the segmentation.py config file, and was able to successfully change the label names, so it is helpful to know that that is the correct process.</p>
<aside class="quote no-group" data-username="rbumm" data-post="11" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Do not understand this, please post an image</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99fd5e2b7db1955148e0546f80b39588fe48291f.png" data-download-href="/uploads/short-url/lYfTfnaFf91oWg43q0H6j48SWlh.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99fd5e2b7db1955148e0546f80b39588fe48291f_2_517x105.png" alt="" data-base62-sha1="lYfTfnaFf91oWg43q0H6j48SWlh" width="517" height="105" role="presentation" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99fd5e2b7db1955148e0546f80b39588fe48291f_2_517x105.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99fd5e2b7db1955148e0546f80b39588fe48291f_2_775x157.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99fd5e2b7db1955148e0546f80b39588fe48291f_2_1034x210.png 2x" data-dominant-color="EAEAE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1058×216 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regarding the question, my phrasing may not have been clear. The picture is from the Segment Editor module of a segmented file. The segmented files in the dataset were originally segmented into ‘scapula,’ ‘clavicle,’ ‘humerus,’ and ‘other,’ which is essentially the same as ‘background.’ The ‘MONAI Label-Training from Scratch’ Youtube video, however, does not list ‘background’ as a label when editing the config file, it adds it when using the Segment Editor tab of the MONAI Label extension to paint seeds. I did not know if there was a specific reason for following that order.</p>
<aside class="quote no-group" data-username="rbumm" data-post="11" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Most AI tools work with NIFTI (*.nii.gz) format and this is the format in which the MONAILabel server will store your labels in its dataset directory.</p>
</blockquote>
</aside>
<p>My workflow would be slightly different since I would not be making any edits to the segmentations after loading them, they would just be opened in slicer and immediately submitted to the server since they are already segmented. When I open files in Slicer, however, I usually drag and drop the locally saved .mrb file. Would I need to go back and convert all of the .mrb files into NIFTI files?</p>
<p>Thanks!</p>

---

## Post #13 by @rbumm (2023-03-03 19:52 UTC)

<aside class="quote no-group" data-username="JacobD" data-post="12" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacobd/48/9414_2.png" class="avatar"> JacobD:</div>
<blockquote>
<p>Would I need to go back and convert all of the .mrb files into NIFTI files?</p>
</blockquote>
</aside>
<p>No, you can work with your MRB files.</p>

---

## Post #14 by @rbumm (2023-03-03 20:34 UTC)

<p>BTW have you tried TotalSegmenator for analyzing your data? It should be able to segment the bones you mentioned out of the box.</p>

---

## Post #15 by @diazandr3s (2023-03-06 11:51 UTC)

<p>Many thanks for the ping, <a class="mention" href="/u/rbumm">@rbumm</a>.</p>
<p>Just came back from leave, and I’m catching up on emails/discussions.</p>
<p><a class="mention" href="/u/jacobd">@JacobD</a> all these are great questions. I see most of them have been addressed by <a class="mention" href="/u/rbumm">@rbumm</a>.</p>
<p>Here are my comments on them:</p>
<blockquote>
<ul>
<li>Based on my goal of using previously segmented images to train a model, is the ‘segmentation’ model the best model to utilize? If not, why would the DeepGrow or DeepEdit be chosen alternatively?</li>
</ul>
</blockquote>
<p>Yes, I’d recommend starting with the Segmentation model.<br>
DeepGrow and DeepEdit are interactive models. They feature an option of modifying/creating the segments by using clicks. One of the disadvantages of DeepEdit though is that it uses the whole volume to train the model. This means a bigger GPU is needed to have high-quality segmentations.</p>
<blockquote>
<p>When preparing the dataset, will multiple multi-label .mrb files suffice if stored in a folder together, or is there a different format that they should be stored as?</p>
</blockquote>
<p>For multi-label segmentation, you should merge all segmentations into a single file. Here you can find an example using the Total Segmentator dataset showing how you should prepare the label files for multi-label segmentation: <a href="https://youtu.be/KtPE8m0LvcQ?t=500" rel="noopener nofollow ugc">https://youtu.be/KtPE8m0LvcQ?t=500</a></p>
<blockquote>
<p>As part of the stored segmentations, a background segment has already been established prior to loading onto the MONAI Label module. Can that simply be added as a label when adjusting the labels of the model in the ‘configs’ folder?</p>
</blockquote>
<p>If using the Segmentation model, you don’t need to specify the background label</p>
<blockquote>
<p>As the seeds would have already been added when the files are loaded, and the ‘grow from seeds’ function has been initialized and applied, as these files are previously segmented, can that be submitted to the server to train the model?</p>
</blockquote>
<p>Yes, you should be able to submit the segmentation to the MONAI Label model regardless of how they have been created.</p>
<blockquote>
<p>When the label is ‘submitted to the server,’ how secure is that? Would the data have the potential to be accessible by an outside source in any way?</p>
</blockquote>
<p>As <a class="mention" href="/u/rbumm">@rbumm</a> nicely pointed out, if you run both server and Slicer on the same PC, no data will go outside the computer. Another situation is when MONAI Label server runs on a different PC - in that case, security will depend on the type of connection you have to that PC.</p>
<p>I hope this helps.</p>
<p>Thanks again, <a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #16 by @JacobD (2023-03-14 14:04 UTC)

<p>Thank you both for the information. Starting with the Segmentation model appears to be a good approach.</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="15" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>For multi-label segmentation, you should merge all segmentations into a single file.</p>
</blockquote>
</aside>
<p>Thanks for the direction to the video. To help me understand the dataset preparation slide, would the green files be the original, not segmented scans, and the red files be the single file multi-label segmentations?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e0835d7b75c5be63ef1d677f654debe96074d7b.jpeg" alt="image" data-base62-sha1="8QLc0AVQ9VGvBdBI8Y7Kxxmpf2b" width="158" height="214"><br>
Separately, would my segmentations already be in a single file if they were created at the same time and saved as an .mrb file together? Would it be best to simply ‘export to label’ the multi-segmented files and store it as .nii.gz if I am not sure how it is currently arranged?</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="15" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>If using the Segmentation model, you don’t need to specify the background label</p>
</blockquote>
</aside>
<p>Does this mean that I would have to remove the background label if it was previously added, or would it still function properly if it was already listed?</p>
<aside class="quote no-group" data-username="rbumm" data-post="14" data-topic="27504" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>BTW have you tried TotalSegmenator for analyzing your data? It should be able to segment the bones you mentioned out of the box.</p>
</blockquote>
</aside>
<p>I do not have much experience using Total Segmentator, but looked into it. I did not think that it would work best for segmenting the specific type of MRI sequence being used, since it associated with CT scans, so it seemed best to train a new model.</p>
<p>Thank you!</p>

---

## Post #17 by @diazandr3s (2023-03-20 22:14 UTC)

<p>Hi <a class="mention" href="/u/jacobd">@JacobD</a>,</p>
<blockquote>
<p>would the green files be the original, not segmented scans, and the red files be the single file multi-label segmentations?</p>
</blockquote>
<p>Green files are the volumes. Red files located in <strong>labels/final</strong> folder are the ground truth/expert annotations of green files (volumes)</p>
<blockquote>
<p>Separately, would my segmentations already be in a single file if they were created at the same time and saved as an .mrb file together? Would it be best to simply ‘export to label’ the multi-segmented files and store it as .nii.gz if I am not sure how it is currently arranged?</p>
</blockquote>
<p>Not sure if I understood this correctly. In order to use MONAI Label + Slicer, annotations should be in a single file per volume. Regardless if they are single or multiple annotations per volume.</p>
<blockquote>
<p>Does this mean that I would have to remove the background label if it was previously added, or would it still function properly if it was already listed?</p>
</blockquote>
<p>You shouldn’t have an issue with the background label</p>
<p>Hope this helps,</p>

---

## Post #18 by @Pragnesh_Patel (2023-11-20 04:39 UTC)

<p>“I encountered a NameError: name ‘AddChanneld’ is not defined in my MONAI code. I suspect there might be a typo or a misnaming issue. Has anyone experienced a similar error, and can you provide guidance on resolving this issue? The specific line of code causing the error seems to involve the term ‘AddChanneld.’ Should it be ‘AddChannel,’ or is there a specific function or import that I might be missing?”</p>

---

## Post #19 by @rbumm (2023-11-20 13:36 UTC)

<p>Did you install MonaiLabel as <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html" rel="noopener nofollow ugc">we have recommended here</a> ?<br>
Please provide some system and dataset specifications.<br>
Is the MonaiLabel server starting without errors ? If not please post the complete error message.</p>

---

## Post #20 by @Pragnesh_Patel (2023-11-21 03:54 UTC)

<p>NameError                                 Traceback (most recent call last)<br>
 in &lt;cell line: 16&gt;()<br>
30     ).to(device)<br>
31<br>
—&gt; 32     data_in = prepare(data_dir, cache=True)<br>
33<br>
34     <span class="hashtag-raw">#loss_function</span> = DiceCELoss(to_onehot_y=True, sigmoid=True, squared_pred=True, ce_weight=calculate_weights(1792651250,2510860).to(device))</p>
<p> in prepare(in_dir, pixdim, a_min, a_max, spatial_size, cache)<br>
79             LoadImaged(keys=[“vol”, “seg”]),<br>
80             # EnsureChannelFirst(),<br>
—&gt; 81             AddChanneld(keys=[“vol”, “seg”]),<br>
82             Spacingd(keys=[“vol”, “seg”], pixdim=pixdim, mode=(“bilinear”, “nearest”)),<br>
83             Orientationd(keys=[“vol”, “seg”], axcodes=“RAS”),</p>
<p>NameError: name ‘AddChanneld’ is not defined</p>

---

## Post #21 by @rbumm (2023-11-21 05:49 UTC)

<aside class="quote no-group" data-username="Pragnesh_Patel" data-post="20" data-topic="27504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pragnesh_patel/48/68377_2.png" class="avatar"> Pragnesh_Patel:</div>
<blockquote>
<p>NameError Traceback (most recent call last)<br>
in &lt;cell line: 16&gt;()<br>
30 ).to(device)<br>
31<br>
—&gt; 32 data_in = prepare(data_dir, cache=True)<br>
33<br>
34 <span class="hashtag-raw">#loss_function</span> = DiceCELoss(to_onehot_y=True, sigmoid=True, squared_pred=True, ce_weight=calculate_weights(1792651250,2510860).to(device))</p>
<p>in prepare(in_dir, pixdim, a_min, a_max, spatial_size, cache)<br>
79 LoadImaged(keys=[“vol”, “seg”]),<br>
80 # EnsureChannelFirst(),<br>
—&gt; 81 AddChanneld(keys=[“vol”, “seg”]),<br>
82 Spacingd(keys=[“vol”, “seg”], pixdim=pixdim, mode=(“bilinear”, “nearest”)),<br>
83 Orientationd(keys=[“vol”, “seg”], axcodes=“RAS”),</p>
</blockquote>
</aside>
<p>I think this is code from the MONAI framework and you are in the wrong forum here. Sorry we can not help with such limited information.</p>

---
