# MarkupsLine .fcsv loads as MarkupsFiducials

**Topic ID**: 11545
**Date**: 2020-05-14
**URL**: https://discourse.slicer.org/t/markupsline-fcsv-loads-as-markupsfiducials/11545

---

## Post #1 by @fedorov (2020-05-14 20:03 UTC)

<p>If I create a Line Markups annotation, save it as “Markups Fidicials .fcsv” (the only format available to save Markups annotations in the “Save as” dialog) and load back in Slicer, it shows up not as MarkupsLine, but as MarkupsFiducials. Is this a bug?</p>

---

## Post #2 by @muratmaga (2020-05-14 20:32 UTC)

<p>My understanding is that currently reload of MarkupsLine, Angles, Planes are not supported. They are being loaded as individual fiducials. It don’t it is not a bug, but a feature that is not implemented yet.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> can give better feedback.</p>

---

## Post #3 by @lassoan (2020-05-14 21:24 UTC)

<p>Yes, it has not been implemented yet. The main challenge is that we don’t want to invent a new file format for this and it is not easy to find a good standard one. The new DICOM-compliant json format looks promising but we did not have time for a thorough analysis. We also welcome suggestions for file formats from the community (any annotation file format that is used by a significant number of people can be a candidate).</p>

---

## Post #4 by @Sam_Horvath (2020-05-14 21:34 UTC)

<p>Possible workaround:  If you save the line/curve etc with a scene and reload using the MRML file, it will load as the correct type.</p>

---

## Post #5 by @fedorov (2020-05-14 21:51 UTC)

<p>Andras, I appreciate the concern, and I am the last one who would argue for inventing a new format … BUT the .fcsv format already exists, whether we like it or not, and the Line annotations are already saved, but cannot be reloaded.</p>
<p>It is a good idea to consider DICOM as an option, but the scope of use for Slicer is broader than medical imaging covered by DICOM, the annotations may need to exist without any images being annotated, and it just may never happen that DICOM will be able to meet the needs of all Slicer users.</p>
<p>I would argue that LineMarkups should be saved in a Slicer-specific format, but with the attributes that, when applicable, would allow to convert that general-purpose representation into something more specific. So for example, for DICOM, if Line is annotated on the images that are loaded from DICOM, it might be helpful to store the SeriesInstanceUID for the volume being annotated.</p>
<p>I asked this question because I work with a user who is submitting a very valuable dataset (at least, in my opinion) to TCIA (3D Ultrasound volumes, MR series, segmentations, and annotated locations of biopsy samples). The user initially was submitting the data that could only be loaded into the custom Matlab tools he had. We worked together to make sure that the 3D US DICOM files could be loaded into Slicer, and STL surfaces are in the same coordinate frame as images, and I also suggested that instead of a spreadsheet with biopsy locations he uses Slicer .fcsv, and based on his assessment, Line annotation is best suitable for this purpose. But it is not possible to reload it back.</p>
<p>He also identified the workaround suggested by <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>. After playing with it a bit, I think I am going to suggest to save all annotations for individual studies and save as a MRML scene, without images (I didn’t know that a scene can be reloaded without replacing the existing scene!). Then the consumers of the dataset would just need to follow the directions to compose the scene from the DICOM, STL and MRML bits … In this specific case, we could probably come up with a standard way to store all of the components in DICOM, but implementing all of the pieces that would be needed to do the conversion, figure out details of encoding, and support loading in Slicer are incompatible with the time constraints for the dataset submission, and will require non-trivial effort. Eventually, I hope we will get to do it, but for now my goal is to have the dataset that can be loaded using 3D Slicer, so we are prepared to do the conversion later.</p>

---

## Post #6 by @pieper (2020-05-14 22:09 UTC)

<p>Totally agree with these points - if you are okay with a Slicer-specific data format then MRML is totally the right answer.</p>

---

## Post #7 by @muratmaga (2020-05-15 06:37 UTC)

<p>While MRML retains the Markups as they are intended (angles, lines), it is a harder format to extract the coordinates from. The simplicity of fcsv is great, and it can be readily imported into other data analysis platforms. MRML harder to decipher.</p>
<p>While I will agree with the notion to NOT to invent a yet another format, I am wondering if we can’t find a compromise, and add another field to fcsv called “type” which would be line, curve, closedcurve, angle and plane. So when they are read in, they can be reconstructed as MarkupLine, MarkupAngle and MarkupPlane etc.</p>
<p>The measurements they report perhaps can be recalculated at the time of loading the data (length, angle, area)? So, while the measurement value itself is not saved in the file, it can still be reconstituted by reloading the data into the scene.</p>
<p>Would this be an acceptable half-solution?</p>

