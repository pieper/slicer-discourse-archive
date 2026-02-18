# RFC: should this method be generally available?

**Topic ID**: 28332
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/rfc-should-this-method-be-generally-available/28332

---

## Post #1 by @chir.set (2023-03-12 17:49 UTC)

<p>To developers.</p>
<p>I am thinking about proposing this <a href="https://github.com/chir-set/SlicerExtraMarkups/blob/0e1309b4d518d903d9d53ada237fcac56c87203a/Shape/MRML/vtkMRMLMarkupsShapeNode.cxx#L331" rel="noopener nofollow ugc">function</a> for inclusion in vtkMath.</p>
<p>It determines a point coordinate along a line defined by p1 and p2, given an offset relative to p2. Basically, it</p>
<ul>
<li>shifts p1 to origin,</li>
<li>determines the resulting p2 (rp2) accounting for this shift,</li>
<li>calculates a linear proportional scale based on lengths,</li>
<li>applies the scale to get the expected coordinate component in each dimension,</li>
<li>reverts the shift.</li>
</ul>
<p>I found it very useful in many places and think that it might be of interest more generally.</p>
<p>Looking forward for your inputs.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2023-03-12 23:13 UTC)

<p>Thanks for considering contributing this to Slicer/vtkAddon. We usually create utility functions for frequent and/or complex operations.</p>
<p>The function you suggest is not a complex operation - it is a single-line operation in Python, single-line operation in C++ if you use VNL or Eigen, and even if you use VTK it is quite short and simple:</p>
<pre><code class="lang-auto">double directionVector[3] = { p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2] };
vtkMath::Normalize(directionVector);
result[0] = p2[0] + lineLength * directionVector[0];
result[1] = p2[1] + lineLength * directionVector[1];
result[2] = p2[2] + lineLength * directionVector[2];
</code></pre>
<p>Still, if this function was used very often then it would make sense to make it a widely available utility function. If you can find at least a few cases anywhere in Slicer code where this utility function would simplify the code (you can find candidates by searching for <code>vtkMath::Normalize(</code> in the Slicer source code) then I think it is a good justification to add it to vtkAddon (using a name like <code>GetPointAlongLine</code>). If it seems that it would not be used at all in Slicer’s relative large code base then it is probably enough to keep it in your module for now.</p>

---

## Post #3 by @chir.set (2023-03-13 10:11 UTC)

<p>Thank you for considering.</p>
<p>Using ‘vtkMath::Normalize’ is indeed an elegant approach to a more <em>professional</em> code style. In your code snippet, ‘linelength’ should nevertheless be replaced by ‘offset’ or ‘difference’ to obtain same results.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="28332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if this function was used very often</p>
</blockquote>
</aside>
<p>‘vtkMath::Normalize’ is used very often in the Slicer code base, I could not go to every place where it is called. I have found only one <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionInteractionRepresentation.cxx#L267" rel="noopener nofollow ugc">instance</a> where this function could have a place.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="28332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you can find at least a few cases</p>
</blockquote>
</aside>
<p>A single case will not justify an addition to vtkAddonMathUtilities. So we may leave things as they are.</p>
<p>Thank you again.</p>

---

## Post #4 by @lassoan (2023-03-13 12:19 UTC)

<p>Maybe what we could add is an <code>AddScaledVector</code> method. That would be less specialized and that could replace 3 lines by a single command at a number of places.</p>
<pre><code class="lang-python">double directionVector[3] = { p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2] };
vtkMath::Normalize(directionVector);
vtkAddonMath::AddScaledVector(result, p2, directionVector, lineLength);
</code></pre>

---

## Post #5 by @chir.set (2023-03-13 13:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="28332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe what we could add</p>
</blockquote>
</aside>
<p>Ok, I’ll bake something and continue in a PR.</p>

---

## Post #6 by @lassoan (2023-03-13 14:11 UTC)

<p>OK. Submit it to vtkAddon, as we maintain general-purpose low-level vector/matrix computation utility functions there. Or maybe you can even try submitting to VTK.</p>

---
