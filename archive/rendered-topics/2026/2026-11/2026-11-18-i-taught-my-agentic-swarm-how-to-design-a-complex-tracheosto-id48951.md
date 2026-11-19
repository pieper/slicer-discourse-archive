---
topic_id: 48951
title: "I taught my agentic swarm how to design a complex tracheostomy tube"
date: 2026-11-18
url: https://discourse.slicer.org/t/48951
last_bumped: 2026-11-18T12:29:25.858Z
---

# I taught my agentic swarm how to design a complex tracheostomy tube

**Topic ID**: 48951
**Date**: 2026-11-18
**URL**: https://discourse.slicer.org/t/i-taught-my-agentic-swarm-how-to-design-a-complex-tracheostomy-tube/48951

---

## Post #1 by @LukaBloomRox (2026-11-18 05:09 UTC)

<p>I wanted to let the community know I have recently accomplished some interesting goals for the little patient with complex Kyphosis and Scoliosis who I support as a tracheostomy tube designer.</p>
<p>I have now taught my AI agent running Claude-5.5 how to replicate the trach tube design process I performed manually with the use of 3D Slicer software three years ago, when I considered several dozen possible designs and manually created a curved centerline approximating the tube we were hoping to order and then extruded it to form a recognizable tube with real width.</p>
<p>Slicer was once again a significantly important part of my workflow, but this time agentically driven.  After having my agent assess several online Slicer skills it chose to create its own that was lean and scoped down to the particular job it needed to do.</p>
<p>Once I taught it my process I had it redo the original design using the same source data but without my manually drawn design to draw from. It considered several thousand designs where it sampled the space of designs that had the chance of being patent, taking tracheal cross sections and scoring the current tube for safety taking into account multiple poses (multiple CT exposures in the variety of positions the patient spends most of her time in).  All designs that had the tip dig into the tracheal wall were disallowed. Designs that resulted in the tube lying against the tracheal wall and spreading the force scored higher. Designs that promoted airspace around and in front of the shaft and distal tip scored highest. I estimated approximate pressure of trach tube sections that touched the tracheal wall, considered that the trachea when subjected to repetitive stress by a current misshapen tube and distended might when that pressure was removed bounce back a little differently on the aspects of the trachea facing and facing away from the spine (anterior and posterior are not appropriate terms for a trachea that more closely resembles a corkscrew, running from front to back instead of up and down for part of its length).  I scored and ranked the designs by a safety metric I calculated. The agent was able to do sub-millimetre analysis subject to the CT scan resolution and several HU thresholding strategies to best estimate the actual air / tracheal wall boundary.</p>
<p>I then had the agent follow the now familiar process to analyze novel data consisting of a series of CT scans recently taken in multiple poses.</p>
<p>I defined my datum as the centrepoint of the circle formed by the intersection of the tube and the skin adjacent flange plane (not wrapped around the neck where they would normally be tied but extending to the side). I defined a point V as the intersection of the normal to the flange plane passing through the datum and the normal to the distal tip plane. I defined a proximal segment from the datum to point V and a distal segment from point V to the center of the distal tip.  I defined the front to back angle as the inside angle formed between the proximal and distal segments. I defined the side angle as the angle between the mid sagittal plane crossing the datum and the distal tip taken from point V. I assumed a curvature pattern with incoming and outgoing clothid curves with a common radius section in between (similar to how an automotive roadway is constructed).</p>
<p>I had my agents create and show me the ranking of the top designs in the various positions by focusing on the safety profile at the distal tip:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/rnz2vslguijjk7ot067cw/candidates_sections.png?rlkey=7x01ykxk4l1h6xyhm2c7tx1gw&amp;st=5soqtjxo&amp;dl=0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c086495bfdff34a838874e415cd8bcef4fc5f56.png" alt="rnz2vslguijjk7ot067cw.png" data-base62-sha1="hHfbEUxu7NVfpWO2Sl2cdTTmh3U" width="300" height="221"></a></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/rnz2vslguijjk7ot067cw/candidates_sections.png?rlkey=7x01ykxk4l1h6xyhm2c7tx1gw&amp;st=5soqtjxo&amp;dl=0" rel="noopener nofollow ugc">candidates_sections.png</a></th>
<th><a href="https://www.dropbox.com/scl/fi/rnz2vslguijjk7ot067cw/candidates_sections.png?rlkey=7x01ykxk4l1h6xyhm2c7tx1gw&amp;st=5soqtjxo&amp;dl=0" rel="noopener nofollow ugc">dropbox.com</a></th>
</tr>
</thead>
</table>
</div><p>And then chose a design that threaded the needle the best.</p>
<p>I then defined an ordering standard with specifics added that our order three years ago was missing and had my agent draft it up:</p>
<p><a href="https://www.dropbox.com/scl/fi/yhllq1jkde4skzgnqdrl1/brief_sheet6_standard.png?rlkey=roou7vw9wj8ln4ozhp21tfzx0&amp;st=7ozx65dq&amp;dl=0" rel="noopener nofollow ugc">Proposed Ordering Standard for Complex Custom Tracheostomy Tube</a></p>
<p>I then had my agents create a rendering in Blender:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/jxrq1jf51fqk2z67kamzu/ordered_design_isometric.png?rlkey=rduj2kwhgc3cn0p5oauhnu79q&amp;st=oan1d5jg&amp;dl=0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b24cd22a4ac6d0b487e71414571a4df2752ca5a9.png" alt="jxrq1jf51fqk2z67kamzu.png" data-base62-sha1="prjzPnHoPViacgy0bOAhbtmttgZ" width="228" height="212"></a></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/jxrq1jf51fqk2z67kamzu/ordered_design_isometric.png?rlkey=rduj2kwhgc3cn0p5oauhnu79q&amp;st=oan1d5jg&amp;dl=0" rel="noopener nofollow ugc">ordered_design_isometric.png</a></th>
<th><a href="https://www.dropbox.com/scl/fi/jxrq1jf51fqk2z67kamzu/ordered_design_isometric.png?rlkey=rduj2kwhgc3cn0p5oauhnu79q&amp;st=oan1d5jg&amp;dl=0" rel="noopener nofollow ugc">dropbox.com</a></th>
</tr>
</thead>
</table>
</div><p>I had my agents create generate 3D slicer segmentations to show two aspects in every supported pose (I manually inspected these and zoomed/panned/rotated to confirm fit):</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/38c2o59mnsz4xplwqhp4b/OrderedDesign_24mm_SupineElevated_front.png?rlkey=ghkz09ah68jvbnsj3mx34zrba&amp;st=fl7h2uty&amp;dl=0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c80ada75f7e1a605e6acee92d6a8b990e337ed6.png" alt="38c2o59mnsz4xplwqhp4b.png" data-base62-sha1="mkub07HfRciLVWzOp8ukkOctxEa" width="228" height="211"></a></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/38c2o59mnsz4xplwqhp4b/OrderedDesign_24mm_SupineElevated_front.png?rlkey=ghkz09ah68jvbnsj3mx34zrba&amp;st=fl7h2uty&amp;dl=0" rel="noopener nofollow ugc">OrderedDesign_24mm_SupineElevated_front.png</a></th>
<th><a href="https://www.dropbox.com/scl/fi/38c2o59mnsz4xplwqhp4b/OrderedDesign_24mm_SupineElevated_front.png?rlkey=ghkz09ah68jvbnsj3mx34zrba&amp;st=fl7h2uty&amp;dl=0" rel="noopener nofollow ugc">dropbox.com</a></th>
</tr>
</thead>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/pcmkkzpw01wwmj1ofjirq/OrderedDesign_24mm_SupineElevated_side.png?rlkey=vmd0rbjqqrfech3ijj8h2bfob&amp;st=y2a8aenc&amp;dl=0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23dbc700bbdec1bee03eedcaf6a609c63c072e46.png" alt="pcmkkzpw01wwmj1ofjirq.png" data-base62-sha1="57dA6gVtUDW7zHZqqd1X5W6RwPQ" width="300" height="270"></a></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th><a href="https://www.dropbox.com/scl/fi/pcmkkzpw01wwmj1ofjirq/OrderedDesign_24mm_SupineElevated_side.png?rlkey=vmd0rbjqqrfech3ijj8h2bfob&amp;st=y2a8aenc&amp;dl=0" rel="noopener nofollow ugc">OrderedDesign_24mm_SupineElevated_side.png</a></th>
<th><a href="https://www.dropbox.com/scl/fi/pcmkkzpw01wwmj1ofjirq/OrderedDesign_24mm_SupineElevated_side.png?rlkey=vmd0rbjqqrfech3ijj8h2bfob&amp;st=y2a8aenc&amp;dl=0" rel="noopener nofollow ugc">dropbox.com</a></th>
</tr>
</thead>
</table>
</div><p>The entire process to train and produce the novel design took place in a contiguous 20 hour session with multiple agents active at once taking care of different defined sub tasks and the total job took approximately $200 CDN to complete.</p>
<p>I feel this was a worthwhile effort and wanted to let you know the details in the spirit of collegial sharing.</p>
<p>Kind regards,<br>
Myles Dear<br>
Ottawa, Ontario, Canada</p>
<p>Engineer and community advocate for the disabled</p>
<p>Nov 17, 2026</p>

---

## Post #2 by @pieper (2026-11-18 12:29 UTC)

<p>Amazing, thank you for the post.</p>

---