---

## Post #8 by @lassoan (2020-05-15 16:25 UTC)

<p>What do you think about saving current content of markup node into a json file like this:</p>
<pre><code class="lang-json">{
  "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/doc/markups-schema.json#",
  "markups": [ {
    "label": "Some Angle",
    "type": "angle",
    "coordinateSystem": "LPS",
    "controlPoints": [
        {
            "id": "1",
            "label": "A-1",
            "description": "",
            "associatedNodeID": "",
            "position": [12.3, 28.4, 11.2],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
            "selected": True,
            "locked": False,
            "visibility": True,
            "positionStatus": "defined"
        },
        {
            "id": "2",
            "label": "A-2",
            "description": "",
            "associatedNodeID": "",
            "position": [12.3, 28.4, 11.2],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
            "selected": True,
            "locked": False,
            "visibility": True,
            "positionStatus": "defined"
        },
        {
            "id": "3",
            "label": "A-3",
            "description": "",
            "associatedNodeID": "",
            "position": [12.3, 28.4, 11.2],
            "orientation": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
            "selected": True,
            "locked": False,
            "visibility": True,
            "positionStatus": "defined"
        }
    ],
    "measurements" : [
        {
            "name": "angle",
            "printableValueWithUnit": "23.5 deg",
            "value": 23.5,
            "units": "degrees",
            "description": "angle between first two and last two points",
            "printFormat": "",
            "quantityCode": "",
            "unitsCode": "",
            "methodCode": ""
        },
        {
            "name": "length",
            "printableValueWithUnit": "11.2 mm",
            "value": 11.2,
            "units": "mm",
            "description": "distance between first and last points",
            "printFormat": "",
            "quantityCode": "",
            "unitsCode": "",
            "methodCode": ""
        }
    ],
    "display": {
        "color": [1.0, 0.0, 0.0],
        "selectedColor": [1.0, 1.0, 0.0],
        "propertiesLabelVisibility": True,
        "pointLabelsVisibility": True,
        "textScale": 5.0,
        "glyphType": "sphere3D",
        "glyphScale": 5.0,
        "glyphSize": 3.0,
        "useGlyphScale": True,
        "sliceProjection": False,
        "sliceProjectionUseFiducialColor": True,
        "sliceProjectionOutlinedBehindSlicePlane": True,
        "sliceProjectionColor": [0.2, 0.4, 0.8],
        "sliceProjectionOpacity": 0.5,
        "lineColormap": "viridis",
        "LineThickness": 2.0,
        "LineColorFadingStart": 2.0,
        "LineColorFadingEnd": 2.0,
        "LineColorFadingSaturation": 2.0,
        "LineColorFadingHueOffset": 2.0
    },
    "behavior": {
          "snapMode": "snapToVisibleSurface",
          "handlesInteractive": False
    },
    "curvePoints": [
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9],
        [0.0, 0.1, 0.2],
        [0.2, 0.3, 0.5],
        [0.5, 0.8, 0.9]
    ] }
  ]
}
</code></pre>
<p>Some sections, such as display, behavior, and cuvePoints could be optional or not used for all types of markups.</p>
<p>Reading/writing speed in C++ and Python looks good - a few seconds for tens of thousands of points.</p>
<p>The file could store any number of markups (e.g., a folder could be selected in data module and all markups in that folder could be exported into a single json file).</p>
<p>You can import a json file and export a csv file with columns populated with control point properties in about 10 lines of Python code (or we could also add a csv export option). However, these csv files could not be imported as markups.</p>

---

## Post #9 by @fedorov (2020-05-15 17:02 UTC)

