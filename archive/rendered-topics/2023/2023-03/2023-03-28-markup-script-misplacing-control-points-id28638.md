# Markup script misplacing control points

**Topic ID**: 28638
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/markup-script-misplacing-control-points/28638

---

## Post #1 by @Kae1 (2023-03-28 22:43 UTC)

<p>My mark up script is placing mark up control points inaccurately when loaded at a later point: I am creating a mark up script by placing markup control points manually, then saving the mark up script as a json file. Later, when I drag and drop the mark up json file back into Slicer, the control point RAS values have changed positive/negative values, resulting in mark up fiducial points which are no longer co-registered to the original MRI.</p>
<p>Here is an example of the correctly positioned mark up script which I save as a JSON file:</p>
<p>{“<span class="mention">@schema</span>”: “<a href="https://urldefense.com/v3/__https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json*__;Iw!!Ek5y5249UU0kCz0!iQwT06Ekr050C2dTbGT5Ml-QpRyaA5nuJcm5yG-N3zME_sZL4cluIn2UqNdKdjhVtDO7b487jj3MFUL1vmmsmLOXyYTEKKQ%24" rel="noopener nofollow ugc">https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json#</a>”,<br>
“markups”: [{“type”: “Fiducial”, “coordinateSystem”: “LPS”, “controlPoints”: [<br>
{ “label”: “A”, “position”: [ -13.225200 , 328.873000 , 589.979000 ]},<br>
{ “label”: “A1”, “position”: [ -5.954760 , 166.782000 , 581.928000 ]}<br>
]}]}</p>
<p>However the markup file when later drag and dropped into Slicer inverts the +/- values, giving positions as following. The position values are the same, but the +/- have been inverted:</p>
<p>{ “label”: “A”, “position”: [ 13.225200 , -328.873000 , 589.979000 ]},<br>
{ “label”: “A1”, “position”: [ 5.954760 , -166.782000 , 581.928000 ]}</p>
<p>Can anyone please let me know what I am doing wrong?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @muratmaga (2023-03-29 05:29 UTC)

<p>Markup coordinates are displayed as RAS, but written in LPS. So, the sign flip in the first two coordinates are normal. For correctly written and interpreted json/fcsv files, this would not affect the position of the landmarks, it is simply different ways of book keeping.</p>
<p>But are you saying that when you load your JSON file, the coordinates are not retrieved correctly?</p>
<p>I suspect your JSON is ill-formed. It should look something like this:.</p>
<pre><code class="lang-auto">{
    "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json#",
    "markups": [
        {
            "type": "Fiducial",
            "coordinateSystem": "LPS",
            "coordinateUnits": "mm",
            "locked": false,
            "fixedNumberOfControlPoints": false,
            "labelFormat": "%N-%d",
            "lastUsedControlPointNumber": 2,
            "controlPoints": [
                {
                    "id": "1",
                    "label": "A",
                    "description": "",
                    "associatedNodeID": "",
                    "position": [-13.225, 328.873, 589.979],
                    "orientation": [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],
                    "selected": true,
                    "locked": false,
                    "visibility": true,
                    "positionStatus": "defined"
                },
                {
                    "id": "2",
                    "label": "A1",
                    "description": "",
                    "associatedNodeID": "",
                    "position": [-5.955, 166.782, 581.928],
                    "orientation": [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],
                    "selected": true,
                    "locked": false,
                    "visibility": true,
                    "positionStatus": "defined"
                }
            ],
            "measurements": [],
            "display": {
                "visibility": true,
                "opacity": 1.0,
                "color": [0.4, 1.0, 0.0],
                "selectedColor": [0.5529411764705883, 0.4745098039215686, 1.0],
                "activeColor": [1.0, 0.8823529411764706, 0.7372549019607844],
                "propertiesLabelVisibility": false,
                "pointLabelsVisibility": true,
                "textScale": 2.9000000000000005,
                "glyphType": "StarBurst2D",
                "glyphScale": 1.7000000000000002,
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
                "handlesInteractive": false,
                "translationHandleVisibility": true,
                "rotationHandleVisibility": true,
                "scaleHandleVisibility": true,
                "interactionHandleScale": 1.9000000000000002,
                "snapMode": "toVisibleSurface"
            }
        }
    ]
}
</code></pre>

---

## Post #3 by @Kae1 (2023-03-29 22:01 UTC)

<p>Thanks for this. Yes, when I reload the json file, the markups are no-longer co-registered.<br>
However I have just realized that when I change coordinateSystem to ‘RAS’ and add “coordinateUnits”: “um”, it will load and co-register correctly. So I guess that’s a solution for now. Unless there is something about that that is bad practice.<br>
Thanks again for your response and script.</p>

---

## Post #4 by @muratmaga (2023-03-30 01:36 UTC)

<aside class="quote no-group" data-username="Kae1" data-post="3" data-topic="28638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b5a626/48.png" class="avatar"> Kae1:</div>
<blockquote>
<p>Unless there is something about that that is bad practice.</p>
</blockquote>
</aside>
<p>It might give you some additional problems down the line in terms of interoperability, as most other imaging software expects coordinates in LPS. That way Slicer writes them in LPS as opposed to RAS.</p>
<p>So perhaps you can do the reverse. Keep your JSON header LPS, but multiply the RAS value by -1, -1, before writing it. That should read back correctly as you expect.</p>

---
