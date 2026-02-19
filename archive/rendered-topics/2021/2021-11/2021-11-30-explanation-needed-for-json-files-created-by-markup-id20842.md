---
topic_id: 20842
title: "Explanation Needed For Json Files Created By Markup"
date: 2021-11-30
url: https://discourse.slicer.org/t/20842
---

# Explanation needed for JSON files created by Markup

**Topic ID**: 20842
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/explanation-needed-for-json-files-created-by-markup/20842

---

## Post #1 by @IrisZzz (2021-11-30 13:45 UTC)

<p>Hello everyone,<br>
I am currently processing some 3D MRI images. I used the ROI module in Markups to help me mark some areas of interest and I exported all the markups into JSON files. When I tried to use Python to crop the image based on the “center” and “size” information provided in the JSON, I found that the resulting image was not what I expected.<br>
I guess it may be because my definition of “center” is not clear enough. I think this center refers to the offset of the center of the MarkupROI relative to the original image. But I am not sure what is the definition of the center of the original image is defined?</p>
<p>Could anyone tell me how to use the “center” and “size” information provided in the JSON output by Markup to crop the image?</p>
<p>Part of my JSON file is listed as below.<br>
“markups”: [<br>
{<br>
“type”: “ROI”,<br>
“coordinateSystem”: “LPS”,<br>
“locked”: false,<br>
“labelFormat”: “%N-%d”,<br>
“roiType”: “Box”,<br>
“center”: [-16.894228455178224, 69.62730835505622, -20.637574207785045],<br>
“orientation”: [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],<br>
“size”: [125.63666428522919, 156.5933399713489, 165.8335293801675],</p>

---

## Post #2 by @pieper (2021-11-30 13:52 UTC)

<p>Coordinates are expressed in LPS, so if you want to operate on a image you also need to take into account the matrix that maps indices to LPS space.  More information at the link below.</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @lassoan (2021-11-30 17:46 UTC)

<p>You may also find definition of all the properties specified in the markups json file useful: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json" class="inline-onebox">Slicer/markups-schema-v1.0.3.json at master · Slicer/Slicer · GitHub</a></p>

---

## Post #4 by @mikebind (2021-11-30 18:46 UTC)

<p>The “center” coordinates given are the location of the center of your ROI in a 3D world coordinate system.  Your image volume is also positioned in the same 3D world coordinate system.  Slicer internally uses an RAS coordinate system (right-anterior-superior), but much of the rest of the medical software world expects an LPS coordinate system (left-posterior-superior), so the saved exported coordinates are LPS. The image volume voxels are positioned in 3D space according to a transformation matrix which takes an IJK index vector into the image volume voxel array and transforms it to a spatial location.  This transformation matrix is the IJKtoRASMatrix.<br>
In addition to a center, your ROI has to have dimensions (how long the sides are) and an orientation (which directions the sides are oriented in). The “size” output is either the distance from the center to each of the faces of the ROI, or it is the distance from one face to the opposite face (the schema linked to doesn’t make this clear), you can figure out which it is by testing it out.  The “orientation” describes the three LPS directions to the faces of the ROI.</p>
<p>To do the cropping you want to achieve, you would need to figure out how your ROI is positioned relative to your image volume, which involves making sure you understand the coordinate systems involved and the relationships between them very well.  The “Crop Volumes” module in Slicer can do all this for you, is there a reason that won’t work for you?  It will even take your ROI as an input directly and use it for the cropping.</p>

---

## Post #5 by @IrisZzz (2021-12-01 01:51 UTC)

<p>Thanks Mike,</p>
<p>The reason I chose to use Markups instead of Crop is that I was expected to build a model to crop my volumes automatically. So I am afraid I will need the information of all boundaries. The output .txt file from the crop module seems does not contain any ‘start-end’ information for each dimension. I will try to explore more with the coordinate system but meanwhile, I would like to ask do you know if any other module in 3D slicer could help me to achieve this?</p>
<p>Cheers.</p>

---

## Post #6 by @mikebind (2021-12-01 17:47 UTC)

<p>Can you share a little more about what you are trying to accomplish?  Do you want to crop a series of volumes using the same ROI?  Are you trying to figure out how to programmatically generate a Markups ROI? What is your ultimate goal?  There may be many alternative ways to reach that goal.</p>

---

## Post #7 by @lassoan (2021-12-01 22:16 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="20842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>The “size” output is either the distance from the center to each of the faces of the ROI, or it is the distance from one face to the opposite face (the schema linked to doesn’t make this clear)</p>
</blockquote>
</aside>
<p>Distance from center to faces would be “radius” and not “size”, but it would not harm if the description would be more explicit. Feel free to improve the description in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json">schema file</a> - github will automatically create a pull request that we can easily review and merge.</p>

---
