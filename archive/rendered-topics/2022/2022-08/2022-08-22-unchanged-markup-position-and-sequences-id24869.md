---
topic_id: 24869
title: "Unchanged Markup Position And Sequences"
date: 2022-08-22
url: https://discourse.slicer.org/t/24869
---

# Unchanged Markup Position and Sequences

**Topic ID**: 24869
**Date**: 2022-08-22
**URL**: https://discourse.slicer.org/t/unchanged-markup-position-and-sequences/24869

---

## Post #1 by @ChristophG123 (2022-08-22 16:34 UTC)

<p>Slicer Version: 5.1.0-2022-07-17<br>
OS: Windows 10</p>
<p>Hi,<br>
I made a sequence where I tracked 1 transformed markup list at 22 different positions (as 22 sequences). However, when I try copy and pasting each of the unique marker positions into a new markup list, it just pastes the original position of the markups rather than each tracked and transformed position. For example, when I try copy and pasting “bigHole”:<br>
At 0.10s, the position of the points “bigHole” and “smallHole” in “trackLine” are this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b0a9be3a60245e2ee5e2c09b8cc024ed1dade2b.png" data-download-href="/uploads/short-url/hytsqacdhtNFzNCgaDi89lBsI1J.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b0a9be3a60245e2ee5e2c09b8cc024ed1dade2b_2_597x500.png" alt="image" data-base62-sha1="hytsqacdhtNFzNCgaDi89lBsI1J" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b0a9be3a60245e2ee5e2c09b8cc024ed1dade2b_2_597x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b0a9be3a60245e2ee5e2c09b8cc024ed1dade2b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b0a9be3a60245e2ee5e2c09b8cc024ed1dade2b.png 2x" data-dominant-color="D4D5D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">763×638 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then when I try copy and pasting the position of “bigHole” into the new markup list “tracked_BigHole”, it just gives the original untransformed and untracked position of “bigHole”:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e67dd81fbb2119bc2c4be2cb502b6e8f58f694c.png" data-download-href="/uploads/short-url/i2eGSqOYh8QIDESiTScEEoT6Fmk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e67dd81fbb2119bc2c4be2cb502b6e8f58f694c_2_485x500.png" alt="image" data-base62-sha1="i2eGSqOYh8QIDESiTScEEoT6Fmk" width="485" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e67dd81fbb2119bc2c4be2cb502b6e8f58f694c_2_485x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e67dd81fbb2119bc2c4be2cb502b6e8f58f694c_2_727x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e67dd81fbb2119bc2c4be2cb502b6e8f58f694c.png 2x" data-dominant-color="CFD3D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">763×785 56.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a8ecacdc8820156a2f2e16f1a52c070a97da01.png" data-download-href="/uploads/short-url/7EHdX1FpIevpnN4fNWrb5qF93hf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35a8ecacdc8820156a2f2e16f1a52c070a97da01_2_556x499.png" alt="image" data-base62-sha1="7EHdX1FpIevpnN4fNWrb5qF93hf" width="556" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35a8ecacdc8820156a2f2e16f1a52c070a97da01_2_556x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a8ecacdc8820156a2f2e16f1a52c070a97da01.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a8ecacdc8820156a2f2e16f1a52c070a97da01.png 2x" data-dominant-color="D6D7D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×686 42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The same thing happens when I try it at other time positions. For example, at 0.4s:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ee54ceb58ebbf46bdb39ecd2312cdeed6d4a265.png" data-download-href="/uploads/short-url/ko74DtLd6OzkpKe0hJHFANbEVff.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ee54ceb58ebbf46bdb39ecd2312cdeed6d4a265_2_570x500.png" alt="image" data-base62-sha1="ko74DtLd6OzkpKe0hJHFANbEVff" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ee54ceb58ebbf46bdb39ecd2312cdeed6d4a265_2_570x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ee54ceb58ebbf46bdb39ecd2312cdeed6d4a265.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ee54ceb58ebbf46bdb39ecd2312cdeed6d4a265.png 2x" data-dominant-color="D4D5D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">766×671 46.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9774708b4a37c4bdf6773c47b6813afbc09e286c.png" data-download-href="/uploads/short-url/lBPzgpjorfHc5o0rWTPgthyGu4c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9774708b4a37c4bdf6773c47b6813afbc09e286c_2_593x500.png" alt="image" data-base62-sha1="lBPzgpjorfHc5o0rWTPgthyGu4c" width="593" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9774708b4a37c4bdf6773c47b6813afbc09e286c_2_593x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9774708b4a37c4bdf6773c47b6813afbc09e286c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9774708b4a37c4bdf6773c47b6813afbc09e286c.png 2x" data-dominant-color="D5D7D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">765×644 43.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, the reason why I’m doing this manually is because when I took the tracked points, the sequence “wireToProbe” I created to record these markup positions didn’t take any of the positions for some reason. This may have been a mistake on my part, though:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58af5117f655579a3dee9d2a99641a30d2822a7b.png" alt="image" data-base62-sha1="cExDaPM9vdc7sxeZkm9umHgkIu7" width="641" height="407"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e89f51e75b0059610e89958636af4934950432.png" data-download-href="/uploads/short-url/axPfhdDthCaRP8kWnxIJE7g2E02.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e89f51e75b0059610e89958636af4934950432.png" alt="image" data-base62-sha1="axPfhdDthCaRP8kWnxIJE7g2E02" width="508" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">622×612 15.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,<br>
Chris</p>

