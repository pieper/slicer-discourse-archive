---
topic_id: 1728
title: "Model Vtk File Name Problem In Slicer 4 7 And 4 9"
date: 2017-12-26
url: https://discourse.slicer.org/t/1728
---

# Model vtk file name problem in Slicer 4.7 and 4.9

**Topic ID**: 1728
**Date**: 2017-12-26
**URL**: https://discourse.slicer.org/t/model-vtk-file-name-problem-in-slicer-4-7-and-4-9/1728

---

## Post #1 by @BlueOctopus (2017-12-26 14:38 UTC)

<p>Hi!<br>
I have found some error in 3D Slicer V4.7 and V4.9<br>
In MRML file making after updating some scenes,<br>
they make vtk file name incorrectly.<br>
As like<br>
</p>
<p>So error message occured in Python console.<br>
ReadDataInternal: model file ‘D:/3D…/3DVisualizationData/3DVisualizationData/3DHeadData/hemispheric_white_matter.vtk.vtk’ not found.</p>
<p>==&gt; No 3D Scene and only 2D scene displayed in 3D panel.<br>
So update .vtk.vtk to .vtk with text editor.<br>
perpectly screen maked with updated 3D scene.</p>
<p>I used sample 3DheadScene.mrml file in your tutorial site.<br>
(<a href="https://www.slicer.org/wiki/Documentation/4.8/Training" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Training</a>)</p>
<p>my PC environment : Windows 10 recently version, HP notebook with AMD A10 processor and 8GB memory.</p>

---

## Post #2 by @lassoan (2017-12-26 14:41 UTC)

<aside class="quote no-group" data-username="BlueOctopus" data-post="1" data-topic="1728">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blueoctopus/48/78517_2.png" class="avatar"> BlueOctopus:</div>
<blockquote>
<p>In MRML file making after updating some scenes</p>
</blockquote>
</aside>
<p>I cannot reproduce this. Could you describe what exact steps do you do after loading the scene? Only use Slicer 4.8 (latest stable) or 4.9 (latest nightly).</p>

---

## Post #3 by @BlueOctopus (2017-12-27 05:30 UTC)

<p>** Sorry, in previous messgae, vanished tag statements **</p>
<p>There are no specific scene editing.<br>
When saving to a new file for new edition,<br>
(ex: mynew.mrml)  in that file,<br>
updated vtk file name incorrectly.<br>
As like (XML tag) below,<br>
ModelStorage<br>
id=“vtkMRMLModelStorageNode1” name=“vtkMRMLModelStorageNode1” hideFromEditors=“true” selectable=“true” selected=“false” attributes=“Category:” fileName=“hemispheric_white_matter.vtk.vtk” useCompression=“1” defaultWriteFileExtension=“vtk” readState=“0” writeState=“0” coordinateSystem=“RAS”</p>
<p>It is file name construction problem in XML tag of mrml file,</p>

---

## Post #4 by @Nicole_Aucoin (2017-12-27 15:12 UTC)

