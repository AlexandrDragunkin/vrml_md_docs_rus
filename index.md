# ![](./pix/vrmllogo2.0.gif)

# The Virtual Reality Modeling Language

### ISO/IEC DIS 14772-1

This is the VRML/ISO Draft for International Standard
(DIS). This document will be submitted to ISO for a vote.

A [summary of changes](#Summary) is listed
below. See [ftp://ftp.megatek.com/pub/puk/Response.doc](ftp://ftp.megatek.com/pub/puk/Response.doc)
for a Word document that lists most of changes made (warning: this is
a very long document).

**Schedule**

```
22Feb.................Publish Editor's Draft of VRML97 DIS [done]
22Feb-12Mar...........3 week review period (send comments to rikk@best.com) [done]
14Mar.................Freeze the draft (DIS) [done]
6April................Publish DIS and release ISO ballot
~Jul..................ISO vote
~Sept.................Finalize document and publish International Standard (IS)

```

![](./pix/vrmlbar.gif)

This document is the official and complete specificationof the **Virtual Reality Modeling Language**, (VRML), ISO/IEC DIS 14772.

**Background****Clauses****Annexes**![](./pix/cube.gif)[Foreword](part1/foreword.html)![](./pix/cube.gif)
 1 [Scope](part1/scope.md)![](./pix/cube.gif)
 A [Grammar](part1/grammar.md)![](./pix/cube.gif)[Introduction](part1/introduction.html)![](./pix/cube.gif)
 2 [Normative \
 References](part1/references.md)![](./pix/cube.gif)
 B [Java](part1/java.md)![](./pix/cube.gif)
 3 [Definitions](part1/glossary.md)![](./pix/cube.gif)
 C [JavaScript](part1/javascript.md)![](./pix/cube.gif)
 4 [Concepts](part1/concepts.md)![](./pix/cube.gif)
 D [Examples](part1/examples.md)![](./pix/cube.gif)
 5 [Fields and \
 Events](part1/fieldsRef.md)![](./pix/cube.gif)
 E [Bibliography](part1/bibliography.html)![](./pix/cube.gif)
 6 [Nodes](part1/nodesRef.md)![](./pix/cube.gif)
 7 [Conformance](part1/conformance.md)

The **_Foreword_** provides background on the standards process
for VRML. The **_Introduction_** describes the purpose, design
criteria, and characteristics of VRML. The following clauses define the
specifications for VRML ISO/IEC DIS 14772-1:

1. **_Scope_** defines the problem area that VRML addresses.

2. **_References_** lists the normative standards referenced
    in the specification.

3. **_Definitions_** contains the glossary of terminology used
    in the specification.

4. **_Concepts_** describes various fundamentals of VRML.

5. **_Fields_** _**and Events**_ specifies the
    datatypes used by nodes.

6. **_Nodes_** defines the syntax and semantics of VRML nodes.

7. **_Conformance_** describes the minimum support
    requirements for VRML implementations.


There are several annexes included in the specification:

1. **_Grammar_** presents the BNF for the VRML file format.

2. **_Java_** describes how VRML scripting integrates
    with Java.

3. **_JavaScript_** describes how VRML scripting integrates
    with JavaScript.

4. **_Examples_** includes a variety of VRML example files.

5. **_Bibliography_** lists the informative, non-standard
    topics referenced in the specification.


![](./pix/vrmlbar.gif)

## Summary of changes to the spec since August 4th

##### \[Note: Functional changes are in BOLD.\]

#### Overall

1. A large number of typos and document errors have been fixed.

2. ISO document conventions were adopted throughout (due to the fact that
    this is an online HTML document, many of these conventions were ignored
    or interpreted).

3. Field and Event Reference has been moved to Clause 5, and Node
    Reference has been moved to Clause 6.

4. Examples annex has been moved from Annex B to Annex D.

5. Consistent numbering of all sections, subsections, figures, and tables.

6. Annexes (previously called appendices) have been labeled
    "normative" and "informative".

7. Removed non-specification language ( _e.g.,_ user tips)
    throughout.

8. Moved all conformance discussion to Clause 7.


#### Clause 1, Scope

1. This section has been rewritten.


#### Clause 2, Normative References

1. Several new refererences were added.

2. A few references were clarified.


#### Clause 3, Definitions

1. Many new definitions were added.

2. Many definitions were clarified.


#### Clause 4, Concepts

1. This clause has been significantly revised. The order has
    been completely rearranged for better presentation. Several new
    sections have been added and many sections have been clarified.

2. Two new diagrams were added.

3. **\+ and - chararcters are illegal first characters for DEF names.**
4. _children_ exposedFields are order-dependent (previously this
    was undefined).

5. Clarified _ccw_, _solid_, and _creaseAngle_ fields.

6. Prototypes have been significantly re-written for clarity. A variety of
    cases have been clarified ( _e.g.,_ scope of DEF names within
    PROTOs).

7. Lighting model: fixed redundant ambient term, attentuation term, and
    spotlight eqns.

8. Clarified how to interpret various image file formats as texture maps.

9. Field/event names in a ROUTE statement do not require the _set\__
    and \_ _changed_ prefix/suffix. If a field/event name (in a
    ROUTE statement) is not found (e.g. _foo_), browsers
    shall prepend the _set\__ prefix ( _set\_foo_) and append
    the _\_changed_ suffix ( _foo\_changed_) to the name in an
    attempt to check if the user is using the shorthand notation.


#### Clause 6, Nodes Reference

01. Numerous small clarifications and fixes were made throughout.

02. Backgorund: restrict _groundAngle_ field from 0.0 to PI/2, not
     PI(this was an error).

03. Cylinder: fixed error in top and bottom calculations (height/2).

04. CylinderSensor: fixed error in defintion of disk rotation.

05. ElevationGrid: fixed several errors in eqns and clarified all fields.

06. Extrusion: fixed errors and major re-write (including a new
     figure).

07. **FontStyle: changed _family_ field from SFString to MFString**
    **to support orderered list of choices; similar to URL fields.**
08. IndexedFaceSet: fixed errors in the figure.

09. **MovieTexture: changed _duration\_changed_ eventOut from**
    **SFFloat to SFTime to be consistent with AudioClip.**
10. **NavigationInfo: new value for type field "ANY" (means**
    **browser can do whatever it wants. This was added because several**
    **browsers were doing this anyway (misinterpreting the spec) and thus we**
    **needed a mechanism to support the existing policy. This change implies**
    **that the other NavInfo _type_ s are now strictly enforced (see [NavigationInfo](part1/nodesRef.html#NavigationInfo)).**
11. NavigationInfo: Clarified that NavInfo type is restrictive (unless
     "ANY").

12. Sound: the text has been significantly rewritten for accuracy and
     clarity, and a figure has been added.

13. Sound: clarified that the _intensity_ field means audio volume
     or loudness, not the technical term _audio intensity_(which
     implies a perceptual logarithmic volume). Note that light _intensity_
     fields are also based on _perceptual intensity_ not _energy_
    _intensity_--we have tried to design the VRML parameters to be
     perceptual controls in order to make authoring easier. Some VRML
     browsers may need to perform the log conversion before invoking their
     respective audio library.

14. SpotLight: fixed errors in equations.

15. TextureTransform: fixed (reversed) errors in matrix equations (note:
     that some browsers may be implemented this literally and must change).

16. TextureTransform: allow _scale_ values from -infinity to
     +infinity.

17. Transform: clarified that negative scale is undefined.

18. Transform: fixed errors in matrix equations.

19. Transform: fixed typo that allowed zero _scale,_ ( _scale_
     must be > 0.0).

20. Viewpoint: clarified _jump_ = TRUE to mean an instantaneous
     hyperjump.

21. Viewpoint: clarified jump transitions for Anchor, and loadURL().

22. **Viewpoint: fixed error in FOV text; uses minimum angle for FOV,**
    **not maximum.**

#### Clause 7, Conformance and minimum support requirements

1. This clause was re-written.

2. **A variety of additions and changes were made to Annex 7.**
   **Conformance and minimum support requirements; see Table 7-1.**

#### Annex A, VRML Grammar definition

1. **\+ and - chararcters are illegal first characters for DEF names.**

#### Annex B, Java Scripting Reference

1. **A variety of clarifications, fixes, and improvements have been**
   **made. See [http://vs.sme.co.jp/~sugino/vrml2.0/Aug4\_to\_Dec2.txt](http://vs.sme.co.jp/~sugino/vrml2.0/Aug4_to_Dec2.txt)**
   **for some details.**

#### Annex C, JavaScript Scripting Reference

1. **A variety of clarifications, fixes, and improvements have been**
   **made. See [http://www.jch.com/~jch/vrml/jsdeltas.html](http://www.jch.com/~jch/vrml/jsdeltas.html)**
   **for partial list of changes.**

#### Annex D, Examples

1. Many errors have been corrected and links to valid .wrl files have been
    added.


#### Annex E, Bibliography

1. Several new references were added.


#### Annex F, Index

1. Nuked it.


![](./pix/vrmlbar.gif)

```
http://www.vrml.org/Specifications/VRML97/DIS/index.html

```

