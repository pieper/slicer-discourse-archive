# Json markups colors do not work

**Topic ID**: 35739
**Date**: 2024-04-25
**URL**: https://discourse.slicer.org/t/json-markups-colors-do-not-work/35739

---

## Post #1 by @FatihSogukpinar (2024-04-25 19:24 UTC)

<p>Hi all,</p>
<p>I am trying to show a bunch of markup points using json file. The points are being loaded, and their positions are correct. However, I am also trying to set their colors and sizes, but somehow, slicer uses the default color and size. It is as if the colors and sizes I set in json do not have an effect at all…</p>
<p>I am using Slicer 5.6.2 and Json scheme here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json</a></h4>


      <pre><code class="lang-json">    {
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": "https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-v1.0.3-schema.json#",
        "type": "object",
        "title": "Schema for storing one or more markups",
        "description": "Stores points, lines, curves, etc.",
        "required": ["@schema", "markups"],
        "additionalProperties": true,
        "properties": {
            "@schema": {
                "$id": "#schema",
                "type": "string",
                "title": "Schema",
                "description": "URL of versioned schema."
            },
            "markups": {
                "$id": "#markups",
                "type": "array",
                "title": "Markups",
                "description": "Stores position and display properties of one or more markups.",
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Does anyone have any idea about what might be going on ?<br>
Would a mismatch in versions cause this ? I assume if my json file format was totally wrong, the positions would be wrong too, not just colors and sizes.</p>
<p>Thanks a lot !!<br>
Fatih.</p>

---

## Post #2 by @muratmaga (2024-04-25 19:29 UTC)

<p>I can’t replicate this in 5.6.2. PointList markup load exactly with the color I specified. I suspect your JSON is incorrect somehow.</p>
<p>Perhaps work of an example you saved directly from Slicer?</p>

---

## Post #3 by @FatihSogukpinar (2024-04-25 20:16 UTC)

<p>Thank you ! I am trying it.</p>
<p>Just to make sure: With the correct json file, I should be able to adjust the colors of markups such that, I am using a continuous colorbar for hundreds of points, right ?<br>
I mean, I am not forced to use the same color for all markup points when I use json, right ?</p>
<p>Thanks!</p>

---

## Post #4 by @muratmaga (2024-04-25 20:26 UTC)

<aside class="quote no-group" data-username="FatihSogukpinar" data-post="3" data-topic="35739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>I mean, I am not forced to use the same color for all markup points when I use json, right ?</p>
</blockquote>
</aside>
<p>All the control points in a markup node (whether it is a curve or pointlist) will have the same color.</p>
<p>From a different thread, I saw that it is possible to write a JSON file that will have multiple markup nodes. that way you can create one node for every point and have full control over its colors. But you have to do it yourself.</p>
<p>I couldn’t find the thread (I am really no happy with the search on discourse), but it was last week, someone was asking a similar thing.</p>

---

## Post #5 by @lassoan (2024-04-25 22:39 UTC)

<p>Markup control points all displayed with the selected or unselected color. I would not recommend to add a new markup node for each point for performance reasons. If you want to assign an individual color to each point then you can do it with a model node.</p>
<p>It woild not be hard at all to color control points by a data array, but it has not been requested yet.</p>

---

## Post #6 by @FatihSogukpinar (2024-04-26 15:58 UTC)

<p>Thanks a lot for helpful comments !</p>
<p>How about simply creating many different json files, one for each markup point, with its corresponding color, size, etc. properties ? I know it sounds odd. But I don’t know how to do it the way <a class="mention" href="/u/lassoan">@lassoan</a> described:</p>
<blockquote>
<p>Blockquote<br>
If you want to assign an individual color to each point then you can do it with a model node.</p>
</blockquote>
<p>Also, I think it could be useful to have this feature in Slicer. I don’t know if I we are the only ones who use Slicer to display brain electrophysiology recordings and activity, but indeed we frequently need to show different subset of points with different display properties, and sometimes we also need to change display properties in a continuous manner, as in this case.</p>
<p>Thanks a lot,<br>
Fatih.</p>

---

## Post #7 by @muratmaga (2024-04-26 17:00 UTC)

<aside class="quote no-group" data-username="FatihSogukpinar" data-post="6" data-topic="35739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>How about simply creating many different json files, one for each markup point, with its corresponding color, size, etc. properties ? I know it sounds odd. But I don’t know how to do it the way <a class="mention" href="/u/lassoan">@lassoan</a> described:</p>
</blockquote>
</aside>
<p>Depends on how many you have, if you have hundreds your scene fill get bogged down, and interactions will be too slow.</p>
<p>You can convert the markups to models (3d spheres), see the example here:<br>
<a href="https://github.com/SlicerMorph/Scripts?tab=readme-ov-file#3-turn-landmarks-into-3d-sphere-models">SlicerMorph/Scripts (github.com)</a></p>
<p>You can modify the script to change their color properties…</p>

---

## Post #8 by @FatihSogukpinar (2024-04-28 16:06 UTC)

<p>Thanks!</p>
<p>To be able able to run these python scripts, do I need to run them using Slicer python extension? Or should I save the control points in a way that allows this script to work?</p>
<p>Thanks a lot,<br>
Fatih</p>

---

## Post #9 by @muratmaga (2024-04-28 17:37 UTC)

<p>Create your points. And copy paste the script into the python console. You may need to change the pointList name to match it to the script one (F)</p>

---
