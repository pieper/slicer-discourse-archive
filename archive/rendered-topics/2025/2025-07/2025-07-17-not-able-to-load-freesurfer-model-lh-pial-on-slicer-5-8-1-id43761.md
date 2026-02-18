# Not able to load Freesurfer Model (lh.pial) on Slicer 5.8.1

**Topic ID**: 43761
**Date**: 2025-07-17
**URL**: https://discourse.slicer.org/t/not-able-to-load-freesurfer-model-lh-pial-on-slicer-5-8-1/43761

---

## Post #1 by @justomont (2025-07-17 18:35 UTC)

<p>I’m trying to load a FreeSurfer model (lh.pial) programmatically through a scripted module but I’m not achieving it.</p>
<p>I’ve tried:</p>
<pre><code class="lang-auto">fsImporterLogic = slicer.util.getModuleLogic('FreeSurferImporter')
volumeNode = fsImporterLogic.LoadFreeSurferVolume(file_path)
</code></pre>
<p>where file_path is the path to one of the files I want to open, and got the following error:</p>
<pre><code class="lang-auto">vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial. ITK exception info: error in unknown:  Could not create IO object for reading file /Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial
[VTK]   Tried to create one of the following:
[VTK]     BMPImageIO
[VTK]     BioRadImageIO
[VTK]     DCMTKImageIO
[VTK]     GDCMImageIO
[VTK]     GiplImageIO
[VTK]     JPEGImageIO
[VTK]     LSMImageIO
[VTK]     MGHImageIO
[VTK]     MINCImageIO
[VTK]     MRCImageIO
[VTK]     MetaImageIO
[VTK]     NiftiImageIO
[VTK]     NrrdImageIO
[VTK]     PNGImageIO
[VTK]     ScancoImageIO
[VTK]     StimulateImageIO
[VTK]     TIFFImageIO
[VTK]     VTKImageIO
[VTK]     MRMLIDImageIO
[VTK]   You probably failed to set a file suffix, or
[VTK]     set the suffix to an unsupported type.
[VTK] Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7f8fc479ae80) returned failure for request: vtkInformation (0x60001155aa00)
[VTK]   Debug: Off
[VTK]   Modified Time: 5320081
[VTK]   Reference Count: 1
[VTK]   Registered Events: (none)
[VTK]   Request: REQUEST_INFORMATION
[VTK]   ALGORITHM_AFTER_FORWARD: 1
[VTK]   FORWARD_DIRECTION: 0
[VTK] vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file '/Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial' failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 0 files. File reader used the archetype file name of '/Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial' (first filename: '')
[VTK] vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file '/Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial' failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 0 files. File reader used the archetype file name of '/Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial' (first filename: '')
[VTK] vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read '/Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial' file as a volume of type 'Volume'. Details: FileFormatError.
[VTK] vtkMRMLStorageNode::ReadData: Failed to read node lh (vtkMRMLScalarVolumeNode5) from filename='/Users/justo/Library/CloudStorage/GoogleDrive-justo.montoya@upf.edu/Mi unidad/SLICER/test_raw/fsfolder/surf/lh.pial'
</code></pre>
<p>I’ve also tried other options like:<br>
<code>modelNode = slicer.util.loadModel(file_path)</code></p>
<p>But it’s not working either. How can I open this FreeSurfer model programmatically?</p>
<p>Thanks in advance! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2025-07-18 11:35 UTC)

<p>The method you tried is for loading images.  You can load models (in freesurfer terminology overlays) using <code>LoadFreeSurferScalarOverlay</code>.</p>

---

## Post #3 by @justomont (2025-07-18 12:36 UTC)

<p>Thanks.</p>
<p>What is an example usage of <code>LoadFreeSurferScalarOverlay()</code>?</p>
<p>I’ve seen that the logic is defined here <a href="https://github.com/PerkLab/SlicerFreeSurfer/blob/master/FreeSurferImporter/Logic/vtkSlicerFreeSurferImporterLogic.h" class="inline-onebox" rel="noopener nofollow ugc">SlicerFreeSurfer/FreeSurferImporter/Logic/vtkSlicerFreeSurferImporterLogic.h at master · PerkLab/SlicerFreeSurfer · GitHub</a> but I can’t understand how to apply it to my situation.</p>

