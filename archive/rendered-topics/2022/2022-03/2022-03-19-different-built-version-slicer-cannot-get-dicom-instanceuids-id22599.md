# different built version slicer cannot get dicom.instanceUIDs attribute

**Topic ID**: 22599
**Date**: 2022-03-19
**URL**: https://discourse.slicer.org/t/different-built-version-slicer-cannot-get-dicom-instanceuids-attribute/22599

---

## Post #1 by @luxiaoyanglxy9999 (2022-03-19 12:23 UTC)

<p>Hi,</p>
<p>When use a self-build verison slicer (the latest slicer code and source code version: Slicer-88f0c40fa19d00616ba984abd0512e540a974525), I found I cannot get the DICOM.instanceUIDs vtkMRMLScalarVolumeNode as follows.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7fd4c86261ac5166cb1bb12c9c14b855e1df86.png" data-download-href="/uploads/short-url/fLwoIY1JJhQQcdUJ5nGNReULvNA.png?dl=1" title="badone" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7fd4c86261ac5166cb1bb12c9c14b855e1df86.png" alt="badone" data-base62-sha1="fLwoIY1JJhQQcdUJ5nGNReULvNA" width="690" height="480" data-dominant-color="384552"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">badone</span><span class="informations">1155×804 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, in my previous self-build slicer (4.11.0), there is a DICOM.instanceUIDs attribute in vtkMRMLScalarVolumeNode as follows.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dacc0c1a70276524fc540c57c96abbd00673dda.png" data-download-href="/uploads/short-url/kdjrzVYbOWTT48wqsNAEyoBsOWm.png?dl=1" title="KO~E%2F``$MW7H73UH9F_3R" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dacc0c1a70276524fc540c57c96abbd00673dda.png" alt="KO~E%2F``$MW7H73UH9F_3R" data-base62-sha1="kdjrzVYbOWTT48wqsNAEyoBsOWm" width="690" height="495" data-dominant-color="384654"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KO~E%2F``$MW7H73UH9F_3R</span><span class="informations">1005×721 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>why this happens? what should I do to solve this problem?</p>

---

## Post #2 by @pieper (2022-03-19 15:59 UTC)

<p>The volume node will only have the <code>dicom.instanceUIDs</code> attribute if it was loaded through the DICOM module.  Check that you loaded the data the same way in both your Slicer versions.</p>

---

## Post #3 by @luxiaoyanglxy9999 (2022-03-20 04:03 UTC)

<p>Yes, I use the same way to load dicom data, it is shown as follows.</p>
<pre><code class="lang-auto">                with DICOMUtils.TemporaryDICOMDatabase(sql_folder_path) as db:
                    DICOMUtils.importDicom(dicomDataDir, db)
                    patientUIDs = db.patients()
                    for patientUID in patientUIDs:
                        loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
                        loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>

---

## Post #4 by @lassoan (2022-03-20 12:31 UTC)

<p>Are the dicom.instanceUIDs there if you use the latest Slicer Preview Release?</p>

---

## Post #5 by @luxiaoyanglxy9999 (2022-03-21 11:09 UTC)

<p>I use the same code in the latest Slicer Preview Release to get DICOM.instancesUIDs,</p>
<pre><code class="lang-auto">redCompsiteNode=slicer.app.layoutManager().sliceWidget("Green").sliceLogic().GetSliceCompositeNode()
volumeID=redCompsiteNode.GetBackgroundVolumeID()
key='0010,0010'
volumeNode = slicer.util.getNode(volumeID)
value = slicer.dicomDatabase.instanceValue(volumeNode.GetAttribute('DICOM.instanceUIDs'), key)
</code></pre>
<p>but it occurs an error in redCompsiteNode.GetBackgroundVolumeID() . But this code does not report error in my sekf-build slicer with latest source code.</p>

---

## Post #6 by @lassoan (2022-03-21 12:21 UTC)

<aside class="quote no-group" data-username="luxiaoyanglxy9999" data-post="5" data-topic="22599">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luxiaoyanglxy9999/48/14719_2.png" class="avatar"> luxiaoyanglxy9999:</div>
<blockquote>
<p>but it occurs an error in redCompsiteNode.GetBackgroundVolumeID()</p>
</blockquote>
</aside>
<p>What is the error message?</p>

---

## Post #7 by @luxiaoyanglxy9999 (2022-03-22 05:30 UTC)

