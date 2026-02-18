# Collision Detection

**Topic ID**: 19635
**Date**: 2021-09-12
**URL**: https://discourse.slicer.org/t/collision-detection/19635

---

## Post #1 by @Fluvio_Lobo (2021-09-12 23:40 UTC)

<p>Here is a follow-up on the topic of collision detection as suggested by <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> on <a href="https://discourse.slicer.org/t/surface-intersection/19630/6">this post</a>.</p>
<p>Following <a class="mention" href="/u/manjula">@manjula</a> example, I was able to integrate the <strong>vtk.collisionDetectionFilter()</strong> into my code;</p>
<pre><code class="lang-auto">def findMeshCollision( inputNodeNames, visibility=True, verbose=False ):
    '''
        Find Mesh Collision
            This function finds a collision or intersection between two surface meshesu=fluvio_lobo
    '''

    # Variables
    if isinstance( inputNodeNames, str ):
        inputNodeNames      = [ inputNodeNames ]
    numberOfNodes           = len( inputNodeNames )
    #collisionDetection      = vtkSRCP.vtkCollisionDetectionFilter()
    collisionDetection      = vtk.vtkCollisionDetectionFilter()
    numberOfCollisions      = 0
    collisionFlag           = False
    inputNodes              = []
    
    for i in range( 0, numberOfNodes ):
        inputNode           = slicer.util.getNode( inputNodeNames[i] )
        inputNodes.append( inputNode )

    # Collision Detection
    for i in range( 0, numberOfNodes-1 ):
        collisionDetection.SetInputData( 0, inputNodes[i].GetPolyData() )
        collisionDetection.SetInputData( 1, inputNodes[i+1].GetPolyData() )
        matrix              = vtk.vtkMatrix4x4()
        collisionDetection.SetMatrix( 0, matrix )
        collisionDetection.SetMatrix( 1, matrix )
        collisionDetection.SetBoxTolerance( 0.0 )
        collisionDetection.SetCellTolerance( 0.0 )
        collisionDetection.SetNumberOfCellsPerNode( 2 )
        collisionDetection.Update()
    
    numberOfCollisions      = collisionDetection.GetNumberOfContacts()
    if numberOfCollisions &gt; 0:
        collisionFlag       = True
    else:
        collisionFlag       = False
    
    # Status Verbose
    if(verbose):
        if(collisionFlag == True ):
            print( "{} Collisions Detected".format( numberOfCollisions ) )
        else:
            print( "No Collisions Detected" )

    # Return;
    return collisionFlag, numberOfCollisions
</code></pre>
<p>I had to use the <strong>vtk.collisionDetectionFilter()</strong> function call, <strong>vtkSlicerRtCommonPython.vtkCollisionDetectionFilter()</strong> kept giving the missing attribute error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "D:\Gits\DASH\cmf\_functions.py", line 365, in findMeshCollision
    collisionDetection      = vtkSRCP.vtkCollisionDetectionFilter()
AttributeError: module 'vtkSlicerRtCommonPython' has no attribute 'vtkCollisionDetectionFilter'
</code></pre>
<p>Either way, the function seems work thus far…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8de9e298db51b8c6f8f083eb0a4771a67f7a9cdc.jpeg" data-download-href="/uploads/short-url/kfqq2gI744UK4Vfx94LoLSYTGK8.jpeg?dl=1" title="separated" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de9e298db51b8c6f8f083eb0a4771a67f7a9cdc_2_345x191.jpeg" alt="separated" data-base62-sha1="kfqq2gI744UK4Vfx94LoLSYTGK8" width="345" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de9e298db51b8c6f8f083eb0a4771a67f7a9cdc_2_345x191.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de9e298db51b8c6f8f083eb0a4771a67f7a9cdc_2_517x286.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de9e298db51b8c6f8f083eb0a4771a67f7a9cdc_2_690x382.jpeg 2x" data-dominant-color="A09AAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">separated</span><span class="informations">1171×650 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">No Collisions Detected
(False, 0)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b134626cf6443998ba0a8836be31206c55a7e9b8.jpeg" data-download-href="/uploads/short-url/phCKdF6cUYlOkIpYuBm3UmEi7c4.jpeg?dl=1" title="collided" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b134626cf6443998ba0a8836be31206c55a7e9b8_2_345x191.jpeg" alt="collided" data-base62-sha1="phCKdF6cUYlOkIpYuBm3UmEi7c4" width="345" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b134626cf6443998ba0a8836be31206c55a7e9b8_2_345x191.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b134626cf6443998ba0a8836be31206c55a7e9b8_2_517x286.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b134626cf6443998ba0a8836be31206c55a7e9b8_2_690x382.jpeg 2x" data-dominant-color="9A98B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">collided</span><span class="informations">1171×650 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">56 Collisions Detected
(True, 56)
</code></pre>

