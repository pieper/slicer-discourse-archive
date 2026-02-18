# Running Slicer from PyCharm/external

**Topic ID**: 37095
**Date**: 2024-06-29
**URL**: https://discourse.slicer.org/t/running-slicer-from-pycharm-external/37095

---

## Post #1 by @b_srf (2024-06-29 04:35 UTC)

<p>Hello! I want to run a python script for Slicer from PyCharm. I’m using the SegmentEditor module and PyRadiomics, and would like to automate the process for batch processing.</p>
<p>I’m able to write a script that runs on Slicer’s python console but I can’t figure out how to run it from PyCharm. I’m aware slicer has a debugger on pycharm and I tried setting slicer’s python.exe as the interpreter in pycharm. It hasn’t worked for me. Would anyone be able to advise?</p>

---

## Post #2 by @muratmaga (2024-06-29 04:43 UTC)

<p>Is there a reason you want to do this from PyCharm? This sounds more suitable for Jupyter notebooks?</p>
<p>See <a href="https://github.com/Slicer/SlicerJupyter" class="inline-onebox">GitHub - Slicer/SlicerJupyter: Extension for 3D Slicer that allows the application to be used from Jupyter notebook</a></p>

---

## Post #3 by @rfenioux (2024-07-01 10:18 UTC)

<p>The python interpreter of slicer can’t run on its own, you need the slicer environment if you use the modules and/or the slicer API.</p>
<p>You can run a python script in the slicer environment using this command :<br>
<code>Slicer.exe --python-script "/full/path/to/myscript.py" --no-splash --no-main-window</code></p>
<p>I haven’t tried but you can probably configure pycharm to execute this command for you if you want to stay in pycharm.</p>

---

## Post #4 by @b_srf (2024-07-03 18:59 UTC)

<p>Thank you for the suggestions! I was able to do what I needed with Jupyter. I wanted to do it on PyCharm since it was what I was familiar with.</p>

---

## Post #5 by @b_srf (2024-07-04 20:00 UTC)

<p>I ran into a problem with my code. Below is a snippet. When I want to export the features table, the csv is empty; it just has the headers. I think this is because the feature extractor is not done working and the table is already exported as csv, because when I wait for the extracted to be done then save as table, it works fine. However, this won’t be good if I have to do this for every time I extract the features. Can you by any chance advise how to go about this?</p>
<pre><code class="lang-auto">inputSeg = slicer.util.getNode("Segmentation")
radiomicsModule = slicer.modules.SlicerRadiomicsWidget
radiomicsModule.inputVolumeSelector.setCurrentNode(volNode)
radiomicsModule.inputMaskSelector.setCurrentNode(inputSeg)
radiomicsModule.manualCustomizationRadioButton.setChecked(True)

#firstorder feature selected by default

radiomicsModule.onApplyButton()

outputTableNode = radiomicsModule.outputTableSelector.currentNode()
outputFilePath = r"path to file"
slicer.util.saveNode(outputTableNode, outputFilePath)
</code></pre>

---
