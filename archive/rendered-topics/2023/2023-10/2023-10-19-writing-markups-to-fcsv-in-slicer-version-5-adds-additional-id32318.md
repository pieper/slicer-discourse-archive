# Writing markups to FCSV in Slicer version 5+ adds additional columns

**Topic ID**: 32318
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/writing-markups-to-fcsv-in-slicer-version-5-adds-additional-columns/32318

---

## Post #1 by @Greydon_Gilmore (2023-10-19 02:27 UTC)

<p>Hi all,</p>
<p>I’ve noticed a bug when saving control points to FCSV in Slicer version 5.4. There is a trailing <code>,2,0</code> written at the end of each data line. These additional columns have not been in previous versions of Slicer and are not defined in the header info. I’ve found the same behavior in Slicer 5.2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93e1c5225be4486275dbde5df91a4f00d1089378.png" data-download-href="/uploads/short-url/l6dTGWGsfyQkNNvvAJqMJf6BvXq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93e1c5225be4486275dbde5df91a4f00d1089378_2_690x139.png" alt="image" data-base62-sha1="l6dTGWGsfyQkNNvvAJqMJf6BvXq" width="690" height="139" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93e1c5225be4486275dbde5df91a4f00d1089378_2_690x139.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93e1c5225be4486275dbde5df91a4f00d1089378_2_1035x208.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93e1c5225be4486275dbde5df91a4f00d1089378.png 2x" data-dominant-color="444C55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×262 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Greydon</p>

---

## Post #2 by @muratmaga (2023-10-19 02:31 UTC)

<p>Fcsv is a legacy format and you should use json to store markups (there should be warning popping up each time when you are saving a markup in fcsv fomrat)</p>
<p>Those two fields store the status of markup point (being editted, missing, not olaced etc) and are necessary.</p>

---

## Post #3 by @Greydon_Gilmore (2023-10-19 02:37 UTC)

<p>I am aware of the switch to <code>mrk.json</code>. However, our lab has many pipelines and datasets implementing this format so we prefer to hold this version stationary for as long as possible.</p>
<p>In future Slicer versions, would it be possible to remove these two additional columns when writing FCSV or update the file header to include the two additional column metadata?</p>

---

## Post #4 by @Greydon_Gilmore (2023-10-19 04:15 UTC)

<p>This change in how Slicer hands FCSV files breaks a previously working file standard. I understand that the majority of users will convert to the new standard but it would be great to have legacy support for previous FCSV files.</p>
<p>Correct if wrong but the behaviors associated with the new columns only occur when the <code>vtkMRMLMarkupsNode</code> is open. I do not see the reason for needing to write them to the FCSV file.</p>

---

## Post #5 by @muratmaga (2023-10-19 04:20 UTC)

<p>It is of course your call, but the longer you hold on more troublesome the transition will be. (we also have thousands of files almost a decade).</p>
<p>I can’t speak for others, but it is unlikely that anyone will spend time doing anything for a format that might be deprecated pretty soon. It is also not that trivial, if we add those two columns in the header then older slicer versions will not be able to read the format. if we do not write it, we will be ignoring information. (these were all the reasons for switch to json, fcsv cannot be expanded easily).</p>
<p>Where are you having trouble reading this files, as far as I know any Slicer would read the fcsv file correctly. If you are trying to read the file to some other software, your best best would ignoring the header and parsing the file.</p>

---

## Post #6 by @muratmaga (2023-10-19 04:32 UTC)

<p>FYI, if you are using any of the status features, FCSV may not be even saving coordinates correctly.<br>
This is what I have in my scene:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb2177b51ec21ec0ce1f076f18194300df44484.png" data-download-href="/uploads/short-url/de1ucc4HomLbA2SIT1PH5hHzjFi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb2177b51ec21ec0ce1f076f18194300df44484_2_690x99.png" alt="image" data-base62-sha1="de1ucc4HomLbA2SIT1PH5hHzjFi" width="690" height="99" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb2177b51ec21ec0ce1f076f18194300df44484_2_690x99.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb2177b51ec21ec0ce1f076f18194300df44484_2_1035x148.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb2177b51ec21ec0ce1f076f18194300df44484_2_1380x198.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1798×260 29.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is what fcsv reports (first and third landmark shouldn’t have any coordinates)</p>
<pre><code class="lang-auto"># Markups fiducial file version = 5.4
# CoordinateSystem = LPS
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
1,-322.5806451612903,-5.684341886080802e-14,-35.993208828522924,0,0,0,1,1,1,0,crossed,,,3,0
2,-517.4872665534805,-5.684341886080802e-14,122.92020373514431,0,0,0,1,1,1,1,locked,,,2,0
3,-361.6298811544991,5.684341886080802e-14,44.82173174872663,0,0,0,1,1,1,0,editing,,,0,0
</code></pre>
<p>this what JSON reports correctly:</p>
<pre><code class="lang-auto">  "@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json#",
    "markups": [
        {
            "type": "Fiducial",
            "coordinateSystem": "LPS",
            "coordinateUnits": "mm",
            "locked": false,
            "fixedNumberOfControlPoints": false,
            "labelFormat": "%N-%d",
            "lastUsedControlPointNumber": 3,
            "controlPoints": [
                {
                    "id": "1",
                    "label": "crossed",
                    "description": "",
                    "associatedNodeID": "",
                    "position": "",
                    "orientation": [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],
                    "selected": true,
                    "locked": false,
                    "visibility": true,
                    "positionStatus": "missing"
                },
                {
                    "id": "2",
                    "label": "locked",
                    "description": "",
                    "associatedNodeID": "",
                    "position": [-517.4872665534805, -5.684341886080802e-14, 122.92020373514431],
                    "orientation": [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],
                    "selected": true,
                    "locked": true,
                    "visibility": true,
                    "positionStatus": "defined"
                },
                {
                    "id": "3",
                    "label": "editing",
                    "description": "",
                    "associatedNodeID": "",
                    "position": "",
                    "orientation": [-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0],
                    "selected": true,
                    "locked": false,
                    "visibility": true,
                    "positionStatus": "undefined"
                }
</code></pre>

---