<p>Overall, I think it is definitely a much better approach than the current fcsv, but predictably it does open the cans of worms! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>
<p>Couple of quick thoughts:</p>
<ul>
<li>Can you share the schema file? <a href="https://raw.githubusercontent.com/slicer/slicer/master/doc/markups-schema.json">https://raw.githubusercontent.com/slicer/slicer/master/doc/markups-schema.json</a> doesn’t work for me.</li>
<li>I understand the reasons behind keeping <code>associatedNodeID</code>, but it would be nice to have some reference that is not scene-specific. Can we add some reference to the DICOM series, if available? A related question is what else, if anything, should be recorded about the state of the viewers at the time given markup was created.</li>
<li>Would it make sense to have a UID assigned to each element in the scene to disambiguate the references? Or maybe better to have scene assigned a UID, and then items within the scene can be interpreted in the context of the scene UID?</li>
<li>
<code>FrameOfReferenceUID</code> from DICOM, if available, could be valuable to include.</li>
<li>Should we consider including any information about the authoring of the annotation? (e.g., information about the user, whether the annotation was generated manually or automaticaly)</li>
</ul>
<p>Somewhat related, here’s the <a href="https://docs.google.com/document/d/1bR6m7foTCzofoZKeIRN5YreBrkjgMcBfNA7r9wXEGR4/edit?ts=5e80adb1">white paper summarizing DICOM SR capabilities related to planar annotations</a>. We’ve been working on this in the context of the IDC project.</p>
<p>I don’t want to derail or delay your initiative by adding more requirements, just a couple of thoughts to consider. This is definitely a great start, but we should discuss this more. I suggest we split this off into a separate conversation?</p>

---

## Post #10 by @muratmaga (2020-05-15 21:02 UTC)

<p>So this format would also contain the regular MarkupsFiducials as well, or do we retain them as fcsv?</p>

---

## Post #11 by @lassoan (2020-05-16 04:16 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Can you share the schema file? <a href="https://raw.githubusercontent.com/slicer/slicer/master/doc/markups-schema.json">https://raw.githubusercontent.com/slicer/slicer/master/doc/markups-schema.json</a> doesn’t work for me.</p>
</blockquote>
</aside>
<p>There is no schema yet. We can create that once we have a good idea of the final format.</p>
<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I understand the reasons behind keeping <code>associatedNodeID</code> , but it would be nice to have some reference that is not scene-specific</p>
</blockquote>
</aside>
<p>This is what is in the markups node now. I agree that it is not very useful, as node IDs can only be used with a scene file. How would you recommend to refer to a DICOM series? Would a series instance UID be enough?</p>
<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Would it make sense to have a UID assigned to each element in the scene to disambiguate the references? Or maybe better to have scene assigned a UID, and then items within the scene can be interpreted in the context of the scene UID?</p>
</blockquote>
</aside>
<p>You mean using a universal unique identifier (UUID) to each node in the scene? What if you load the same scene twice? Would you generate new UUIDs?</p>
<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><code>FrameOfReferenceUID</code> from DICOM, if available, could be valuable to include.</p>
</blockquote>
</aside>
<p>We could definitely allow a field like that in the file. It might be tricky to get this information in general (data may be loaded from multiple sources and so there could be several frame of references), but there could be modules that implement specific workflows and can determine this information reliably.</p>
<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Should we consider including any information about the authoring of the annotation?</p>
</blockquote>
</aside>
<p>Yes, sure. Do you have any suggestion of what information should be recorded exactly?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="11545" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So this format would also contain the regular MarkupsFiducials as well, or do we retain them as fcsv?</p>
</blockquote>
</aside>
<p>We could still allow saving markup fiducials as .fcsv, in addition to the new .mrk.json. Similarly how a volume can be saved in .nrrd or .mha format.</p>

---

## Post #12 by @fedorov (2020-05-17 14:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How would you recommend to refer to a DICOM series? Would a series instance UID be enough?</p>
</blockquote>
</aside>
<p>Maybe better to record SOPInstanceUIDs for individual points, initialized from the slice from the foreground volume in the viewer that was used to place the point?</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You mean using a universal unique identifier (UUID) to each node in the scene? What if you load the same scene twice? Would you generate new UUIDs?</p>
</blockquote>
</aside>
<p>How about a new UUID assigned to a scene every time the scene is saved, and keeping the individual nodes IDs unchanged?</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, sure. Do you have any suggestion of what information should be recorded exactly?</p>
</blockquote>
</aside>
<p>For example, whether annotations were created manually or by an automated tool, and maybe also have an option to include some kind of user identification (either collected from the system, or self-declared by the user in the settings).</p>

---

## Post #13 by @lassoan (2020-05-27 23:29 UTC)

<p>I’ve submitted a pull request that implements storage of markup data and display node in JSON file:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/4938" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/4938" target="_blank">ENH: Added json file format for markups</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:markups-json2</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-27" data-time="23:18:17" data-timezone="UTC">11:18PM - 27 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 20 files with 1442 additions and 282 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/4938/files" target="_blank">
          <span class="added">+1442</span>
          <span class="removed">-282</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The file content right now is a trivial mapping of MRML node properties to JSON name:value pairs, but there are undergoing discussions to adopt DICOM SR compliant JSON representation instead. See more information and examples in <a>this DICOM supplement</a>.</p>

