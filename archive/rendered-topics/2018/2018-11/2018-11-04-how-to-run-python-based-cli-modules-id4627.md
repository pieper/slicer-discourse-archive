---
topic_id: 4627
title: "How To Run Python Based Cli Modules"
date: 2018-11-04
url: https://discourse.slicer.org/t/4627
---

# How to run python based CLI modules?

**Topic ID**: 4627
**Date**: 2018-11-04
**URL**: https://discourse.slicer.org/t/how-to-run-python-based-cli-modules/4627

---

## Post #1 by @Saima (2018-11-04 05:08 UTC)

<p>I have gone through this<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Python" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Python</a></p>
<p>So, what I understand about python based CLI is:<br>
there is an xml file which will produce GUI for application and the same xml is used by the .py file to parse elements.<br>
the execute function is in the xml file that will be run by slicer and the name of the script .py file is within this function.</p>
<p>how to run and test the python based cli module?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @pieper (2018-11-04 16:13 UTC)

<p>Hi Saima -</p>
<p>For a new style python scripted cli, you can run like you would any other cli.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>
<p>E.g.</p>
<pre><code class="lang-auto">node = slicer.cli.runSync(slicer.modules.slicerradiomicscli)
print(node)
</code></pre>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @Saima (2018-11-06 09:59 UTC)

<p>How to run and test newly created cli modules?<br>
and how do you get the GUI for newly created CLI module?</p>
<p>I am new  in this and I want to create a python based CLI module. The module will take input image send it to external python file for execution (as python 3 external libraries are required) and return the resultant image.</p>
<p>Please help me as I could not understand how to do this?</p>
<p>I have found this script<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Python" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Python</a></p>
<p>I need to do this but I do not know how I can do this in slicer?</p>
<p>Do I need to build with cmake. then create a scripted module for the cli and then run thought the scripted module?</p>
<p>Please guide how can I create python based CLI modules</p>

---

## Post #4 by @pieper (2018-11-06 16:36 UTC)

<p>Hi <a class="mention" href="/u/saima">@Saima</a> -</p>
<p>As it says at the top of the page you linked that older style was only supported in Slicer 3.x.  There is a new style for Slicer 4.x that you can follow like in <a href="https://github.com/Radiomics/SlicerRadiomics/tree/master/SlicerRadiomicsCLI">this repository</a>.</p>
<p>The description of the parameters goes in the .xml file, and the script to run is the .py file.</p>
<p>You can also look at the <a href="https://github.com/Slicer/Slicer/tree/master/Base/QTCLI/Testing">PyCLIModule tests here</a>.</p>
<p>I haven’t tried running python3 - you will probably run into environment variable issues.  <a class="mention" href="/u/ihnorton">@ihnorton</a> did you have any suggestions for that?</p>

---

## Post #5 by @Saima (2018-11-07 09:58 UTC)

<p>Thank you so much for replying.</p>
<p>I will look into the things you suggested and will come back again.</p>

---

## Post #6 by @Saima (2018-11-21 12:50 UTC)

<p>Hi,<br>
How can you put a newly written python based cli into slicer?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #7 by @pieper (2018-11-21 18:28 UTC)

<p>You should be able to just add the directory to the module path like you would with a scripted module (module path selector in the preferences dialog)</p>

---

## Post #8 by @Saima (2018-11-22 04:02 UTC)

<p>I added the folder “newfuzzypython” containing the example .py and .xml. Like below in the screen shot.<br>
Is it correct? How can I see this in slicer. I dont see any new module added to module section.<br>
Sorry, if i am asking general questions. I am new to this environment. Trying to understand.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3829731f10816d86d16d6bd1133a0a420ad43625.png" data-download-href="/uploads/short-url/80PxIL9hZm9ax88cIoNENQv1Jbv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3829731f10816d86d16d6bd1133a0a420ad43625_2_690x388.png" alt="image" data-base62-sha1="80PxIL9hZm9ax88cIoNENQv1Jbv" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3829731f10816d86d16d6bd1133a0a420ad43625_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3829731f10816d86d16d6bd1133a0a420ad43625_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3829731f10816d86d16d6bd1133a0a420ad43625_2_1380x776.png 2x" data-dominant-color="EAECED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2018-11-22 16:59 UTC)

<p>Could you upload your source code to GitHub and post the link here so that we can have a look?</p>

---

## Post #10 by @Saima (2018-11-28 10:58 UTC)

<p>Sorry I was away. the issue to load the cli module is resolved. will come back again if I have problems.</p>
<p>Please would you tell me one thing. if I made changes in cli module I have to restart slicer to see those changes. is it the only way to test the new module again and again.</p>

---

## Post #11 by @lassoan (2018-11-28 14:01 UTC)

