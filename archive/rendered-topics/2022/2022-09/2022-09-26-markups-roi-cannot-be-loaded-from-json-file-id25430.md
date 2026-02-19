---
topic_id: 25430
title: "Markups Roi Cannot Be Loaded From Json File"
date: 2022-09-26
url: https://discourse.slicer.org/t/25430
---

# Markups ROI cannot be loaded from JSON file

**Topic ID**: 25430
**Date**: 2022-09-26
**URL**: https://discourse.slicer.org/t/markups-roi-cannot-be-loaded-from-json-file/25430

---

## Post #1 by @WilliamDaniel (2022-09-26 02:13 UTC)

<p>System: WIN 10<br>
Slicer version: Slicer 5.0.3</p>
<p>Hi There,<br>
I’m trying to save markups ROI node as a markups JSON file programmatically.</p>
<p>First, I added a markups ROI node to the 3d view using ‘Markups’ module manually.<br>
And then, I saved the markups ROI node to a JSON file. I referenced the code snippet in the Script repository to do that: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups" rel="noopener nofollow ugc">Save markups to file</a></p>
<p>As shown in the figure below, here is the code I executed in the Python console:</p>
<pre><code class="lang-auto">markupsNode = slicer.util.getNode('R')
slicer.util.saveNode(markupsNode, slicer.app.defaultScenePath + "/" + "MyMarkups.mrk.json")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79f1ede04ac8cf0520ef6268918c67f0bbbb1b64.png" data-download-href="/uploads/short-url/hoM6v3kEziWOqgCSGRlQ9RdKf0E.png?dl=1" title="ROI 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79f1ede04ac8cf0520ef6268918c67f0bbbb1b64_2_690x362.png" alt="ROI 1" data-base62-sha1="hoM6v3kEziWOqgCSGRlQ9RdKf0E" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79f1ede04ac8cf0520ef6268918c67f0bbbb1b64_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79f1ede04ac8cf0520ef6268918c67f0bbbb1b64_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79f1ede04ac8cf0520ef6268918c67f0bbbb1b64_2_1380x724.png 2x" data-dominant-color="CCC8E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI 1</span><span class="informations">1766×929 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, When I trying to load the markups from the JSON file, the ROI cannot be reloaded into 3D view, it is displayed as a dot instead of the box:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06fd2b85df778c92e594933ea21b7e2f9ef10530.png" data-download-href="/uploads/short-url/ZPhiKmJY1BNvXN1H0aciEyo3u0.png?dl=1" title="ROI2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06fd2b85df778c92e594933ea21b7e2f9ef10530_2_690x433.png" alt="ROI2" data-base62-sha1="ZPhiKmJY1BNvXN1H0aciEyo3u0" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06fd2b85df778c92e594933ea21b7e2f9ef10530_2_690x433.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06fd2b85df778c92e594933ea21b7e2f9ef10530_2_1035x649.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06fd2b85df778c92e594933ea21b7e2f9ef10530_2_1380x866.png 2x" data-dominant-color="B9BBDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI2</span><span class="informations">1644×1033 63.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the JSON file automatically created by the code snippet (MyMarkups.mrk.json):</p>
<pre><code class="lang-auto">{
    "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json#",
    "markups": [
        {
            "type": "ROI",
            "coordinateSystem": "LPS",
            "coordinateUnits": "mm",
            "locked": false,
            "fixedNumberOfControlPoints": false,
            "labelFormat": "%N-%d",
            "lastUsedControlPointNumber": 1,
            "controlPoints": [
                {
                    "id": "1",
                    "label": "R-1",
                    "description": "",
                    "associatedNodeID": "",
                    "position": [-46.1154670715332, -0.0, -11.705148696899414],
                    "orientation": [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],
                    "selected": true,
                    "locked": false,
                    "visibility": true,
                    "positionStatus": "defined"
                }
            ],
            "measurements": [
                {
                    "name": "volume",
                    "enabled": false,
                    "units": "cm3",
                    "printFormat": "%-#4.4g%s"
                }
            ],
            "display": {
                "visibility": true,
                "opacity": 1.0,
                "color": [0.4, 1.0, 0.0],
                "selectedColor": [0.9372549019607843, 0.34901960784313726, 0.3843137254901961],
                "activeColor": [0.4, 1.0, 0.0],
                "propertiesLabelVisibility": true,
                "pointLabelsVisibility": false,
                "textScale": 3.0,
                "glyphType": "Sphere3D",
                "glyphScale": 1.0,
                "glyphSize": 5.0,
                "useGlyphScale": true,
                "sliceProjection": false,
                "sliceProjectionUseFiducialColor": true,
                "sliceProjectionOutlinedBehindSlicePlane": false,
                "sliceProjectionColor": [1.0, 1.0, 1.0],
                "sliceProjectionOpacity": 0.6,
                "lineThickness": 0.2,
                "lineColorFadingStart": 1.0,
                "lineColorFadingEnd": 10.0,
                "lineColorFadingSaturation": 1.0,
                "lineColorFadingHueOffset": 0.0,
                "handlesInteractive": true,
                "translationHandleVisibility": true,
                "rotationHandleVisibility": false,
                "scaleHandleVisibility": true,
                "interactionHandleScale": 3.0,
                "snapMode": "toVisibleSurface"
            }
        }
    ]
}
</code></pre>
<p>I found that the JSON file is missing the following keys under the “markups”:</p>
<pre><code class="lang-auto">"roiType":,
"center": ,
"orientation": ,
"size": ,
"insideOut",
</code></pre>
<p>Why is this happening? How do I need to modify the code snippet so that it can automatically generates a full JSON file containing the above keys to be able to reload the ROI box in the 3d view?</p>
<p>Thank you very much!</p>

---

## Post #2 by @WilliamDaniel (2022-09-26 14:44 UTC)

<p>Another thing I’ve found is that after I execute the above code, even if I click the ‘SAVE’ button to regenerate a new JSON file, it’s still incomplete as shown above, which causes when I import the ‘mrml’ file to reload the scene,  the ROI box can not be loaded.<br>
Is there any specific solutions?<br>
Thank you so much!</p>

---

## Post #3 by @Sunderlandkyl (2022-09-26 14:48 UTC)

<p>Thanks! I’m taking a look into it.</p>

---

## Post #4 by @Sunderlandkyl (2022-09-26 15:02 UTC)

<p>This issue should be fixed with this PR: <a href="https://github.com/Slicer/Slicer/pull/6551" class="inline-onebox" rel="noopener nofollow ugc">BUG: Ensure default JSON storage node is used in qSlicerMarkupsWriter by Sunderlandkyl · Pull Request #6551 · Slicer/Slicer · GitHub</a>.</p>
<p>You can call “AddDefaultStorageNode()” as a workaround in Slicer 5.0.3:</p>
<pre><code class="lang-python">markupsNode = slicer.util.getNode('R')
markupsNode.AddDefaultStorageNode()
slicer.util.saveNode(markupsNode, slicer.app.defaultScenePath + "/" + "MyMarkups.mrk.json")
</code></pre>

---

## Post #5 by @WilliamDaniel (2022-09-26 15:20 UTC)

<p>It worked, thanks a lot for your help!</p>

---