---

## Post #14 by @muratmaga (2020-06-01 16:57 UTC)

<p>I tried loading the .json’s without the MRML node into a blank scene, and I got these errors:<br>
It is with today’s build (on windows 10).</p>
<pre><code>vtkMRMLMarkupsJsonStorageNode::ReadDataInternal failed: error parsing the file  'C:/Users/murat/Desktop/A.mrk.json


vtkMRMLMarkupsStorageNode::ReadDataInternal failed: error opening the file 'C:/Users/murat/Desktop/A.mrk.json


vtkMRMLMarkupsJsonStorageNode::ReadDataInternal failed: error parsing the file  'C:/Users/murat/Desktop/C.mrk.json


vtkMRMLMarkupsStorageNode::ReadDataInternal failed: error opening the file 'C:/Users/murat/Desktop/C.mrk.json</code></pre>

---

## Post #15 by @lassoan (2020-06-02 02:28 UTC)

<p>I cannot reproduce this issue using Slicer 4.11.0-2020-05-30 (revision 29099 / e53e8af) win-amd64. The dashboard looks good, too: vtkMRMLMarkupsStorageNodeTest2 test checks if a node can be saved and reloaded and it has not failed on any platforms.</p>
<p>Can you upload somewhere the files that fail to load and post the link here?</p>
<p>Do the files match the <a href="https://raw.githubusercontent.com/Slicer/Slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json">json schema</a>? (you can check with this <a href="https://www.jsonschemavalidator.net/">online tool</a>)</p>

---

## Post #16 by @muratmaga (2020-06-02 04:35 UTC)

<p>Here you go: <a href="https://app.box.com/s/6aguthyvz8o1p7kc0pvwuyiv29noyjne" rel="nofollow noopener">https://app.box.com/s/6aguthyvz8o1p7kc0pvwuyiv29noyjne</a></p>
<p>At least the angles json checked out with the online tool. But I still cannot load them</p>

---

## Post #17 by @lassoan (2020-06-02 05:11 UTC)

<p>Some control points in these files have invalid orientation, which prevents loading them. How did you create the markups?</p>

---

## Post #18 by @muratmaga (2020-06-02 05:25 UTC)

<p>Weird. I just randomly clicked a few points in an empty scene to test the save and load.</p>

---

## Post #19 by @lassoan (2020-06-03 21:37 UTC)

<p>I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/7dbc2dcda8f8d696cbef31caad747eaaebad6c99">fix</a> today. Let me know if you can still reproduce the problem in the Preview Release tomorrow or later.</p>

---

## Post #20 by @jmhuie (2020-06-10 03:49 UTC)

<p>I just downloaded the newest nightly build and realized the markup fudicials are saved as mrk.json files. If possible, I am in favor keeping the option to save them as .fscv files as mentioned by Murat that is a convenient file format to be used elsewhere. Thank you.</p>

---

## Post #21 by @muratmaga (2020-06-10 04:08 UTC)

<p>It should be available. In the save as dialog box, you should be able to change it back to .fcsv (in fact for me that’s the default for fiducials, mrk.json only is enabled for angles, planes, lines, and others).</p>

---

## Post #22 by @jmhuie (2020-06-10 05:04 UTC)

<p>Ah my bad. I got mixed up. I meant to say that it’d be great to still have the option to save curves as .fscv files.</p>

---

## Post #23 by @muratmaga (2020-06-10 17:00 UTC)

<p>The only time it makes sense to curves as fcsv, if you are using the control points as semi-landmarks in the analysis. Is that your use case?</p>
<p>And yes, it appears that ability to save curves as fcsv format also disappeared.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> is it possible to bring back the fcsv format for curves (both open and close), or should we approach this specifically in SlicerMorph?</p>

---

## Post #24 by @lassoan (2020-06-10 19:37 UTC)

