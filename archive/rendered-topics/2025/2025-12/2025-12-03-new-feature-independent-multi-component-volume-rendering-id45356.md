---
topic_id: 45356
title: "New Feature Independent Multi Component Volume Rendering"
date: 2025-12-03
url: https://discourse.slicer.org/t/45356
---

# New Feature: Independent Multi-Component Volume Rendering

**Topic ID**: 45356
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/new-feature-independent-multi-component-volume-rendering/45356

---

## Post #1 by @Sunderlandkyl (2025-12-03 17:32 UTC)

<p>3D Slicer can now independently render each component of multi-component volumes (such as 3D color Doppler ultrasound or multispectral microscopy images) in 3D views. A new json-based file format is introduced to store the volume rendering settings.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd4321fee0e293aadd9292cace9912d14530186e.jpeg" data-download-href="/uploads/short-url/thPIbYukGy06ULjSgF6REK3WcFM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd4321fee0e293aadd9292cace9912d14530186e.jpeg" alt="image" data-base62-sha1="thPIbYukGy06ULjSgF6REK3WcFM" width="417" height="315"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">417×315 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b7bd77e6c06a00be910aa5b6fa9855970c3a86a.jpeg" data-download-href="/uploads/short-url/3V8dJm5r0hc3yKr3k0bhFLfdtHA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b7bd77e6c06a00be910aa5b6fa9855970c3a86a.jpeg" alt="image" data-base62-sha1="3V8dJm5r0hc3yKr3k0bhFLfdtHA" width="645" height="402"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">645×402 54.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Development was funded in part by a Children’s Hospital of Philadelphia (CHOP) Cardiac Center Innovation Grant, a CHOP Cardiac Center Research Grant, a CHOP Frontier Grant, NIH R01 HL153166 and T32GM008562.</p>
<h2><a name="p-130360-for-users-1" class="anchor" href="#p-130360-for-users-1" aria-label="Heading link"></a>For users:</h2>
<p>The Volume Rendering module now supports editing of multi-component volume rendering transfer functions.</p>
<p>To access this interface:</p>
<ul>
<li>Open the “Advanced” tab in the volume rendering module</li>
<li>Select “Independent” components</li>
<li>Changing the “Component Index” allows the transfer function for each component to be modified with the transfer function plot.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7654178c2f63b8ae6a117ba5d11dcdaa9e5083e6.png" data-download-href="/uploads/short-url/gSMvtOhTaN2iNRnSBL0ds6QiFo2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7654178c2f63b8ae6a117ba5d11dcdaa9e5083e6.png" alt="image" data-base62-sha1="gSMvtOhTaN2iNRnSBL0ds6QiFo2" width="321" height="365"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">429×487 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c4ec0d7ddb3be0f46aefaf2e881419f65977b98.png" data-download-href="/uploads/short-url/fs8ihPNJVi5xmnLCmGsj9TpaywM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c4ec0d7ddb3be0f46aefaf2e881419f65977b98.png" alt="image" data-base62-sha1="fs8ihPNJVi5xmnLCmGsj9TpaywM" width="315" height="236"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">420×315 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-130360-for-developers-2" class="anchor" href="#p-130360-for-developers-2" aria-label="Heading link"></a>For developers:</h2>
<ul>
<li><strong>Multi-Component Transfer Functions:</strong> The <code> vtkMRMLVolumePropertyNode</code> now fully supports editing and managing transfer functions for volumes with multiple scalar components</li>
<li><strong>New JSON Storage Format:</strong> The new <code>vtkMRMLVolumePropertyJSONStorageNode</code> class enables reading and writing full volume property configurations to JSON files, including:
<ul>
<li>Transfer functions for each component</li>
<li>Lighting parameters</li>
<li>Clipped voxel intensity settings</li>
</ul>
</li>
</ul>
<p>Independent component rendering can be enabled from python using vtkMRMLVolumeRenderingDisplayNode and vtkMRMLVolumePropertyNode:</p>
<pre data-code-wrap="python"><code class="lang-python">volumeNode = slicer.util.getNode('VolumeNode')
displayNode = slicer.modules.volumerendering.logic().CreateDefaultVolumeRenderingNodes(volumeNode)
volumePropertyNode = displayNode.GetVolumePropertyNode()
numberOfComponents = volumeNode.GetImageData().GetNumberOfScalarComponents()
volumePropertyNode.SetNumberOfIndependentComponents(numberOfComponents)
volumeProperty = volumePropertyNode.GetVolumeProperty()

# Enable independent components mode (vs RGB color mode)
# For volumes with 3-4 components, you can choose between:
# - IndependentComponents = False (RGB/RGBA color mode)
# - IndependentComponents = True (independent transfer functions per component)
volumeProperty.SetIndependentComponents(True)

# Configure transfer functions for each component
for component in range(numberOfComponents):
    # Get the color transfer function for this component
    colorTransfer = volumeProperty.GetRGBTransferFunction(component)
    colorTransfer.RemoveAllPoints()
    colorTransfer.AddRGBPoint(0, 0.0, 0.0, 0.0)
    colorTransfer.AddRGBPoint(255, 1.0, 1.0, 1.0)

