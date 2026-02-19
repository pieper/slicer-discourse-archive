---
topic_id: 8127
title: "Rotate Reformat Slice View In Plane"
date: 2019-08-21
url: https://discourse.slicer.org/t/8127
---

# Rotate reformat slice view (in plane)

**Topic ID**: 8127
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/rotate-reformat-slice-view-in-plane/8127

---

## Post #1 by @mikebind (2019-08-21 19:07 UTC)

<p>I am working on adding some slice views in addition to the standard multiplanar views.  For stereo EEG procedures for epilepsy patients, linear electrodes are inserted into the patient’s skull.  The additional reformat views I want to generate are 1) a plane which contains a selected linear electrode and 2) a plane orthogonal to the linear electrode. I have the RAS vector along the electrode, and have used the logic from the Reformat module to set the view slice normals as follows:</p>
<pre><code>targetPos  # contains the RAS location I want the views to contain
gridVector # contains the vector along the linear electrode 
normalVect # contains a vector perpendicular to the electrode grid

parallelSliceNode = getNode('Parallel')
orthoSliceNode = getNode('Orthogonal')
reformatLogic = slicer.modules.reformat.logic()

reformatLogic.SetSliceNormal(parallelSliceNode,normalVect[0],normalVect[1],normalVect[2])
parallelSliceNode.JumpSliceByOffsetting(targetPos[0],targetPos[1],targetPos[2])

reformatLogic.SetSliceNormal(orthoSliceNode,gridVector[0],gridVector[1],gridVector[2])
orthoSliceNode.JumpSliceByCentering(targetPos[0],targetPos[1],targetPos[2])
</code></pre>
<p>This works perfectly for setting the slice view normal vector and setting the offset to contain the point I want.  However, I don’t see how to control the rotation about that normal vector.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20eada6216633ed46bac5b22fd5b22926fa73603.jpeg" data-download-href="/uploads/short-url/4HcrRxIXPqlhnpaCEN2Vrv9tlDR.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20eada6216633ed46bac5b22fd5b22926fa73603_2_690x430.jpeg" alt="Screenshot" data-base62-sha1="4HcrRxIXPqlhnpaCEN2Vrv9tlDR" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20eada6216633ed46bac5b22fd5b22926fa73603_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20eada6216633ed46bac5b22fd5b22926fa73603_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20eada6216633ed46bac5b22fd5b22926fa73603_2_1380x860.jpeg 2x" data-dominant-color="3E3F45"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">4888×3052 1.88 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The lower left and lower center slices are the “Parallel” and “Orthogonal” slice views I have created.  The “Parallel” one is fine, but the “Orthogonal” one is rotated in an odd way (note the orientation cube in the lower right).  I imagine this is because of the way the rotation to the requested normal vector was carried out, and I understand that simply saying I want the slice normal to be a particular vector is not enough to specify how I want the view to be oriented once that normal is achieved. Ideally, for this view, I would like vertical image axis to correspond as closely as possible to the IS axis and the horizontal image axis to correspond as closely as possible to the AP axis.  Any suggestions as to how to achieve this for this example?</p>
<p>Also, these electrodes can be oriented essentially arbitrarily within the skull, and I would like to figure out a way to automatically have the rotation be as sensible as possible (i.e. if the desired normal is approximately the same as normal to axial, then orient the plane roughly like axial, and if the normal is approximately the same as normal to sagittal, then orient the plane roughly like sagittal, etc), so if there are suggestions for this I would greatly appreciate that as well. Thanks!</p>

---

## Post #2 by @pieper (2019-08-22 14:25 UTC)

<p>Hi -</p>
<p>This looks really close - it shouldn’t be hard to do what you need.  If you look at <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/Logic/vtkSlicerReformatLogic.cxx#L96-L146" rel="nofollow noopener">the implementation of SetSliceNormal</a> you can see that’ it’s just applying a transformation to the slice node’s SliceToRAS matrix, which defines the patient space (RAS) of the slicing plane.  You can define all the rotations to meet your needs.  The defaults <a href="https://github.com/Slicer/Slicer/blob/ec4a9ddef43b99a1b8ef0726355eb9bbb98815b1/Libs/MRML/Core/vtkMRMLSliceNode.cxx#L519-L571" rel="nofollow noopener">are here</a>.</p>

---

## Post #3 by @lassoan (2019-08-22 15:57 UTC)

<p>Orienting reformatted views in a “sensible” way is a common issue. A solution is to define a preferred <em>anatomical up</em> direction and snap the <em>view up</em> direction to this anatomical direction. For cases when slice normal is too close to the <em>anatomical up</em> direction, then the <em>view right</em> axis has to be aligned with an <em>anatomical right</em> direction.</p>
<p>The limitation of this approach is that there is a sudden “jump” when flipping between alignment between up/right direction, which may be confusing, but seeing these highly oblique views are quite confusing for clinicians anyway, so in general it is tolerable.</p>
<p>A complete implementation is available in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_a_normal_vector_and_position" rel="nofollow noopener">script repository</a>.</p>

