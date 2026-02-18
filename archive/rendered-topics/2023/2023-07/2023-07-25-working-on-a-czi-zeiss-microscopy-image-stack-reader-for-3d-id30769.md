# Working on a CZI Zeiss microscopy image stack reader for 3D slicer, any help or advice welcome

**Topic ID**: 30769
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/working-on-a-czi-zeiss-microscopy-image-stack-reader-for-3d-slicer-any-help-or-advice-welcome/30769

---

## Post #1 by @EgorZindy (2023-07-25 01:01 UTC)

<h3><a name="p-98123-some-general-info-1" class="anchor" href="#p-98123-some-general-info-1" aria-label="Heading link"></a>Some general info:</h3>
<p><strong>Operating system:</strong> Windows 10<br>
<strong>Slicer version:</strong> 5.3.0 - 2023.06.17<br>
<strong>Expected behavior:</strong> 3D stack(s) imported from a CZI scene with minimum hassle for the user…<br>
<strong>Actual behavior:</strong> Work in progress, 3D view requires manual adjustments, not fully integrated with Slicer yet.</p>
<p>Hello,</p>
<p>this is my first post here, I am trying to import a multichannel CZI confocal stack into 3D slicer, and found <a href="https://github.com/BodenmillerGroup/napari-czifile2" rel="noopener nofollow ugc">some Python code on GitHub</a> for a napari reader, which I am repurposing for Slicer.</p>
<p>I’m still very far from having a working reader, but the code I have put together is showing some promise:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facd460c2287a0d9d408342507e10918d1a0889e.jpeg" data-download-href="/uploads/short-url/zMHabEaUpGfyfMRFULxx4FE1AOq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facd460c2287a0d9d408342507e10918d1a0889e.jpeg" alt="image" data-base62-sha1="zMHabEaUpGfyfMRFULxx4FE1AOq" width="690" height="351" data-dominant-color="646587"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×542 33.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As I’m not quite sure what I’m able to attach to my first post, here is the code in its entirety:</p>
<details>
  <summary>Click to expand code (czireader.py)</summary>
<h3><a name="p-98123-called-as-2" class="anchor" href="#p-98123-called-as-2" aria-label="Heading link"></a>Called as:</h3>
<p>In the console, I added my working path with a <code>sys.path.append()</code> and then:</p>
<pre><code class="lang-auto">fn = 'an_image.czi'
czireader.reader(fn)
</code></pre>
<p>For some reason, I was not able to do this from the Jupyter plugin:</p>
<blockquote>
<p>File C:\PortableApps\Slicer 5.3.0-2023-06-17\bin\Python\sitkUtils.py:21, in  PushVolumeToSlicer(sitkimage, targetNode, name, className)<br>
19 # Create new node if needed<br>
20 if not targetNode:<br>
—&gt; 21     targetNode = slicer.mrmlScene.AddNewNodeByClass(className, slicer.mrmlScene.GetUniqueNameByString(name))<br>
22     targetNode.CreateDefaultDisplayNodes()<br>
24 myNodeFullITKAddress = GetSlicerITKReadWriteAddress(targetNode)</p>
<p>AttributeError: module ‘slicer’ has no attribute ‘mrmlScene’</p>
</blockquote>
<h3><a name="p-98123-the-code-so-far-3" class="anchor" href="#p-98123-the-code-so-far-3" aria-label="Heading link"></a>The code so far:</h3>
<pre data-code-wrap="python"><code class="lang-python"># Original code lifted almost entirely from:
# https://github.com/BodenmillerGroup/napari-czifile2/blob/main/napari_czifile2/_reader.py
# https://github.com/BodenmillerGroup/napari-czifile2/blob/main/napari_czifile2/io.py
# All credit goes to @jwindhager https://github.com/jwindhager

import SimpleITK as sitk
import sitkUtils
import slicer

from multiprocessing import cpu_count

from pathlib import Path
from typing import Iterable, List, Optional, Union
from xml.etree import ElementTree

