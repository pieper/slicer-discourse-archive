# How to convert a model into a volume and then compress it into a plane (volume) in a direction?

**Topic ID**: 28983
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/how-to-convert-a-model-into-a-volume-and-then-compress-it-into-a-plane-volume-in-a-direction/28983

---

## Post #1 by @jumbojing (2023-04-18 12:57 UTC)

<p>How to convert a model into a volume and then compress it into a plane (a volume with one slice) in a direction?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@pieper@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @pieper (2023-04-18 14:02 UTC)

<p>You can load it as a segmentation and then get the numpy array so you can use <a href="https://numpy.org/doc/stable/reference/generated/numpy.sum.html">sum</a> or similar.</p>

---

## Post #4 by @jumbojing (2023-04-18 23:08 UTC)

<p>At 1St, convert a model into a segmentation…as👇…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a331a0f431ed878046f147ce937c11c8bd08900d.jpeg" data-download-href="/uploads/short-url/nhG9Ivb6dajrK11WtM0zJOazbbL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a331a0f431ed878046f147ce937c11c8bd08900d_2_619x500.jpeg" alt="image" data-base62-sha1="nhG9Ivb6dajrK11WtM0zJOazbbL" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a331a0f431ed878046f147ce937c11c8bd08900d_2_619x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a331a0f431ed878046f147ce937c11c8bd08900d_2_928x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a331a0f431ed878046f147ce937c11c8bd08900d_2_1238x1000.jpeg 2x" data-dominant-color="64636A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1664×1344 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">the model</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a270ca1ce8e4a941f68ca835ba9484468e351357.jpeg" data-download-href="/uploads/short-url/nb102lkrLBq836WiHf8uoVJ9va7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a270ca1ce8e4a941f68ca835ba9484468e351357_2_558x500.jpeg" alt="image" data-base62-sha1="nb102lkrLBq836WiHf8uoVJ9va7" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a270ca1ce8e4a941f68ca835ba9484468e351357_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a270ca1ce8e4a941f68ca835ba9484468e351357_2_837x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a270ca1ce8e4a941f68ca835ba9484468e351357_2_1116x1000.jpeg 2x" data-dominant-color="6C6D62"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1550×1388 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">the segmentation</p>
<p>The segmentation converted is not the desired result on the two-dimensional slice…<br>
<img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"> This is the attachment:</p>
<p><a href="https://drive.google.com/file/d/1h9v8fWfetG2iAab8ZVABcSEaYzvQMitk/view?usp=share_link" rel="noopener nofollow ugc">test.mrb</a></p>

---

## Post #5 by @pieper (2023-04-19 14:40 UTC)

<p>The stl is not a closed surface so the rasterization fails.  Probably you can fix it in some cad tool or your could try rotating it so that the open ends align with the rasterization planes.</p>

---

## Post #6 by @lassoan (2023-04-20 04:23 UTC)

<p>You can project a model node to the current slice plane by setting in Models module: Display / Slice display / Mode → Projection. Also enable Visibility and reduce Opacity a bit in that section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4432f3954b90abe087112ef3c301229c2757ea4b.png" data-download-href="/uploads/short-url/9JjD7PpDQgZGcNO4UGCnzyaSb4T.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4432f3954b90abe087112ef3c301229c2757ea4b_2_690x341.png" alt="image" data-base62-sha1="9JjD7PpDQgZGcNO4UGCnzyaSb4T" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4432f3954b90abe087112ef3c301229c2757ea4b_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4432f3954b90abe087112ef3c301229c2757ea4b_2_1035x511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4432f3954b90abe087112ef3c301229c2757ea4b_2_1380x682.png 2x" data-dominant-color="69696B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1115 457 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Distance encoded projection option may be useful, too:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8a148465598a970bb83a564e1ea6040fb05c3b1.jpeg" data-download-href="/uploads/short-url/qljoOVM56cWy1f10kvul7XGAn3X.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a148465598a970bb83a564e1ea6040fb05c3b1_2_581x500.jpeg" alt="image" data-base62-sha1="qljoOVM56cWy1f10kvul7XGAn3X" width="581" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a148465598a970bb83a564e1ea6040fb05c3b1_2_581x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a148465598a970bb83a564e1ea6040fb05c3b1_2_871x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a148465598a970bb83a564e1ea6040fb05c3b1_2_1162x1000.jpeg 2x" data-dominant-color="8A8A8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1288×1107 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note that these projection modes can be also used for visualizing the pedical screws.</p>

