# Problems replicating an exported sequence

**Topic ID**: 29727
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/problems-replicating-an-exported-sequence/29727

---

## Post #1 by @abravo (2023-05-30 15:10 UTC)

<p>Hello everyone,</p>
<p>I have been trying to use the coordinates of some exported sequences from Slicer to replicate the movements in Blender for demonstration/learning purposes. These sequences have been recorded with slicer using an electromagnetic tracking system.<br>
I have tried both the solution from this post (<a href="https://discourse.slicer.org/t/exporting-transformations-from-sequence-in-3d-slicer/28868" class="inline-onebox">Exporting Transformations from Sequence in 3D Slicer</a>) and parsing the *.seq.mha files directly, obtaining the same coordinates (so I guess I am looking at the correct data).</p>
<p>However, I have hit a snag trying to replicate the same scene outside Slicer. When importing the models to Blender, I import the sequence by creating a keyframe for each transform that has been exported. Doing it this way, I can’t manage to replicate the same movements in Blender at all. Everything moves erratically, even if the starting positions of the elements coincide between Slicer and the scene in Blender.</p>
<p>It looks like there is some kind of transform hierarchy among the models in Slicer’s scene that is affecting the coordinates (so some of them are relative to other models and not to the “world”, I assume?). Is there any way to check if this is what is happening (I am not an experienced Slicer user) and/or export the coordinates being relative to the world instead to other models? Maybe exporting the models somehow according to how they have been defined in Slicer (pivot points, dependencies, etc.) or something like that.</p>
<p>I have also tried to connect slicer to Unity directly for troubleshooting using OpenIGTLink, and I get the same problem. Can somebody guide me on how to debug this?</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2023-05-30 19:47 UTC)

<p>Sequence metafiles contain transforms that you may indeed need to concatenate (multiply and invert as needed) to get a transform from a specific coordinate system to ananother.</p>
<p>For example, you can compute the <code>ProbeModelToReference</code> transform as <code>inv(ReferenceToTracker) * ProbeToTracker * ProbeModelToProbe</code>. <code>ProbeModelToProbe</code> is the transformation between the coordinate system of the surface mesh and the coordinate system of the tracking marker attached to the probe.</p>
<p>If you already have a transform tree in Slicer that works well then that already tells you how which transforms you need to concatenate and how.</p>

---

## Post #3 by @abravo (2023-06-02 16:35 UTC)

<p>Hello Andras.</p>
<p>Thank you for your prompt reply. I have been doing some tests trying to undo the coordinate conversion multiplying by the inverted matrix. Let me explain if I am understanding this right.</p>
<p>According to Slicer’s Transform hierarchy, in the Data module, I have the following structure:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa937548a49575aae267b7e9e96cf01549626dd3.png" alt="transform_hierarchy" data-base62-sha1="zKHiiP4I2BOWIlMWuo807hi805t" width="377" height="438"><br>
Both “BabyBodyToTracker” and “BabyBodyModelToBabyBody” are LinearTransform, while “BabyBodyModel” is a Model.</p>
<p>I am taking the Transform Matrix of each frame coming from the “BabyBodyToTracker” associated sequence and multiplying that by the inverse of the “BabyBodyModelToBabyBody”, which is a fixed coordinate throughout the sequence. However, I am not getting the desired results.<br>
Basically, all I’m doing is: FinalTransform = inv(BabyBodyModelToBabyBody) * BabyBodyToTracker</p>
<p>I don’t know if I am doing something wrong in the conversion of if the erratic animation can be due to the models having different pivot points in Slicer vs other programs. I have exported them directly from Slicer as *.obj and the scene is arranged logically from the start, having all models share a common pivot point.</p>
<p>Could it also be how the rotations are being converted in my script? I get the first 3x3 elements, which if I am not mistaken constitute the rotation and I am applying the following function to convert them to euler angles usable in Blender (Z is up):</p>
<pre><code class="lang-auto">def rotation_angles(matrix, order):
    """
    input
        matrix = 3x3 rotation matrix (numpy array)
        order(str) = rotation order of x, y, z : e.g, rotation XZY -- 'xzy'
    output
        theta1, theta2, theta3 = rotation angles in rotation order
    """
    r11, r12, r13 = matrix[0]
    r21, r22, r23 = matrix[1]
    r31, r32, r33 = matrix[2]
.
.
.
    elif order == 'xyz':
        theta1 = np.arctan(-r23 / r33)
        theta2 = np.arctan(r13 * np.cos(theta1) / r33)
        theta3 = np.arctan(-r12 / r11)

    theta1 = theta1 * 180 / np.pi
    theta2 = theta2 * 180 / np.pi
    theta3 = theta3 * 180 / np.pi

    return (theta1, theta2, theta3)
</code></pre>
<p>Thank you for your attention.</p>

---