<p>We need to distinguish between:</p>
<ul>
<li>node saving/loading: lossless storage of all the information of a markups node, to be used when you save the scene</li>
<li>node export/import: writing of <em>some</em> information of a markups node to a file that can be processed outside of Slicer; and reading markups stored in various formats</li>
</ul>
<p>.fcsv or .csv format is perfectly fine for node export, but it is not suitable for node saving, as it cannot store all information that markups node can contain and the format is not flexible or extensible enough (you cannot easily add more metadata while keeping backward compatibility, you cannot store a variety of markups in a single file, etc.). Therefore, we’ll use json for node saving/loading.</p>
<p>However, users can very easily export markups to any other format of their choice, such as standard csv. If there file formats that seem to be preferred by many users, or used by other popular software then we can add importers/exporters for them in Slicer core.</p>
<p><a class="mention" href="/u/jmhuie">@jmhuie</a> Can you write a bit more about your application and how do you process exported data (what programming language or software do you use)?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="23" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>is it possible to bring back the fcsv format for curves (both open and close), or should we approach this specifically in SlicerMorph?</p>
</blockquote>
</aside>
<p>We now have two storage nodes for markups: vtkMRMLMarkupsJsonStorageNode and vtkMRMLMarkupsFiducialStorageNode. File formats that are displayed in Save dialog are those that are offered by the current storage node. You can create a new storage node and assign it to the markups node to switch between fcsv and json but there is no GUI for this.</p>
<p>There could be many ways to allow users to more easily switch between fcsv and json (for example, merge the two storage nodes), but since fcsv is a lossy format for current markups (it cannot store all information that is in markup nodes), I don’t think we would want to keep using fcsv for saving fiducials. Csv import/export is certainly useful, so when we change default save format for fiducials to json then we’ll have to make csv/fcsv export conveniently available to users.</p>

---

## Post #25 by @pieper (2020-06-10 20:23 UTC)

<p>We already expose some lossy formats in the save dialog (e.g. STL of a model with scalars).  Probably we should flag the lossy ones like fcsv but still give the option.</p>

---

## Post #26 by @lassoan (2020-06-10 21:48 UTC)

<p>Slicer always offers saving in a lossless file format by default and we assume that users know what they are doing when they choose a different one. But of course users don’t always know the limitations of each format. There are some particularly sneaky errors, such as image directions lost when saving image as .vtk, or image axes orthogonalized when saving as nifti.</p>
<p>Maybe we should add a warning icon in the Save data dialog, which would be displayed when not all information of a node can be saved in the chosen format? Or show a warning at the end of the save operation (we wanted to implement display of more detailed error information anyway). Or maybe we should separate scene saving and data export more clearly (as it is done in other software, such as Gimp or Blender)? Although I have to admit that as a user I don’t like this forceful distinction between Dave and export in Gimp - I would just want to save the edited file by clicking “Save” instead of remembering that in this software I need to look for “Overwrite…”.</p>

---

## Post #27 by @muratmaga (2020-06-11 03:26 UTC)

<p>I like the ability to read the measurements, angles into SLicer with the new json format. However, I did probe our users when we discussed this initially a few months ago, and a lot people indicated they like the ease of reading fcsv into R (or other data analysis programs). So if possible, I would like the fcsv save as option to be enabled for curves in particular. I think it make sense to keep the json as the primary ‘lossless’ format, but give the option fcsv as a secondary format that user has to choose.</p>
<p>Another option separating Save As from Export that discussed briefly sometime ago was to implement Export As as a right-click action from the Data module.</p>

---

## Post #28 by @pieper (2020-06-11 12:25 UTC)

<p>To me the most consistent would be to flag the lossy file types, perhaps with a <code>*</code> or other warning icon when the type is selected for save (and a tooltip explaining the icon).  This would help educate people who might choose to save surfaces in STL just because they have heard of it and not realize the limitations.</p>

---

## Post #29 by @lassoan (2020-06-11 14:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="27" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>a lot people indicated they like the ease of reading fcsv into R</p>
</blockquote>
</aside>
<p>Probably people feel more comfortable with tables because they know them already and they need to use them for computations anyway. While tables are great for data processing, they are not well suited for data archival, because if you store data in tables then you either need to use many tables cross-referencing each other; or have fewer tables, with highly redundant information. If you store data in a json file then you can create tables as temporary “views” of the data by a couple of lines of R code, but you need to educate users about how to do that.</p>
<p>But of course Slicer should push people too much to learn, even if that would be the right thing to do. Maybe a good solution would be to add a “Convert” section to markups module, which would allow converting markups to/from table nodes? In table export, there could be a few options about what columns to export and how. Table nodes can be already loaded and saved as standard csv files.</p>
<p>Do you know if users expect to see only control points or all curve point coordinates in the exported csv files?</p>

---

## Post #30 by @pieper (2020-06-11 15:58 UTC)

