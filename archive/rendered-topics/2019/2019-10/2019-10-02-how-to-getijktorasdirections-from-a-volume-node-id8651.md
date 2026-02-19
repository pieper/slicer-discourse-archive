---
topic_id: 8651
title: "How To Getijktorasdirections From A Volume Node"
date: 2019-10-02
url: https://discourse.slicer.org/t/8651
---

# How to GetIJKToRASDirections from a volume node

**Topic ID**: 8651
**Date**: 2019-10-02
**URL**: https://discourse.slicer.org/t/how-to-getijktorasdirections-from-a-volume-node/8651

---

## Post #1 by @Guangshan_Chen (2019-10-02 19:49 UTC)

<p>Dear all,</p>
<p>I would like to get IJKToRASDirections from a node and set IJKToRASDirections to another in python script. But I do not think I get correct one.</p>
<pre><code class="lang-auto">    dirs = [[0] * 3] * 3
    body_roi_labelmap_node.GetIJKToRASDirections(dirs)
    print(dirs)
    copied_labelmap_node.SetIJKToRASDirections(dirs)
</code></pre>
<p>The dirs I got is [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]. The value is same for the three directions.</p>
<p>The corresponding C++ code:</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
void vtkMRMLVolumeNode::CopyOrientation(vtkMRMLVolumeNode *node)
{
  double dirs[3][3];
  node-&gt;GetIJKToRASDirections(dirs);

  int disabledModify = this-&gt;StartModify();
  this-&gt;SetIJKToRASDirections(dirs);
  this-&gt;SetOrigin(node-&gt;GetOrigin());
  this-&gt;SetSpacing(node-&gt;GetSpacing());
  this-&gt;EndModify(disabledModify);
}
</code></pre>
<p>Thanks for any help.</p>

---

## Post #2 by @cpinter (2019-10-02 20:13 UTC)

<aside class="quote no-group" data-username="Guangshan_Chen" data-post="1" data-topic="8651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guangshan_chen/48/4832_2.png" class="avatar"> Guangshan_Chen:</div>
<blockquote>
<p>But I do not think I get correct one</p>
</blockquote>
</aside>
<p>Can you explain why you think that it should not be identity?</p>
<p>If it’s because you put it under a transform, then it’s normal, because the volume itself still has identity directions. You can either set the same transform as parent of the other volume, or you can harden the transform, which will “burn” the matrix in the volume directions and then you can use it the way you want. However, we typically simply use the transform hierarchy and the convenience functions to get the transform between objects when necessary.</p>

---

## Post #3 by @Guangshan_Chen (2019-10-02 21:29 UTC)

<p>it is not identity. The returned value is:<br>
0 0 1<br>
0 0 1<br>
0 0 1</p>

---

## Post #4 by @Guangshan_Chen (2019-10-02 21:35 UTC)

<p>In python script, I could not reproduce the result of<br>
copied_labelmap_node.CopyOrientation(body_roi_labelmap_node) with:</p>
<pre><code class="lang-auto">disableModify = copied_labelmap_node.StartModify()
dirs = [[0] * 3] * 3
body_roi_labelmap_node.GetIJKToRASDirections(dirs)
print(dirs)
copied_labelmap_node.SetIJKToRASDirections(dirs)
copied_labelmap_node.SetOrigin(body_roi_labelmap_node.GetOrigin())
copied_labelmap_node.SetSpacing(body_roi_labelmap_node.GetSpacing())
copied_labelmap_node.EndModify(disableModify)
</code></pre>
<p>The above code is identical to the C++ code of  CopyOrientation.<br>
So the only place could be wrong is where getting GetIJKToRASDirections and SetIJKToRASDirections.</p>

---

## Post #5 by @lassoan (2019-10-03 11:46 UTC)

<aside class="quote no-group" data-username="Guangshan_Chen" data-post="1" data-topic="8651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guangshan_chen/48/4832_2.png" class="avatar"> Guangshan_Chen:</div>
<blockquote>
<p>dirs = [[0] * 3] * 3</p>
</blockquote>
</aside>
<p>This creation of a “matrix” caused the unexpected output: a list was created that referred <em>to the same list</em> 3 times. Effectively, the code did this: <code>dirs = [v,v,v]</code>.</p>
<p>Instead, you need to provide unique values for all the 3x3 values in the matrix. Probably the simplest is to create it as a numpy array: <code>dirs = np.eye(3)</code>.</p>

---

## Post #6 by @Alex_Vergara (2019-10-03 12:13 UTC)

<p>I think what he needs is a zero matrix in which case is <code>dirs = np.zeros([3, 3])</code></p>

---

## Post #7 by @lassoan (2019-10-03 12:55 UTC)

<p>Values will be overwritten anyway by calling <code>GetIJKToRASDirections</code>, so in this specific example, either <code>np.zeros</code> or <code>np.eye</code> works.</p>
<p>However, since a null-matrix is not a valid direction matrix, it is not good practice to store it in a variable called “direction”, even temporarily. <code>np.eye</code> creates an identity matrix, which is what you want as a default direction matrix; and its syntax is a bit simpler than <code>np.zeros</code>, too.</p>

---

## Post #8 by @Guangshan_Chen (2019-10-03 13:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="8651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>dirs = np.eye(3)</p>
</blockquote>
</aside>
<p>Thank you very much. This works.</p>

---
