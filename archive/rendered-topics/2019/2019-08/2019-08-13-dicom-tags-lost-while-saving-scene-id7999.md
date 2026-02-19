---
topic_id: 7999
title: "Dicom Tags Lost While Saving Scene"
date: 2019-08-13
url: https://discourse.slicer.org/t/7999
---

# Dicom tags lost while saving scene

**Topic ID**: 7999
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/dicom-tags-lost-while-saving-scene/7999

---

## Post #1 by @Alex_Vergara (2019-08-13 09:10 UTC)

<p>When I save the scene as a mrb the dicom tags of my files are lost.</p>
<ol>
<li>Load a study from dicom node (modality and acquisition time are available, also other dicom tags)</li>
<li>Do some processing</li>
<li>save scene as mrb</li>
<li>Load scene back (drag and drop)</li>
<li>dicom tags no longer available</li>
</ol>
<p>The problem is that the scene saves the files as nrrd, changing the tags functionality, but then they are not saved, or at least I can’t find them anymore.</p>
<p>This is especially critical when moving mrb files to another computer, the functions that depend on this tags no longer work</p>

---

## Post #2 by @Alex_Vergara (2019-08-13 09:37 UTC)

<p>I have seen that the scalar nodes contain the function</p>
<pre><code class="lang-auto">/// Set node attributes
  void ReadXMLAttributes( const char** atts) override; 
</code></pre>
<p>but this is not visible from within python</p>
<pre><code class="lang-bash">File "/Users/alexvergaragil/Documents/GIT/dosimetry4d/Dosimetry4D/Logic/dicomutils.py", line 22, in getDICOMattributes
    self.imagenode.ReadXMLAttributes(att)
AttributeError: 'MRMLCorePython.vtkMRMLScalarVolumeNode' object has no attribute 'ReadXMLAttributes'
' object has no attribute 'GetMetaDataDictionary'
</code></pre>
<p>In the above exception I also discovered that there is also a ‘GetMetaDataDictionary’ in the vtkMRMLVolumeNode from which the nodes inherits. This function is also hidden for python</p>
<pre><code class="lang-bash">dicomutils.py", line 21, in getDICOMattributes
    print(self.imagenode.GetMetaDataDictionary())
AttributeError: 'MRMLCorePython.vtkMRMLScalarVolumeNode' object has no attribute 'GetMetaDataDictionary'
</code></pre>
<p>There is a way to get the Node data with GetImageData() but this is the output</p>
<pre><code class="lang-bash">vtkImageData (0x7f8fec3b0b80)
  Debug: Off
  Modified Time: 1956077
  Reference Count: 5
  Registered Events: 
    Registered Observers:
      vtkObserver (0x7f8fec3ac590)
        Event: 36
        EventName: ModifiedEvent
        Command: 0x7f8fec3ac530
        Priority: 0
        Tag: 1
  Information: 0x7f8fec3b0d20
  Data Released: False
  Global Release Data: Off
  UpdateTime: 1956397
  Field Data:
    Debug: Off
    Modified Time: 1956049
    Reference Count: 1
    Registered Events: (none)
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
  Number Of Points: 1474560
  Number Of Cells: 1435481
  Cell Data:
    Debug: Off
    Modified Time: 1956073
    Reference Count: 1
    Registered Events: 
      Registered Observers:
        vtkObserver (0x7f8fec3ab840)
          Event: 36
          EventName: ModifiedEvent
          Command: 0x7f8fec3ab570
          Priority: 0
          Tag: 1
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: (none)
    TCoords: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
  Point Data:
    Debug: Off
    Modified Time: 1956077
    Reference Count: 1
    Registered Events: 
      Registered Observers:
        vtkObserver (0x7f8fec3ab6e0)
          Event: 36
          EventName: ModifiedEvent
          Command: 0x7f8fec3ab570
          Priority: 0
          Tag: 1
    Number Of Arrays: 1
    Array 0 name = ImageScalars
    Number Of Components: 1
    Number Of Tuples: 1474560
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 )
    Scalars: 
      Debug: Off
      Modified Time: 1955813
      Reference Count: 2
      Registered Events: 
        Registered Observers:
          vtkObserver (0x7f8fd32380c0)
            Event: 36
            EventName: ModifiedEvent
            Command: 0x7f8fd3237ec0
            Priority: 0
            Tag: 2
          vtkObserver (0x7f8fd3238090)
            Event: 2
            EventName: DeleteEvent
            Command: 0x7f8fd3237ec0
            Priority: 0
            Tag: 1
      Name: ImageScalars
      Data type: double
      Size: 1474560
      MaxId: 1474559
      NumberOfComponents: 1
      Information: 0x7f8fec3a0c30
        Debug: Off
        Modified Time: 1956426
        Reference Count: 1
        Registered Events: (none)
        PER_COMPONENT: vtkInformationVector(0x7f8fec3a1250)
      Name: ImageScalars
      Number Of Components: 1
      Number Of Tuples: 1474560
      Size: 1474560
      MaxId: 1474559
      LookupTable: (none)
    Vectors: (none)
    Normals: (none)
    TCoords: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
  Bounds: 
    Xmin,Xmax: (0, 127)
    Ymin,Ymax: (0, 127)
    Zmin,Zmax: (0, 89)
  Compute Time: 2391599
  Spacing: (1, 1, 1)
  Origin: (0, 0, 0)
  Dimensions: (128, 128, 90)
  Increments: (0, 0, 0)
  Extent: (0, 127, 0, 127, 0, 89)
