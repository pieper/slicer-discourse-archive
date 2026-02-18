# vtkMRMLScalarVolumeNode to SimpleITK image

**Topic ID**: 645
**Date**: 2017-07-07
**URL**: https://discourse.slicer.org/t/vtkmrmlscalarvolumenode-to-simpleitk-image/645

---

## Post #1 by @gulamhus (2017-07-07 15:44 UTC)

<p>Hello all in the Slicer Forum.</p>
<p>I write an python Extension for Slicer and have the following Code that produces an error in the last line:</p>
<pre><code>  for i in range(0, len(inputPlanes)):
    n = slicer.vtkMRMLScalarVolumeNode()  
    tempVolName = "tempVol_" + str(i)
    n.SetName(tempVolName)
    slicer.mrmlScene.AddNode(n)

    ### Compute the temporal volume using the CLI module brainsresample
    cliParams = {'inputVolume': inputPlane.GetID(), 'referenceVolume': referenceVolume.GetID(), 'outputVolume' : n.GetID()}
    cliNode = slicer.cli.run(slicer.modules.brainsresample, None, cliParams)

    itkImageVolume = sitkUtils.PullFromSlicer(n.GetName()) # throws error
</code></pre>
<p>for the last line I get the following intepreter error:</p>
<pre><code>Traceback (most recent call last):
File "D:/repositories/My Slicer Extention/StVRegistration/StVRegistration/StVRegistration/StVRegistration.py", line 176, in onApplyButton
logic.run(inputPlanes, self.referenceVolumeSelector.currentNode(), self.outputVolumeSelector.currentNode())
File "D:/repositories/My Slicer Extention/StVRegistration/StVRegistration/StVRegistration/StVRegistration.py", line 296, in run
tempPlaneVol = sitkUtils.PullFromSlicer(n.GetName())
File "C:\Program Files\Slicer 4.7.0-2017-06-26\bin\Python\sitkUtils.py", line 100, in PullFromSlicer
sitkimage = sitk.ReadImage(myNodeFullITKAddress)
File "C:\Program Files\Slicer 4.7.0-2017-06-26\lib\Python\Lib\site-packages\SimpleITK\SimpleITK.py", line 8335, in ReadImage
return _SimpleITK.ReadImage(*args)
RuntimeError: Exception thrown in SimpleITK ReadImage: D:\D\N\Slicer-1-build\SimpleITK\Code\IO\src\sitkImageReaderBase.cxx:264:
sitk::ERROR: Logic error!
</code></pre>
<p>However, if I type the same last line in the interactive python console in Slicer after performing the script of the module it works just fine. Does anybody know what is going on there?</p>
<p>For the <strong>CLI module brainsresample</strong> I need <em>vtkMRMLScalarVolumeNodes</em> as input but later I want to use <strong>simpleITK</strong> within the python script and therefor need <em>SimpleITK images</em>. How would I go about it?</p>
<p>What I try here is<br>
Thanks for your Reply</p>

---

## Post #2 by @ihnorton (2017-07-07 15:47 UTC)

<p>Try adding <code>wait_for_completion=True</code> in the <code>slicer.cli.run</code> call.</p>

---

## Post #3 by @gulamhus (2017-07-07 17:32 UTC)

<p>That did help thank you. =)</p>

---
