---
topic_id: 10007
title: "Median Image Fiter Command Line"
date: 2020-01-29
url: https://discourse.slicer.org/t/10007
---

# Median Image Fiter - command line

**Topic ID**: 10007
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/median-image-fiter-command-line/10007

---

## Post #1 by @Adam1122 (2020-01-29 19:24 UTC)

<p>Hello all, please, how can I invoke the tool MedianImageFilter through command line?</p>
<p>My Slicer.exe is here: C:\Program Files\Slicer 4.10.2 and MedianImageFilter tools are here: C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10</p>
<p>When I just type “MedianImageFilter” the error message appears that the ITKFactoryRegistration.dll code is not installed. Please, am I doing it right? Please, could you navigate me? I am new to 3D Slicer.</p>
<p>Thanks a lot<br>
Regards<br>
Adam</p>

---

## Post #2 by @Juicy (2020-01-29 20:57 UTC)

<p>Hi Adam.</p>
<p>I am certainly not an expert on Slicer programming but if you want to use the median image filter through the python interactor I think this is what you are after…</p>
<p>I have modified this code from the script repository entry <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK" rel="nofollow noopener">here</a>. First go to the data module and remane the volume which you would like to apply the filter to “myvolume”. Then copy and paste the following script into the python interactor.</p>
<pre><code>import SimpleITK as sitk
import sitkUtils

# Get input volume node
inputVolumeNode = slicer.util.getNode('myvolume')

# Create new volume node for output
outputVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', 'Median Filtered Volume')

# Run Processing
inputImage = sitkUtils.PullVolumeFromSlicer(inputVolumeNode)
filter = sitk.MedianImageFilter()
# Set inputs for the itk median image filter here
filter.SetRadius(1)
outputImage = filter.Execute(inputImage)
sitkUtils.PushVolumeToSlicer(outputImage, outputVolumeNode)

# Show processed Volume
slicer.util.setSliceViewerLayers(background=outputVolumeNode)
</code></pre>
<p>The median filter only takes one input and that is ‘radius’ I have set the radius in the code to 1 as you can see in the line filter.SetRadius(1). You can change the radius input here.</p>
<p>Use this same code structure for using any of the ITK filters. In the python interactor you can type “filter = sitk.” and then press tab to see all the itk filters which are avaliable. It is also useful to find the filter GUI in the “Simple Filters” module to see which input settings the filter has. Then press “filter.Set” and then press tab to find the settings which are available to change for that filter.</p>
<p>Hope this is what you were after.</p>

---

## Post #3 by @pieper (2020-01-29 21:41 UTC)

<p>Yes, running in Slicer with SimpleITK is a good option.</p>
<p>Or if you want to run the module executable directly you need to use the <code>--launch</code> option like this:</p>
<pre><code class="lang-auto">C:\Program Files\Slicer 4.10.2\Slicer.exe --launch MedianImageFilter
</code></pre>

---