---

## Post #7 by @jumbojing (2023-04-26 04:30 UTC)

<p>Another solution: I attempted to project this model onto a plane in one direction, resulting in an array containing all coordinate points Then, project these point coordinates onto an empty volume. However, the current problem is how to generate a <code>schalar volume</code> (or <code>binary labelmap</code>) from a set of point clouds located on a certain plane in 3D space?</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">My failed code, got a empty volume:</p>
<pre><code class="lang-auto">def ps2vol(ps, modName='vol'):
    ps = np.asarray(ps)
    # psX轴的最大值-最小值
    l = len(ps)
    norm = Helper.p3Nor(ps[0], ps[int(l/3)], ps[int(l/3*2)])
    dimX = int(ps[:, 0].max() - ps[:, 0].min())+1
    dimY = int(ps[:, 1].max() - ps[:, 1].min())+1
    dimZ = int(ps[:, 2].max() - ps[:, 2].min())+1
    # 创建vtkImageData数据
    imageSize = [dimX, dimY, dimZ]
    voxelType=vtk.VTK_UNSIGNED_CHAR
    imageOrigin = [ps[:, 0].min(), ps[:, 1].min(), ps[:, 2].min()]
    imageSpacing = [1.0, 1.0, 1.0]
    imageDirections = np.diag(norm)
    fillVoxelValue = 0
    # Create an empty image volume, filled with fillVoxelValue
    imageData = vtk.vtkImageData()
    imageData.SetDimensions(imageSize)
    imageData.AllocateScalars(voxelType, 1)
    imageData.GetPointData().GetScalars().Fill(fillVoxelValue)
    # 将有点的位置设置为1
    for point in ps:
        i, j, k = int(point[0]), int(point[1]), int(point[2])
        imageData.SetScalarComponentFromDouble(i, j, k, 0, 1) #
    imageData.Modified()
#     writer = vtk.vtkXMLImageDataWriter()
#     writer.SetInputData(imageData)
#     writer.SetFileName(modName+'.vti')
#     writer.Write()
#     # Create volume node
    volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", modName)
    volumeNode.SetOrigin(imageOrigin)
    volumeNode.SetSpacing(imageSpacing)
    volumeNode.SetIJKToRASDirections(imageDirections)
    volumeNode.SetAndObserveImageData(imageData)
    volumeNode.CreateDefaultDisplayNodes()
    volumeNode.CreateDefaultStorageNode()
    return volumeNode
</code></pre>
<p><a href="https://drive.google.com/file/d/13T8Mswa18OOogUkBl_Bw_T_wHCEpV3Tg/view?usp=sharing" rel="noopener nofollow ugc">Point cloud files: pjArr.npy</a></p>
<p>pointCloud with markPoint:<img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e0bcb6ae88a958631ea25a1311599acb2dd5b9d.jpeg" data-download-href="/uploads/short-url/4hNAP3yzPEGTjrunrNQ6Ix5rDM9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e0bcb6ae88a958631ea25a1311599acb2dd5b9d_2_642x500.jpeg" alt="image" data-base62-sha1="4hNAP3yzPEGTjrunrNQ6Ix5rDM9" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e0bcb6ae88a958631ea25a1311599acb2dd5b9d_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e0bcb6ae88a958631ea25a1311599acb2dd5b9d_2_963x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e0bcb6ae88a958631ea25a1311599acb2dd5b9d_2_1284x1000.jpeg 2x" data-dominant-color="9796C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1706×1328 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @jumbojing (2023-05-03 04:07 UTC)

<p>???<img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"></p>
<p>what’s wrong?</p>

---
