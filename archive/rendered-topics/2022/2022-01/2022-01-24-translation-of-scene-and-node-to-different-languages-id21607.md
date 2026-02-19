---
topic_id: 21607
title: "Translation Of Scene And Node To Different Languages"
date: 2022-01-24
url: https://discourse.slicer.org/t/21607
---

# Translation of "scene" and "node" to different languages

**Topic ID**: 21607
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/translation-of-scene-and-node-to-different-languages/21607

---

## Post #1 by @lassoan (2022-01-24 23:18 UTC)

<p>Moving a <a href="https://crowdin.com/project/slicer/discussions/3#33">discussion that we started on crowdin</a> to this forum for better visibility and to include more people.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/14733716/medium/4245397b99d0b13bc8813fc20121ca24.jpg" alt="Andras Lasso" title="Andras Lasso" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/lassoan">Andras Lasso</a></p>
<p>2 days ago</p>
<p>We have found it difficult to translate “scene” and “node” to Hungarian. The problem is that the English terms are not the best. Scene and node are computer graphics terms, referring to the scene graph and nodes in this graph. These are not terms that our model user (medical student) would know or understand.</p>
<p>What do you think about using these terms as basis of translations?</p>
<ol>
<li>Use <strong>workspace</strong> instead of scene</li>
</ol>
<p>Examples:</p>
<ul>
<li>Close scene → Close workspace</li>
<li>Save scene and unsaved data → Save workspace and unsaved data</li>
<li>Add data into the scene → Add data into the workspace</li>
<li>Save the entire scene, with all data and display settings embedded in private fields → Save the entire workspace, with all data and display settings embedded in private fields</li>
</ul>
<ol start="2">
<li>Use <strong>item</strong> instead of node</li>
</ol>
<p>Examples:</p>
<ul>
<li>Select views in which to show this node. → Select views in which to show this item.</li>
<li>Resample a curve and optionally constrain the points to a node → Resample a curve and optionally constrain the points to another item</li>
<li>Overwrite current node → Overwrite current item</li>
<li>Select views in which to show this node. → Select views in which to show this item.</li>
<li>Output node: → Output item:</li>
<li>Color node: → Color item: and even considering changing this in the English user interface.</li>
</ul>
<p>If we all agree that these terms work well then we may even change them in the English user interface.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/15112075/medium/6632070822eebc2cd55f961cc1dc2a97.png" alt="Andrey Fedorov" title="Andrey Fedorov" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/andrey.fedorov">Andrey Fedorov (andrey.fedorov)</a></p>
<p>3 hours ago</p>
<p>If the English user interface is changed, would this mean names of the classes that use “Scene” will also need to be changed?</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/14733716/medium/4245397b99d0b13bc8813fc20121ca24.jpg" alt="Andras Lasso" title="Andras Lasso" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/lassoan">Andras Lasso</a></p>
<p>2 hours ago</p>
<p>It would only affect the user interface for now.</p>
<p>I don’t know how much of a problem it will cause for developers that words on the user interface are not the same as in the source code. We would probably still talk about “nodes”, because “items” are just not too specific. I can imagine replacing “scene” by “workspace” in a few years in the source code, too, because “workspace” just so much better describes what it is.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/15112075/medium/6632070822eebc2cd55f961cc1dc2a97.png" alt="Andrey Fedorov" title="Andrey Fedorov" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/andrey.fedorov">Andrey Fedorov (andrey.fedorov)</a></p>
<p>an hour ago</p>
<p>I know I have a tendency of over-complicating things, but I don’t think it’s an easy decision. Yes, maybe for the existing developers it is not a big deal, but for new developers - it might be. There is also a consideration for the variety of known and unknown learning materials that will not be possible to update. I would be very very cautious with changing terminology in the interface. I agree the choices may not have always been optimal, but maybe it is better to deal with that legacy than with the consequences of renaming. I wonder what other developers and users think about this.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/15110441/medium/77753078b93d87bf9a7cc0e4e78685fe.png" alt="Attila Nagy" title="Attila Nagy" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/acetylsalicyl">Attila Nagy (acetylsalicyl)</a></p>
<p>an hour ago</p>
<p>“Workspace” and “item” are both very good substitutions for the terms currently used in Slicer. Better describe what they are, and are easier to translate.</p>
<p>Andrey has a point too. On the other hand, software, the people who use them, and the world, in general, is constantly changing.</p>
<p>We could document this transition in the Slicer documentation, and move forward. I do know from my own experiences how hard it is to describe what a node or a volume is. We can just create a “glossary” of new and old terms, and point users to that. It even could make sense in retrospect. (ie where they see “node” they can think "aha, that’s not some technospeak, it’s just an “item”)</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/14733716/medium/4245397b99d0b13bc8813fc20121ca24.jpg" alt="Andras Lasso" title="Andras Lasso" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/lassoan">Andras Lasso</a></p>
<p>27 minutes ago</p>
<p>I would not worry about developers, as we already deal with many equivalent terms (model=surface=mesh=polydata, etc). For users, it may take some effort to unlearn some some “Slicerisms”, but if we switch to simpler, commonly used terms then this should be easy.</p>
<p>Of course we would need to hear opinion from more users before making any sweeping changes.</p>

---

## Post #2 by @muratmaga (2022-01-24 23:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="21607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Use <strong>workspace</strong> instead of scene</p>
</blockquote>
</aside>
<p>We have been struggling with this for many years when we train biologists. Our solution was to say that a Slicer scene is equivalent to a workspace or a project in other programs, and it may consist of many nodes of different types.</p>
<p>I will wholeheartedly agree to this change.</p>

---

## Post #3 by @jamesobutler (2022-01-24 23:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="21607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Use <strong>workspace</strong> instead of scene</p>
</blockquote>
</aside>
<p>I absolutely agree that “workspace” is a better term. It more closely aligns to terms some academic researchers see such as MATLAB having “workspace” area. It also has made its way as a term for developers since it is used in IDE code workspace areas.</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="21607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Use <strong>item</strong> instead of node</p>
</blockquote>
</aside>
<p>“Node” is the most egregious term that regular people do not know what it means. We’ve attempted to strip all usage of it in our custom application that regular biologists use. We have in the Slicer GUI tried to avoid using this term by saying “Create Point List” instead of “Create Point List Node”. When the specific term is used, it is unnecessary to also say the general term afterwards. <strong>Be succinct.</strong> Also, saying “Overwrite current item” is fine, however when there is only 1 type of item we should be specific and say “Overwrite current Volume” or whatever type it may be. <strong>Be specific.</strong></p>
<p>Using the general term “item” is definitely easier to understand for regular people and Slicer should aim to cater to these people to increase the number of users and therefore funding. I have often told people “node” meant the same as an “object”, but “item” can probably work too.</p>
<p>I will point out one weird location where “Subject Hierarchy Node” becoming “Subject Hierarchy Item” with this terminology change will have conflict with the already used “Subject Hierarchy Item” which is its own thing. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>.</p>

---

## Post #4 by @mikebind (2022-01-25 04:05 UTC)

<p>+1 for <strong>workspace</strong> to replace <strong>scene</strong>.  Much better term and no downsides that I can think of.</p>
<p>I realize this seems to be a minority opinion, but I like the term <strong>node</strong> much better than <strong>item</strong>.  To me “item” sounds like a thing on a list.  I like that the MRML thing is always called a “node”, and I think of it as like a container for the kind of thing it is for.  So, a scalar volume node is the MRML container for a scalar image volume.  A “scalar image item” sounds like a sub-part of a scalar image, not a thing which contains a scalar image. And, a “display node” would need to become a “display item”?  That seems much worse. “Node” correctly carries the connotation that it can be connected with other nodes, like an image or model node with a display node.</p>
<p>I would prefer <strong>object</strong> to <strong>item</strong> in essentially all cases. I can see where <strong>object</strong> would be a more meaningful generic term to many people than <strong>node</strong>.</p>

---

## Post #5 by @cpinter (2022-01-25 09:18 UTC)

<p>Workspace, absolutely.</p>
<p>Item is also good, especially considering that in the Data tree (i.e. Subject hierarchy) we already call the “entries” items, and this way the correspondence would be complete, and confusion less. Also, everybody knows what an item is, but node is something that some people have never heard of (I probably only did because of my university math classes).<br>
The problem with “node” is that although it is concise and sounds cool in English, in other languages (Hungarian definitely) it is almost impossible to translate in a way that people could make sense of.<br>
I understand the points of <a class="mention" href="/u/mikebind">@mikebind</a> , and for example display item is quite bad. So <strong>object</strong> may actually be better than item considering everything (the SH terms are mostly technical and there is usually a 1:1 correspondence between item and node so it’s not a big problem).</p>

---

## Post #6 by @pieper (2022-01-25 13:51 UTC)

<p>Node is arguably the technically correct term, in the sense that MRML references form graph structures and the word node has a long history for things like lymph nodes and nodes in a transportation system.  I know we are trying to make concepts simpler for new users, but part of goal should also be to suggest to them important concepts about Slicer, like the fact that nodes are part of references networks.  Of the two alternatives I do like object better than item.</p>

---

## Post #7 by @lassoan (2022-01-25 14:04 UTC)

<p>I agree that “object” seems to work better overall than “item”, because “object” is a bit more specific, but still understandable.</p>
<p>“Node” of a “scene graph” are proper but very specialized computer graphics terms. Such implementation details should not leak to the user interface that is intended for clinicians. Even ParaView, which is an engineering software, uses simpler, generally understandable terms - “data objects” and “geometric shapes” - to refer to items in their data tree.</p>
<p>The main goal is not to change the English GUI now, but at least we should not make the same mistakes again when choosing the terms in other languages.</p>

---