import numpy as np
from czifile import CziFile, DimensionEntryDV1, DirectoryEntryDV
from tifffile import lazyattr


class CZISceneFile(CziFile):
  @staticmethod
  def get_num_scenes(path: Union[str, Path], *args, **kwargs) -&gt; int:
      with CziFile(path, *args, **kwargs) as czi_file:
          if "S" in czi_file.axes:
              return czi_file.shape[czi_file.axes.index("S")]
          return 1

  def __init__(self, path: Union[str, Path], scene_index: int, *args, **kwargs):
      super(CZISceneFile, self).__init__(str(path), *args, **kwargs)
      self.scene_index = scene_index

  @lazyattr
  def pos_x_um(self) -&gt; float:
      return self.scale_x_um * min(
          (dim_entry.start for dim_entry in self._iter_dim_entries("X")), default=0.0
      )

  @lazyattr
  def pos_y_um(self) -&gt; float:
      return self.scale_y_um * min(
          (dim_entry.start for dim_entry in self._iter_dim_entries("Y")), default=0.0
      )

  @lazyattr
  def pos_z_um(self) -&gt; float:
      return self.scale_z_um * min(
          (dim_entry.start for dim_entry in self._iter_dim_entries("Z")), default=0.0
      )

  @lazyattr
  def pos_t_seconds(self) -&gt; float:
      return self.scale_t_seconds * min(
          (dim_entry.start for dim_entry in self._iter_dim_entries("T")), default=0.0
      )

  @lazyattr
  def scale_x_um(self) -&gt; float:
      return self._get_scale("X", multiplier=10.0**6)

  @lazyattr
  def scale_y_um(self) -&gt; float:
      return self._get_scale("Y", multiplier=10.0**6)

  @lazyattr
  def scale_z_um(self) -&gt; float:
      return self._get_scale("Z", multiplier=10.0**6)

  @lazyattr
  def scale_t_seconds(self) -&gt; float:
      return self._get_scale("T")

  @lazyattr
  def channel_names(self) -&gt; Optional[List[str]]:
      if "C" in self.axes:
          channel_elements = self._metadata_xml.findall(
              ".//Metadata/Information/Image/Dimensions/Channels/Channel"
          )
          if len(channel_elements) == self.shape[self.axes.index("C")]:
              return [c.attrib.get("Name", c.attrib["Id"]) for c in channel_elements]
      return None

  @lazyattr
  def is_rgb(self) -&gt; bool:
      return "0" in self.axes and self.shape[self.axes.index("0")] &gt; 1

  def as_tzcyx0_array(self, *args, **kwargs) -&gt; np.ndarray:
      data = self.asarray(*args, **kwargs)
      tzcyx0_axis_indices = []
      if "T" in self.axes:
          tzcyx0_axis_indices.append(self.axes.index("T"))
      else:
          tzcyx0_axis_indices.append(data.ndim)
          data = np.expand_dims(data, -1)
      if "Z" in self.axes:
          tzcyx0_axis_indices.append(self.axes.index("Z"))
      else:
          tzcyx0_axis_indices.append(data.ndim)
          data = np.expand_dims(data, -1)
      if "C" in self.axes:
          tzcyx0_axis_indices.append(self.axes.index("C"))
      else:
          tzcyx0_axis_indices.append(data.ndim)
          data = np.expand_dims(data, -1)
      tzcyx0_axis_indices.append(self.axes.index("Y"))
      tzcyx0_axis_indices.append(self.axes.index("X"))
      if "0" in self.axes:
          tzcyx0_axis_indices.append(self.axes.index("0"))
      else:
          tzcyx0_axis_indices.append(data.ndim)
          data = np.expand_dims(data, -1)
      for axis_index in range(len(self.axes)):
          if axis_index not in tzcyx0_axis_indices:
              tzcyx0_axis_indices.append(axis_index)
      data = data.transpose(tzcyx0_axis_indices)
      data.shape = data.shape[:6]
      return data

  def _iter_dim_entries(self, dimension: str) -&gt; Iterable[DimensionEntryDV1]:
      for dir_entry in self.filtered_subblock_directory:
          for dim_entry in dir_entry.dimension_entries:
              if dim_entry.dimension == dimension:
                  yield dim_entry

  def _get_scale(self, dimension: str, multiplier: float = 1.0):
      scale_element = self._metadata_xml.find(
          f'.//Metadata/Scaling/Items/Distance[@Id="{dimension}"]/Value'
      )
      if scale_element is not None:
          scale = float(scale_element.text)
          if scale &gt; 0:
              return scale * multiplier
      return 1.0

  @lazyattr
  def _metadata_xml(self) -&gt; ElementTree.Element:
      return ElementTree.fromstring(self.metadata())

  @lazyattr
  def filtered_subblock_directory(self) -&gt; List[DirectoryEntryDV]:
      dir_entries = super(CZISceneFile, self).filtered_subblock_directory
      return list(
          filter(
              lambda dir_entry: self._get_scene_index(dir_entry) == self.scene_index,
              dir_entries,
          )
      )

  @staticmethod
  def _get_scene_index(dir_entry: DirectoryEntryDV) -&gt; int:
      scene_indices = {
          dim_entry.start
          for dim_entry in dir_entry.dimension_entries
          if dim_entry.dimension == "S"
      }
      if len(scene_indices) == 0:
          return 0
      assert len(scene_indices) == 1
      return scene_indices.pop()

