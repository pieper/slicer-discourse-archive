---
topic_id: 20287
title: "Converting Stl To Nifti Without Showing Gui"
date: 2021-10-21
url: https://discourse.slicer.org/t/20287
---

# Converting .stl to nifti without showing GUI

**Topic ID**: 20287
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/converting-stl-to-nifti-without-showing-gui/20287

---

## Post #1 by @ThijsvD (2021-10-21 14:36 UTC)

<p>For the registration of multiple binairy STL files of a femur bone, I want to use Elastix. I need the transformation / rotation matrices as well for the further project. To use Elastix properly I have to convert the STL to a niftii file, so it works with ther program and stays on the same place in the coordinate system. I have a couple questions:</p>
<ul>
<li>I’m using the Python code beneath. I’m running it in Visual Studio Code, not in 3D slicer, is that necessary? Maybe that is the reason for the Error. If not, how can I solve the error?</li>
<li>Is there another easier way to convert the STL to a niftii?</li>
<li>Is there another easier way to registrate two STL’s (while keeping the same coordinate systems)?</li>
</ul>
<p>Thanks for your help in advance! Kind Regards.</p>
<pre><code class="lang-python">    segmentationNode = util.loadSegmentation(stl_file_name)
    outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, outputLabelmapVolumeNode)
    slicer.util.saveNode(outputLabelmapVolumeNode, output_file_name)


I get the following error:

**---------------------------------------------------------------------------** **ImportError** Traceback (most recent call last) **

&lt;ipython-input-10-bde7d0eba18b&gt;** in &lt;module&gt; 31 output_file_name **=** **"vol_stat_T_R.nii"** 32 **---&gt; 33** segmentationNode **=** util **.** loadSegmentation **(** stl_file_name **)** 34 outputLabelmapVolumeNode **=** slicer **.** mrmlScene **.** AddNewNodeByClass **(** **'vtkMRMLLabelMapVolumeNode'** **)** 35 slicer **.** modules **.** segmentations **.** logic **(** **)** **.** ExportVisibleSegmentsToLabelmapNode **(** segmentationNode **,** outputLabelmapVolumeNode **)** 

**c:\Users\Acer\Desktop\TM-II\Stages-TM\Stage_4\Thijs van Deudekom\Slicer\Base\Python\slicer\util.py** in loadSegmentation **(filename, returnNode)** 796 If returnNode **is** **True** then a status flag **and** loaded node are returned **.** 797 """ **--&gt; 798 ****return****** loadNodeFromFile **(** filename **,** **'SegmentationFile'** **,** **{** **}** **,** returnNode **)** 799 800 **def** loadTransform **(** filename **,** returnNode **=** **False** **)** **:** 

**c:\Users\Acer\Desktop\TM-II\Stages-TM\Stage_4\Thijs van Deudekom\Slicer\Base\Python\slicer\util.py** in loadNodeFromFile **(filename, filetype, properties, returnNode)** 629 **:** raises RuntimeError **:** **in** case of failure 630 """ **--&gt; 631 ****from****** Base **.** Python **import** mrml 632 **from** vtk **import** vtkCollection 633 properties **[** **'fileName'** **]** **=** filename **ImportError** : cannot import name 'app' from 'slicer' (C:\Users\Acer\Miniconda3\lib\site-packages\slicer\__init__.py)
</code></pre>

---

## Post #2 by @lassoan (2021-10-22 18:12 UTC)

<p>You need to run these scripts in Slicer’s Python environment or <a href="https://github.com/Slicer/SlicerJupyter">Slicer’s Jupyter kernel</a>. You can configure Visual Studio Code to use Slicer’s Python (such as <code>c:\Users\yourusername\AppData\Local\NA-MIC\Slicer...\bin\PythonSlicer.exe</code>) as Python interpreter.</p>

---

## Post #3 by @pleuvoir (2022-02-28 07:23 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi, I chose the second option you mentioned when I used Python to convert the.nrrd file to nifti without displaying the GUI:<br>
I used the pythonSlicer.exe in the Slicer installation directory as the virtual environment for my project when I created it.  My program prompts the following error after execution:<br>
No module named ‘logic’<br>
Traceback (most recent call last):<br>
File “D:/software/PycharmProjects/For_Xv_of_Tinti/main.py”, line 290, in <br>
execute(slicer)<br>
File “D:/software/PycharmProjects/For_Xv_of_Tinti/main.py”, line 106, in execute<br>
slicer.util.loadSegmentation(codePath+’/L2.nii’)<br>
File “D:\software\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 801, in loadSegmentation<br>
return loadNodeFromFile(filename, ‘SegmentationFile’, {}, returnNode)<br>
File “D:\software\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 634, in loadNodeFromFile<br>
from slicer import app<br>
ImportError: cannot import name ‘app’<br>
I have tried many methods but failed to solve it. I hope to get your help. Thank you very much!</p>

---

## Post #4 by @lassoan (2022-03-13 05:51 UTC)

<p>If you want to use any Slicer application features then you need to run your script not just in a Slicer virtual Python environment but Slicer application’s Python environment (by starting the Slicer application and passing your Python script to it).</p>

---
