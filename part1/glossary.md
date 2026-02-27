![vrmllogo2](../pix/vrmllogo2.0.gif)

# The Virtual Reality Modeling Language

# 3. Definitions

### ISO/IEC DIS 14772-1

#### 4 April 1997

![vrmlbar](../pix/vrmlbar.gif)

<a id="Activate"></a>

### 3.1 activate

Чтобы заставить [_sensor node_](#SensorNode) генерировать [_событие_](#Event) «isActive». Различные типы сенсорных узлов «активируются» взаимодействиями [_user_](#User), прохождением [_time_](#Time) или другими событиями. Только активные датчики влияют на работу [_user's_](#User). Сценарий [_node_](#Node) активируется при получении события. Указательное устройство, такое как [_mouse_](#Mouse), активируется, когда пользователь нажимает одну из его кнопок. Подробности см. в разделе «[4.12.2 Выполнение сценария](concepts.md#4.12.2)».

<a id="Ancestor"></a>

### 3.2 ancestor (предок)

[_Узел_](#Node) который содержит один или несколько [_дочених узлов_](#ChildrenNode). [_grouping node_](#GroupingNode).

<a id="Author"></a>

### 3.3 author

Лицо или агент, создающий [_VRML files_](#VRMLFile). Авторы обычно используют [_generators_](#Generator) для помощи им..

<a id="AuthoringTool"></a>

### 3.4 authoring tool

Смотри [_generator_](#Generator).

<a id="Avatar"></a>

### 3.5 avatar

Абстрактное представление [_user_](#User) в VRML [_world_](#World). Физические размеры аватара используются для обнаружения столкновений и отслеживания местности. Подробности см. в разделе «[6.29 NavigationInfo](nodesRef.md#NavigationInfo)».

<a id="Bearing"></a>

### 3.6 bearing

Прямая линия, проходящая через местоположение [_pointer_](#Pointer) в направлении указателя. Если геометрия нескольких датчиков пересекает эту линию, только ближайший к зрителю датчик сможет генерировать [_events_](#Event) независимо от свойств материала и текстуры (например, прозрачности).

<a id="BindingNode"></a>

### 3.7 binding node (узел привязки)

[_node_](#Node), который может иметь множество [_instances_](#Instance) в [_scene_ _graph_](#SceneGraph), но в любой момент времени [_time_](#Time) может быть активен только один экземпляр. Узел типа Background, Fog, NavigationInfo или Viewpoint. Подробности см. в разделе «[4.6.10 Привязываемые дочерние узлы](concepts.md#4.6.10)".

<a id="Browser"></a>

### 3.8 browser

Компьютерная программа, которая интерпретирует [_VRML files_](#VRMLFile) , представляет их содержимое [_user_](#User) на [_display device_](#DisplayDevice) и позволяет пользователю взаимодействовать с [_worlds_](#World), определенными файлами VRML, посредством пользовательского интерфейса.

<a id="BrowserExtension"></a>

### 3.9 browser extension

[_Nodes_](#Node) определяется с использованием механизма прототипирования, который понятен только определенным [_browsers_](#Browser). Подробности см. в разделе «[4.9.3 Расширения браузера](concepts.md#4.9.3)".

<a id="BuiltinNode"></a>

### 3.10 built-in node

Узел [_type_](#NodeType), явно определенный в этом стандарте.

<a id="Callback"></a>

### 3.11 callback

Функция, определенная в [_scripting_ _language_](#ScriptingLanguage), которому передаются [_events_](#Event). Подробности см. в разделе «[4.12.8 Обработка EventIn](concepts.md#4.12.8)".

<a id="Candidate"></a>

### 3.12 candidate

Один из нескольких возможных вариантов. [_user_](#User) или [_browser_](#Browser) не выберут ни один из вариантов или один из вариантов, когда будут определены все кандидаты.  Подробности см. в разделах "[4.6.10 Привязываемые дочерние узлы](concepts.md#4.6.10)" и "[6.2 Anchor](nodesRef.md#Anchor)".

<a id="Child"></a>

### 3.13 child

Прямой [_потомок_](#Descendent).

<a id="ChildrenNode"></a>

### 3.14 children node

[_Node_](#Node), родительским элементом которого может быть [_grouping node_](#GroupingNode), и на него влияют преобразования всех [_предков_](#Ancestor). Список допустимых дочерних узлов см. в разделе "[4.6.5 Группировка и дочерние узлы](concepts.md#4.6.5)".

<a id="ClientSystem"></a>

### 3.15 client system

Компьютерная система, подключенная к [_сети_](#Network), которая использует другой компьютер (сервер) для выполнения основных функций обработки. Многие клиентские системы также функционируют как автономные компьютеры.

<a id="CollisionProxy"></a>

### 3.16 collision proxy

[_node_](#Node), используемый в качестве замены всех дочерних узлов узла столкновения во время обнаружения столкновений. Подробности см. в разделе «[6.8 Столкновение](nodesRef.md#Collision)».

<a id="ColourModel"></a>

### 3.17 colour model

Характеристика цветового пространства с точки зрения явных параметров. VRML позволяет определять цвета только с помощью цветовой модели RGB. Однако интерполяция цвета выполняется в цветовом пространстве HSV.

<a id="Culling"></a>

### 3.18 culling (отбраковка)

Процесс идентификации [_objects_](#Object) или частей объектов, которые не требуют дальнейшей обработки [_browser_](#Browser) для создания желаемого представления [_world_](#World).

<a id="Descendent"></a>

### 3.19 descendent (потомок не обязательно прямой)

[_node_](#Node) в [_scene_graph_](#SceneGraph), у которого есть родительский элемент. См. [_children_node_](#ChildrenNode).

<a id="DisplayDevice"></a>

### 3.20 display device

Графическое устройство, на котором может отображаться VRML [_worlds_](#World).

<a id="DragSensor"></a>

### 3.21 drag sensor

[_Датчик указывающего устройства_](#PointingDeviceSensor), который вызывает создание [_events_](#Event) в ответ на движения указателя, зависящие от датчика. Например, SphereSensor генерирует события сферического вращения. [_node_](#Node) типа CylinderSensor, PlaneSensor или SphereSensor. Подробности см. в разделах «[4.6.7 Узлы датчиков](concepts.md#4.6.7)» и «[4.6.7.4 DragSensor](concepts.md#4.6.7.4)».

<a id="Element"></a>

### 3.22 element

Наименьшая единица, на которую можно разделить [_object_](#Object). Например, запись в заголовке [_VRML_file_](#VRMLFile) или одно значение многозначного [_поля_](#Field).

<a id="EnvironmentalSensor"></a>

### 3.23 environmental sensor

Датчик окружающей среды [_узла_](#Node) генерирует [_событие_](#Event) на основе местоположения точки обзора в мире или относительно [_объекта_](#Object) в мире. Узел TimeSensor генерирует события через регулярные промежутки времени в [_time_](#Time). Узел типа Collision, ProximitySensor, TimeSensor или VisibilitySensor. Подробности см. в разделе «[4.6.7.2 Датчики окружающей среды](concepts.md#4.6.7.2)».

<a id="Event"></a>

### 3.24 event (событие)

[_Сообщение (сигнал)_](#Message), отправленное с одного [_узла_](#Node) на другой, как определено [_маршрутом_](#Route). [_События_](#Event) сигнализируют о внешних стимулах, изменениях значений [_поля_](#Field) и взаимодействиях между узлами. Событие состоит из [_временной метки_](#Timestamp) и значения поля.

<a id="EventCascade"></a>

### 3.25 event cascade

Последовательность [_событий_](#Event), инициируемая сценарием или событием датчика и распространяющаяся от [_узла_](#Node) к узлу по одному или нескольким [_маршрутам_](#Route). Считается, что все события в каскаде событий произошли одновременно. Подробности см. в разделе «[4.10.3 Модель выполнения](concepts.md#4.10.3)».

<a id="Eventin"></a>

### 3.26 eventIn

Логический рецептор, прикрепленный к [_узлу_](#Node), который получает [_событие_](#Event).

<a id="Eventout"></a>

### 3.27 eventOut

Логический выходной терминал, подключенный к [_узлу_](#Node), из которого отправляются [_события_](#Event). EventOut также сохраняет последнее отправленное событие.

<a id="ExecutionModel"></a>

### 3.28 execution model

Правила, управляющие обработкой [_событий_](#Event) [_брузерами_](#Browser) и скриптами.

<a id="ExposedField"></a>

### 3.29 exposed field

[_Поле_](#Field), которое способно получать [_события_](#Event) через eventIn для изменения его значений и генерировать события через eventOut при изменении его значений.

<a id="ExternalPrototype"></a>

### 3.30 external prototype

[_Прототип_](#Prototype), определенный во внешнем файле и на который ссылается [_URL_](#Url).

<a id="Field"></a>

### 3.31 field (поле, свойство, атрибут...)

Свойство или атрибут [_узла_](#Node). Каждый [_node type_](#NodeType) имеет фиксированный набор полей. Поля могут содержать различные типы данных и одно или несколько значений.

<a id="FieldName"></a>

### 3.32 field name

Имя [_поля_](#Field). Имена полей уникальны в пределах [_узла_](#Node).

<a id="FileFormat"></a>

### 3.33 file format

Подробное описание цифровых данных, которые обычно хранятся в компьютерной файловой системе.

<a id="Frame"></a>

### 3.34 frame (Кадр)

Одиночный рендеринг [_world_](#World) на [_display device_](#DisplayDevice) или один временной шаг в моделировании.

<a id="Generator"></a>

### 3.35 generator

Компьютерная программа, которая создает[_VRML files_](#VRMLFile). Генератор может использоваться человеком или работать автоматически.

<a id="GeometricPropertyNode"></a>

### 3.36 geometric property node

[_Узел_](#Node), определяющий свойства конкретного узла геометрии. Узел типа Color, Coordinate, Normal, или TextureCoordinate. Подробности см. в разделе «[4.6.3.2 Узлы геометрических свойств](concepts.md#4.6.3.2)».

<a id="GeometricSensorNode"></a>

### 3.37 geometric sensor node

[_node_](#Node), который генерирует [_events_](#Event) на основе действий [_user_](#User), таких как щелчок [_mouse_](#Mouse) или навигация вблизи определенного [_object_](#Object). Узел типа CylinderSensor, PlaneSensor, ProximitySensor, SphereSensor, TouchSensor, VisibilitySensor или Collision. Подробности см. в разделе «[4.6.7.1 Введение в узлы датчиков](concepts.md#4.6.7.1)".

<a id="GeometryNode"></a>

### 3.38 geometry node

[_node_](#Node), содержащий математические описания трехмерных (3D) точек, линий, поверхностей, текстовых строк и твердых тел. Узел типа Box, Cone, Cylinder, ElevationGrid, Extrusion, IndexedFaceSet, IndexedLineSet, PointSet, Sphere или Text. Подробности см. в разделе «[4.6.3 Формы и геометрия](concepts.md#4.6.3)".

<a id="Grab"></a>

### 3.39 grab

Для получения [_событий_](#Event) от манипулятора ( [_Мышь_](#Mouse) или [_перо_](#Wand)). [_Датчик указывающего устройства_](#PointingDeviceSensor) становится эксклюзивным получателем событий указывающего устройства, когда указывающее устройство активируется при указании узлов геометрии A [_descendent_](#Descendent), которые являются дочерними элементами родительской группы датчика.

<a id="Gravity"></a>

### 3.40 gravity

Сила, которая заставляет массы притягиваться друг к другу. В контексте этого стандарта гравитацию можно моделировать, ограничивая движение точки обзора наименьшим возможным путем (наименьшая координата y в локальной системе координат точки обзора), согласующимся с следованием по поверхности встреченных объектов. Подробности см. в разделе «[6.29 NavigationInfo](nodesRef.md#NavigationInfo)».

<a id="GroupingNode"></a>

### 3.41 grouping node

[_Узел_](#Node), который собирает [_дочерние узлы_](#ChildrenNode) и другие группирующие узлы вместе и заставляет группу демонстрировать определенное поведение, которое зависит от [_Node type_](#NodeType). Узел типа Anchor, Billboard, Collision, Group, или Transform. Подробности см. в разделе "[4.6.5 Группировка и дочерние узлы](concepts.md#4.6.5)".

<a id="Hsv"></a>

### 3.42 HSV

Цветовая модель оттенка, насыщенности и значения. См. [E.[FILE]](bibliography.md#[FILE]).

<a id="Html"></a>

### 3.43 HTML

HyperText Markup Language. See [2.[HTML]](references.md#[HTML]).

<a id="Hyperlink"></a>

### 3.44 hyperlink

Ссылка на [_URL_](#Url), связанную с узлом привязки. Подробности см. в разделе «[6.2 Anchor](nodesRef.md#Anchor)».

<a id="IdealVrmlImplementation"></a>

### 3.45 ideal VRML implementation

Реализация VRML, которая представляет все [_objects_](#Object) и моделирует движение без аппроксимации. Не реализуемо на практике.

<a id="Iec"></a>

### 3.46 IEC

International Electrotechnical Commission. See [`http://www.iec.ch`](http://www.iec.ch).

<a id="Ietf"></a>

### 3.47 IETF

Internet Engineering Task Force. The organization which develops [_Internet_](#Internet) standards. See [`http://www.ietf.org/overview.html`](http://www.ietf.org/overview.html).

<a id="Image"></a>

### 3.48 image

Двумерный (2D) прямоугольный массив значений пикселей. Значения пикселей могут иметь от одного до четырех компонентов. Подробности см. в разделе «[5.5 SFImage](fieldsRef.md#SFImage)».

<a id="Inlining"></a>

### 3.49 in-lining

Механизм, с помощью которого один [_VRML file_](#VRMLFile) иерархически включается в другой.

<a id="Internet"></a>

### 3.50 Internet

Всемирная сеть под названием [_network_](#Network), которая взаимодействует друг с другом с использованием общего набора протоколов связи, известных как TCP/IP. См. [_IETF_](#Ietf). [_Всемирная паутина_](#WorldWideWeb) реализована в Интернете.

<a id="Instance"></a>

### 3.51 instance

Ссылка на ранее определенный и названный [_узел_](#Node) через синтаксис USE. Узлы именуются с помощью синтаксиса DEF. Экземпляры узлов могут использоваться в любом контексте, в котором может использоваться определяющий узел.

<a id="InterpolatorNode"></a>

### 3.52 interpolator node

[_Узел_](#Node), который определяет кусочную линейную интерполяцию определенного типа значения в указанное время [_times_](#Time). Узел типа ColorInterpolator,CoordinateInterpolator, NormalInterpolator, OrientationInterpolator, PositionInterpolator или ScalarInterpolator. Подробности см. в разделе «[4.6.8 Интерполяторы](concepts.md#4.6.8)».

<a id="Intranet"></a>

### 3.53 intranet

Частная [_сеть_](#Network), использующая те же протоколы и стандарты, что и [_Интернет_](#Internet).

<a id="Iso"></a>

### 3.54 ISO

International Organization for Standardization. See [`http://www.iso.ch/infoe/intro.html`](http://www.iso.ch/infoe/intro.html).

<a id="Jpeg"></a>

### 3.55 JPEG

Joint Photographic Experts Group. See [2.[JPEG]](references.md#[JPEG]).

<a id="Jtc1"></a>

### 3.56 JTC 1

Joint Technical Committee 1. See [`http://www.iso.ch/meme/JTC1.html`](http://www.iso.ch/meme/JTC1.html).

<a id="LevelOfDetailLod"></a>

### 3.57 level of detail (LOD)

Степень детализации или сложности, отображаемая в любой конкретный [_момент времени_](#Time) для любого конкретного [_объекта_](#Object). Уровень детализации объекта можно контролировать в зависимости от расстояния объекта до зрителя. Подробности см. в разделе «[6.26 LOD](nodesRef.md#LOD)».

<a id="Lod"></a>

### 3.58 LOD

Level Of Detail.

<a id="LineTerminator"></a>

### 3.59 line terminator

Символ (или последовательность двух символов), используемый для завершения строки в [_VRML file_](#VRMLFile). В частности, один или оба символа [_UTF-8_](#Utf8) «возврат каретки CR» и «перевод строки LF». Если присутствуют оба символа, любой из них может быть первым в последовательности.

<a id="Loop"></a>

### 3.60 loop

Последовательность [_событий_](#Event), в результате которой событие логически ответственно за создание самого себя. Подробности см. в разделе «[4.10.4 Циклы](concepts.md#4.10.4)».

<a id="Message"></a>

### 3.61 message

Строка, передаваемая между [_узлами_](#Node) при возникновении [_событияллллллллл_](#Event). Подробности см. в разделе «[4.10 Обработка событий](concepts.md#4.10)».

<a id="Midi"></a>

### 3.62 MIDI

Musical Instrument Digital Interface. A standard for digital music representation. See [2.[MIDI]](references.md#[MIDI]).

<a id="Mime"></a>

### 3.63 MIME

Multipurpose Internet Mail Extension. Used to specify filetyping rules for [_Internet_](#Internet) applications, including [_browsers_](#Browser). See " [4.5.1 File extension and MIME types](concepts.md#4.5.1)" for details. See also [2.[MIME]](references.md#[MIME]).

<a id="Mouse"></a>

### 3.64 mouse

A 2D pointing device which enables a [_user_](#User) to move a cursor on a display device in order to point at displayed [_objects_](#Object). One or more push buttons on the mouse allow the user to indicate to the computer program that some action is to be taken.

<a id="Mpeg"></a>

### 3.65 MPEG

Moving Picture Experts Group.

<a id="Multimedia"></a>

### 3.66 multimedia

An integrated presentation, typically on a computer, of content of various types, such as computer graphics, audio, and video.

<a id="Network"></a>

### 3.67 network

Chain of interconnected computers.

<a id="Now"></a>

### 3.68 now

The present [_time_](#Time) as perceived by the [_user_](#User).

<a id="Node"></a>

### 3.69 node

The fundamental component of a [_scene graph_](#SceneGraph) in VRML. Nodes are abstractions of various real-world objects and concepts. Examples include spheres, lights, and material descriptions. Nodes contain [_fields_](#Field) and [_events_](#Event). [_Messages_](#Message) may be sent between nodes along [_routes_](#Route).

<a id="NodeType"></a>

### 3.70 node type

A required parameter for each [_node_](#Node) that describes, in general, its particular semantics. For example, Box, Group, Sound, and SpotLight are node types. See " [4.6 Node semantics](concepts.md#4.6)" and " [6. Node Reference](nodesRef.md)" for details.

<a id="Object"></a>

### 3.71 object

A collection of data and procedures, packaged according to the rules and syntax defined in this standard. "Object" is usually synonymous with [_node_](#Node) _._

<a id="ObjectSpace"></a>

### 3.72 object space

The coordinate system in which an [_object_](#Object) is defined.

<a id="Panorama"></a>

### 3.73 panorama

A background texture that is placed behind all geometry in the scene and in front of the ground and sky. See " [6.5 Background](nodesRef.md#Background)" for details.

<a id="Png"></a>

### 3.74 PNG

Portable Network Graphics. A [_file format_](#FileFormat) for 2D images. See [2.[PNG]](references.md#[PNG]).

<a id="Pointer"></a>

### 3.75 pointer

A location and direction in the [_virtual world_](#VirtualWorld) defined by the [_pointing device_](#PointingDevice) which the [_user_](#User) is currently using to interact with the virtual world.

<a id="PointingDevice"></a>

### 3.76 pointing device

A hardware device connected to the [_user's_](#User) computer by which the user directly controls the location and direction of the [_pointer_](#Pointer). Pointing devices may be either 2D or 3D and may have one or more control buttons. See " [4.6.7.5 Activating and manipulating sensors](concepts.md#4.6.7.5)" for details.

<a id="PointingDeviceSensor"></a>

### 3.77 pointing device sensor

Pointing device sensor [_nodes_](#Node) generate [_events_](#Event) based on [_user_](#User) actions, such as [_pointing device_](#PointingDevice) motions or button activations. A node of type Anchor, CylinderSensor, PlaneSensor, SphereSensor, or TouchSensor. See " [4.6.7.3 Pointing device sensors](concepts.md#4.6.7.3)" for details.

<a id="Polyline"></a>

### 3.78 polyline

A sequence of straight line segments where the end point of the first segment is coincident with the start point of the second segment, the endpoint of the second segment is coincident with the start point of the third segment, and so on. A piecewise linear curve.

<a id="Profile"></a>

### 3.79 profile

A named collection of functionality and conformance criteria which define an implementable subset of a standard.

<a id="Prototype"></a>

### 3.80 prototype

The definition of a new [_node type_](#NodeType) in terms of the [_nodes_](#Node) defined in this standard. See " [4.8 Prototype semantics](concepts.md#4.8)" for details.

<a id="Prototyping"></a>

### 3.81 prototyping

The mechanism for extending the set of [_node types_](#NodeType) from within a [_VRML file_](#VRMLFile).

<a id="PublicInterface"></a>

### 3.82 public interface

The formal definition of a [_node type_](#NodeType) in this standard.

<a id="Rgb"></a>

### 3.83 RGB

Red, Green, Blue colour model. This is the colour model used within VRML for the specification of colours. Each colour is represented as a combination of the three primary colours red, green, and blue. See [E.[FOLE]](bibliography.md#[FOLE]).

<a id="Route"></a>

### 3.84 route

The connection between a [_node_](#Node) generating an [_event_](#Event) and a node receiving the event. See " [4.3.9 Route statement syntax](concepts.md#4.3.9)" and " [4.10.2 Route semantics](concepts.md#4.10.2)" for details.

<a id="Rurl"></a>

### 3.85 RURL

Relative Uniform Resource Locator. See [2.[RURL]](references.md#[RURL]).

<a id="SceneGraph"></a>

### 3.86 scene graph

An ordered collection of grouping [_nodes_](#Node) and other nodes. [_Grouping nodes_](#GroupingNode), (such as LOD, Switch, and Transform nodes) may have [_children_ _nodes_](#ChildrenNode). See " [4.2.3 Scene graph](concepts.md#4.2.3)" and " [4.4.2 Scene graph structure](concepts.md#4.4.2)" for details.

<a id="Scripting"></a>

### 3.87 scripting

The process of creating or referring to a script.

<a id="ScriptingLanguage"></a>

### 3.88 scripting language

A system of syntactical and semantic constructs used to define and automate procedures and processes on a computer. Typically, scripting languages are interpreted and executed sequentially on a statement-by-statement basis wheras programming languages are generally compiled prior to execution.

<a id="SensorNode"></a>

### 3.89 sensor node

A [_node_](#Node) which enables the [_user_](#User) to interact with the [_world_](#World) in the scene graph hierarchy. Sensor nodes respond to user interaction with geometric [_objects_](#Object) in the world, the movement of the user through the world, or the passage of [_time_](#Time). See " [4.6.7 Sensor nodes](concepts.md#4.6.7)" for details.

<a id="SeparatorCharacter"></a>

### 3.90 separator character

A [_UTF-8_](UTF-8) character used to separate syntactical entities in a [_VRML file_](#VRMLFile). Specifically, commas, spaces, tabs, linefeeds, and carriage-returns are separator characters wherever they appear outside of string [_fields_](#Field). See " [4.3.1 Clear text encoding](concepts.md#4.3.1)" for details.

<a id="SimulationTick"></a>

### 3.91 simulation tick

The smallest time unit capable of being identified in a digital simulation of analog time. [_Time_](#Time) in the context of VRML is conceptually analog but is realized by an implementation as a digital simulation of abstract analog time. See " [4.11 Time](concepts.md#4.11)" for details.

<a id="SpecialGroupNode"></a>

### 3.92 special group node

A [_grouping node_](#GroupingNode) which exhibits special behaviour. Examples of such special behaviour include selecting one of many [_children nodes_](#ChildrenNode) to be rendered based on a dynamically changing parameter value and dynamically loading children nodes from an external file. A node of type Inline, LOD (level of detail), or Switch. See " [4.6.5 Grouping and children nodes](concepts.md#4.6.5)" for details.

<a id="Texture"></a>

### 3.93 texture

An [_image_](#Image) used in a [_texture_ _map_](#TextureMap) to create visual appearance effects when applied to [_geometry nodes_](#GeometryNode).

<a id="TextureCoordinates"></a>

### 3.94 texture coordinates

The set of 2D coordinates used by some vertex-based [_geometry nodes_](#GeometryNode) ( _e.g._, IndexedFaceSet and ElevationGrid) and specified in the TextureCoordinate node to map textures to the vertices of those nodes. Texture coordinates range from 0 to 1 across each axis of the texture image. See " [4.6.11 Texture maps](concepts.md#4.6.11)" and " [6.48 TextureCoordinate](nodesRef.md#TextureCoordinate)" for details.

<a id="TextureMap"></a>

### 3.95 texture map

A [_texture_](#Texture) plus the general parameters necessary for mapping the texture to geometry.

<a id="Time"></a>

### 3.96 time

A monotonically increasing value generated by a time sensor nodes. Time (0.0) starts at 00:00:00 GMT January 1, 1970. See " [4.11 Time](concepts.md#4.11)" for details.

<a id="Timestamp"></a>

### 3.97 timestamp

The part of a [_message_](#Message) which describes the [_time_](#Time) the [_event_](#Event) occurred which caused the message to be sent. See " [4.11 Time](concepts.md#4.11)" for details.

<a id="Traverse"></a>

### 3.98 traverse

To process the [_nodes_](#Node) in a [_scene graph_](#SceneGraph) in the correct order.

<a id="Ucs"></a>

### 3.99 UCS

Universal multiple-octet coded Character Set. See [2.[UTF8]](references.md#[UTF8]).

<a id="Url"></a>

### 3.100 URL

Uniform Resource Locator. See [2.[URL]](references.md#[URL]).

<a id="Urn"></a>

### 3.101 URN

Universal Resource Name. See [2.[URN]](references.md#[URN]).

<a id="Utf8"></a>

### 3.102 UTF-8

The character set used to encode [_VRML files_](#VRMLFile). The 8-bit UCS Transformation Format. See [2.[UTF8]](references.md#[UTF8]).

<a id="User"></a>

### 3.103 user

Person or agent who uses and interacts with [_VRML_ _files_](#VRMLFile) by means of a [_browser_](#Browser).

<a id="Viewer"></a>

### 3.104 viewer

A location, direction, and viewing angle in a [_virtual_ _world_](#VirtualWorld) which determines the portion of the virtual world presented by the [_browser_](#Browser) to the [_user_](#User).

<a id="VirtualWorld"></a>

### 3.105 virtual world

See [_world_](#World).

<a id="VRMLBrowser"></a>

### 3.106 VRML browser

See [_browser_](#Browser).

<a id="VRMLDocumentServer"></a>

### 3.107 VRML document server

Компьютерная программа, которая находит и передает [_VRML_files_](#VRMLFile) и вспомогательные файлы в ответ на запросы клиентских приложений VRML ( [_browsers_](#Browser)).

<a id="VRMLFile"></a>

### 3.108 VRML file

A file, data stream, or string of UTF-8 characters, which contains information encoded according to ISO/IEC 14772 (this standard).

<a id="Wand"></a>

### 3.109 wand

A 3D [_pointing devices_](#PointingDevice).

<a id="WhiteSpace"></a>

### 3.110 white space

One or more consecutive occurrences of a separator character. See " [4.3.1 Clear text encoding](concepts.md#4.3.1)" for details.

<a id="World"></a>

### 3.111 world

A collection of one or more [_VRML files_](#VRMLFile) and other multimedia content which, when interpreted by a [_VRML browser_](#VRMLBrowser), presents an interactive experience to the [_user_](#User) consistent with the [_author's_](#Author) intent.

<a id="WorldCoordinateSpace"></a>

### 3.112 world coordinate space

The coordinate system in which each VRML [_world_](#World) is defined. The world coordinate space is an orthogonal right-handed Cartesian coordinate system. The units of length are metres.

<a id="WorldWideWeb"></a>

### 3.113 World Wide Web

The collection of documents, information, and content accessible via the [_Internet_](#Internet).

<a id="XyPlane"></a>

### 3.114 XY plane

The plane perpendicular to the Z-axis which passes through the point Z = 0.0.

<a id="YzPlane"></a>

### 3.115 YZ plane

The plane perpendicular to the X-axis which passes through the point X = 0.0.

<a id="ZxPlane"></a>

### 3.116 ZX plane

The plane perpendicular to the Y-axis which passes through the point Y = 0.0.

![vrmlbar](../pix/vrmlbar.gif)

``` https://graphics.stanford.edu/courses/cs248-98-fall/Assignments/Assignment3/VRML2_Specification/spec/part1/glossary.html

```