---

## Post #4 by @lassoan (2025-07-18 14:43 UTC)

<p>I misspoke above, Slicer models correspond to freesurfer surfaces (*h.white, *h.pial, *h.inflated, *h.sphere, <em>h.sphere.reg, <em>h.orig files), and Slicer scalar arrays correspond to freesurfer overlays (</em>.area</em>, <em>.curv</em>, *.sulc, *.W files).</p>
<p>Surface reading was reworked about 1-2 years ago to use nibabel and is now implemented in a separate logic. You can use it as it is shown in this test:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerFreeSurfer/blob/85980a0bf6558a36985fa57ae1c65e67a268043b/NiBabelModelIO/NiBabelModelIO.py#L261-L288">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerFreeSurfer/blob/85980a0bf6558a36985fa57ae1c65e67a268043b/NiBabelModelIO/NiBabelModelIO.py#L261-L288" target="_blank" rel="noopener">github.com/PerkLab/SlicerFreeSurfer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerFreeSurfer/blob/85980a0bf6558a36985fa57ae1c65e67a268043b/NiBabelModelIO/NiBabelModelIO.py#L261-L288" target="_blank" rel="noopener">NiBabelModelIO/NiBabelModelIO.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/PerkLab/SlicerFreeSurfer/blob/85980a0bf6558a36985fa57ae1c65e67a268043b/NiBabelModelIO/NiBabelModelIO.py#L261-L288" rel="noopener"><code>85980a0bf</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="261" style="counter-reset: li-counter 260 ;">
          <li>def load(self, properties):</li>
          <li>    try:</li>
          <li>        filePath = properties['fileName']</li>
          <li></li>
          <li>        # Get node base name from filename</li>
          <li>        baseName = ""</li>
          <li>        if 'name' in properties.keys():</li>
          <li>            baseName = properties['name']</li>
          <li></li>
          <li>        # Read file content</li>
          <li>        logic = NiBabelModelIOLogic()</li>
          <li>        loadedNode = logic.createAndReadModelNode(filePath, baseName)</li>
          <li></li>
          <li>        # Uncomment the next line to display a warning message to the user.</li>
          <li>        if loadedNode is None:</li>
          <li>            self.parent.userMessages().AddMessage(vtk.vtkCommand.ErrorEvent, "Could not load file: " + filePath)</li>
          <li>            return</li>
          <li></li>
          <li>    except Exception as e:</li>
          <li>        import traceback</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/PerkLab/SlicerFreeSurfer/blob/85980a0bf6558a36985fa57ae1c65e67a268043b/NiBabelModelIO/NiBabelModelIO.py#L261-L288" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><code>slicer.util.loadNodeFromFile()</code> would work if the NiBabelModelIO registered itself as a reader plugin. It would be nice if you could implement it (you would add a <code>NiBabelModelIOFileReader</code> class to the <code>NiBabelModelIO.py</code> and implement  a few methods - similarly to <a href="https://github.com/Slicer/Slicer/blob/40b45ad844a2148cc19d694f622833e712fff72f/Modules/Scripted/ImportItkSnapLabel/ImportItkSnapLabel.py#L33-L59">this</a>). But if you don’t have the time then you can simply use the NiBabelModelIO module logic directly.</p>

---

## Post #5 by @justomont (2025-07-22 09:31 UTC)

<p>Thank you very much for the clarification!</p>
<p>Regarding the suggestion to implement the <code>NiBabelModelIOFileReader</code> class, I’d be genuinely happy to contribute something useful to the community. However, I’m currently in the final stages of my PhD, and unfortunately I won’t be able to commit the necessary time and focus right now.</p>
<p>That said, once my schedule opens up a bit post-dissertation, I’d be glad to revisit this and potentially work on the implementation. I’ll keep your suggestion in mind and reach out when I have the bandwidth to properly contribute.</p>
<p>Thanks again for your support and for all the work you do on Slicer!!</p>

---
