---
topic_id: 45362
title: "How To Get The Ijk Coordinate Of A Fiducial Node In 3D Slice"
date: 2025-12-04
url: https://discourse.slicer.org/t/45362
---

# How to get the IJK coordinate of a fiducial node in 3d slicer development

**Topic ID**: 45362
**Date**: 2025-12-04
**URL**: https://discourse.slicer.org/t/how-to-get-the-ijk-coordinate-of-a-fiducial-node-in-3d-slicer-development/45362

---

## Post #1 by @zhutouzjq (2025-12-04 02:38 UTC)

<p>thank the help provided by jamesobulter and cpinter, now i can successfully choose the fiducial in myself extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28d2a9002167cd5ab11adf2bca1c4418aef02caf.png" data-download-href="/uploads/short-url/5P8r2sUa8XgP208KxkuNxYZWCwn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d2a9002167cd5ab11adf2bca1c4418aef02caf_2_690x173.png" alt="image" data-base62-sha1="5P8r2sUa8XgP208KxkuNxYZWCwn" width="690" height="173" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d2a9002167cd5ab11adf2bca1c4418aef02caf_2_690x173.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d2a9002167cd5ab11adf2bca1c4418aef02caf_2_1035x259.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28d2a9002167cd5ab11adf2bca1c4418aef02caf.png 2x" data-dominant-color="AEAEAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1287×323 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but i fail to get the ijk coordinate of this fudicial node in my extension. i can only get the ras coordinate through the python code in class called ‘Logic‘.</p>
<p>def process(self,</p>
<pre><code>            inputVolume: vtkMRMLScalarVolumeNode,

            imageThreshold: float,

            inputlowerpoint, #this is the name of qMRMLNodeCombobox by which i choose the fiducial node in 3D slicer

            inputupperpoint,

            showResult: bool = True) -&gt; None:

    ras = vtk.vtkVector3d(0,0,0)

    inputlowerpoint.GetNthControlPointPositionWorld(0, ras)

    print('lowerpoint : IJK =’,ras)
</code></pre>
<p>after running the extension, the result in pyhton console like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09da4ac3446f28ed098d31b7f71184087ccf0e3.png" data-download-href="/uploads/short-url/ykAlcIFnlv3vQgTHiMEDqwO7tXZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09da4ac3446f28ed098d31b7f71184087ccf0e3_2_690x118.png" alt="image" data-base62-sha1="ykAlcIFnlv3vQgTHiMEDqwO7tXZ" width="690" height="118" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09da4ac3446f28ed098d31b7f71184087ccf0e3_2_690x118.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09da4ac3446f28ed098d31b7f71184087ccf0e3_2_1035x177.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09da4ac3446f28ed098d31b7f71184087ccf0e3.png 2x" data-dominant-color="C8C7C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1305×224 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>however, what i need is the IJK coordinate of this fudicial node. So, how can i get the IJK coordinate of a fiducial node and print in the python console?</p>

---

## Post #2 by @muratmaga (2025-12-04 03:09 UTC)

<p>AI is great for this type of things. I asked your question to Gemini:</p>
<p>“how can I get the IJK coordinates of Fiducial point that I know its world coordinates (RAS) using Slicer’s python API? Assume the coordinate is in the first control point of PointList F”</p>
<p>and I got</p>
<pre><code class="lang-auto">import slicer
import vtk
import numpy as np

# 1. Define the RAS coordinates (World Coordinates)
ras_point = np.array([-38.0, 24.0, -617.0, 1.0]) # Homogeneous coordinates (R, A, S, 1)

# 2. Get the reference volume node
# Replace 'YourVolumeNodeName' with the actual name or ID of your loaded volume node.
# For example, if you have the built-in MRHead:
volumeNode = slicer.util.getNode('MRHead')

if volumeNode is None:
    print("Error: Volume node not found. Please load a volume into the scene.")
else:
    # 3. Get the WorldToIJK transform matrix from the volume node
    worldToIjkMatrix = vtk.vtkMatrix4x4()
    volumeNode.GetWorldToIJKMatrix(worldToIjkMatrix)
    
    # You can convert the vtkMatrix4x4 to a numpy array for easier calculation
    worldToIjkNp = slicer.util.vtkMatrixToNumpy(worldToIjkMatrix)
    
    # 4. Calculate the IJK coordinates
    # Matrix multiplication: [I, J, K, 1] = WorldToIJK_Matrix @ [R, A, S, 1]
    ijk_point_homog = worldToIjkNp @ ras_point
    
    # The IJK coordinates are the first three components (the last is 1.0)
    # The coordinates are typically rounded to the nearest integer for voxel indices.
    ijk_point = np.round(ijk_point_homog[:3]).astype(int)
    
    print(f"RAS Coordinates (R, A, S): {ras_point[:3]}")
    print(f"IJK Coordinates (I, J, K): {ijk_point}")
    
    # Optional: Display the IJK coordinates for a specific fiducial point
    # in an existing markups node (if needed for context)
    # fiducialNode = slicer.util.getNode('F') # Replace 'F' with your markups node name
    # if fiducialNode:
    #     fiducialNode.SetNthControlPointPositionWorld(0, ras_point[0], ras_point[1], ras_point[2])
    #     # After setting the position, you can use the node's internal function to get IJK:
    #     # ijk = [0, 0, 0]
    #     # fiducialNode.GetNthControlPointPositionIJK(0, ijk)
    #     # print(f"IJK from Markups node: {ijk}")
</code></pre>
<p>which seems to work.</p>

---

## Post #3 by @zhutouzjq (2025-12-04 03:13 UTC)

<p>thank the discussion in “<a href="https://discourse.slicer.org/t/ras-to-ijk-conversion-issues/41863">RAS to IJK conversion issues</a>“. the reply by muratmaga help me a lot.</p>
<p>in the script repository of 3D slicer, they suggest use the follow code to transform the ras to ijk:</p>
<pre><code class="lang-auto"># Inputs
volumeNode = getNode("MRHead")
pointListNode = getNode("F")
markupsIndex = 0

# Get point coordinate in RAS
point_Ras = [0, 0, 0]
pointListNode.GetNthControlPointPositionWorld(markupsIndex, point_Ras)

# If volume node is transformed, apply that transform to get volume's RAS coordinates
transformRasToVolumeRas = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transformRasToVolumeRas)
point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras)

