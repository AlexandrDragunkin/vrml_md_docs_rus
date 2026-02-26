# ![](../pix/vrmllogo2.0.gif)

# The Virtual Reality Modeling Language

# 3\. Definitions

### ISO/IEC DIS 14772-1

#### 4 April 1997

![](../pix/vrmlbar.gif)

### 3.1 activate

To cause a [_sensor node_](#SensorNode) to generate an
"isActive" [_event_](#Event). The various
types of sensor nodes are "activated" by [_user_](#User)
interactions, the passage of [_time_](#Time), or other
events. Only active sensors affect the [_user's_](#User)
experience. A Script [_node_](#Node) is activated when
it receives an event. A pointing device such as a [_mouse_](#Mouse)
is activated when one of its buttons is depressed by a user. See " [4.12.2 Script Execution](concepts.md#4.12.2)"
for details.

### 3.2 ancestor

A [_node_](#Node) which contains one or more [_children nodes_](#ChildrenNode). A [_grouping node_](#GroupingNode).

### 3.3 author

Person or agent that creates [_VRML files_](#VRMLFile).
Authors typically utilize [_generators_](#Generator) to
assist them.

### 3.4 authoring tool

See [_generator_](#Generator).

### 3.5 avatar

The abstract representation of the [_user_](#User) in a
VRML [_world_](#World). The physical dimensions of the
avatar are used for collision detection and terrain following. See
" [6.29 NavigationInfo](nodesRef.md#NavigationInfo)"
for details.

### 3.6 bearing

A straight line passing through the [_pointer_](#Pointer)
location in the direction of the pointer. If multiple sensors'
geometry intersect this line, only the sensor nearest the viewer will
be eligible to generate [_events_](#Event) regardless
of material and texture properties (e.g., transparency).

### 3.7 binding node

A [_node_](#Node) which may have many [_instances_](#Instance) in a [_scene_\
_graph_](#SceneGraph), but only one instance may be active at any instant of [_time_](#Time). A node of type Background, Fog,
NavigationInfo, or Viewpoint. See " [4.6.10 Bindable children nodes](concepts.md#4.6.10)"
for details.

### 3.8 browser

A computer program which interprets [_VRML files_](#VRMLFIle)
, presents their content to a [_user_](#User) on a [_display device_](#DisplayDevice), and allows the user
to interact with [_worlds_](#World) defined by VRML
files by means of a user interface.

### 3.9 browser extension

[_Nodes_](#Node) defined using the prototyping
mechanism which are understood only by certain [_browsers_](#Browser).
See " [4.9.3 Browser Extensions](concepts.md#4.9.3)"
for details.

### 3.10 built-in node

A node of a [_type_](#NodeType) explicitly defined in
this standard.

### 3.11 callback

A function defined in a [_scripting_\
_language_](#ScriptingLanguage) to which [_events_](#Event) are
passed. See " [4.12.8 EventIn handling](concepts.md#4.12.8)"
for details.

### 3.12 candidate

One of potentially several choices. The [_user_](#User)
or the [_browser_](#Browser) will select none or one
of the choices when all candidates are identified. See " [4.6.10 Bindable children nodes](concepts.md#4.6.10)"
and " [6.2 Anchor](nodesRef.md#Anchor)" for
details.

### 3.13 child

A direct [_descendent_](#Descendent).

### 3.14 children node

[_Node_](#Node) which may be parented by a [_grouping node_](#GroupingNode) and is affected by the
transformations of all [_ancestors_](#Ancestor). See
" [4.6.5 Grouping and children nodes](concepts.md#4.6.5)"
for list of allowable children nodes.

### 3.15 client system

A computer system , attached to a [_network_](#Network),
which relies on another computer (the server) for essential processing
functions. Many client systems also function as stand-alone computers.

### 3.16 collision proxy

A [_node_](#Node) used as a substitute for all of a
Collision node's children during collision detection. See " [6.8 Collision](nodesRef.md#Collision)" for
details.

### 3.17 colour model

Characterization of a colour space in terms of explicit parameters.
VRML allows colours to be defined only with the RGB colour model.
However, colour interpolation is performed in the HSV colour space.

### 3.18 culling

The process of identifying [_objects_](#Object) or
parts of objects which do not need to be processed further by the [_browser_](#Browser) in order to produce the desired
view of a [_world_](#World).

### 3.19 descendent

A [_node_](#Node) in a [_scene_\
_graph_](#SceneGraph) which has a parent. See [_children_\
_node_](#ChildrenNode).

### 3.20 display device

A graphics device on which VRML [_worlds_](#World) may
be rendered.

### 3.21 drag sensor

A [_pointing device sensor_](#PointingDeviceSensor)
which causes [_events_](#Event) to be generated in
response to sensor-dependent pointer motions. For example, the
SphereSensor generates spherical rotation events. A [_node_](#Node)
of type CylinderSensor, PlaneSensor, or SphereSensor. See " [4.6.7 Sensor nodes](concepts.md#4.6.7)" and
" [4.6.7.4 Drag sensors](concepts.md#4.6.7.4)"
for details.

### 3.22 element

The smallest unit into which an [_object_](#Object) may
be divided. For example, the header record of a [_VRML_\
_file_](#VRMLFile) or a single value of a multi-valued [_field_](#Field).

### 3.23 environmental sensor

Environmental sensor [_nodes_](#Node) generate [_events_](#Event) based on the location of the viewpoint
in the world or in relation to [_objects_](#Object) in
the world. The TimeSensor node generates events at regular intervals in [_time_](#Time). A node of type Collision,
ProximitySensor, TimeSensor, or VisibilitySensor. See " [4.6.7.2 Environmental sensors](concepts.md#4.6.7.2)"
for details.

### 3.24 event

A [_message_](#Message) sent from one [_node_](#Node)
to another as defined by a [_Route_](#Route). [_Events_](#Event) signal external stimuli, changes to [_field_](#Field) values, and interactions between nodes.
An event consists of a [_time stamp_](#TimeStamp) and a
field value.

### 3.25 event cascade

A sequence of [_events_](#Event) initiated by a script
or sensor event and propagated from [_node_](#Node) to
node along one or more [_routes_](#Route). All events
in an event cascade are considered to have occurred simultaneously. See
" [4.10.3 Execution model](concepts.md#4.10.3)"
for details.

### 3.26 eventIn

A logical receptor attached to a [_node_](#Node) which
receives [_events_](#Event).

### 3.27 eventOut

A logical output terminal attached to a [_node_](#Node)
from which [_events_](#Event) are sent. The eventOut
also stores the event most recently sent.

### 3.28 execution model

The rules governing how [_events_](#Event) are
processed by [_browsers_](#Browser) and scripts.

### 3.29 exposed field

A [_field_](#Field) which is capable of receiving [_events_](#Event) via an eventIn to change its value(s),
and generating events via an eventOut when its value(s) change.

### 3.30 external prototype

A [_prototype_](#Prototype) defined in an external file
and referenced by a [_URL_](#URL).

### 3.31 field

A property or attribute of a [_node_](#Node). Each [_node type_](#NodeType) has a fixed set of fields.
Fields may contain various kinds of data and one or many values.

### 3.32 field name

The name of a [_field_](#Field). Field names are unique
within the scope of the [_node_](#Node).

### 3.33 file format

A detailed description of digital data which is typically stored in a
computer-based file system.

### 3.34 frame

A single rendering of a [_world_](#World) on a [_display device_](#DisplayDevice) or a single time-step
in a simulation.

### 3.35 generator

A computer program which creates [_VRML files_](#VRMLFile).
A generator may be used by a person or operate automatically.

### 3.36 geometric property node

A [_node_](#Node) defining the properties of a specific
geometry node. A node of type Color, Coordinate, Normal, or
TextureCoordinate. See " [4.6.3.2 Geometric property nodes](concepts.md#4.6.3.2)"
for details.

### 3.37 geometric sensor node

A [_node_](#Node) which generates [_events_](#Event)
based on [_user_](#User) actions, such as a [_mouse_](#Mouse) click or navigating close to a
particular [_object_](#Object). A node of type
CylinderSensor, PlaneSensor, ProximitySensor, SphereSensor,
TouchSensor, VisibilitySensor, or Collision. See " [4.6.7.1 Sensor nodes introduction](concepts.md#4.6.7.1)"
for details.

### 3.38 geometry node

A [_node_](#Node) containing mathematical descriptions
of three-dimensional (3D) points, lines, surfaces, text strings and
solids. A node of type Box, Cone, Cylinder, ElevationGrid, Extrusion,
IndexedFaceSet, IndexedLineSet, PointSet, Sphere, or Text. See " [4.6.3 Shapes and geometry](concepts.md#46.3)"
for details.

### 3.39 grab

To receive [_events_](#Event) from the pointing device ( [_mouse_](#Mouse) or [_wand_](#Wand)). A [_pointing device sensor_](#PointingDeviceSensor) becomes
the exclusive recipient of pointing device events when the pointing
device is activated while indicating A [_descendent_](#Descendent)
geometry nodes which are children of the sensor's parent group.

### 3.40 gravity

The force which causes masses to be attracted to one another. In the
context of this standard, gravity may be simulated by constraining the
motion of the viewpoint to the lowest possible path (smallest y
coordinate in the local coordinate system of the viewpoint) consistent
with following the surface of encountered objects. See " [6.29 NavigationInfo](nodesRef.md#NavigationInfo)"
for details.

### 3.41 grouping node

A [_node_](#Node) which collects [_children nodes_](#ChildrenNode) and other grouping
nodes together and causes the group to exhibit specific behaviour which
is dependent on the [_Node type_](#NodeType). A node of
type Anchor, Billboard, Collision, Group, or Transform. See " [4.6.5 Grouping and children nodes](concepts.md#4.6.5)"
for details.

### 3.42 HSV

Hue, Saturation, and Value colour model. See [E.\[FOLE\]](bibliography.md#[FOLE]).

### 3.43 HTML

HyperText Markup Language. See [2.\[HTML\]](references.md#[HTML]).

### 3.44 hyperlink

A reference to a [_URL_](#URL) which is associated with
an Anchor node. See " [6.2 Anchor](nodesRef.md#Anchor)"
for details.

### 3.45 ideal VRML implementation

An implementation of VRML which presents all [_objects_](#Object)
and simulates movement without approximation. Not realizable in
practice.

### 3.46 IEC

International Electrotechnical Commission. See [`http://www.iec.ch`](http://www.iec.ch).

### 3.47 IETF

Internet Engineering Task Force. The organization which develops [_Internet_](#Internet) standards. See [`http://www.ietf.org/overview.html`](http://www.ietf.org/overview.html).

### 3.48 image

A two-dimensional (2D) rectangular array of pixel values. Pixel values
may have from one to four components. See " [5.5 SFImage](fieldsRef.md#SFImage)" for details.

### 3.49 in-lining

The mechanism by which one [_VRML file_](#VRMLFile) is
hierarchically included in another.

### 3.50 Internet

The world-wide named [_network_](#Network) which
communicate with each other using a common set of communication
protocols known as TCP/IP. See [_IETF_](#IETF). The [_World Wide Web_](#WorldWideWeb) is implemented on the
Internet.

### 3.51 instance

A reference to a previously defined and named [_node_](#Node)
via the USE syntax. Nodes are named by means of the DEF syntax.
Instances of nodes may be used in any context in which the defining
node may be used.

### 3.52 interpolator node

A [_node_](#Node) which defines a piece-wise linear
interpolation of a particular type of value at specified [_times_](#Time). A node of type ColorInterpolator,
CoordinateInterpolator, NormalInterpolator, OrientationInterpolator,
PositionInterpolator, or ScalarInterpolator. See " [4.6.8 Interpolators](concepts.md#4.6.8)" for
details.

### 3.53 intranet

A private [_network_](#Network) which uses the same
protocols and standards as the [_Internet_](#Internet).

### 3.54 ISO

International Organization for Standardization. See [`http://www.iso.ch/infoe/intro.html`](http://www.iso.ch/infoe/intro.html).

### 3.55 JPEG

Joint Photographic Experts Group. See [2.\[JPEG\]](references.md#[JPEG]).

### 3.56 JTC 1

Joint Technical Committee 1. See [`http://www.iso.ch/meme/JTC1.html`](http://www.iso.ch/meme/JTC1.html).

### 3.57 level of detail (LOD)

The amount of detail or complexity which is displayed at any particular [_time_](#Time) for any particular [_object_](#Object).
The level of detail for an object is controllable as a function of the
distance of the object from the viewer. See " [6.26 LOD](nodesRef.md#LOD)" for details.

### 3.58 LOD

Level Of Detail.

### 3.59 line terminator

A character (or sequence of two characters) used to terminate a line in
a [_VRML file_](#VRMLFile). Specifically, one or both
of the [_UTF-8_](#UTF-8) characters
"carriage-return" and "linefeed". If both
characters are present either may be first in the sequence.

### 3.60 loop

A sequence of [_events_](#Event) that results in an
event being logically reponsible for generating itself. See " [4.10.4 Loops](concepts.md#4.10.4)" for details.

### 3.61 message

A string sent between [_nodes_](#Node) upon the
occurrence of an [_event_](#Event). See " [4.10 Event processing](concepts.md#4.10)"
for details.

### 3.62 MIDI

Musical Instrument Digital Interface. A standard for digital music
representation. See [2.\[MIDI\]](references.md#[MIDI]).

### 3.63 MIME

Multipurpose Internet Mail Extension. Used to specify filetyping rules
for [_Internet_](#Internet) applications, including [_browsers_](#Browser). See " [4.5.1 File extension and MIME types](concepts.md#4.5.1)"
for details. See also [2.\[MIME\]](references.md#[MIME]).

### 3.64 mouse

A 2D pointing device which enables a [_user_](#User) to
move a cursor on a display device in order to point at displayed [_objects_](#Object). One or more push buttons on the
mouse allow the user to indicate to the computer program that some
action is to be taken.

### 3.65 MPEG

Moving Picture Experts Group.

### 3.66 multimedia

An integrated presentation, typically on a computer, of content of
various types, such as computer graphics, audio, and video.

### 3.67 network

Chain of interconnected computers.

### 3.68 now

The present [_time_](#Time) as perceived by the [_user_](#User).

### 3.69 node

The fundamental component of a [_scene graph_](#SceneGraph)
in VRML. Nodes are abstractions of various real-world objects and
concepts. Examples include spheres, lights, and material descriptions.
Nodes contain [_fields_](#Field) and [_events_](#Event). [_Messages_](#Message) may be sent between nodes along [_routes_](#Route).

### 3.70 node type

A required parameter for each [_node_](#Node) that
describes, in general, its particular semantics. For example, Box,
Group, Sound, and SpotLight are node types. See " [4.6 Node semantics](concepts.md#4.6)" and
" [6. Node Reference](nodesRef.md)" for
details.

### 3.71 object

A collection of data and procedures, packaged according to the rules
and syntax defined in this standard. "Object" is usually
synonymous with [_node_](#Node) _._

### 3.72 object space

The coordinate system in which an [_object_](#Object)
is defined.

### 3.73 panorama

A background texture that is placed behind all geometry in the scene
and in front of the ground and sky. See " [6.5 Background](nodesRef.md#Background)" for details.

### 3.74 PNG

Portable Network Graphics. A [_file format_](#FileFormat)
for 2D images. See [2.\[PNG\]](references.md#[PNG]).

### 3.75 pointer

A location and direction in the [_virtual world_](#VirtualWorld)
defined by the [_pointing device_](#PointingDevice)
which the [_user_](#User) is currently using to
interact with the virtual world.

### 3.76 pointing device

A hardware device connected to the [_user's_](#User)
computer by which the user directly controls the location and
direction of the [_pointer_](#Pointer). Pointing
devices may be either 2D or 3D and may have one or more control
buttons. See " [4.6.7.5 Activating and manipulating sensors](concepts.md#4.6.7.5)"
for details.

### 3.77 pointing device sensor

Pointing device sensor [_nodes_](#Node) generate [_events_](#Event) based on [_user_](#User)
actions, such as [_pointing device_](#PointingDevice)
motions or button activations. A node of type Anchor, CylinderSensor,
PlaneSensor, SphereSensor, or TouchSensor. See " [4.6.7.3 Pointing device sensors](concepts.md#4.6.7.3)"
for details.

### 3.78 polyline

A sequence of straight line segments where the end point of the first
segment is coincident with the start point of the second segment, the
endpoint of the second segment is coincident with the start point of
the third segment, and so on. A piecewise linear curve.

### 3.79 profile

A named collection of functionality and conformance criteria which
define an implementable subset of a standard.

### 3.80 prototype

The definition of a new [_node type_](#NodeType) in
terms of the [_nodes_](#Node) defined in this standard.
See " [4.8 Prototype semantics](concepts.md#4.8)"
for details.

### 3.81 prototyping

The mechanism for extending the set of [_node types_](#NodeType)
from within a [_VRML file_](#VRMLFile).

### 3.82 public interface

The formal definition of a [_node type_](#NodeType) in
this standard.

### 3.83 RGB

Red, Green, Blue colour model. This is the colour model used within
VRML for the specification of colours. Each colour is represented as a
combination of the three primary colours red, green, and blue. See [E.\[FOLE\]](bibliography.md#[FOLE]).

### 3.84 route

The connection between a [_node_](#Node) generating an [_event_](#Event) and a node receiving the event. See
" [4.3.9 Route statement \
syntax](concepts.md#4.3.9)" and " [4.10.2 Route \
semantics](concepts.md#4.10.2)" for details.

### 3.85 RURL

Relative Uniform Resource Locator. See [2.\[RURL\]](references.md#[RURL]).

### 3.86 scene graph

An ordered collection of grouping [_nodes_](#Node) and
other nodes. [_Grouping nodes_](#GroupingNode), (such
as LOD, Switch, and Transform nodes) may have [_children_\
_nodes_](#ChildrenNode). See " [4.2.3 Scene graph](concepts.md#4.2.3)"
and " [4.4.2 Scene graph structure](concepts.md#4.4.2)"
for details.

### 3.87 scripting

The process of creating or referring to a script.

### 3.88 scripting language

A system of syntactical and semantic constructs used to define and
automate procedures and processes on a computer. Typically, scripting
languages are interpreted and executed sequentially on a
statement-by-statement basis wheras programming languages are generally
compiled prior to execution.

### 3.89 sensor node

A [_node_](#Node) which enables the [_user_](#User)
to interact with the [_world_](#World) in the scene
graph hierarchy. Sensor nodes respond to user interaction with
geometric [_objects_](#Object) in the world, the
movement of the user through the world, or the passage of [_time_](#Time). See " [4.6.7 Sensor nodes](concepts.md#4.6.7)"
for details.

### 3.90 separator character

A [_UTF-8_](UTF-8) character used to separate
syntactical entities in a [_VRML file_](#VRMLFile).
Specifically, commas, spaces, tabs, linefeeds, and carriage-returns are
separator characters wherever they appear outside of string [_fields_](#Field). See " [4.3.1 Clear text encoding](concepts.md#4.3.1)"
for details.

### 3.91 simulation tick

The smallest time unit capable of being identified in a digital
simulation of analog time. [_Time_](#Time) in the
context of VRML is conceptually analog but is realized by an
implementation as a digital simulation of abstract analog time. See
" [4.11 Time](concepts.md#4.11)" for details.

### 3.92 special group node

A [_grouping node_](#GroupingNode) which exhibits
special behaviour. Examples of such special behaviour include selecting
one of many [_children nodes_](#ChildrenNode) to be
rendered based on a dynamically changing parameter value and
dynamically loading children nodes from an external file. A node of
type Inline, LOD (level of detail), or Switch. See " [4.6.5 Grouping and children nodes](concepts.md#4.6.5)"
for details.

### 3.93 texture

An [_image_](#Image) used in a [_texture_\
_map_](#TextureMap) to create visual appearance effects when applied to [_geometry nodes_](#GeometryNode).

### 3.94 texture coordinates

The set of 2D coordinates used by some vertex-based [_geometry nodes_](#GeometryNode) ( _e.g._,
IndexedFaceSet and ElevationGrid) and specified in the
TextureCoordinate node to map textures to the vertices of those nodes.
Texture coordinates range from 0 to 1 across each axis of the texture
image. See " [4.6.11 Texture maps](concepts.md#4.6.11)"
and " [6.48 TextureCoordinate](nodesRef.md#TextureCoordinate)"
for details.

### 3.95 texture map

A [_texture_](#Texture) plus the general parameters
necessary for mapping the texture to geometry.

### 3.96 time

A monotonically increasing value generated by a time sensor nodes. Time
(0.0) starts at 00:00:00 GMT January 1, 1970. See " [4.11 Time](concepts.md#4.11)" for details.

### 3.97 timestamp

The part of a [_message_](#Message) which describes the [_time_](#Time) the [_event_](#Event)
occurred which caused the message to be sent. See " [4.11 Time](concepts.md#4.11)" for details.

### 3.98 traverse

To process the [_nodes_](#Node) in a [_scene graph_](#SceneGraph) in the correct order.

### 3.99 UCS

Universal multiple-octet coded Character Set. See [2.\[UTF8\]](references.md#[UTF8]).

### 3.100 URL

Uniform Resource Locator. See [2.\[URL\]](references.md#[URL]).

### 3.101 URN

Universal Resource Name. See [2.\[URN\]](references.md#[URN]).

### 3.102 UTF-8

The character set used to encode [_VRML files_](#VRMLFile).
The 8-bit UCS Transformation Format. See [2.\[UTF8\]](references.md#[UTF8]).

### 3.103 user

Person or agent who uses and interacts with [_VRML_\
_files_](#VRMLFile) by means of a [_browser_](#Browser).

### 3.104 viewer

A location, direction, and viewing angle in a [_virtual_\
_world_](#VirtualWorld) which determines the portion of the virtual world
presented by the [_browser_](#Browser) to the [_user_](#User).

### 3.105 virtual world

See [_world_](#World).

### 3.106 VRML browser

See [_browser_](#Browser).

### 3.107 VRML document server

A computer program that locates and transmits [_VRML_\
_files_](#VRMLFile) and supporting files in response to requests from VRML
client applications ( [_browsers_](#Browser)).

### 3.108 VRML file

A file, data stream, or string of UTF-8 characters, which contains
information encoded according to ISO/IEC 14772 (this standard).

### 3.109 wand

A 3D [_pointing devices_](#PointingDevice).

### 3.110 white space

One or more consecutive occurrences of a separator character. See " [4.3.1 Clear text encoding](concepts.md#4.3.1)"
for details.

### 3.111 world

A collection of one or more [_VRML files_](#VRMLFile)
and other multimedia content which, when interpreted by a [_VRML browser_](#VRMLBrowser), presents an interactive
experience to the [_user_](#User) consistent with the [_author's_](#Author) intent.

### 3.112 world coordinate space

The coordinate system in which each VRML [_world_](#World)
is defined. The world coordinate space is an orthogonal right-handed
Cartesian coordinate system. The units of length are metres.

### 3.113 World Wide Web

The collection of documents, information, and content accessible via
the [_Internet_](#Internet).

### 3.114 XY plane

The plane perpendicular to the Z-axis which passes through the point Z
= 0.0.

### 3.115 YZ plane

The plane perpendicular to the X-axis which passes through the point X
= 0.0.

### 3.116 ZX plane

The plane perpendicular to the Y-axis which passes through the point Y
= 0.0.

![](../pix/vrmlbar.gif)

```
https://graphics.stanford.edu/courses/cs248-98-fall/Assignments/Assignment3/VRML2_Specification/spec/part1/glossary.html

```

