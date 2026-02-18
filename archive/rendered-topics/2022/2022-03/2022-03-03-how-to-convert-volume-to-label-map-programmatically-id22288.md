# How to convert volume to label map programmatically

**Topic ID**: 22288
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/how-to-convert-volume-to-label-map-programmatically/22288

---

## Post #1 by @koeglfryderyk (2022-03-03 14:35 UTC)

<p>I know how to do it in the GUI (go to ‘Volumes’ and at the bottom of ‘Volume Information’ go to ‘Convert to label map’).</p>
<p>I found the corresponding function to be:</p>
<pre><code class="lang-auto">void qSlicerVolumesModuleWidget::convertVolume()
</code></pre>
<p>But I cannot figure out how to access the function.</p>
<p>I can get<br>
<code>qSlicerVolumesModuleWidget</code><br>
with<br>
<code>slicer.util.getModuleWidget('Volumes')</code><br>
but it does not have the <code>convertVolume()</code> method (contrary to the <a href="https://apidocs.slicer.org/master/classqSlicerVolumesModuleWidget.html" rel="noopener nofollow ugc">documentation</a>)</p>
<p>Am I missing something or is this a bug?</p>

---

## Post #2 by @mikebind (2022-03-03 18:27 UTC)

<p>The <code>convertVolume()</code> method is present in the current Slicer code <a href="https://github.com/Slicer/Slicer/blob/cb3a1ff14fac3419f3e3f08632a6cac6bedb52ca/Modules/Loadable/Volumes/qSlicerVolumesModuleWidget.cxx#L151" class="inline-onebox">Slicer/qSlicerVolumesModuleWidget.cxx at cb3a1ff14fac3419f3e3f08632a6cac6bedb52ca · Slicer/Slicer · GitHub</a>, but I can confirm that it does not seem to be accessible from Python any way I can figure out either. Maybe something has gone wrong with the wrapping?</p>
<p>As a hack workaround, you could programmatically press the button in the Volumes module as follows:</p>
<pre><code class="lang-auto">w = slicer.util.getModuleWidget('Volumes')
convertButton = slicer.util.findChild(w, 'ConvertVolumeButton')
convertButton.clicked()
</code></pre>
<p>You would need to select the active volume in the module (and the target node if you aren’t replacing the input node) if you were to go this route.</p>
<p>Alternatively, you could look at the code inside the <code>convertVolume()</code> method and reimplement it in your own module.</p>

---

## Post #3 by @koeglfryderyk (2022-03-03 20:16 UTC)

<p>Another workaround: create a label-map volume node from the pixel data of the volume node</p>
<ol>
<li>
<p>get the volume node data that you want to convert to a label map:</p>
<pre><code class="lang-auto">volume_node = slicer.util.getFirstNodeByName(volume_name)
volume_data = slicer.util.arrayFromVolume(volume_node)
volume_data = volume_data.astype(np.uint8())
</code></pre>
</li>
<li>
<p>Create a new label map volume node (or use an existing one):</p>
<pre><code class="lang-auto">label_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
</code></pre>
</li>
<li>
<p>Place the volume data into the label map node:</p>
<pre><code class="lang-auto">slicer.util.updateVolumeFromArray(label_node, volume_data)
</code></pre>
</li>
<li>
<p>The new label-map volume node will probably have a different IJKToRAS matrix (and origin), so update them with the ones from the original volume node</p>
<pre><code class="lang-auto">volume_matrix = vtk.vtkMatrix4x4()
volume_node.GetIJKToRASMatrix(volume_matrix)
volume_origin = volume_node.GetOrigin()

label_node.SetIJKToRASMatrix(volume_matrix)
label_node.SetOrigin(volume_origin)
</code></pre>
</li>
</ol>

---

## Post #4 by @mikebind (2022-03-03 20:30 UTC)

<p>Also, I just looked a little deeper, and the functionality you originally wanted (and pretty much recreated) is available through the following:</p>
<pre><code class="lang-auto">volume_node = slicer.util.getFirstNodeByName(volume_name)
label_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
volumes_logic = slicer.modules.volumes.logic()
volumes_logic.CreateLabelVolumeFromVolume(slicer.mrmlScene, label_node, volume_node)
</code></pre>
<p>This function requires a labelmap node, so it, by itself, does not handle the case where you want to created labelmap node to replace the original scalar volume node, but it does duplicate the functionality in the code you just shared, where you get a new labelmap node created from the volume node.</p>
<p>The <code>CreateLabelVolumeFromVolume</code> method code is here <a href="https://github.com/Slicer/Slicer/blob/409c7f035aa9015863cffc827ed37661322a550d/Modules/Loadable/Volumes/Logic/vtkSlicerVolumesLogic.cxx#L843" class="inline-onebox">Slicer/vtkSlicerVolumesLogic.cxx at 409c7f035aa9015863cffc827ed37661322a550d · Slicer/Slicer · GitHub</a></p>

---