---

## Post #4 by @mikebind (2019-08-22 17:31 UTC)

<p>Thanks, I am getting closer. I’ll post what I end up with here once I get it. The implementation in SetSliceNormal is helpful.  I think I now understand what the rotation code in SetSliceNormal is doing.</p>
<p>Here is my current understanding:</p>
<ul>
<li>Get the current slice normal (before rotation), which can be found as the 3rd column of the current sliceToRAS matrix, and puts it into the variable <code>nodeNormal</code>.</li>
<li>Find the cross product between nodeNormal and the desired new normal vector (stored in the variable <code>normal</code>)</li>
<li>Find the angle between the the two vectors as the acos of the dot product.  (Both vectors are unit vectors at this point, so there is no need to normalize by length)</li>
<li>Create a vtk Transform and initialize it with the current sliceToRAS matrix</li>
<li>Use the transform’s RotateWXYZ to rotate around the cross product vector by the angle found.  This should be the most direct rotation between the the two normal vectors (the current one and the new one)</li>
<li>Put the rotated matrix back in sliceToRAS and call the node’s UpdateMatrices() function to trigger the actual update of the view</li>
</ul>

---

## Post #5 by @mikebind (2019-08-22 17:35 UTC)

<p>Thanks, that looks like exactly what I need. If it works for me I’ll come back and mark this as the solution.</p>

---

## Post #6 by @mikebind (2019-08-23 23:02 UTC)

<p>Here is what ended up working for me:</p>
<p><code>def setSlicePoseFromSliceNormalAndPosition(sliceNode, sliceNormal, slicePosition, offsetOrCenter='offset'):</code></p>
<blockquote>
<pre><code>"""
Set slice pose from the provided plane normal and position. The most similar canonical view (sagittal, coronal, 
or axial) is determined by the direction of the sliceNormal.  For example, if the largest component of the 
sliceNormal is in the superior direction (or negative superior direction), then the most similar canonical view
is the axial view. Care is taken to not allow misleading views, such as an axial-appearing view which has the 
patient's right on the right hand side (reversed from the standard axial view). If the supplied normal would 
naturally lead to such a misleading view, it is negated. 
:param offsetOrCenter should be either 'offset' or 'center', and is used to determine whether the view should 
be shifed to the given slicePosition by jumping by offsetting or by centering (using sliceNode.JumpSlicesByOffsetting
or sliceNode.JumpSlicesByCentering, respectively).   
"""
</code></pre>
</blockquote>
<pre><code># Ensure sliceNormal is numpy array
sliceNormal = np.array(sliceNormal)

# Find largest and smallest components of sliceNormal
largestComponentAxis = np.argmax(np.abs(sliceNormal)) # used to determine most similar view
smallestComponentAxis = np.argmin(np.abs(sliceNormal)) # used to decide which of the slice X or Y axes to precisely align

if largestComponentAxis==smallestComponentAxis:
    raise ValueError('Largest and smallest slice normal components are the same!!')

viewLookup = {0: 'sagittal',
         1: 'coronal',
         2: 'axial'}

mostSimilarView = viewLookup[largestComponentAxis]
#print mostSimilarView
    
# In order to make the adjusted view as similar as possible to a standard view, it may be necessary to use
# the negation of the given slice normal rather than the given slice normal.  

# The cross product relationships among the 3 axes are
# Y = NxX, X = YxN, N = XxY  (where x means vector cross product here, recall that order matters)

# In each of the mostSimilarView cases which follow, we 
# 1) use the sign of the largest component to determine whether the sliceNormal needs to be negated 
#    to more closely conform to the corresponding canonical view, 
# 2) use the smallest component to determine which of the remaining axes is closer to lying in the new slice view 
#    plane. The smaller the component in the direction of the sliceNormal, the larger the component must be in 
#    the orthogonal plane.
# 3) set the direction of the slice X axis so that the projection of the most in-plane of the R,A, or S axes 
#    points precisely in the correct direction. If it is the new Y axis which is to be aligned, the X axis direction
#    is determined by finding the cross product of the Y axis with the sliceNormal. 
# 
# Note that we can handle the normalization to unit vectors later, so if we want the slice Y axis to align as closely
# as possible to the Superior axis, we can assign sliceAxisY to be [0,0,1] for now, even if the sliceNormal guarantees
# that the vector [0,0,1] is not in the slice plane. After the cross products and normalization, the sliceAxisY