<p>I like the idea of providing an option to convert the Markups to Table nodes - that way people can see them directly in Slicer before saving.  Maybe they can even do some simple plotting without having to leave Slicer.  Would also be cool if we could create something like a MarkupStatistics that would create more sophisticated tables and plots.</p>

---

## Post #31 by @muratmaga (2020-06-11 16:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="29" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you know if users expect to see only control points or all curve point coordinates in the exported csv files?</p>
</blockquote>
</aside>
<p>We only need the control points. <a class="mention" href="/u/smrolfe">@smrolfe</a> can chime in, but the curve resampling function in the curves would take a curve (and optioanlly a model) with a few control points, and would create a new curve by resampling specifed number of equidistant points on curve. These become the control points of the new curve, and that’s what people need to save and use in their analyses.</p>
<p>Ideas about the implementing additional summary tables and conversion tools is fine to continue to discuss, but for the time being we do need the fcsv save as option for curves for people to continue saving the way they used to.</p>
<p>Again, I think the default save mode should be json, with an option to choose to save as fcsv as format (perhaps with an indicator about lossiness).</p>

---

## Post #32 by @smrolfe (2020-06-11 16:48 UTC)

<p>I agree. I don’t see a need for all curve point coordinates when the resampling function can provide more/equidistant control points when needed. The control points should be sufficient.</p>

---

## Post #33 by @lassoan (2020-06-11 18:05 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="31" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>but for the time being we do need the fcsv save as option for curves for people to continue saving the way they used to</p>
</blockquote>
</aside>
<p>How do your users use .fcsv files now?</p>
<ul>
<li>They cannot be parsed by standard csv readers because they have an invalid header (multiple lines of non comma-separated values). Do they manually remove the first few lines after each saving? Do they remove those lines programmatically in their analysis scripts?</li>
<li>What do they do with the .fcsv curves after saving? They cannot load it back into Slicer as curves, just as fiducials.</li>
<li>Is not a problem for them that they end up with as many files as curves? It is so much harder to manage, compare, process models if they are stored across many files. You can easily export many curves, labels, etc. into a single json file.</li>
</ul>
<p>If your users really want direct csv export from Slicer then they would be probably much better off having a one-click export of standard .csv format (not .fcsv) in your module, rather than trying to make the generic Save data dialog work well for this specific use case.</p>
<p>I think for most other users it would be enough to add an Export/import section in Markups module, which could export/import markups to table and model nodes (similarly to how Segmentations can be imported/exported to labelmap volume and model nodes).</p>
<p><a class="mention" href="/u/jclauneuro">@jclauneuro</a> I know that you use .fcsv files extensively, too. What do you think about switching to json? It would have many advantages, but we would want to ensure smooth transition and backward compatibility with old files.</p>

---

## Post #34 by @muratmaga (2020-06-11 19:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="33" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>They cannot be parsed by standard csv readers because they have an invalid header (multiple lines of non comma-separated values). Do they manually remove the first few lines after each saving? Do they remove those lines programmatically in their analysis scripts?</p>
</blockquote>
</aside>
<p>Reading the coordinates from fcsv into a dataframe in R is a single liner, which they loop over.<br>
<code>read.csv(file='F.fcsv', skip=2, header=T)[,2:4]</code><br>
that’s what most people do.</p>
<blockquote>
<p>What do they do with the .fcsv curves after saving? They cannot load it back into Slicer as curves, just as fiducials.</p>
</blockquote>
<p>Most often, we only need the coordinates from the resampled curve. If they want to retain their original hand-drawn curve, they can save that as a json.</p>
<aside class="quote no-group" data-username="lassoan" data-post="33" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is not a problem for them that they end up with as many files as curves? It is so much harder to manage, compare, process models if they are stored across many files. You can easily export many curves, labels, etc. into a single json file.</p>
</blockquote>
</aside>
<p>But this is already the default behavior for json format too! I get as many json’s to save as I have curve nodes.</p>
<p>By the way I am not opposing these changes, and I am sure we will find a good solution moving forward. However, not enabling the existing fcsv format cripples our current users. So, until we have a final solution, my suggestion is to re-enable (albeit temporarily) the fcsv format as a secondary file saving option.</p>

---