---

## Post #2 by @mau_igna_06 (2021-09-12 23:50 UTC)

<blockquote>
<p><strong>vtkSlicerRtCommonPython.vtkCollisionDetectionFilter()</strong> kept giving the missing attribute error</p>
</blockquote>
<p>This happens because you need to install SlicerRT extension to use that class. But <code>vtk.vtkCollisionDetectionFilter()</code> class was added to Slicer core in recent Slicer Preview releases (it is the same filter)</p>

---

## Post #3 by @lassoan (2021-09-13 14:17 UTC)

<p>We had to remove vtkCollisionDetectionFilter from SlicerRT as it was not necessary anymore and it interfered with the one that is in VTK.</p>

---

## Post #4 by @mau_igna_06 (2021-09-13 14:56 UTC)

<blockquote>
<p>We had to remove vtkCollisionDetectionFilter from SlicerRT as it was not necessary anymore and it interfered with the one that is in VTK.</p>
</blockquote>
<p>Does SlicerRT on the Slicer Stable release have this filter? BoneReconstructionPlanner uses this filter and currently only works on Slicer Stable Release.<br>
Some functions BRP used changed name on preview release. Maybe I can have two different branches, one for each release type, if the answer to the question above is yes</p>

---

## Post #5 by @lassoan (2021-09-13 15:05 UTC)

<p>Slicer Stable Release (Slicer-4.11.20210226) uses VTK-8.2, which does not contain vtkCollisionDetectionFilter, so there SlicerRT provides it.</p>
<p>Usually we try to keep the same extension source code to work with the latest Slicer Stable Release and Slicer Preview Release and manage small API differences using if/else or try/except blocks. If this gets too complicated (e.g., in case of vtkCollisionDetectionFilter we should have moved the filter into a separate library to prevent the header files from clashing, which would have been too much work) then we create a separate branch, which usually means that the stable branch does not get any more updates (because we don’t have time to backport and test all changes).</p>

---

## Post #6 by @tsims (2021-09-16 14:54 UTC)

<p>Just wanted to jump into this thread, I implemented the code that Fluvio discussed above, and it seems to be working only when the transforms are hardened and won’t use geometry location if it is observing a transform node. Is there any way to make the vtkCollisionDetectionFilter observe a transform node?</p>

---

## Post #7 by @mau_igna_06 (2021-09-16 18:00 UTC)

<p>I would modify the function like this:</p>
<pre><code class="lang-auto">def findMeshCollision( node1, node2, verbose=False ):
    '''
        Find Mesh Collision
            This function finds a collision or intersection between two surface meshesu=fluvio_lobo
    '''
    #
    # Variables
    #collisionDetection      = vtkSRCP.vtkCollisionDetectionFilter()
    collisionDetection      = vtk.vtkCollisionDetectionFilter()
    numberOfCollisions      = 0
    collisionFlag           = False
    #
    # Collision Detection
    node1ToWorldTransformMatrix = vtk.vtkMatrix4x4()
    node2ToWorldTransformMatrix = vtk.vtkMatrix4x4()
    node1ParentTransformNode = node1.GetParentTransformNode()
    node2ParentTransformNode = node2.GetParentTransformNode()
    if node1ParentTransformNode != None:
        node1ParentTransformNode.GetMatrixTransformToWorld(node1ToWorldTransformMatrix)
    if node2ParentTransformNode != None:
        node2ParentTransformNode.GetMatrixTransformToWorld(node2ToWorldTransformMatrix)
    #
    collisionDetection.SetInputData( 0, node1.GetPolyData() )
    collisionDetection.SetInputData( 1, node2.GetPolyData() )
    collisionDetection.SetMatrix( 0, node1ToWorldTransformMatrix )
    collisionDetection.SetMatrix( 1, node2ToWorldTransformMatrix )
    collisionDetection.SetBoxTolerance( 0.0 )
    collisionDetection.SetCellTolerance( 0.0 )
    collisionDetection.SetNumberOfCellsPerNode( 2 )
    collisionDetection.Update()
    #
    numberOfCollisions      = collisionDetection.GetNumberOfContacts()
    if numberOfCollisions &gt; 0:
        collisionFlag       = True
    else:
        collisionFlag       = False
    #
    # Status Verbose
    if(verbose):
        if(collisionFlag == True ):
            print( "{} Collisions Detected".format( numberOfCollisions ) )
        else:
            print( "No Collisions Detected" )
    #
    # Return;
    return collisionFlag, numberOfCollisions
</code></pre>
<p>Hope it helps</p>

---
