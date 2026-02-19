---
topic_id: 40213
title: "Script Cli Module Output Volume Fails"
date: 2024-11-15
url: https://discourse.slicer.org/t/40213
---

# Script cli module output volume fails

**Topic ID**: 40213
**Date**: 2024-11-15
**URL**: https://discourse.slicer.org/t/script-cli-module-output-volume-fails/40213

---

## Post #1 by @fqzhice (2024-11-15 08:11 UTC)

<p>i called i scriptd cli module and outputvolume is vtkMRMLVectorVolumeNode</p>
<p>Here is code in ctacli.py file and fusion_image is np array</p>
<pre><code class="lang-auto">ImageType = itk.Image[itk.F, 3]
itk_image = itk.PyBuffer[ImageType].GetImageFromArray(fusion_image)
writer = itk.ImageFileWriter[ImageType].New()
writer.SetFileName(sys.argv[6])
writer.SetInput(itk_image)
writer.UseCompressionOn()
writer.Update();
</code></pre>
<p>In main thread:</p>
<pre><code class="lang-auto">    fusion_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLVectorVolumeNode", "bone_blended")
    params['outputVolume']=fusion_node.GetID() 
    # ID is  C:/Users/xxx/AppData/Local/Temp/Slicer/CEGJC_vtkMRMLVectorVolumeNodeB.nrrd when running
    cliNode=slicer.cli.run(slicer.modules.ctacli,None, parameters=params,wait_for_completion=True)
    fusion_image= slicer.util.arrayFromVolume(fusion_node)
</code></pre>
<p>It runs without error when calling ctacli.py, but the file doesn’t exists.</p>
<p>output error is as below:</p>
<p>…</p>
<p>ctacli completed without errors</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node (vtkMRMLVectorVolumeNode1) from filename=‘C:/Users/xxx/AppData/Local/Temp/Slicer/CEGJC_vtkMRMLVectorVolumeNodeB.nrrd’</p>
<p>…</p>

---

## Post #2 by @pieper (2024-11-15 21:15 UTC)

<p>To help you get help, it could be good to follow the guidelines here: <a href="https://sscce.org/">https://sscce.org/</a></p>

---

## Post #3 by @fqzhice (2024-11-16 12:10 UTC)

<p>I mean that with the above code , script cli module cant generate output nrrd file and i dont know how to fix it</p>
<p>Thanks for you reply</p>

---

## Post #4 by @pieper (2024-11-16 17:27 UTC)

<p>What I meant by suggesting you look at the SSCCE guidance is that it’s difficult for others on this forum to help when you post fragments of code rather than a complete example.  I can look at what you posted and maybe guess what’s going on but it’s also possible that your issue lies with some other code.  The process of making the smallest possible example that replicates the issue you are asking about  often leads you to solve the problem yourself, so it helps everyone.</p>

---

## Post #5 by @fqzhice (2024-11-21 03:39 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
very grateful for your help and i will try later.</p>
<p>About this question,  it is very  urgent for me to do a simple example. i am sorry for that.</p>
<p>for output vtkMRMLVecotrVolumeNode in this script. i try to convert from numpy array [1000,1000,3] , then it fails. At last , i expanded the numpy dimension and it works. itk or simple itk api both fulfill the requirement</p>
<p>just add ‘fusion_image = np.expand_dims(fusion_image, axis=0)’ before outpu t *.nrrd file</p>

---
