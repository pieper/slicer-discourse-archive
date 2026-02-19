---
topic_id: 24894
title: "Cant Access Markupfiduciallist Control Points"
date: 2022-08-23
url: https://discourse.slicer.org/t/24894
---

# Can't access MarkupFiducialList control points

**Topic ID**: 24894
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/cant-access-markupfiduciallist-control-points/24894

---

## Post #1 by @ChristophG123 (2022-08-23 20:00 UTC)

<p>Slicer Version: 5.1.0-2022-07-17<br>
OS: Windows 10</p>
<p>Hi,<br>
I’m not sure why, but when I try accessing control points from my MarkupFiducialList, it says it doesn’t have the attribute “GetNthControlPoint”.<br>
What I’m trying to do is loop through several sequences and add a new control point onto the list “originListNode” for each iteration. The initial values of these “origin” points are the same every time, but are transformed within the loop. So basically, I want to have one list of markups with unique positions using each sequence’s unique “platformVTK” and “trackerVTk” transform values:</p>
<pre><code class="lang-auto">originalPoints = slicer.util.getNode('trackLine')
        originalArray = slicer.util.arrayFromMarkupsControlPoints(originalPoints)
        originListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "originList")
        directionListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "directionList")

        print('START\n')
        #wireSequenceNode.GetNumberOfDataNodes()
        for count in range(3):  # Loops 22 times
            browserNode.SetSelectedItemNumber(count)  # Moves to next sequence


            # Gets the current sequence's unique 'PlatformToMarker2' transform values
            currentPTMNode = slicer.util.getNode('PlatformToMarker2')
            currentTrackNode = slicer.util.getNode('Marker2ToTracker')

            # copyArray = slicer.util.arrayFromMarkupsControlPoints(originalPoints)
            platformVTK = currentPTMNode.GetMatrixTransformFromParent().Invert()
            trackerVTK = currentTrackNode.GetMatrixTransformFromParent()

            # The current origin point added to the list is originally just "bigHole" from the originalPoints list
            newOriginIndex = originListNode.AddControlPoint([originalArray[0][0], originalArray[0][1], originalArray[0][2]])
            newOrigin = originListNode.GetNthControlPoint(newOriginIndex)
            originListNode.SetNthControlPointLabel(newOriginIndex, "origin" + str(count))

            # Applying the current transforms onto the origin
            transformedOrigin = newOrigin.ApplyTransformMatrix(platformVTK)
            transformedOrigin = transformedOrigin.ApplyTransformMatrix(trackerVTK)

            print(transformedOrigin)
</code></pre>
<p>I am able to create the list node “originListNode” (named “originList” on Slicer) and add points using “AddControlPoint”. This is outputted successfully on Slicer. I can also access each control point’s position using originListNode.GetNthControlPointPosition(newOriginIndex). But when I try accessing these control point objects in “originList” using “GetNthControlPoint(newOriginIndex)”, it says it is not an attribute of the MarkupsFiducial node:</p>
<pre><code class="lang-auto">File "C:/d/ClariusTracker/calibrationClarius/Procrustean_PTLR/PTL_Registration/PTL_Registration.py", line 259, in setup
    newOrigin = originListNode.GetNthControlPoint(newOriginIndex)
AttributeError: 'vtkSlicerMarkupsModuleMRML.vtkMRMLMarkupsFiducialN' object has no attribute 'GetNthControlPoint'
</code></pre>
<p>On the Slicer documentation it says this is a command that exists, but it doesn’t seem to work:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html</a></p>
<p>I was going to use Fiducial functions originally, but it seems they’ve been deprecated. I might also try this on a more stable version of Slicer. Also, this might just be an issue with inheritance because I’m not too familiar with Slicer classes.</p>

---

## Post #2 by @Sunderlandkyl (2022-08-23 20:20 UTC)

<p>The “ControlPoint” class is not wrapped in Python, so the method is not wrapped either.<br>
There should be functions in vtkMRMLMarkupsNode to access information on each control point from Python.</p>

---

## Post #3 by @ChristophG123 (2022-08-23 20:25 UTC)

<p>Hmm, ok. How would you recommend I Get each of these control points so I can transform them? Is there a way to convert each control point objects inside my originListNode to a transformable node? I know I could perform the transform on the entire originListNode, but that is not suited for my needs.</p>
<p>I’m not entirely sure what the ApplyTransformMatrix function does mathematically, but perhaps I might need to do this operation on each individual point with each individual transform (platformVTK, trackerVTk)?</p>

---

## Post #4 by @Sunderlandkyl (2022-08-23 20:32 UTC)

<p>You can use GetNthControlPointPosition (or GetNthControlPointPositionWorld), and transform them using the vtkMatrix4x4.</p>
<p>Something like:</p>
<pre><code class="lang-python">position = list(fiducialNode.GetNthControlPointPosition(0))
position.append(1.0) # Convert to a len 4 vector
matrix.MultiplyPoint(position)
</code></pre>

---

## Post #5 by @ChristophG123 (2022-08-23 21:15 UTC)

<p>Ok, that works. I wrote this little function if you think this is a feature that might be useful on slicer, but it’s up to you.</p>
<pre><code class="lang-auto">def ApplyTransformMatrixToControlPoint(vtkMRMLMarkupsFiducialNode pointListNode, int index, vtkMatrix4x4 transformMatrix):
        position = pointListNode.GetNthControlPointPosition(index)
        position.append(1.0)
        transformMatrix.MultiplyPoint(position)

        return position
</code></pre>
<p>The function didn’t work on my module, but I think I might’ve just written something wrong on the parameters. The code itself works on my module, though.</p>

---

## Post #6 by @ChristophG123 (2022-08-23 21:40 UTC)

<p>Hi Kyle, so I am able to get these transforms and apply them to each point. However, I’m having the same issue as <a href="https://discourse.slicer.org/t/unchanged-markup-position-and-sequences/24869">this topic</a> I posted yesterday, where it doesn’t actually calculate the correct transformed values that normally show up on each sequence. Any idea why this might be the case? The only transform that actually is applied to trackLine is PlatformToMarker2. And PlatformToMarker2 is linked with several other transforms. But I get positions that are way off for some reason.<br>
I might just write code to harden the transforms each time like I was planning on doing yesterday. It seems like the only solution. The reason I tried this was because I thought copying the original points every time was affecting the transforms in some way, but this code has proven that’s not really true.</p>

---
