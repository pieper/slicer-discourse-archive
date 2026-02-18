# reload slicerrc.py without having to restart slicer

**Topic ID**: 6638
**Date**: 2019-04-29
**URL**: https://discourse.slicer.org/t/reload-slicerrc-py-without-having-to-restart-slicer/6638

---

## Post #1 by @maxaerosat.co.za (2019-04-29 03:08 UTC)

<p>I somehow can create new customised  volume rendering presets as per explanations<br>
however at present need to restart slicer to see the effects as i need the slicerrc.py file to be read</p>
<p>Is there a way to re read the slicerrc.py file without having to restart slicer</p>
<p>ps : is there anywhere a good detailed explanation for all the settings in custom volume presets<br>
ie the format of the numbers ; pairs / triplets  etc<br>
Thanks<br>
Greatly appreciated</p>

---

## Post #2 by @lassoan (2019-04-29 03:14 UTC)

<p>You can experiment with copy-pasting code to the Python console. Once you have the final code snippet, you can put it in your .slicerrc file.</p>
<p>Format of volume property file is described in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#Format_of_Volume_Property_.28.vp.29_file" rel="nofollow noopener">volume rendering module documentation</a>. Volume rendering transfer functions are explained in <a href="https://www.kitware.com/products/books/VTKTextbook.pdf" rel="nofollow noopener">VTK textbook</a>.</p>

---

## Post #3 by @maxaerosat.co.za (2019-05-12 12:11 UTC)

<p>Thanks for the reply ; Have achieved what i wanted  ( the long way )  multiple anchor points on a preset and alter them when using slicer   ; I came across this code   propNode = displayNode.GetVolumePropertyNode()<br>
volumeProp = propNode.GetVolumeProperty()<br>
slicer.modules.volumerendering.logic().SetThresholdToVolumeProp(self.scalarRange,[thresholdLevel - thresholdWindow/2, thresholdLevel + thresholdWindow/2],volumeProp,True,True)<br>
color = vtk.vtkColorTransferFunction()<br>
color.AddRGBPoint(-3000, 0, 0, 0)<br>
color.AddRGBPoint(thresholdLevel-self.thresholdWindow/2, 0.6, 0.3, 0.2)<br>
color.AddRGBPoint(thresholdLevel, 1.0, 1.0, 1.0)<br>
color.AddRGBPoint(thresholdLevel+self.thresholdWindow/2, 1.0, 0.9, 0.9)<br>
color.AddRGBPoint(3000, 0.8, 0.7, 1.0)<br>
volumeProp.SetColor(color)<br>
from another discussion  ;<br>
which i can find verry useful ;<br>
however when i try it the volume does not respond  ; ie aware the line with the feachure  i want is the second last  and need to alter the x position and the corresponding rgb values , slicer find no error in the code   but the volume does not respond with the altered values ; any advice would be useful to me</p>

---