---

## Post #2 by @pieper (2022-08-22 19:54 UTC)

<p>Did you try hardening the markups?</p>

---

## Post #3 by @ChristophG123 (2022-08-22 21:20 UTC)

<p>I just tried that, and it does work the first time. But then when I try applying “trackLine” back to its original transform “PlatformToMarker2” so I can get the position of the next sequence, I think it applies “PlatformToMarker2” to the hardened transformed points rather than the original points. This causes my points to move into this strange position:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc09311ace4d2ba605796d8c4855c3e0a99ed7c9.png" alt="image" data-base62-sha1="zXC0ZdKfty65InqVhJ6CEMq9FIB" width="234" height="171"></p>
<p>One other solution I’ve been working on is writing a small Slicer Module instead. So far, I can loop through each sequence and acquire the values of the transform “PlatformToMarker2”, and have the original untransformed points of “trackLine”. Right now, I’m trying to use a Slicer transform function which I thought would just do the same thing as dragging my Markup list onto a Slicer transform, but the new positions end up looking like this instead:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25131ea1a1b65b868b794f7d542a13548366a0fc.png" alt="image" data-base62-sha1="5hYD40KchfzJZCmtAuReirukGoA" width="433" height="213"></p>
<p>The code I’ve tried using looks like this:</p>
<pre><code class="lang-auto">wireSequenceNode = slicer.util.getNode('boxToProbe-boxToProbe-Seq')
        browserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(wireSequenceNode)
        browserNode.SetSelectedItemNumber(0)

        originalPoints = slicer.util.getNode('trackLine')
        shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
        originalID = shNode.GetItemByDataNode(originalPoints)

        print('START\n')

        for count in range(wireSequenceNode.GetNumberOfDataNodes()):  # Loops 22 times
            browserNode.SetSelectedItemNumber(count)  # Moves to next sequence

            # Creates a copy of the original untransformed line points
            clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, originalID)
            clonedNode = shNode.GetItemDataNode(clonedItemID)

            # Gets the current sequence's unique 'PlatformToMarker2' transform values
            currentPTMNode = slicer.util.getNode('PlatformToMarker2')
            currentTrackNode = slicer.util.getNode('Marker2ToTracker')

            #copyArray = slicer.util.arrayFromMarkupsControlPoints(originalPoints)
            platformVTK = currentPTMNode.GetMatrixTransformFromParent()
            trackerVTK = currentTrackNode.GetMatrixTransformFromParent()

            print("ITERATION:", count+1, "\n")
            print("TRANSFORM PTM:", platformVTK, "\n")
            print("TRANSFORM TRACK:", trackerVTK, "\n")
            print("POINTS:", slicer.util.arrayFromMarkupsControlPoints(clonedNode), "\n")
            clonedNode.ApplyTransformMatrix(platformVTK)
            clonedNode.ApplyTransformMatrix(trackerVTK)
            
            print("PTS TRANSFORMED:", slicer.util.arrayFromMarkupsControlPoints(clonedNode), "\n")
            #copyPoints.SetAndObserveTransformNodeID(currentTransformNode.GetID())

            #print(slicer.util.arrayFromMarkupsControlPoints(copyPoints))
            #print(slicer.util.arrayFromTransformMatrix(currentTransformNode))

        print('FINISH\n')
</code></pre>
<p>I might also try finding some code to harden/unharden the markup list and then just reuse a copy of the original points at each new sequence.</p>
<p>Thanks,<br>
Chris</p>

---

## Post #4 by @lassoan (2022-08-22 22:50 UTC)

<p>Yes, you need a script for this, as there is no module offered for this yet.</p>
<p>Your script looks quite good and it could be actually quite easily generalized so that it works for any node and transform (for each time point in the sequence, clone the transformed node and apply and harden the transform). The script could then be added to a Python scripted module so that it can be used with a convenient GUI. Let us know if you would be interested to contribute this (maybe in the <a href="https://github.com/PerkLab/SlicerSandbox/">Sandbox extension</a>).</p>