# Get voxel coordinates from physical coordinates
volumeRasToIjk = vtk.vtkMatrix4x4()
volumeNode.GetRASToIJKMatrix(volumeRasToIjk)
point_Ijk = [0, 0, 0, 1]
volumeRasToIjk.MultiplyPoint(np.append(point_VolumeRas,1.0), point_Ijk)
point_Ijk = [ int(round(c)) for c in point_Ijk[0:3] ]

# Print output
print(point_Ijk)
</code></pre>
<p>but what i didn’t know is that in my code, the second line “volumeNode = getNode(“MRHead”)” should be change into “volumeNode = slicer.util.getNode(“5: CTA 0.5 CE”)“.</p>
<p>“MRHead“ or “5: CTA 0.5 CE“ is the name of volume which could be found here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/757124617e2ec162960d71567ac1c32d398beb95.png" data-download-href="/uploads/short-url/gKWgJuVXID6nLHIp3KAUDSofrSd.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/757124617e2ec162960d71567ac1c32d398beb95_2_463x499.png" alt="无标题" data-base62-sha1="gKWgJuVXID6nLHIp3KAUDSofrSd" width="463" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/757124617e2ec162960d71567ac1c32d398beb95_2_463x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/757124617e2ec162960d71567ac1c32d398beb95.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/757124617e2ec162960d71567ac1c32d398beb95.png 2x" data-dominant-color="F3F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">662×714 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and use the python code like this in Logic class, i can print the IJK coordinate in console now.</p>
<pre><code>def process(self,

            inputVolume: vtkMRMLScalarVolumeNode,

            imageThreshold: float,

            inputlowerpoint,

            inputupperpoint,

            showResult: bool = True) -&gt; None:

    """

    Run the processing algorithm.

    Can be used without GUI widget.

    :param inputVolume: volume to be thresholded

    :param outputVolume: thresholding result

    :param imageThreshold: values above/below this threshold will be set to 0

    :param invert: if True then values above the threshold will be set to 0, otherwise values below are set to 0

    :param showResult: show output volume in slice viewers

    """



    if not inputVolume:

        raise ValueError("Input volume is invalid")



    import time



    startTime = time.time()

    logging.info("Processing started")



    volumeNode = slicer.util.getNode("5: CTA 0.5 CE")

    markupsIndex = 0

    point_Ras = \[0, 0, 0\]

    inputlowerpoint.GetNthControlPointPositionWorld(markupsIndex, point_Ras)

    

    transformRasToVolumeRas = vtk.vtkGeneralTransform()

    slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transformRasToVolumeRas)

    point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras)



    \# Get voxel coordinates from physical coordinates

    volumeRasToIjk = vtk.vtkMatrix4x4()

    volumeNode.GetRASToIJKMatrix(volumeRasToIjk)

    point_Ijk = \[0, 0, 0, 1\]

    volumeRasToIjk.MultiplyPoint(np.append(point_VolumeRas,1.0), point_Ijk)

    point_Ijk = \[ int(round(c)) for c in point_Ijk\[0:3\] \]

    print('lowerpoint : RAS =',point_Ras)

    print('lowerpoint : IJK =',point_Ijk)



    stopTime = time.time()

    logging.info(f"Processing completed in {stopTime-startTime:.2f} seconds")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fd4f99f5d519128e5ecd605e4d8ee52379097ef.png" data-download-href="/uploads/short-url/fXjimKC9GXbjXeQs620NoG8XbZl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fd4f99f5d519128e5ecd605e4d8ee52379097ef_2_690x98.png" alt="image" data-base62-sha1="fXjimKC9GXbjXeQs620NoG8XbZl" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fd4f99f5d519128e5ecd605e4d8ee52379097ef_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fd4f99f5d519128e5ecd605e4d8ee52379097ef_2_1035x147.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fd4f99f5d519128e5ecd605e4d8ee52379097ef.png 2x" data-dominant-color="F2F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1300×186 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @zhutouzjq (2025-12-04 03:17 UTC)

<p>thank you for your reply. with your discussion under the issue “<a href="https://discourse.slicer.org/t/ras-to-ijk-conversion-issues/41863">RAS to IJK conversion issues</a>“, i have solve this problem. your are very professional in developping 3d slicer extension</p>

---
