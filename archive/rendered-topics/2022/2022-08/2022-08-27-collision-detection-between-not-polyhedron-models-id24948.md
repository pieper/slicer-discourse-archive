# Collision detection between not polyhedron models

**Topic ID**: 24948
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/collision-detection-between-not-polyhedron-models/24948

---

## Post #1 by @mosenco (2022-08-27 17:10 UTC)

<p>i’ve been following <a href="https://discourse.slicer.org/t/surface-intersection/19630/6">this</a> guide and implemented into my code and it doesnt work.</p>
<p>I have a white and pial file, from freesurfer that are models that represent the white and pial surface of the brain.</p>
<p>I have also multiple cylinder vtk aligned in some random direction that goes through the brain to represent the electrodes implanted into the patient’s brain.</p>
<p>My goal is to detect whenever the electrodes is inside the brain and detecting correctly the brain activities or outside the brain, so ignore anything that electrode is recording.<br>
So from the link provided at the beginning of the thread i’ve built this code</p>
<pre><code class="lang-auto">for i in range(0, len(listCylinderModel)):
            for j in range(0, len(listBrain)):
                collisionDetection = vtk.vtkCollisionDetectionFilter()
                collisionDetection.SetInputData(0, listCylinderModel[i].GetPolyData())
                collisionDetection.SetInputData(1, listBrain[j])
                matrix1 = vtk.vtkMatrix4x4()
                collisionDetection.SetMatrix(0, matrix1)
                collisionDetection.SetMatrix(1, matrix1)
                collisionDetection.SetBoxTolerance(0.0)
                collisionDetection.SetCellTolerance(0.0)
                collisionDetection.SetNumberOfCellsPerNode(100)

                collisionDetection.Update()

            if collisionDetection.GetNumberOfContacts() &gt; 0:
                print("collision detected")
                listCylinderDisplay[i].SetColor(1,1,1)
</code></pre>
<p>listcylinder are the list of the electrodes.<br>
listbrain are the list of the pial and white surfaces and there are only 4 elements there (left pial, left white, right pial, right white).<br>
So each cycle of the outer for take 1 electrodes and check if it collides with any of the 4 elements inside listbrain. If so, the selected electrodes, change its vtk color and update itself.</p>
<p>But it doesnt work. It detect nothing. I’ve read from the doc <a href="https://vtk.org/doc/nightly/html/classvtkCollisionDetectionFilter.html" rel="noopener nofollow ugc">here</a> that it detects collision only between two polyhedral surfaces. And if i recall correctly, a polyhedral surfaces it’s a surface where, given two random selected point inside the surface x and y, any points z in the direction of x,y and between x,y has to be inside the surface. so if i have a C shape model, that isn’t a polyhedron.</p>
<p>I tried the collision detection between two cylinder, and because a cylinder is a polyhedral surface, the code works.</p>
<p>But still, from the other post that i linked at the start of this thread, when that user was trying to detect a collision for a orthodontical procedure, the model of the teeth doesn’t seems a polyhedral surface.</p>
<p>So. What can you suggest me to do? I’ve search up again and found <a href="https://vtk.org/doc/nightly/html/classvtkOverlappingCellsDetector.html" rel="noopener nofollow ugc">this</a>, overlapping cell detector. But i have no idea how it works, and there isn’t any example or anything so far</p>

---

## Post #2 by @lassoan (2022-08-27 21:53 UTC)

<p>As far as I know, all FreeSurfer surfaces are triangle meshes (but you can run the meshes through a <code>vtkTriangleFilter</code> to ensure). Since triangle is a polyhedron (the simplest one), the <code>vtkCollisionDetectionFilter</code> should work well.</p>
<p>In your code the issue seems to be that you don’t set <code>matrix1</code> (you leave the default identity matrix, i.e., not transformed). I would not mess with the tolerance values and number of cells either - the defaults are generally a good choice. Instead, I would recommend to experiment with different <code>CollisionMode</code> choices and inspect all the outputs (cells and points in <code>ContactsOutput</code>, <code>ContactCells</code>, etc.).</p>
<p>If none of these help then you can share an example scene saved as a .mrb file (upload to dropbox/onedrive/etc. and post the link) and provide a script that you expect to work and we’ll have a look.</p>

---