</code></pre>
<p>From all these records I see no reference to the initial Dicom tags, What is the “Modified Time”? Where is the modality?</p>

---

## Post #3 by @pieper (2019-08-13 13:34 UTC)

<p>Right, the MetaDataDictionary is only used if you load dicom via itk, so it doesn’t get stored in the scene or in nrrd.  I’d avoid relying on that.</p>
<p>If you want to access dicom information across scene save and restore, then you can import the volume via the DICOM module and the <code>DICOM.instanceUIDs</code> attribute will be stored and restored as a node attribute.  Then you can use these UIDs to look up information in the database or reload the files with pydicom to get a the headers.</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="2" data-topic="7999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>What is the “Modified Time”?</p>
</blockquote>
</aside>
<p>This is an <a href="https://vtk.org/doc/nightly/html/classvtkTimeStamp.html">internal part of VTK</a>, nothing to do with dicom.</p>

---

## Post #4 by @pieper (2019-08-13 13:36 UTC)

<p>Note too that if you want to move the data to another machine you need to be sure they also have the dicom data in their database.</p>
<p>Depending on your use case it may be better to cache whatever data you need, for example in an attribute of a <code>vtkMRMLScriptedModuleNode</code>.</p>

---

## Post #5 by @lassoan (2019-08-13 17:54 UTC)

<p>A number of essential DICOM tags are stored in Subject Hierarchy, associated with Patient, Study, and data items. You can save additional DICOM tags there.</p>

---

## Post #6 by @Alex_Vergara (2019-08-14 07:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="7999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A number of essential DICOM tags are stored in Subject Hierarchy,</p>
</blockquote>
</aside>
<p>Do you mean these:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8cc05ec70c109879f4c032b2225b8090956ff86.png" data-download-href="/uploads/short-url/sEkBVb8PiYxDlSluFu7kPniginI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8cc05ec70c109879f4c032b2225b8090956ff86_2_295x500.png" alt="image" data-base62-sha1="sEkBVb8PiYxDlSluFu7kPniginI" width="295" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8cc05ec70c109879f4c032b2225b8090956ff86_2_295x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8cc05ec70c109879f4c032b2225b8090956ff86_2_442x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8cc05ec70c109879f4c032b2225b8090956ff86_2_590x1000.png 2x" data-dominant-color="EBECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">596×1007 91.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thats only useful if I have only one DICOM file, but I have several (several acquisitions in different times, forget for now about the segmentations, transfoms, tables and intermediate volumes). I would need at least the acquisition time and modality of original acquisition files,  for sanity checks about wether a proposed file is SPECT or CT and if the suggested time is correct. It works If I load the original DICOM, but after processing the scene and reloading then it no longer works.</p>

---