<p>I recall trying to fix this problem on saving scenes, with this commit:</p>
<p><a href="https://github.com/Slicer/Slicer/commit/c44f73b3e79f1ef10b876a963bcd472e488145f4#diff-38c329d977c74c8714c51bd6c0401b0c" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/commit/c44f73b3e79f1ef10b876a963bcd472e488145f4#diff-38c329d977c74c8714c51bd6c0401b0c</a></p>
<p>vtkMRMLStorageNode::GetSupportedFileExtension just returns the last extension in a doubled one, and the storage node call GetFileNameWithoutExtension only removes the last one:<br>
(load cube.vtk from Slicer/Libs/MRML/Core/Testing/TestData/cube.vtk)</p>
<blockquote>
<blockquote>
<blockquote>
<p>snode.SetFileName(‘C:/Slicer_src/Slicer/Libs/MRML/Core/Testing/TestData/cube.vtk.vtk’)<br>
snode.GetFileNameWithoutExtension()<br>
‘cube.vtk’</p>
</blockquote>
</blockquote>
</blockquote>
<p>So where there’s code that’s just using GetFileNameWithoutExtension and adding an extension:<br>
Libs/MRML/Logic/vtkMRMLApplicationLogic.cxx:      uniqueFileName = storageNode-&gt;GetFileNameWithoutExtension(fileBaseName.c_str()) + defaultWriteExtension;</p>
<p>that’s going to result in the doubled extension again.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Base/QTGUI/qSlicerSaveDataDialog.cxx#L516">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Base/QTGUI/qSlicerSaveDataDialog.cxx#L516" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Base/QTGUI/qSlicerSaveDataDialog.cxx#L516" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Base/QTGUI/qSlicerSaveDataDialog.cxx#L516</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="506" style="counter-reset: li-counter 505 ;">
          <li>    if (QString(filenameWithoutExtension.c_str()) != safeNodeName)</li>
          <li>      {</li>
          <li>      QFileInfo existingInfo(snode-&gt;GetFileName());</li>
          <li>      std::string extension = snode-&gt;GetSupportedFileExtension();</li>
          <li>      QFileInfo newInfo(existingInfo.path(), safeNodeName + QString(extension.c_str()));</li>
          <li>      snode-&gt;SetFileName(newInfo.filePath().toUtf8());</li>
          <li>      node-&gt;StorableModified();</li>
          <li>      }</li>
          <li>    }</li>
          <li>  }</li>
          <li class="selected">if (snode-&gt;GetFileName() == nullptr &amp;&amp; !this-&gt;DirectoryButton-&gt;directory().isEmpty())</li>
          <li>  {</li>
          <li>  QString fileExtension = snode-&gt;GetDefaultWriteFileExtension();</li>
          <li>  if (!fileExtension.isEmpty())</li>
          <li>    {</li>
          <li>    fileExtension = QString(".") + fileExtension;</li>
          <li>    }</li>
          <li></li>
          <li>  QFileInfo fileName(QDir(this-&gt;DirectoryButton-&gt;directory()),</li>
          <li>                     safeNodeName + fileExtension);</li>
          <li>  snode-&gt;SetFileName(fileName.absoluteFilePath().toUtf8());</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
More checks could be added in the save data dialog to ensure that safeNodeName doesn’t have a file extension or that it doesn’t get doubled.</p>

---

## Post #5 by @lassoan (2017-12-27 15:53 UTC)

<p>There have been further fixes to this since then and it should work correctly now. Exactly one extension is removed and added to the node name or previous file name, so there should be no duplication.</p>
<p>I could not reproduce duplication with 4.8, no matter how or how many times I saved the scene.</p>
<p>Could you provide step-by-step instructions (describe each click) or screen capture video?</p>

---

## Post #6 by @BlueOctopus (2017-12-28 00:27 UTC)

<p>During editing on V4.7 and V4.9 using sample file, 3DHeadScene.mrml.<br>
(<a href="https://www.slicer.org/wiki/Documentation/4.8/Training" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Training</a>)<br>
Not edit vtk files in directory 3DHeadData.</p>
<p>My editing work is based training manual<br>
3DDataLoadingandVisualization_Slicer4.5_SoniaPujol.pdf.</p>
<p>There are no special working.<br>
Load data 3DHeadScene.mrml.<br>
Work editing following training manual.<br>
(Part2: 3D visualization of surface models of the brain)<br>
And as Part3, save to new mrml file only.<br>
No more other work, only tutorial.</p>
<p>But double extention name (.vtk.vtk) occured in saving.<br>
So I edit .vtk.vtk to .vtk directly from new  mrml file.<br>
And no problem and no error message on python console.</p>

---

## Post #7 by @BlueOctopus (2017-12-28 01:15 UTC)

<p>this is 2nd test.</p>
<ul>
<li>
<p>load 3DHeadScene.mrml</p>
</li>
<li>
<p>rotate face on 3D View</p>
</li>
<li>
<p>select Models module</p>
</li>
<li>
<p>select Skin.vtk on Scene tab</p>
</li>
<li>
<p>Opacity to 0.4</p>
</li>
<li>
<p>save to new.mrml file</p>
</li>
<li>
<p>Close scene</p>
</li>
<li>
<p>load new.mrml file</p>
</li>
<li>
<p>vanised face on 3D View</p>
</li>
<li>
<p>shutdown 3D Slicer and run</p>
</li>
<li>
<p>so, .vtk.vtk to .vtk with text editor</p>
</li>
<li>
<p>load new.mrml file</p>
</li>
<li>
<p>no problem</p>
</li>
<li>
<p>but other python console message below</p>
</li>
</ul>
<hr>
<p>already has observer<br>
already has observer<br>
already has observer<br>
Warning: In C:\D\N\Slicer-0\Libs\MRML\Core\vtkMRMLDisplayNode.cxx, line 523<br>
vtkMRMLModelDisplayNode (0000019278701260): Invalid activeAttributeLocation:</p>
<p>Loaded volume from file: F:/3D Slicer/Slicer4Sample/3DVisualizationData/3DVisualizationData/3DHeadData/grayscale.nrrd. Dimensions: 256x256x159. Number of components: 1. Pixel type: short.</p>
<p>ReadDataInternal: file does not exist: F:/3D Slicer/Slicer4Sample/3DVisualizationData/3DVisualizationData/3DHeadData/Axial.png</p>
<p>ReadDataInternal: file does not exist: F:/3D Slicer/Slicer4Sample/3DVisualizationData/3DVisualizationData/3DHeadData/Sagittal .png</p>
<h2>ReadDataInternal: file does not exist: F:/3D Slicer/Slicer4Sample/3DVisualizationData/3DVisualizationData/3DHeadData/Coronal .png</h2>
<p>( …png file not found problem)</p>
<p>==&gt; white space on file name as like Sagittal .png, Coronal.png.<br>
(20% space exist in xml file new.mrml,<br>
SceneViewStorage<br>
id=“vtkMRMLSceneViewStorageNode4” name=“vtkMRMLSceneViewStorageNode4” hideFromEditors=“true” selectable=“true” selected=“false” fileName=“Sagittal20%.png” useCompression=“1” defaultWriteFileExtension=“png” readState=“4” writeState=“4”<br>
)<br>
but “Axial.png” is correct.</p>
<ul>
<li>png files not exist on distribution zip file</li>
<li>this png files make from saving??</li>
</ul>

---

## Post #8 by @lassoan (2017-12-28 05:55 UTC)

<p>Thank you, I was able to reproduce the problems using Slicer 4.8. The main issue is that this scene was created with a much older version of Slicer and it had some inconsistencies (such as node name ending with “.vtk”) and some files were missing (thumbnail for scene views).</p>
<p>I’ve fixed these issues (see <a href="http://slicer.kitware.com/midas3/item/330421">resulting scene</a>), and updated links to the data set in <a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Data_Loading_and_3D_Visualization">4.8</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Data_Loading_and_3D_Visualization">nightly</a> training pages.</p>

---
