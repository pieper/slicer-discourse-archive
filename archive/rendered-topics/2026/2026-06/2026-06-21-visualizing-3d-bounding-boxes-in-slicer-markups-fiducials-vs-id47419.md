---
topic_id: 47419
title: "Visualizing 3D bounding boxes in Slicer Markups (Fiducials vs Lines) + JSON format question"
date: 2026-06-21
url: https://discourse.slicer.org/t/47419
last_bumped: 2026-06-21T23:19:14.323Z
---

# Visualizing 3D bounding boxes in Slicer Markups (Fiducials vs Lines) + JSON format question

**Topic ID**: 47419
**Date**: 2026-06-21
**URL**: https://discourse.slicer.org/t/visualizing-3d-bounding-boxes-in-slicer-markups-fiducials-vs-lines-json-format-question/47419

---

## Post #1 by @khorlint (2026-06-21 23:19 UTC)

<p><strong>Description:</strong></p>
<p>I am working with 3D Slicer markups to debug an interactive model that uses prompt-based inputs (3D bounding boxes). My goal is to ensure that the voxel → world coordinate transformation is correct and that the prompts being sent to the model correspond exactly to what is visualized in Slicer.</p>
<p>Currently, I generate a markup JSON file from bounding boxes by converting each box into its 8 corner points:</p>
<pre data-code-wrap="python"><code class="lang-python">def bbox_to_points(bbox):
    (x0, x1), (y0, y1), (z0, z1) = bbox

    return [
        (x0, y0, z0),
        (x0, y0, z1),
        (x0, y1, z0),
        (x0, y1, z1),
        (x1, y0, z0),
        (x1, y0, z1),
        (x1, y1, z0),
        (x1, y1, z1),
    ]
</code></pre>
<p>Then I serialize them into a Slicer Markups JSON file:</p>
<pre data-code-wrap="python"><code class="lang-python">def save_prompts_as_json(prompts_dict, affine, out_path):

    control_points = []

    for label, bboxes in (prompts_dict.get("pos_bboxes") or {}).items():
        for idx, bbox in enumerate(bboxes):
            for pt in bbox_to_points(bbox):
                control_points.append({
                    "label": f"BOX-POS-label={label}-idx={idx}",
                    "position": [float(coord) for coord in voxel_to_world(pt, affine)]
                })

    output = {
        "@schema": SCHEMA,
        "markups": [
            {
                "type": "Fiducial",
                "coordinateSystem": "RAS",
                "controlPoints": control_points
            }
        ]
    }

    with open(Path(out_path) / "prompts.json", "w") as f:
        json.dump(output, f, indent=2)
</code></pre>
<p>This works in the sense that all points are correctly displayed in Slicer, and I can verify the coordinate transformations.</p>
<p>However, the bounding box is only visible as 8 independent fiducial points (see the image below, with a sample from <code>Totalsegmentator_dataset_v201</code>). This is sufficient for validation, but not ideal for clear visualization or presentations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97fd6d5366284da2ab0d83c4b85c5608f1f9dcb5.jpeg" data-download-href="/uploads/short-url/lGz3U9PeReWqSwhzy3xeEYLcyBD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97fd6d5366284da2ab0d83c4b85c5608f1f9dcb5_2_690x388.jpeg" alt="image" data-base62-sha1="lGz3U9PeReWqSwhzy3xeEYLcyBD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97fd6d5366284da2ab0d83c4b85c5608f1f9dcb5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97fd6d5366284da2ab0d83c4b85c5608f1f9dcb5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97fd6d5366284da2ab0d83c4b85c5608f1f9dcb5_2_1380x776.jpeg 2x" data-dominant-color="5E5D64"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I would like is either:</p>
<ul>
<li>A way to represent a true 3D bounding box directly in Slicer Markups, or</li>
<li>A way to connect these points with edges (wireframe box) inside Slicer</li>
</ul>
<p>If possible, it would also be very helpful to provide an example of how to implement the line connections between the 8 points (i.e., defining the 12 edges of the bounding box) using Slicer Markups JSON or Python API.</p>
<p><strong>Question:</strong><br>
What is the recommended way to visualize 3D bounding boxes in Slicer Markups for presentation purposes?</p>
<ul>
<li>Is there a supported way to represent a wireframe box directly in Markups JSON?</li>
<li>Or should I construct edges manually using additional markup types?</li>
<li>If so, what would be the cleanest way to extend my current JSON generation approach?</li>
</ul>
<p>Any guidance or example Python code or JSON would be very helpful.</p>

---