<aside class="quote no-group" data-username="Saima" data-post="10" data-topic="4627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Please would you tell me one thing. if I made changes in cli module I have to restart slicer</p>
</blockquote>
</aside>
<p>There is no need to restart Slicer to test changes. You can reload your module by clicking “Reload” button at the top of your scripted module user interface. Make sure you use a module template generated by a recent version of Extension Wizard module, and enable “Developer mode” in application settings.</p>

---

## Post #12 by @Saima (2018-11-30 03:29 UTC)

<p>Dear Andras,<br>
when I create scripted python module I do find restore and the changes reflect but when I am working with cli based python module I could not see a reload button. the template produces this as below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2999e6080adf7c2d8511e8d59c9a730a24eb9f97.png" alt="image" data-base62-sha1="5W1iKyfBkmyWhHpHrQwDvPA8Tob" width="298" height="169"></p>

---

## Post #13 by @lassoan (2018-12-01 15:39 UTC)

<p>For Python CLIs you don’t even need to click Reload, as when you click Apply then always the current version of the code is used.</p>
<p>If you update the GUI (the XML description) then you need to restart Slicer to see the changes, but since it is just a descriptive text, it should not require frequent modifications or debugging.</p>

---

## Post #14 by @Timberwolf009 (2022-05-03 16:04 UTC)

<p>Hello,</p>
<p>I was able to follow the instructions above and it worked fine for the moment. I just had a quick question:</p>
<p>I’m using a script to automate extraction of radiomics features after histogram matching. I’m using the radiomics CLI module for this. However, I’m not sure how to import a params.yaml file into slicer so I can use it for radiomics extraction. Should I directly import it using a python function or is there a slicer function I can use e.g. the “loadNodeFromFile” function</p>
<p>Thanks</p>

---

## Post #15 by @lassoan (2022-05-03 23:19 UTC)

<p>I don’t think you need to load the file, just pass the filename. This <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L871-L908">automatic test</a> could be a useful example.</p>

---

## Post #16 by @Timberwolf009 (2022-05-05 21:33 UTC)

<p>Yes that worked out. Thank you!</p>
<p>However, now I have a new problem. I have attached my code below. I’m trying to extract radiomics features from a node called “Pref_hist” using a segmentation node but the parameter file is not considered during the extraction of raiomics features. I manually extracted radiomics using the interative module and compared the values and it turns out that the parameter set supplied in the “param” argument is not considered (or is being ignored). I have also attached a copy of the params file as a jpg here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee72e5ecf756d20c666ce9d055c148120646b159.jpeg" data-download-href="/uploads/short-url/y1pNYGYAGWNVkiSRRlHzJqunQbT.jpeg?dl=1" title="Parameter_File_Img" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee72e5ecf756d20c666ce9d055c148120646b159_2_690x335.jpeg" alt="Parameter_File_Img" data-base62-sha1="y1pNYGYAGWNVkiSRRlHzJqunQbT" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee72e5ecf756d20c666ce9d055c148120646b159_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee72e5ecf756d20c666ce9d055c148120646b159_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee72e5ecf756d20c666ce9d055c148120646b159_2_1380x670.jpeg 2x" data-dominant-color="F4F7F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Parameter_File_Img</span><span class="informations">1411×686 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Please let me know if you have any suggestions.</p>
<p><span class="hashtag">#Create</span> a new blank table to store radiomics<br>
tableNode=slicer.vtkMRMLTableNode()<br>
tableNode.SetName(“Pre”)</p>
<p>slicer.mrmlScene.AddNode(tableNode)<br>
radiomics=slicer.modules.slicerradiomicscli</p>
<p><span class="hashtag">#Parameters</span> for radiomics extraction<br>
parameters_rad={}<br>
parameters_rad[“Image”]=Pre_hist<br>
parameters_rad[“Mask”]=getNode(‘Segmentation’)<br>
parameters_rad[“param”]={Location of file “Parameter_File.yaml” attached in screenshot}<br>
parameters_rad[“out”]=tableNode<br>
node_rad=slicer.cli.runSync(radiomics,None,parameters_rad)</p>

---

## Post #17 by @lassoan (2022-05-05 22:26 UTC)

<p>You can have a look at the application log to see the command-line arguments that are generated from your <code>parameters_rad</code> variable. Compare it to the command-line arguments that are generated when you run the interactive module.</p>

---

## Post #18 by @Thu_n_Chu_th (2022-08-02 10:41 UTC)

<p>hi Lassoan!<br>
3D slicer is very convinnent in analysis medical images, specially show 3D models.<br>
recently, I want to combine my deep learning code python with 3D slicer.<br>
it is the algorithm for segmenting the liver in CT images on pytorch.<br>
but I don’t know how to do this work. can you give me instructions, specific documents, links… for it.<br>
thankyou!!!</p>

---

## Post #19 by @pieper (2022-08-02 15:04 UTC)