---

## Post #6 by @ChristophG123 (2022-08-23 22:01 UTC)

<p>So when I tried to clone and harden the “trackLine” markup list, it just gave me the original untransformed positions. Is it possible to copy the markup list with the points already transformed? I know I can manually harden the original point at the start (as I spoke about earlier), which I’ll use as a starting point. The code looks like this:</p>
<pre><code class="lang-auto">originListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "originList")
        directionListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "directionList")

        print('START\n')
        #wireSequenceNode.GetNumberOfDataNodes()
        for count in range(1):  # Loops 22 times
            # Moves to current sequence
            browserNode.SetSelectedItemNumber(count)
            # Get the sequence's current transformed node
            currentNode = slicer.util.getNode('trackLine')

            # Clone the sequence's current transformed node
            shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
            itemIDToClone = shNode.GetItemByDataNode(currentNode)
            clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
            clonedNode = shNode.GetItemDataNode(clonedItemID)

            # Harden the clone and copy its points onto each markup list
            clonedNode.HardenTransform()
            print(slicer.util.arrayFromMarkupsControlPoints(clonedNode))
</code></pre>
<p>UPDATE:<br>
Yes, when I just harden the currentNode, it does print the correct positions the first time. But after that, it just gives incorrect values again like I explained earlier. Perhaps I can undo a Harden but maintain the original position using some commands?</p>
<pre><code class="lang-auto">START

[[ -36.5066296  -175.44519425  162.36295889]
 [ -16.77793346 -159.36146699  -48.94167894]]
[[1143.41438904 -764.82269612  -14.8033893 ]
 [ 950.82061968 -674.30338919  -18.18966374]]
[[  217.3803255    -94.13977669 -1729.84833624]
 [  329.31301792  -126.13236205 -1551.67673178]]
FINISH


</code></pre>

---

## Post #7 by @lassoan (2022-08-24 03:24 UTC)

<p>You can find examples for all commonly used operations, including how to harden a transform on a node, in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-nodes-warped-by-transform-sequence">script repository</a>.</p>

---

## Post #8 by @ChristophG123 (2022-08-24 05:26 UTC)

<p>Excellent, I got it working. I’m sure this could be generalized and put into one of your Extensions, as you mentioned. And yes, I would be interested in doing this. The code is here:</p>
<pre><code class="lang-auto">transformSequenceNode = slicer.util.getNode("PlatformToMarker2")
        originalListNode = slicer.util.getNode('trackLine')

        wireSequenceNode = slicer.util.getNode('boxToProbe-boxToProbe-Seq')
        browserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(wireSequenceNode)
        browserNode.SetSelectedItemNumber(0)

        print('START\n')
        print("Unhardened Original Points:", slicer.util.arrayFromMarkupsControlPoints(originalListNode))

        #wireSequenceNode.GetNumberOfDataNodes()
        for index in range(3):
            # Moves sequence browser to the current sequence
            browserNode.SetSelectedItemNumber(index)

            # Obtain the current sequence's unique "PlatformToMarker2" transform values
            currentTransform = wireSequenceNode.GetNthDataNode(index).GetTransformToParent()

            # Clone the original markup list node
            shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
            itemIDToClone = shNode.GetItemByDataNode(originalListNode)
            clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
            clonedNode = shNode.GetItemDataNode(clonedItemID)
            clonedNode.ApplyTransform(currentTransform)
            clonedNode.HardenTransform()
            print("Hardened Clone Point ", index, ":\n", slicer.util.arrayFromMarkupsControlPoints(clonedNode), "\n")

            # Removing the cloned node since it is no longer needed.
            slicer.mrmlScene.RemoveNode(clonedNode)
</code></pre>
<p>Output:</p>
<pre><code class="lang-auto">START

Unhardened Original Points: [[ -101.747   -27.208 -1134.565]
 [  111.037   -24.332 -1138.072]]
Hardened Clone Point  0 :
 [[ -36.5066296  -175.44519425  162.36295889]
 [ -16.77793346 -159.36146699  -48.94167894]] 

Hardened Clone Point  1 :
 [[  -7.30387223 -167.37110704  149.97626905]
 [ -25.2482563  -158.40310593  -61.90847158]] 

Hardened Clone Point  2 :
 [[  54.83111357 -251.74909748   85.94484956]
 [ -49.3164436  -131.60420018  -55.53333947]] 

FINISH
</code></pre>
<p>I just iterated 3 times for testing, but the line commented above the for loop allows you to loop through the entire sequence.</p>

---