if mostSimilarView=='sagittal':
    # Canonical view is image up is superior, image right is posterior, and patient right points out of screen
    if sliceNormal[largestComponentAxis]&gt;0:
        sliceNormal = -sliceNormal # invert the normal if it would lead the Right axis to point into the screen
    if smallestComponentAxis==2:
        # if superior is closest to in-plane, say that up should be superior
        sliceAxisY = [0,0,1]
        sliceAxisX = np.cross(sliceAxisY,sliceNormal)
        #print 'up should be superior'
    elif smallestComponentAxis==1:
        # if right is closest to in-plane, say that right should be posterior
        sliceAxisX = [0,-1,0]
        #print 'right should be posterior'
    
elif mostSimilarView=='coronal':
    # Canonical view is image up is superior, image right is patient left, and anterior points into the screen
    if sliceNormal[largestComponentAxis]&lt;0:
        sliceNormal = -sliceNormal # invert the normal if it would lead the anterior axis to point out of the screen        
    if smallestComponentAxis==2:
        # if superior is closest to in-plane, say that up should be superior
        sliceAxisY = [0,0,1]
        sliceAxisX = np.cross(sliceAxisY,sliceNormal)
        #print('up should be superior')
    elif smallestComponentAxis==0:
        # if right is closest to in-plane, say that right should be left
        sliceAxisX = [-1,0,0]
        print 'right should be patient left'
    
elif mostSimilarView=='axial':
    # Canonical view is image up is anterior and image right is left
    if sliceNormal[largestComponentAxis]&gt;0:
        sliceNormal=-sliceNormal # invert the normal if it would lead the Superior axis to point into the screen        
    if smallestComponentAxis==1:
        # if anterior is closest to in-plane, say that up should be anterior
        sliceAxisY = [0,1,0]
        sliceAxisX = np.cross(sliceAxisY,sliceNormal)
        print 'up should be anterior'+' sliceAxisX='+str(sliceAxisX)
    elif smallestComponentAxis==0:
        # if right is closest to in-plane, say that right should be left
        sliceAxisX = [-1,0,0]
        print 'right should be patient left'+' sliceAxisX='+str(sliceAxisX)
    
else:
    # Should throw error here
    raise ValueError('mostSimilarView must be axial, coronal, or sagittal, but is "'+mostSimilarView+'"')


vtkSliceToRAS = sliceNode.GetSliceToRAS()
oldPosition = [vtkSliceToRAS.GetElement(0,3),
               vtkSliceToRAS.GetElement(1,3),
               vtkSliceToRAS.GetElement(2,3)]

# In the new SliceToRAS matrix, sliceAxisX should be the first column, sliceAxisY should be the second column, 
# and the normal vector should be the third colum (sliceAxisZ).  These should all be normalized and orthogonal.

# SetSliceToRASByNTP handles this by 1) normalizing the input N and T vectors (slice normal and sliceAxisX),
# 2) crossing them to generate sliceAxisY, and then 3) crossing the slice normal and sliceAxisY to generate
# an updated version of sliceAxisX which is guaranteed to be orthogonal to both sliceAxisY and the slice normal. 

sliceNormal = np.array(sliceNormal)
magNormal = np.linalg.norm(sliceNormal)
sliceNormal = sliceNormal/magNormal # normalize

sliceAxisX = np.array(sliceAxisX)
magSliceAxisX = np.linalg.norm(sliceAxisX)
sliceAxisX = sliceAxisX/magSliceAxisX

sliceAxisY = np.cross(sliceNormal,sliceAxisX) # Y = NxX (recall that order matters for cross products)
magSliceAxisY = np.linalg.norm(sliceAxisY)
sliceAxisY = sliceAxisY/magSliceAxisY # normalize

sliceAxisX = np.cross(sliceAxisY,sliceNormal) # X = YxN (this order ensures X points in the same general direction as the original X, but is guaranteed to be orthogonal)
magSliceAxisX = np.linalg.norm(sliceAxisX)

# Set the elements of the SliceToRAS matrix
for rowInd in range(3):
    vtkSliceToRAS.SetElement(rowInd,0,sliceAxisX[rowInd])
    vtkSliceToRAS.SetElement(rowInd,1,sliceAxisY[rowInd])
    vtkSliceToRAS.SetElement(rowInd,2,sliceNormal[rowInd])
    if offsetOrCenter.lower()=='center':
        # use the requested position as the slice center position
        vtkSliceToRAS.SetElement(rowInd,3,slicePosition[rowInd])
        

sliceNode.UpdateMatrices() # This applies the changes to the SliceToRAS matrix

if offsetOrCenter.lower()=='offset':
    # keep the original slice center position, but then adjust offset until it contains requested position
    sliceNode.JumpSliceByOffsetting(slicePosition[0],slicePosition[1],slicePosition[2])
elif offsetOrCenter.lower()=='center':
    sliceNode.JumpSliceByCentering(slicePosition[0],slicePosition[1],slicePosition[2]) [/code]
</code></pre>

---
