# Howto delete all nodes by 'nodeName*'?

**Topic ID**: 23423
**Date**: 2022-05-14
**URL**: https://discourse.slicer.org/t/howto-delete-all-nodes-by-nodename/23423

---

## Post #1 by @jumbojing (2022-05-14 04:30 UTC)

<p>我想删除所有的nodes通过<code>nodeName*</code> 或者 slicer.util.getNodes(‘x*’), 我该咋做呢?</p>
<blockquote>
<ul>
<li><strong>注意⚠️</strong>:  其中有同名的node</li>
</ul>
</blockquote>
<blockquote>
<p>I want to delete all nodes via ‘nodeName*’ or <code>slicer.util.getNodes('x*')</code>, what should I do?</p>
<ul>
<li><strong>Note⚠️</strong>: There are some nodes with the same nodeName</li>
</ul>
</blockquote>

---

## Post #2 by @lassoan (2022-05-14 22:28 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="1" data-topic="23423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>There are some nodes with the same nodeName</p>
</blockquote>
</aside>
<p>For this reason, I would recommend to never identify nodes by name (except for testing and debugging).</p>
<p>You can keep track of your nodes by storing the node object or node ID when you create the node. You can also get the list of all nodes, iterate through them and decide for each if you want to delete it.</p>

---

## Post #3 by @jumbojing (2022-05-16 04:40 UTC)

<pre data-code-wrap="pytthon"><code class="lang-nohighlight">nodes = slicer.util.getNodes(nodeName,useLists=True)
if len(nodes) == 0:
  print(f"no found a node named '{nodeName}' in the scene")
  return 0
else:
  for key in nodes.keys():
    for modNode in nodes[key]:
      slicer.mrmlScene.RemoveNode(modNode)
</code></pre>
<p>似乎像👆🏻这样可以奏效…</p>
<p>Seems like <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> those codes could work…</p>

---