## Post #35 by @lassoan (2020-06-11 19:41 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="34" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Most often, we only need the coordinates from the resampled curve. If they want to retain their original hand-drawn curve, they can save that as a json</p>
</blockquote>
</aside>
<p>The main issue is that vtkMRMLMarkupsFiducialStorageNode and vtkMRMLMarkupsJsonStorageNode are two different storage nodes, so you cannot switch between formats offered by them in Save data dialog (you need to delete one storage node and create the other type if you want to switch). Calling vtkMRMLMarkupsFiducialStorageNode from vtkMRMLMarkupsJsonStorageNode could be feasible, but not clear, would complicate things, and not something that we would want to maintain in the long term.</p>
<p>I think what your users would prefer is a convenient export option. You could export all the curves by a single click (you would not need to manually select/unselect node in save dialog, remember to set output folder, remember to set file format; then later remember to set file format back to json for saving). You could further simplify things for the users by doing resampling automatically during this export step (so users would not need to manually resample the curves). Doing resampling during export could be also beneficial because resampling is a destructive operation.</p>
<p>In the long term, everybody will win with switching to json. Reading part of a json file into an R dataframe may not be a one-liner, but should not be more than a couple of lines, and of course SlicerMorph could implement a small reader functions in Python and R to simplify things.</p>
<p>Saving multiple markups could be added as a subject hierarchy action to markups module’s plugin. It should be quite easy and it would be great if you could work on it, but eventually <a class="mention" href="/u/jcfr">@jcfr</a> or I will get to it, too.</p>

---

## Post #36 by @muratmaga (2020-06-11 19:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="35" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think what your users would prefer is a convenient export option.</p>
</blockquote>
</aside>
<p>I agree. Can the vtkMRMLMarkupsJsonStorageNode converted to vtkMRMLMarkupsFiducialStorageNode and exported as regular fcsv? Like right-click export as function? <a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="35" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You could further simplify things for the users by doing resampling automatically during this export step (so users would not need to manually resample the curves). Doing resampling during export could be also beneficial because resampling is a destructive operation.</p>
</blockquote>
</aside>
<p>Resampling may need tweaking of some parameters, and it can’t be done at bulk effectively. It is not destructive either, you can choose to output a new curve (although current default behavior is to overwrite the existing node).</p>

---

## Post #37 by @lassoan (2020-06-11 20:34 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="36" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Can the vtkMRMLMarkupsJsonStorageNode converted to vtkMRMLMarkupsFiducialStorageNode and exported as regular fcsv? Like right-click export as function?</p>
</blockquote>
</aside>
<p>No need to convert storage nodes. For export, you can create a temporary vtkMRMLMarkupsFiducialStorageNode, which does not interfere with the regular storage node that is used for saving (filename, format, and saved state are all preserved):</p>
<pre><code class="lang-auto">markupsNode = getNode('Curve1')
temporaryStorageNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialStorageNode")
temporaryStorageNode.SetFileName("c:/tmp/something.fcsv")
temporaryStorageNode.WriteData(markupsNode)
slicer.mrmlScene.RemoveNode(temporaryStorageNode)
</code></pre>

---

## Post #38 by @jmhuie (2020-06-11 23:03 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="23" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The only time it makes sense to curves as fcsv, if you are using the control points as semi-landmarks in the analysis. Is that your use case?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="24" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/jmhuie">@jmhuie</a> Can you write a bit more about your application and how do you process exported data (what programming language or software do you use)</p>
</blockquote>
</aside>
<p>I have been using the curves as semi-landmarks and exporting them as .fscv to be read and processed in R. I recognize the issue with .fscv not holding any data and trying to load those back into Slicer.</p>
<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="34" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="33" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>They cannot be parsed by standard csv readers because they have an invalid header (multiple lines of non comma-separated values). Do they manually remove the first few lines after each saving? Do they remove those lines programmatically in their analysis scripts?</p>
</blockquote>
</aside>
<p>Reading the coordinates from fcsv into a dataframe in R is a single liner, which they loop over.<br>
<code>read.csv(file='F.fcsv', skip=2, header=T)[,2:4]</code><br>
that’s what most people do.</p>
</blockquote>
</aside>
<p>I do something along this line. I’ve written a short function in R that reads all of the .fscv files with a “XXXX_Genus_species.fscv” from a folder and converts it into an R friendly format. XXXX could represent any set of MarkupFiducials or curve with semi-landmarks. From there, it’s not really that bad to concatenate curves and points.</p>

---

## Post #39 by @lassoan (2020-06-11 23:53 UTC)