def reader(paths):
  layer_data = []
  if not isinstance(paths, list):
      paths = [paths]
  for path in paths:
      num_scenes = CZISceneFile.get_num_scenes(path)
      for scene_index in range(num_scenes):
          with CZISceneFile(path, scene_index) as f:
              if f.is_rgb:
                  continue
                  
              data = f.as_tzcyx0_array(max_workers=cpu_count())
              # https://github.com/BodenmillerGroup/napari-czifile2/issues/5
              contrast_limits = None
              if data.dtype == np.uint16:
                  contrast_limits = (0, 65535)
              # https://github.com/napari/napari/issues/2348
              data = data[:, :, :, :, :, 0]
              shape = data.shape #t z c y x

              for t in range(shape[0]):
                  for c in range(shape[2]):
                      
                      #Here we load the volumes one at a time:
                      image_sitk = sitk.GetImageFromArray(data[t,:,c,:,:])
                      image_sitk.SetOrigin((f.pos_x_um, f.pos_y_um, f.pos_z_um))
                      image_sitk.SetSpacing((f.scale_x_um,f.scale_y_um,f.scale_z_um))
                      volumeNode = sitkUtils.PushVolumeToSlicer(image_sitk,None)
                      volumeNode.SetName(f.channel_names[c])
                      #volumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
                      #volumeNode.SetAndObserveImageData(imageData)
                      #volumeNode.SetSpacing(spacing)
                      #volumeNode.SetOrigin(origin)
                      #slicer.util.setSliceViewerLayers(volumeNode, fit=True)

                      slicer.util.setSliceViewerLayers(background=volumeNode, fit=True)
