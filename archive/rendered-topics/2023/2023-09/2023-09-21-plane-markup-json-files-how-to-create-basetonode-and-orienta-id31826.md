---
topic_id: 31826
title: "Plane Markup Json Files How To Create Basetonode And Orienta"
date: 2023-09-21
url: https://discourse.slicer.org/t/31826
---

# Plane markup json files - how to create "baseToNode" and "orientation" matrices

**Topic ID**: 31826
**Date**: 2023-09-21
**URL**: https://discourse.slicer.org/t/plane-markup-json-files-how-to-create-basetonode-and-orientation-matrices/31826

---

## Post #1 by @drobny (2023-09-21 14:08 UTC)

<p>Hi,<br>
I’m looking into using slicer for the visualisation of results from another tool. Therefore, I’d like to import plane definitions to quickly inspect whether they are as expected.<br>
I use a point and normal vector in world coordinates. I keep the rest of a slicer generated json file as template while replacing “center” and “normal”.<br>
The “objectToBase” matrix seems straight forward enough the conversion between the image orientation to the default LPS orientation of the markups.<br>
But it’s not immediately clear how the “baseToNode” and “orientation” matrices are defined and I can’t find a reference. I hoped I could omit those in the definition as the point and normal should be sufficient for defining a plane (to my needs). This does not seem to be the case so I assume I will have to calculate the matrices to make Slicer read my file.</p>
<p>Could someone point me to a resource of how these should behave or how they would be calculated based on the point and normal vector? Much appreciated!</p>

---

## Post #2 by @lassoan (2023-09-22 02:58 UTC)

<p>Definition of these coordinate systems are <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsPlaneNode.h">here</a>.</p>
<p>If you specify a plane by a single point (<code>"planeType": "pointNormal"</code>) then you only need to specify:</p>
<ul>
<li>plane position: position of the one and only control point</li>
<li>plane orientation: <code>baseToNode</code> matrix. Note that a plane in mathematical sense is specified by a position and a normal, but if you want to display a plane then you need to specify its rotation around that normal. <code>baseToNode</code> contains the two axis of the plane and the plane normal. If you don’t care about the rotation then you can choose an arbitrary orientation and use cross product with the normal vector to make it orthogonal to the normal vector. Translation component of <code>baseToNode</code> matrix is ignored (because position is set by the control point), so it can be set to <code>0.0, 0.0, 0.0</code>.</li>
<li>plane bounds: specifies how far the plane extends in 4 directions (-x, +x, -y, +y) from the plane position</li>
</ul>
<p>Example:</p>
<pre><code class="lang-auto">{
    "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json#",
    "markups": [
        {
            "type": "Plane", "coordinateSystem": "LPS", "planeType": "pointNormal",
            "baseToNode": [
                -0.7177763971220261, -0.48438183588553957, -0.5001712514716112, 0.0,
                0.3974111999339178, -0.8748566951587867, 0.2769297764830091, 0.0,
                -0.5717179216201003, -1.1102230246251565e-16, 0.820450253274623, 0.0,
                0.0, 0.0, 0.0, 1.0],
            "planeBounds": [-50.0, 50.0, -50.0, 50.0],
            "controlPoints": [{ "position": [60.6068749511193, -26.833897399804197, -175.25000000000006] }],
            "display": { "visibility": true, "opacity": 1.0, "color": [0.4, 1.0, 1.0] }
       }
    ]
}</code></pre>

---

## Post #3 by @angolin22_fan (2024-01-31 11:44 UTC)

<p>Dear teacher,<br>
Hello, Thanks for your excellent work!<br>
I have a question, If I know the plane center(c1,c2,c3) and normal(n1,n2,n3), How can I calculate the ‘baseToNode’?</p>

---

## Post #4 by @phiro753 (2024-05-02 05:56 UTC)

<p>Hi team,</p>
<p>I seem to be struggling with the same issue coming to the end of my PhD on Sarcoma. (I have worked across disciplines to propose a method for bone histology registration because bone can be a little tricky… We are aiming to enable similar correlation to prostate research, <a href="https://github.com/pimed/Slicer-RadPathFusion" rel="noopener nofollow ugc">Mirabela and PIMed</a>).</p>
<p>I can get the planes for histology initalisaiton in python working, but these are only specified by a centre and normal… The baseToNode seems to be giving similar issues to this thread when I try import jsons to Slicer… Mind expanding on your comments about circumventing baseToNormal above Andras?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e20ddae7c399a1b95e135ced722a693fad3131ab.png" data-download-href="/uploads/short-url/wfLAKt7CE9B21shEqFWZ1KIpqGv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e20ddae7c399a1b95e135ced722a693fad3131ab_2_690x371.png" alt="image" data-base62-sha1="wfLAKt7CE9B21shEqFWZ1KIpqGv" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e20ddae7c399a1b95e135ced722a693fad3131ab_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e20ddae7c399a1b95e135ced722a693fad3131ab_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e20ddae7c399a1b95e135ced722a693fad3131ab_2_1380x742.png 2x" data-dominant-color="7E8188"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×1030 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @phiro753 (2024-05-29 03:13 UTC)

<p>I missed posting this a little while ago. To wrap my problem up I managed to cobble something together that seemed to work for my issue… A wee function for calculating the baseToNode array:</p>
<pre><code class="lang-auto">def CalcBase2Node(self):
    '''Calculating the baseToNode matrix for .JSON import into Slicer'''
    # Normalize the plane normal vector
    self.normal /= np.linalg.norm(self.normal)

    # Choose an arbitrary vector not parallel to the self.normal (e.g., x-axis)
    arbitrary_vector = np.array([1, 0, 0])

    # Calculate a third axis of the plane coordinate system
    third_axis = np.cross(self.normal, arbitrary_vector)
    third_axis /= np.linalg.norm(third_axis)

    # Calculate the second axis of the plane coordinate system
    second_axis = np.cross(self.normal, third_axis)
    second_axis /= np.linalg.norm(second_axis)

    # Construct the rotation-translation matrix baseToNode
    base_to_node_matrix = np.eye(4)
    base_to_node_matrix[:3, 0] = third_axis
    base_to_node_matrix[:3, 1] = second_axis
    base_to_node_matrix[:3, 2] = self.normal
    base_to_node_matrix[:3, 3] = self.centre

    return base_to_node_matrix
</code></pre>
<p>This feeds a seraliser and produces .json files which import well into Slicer now.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ccc1333e200f714da319b608e0f9625b8e29bb1.png" data-download-href="/uploads/short-url/hO0qYfB5O3IPRNNk0CmV7dgJYY1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ccc1333e200f714da319b608e0f9625b8e29bb1_2_690x416.png" alt="image" data-base62-sha1="hO0qYfB5O3IPRNNk0CmV7dgJYY1" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ccc1333e200f714da319b608e0f9625b8e29bb1_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ccc1333e200f714da319b608e0f9625b8e29bb1_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7ccc1333e200f714da319b608e0f9625b8e29bb1_2_1380x832.png 2x" data-dominant-color="8A8795"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1156 444 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
