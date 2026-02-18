# Python wrappers for a templated class derived from vtkMRMLNode

**Topic ID**: 26238
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/python-wrappers-for-a-templated-class-derived-from-vtkmrmlnode/26238

---

## Post #1 by @adeguet1 (2022-11-14 16:29 UTC)

<p>Hello,</p>
<p>I’m trying to figure out if I can use C++ templates for a vtkMRMLNode.  My current implementation has the following classes (pseudo-code):</p>
<pre><code class="lang-auto">/// generic base class so I can have containers of all my nodes
class vtkMRMLMyBaseNode: public vtkMRMLNode
{
public:
   virtual void MyMethod(void) = 0;
};

/// templated class
template &lt;typename _some_type&gt;
class vtkMRMLMyTemplatedNode: public vtkMRMLMyBaseNode
{
public:
  void GetValue(_some_type &amp; result) const;
}

/// my template specialization:
typedef vtkMRMLMyTemplatedNode&lt;double&gt; vtkMRMLMyDoubleNode ;
</code></pre>
<p>Note that I skipped the code to support ::New(), hidden constructor and destructor, etc for conciseness.   At that point I can create nodes using the specialized types in C++.  I can see the nodes in the MRML scene but I run into a small (and expected) issue with the python interpreter.  When I retrieve the node, I get the correct type but I can only access the methods from the MyBase class (MyMethod) but not the methods from the templated class (GetValue).  I expected this to happen this I never “indicated” that the wrapping process should create wrappers for my specialization (aka typedef).  I used SWIG in the past and needed to explicitly call %template.  Is there an equivalent in VTK/Slicer to explicitly require wrappers for a template specialization?</p>

---

## Post #2 by @lassoan (2022-11-14 20:50 UTC)

<p>VTK classes are wrapped with the VTK Python wrapper. This wrapper does not support templates in the public interface of the class (with a few very specific exceptions). You need to move any templated methods to private implementation an you can use VTK objects to get/set values of any type (e.g., vtkVariant for a single value VTK data arrays for efficient, zero-copy transfer of large arrays of any type).</p>

---