</code></pre>
</details>
<p>So, as you can see, I’m still struggling with really basic things such as:</p>
<ul>
<li>reading colors for each channel in the CZI file, and setting them for each of the imported volumes</li>
<li>maybe some kind of GUI interface for the user to select which scene to import (there may be multiple scenes and timepoints, not sure how to handle those nicely yet)</li>
<li>units: The code I lifted from <span class="mention">@jwindhager</span> conveniently provides a pixel size in microns, but they’re set as mm in Slicer (check whether the units are always mm or if it is possible to set the units)</li>
<li>Follow the help provided in the Slicer help to turn the code into a reader plugin</li>
<li>A few manual operations required to actually display the volume, maybe I can set more things in the reader to avoid the manual steps.</li>
<li>How big can the images be? For now I’m not sure…</li>
<li>RGB images? For now I’m only interested in confocal stacks, but maybe histology slides could also be handled through a potential future reader. For now I’m not going to worry too much about this.</li>
</ul>
<h3><a name="p-98123-and-what-would-be-the-end-goal-4" class="anchor" href="#p-98123-and-what-would-be-the-end-goal-4" aria-label="Heading link"></a>And what would be the end goal?</h3>
<p>After I finish writing this plugin, the two main image processing tasks I will need to perform are:</p>
<ul>
<li>3-D registration of multiple acquired stacks using the DAPI nuclei as landmarks</li>
<li>Segmentation of each cell in 3-D if possible (cellpose?)</li>
</ul>
<p>And in terms of data output:</p>
<ul>
<li>Size / shape of cells and</li>
<li>Mean intensity in all the different channels (up to 6) for each cell.</li>
</ul>
<p>That’s it, thank you for reading and any advice you might have will be greatly appreciated!</p>
<p>Kind regards,<br>
Egor</p>

---

## Post #2 by @lassoan (2023-07-25 04:46 UTC)

<p>It is awesome that you work on this and the volume rendered image looks very nice (you can make it even more impressive by adding some colors to the color transfer function in Volume rendering module).</p>
<p>Napari io plugins are nice in that they don’t depend on napari itself, so it is really easy to import them and use in Slicer:</p>
<pre data-code-wrap="python"><code class="lang-python"># CZI file reading using napari-czifile2 plugin in 3D Slicer
# Tested with: https://downloads.openmicroscopy.org/images/Zeiss-CZI/idr0011/Plate1-Blue-A_TS-Stinger/

filepath = r'c:\Users\andra\Downloads\Plate1-Blue-A-12-Scene-3-P3-F2-03.czi'
timePoint = 0
component = 0  # set to `None` to read as vector volume, set to 0, 1, 2, ... to read a single component as scalar volume

# Install napari-czifile2
try:
    import napari_czifile2
except ImportError as e:
    pip_install('napari-czifile2')
    import napari_czifile2

import numpy as np

reader = napari_czifile2.napari_get_reader(filepath)
result = reader(filepath)

voxelsZYXC = np.moveaxis(result[0][0][timePoint], [1], [3]) # z c y x -&gt; z y x c

if component is None:
    # Read RGB volume    
    volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLVectorVolumeNode')
    voxels = voxelsZYXC
else:
    # Read scalar volume from a single component
    volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
    voxels = voxelsZYXC[:, :, :, component]

scaleZYX = result[0][1]['scale'][1:]
volumeNode.SetSpacing(scaleZYX[2], scaleZYX[1], scaleZYX[0])
</code></pre>
<p>To show the image in slice/3D views:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.updateVolumeFromArray(volumeNode, voxels)
slicer.util.setSliceViewerLayers(volumeNode, fit=True)

if component is not None:
    vrLogic = slicer.modules.volumerendering.logic()
    vrDisplayNode = vrLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
    vrDisplayNode.SetVisibility(True)
    # Use the same window/level and colormap settings for volume rendering as for slice display
    vrDisplayNode.SetFollowVolumeDisplayNode(True)
    # Recenter 3D view
    slicer.util.resetThreeDViews()