<p>There is an error as the value of  volumeID is None.</p>
<pre><code class="lang-auto">redCompsiteNode = slicer.app.layoutManager().sliceWidget("Green").sliceLogic().GetSliceCompositeNode()
volumeID=redCompsiteNode.GetBackgroundVolumeID()
</code></pre>
<p>Moreover, When I use load two dicom data, there is only one dicom data is shown in windows, but my self-build version will display both two dicom data in all windows as shown in follows.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f41919106e4b41721b074be8498d13c1786582f.jpeg" data-download-href="/uploads/short-url/kriL1ggMhgHb4628EOTmKDp47ZZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41919106e4b41721b074be8498d13c1786582f_2_690x273.jpeg" alt="image" data-base62-sha1="kriL1ggMhgHb4628EOTmKDp47ZZ" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41919106e4b41721b074be8498d13c1786582f_2_690x273.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41919106e4b41721b074be8498d13c1786582f_2_1035x409.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f41919106e4b41721b074be8498d13c1786582f_2_1380x546.jpeg 2x" data-dominant-color="1B1B1B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1637×650 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d937d8777e20aa576a164085411af654fc256ac.jpeg" data-download-href="/uploads/short-url/8MJ7AadlTYfaqaynddbCbvogO8k.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d937d8777e20aa576a164085411af654fc256ac_2_690x294.jpeg" alt="image" data-base62-sha1="8MJ7AadlTYfaqaynddbCbvogO8k" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d937d8777e20aa576a164085411af654fc256ac_2_690x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d937d8777e20aa576a164085411af654fc256ac_2_1035x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d937d8777e20aa576a164085411af654fc256ac_2_1380x588.jpeg 2x" data-dominant-color="1F1E1F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1624×694 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Additionally, due to this error, the I cannot run my code in these versions Slicer, so I want to build a  Slicer use former source code ,but I cannot download former soruce code as follows.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de5c503058cd5de9cb72555d41e0e3b586bf1b08.jpeg" data-download-href="/uploads/short-url/vJ5Mh5ywXlWkVPx1j7J1wq99rcI.jpeg?dl=1" title="d80b61cb17c50cd270f4e8fb8514ef6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5c503058cd5de9cb72555d41e0e3b586bf1b08_2_690x349.jpeg" alt="d80b61cb17c50cd270f4e8fb8514ef6" data-base62-sha1="vJ5Mh5ywXlWkVPx1j7J1wq99rcI" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5c503058cd5de9cb72555d41e0e3b586bf1b08_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5c503058cd5de9cb72555d41e0e3b586bf1b08_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de5c503058cd5de9cb72555d41e0e3b586bf1b08.jpeg 2x" data-dominant-color="2D1F21"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">d80b61cb17c50cd270f4e8fb8514ef6</span><span class="informations">1130×573 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c295120eca7781d0cb0c11c322b6b5d5a85b2d34.jpeg" data-download-href="/uploads/short-url/rLm0HUeuUs9FnwBXlGoPsG6PUOM.jpeg?dl=1" title="223d4df55e62fdf493fc81c35bb9874" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c295120eca7781d0cb0c11c322b6b5d5a85b2d34_2_690x167.jpeg" alt="223d4df55e62fdf493fc81c35bb9874" data-base62-sha1="rLm0HUeuUs9FnwBXlGoPsG6PUOM" width="690" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c295120eca7781d0cb0c11c322b6b5d5a85b2d34_2_690x167.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c295120eca7781d0cb0c11c322b6b5d5a85b2d34_2_1035x250.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c295120eca7781d0cb0c11c322b6b5d5a85b2d34.jpeg 2x" data-dominant-color="232023"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">223d4df55e62fdf493fc81c35bb9874</span><span class="informations">1141×277 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Could you please tell me how to get foremer Slcier source code?</p>

---

## Post #8 by @lassoan (2022-03-22 06:29 UTC)

<p>All Slicer versions are available at <a href="https://github.com/Slicer/Slicer/commits/master">https://github.com/Slicer/Slicer/commits/master</a>.</p>
<p>It looks like you are loading a GE Invenia ABUS image. A <a href="https://discourse.slicer.org/t/load-ge-invenia-abus-images-from-dicom/15067">reader plugin for such images was added to Slicer Preview Release a couple of months ago</a>.</p>
<p>To load the images correctly (i.e., reconstructing the curved geometry), make sure that the <code>DICOMGeAbusPlugin</code> plugin is enabled in DICOM module / DICOM Plugins section. <code>DICOM.instanceUIDs</code> is only set if loaded by <code>DICOMScalarVolumePlugin</code>. For all other DICOM data objects, such as the ABUS image, you can get the series instance UID from the subject hierarchy, as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-an-item-in-the-subject-hierarchy-tree">here</a>.</p>

---

## Post #9 by @luxiaoyanglxy9999 (2022-03-23 03:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="22599">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DICOMScalarVolumePlugin</p>
</blockquote>
</aside>
<p>I have check the node type and it is MRMLCore.vtkMRMLScalarVolumeNode, so I think  maybe it is loaded by DICOMScalarVolumePlugin, is it correct?, If not, how can I use DICOMScalarVolumePlugin to load dicom data? Moreover, I also try to get the series instance UID from the subject hierarchy, but I cannot use series UID to get instance UID, the return of following code is empty.</p>
<pre><code class="lang-auto">redCompsiteNode = slicer.app.layoutManager().sliceWidget("Green").sliceLogic().GetSliceCompositeNode()
volumeID=redCompsiteNode.GetBackgroundVolumeID()
volumeNode = slicer.util.getNode(volumeID)

# Get series instance UID from subject hierarchy
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
volumeItemId = shNode.GetItemByDataNode(volumeNode)
seriesInstanceUID = shNode.GetItemUID(volumeItemId, 'DICOM')

instUids = slicer.dicomDatabase.instancesForSeries(seriesInstanceUID)
</code></pre>

---

## Post #10 by @lassoan (2022-04-09 18:23 UTC)

<p>There are a number of DICOM reader plugins that create a scalar volume node. DICOMScalarVolumePlugin is just the generic 3D volume reader.</p>
<p>Does <code>seriesInstanceUID</code> look valid? Does it match the series instance UID in the DICOM metadata in the DICOM browser?</p>

---