## Post #7 by @Alex_Vergara (2019-08-14 08:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="7999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>vtkMRMLScriptedModuleNode</p>
</blockquote>
</aside>
<p>This is likely the solution, I can have the required tags inside a vtkMRMLScriptedModuleNode, but this module is hidden and not exportable to mrb. I tried setting tagnode.HideFromEditors to 0 and to False but nothing works.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a995a4574517ebbff3341edd534c93b9a75ff981.png" data-download-href="/uploads/short-url/ocdix2QPjUPdeMZq9t2aTdYV4CB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a995a4574517ebbff3341edd534c93b9a75ff981_2_539x499.png" alt="image" data-base62-sha1="ocdix2QPjUPdeMZq9t2aTdYV4CB" width="539" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a995a4574517ebbff3341edd534c93b9a75ff981_2_539x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a995a4574517ebbff3341edd534c93b9a75ff981.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a995a4574517ebbff3341edd534c93b9a75ff981.png 2x" data-dominant-color="EBEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">598×554 41.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So far so good BUT</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2272d7a3188e8f098132843c212b741872588a71.png" alt="image" data-base62-sha1="4UKhw9oY7qBgojnjvRKcRlV0eNH" width="598" height="445"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed64bb784a3caa260a3d9b61f2d4c8e9339bfa14.png" data-download-href="/uploads/short-url/xS4YFd6vwFozq0ose6fxlWie5fK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed64bb784a3caa260a3d9b61f2d4c8e9339bfa14_2_457x499.png" alt="image" data-base62-sha1="xS4YFd6vwFozq0ose6fxlWie5fK" width="457" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed64bb784a3caa260a3d9b61f2d4c8e9339bfa14_2_457x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed64bb784a3caa260a3d9b61f2d4c8e9339bfa14_2_685x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed64bb784a3caa260a3d9b61f2d4c8e9339bfa14_2_914x998.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1031×1128 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2019-08-14 12:37 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="6" data-topic="7999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Thats only useful if I have only one DICOM file, but I have several (several acquisitions in different times,</p>
</blockquote>
</aside>
<p>You can save patient-level tags in patient subject hierarchy item, study-level tags in study item, and series-level tags in the subject hierarchy item or in custom node attributes of the image, transform, etc. node. These tags are already automatically populated during DICOM import and used during DICOM export. Since you can save any additional custom tags there, I don’t see any reason why you would use a different mechanism.</p>
<p>Saving DICOM tags in scripted module nodes is possible, too, but you would need to manage association of these tags with data nodes. So, it is simpler to store these tags directly in the data node or the node’s subject hierarchy item.</p>
<p>Storing tags in the subject hierarchy item is useful if you want to allow the user to edit the DICOM patient/study/series tags (the tags are stored at one place, so you don’t need to worry about keeping redundant copies consistent) or you want to allow the users to create/change patients/studies/series  by drag-and-dropping items in the subject hierarchy tree. There is also GUI available to view/edit custom subject hierarchy item and node attributes, which is useful for advanced users and for debugging.</p>

---

## Post #9 by @Alex_Vergara (2019-08-14 13:19 UTC)

<p>I have tried what you seggested but I found this error</p>
<pre><code class="lang-auto">    node.SetParameter('DICOM.Acquisition', str(acquisition))
AttributeError: 'MRMLCorePython.vtkMRMLScalarVolumeNode' object has no attribute 'SetParameter'
</code></pre>
<p>However in the subject hierarchy item information I get<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6908388c459ffeb183d0a5d7991fdb03b2aad3e.png" data-download-href="/uploads/short-url/wTFr89gMye5TmvgI9Ziq6bbz7yK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6908388c459ffeb183d0a5d7991fdb03b2aad3e_2_557x500.png" alt="image" data-base62-sha1="wTFr89gMye5TmvgI9Ziq6bbz7yK" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6908388c459ffeb183d0a5d7991fdb03b2aad3e_2_557x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6908388c459ffeb183d0a5d7991fdb03b2aad3e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6908388c459ffeb183d0a5d7991fdb03b2aad3e.png 2x" data-dominant-color="E8EBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">597×535 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, How to access and set those attributes?</p>

---

## Post #10 by @Alex_Vergara (2019-08-14 13:25 UTC)

<p>OK found it! It is in the subject hierarchy structure itself, not in the node. Now exporting to mrb and drag and drop back maintain the required attributes!</p>
<pre data-code-wrap="python"><code class="lang-python">        shNode.SetItemAttribute(itemID, 'DICOM.Acquisition', str(acquisition))
        shNode.SetItemAttribute(itemID, 'DICOM.Modality', str(modality))
        acquisition = datetime.strptime(shNode.GetItemAttribute(itemID,'DICOM.Acquisition'), '%Y-%m-%d %H:%M:%S')
        modality = shNode.GetItemAttribute(itemID,'DICOM.Modality')
</code></pre>
<p>That was very well hidden in the source code!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca97d1ff9b3b4b39d1198c0a37e9aa0ed81cb40.png" data-download-href="/uploads/short-url/mlTC1VanE8jecO2tmuml5szQSYg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca97d1ff9b3b4b39d1198c0a37e9aa0ed81cb40_2_552x500.png" alt="image" data-base62-sha1="mlTC1VanE8jecO2tmuml5szQSYg" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca97d1ff9b3b4b39d1198c0a37e9aa0ed81cb40_2_552x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca97d1ff9b3b4b39d1198c0a37e9aa0ed81cb40.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca97d1ff9b3b4b39d1198c0a37e9aa0ed81cb40.png 2x" data-dominant-color="E8EBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">606×548 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2019-08-14 15:01 UTC)

<p>This is how the item attributes are populated in the DICOM plugin: <a href="https://github.com/Slicer/Slicer/blob/1b7888e90e233729e4beb4941e8b33e622373655/Modules/Scripted/DICOMLib/DICOMPlugin.py#L164" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/1b7888e90e233729e4beb4941e8b33e622373655/Modules/Scripted/DICOMLib/DICOMPlugin.py#L164</a></p>

---