<p>You can install PyTorch directly in slicer like this:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/fepegar/SlicerPyTorch">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/fepegar/SlicerPyTorch" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e030cb95a5695191b1b0403d91cddbb2889df6c00dd67b0ff990ab765013d08a/fepegar/SlicerPyTorch" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/fepegar/SlicerPyTorch" target="_blank" rel="noopener">GitHub - fepegar/SlicerPyTorch: This extension contains only a module with...</a></h3>

  <p>This extension contains only a module with some tools to install PyTorch inside Slicer, using the best possible version. - GitHub - fepegar/SlicerPyTorch: This extension contains only a module with...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or you can use your model in something like the MONAI Label server:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Project-MONAI/MONAILabel">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/8b1542d48e5155cc177280fb8822a24445fc1d926bc94034a3c8c127e29be45c/Project-MONAI/MONAILabel" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Project-MONAI/MONAILabel" target="_blank" rel="noopener">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source...</a></h3>

  <p>MONAI Label is an intelligent open source image labeling and learning tool. - GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #20 by @Thu_n_Chu_th (2022-08-02 15:12 UTC)

<p>hi Pieper!<br>
thankyou so much.</p>

---

## Post #21 by @Thu_n_Chu_th (2022-08-02 15:14 UTC)

<p>i have a little question.<br>
do these parts need to install more cmake?</p>

---

## Post #22 by @pieper (2022-08-02 15:18 UTC)

<p>No, not if you do everything in python.</p>

---

## Post #23 by @Thu_n_Chu_th (2022-08-02 16:06 UTC)

<p>Can you give me a tutorial or link on how to combine python code into 3D slicer?<br>
I’ve read a lot of ways but still don’t know how to do it.<br>
Since I am still a student, my ability to analyze documents is still a bit poor. hope you can help me.</p>

---

## Post #24 by @rbumm (2022-08-02 16:25 UTC)

<p>Sure - open the Python interactor:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c13de5b897fe02a565130c41061bfbd7f0de5bd7.png" alt="image" data-base62-sha1="rzuLvtxCz0UEKN5PIxy97YpqNvh" width="439" height="253"></p>
<p>and enter some Python code.</p>
<p>A good starting point for reading is:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>
<p>Copy/paste source code from that page into the Python interactor.</p>
<p>If you want to integrate deep learning source code into 3D Slicer you will probably need a programmer.</p>

---

## Post #25 by @Thu_n_Chu_th (2022-08-02 16:26 UTC)

<p>hi Rbumm!<br>
thankyou so much.</p>

---

## Post #26 by @Thu_n_Chu_th (2022-08-02 16:29 UTC)

<p>Can I ask if the integration of deep learning code is also done on Python interactor?</p>

---

## Post #27 by @Thu_n_Chu_th (2022-08-02 16:32 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/424d06e935554361010dc829968294d1952e2ba8.png" data-download-href="/uploads/short-url/9swxDRiVjY9o9Kg4OLAbS1M4aQE.png?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424d06e935554361010dc829968294d1952e2ba8_2_690x412.png" alt="slicer" data-base62-sha1="9swxDRiVjY9o9Kg4OLAbS1M4aQE" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424d06e935554361010dc829968294d1952e2ba8_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424d06e935554361010dc829968294d1952e2ba8_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/424d06e935554361010dc829968294d1952e2ba8.png 2x" data-dominant-color="969796"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1142×682 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i tried integrating deep learning in this way, but i don’t know is it correct?</p>

---

## Post #28 by @rbumm (2022-08-02 16:33 UTC)

<p>If your deep learning code is written in Python - it probably is. You would need to write a program in Python language and load and test it via the Python interactor.</p>

---

## Post #29 by @rbumm (2022-08-02 16:34 UTC)

<p>This would be a starting point to write your own 3D Slicer extension.</p>
<p>Please remember that this forum is not a chat program and every question you ask pushes the thread up to the beginning again.</p>

---

## Post #30 by @Thu_n_Chu_th (2022-08-02 16:39 UTC)

<p>sorry so much, I’ll keep an eye on this.</p>

---

## Post #31 by @Saima (2023-10-17 05:23 UTC)

<p>Hi Andras,<br>
I am working on running the radiomics cli for batch processing. I want to update the binwidth. I have the following code.</p>
<p>how can I define the binwidth using params.</p>
<pre><code class="lang-auto"> params = {}
            params["Image"] = slicer.util.getNode(apt_data.GetID())
            params["Mask"] = slicer.util.getNode(seg.GetID())
            params["param"] = directoryPath+"/param_file.file.yaml" this line is not working when I run default without passing file it works. 
            params["out"] = t
cliModule = slicer.modules.slicerradiomicscli
                cliNode = slicer.cli.runSync(cliModule, None, params)
</code></pre>
<p>regards,<br>
Saima</p>

---