# Get the opacity transfer function for this component
opacityTransfer = volumeProperty.GetScalarOpacity(component)
opacityTransfer.RemoveAllPoints()
opacityTransfer.AddPoint(0, 0.0)
opacityTransfer.AddPoint(128, 0.5)
opacityTransfer.AddPoint(255, 1.0)

# Configure component-specific shading
volumeProperty.SetShade(component, 1)
volumeProperty.SetAmbient(component, 0.2)
volumeProperty.SetDiffuse(component, 0.7)
volumeProperty.SetSpecular(component, 0.3)
volumeProperty.SetSpecularPower(component, 10.0)
displayNode.SetVisibility(True)
</code></pre>
<h2><a name="p-130360-format-of-vpjson-volume-property-json-3" class="anchor" href="#p-130360-format-of-vpjson-volume-property-json-3" aria-label="Heading link"></a>Format of .vp.json (volume property JSON)</h2>
<p>Since Slicer version 5.9, volume rendering properties are stored in JSON format by default, with the file extension <code>.vp.json</code>. This format is self-describing and easier to interpret than the legacy text file format. Details are specified by this JSON schema: <a href="https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fslicer%2Fslicer%2Fmain%2FModules%2FLoadable%2FVolumeRendering%2FResources%2FSchema%2Fvolume-property-schema-v1.0.0.json&amp;data=05%7C02%7Ckyle.sunderland%40queensu.ca%7C9711180bdc7c4476467308de329119d1%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C639003795956111216%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=qu10rtoL4oc09G0JeHYNSlxDVfnPRZRuV8zrNs5yszQ%3D&amp;reserved=0" rel="noopener nofollow ugc">https://raw.githubusercontent.com/slicer/slicer/main/Modules/Loadable/VolumeRendering/Resources/Schema/volume-property-schema-v1.0.0.json</a></p>
<p>Example <code>.vp.json</code> file:</p>
<pre data-code-wrap="json"><code class="lang-json">{
    "@schema": https://raw.githubusercontent.com/slicer/slicer/main/Modules/Loadable/VolumeRendering/Resources/Schema/volume-property-schema-v1.0.0.json#,
    "volumeProperties": [
        {
            "effectiveRange": [0.0, 220.0],
            "components": [
                {
                    "shade": true,
                    "lighting": {
                        "diffuse": 1.0,
                        "ambient": 0.2,
                        "specular": 0.0,
                        "specularPower": 1.0
                    },
                    "rgbTransferFunction": {
                        "type": "colorTransferFunction",
                        "points": [
                            { "x": 0.0, "color": [0.0, 0.0, 0.0] },
                            { "x": 20.0, "color": [0.168627, 0.0, 0.0] },
                            { "x": 40.0, "color": [0.403922, 0.145098, 0.0784314] },
                            { "x": 40.0, "color": [0.403922, 0.145098, 0.0784314] },
                            { "x": 120.0, "color": [0.780392, 0.607843, 0.380392] },
                            { "x": 220.0, "color": [0.847059, 0.835294, 0.788235] },
                            { "x": 1024.0, "color": [1.0, 1.0, 1.0] }
                        ]
                    },
                    "scalarOpacityUnitDistance": 1.0,
                    "scalarOpacity": {
                        "type": "piecewiseLinearFunction",
                        "points": [
                            { "x": 0.0, "y": 0.0 },
                            { "x": 120.0, "y": 0.3 },
                            { "x": 220.0, "y": 0.375 },
                            { "x": 1024.0, "y": 0.5 }
                        ]
                    },
                    "gradientOpacity": {
                        "type": "piecewiseLinearFunction",
                        "points": [
                            { "x": 0.0, "y": 1.0 },
                            { "x": 255.0, "y": 1.0 }
                        ]
                    }
                }
            ]
        }
    ]
}
</code></pre>

---

## Post #2 by @jcfr (2025-12-05 14:43 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>  Do you think you could add a short note near each images describing which anatomical part are being rendered ? <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=15" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>
<p>We will then update the release note to include the relevant details.</p>
<p>cc: <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/rkikinis">@rkikinis</a></p>

---

## Post #3 by @Sunderlandkyl (2025-12-08 16:50 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I don’t have the ability to edit the post past a few minutes.</p>
<p>I’m not sure what is in the first image, I took it from this post: <a href="https://discourse.slicer.org/t/working-with-rgba-in-volume-rendering/44814/9" class="inline-onebox">Working with RGBA in Volume Rendering - #9 by lassoan</a><br>
<a class="mention" href="/u/muratmaga">@muratmaga</a> or <a class="mention" href="/u/lassoan">@lassoan</a> Could you explain what’s in the image?</p>
<p>The second image is a 2-component volume containing:</p>
<ol>
<li>Heart-valve ultrasound</li>
<li>Doppler volume showing blood flow</li>
</ol>

---

## Post #4 by @muratmaga (2025-12-08 17:44 UTC)

<p>I don’t really know much more than it is a multichannel confocal image of a mouse brain.</p>

---
