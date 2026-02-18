# Change size and color of markups fiducials

**Topic ID**: 14063
**Date**: 2020-10-15
**URL**: https://discourse.slicer.org/t/change-size-and-color-of-markups-fiducials/14063

---

## Post #1 by @jj31 (2020-10-15 22:11 UTC)

<p>I’m loading a list of fiducials programmatically using:<br>
slicer.util.loadMarkupsFiducialList(file.fcsv)</p>
<p>Then, I’m trying to change their color and size using the following:</p>
<p>defaultMarkupsFiducialDisplayNode = slicer.vtkMRMLMarkupsFiducialDisplayNode()<br>
defaultMarkupsFiducialDisplayNode.SetColor(255,255,255) <span class="hashtag">#Color</span> of fiducials on simulation slice<br>
defaultMarkupsFiducialDisplayNode.SetGlyphScale(1.5)<br>
slicer.mrmlScene.AddDefaultNode(defaultMarkupsFiducialDisplayNode)</p>
<p>But it doesn’t work. Any ideas on why is not working?<br>
Thanks,</p>
<p>JJ</p>

---

## Post #2 by @lassoan (2020-10-15 23:39 UTC)

<p><code>AddDefaultNode</code> changes the default for new nodes. If you want to change it for a specific node then modify the display node of that particular markups node:</p>
<pre><code class="lang-python">markupsNode = slicer.util.loadMarkupsFiducialList('file.fcsv')
markupsNode.GetDisplayNode().SetSelectedColor(0.3, 0.6, 0.1)
</code></pre>
<p>Alternatively, you can save your markups in a json file (<code>something.mrk.json</code>) and define both point positions and display properties in this file:</p>
<pre><code class="lang-json">{
    "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json#",
    "markups": [
        {
            "type": "Fiducial",
            "coordinateSystem": "LPS",
            "controlPoints": [
                { "label": "F-1", "position": [-53.388409961685827, -73.33572796934868, 0.0] },
                { "label": "F-2", "position": [49.8682950191571, -88.58955938697324, 0.0] },
                { "label": "F-3", "position": [-25.22749042145594, 59.255268199233729, 0.0] }
            ],
            "display": {
                "color": [0.4, 1.0, 1.0],
                "selectedColor": [1.0, 0.2196078431372549, 0.9215686274509803],
                "glyphType": "Sphere3D",
                "glyphScale": 16.2,
                "useGlyphScale": true
            }
        }
    ]
}
</code></pre>

---