<p>The AFIDS group seems to be on board with switching to json (they already convert fcsv to json). From <a href="https://github.com/afids/afids-validator/issues/90#issuecomment-642941617:" class="inline-onebox">Switching to json? · Issue #90 · afids/afids-validator · GitHub</a></p>
<blockquote>
<p>This sounds great for us on the validator development end. With the majority of the code in Python, we are currently storing relevant information in an json object after reading in the fcsv file (skipping a few lines as someone in the discussion mentioned) as its easier for us to work with. A change in file format would likely be pretty simple to update once we know what keys to look for and would likely allow us to skip a few steps for users using Slicer5.</p>
</blockquote>

---

## Post #40 by @jclauneuro (2020-06-12 03:45 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> thanks for looping our team in. I think the simple answer is that we will adapt to whatever specs are decided on for Slicer5, but ultimately we have interest in easily being able to convert between Slicer’s Markup file format and one that would be compatible with the Brain Imaging Data Structure (BIDS) specifications.</p>
<p>This may be a good time to try to determine if there is a point of convergence between the needs of both Slicer and BIDS for handling coordinates in .json files that might eliminate the need for any conversion tool. It may be better if I start a new thread about this since I would be veering quite off topic from the original thread.</p>

---

## Post #41 by @jclauneuro (2020-06-12 03:58 UTC)

<p>Just made the following thread: <a href="https://discourse.slicer.org/t/switching-to-json-for-markup-files-any-convergence-with-bids/">https://discourse.slicer.org/t/switching-to-json-for-markup-files-any-convergence-with-bids/</a></p>

---

## Post #42 by @muratmaga (2020-06-12 04:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="37" data-topic="11545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>No need to convert storage nodes. For export, you can create a temporary vtkMRMLMarkupsFiducialStorageNode, which does not interfere with the regular storage node that is used for saving (filename, format, and saved state are all preserved):</p>
</blockquote>
</aside>
<p>OK. <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/smrolfe">@smrolfe</a> will work on a ‘Export’ fun will likely send a PR somepoint.</p>

---

## Post #43 by @muratmaga (2020-08-19 15:08 UTC)

<p>ExportAs Subject hierarchy plugin is now available in the SlicerMorph extension. It allows export of non-fiducial Markup nodes to be saved in the lossy fcsv format through right-click context menu.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/ExportAs" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/45026482?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/ExportAs" target="_blank" rel="nofollow noopener">SlicerMorph/SlicerMorph</a></h3>

<p>Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #44 by @J_Deng (2020-09-11 12:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff64228180c4606165160370ae56e3ce1b514c50.png" data-download-href="/uploads/short-url/Arii9mNBbGfBD3L5mJSNL5EwzHW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff64228180c4606165160370ae56e3ce1b514c50_2_621x499.png" alt="image" data-base62-sha1="Arii9mNBbGfBD3L5mJSNL5EwzHW" width="621" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff64228180c4606165160370ae56e3ce1b514c50_2_621x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff64228180c4606165160370ae56e3ce1b514c50_2_931x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff64228180c4606165160370ae56e3ce1b514c50.png 2x" data-dominant-color="BFBED9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1042×838 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am using the latest preview version 4.11.0-2020-09-08 r29363 / c565268 to mark the anatomies in the 3D views. Among various possible options: annotation, markup, label, I’ve found markups are the closest ones to do so [as the markups can move together with corresponding anatomies in 3D]. But despite having changed default names MarkupsF… on the left panel, the names in 3D do not make corresponding changes. Am I using a wrong function to label structures or is is a glitch with the latest version? By the way, how to remove the cubical box lines and orientation indicators [S, L, I … ; the latter are often irrelevant to ultrasound volume data as we acquire images not in standard CT or MRI ways]. Thanks.</p>

---

## Post #45 by @muratmaga (2020-09-11 14:59 UTC)

<p>My suspicion is you are using the create MarkupFiducial button, and then rename the resultant node later one, but not the individual fiducial point. The buttons shown below (two small red rectangles) are actually differ in functionality.</p>
<p>In any event, you can rename the individual points within a MarkupFiducial by expanding the Control Points tab, and changing the associated labels.</p>
<p>For SlicerMorph, we have a tutorial on markups (it is more towards landmark data collection), but I think it will be still useful if you are new to Slicer: <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_2/Markups/Markups.md" rel="nofollow noopener">https://github.com/SlicerMorph/S_2020/blob/master/Day_2/Markups/Markups.md</a></p>
<p>                    <a href="https://raw.githubusercontent.com/SlicerMorph/S_2020/master/Day_2/Markups/markupsModule1.png" target="_blank" rel="nofollow noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/SlicerMorph/S_2020/master/Day_2/Markups/markupsModule1.png" width="690" height="388">
          </a>

</p>

---