</code></pre>
<p>The advantage of using the napari reader as it is would be that we would automatically benefit from all fixes and improvements of the reader. It would also serve as a good example for using other napari reader plugins in Slicer.</p>
<blockquote>
<ul>
<li>reading colors for each channel in the CZI file, and setting them for each of the imported volumes</li>
</ul>
</blockquote>
<p>See my example above</p>
<blockquote>
<ul>
<li>maybe some kind of GUI interface for the user to select which scene to import (there may be multiple scenes and timepoints, not sure how to handle those nicely yet)</li>
</ul>
</blockquote>
<p>You could add an IO options widget (that is displayed in the “Add data” window when you check “Show options”, but I’m not sure if this would be convenient/dynamic enough.</p>
<blockquote>
<ul>
<li>units: The code I lifted from <span class="mention">@jwindhager</span> conveniently provides a pixel size in microns, but they’re set as mm in Slicer (check whether the units are always mm or if it is possible to set the units)</li>
</ul>
</blockquote>
<p>When you read the image the data must be converted to the current length unit, which is millimeter by default. In application settings you can set displayed length unit to micrometer (which means that values are stored as millimeter but when displayed on the GUI the value x 1000 is shown and the µm suffix instead of mm).</p>
<pre data-code-wrap="python"><code class="lang-python">selectionNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSelectionNodeSingleton')
lengthUnitNode = slicer.mrmlScene.GetNodeByID(selectionNode.GetUnitNodeID('length'))
lengthUnitNode.GetSuffix()  # returns 'mm' by default
lengthUnitNode.GetDisplayCoefficient()  # returns 1.0 by default

# After you set displayed length unit to micrometer in the application settings:
lengthUnitNode.GetSuffix()  # returns 'µm'
lengthUnitNode.GetDisplayCoefficient()  # returns 1000.0
</code></pre>
<p>If you work with microscopy image then it may make sense to change the actual unit to micrometer by setting <code>Suffix</code> to <code>µm</code> and <code>Coefficient</code> to <code>1.0</code> because you could avoid potential numerical instabilities and GUI inconveniences due to using too small numbers. After setting these, you would then get:</p>
<pre data-code-wrap="python"><code class="lang-python">lengthUnitNode.GetSuffix()  # returns 'µm'
lengthUnitNode.GetDisplayCoefficient()  # returns 1.0
</code></pre>
<p>In the reader you could just handle these 3 cases (mm suffix with 1.0 coefficient; µm with 1000.0; µm with 1.0) and refuse to load the images if a different length unit is set.</p>
<aside class="quote no-group" data-username="EgorZindy" data-post="1" data-topic="30769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/egorzindy/48/66942_2.png" class="avatar"> EgorZindy:</div>
<blockquote>
<p>Follow the help provided in the Slicer help to turn the code into a reader plugin</p>
</blockquote>
</aside>
<p>This should be fairly straightforward - see an <a href="https://github.com/Slicer/Slicer/blob/main/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">example in Slicer core</a> or this <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOCT/ImportOCT.py">example in Sandbox</a>.</p>
<aside class="quote no-group" data-username="EgorZindy" data-post="1" data-topic="30769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/egorzindy/48/66942_2.png" class="avatar"> EgorZindy:</div>
<blockquote>
<p>A few manual operations required to actually display the volume, maybe I can set more things in the reader to avoid the manual steps.</p>
</blockquote>
</aside>
<p>My code snippet above should help with this but you can ask more details here.</p>
<aside class="quote no-group" data-username="EgorZindy" data-post="1" data-topic="30769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/egorzindy/48/66942_2.png" class="avatar"> EgorZindy:</div>
<blockquote>
<p>How big can the images be? For now I’m not sure…</p>
</blockquote>
</aside>
<p>Whatever fits into your virtual memory space. If you work with multiscale images then it may be useful to load the image at the current display resolution, and only those tiles that are visible. You can find some experimentation with that <a href="https://github.com/gaoyi/SlicerBigImage">here</a>.</p>
<aside class="quote no-group" data-username="EgorZindy" data-post="1" data-topic="30769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/egorzindy/48/66942_2.png" class="avatar"> EgorZindy:</div>
<blockquote>
<p>RGB images? For now I’m only interested in confocal stacks, but maybe histology slides could also be handled through a potential future reader. For now I’m not going to worry too much about this.</p>
</blockquote>
</aside>
<p>The example above shows how to load a multi-component image and if it has 3 components then it is interpreted as RGB by default. You need to cast the values to unsigned char if you want to use the GPU volume renderer for displaying it in 3D views.</p>

---

## Post #3 by @EgorZindy (2023-07-25 05:10 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your awesome reply!</p>
<p>Lots to digest, so it may take me some time to come back with some significant progress, but I’ll let you know how this progresses. I’m happy to develop any plugins in the open.</p>
<p>At least, 3D Slicer seems well suited for working with these types of microscopy images. I really like the fine tuning of the renderer look-up tables (both colour and opacity) which is not something I’m used to from the usual microscopy oriented tools I use (e.g. Imaris). And you’re absolutely right, adding colours makes the image way more interesting <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fde4ef91dd18a4fc09c0b809c472e64fa1774441.jpeg" alt="image" data-base62-sha1="Ae3i9lDdwgv8U2WLBOcJKQHdAg9" width="581" height="424"></p>
<p>Kind regards,<br>
Egor</p>

---

## Post #4 by @lassoan (2023-07-25 11:42 UTC)

<p>Nice job with the coloring! Keep us updated about your progress.</p>

---

## Post #5 by @EgorZindy (2023-07-25 17:55 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I now have a very early but working reader! I still need to implement sequences when time series are detected (possibly taking inspiration from <a href="https://github.com/Slicer/Slicer/pull/6733" rel="noopener nofollow ugc">the .npy reader</a>). Also, colours , but I will need to read them from the Napari reader first and maybe improve that module first.</p>
<p>So, I’ll make a pull request for  my ImportCZI reader and let you decide whether the code is worth including into Slicer at some point (or not <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ).</p>
<p>Is it better to direct the pull request at the Slicer or to the SlicerSandbox repository?</p>
<p>Cheers,<br>
Egor</p>

---

## Post #6 by @lassoan (2023-07-30 13:33 UTC)

<p>Since the reader will be under development for a while, it depends on external Python packages, and it is a quote specialized file format, it makes sense to maintain it in an extension. The Sandbox extension would be suitable or it could be added to the BigImage extension. If more microscopy-specific modules will be developed then it could make sense to add a microscopy extension.</p>

---

## Post #7 by @EgorZindy (2023-07-31 06:31 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I’ve been working on a pull request for <a href="https://github.com/napari/napari/pull/6102" rel="noopener nofollow ugc">hex colors in napari image layers</a>. Then when this is committed, I will try to get channel colours added into napari-czifile2 module.</p>
<p>It may take some time before all the pieces are in place for the slicer CZI reader, but I’ll push my code to a fork of the Sandbox and keep this thread updated with any progress.</p>
<p>I’ll adapt your pip commands to install czi-file2 from source from <a href="https://github.com/zindy/napari-czifile2/tree/channel-colors" rel="noopener nofollow ugc">my own github branch</a> while this is going on.</p>
<blockquote>
<p>If more microscopy-specific modules will be developed then it could make sense to add a microscopy extension.</p>
</blockquote>
<p>Actually, this may not be a bad idea as a colleague of mine is interested in a ND2 (Nikon) reader for some of his confocal stacks. His are mostly 5-D (3D + channels + time).</p>
<p>… So that’s at least two new microscopy related extensions! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Cheers,<br>
Egor</p>

---

## Post #8 by @pieper (2023-07-31 13:53 UTC)

<p>It’s great to see this progress <a class="mention" href="/u/egorzindy">@EgorZindy</a> I think there’s a lot of potential to work together on this.</p>
<p>The <a href="https://github.com/SlicerMicro">SlicerMicro</a> github organization was a start on something like this and could be repurposed and expanded if it meets the needs.  We can add new members if we want to use it.</p>
<p>Also here are <a href="https://docs.google.com/presentation/d/12cDI-HHQ4OhNTN4oqx-yFiyPAqvDB5sxKrimrWgdAOY/edit#slide=id.p1">summary slides of some previous work on Slicer for Microscopy and thoughts about what more is needed</a>.</p>

---

## Post #9 by @ylcnkzy (2023-08-03 12:53 UTC)

<p>Hi EgorZindy,</p>
<p>This is great! I am also working with light-sheet and confocal data in 3D. I am looking forward to seeing the progress. 3D-Slicer is a really promising platform for such data. I believe we all need to create a subtitle to gather all microscopists and create a plugin depending on the needs.</p>
<p>Commercial software is (such as Imaris) really ripping off universities and research institutions for licenses.</p>

---

## Post #10 by @pieper (2023-08-03 14:06 UTC)

<p>It would be great if people could start listing any missing features that would be helpful for these applications.  Maybe start adding ideas in this thread and then they can be migrated to an appropriate issue tracker as the are formalized.</p>
<p>One wish-list item might be to modernize <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/IASEM">this IASEM extension</a> to work with the latest Slicer features if it hasn’t already been done.  It had a nice feature with a low-res proxy volume that you could interactively sample at full resolution using a box ROI.</p>

---

## Post #11 by @EgorZindy (2023-08-04 17:06 UTC)

<p>Hi everyone,</p>
<p>definitely interested in any microscopy related use of 3-D slicer!</p>
<p>I made some (slow) progress this week. My pull request for hex colors in napari was accepted, which means I can have a look at the slicer reader again. Eventually, instead of pulling the napari-czifile2 module from my github, my czi reader should be able to use the pypi one (since napari itself will be able to import channel colours).</p>
<p>I’ll update you when I get round pushing the reader code to my own Sandbox branch.</p>
<p>Cheers,<br>
Egor</p>

---

## Post #12 by @EgorZindy (2023-08-24 10:15 UTC)

<p>Hi everyone,</p>
<p>I got a bit further! I noticed that <a href="https://github.com/sebi06/czitools" rel="noopener nofollow ugc">the czitools repository</a> had an interesting reader that can read data into dask arrays, so I decided to redesign my Slicer importer around czitools instead of the napari reader I used before.</p>
<p>For now, I install czitools directly from my own github czitools fork (one that isn’t dependent on napari, pandas,…) but in the long term, I hope I can just install the official czitools instead.</p>
<p>Since I install my fork via git+pip, a message is displayed if the <code>git</code> tool is not accessible from 3D Slicer.</p>
<p>The two repositories are:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/zindy/czitools_lite">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/zindy/czitools_lite" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/04fadbb7f9a9839fcce5ab77b914d5b3fe7ffd73fd79a75c96798e389fded408/zindy/czitools_lite" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/zindy/czitools_lite" target="_blank" rel="noopener nofollow ugc">GitHub - zindy/czitools_lite: This repository provides a collection of tools...</a></h3>

  <p>This repository provides a collection of tools to simplify reading CZI (Carl Zeiss Image) pixel and metadata in Python. In addition it also contains other useful utilities to visualize CZI images i...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and <a href="https://github.com/zindy/SlicerSandbox/tree/master/ImportCZI" rel="noopener nofollow ugc">ImportCZI</a> in</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/zindy/SlicerSandbox">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/zindy/SlicerSandbox" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/e1a2a3935930c1ba686a50f695880c67e88ab9412b6f7097827569c7d7b3f9b6/zindy/SlicerSandbox" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/zindy/SlicerSandbox" target="_blank" rel="noopener nofollow ugc">GitHub - zindy/SlicerSandbox: Collection of utilities that are not polished...</a></h3>

  <p>Collection of utilities that are not polished implementations but can be useful to users - GitHub - zindy/SlicerSandbox: Collection of utilities that are not polished implementations but can be use...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m going to try and make a little dialog box (ImportOsirixROI has one) to</p>
<ul>
<li>choose whether to import a numpy or a dask array</li>
<li>choose which scene to load (for now only scene 0 is imported)</li>
<li>choose the colours for each channels (preloaded with the colours found in the metadata).</li>
</ul>
<p>I’m not super confident with Qt / Designer, so I’ll let you know how I get on! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Cheers for now,<br>
Egor</p>

---
