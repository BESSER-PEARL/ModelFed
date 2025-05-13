Vocabulary
==========

The ModelFed Vocabulary extends the `Activity Streams 2.0 <https://www.w3.org/TR/activitystreams-vocabulary/>`_
Vocabulary.

A graphical representation of the Vocabulary concepts and their relationships is shown below:

.. figure:: images/vocabulary.png
   :alt: Modelverse Vocabulary
   :width: 100%
   :align: center

The typical ``@context`` for ModelFed objects is as follows:

.. code-block:: json

    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
    ]

Extended Types
--------------

Objects
~~~~~~~
The list of additional objects in the Modelverse Vocabulary are presented below.

.. _domainModel:

Domain Model
^^^^^^^^^^^^

+--------------+---------------------------------------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#DomainModel                                    |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Description: | Represents a domain model that defines the structure and relationships                                        |
|              | of entities within a specific domain.                                                                         |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Extends:     | `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_                                      |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Properties:  | :ref:`types` | :ref:`associations` | :ref:`packages` | :ref:`generalizations` | :ref:`grants`                 |
|              |                                                                                                               |
|              | Other properties are inherited from `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_. |
+--------------+---------------------------------------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "DomainModel",
        "id": "http://www.modeling-platform/domainmodel/a1b2c3",
        "name": "A simple Domain Model"
    }

.. _modelElement:

ModelElement
^^^^^^^^^^^^
+--------------+---------------------------------------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#ModelElement                                   |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Description: | Represents a model element as part of a domain model. This class is **abstract**.                             |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Extends:     | `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_                                      |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Properties:  | :ref:`timestamp`                                                                                              |
|              |                                                                                                               |
|              | Other properties are inherited from `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_. |
+--------------+---------------------------------------------------------------------------------------------------------------+

.. _package:

Package
^^^^^^^
+--------------+------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Package |
+--------------+------------------------------------------------------------------------+
| Description: | Represents a package that groups a set of model elements.              |
+--------------+------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                    |
+--------------+------------------------------------------------------------------------+
| Properties:  | :ref:`elements`                                                        |
|              |                                                                        |
|              | Other properties are inherited from :ref:`modelElement`.               |
+--------------+------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Package",
        "id": "http://www.modeling-platform/package/p1d2e3",
        "name": "A simple Package",
        "elements": [
            "http://www.modeling-platform/classes/C1D2E3",
            "http://www.modeling-platform/classes/a3m4bs",
            "http://www.modeling-platform/packages/pckbs",
        ]
    }

.. _type:

Type
^^^^
+--------------+------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Type    |
+--------------+------------------------------------------------------------------------+
| Description: | Represents a type in the model. This class is **abstract**             |
+--------------+------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                    |
+--------------+------------------------------------------------------------------------+
| Properties:  | Inherits all properties from :ref:`modelElement`.                      |
+--------------+------------------------------------------------------------------------+

.. _class:

Class
^^^^^
+--------------+----------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Class       |
+--------------+----------------------------------------------------------------------------+
| Description: | Represents a class in the model.                                           |
+--------------+----------------------------------------------------------------------------+
| Extends:     | :ref:`type`                                                                |
+--------------+----------------------------------------------------------------------------+
| Properties:  | :ref:`attributes` | :ref:`methods` | :ref:`isAbstract`                     |
|              |                                                                            |
|              | Other properties are inherited from :ref:`type`.                           |
+--------------+----------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Class",
        "id": "http://www.modeling-platform/class/c1d2e3",
        "name": "A simple Class",
        "attributes": [
            "http://www.modeling-platform/attribute/a1b2c3",
            "http://www.modeling-platform/attribute/aasdf3",
        ],
        "methods": []
    }

.. _dataType:

DataType
^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Enumeration       |
+--------------+----------------------------------------------------------------------------------+
| Description: | This class is **abstract** and represents data types.                            |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`type`                                                                      |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | Inherits all properties from :ref:`type`.                                        |
+--------------+----------------------------------------------------------------------------------+

.. _enumeration:

Enumeration
^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Enumeration       |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents an enumeration in the model.                                          |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`dataType`                                                                  |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`literals`                                                                  |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`dataType`.                             |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Enumeration",
        "id": "http://www.modeling-platform/enumerations/e1f2g3",
        "name": "A simple Enumeration",
        "literals": [
            "http://www.modeling-platform/enumerationliterals/l1m2n3",
            "http://www.other-platform/enumerationliterals/l3m5n7"
        ]
    }

.. _enumerationLiteral:

EnumerationLiteral
^^^^^^^^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#EnumerationLiteral|
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a literal value of an enumeration.                                    |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                              |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`owner` | :ref:`value`                                                      |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`modelElement`.                         |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "EnumerationLiteral",
        "id": "http://www.modeling-platform/enumerationliterals/l1m2n3",
        "name": "A simple Enumeration Literal",
        "value": "LiteralValue",
        "owner": "http://www.modeling-platform/enumerations/e1f2g3"
    }

.. _primitiveDataType:

PrimitiveDataType
^^^^^^^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#PrimitiveDataType |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a primitive data type in the model.                                   |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`dataType`                                                                  |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | Inherits all properties from :ref:`dataType`.                                    |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "PrimitiveDataType",
        "id": "http://www.modeling-platform/primitivedatatype/p1d2e3",
        "name": "type name",
        "timestamp": "2025-01-20T08:30:00Z"
    }

.. _typedElement:

TypedElement
^^^^^^^^^^^^
+--------------+-----------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#TypedElement |
+--------------+-----------------------------------------------------------------------------+
| Description: | Typed element is an **abstract** class that is used to represent            | 
|              | elements that have a type.                                                  |
+--------------+-----------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                         |
+--------------+-----------------------------------------------------------------------------+
| Properties:  | :ref:`elementType`                                                          |
|              |                                                                             |
|              | Other properties are inherited from :ref:`modelElement`.                    |
+--------------+-----------------------------------------------------------------------------+

.. _property:

Property
^^^^^^^^
+--------------+-------------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Property             |
+--------------+-------------------------------------------------------------------------------------+
| Description: | A property can represents an attribute of a class or an end of an association.      |
+--------------+-------------------------------------------------------------------------------------+
| Extends:     | :ref:`typedElement`                                                                 |
+--------------+-------------------------------------------------------------------------------------+
| Properties:  | :ref:`owner` | :ref:`multiplicity` | :ref:`isComposite` | :ref:`isNavigable` |      |
|              | :ref:`isId`                                                                         |
|              |                                                                                     |
|              | Other properties are inherited from :ref:`typedElement`.                            |
+--------------+-------------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Property",
        "id": "http://www.modeling-platform/property/p1d2e3",
        "name": "title",
        "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
        "isId": false,
        "multiplicity": "0..1"
    }

.. _association:

Association
^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Association       |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a relationship between classes.                                       |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                              |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`ends`                                                                      |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`modelElement`.                         |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Association",
        "id": "http://www.modeling-platform/associations/a1b2c3",
        "name": "has_books",
        "ends": [
            "http://www.modeling-platform/properties/p1r2y3",
            "http://www.modeling-platform/properties/p4r5y6",
            "http://www.other-platform/properties/p555y6"
        ]
    }

.. _binaryAssociation:

BinaryAssociation
^^^^^^^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#BinaryAssociation |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a binary association between two classes.                             |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`association`                                                               |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | Inherits all properties from :ref:`association`.                                 |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "BinaryAssociation",
        "id": "http://www.modeling-platform/associations/b1c2d3",
        "name": "belongs_to",
        "ends": [
            "http://www.modeling-platform/properties/p1f2g3",
            "http://www.modeling-platform/properties/p4f5g6"
        ]
    }

.. _generalization:

Generalization
^^^^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Generalization    |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a generalization relationship between a general and a specific class. |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                              |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`general` | :ref:`specific`                                                 |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`modelElement`.                         |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Generalization",
        "id": "http://www.modeling-platform/generalizations/g1h2i3",
        "general": "http://www.modeling-platform/class/c1d2e3",
        "specific": "http://www.modeling-platform/class/c4d5e6"
    }

.. _parameter:

Parameter
^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Parameter         |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a parameter of a method.                                              |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`typedElement`                                                              |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`defaultValue`                                                              |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`typedElement`.                         |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Parameter",
        "id": "http://www.modeling-platform/parameter/p1q2r3",
        "name": "Age",
        "elementType": "int",
        "defaultValue": 20
    }

.. _method:

Method
^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Method            |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents a method of a class.                                                  |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`typedElement`                                                              |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`parameters` | :ref:`code` | :ref:`owner` | :ref:`isAbstract`               |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`typedElement`.                         |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Method",
        "id": "http://www.modeling-platform/methods/m1n2o3",
        "name": "Example Method",
        "timestamp": "2025-01-20T08:30:00Z",
        "owner": "http://www.modeling-platform/classes/c1d2e3",
        "elementType": "datetime",
        "isAbstract": false,
        "parameters": [
            "http://www.modeling-platform/parameters/p1q2r3"
        ],
        "code": "return 42"
    }

Activities
~~~~~~~~~~
Modelverse define some additional activities that inherit from the 
`Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_ type.

Reclassify
^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Reclassify        |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents an activity to reclassify an element to a different type.             |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_     |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | Inherits all properties from                                                     |
|              | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_.    |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Reclassify",
        "id": "http://www.modeling-platform/activity/reclassify/a1b2c3",
        "object": "http://www.modeling-platform/modelelement/W3E3R4",
        "target": "http://www.modeling-platform/type/t1d2e3"
    }

Clone
^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Clone             |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents an activity to clone an object.                                       |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_     |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | All properties inherited from                                                    |
|              | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_.    |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Clone",
        "id": "http://www.modeling-platform/activity/clone/a1b2c3",
        "object": "http://www.modeling-platform/class/CLAS3"
    }

Actors
~~~~~~
The ActivityPub Vocabulary alredy defines a list of actors. The Modelverse Vocabulary only defines
one additional actor (Agent), which is a specialized type inherited from 
`Application <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-application>`_.

.. _agent:

Agent
^^^^^
+--------------+--------------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Agent                 |
+--------------+--------------------------------------------------------------------------------------+
| Description: | Represents an agent that acts on behalf of a user or system.                         |
+--------------+--------------------------------------------------------------------------------------+
| Extends:     | `Application <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-application>`_   |
+--------------+--------------------------------------------------------------------------------------+
| Properties:  | :ref:`interfaces` | :ref:`underlyingModel` | :ref:`adaptability` | :ref:`mediaTypes` |
|              |                                                                                      |
|              | Other properties are inherited from                                                  |
|              | `Application <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-application>`_.  |
+--------------+--------------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Agent",
        "id": "http://www.modeling-platform/agents/a1b2c3",
        "name": "AI Agent",
        "summary": "An agent acting on behalf of a user"
    }

Access Control
~~~~~~~~~~~~~~
The Modelverse Vocabulary defines a set of access control types used to manage access to
domain models.

.. _grant:

Grant
^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Grant             |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents an activity to grant access to a resource.                            |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_     |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`role`                                                                      |
|              |                                                                                  |
|              | Other properties are inherited from                                              |
|              | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_.    |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Grant",
        "id": "http://www.modeling-platform/domainmodel/grants/a1b2c3",
        "actor": "https://modeling-platform/maintainer-user",
        "to": "https://other-platform/modeler-user",,
        "target": "http://www.modeling-platform/domainmodels/m1o2d3",
        "role": "write"
    }

Revoke
^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Revoke            |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents an activity to revoke a Grant.                                        |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_     |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`grant`                                                                     |
|              |                                                                                  |
|              | Other properties are inherited from                                              |
|              | `Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_.    |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Revoke",
        "id": "http://www.modeling-platform/activity/revoke/a1b2c3",
        "actor": "https://modeling-platform/maintainer-user",
        "grant": "http://www.modeling-platform/grants/a1b2c3"
    }


Properties
----------

The following properties are used in the Modelverse Vocabulary.
In the tables below, **Domain** indicates the type object the property applies to,
**Range** indicates the type of the value of the property, and **Allow multiple** is marked
as *True* if the property can have multiple values.

.. _timestamp:

timestamp
~~~~~~~~~
+-----------------+--------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#timestamp |
+-----------------+--------------------------------------------------------------------------+
| Description:    | Represents the object creation datetime. The timestamp value should be   |
|                 | auto-generated for all kind of activities and objects.                   |
+-----------------+--------------------------------------------------------------------------+
| Domain:         | `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_ |
+-----------------+--------------------------------------------------------------------------+
| Range:          | xsd:dateTime                                                             |
+-----------------+--------------------------------------------------------------------------+
| Allow multiple: | False                                                                    |
+-----------------+--------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Class",
        "id": "http://www.modeling-platform/class/c1d2e3",
        "name": "A simple Class",
        "timestamp": "2025-01-20T08:30:00Z"
    }

.. _visibility:

visibility
~~~~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#visibility |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the visibility of a model element (e.g., public, private).     |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_  |
+-----------------+---------------------------------------------------------------------------+
| Range:          | xsd:string                                                                |
+-----------------+---------------------------------------------------------------------------+
| Allow multiple: | False                                                                     |
+-----------------+---------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Class",
        "id": "http://www.modeling-platform/classes/c1d2e3",
        "name": "A simple Class",
        "visibility": "public"
    }

.. _owner:

owner
~~~~~
+-----------------+--------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#owner     |
+-----------------+--------------------------------------------------------------------------+
| Description:    | Represents the owner of an attribute, property, method, etc.             |
+-----------------+--------------------------------------------------------------------------+
| Domain:         | :ref:`property`  | :ref:`method` | :ref:`enumerationLiteral`             |
+-----------------+--------------------------------------------------------------------------+
| Range:          | :ref:`class` | :ref:`enumeration` |                                      |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_     |
+-----------------+--------------------------------------------------------------------------+
| Allow multiple: | False                                                                    |
+-----------------+--------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Method",
        "id": "http://www.modeling-platform/methods/m1e2t3",
        "name": "average",
        "owner": "http://www.modeling-platform/classes/c1l2a3"
    }

.. _attributes:

attributes
~~~~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#attributes |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the attributes of a class.                                     |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`class`                                                              |
+-----------------+---------------------------------------------------------------------------+
| Range:          | :ref:`property` |                                                         |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_      |
+-----------------+---------------------------------------------------------------------------+
| Allow multiple: | True                                                                      |
+-----------------+---------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Class",
        "id": "http://www.modeling-platform/classes/c1d2e3",
        "name": "Library",
        "attributes": [
            "http://www.modeling-platform/attributes/a1b2c3",
            {
                "type": "Property",
                "id": "http://www.modeling-platform/properties/p1d2e3",
                "name": "location",
                "elementType": "str",
            }
        ]
    }

.. _literals:

literals
~~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#literals   |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the literals of an enumeration.                                |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`enumeration`                                                        |
+-----------------+---------------------------------------------------------------------------+
| Range:          | :ref:`enumerationLiteral` |                                               |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_      |
+-----------------+---------------------------------------------------------------------------+
| Allow multiple: | True                                                                      |
+-----------------+---------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Enumeration",
        "id": "http://www.modeling-platform/enumeration/e1f2g3",
        "name": "Metric",
        "timestamp": "2025-01-20T08:30:00Z",
        "literals": [
            "http://www.modeling-platform/enumerationliterals/l1m2n3",
            {
                "type": "EnumerationLiteral",
                "id": "http://www.modeling-platform/enumerationliterals/l3m5n7",
                "name": "temperature",
                "timestamp": "2025-01-20T08:30:00Z",
                "owner": "http://www.modeling-platform/enumerations/e1f2g3"
            }
        ]
    }

.. _multiplicity:

multiplicity
~~~~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#multiplicity      |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the multiplicity of a property.                                       |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`property`                                                                  |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:string                                                                       |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Property",
        "id": "http://www.modeling-platform/properties/p1r2op3",
        "name": "scores"
        "elementType": "int",
        "multiplicity": "0..*"
    }

.. _isComposite:

isComposite
~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isComposite       |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the property is composite.                                     |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`property`                                                                  |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:boolean                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Property",
        "id": "http://www.modeling-platform/properties/p1d2e3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/classes/t1d2e3",
        "isComposite": true
    }

.. _isNavigable:

isNavigable
~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isNavigable       |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the property is navigable.                                     |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`property`                                                                  |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:boolean                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Property",
        "id": "http://www.modeling-platform/properties/p1d2e3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/classes/t1d2e3",
        "isComposite": true,
        "isNavigable": true
    }

.. _elementType:

elementType
~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#elementType       |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the type of an element.                                               |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`typedElement`                                                              |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`class` | :ref:`enumeration` | :ref:`primitiveDataType` |                   |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+


.. note::

   In Modelverse, the following default primitive data types can be defined as strings, for simplicity:  
   "str", "int", "float", "boolean", "date", "time", "datetime", and "timedelta".

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Method",
        "id": "http://www.modeling-platform/methods/m1d2e3",
        "name": "get_alias",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "str"
    }
.. _defaultValue:

defaultValue
~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#defaultValue      |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the default value of a parameter.                                     |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`parameter`                                                                 |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:any                                                                          |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Parameter",
        "id": "http://www.modeling-platform/parameters/p1q2r3",
        "name": "age",
        "timestamp": "2025-01-20T08:30:00Z",
        "defaultValue": 20
        "elementType": "int"
    }

.. _parameters:

parameters
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#parameters        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the parameters of a method.                                           |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`method`                                                                    |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`parameter` |                                                               |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | True                                                                             |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Method",
        "id": "http://www.modeling-platform/methods/m1n2o3",
        "name": "calculateSum",
        "timestamp": "2025-01-20T08:30:00Z",
        "parameters": [
            {
                "type": "Parameter",
                "id": "http://www.modeling-platform/parameters/p1q2r3",
                "name": "a",
                "elementType": "float",
                "defaultValue": 0
            },
            {
                "type": "Parameter",
                "id": "http://www.modeling-platform/parameters/p4q5r6",
                "name": "b",
                "elementType": "int",
                "defaultValue": 0
            }
        ]
    }

.. _code:

code
~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#code              |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the code of a method.                                                 |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`method`                                                                    |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:string                                                                       |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Method",
        "id": "http://www.modeling-platform/method/m1n2o3",
        "name": "calculateSum",
        "timestamp": "2025-01-20T08:30:00Z",
        "code": "return a + b;",
        "parameters": [
            "http://www.modeling-platform/parameter/p1q2r3",
            "http://www.modeling-platform/parameter/p4q5r6"
        ]
    }

.. _methods:

methods
~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#methods    |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the methods of a class.                                        |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`class`                                                              |
+-----------------+---------------------------------------------------------------------------+
| Range:          | :ref:`method` |                                                           |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_      |
+-----------------+---------------------------------------------------------------------------+
| Allow multiple: | True                                                                      |
+-----------------+---------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Class",
        "id": "http://www.modeling-platform/classes/c1d2e3",
        "name": "Library",
        "timestamp": "2025-01-20T08:30:00Z",
        "methods": [
            "http://www.modeling-platform/methods/m1n2o3",
            {
                "type": "Method",
                "id": "http://www.modeling-platform/methods/m4n5o6",
                "name": "getBook",
                "timestamp": "2025-01-20T08:30:00Z",
                "code": "return book;",
                "elementType": "http://www.modeling-platform/classes/book1234"
                "parameters": []
            }
        ]
    }

.. _isAbstract:

isAbstract
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isAbstract        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the method or class is abstract.                               |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`method` | :ref:`class`                                                     |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:boolean                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Class",
        "id": "http://www.modeling-platform/classes/c1d2e3",
        "name": "AbstractClass",
        "timestamp": "2025-01-20T08:30:00Z",
        "isAbstract": true
    }

.. _isId:

isId
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isId              |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the property is an identifier.                                 |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`property`                                                                  |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:boolean                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Property",
        "id": "http://www.modeling-platform/properties/p1d2e3",
        "name": "identifier",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "str",
        "isId": true
    }

.. _ends:

ends
~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#ends              |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the ends of an association.                                           |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`association`                                                               |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`property` |                                                                |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | True                                                                             |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Association",
        "id": "http://www.modeling-platform/associations/a1b2c3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "ends": [
            "http://www.modeling-platform/properties/p1r2y3",
            "http://www.modeling-platform/properties/p4r5y6"
        ]
    }

.. _general:

general
~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#general           |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the general element in a generalization relationship.                 |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`generalization`                                                            |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`class` |                                                                   |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Generalization",
        "id": "http://www.modeling-platform/generalization/g1h2i3",
        "timestamp": "2025-01-20T08:30:00Z",
        "general": "http://www.modeling-platform/classes/c1d2e3",
        "specific": "http://www.modeling-platform/classes/c4d5e6"
    }

.. _specific:

specific
~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#specific          |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the specific element in a generalization relationship.                |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`generalization`                                                            |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`class` |                                                                   |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Generalization",
        "id": "http://www.modeling-platform/generalizations/g1h2i3",
        "name": "Generalization Example",
        "timestamp": "2025-01-20T08:30:00Z",
        "general": "http://www.modeling-platform/classes/c1d2e3",
        "specific": "http://www.modeling-platform/classes/c4d5e6"
    }

.. _value:

value
~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#value             |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the value of an enumeration literal.                                  |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`enumerationLiteral`                                                        |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:string                                                                       |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "EnumerationLiteral",
        "id": "http://www.modeling-platform/enumerationliterals/l1m2n3",
        "name": "Public",
        "value": "1",
        "owner": "http://www.modeling-platform/enumerations/e1f2g3"
    }

.. _generalizations:

generalizations
~~~~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#generalizations   |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the generalization relationships of a domain model.                   |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`domainModel`                                                               |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`generalization` |                                                          |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | True                                                                             |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "DomainModel",
        "id": "http://www.modeling-platform/domainmodel/m1d2e3",
        "name": "Domain Model Example",
        "generalizations": [
            "http://www.modeling-platform/generalizations/g1h2i3",
            {
                "type": "Generalization",
                "id": "http://www.modeling-platform/generalizations/g4h5i6",
                "general": "http://www.modeling-platform/classes/c7d8e9",
                "specific": "http://www.modeling-platform/classes/c1d2e3"
            }
        ]
    }

.. _elements:

elements
~~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#classes    |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the model elements contained in a package                      |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`package`                                                            |
+-----------------+---------------------------------------------------------------------------+
| Range:          | :ref:`class` |                                                            |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_      |
+-----------------+---------------------------------------------------------------------------+
| Allow multiple: | True                                                                      |
+-----------------+---------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Package",
        "id": "http://www.modeling-platform/package/p1d2e3",
        "name": "LibraryPackage",
        "elements": [
            "http://www.modeling-platform/class/c1d2e3",
            "http://www.modeling-platform/class/c1l3k4",
            "http://www.modeling-platform/class/c1b5n6"
        ]
    }

.. _types:

types
~~~~~
+-----------------+----------------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#types                   |
+-----------------+----------------------------------------------------------------------------------------+
| Description:    | Represents the types contained in a domain model including classes, enumerations, etc. |
+-----------------+----------------------------------------------------------------------------------------+
| Domain:         | :ref:`domainModel`                                                                     |
+-----------------+----------------------------------------------------------------------------------------+
| Range:          | :ref:`class` | :ref:`enumeration` | :ref:`primitivedatatype`                           |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_                   |
+-----------------+----------------------------------------------------------------------------------------+
| Allow multiple: | True                                                                                   |
+-----------------+----------------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "DomainModel",
        "id": "http://www.modeling-platform/domainmodel/a1b2c3",
        "name": "A simple Domain Model",
        "types": [
            "http://www.modeling-platform/classes/t1d2e3",
            "http://www.modeling-platform/enumerations/e1n2m3"
        ]
    }

.. _associations:

associations
~~~~~~~~~~~~
+-----------------+-----------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#associations |
+-----------------+-----------------------------------------------------------------------------+
| Description:    | Represents the associations contained in a domain model.                    |
+-----------------+-----------------------------------------------------------------------------+
| Domain:         | :ref:`domainModel`                                                          |
+-----------------+-----------------------------------------------------------------------------+
| Range:          | :ref:`association` | :ref:`binaryassociation`                               |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_        |
+-----------------+-----------------------------------------------------------------------------+
| Allow multiple: | True                                                                        |
+-----------------+-----------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "DomainModel",
        "id": "http://www.modeling-platform/domainmodels/a1b2c3",
        "name": "A simple Domain Model",
        "associations": [
            "http://www.modeling-platform/associations/a1b2c3",
            {
                "type": "BynaryAssociation",
                "id": "http://www.modeling-platform/associations/a4b5c6",
                "name": "Another Association",
                "timestamp": "2025-01-20T08:30:00Z",
                "ends": [
                    "http://www.modeling-platform/properties/p1r2y3",
                    "http://www.modeling-platform/properties/p4r5y6"
                ]
            }
        ]
    }

.. _packages:

packages
~~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#packages   |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the packages contained in a domain model.                      |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`domainModel`                                                        |
+-----------------+---------------------------------------------------------------------------+
| Range:          | :ref:`package` |                                                          |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_      |
+-----------------+---------------------------------------------------------------------------+
| Allow multiple: | True                                                                      |
+-----------------+---------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "DomainModel",
        "id": "http://www.modeling-platform/domainmodels/a1b2c3",
        "name": "A simple Domain Model",
        "packages": [
            "http://www.modeling-platform/packages/p1d2e3",
            "http://www.modeling-platform/packages/p5d6e7",
        ]
    }

.. _interfaces:

interfaces
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#interfaces        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the interfaces implemented by an agent.                               |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`agent`                                                                     |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:string                                                                       |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | True                                                                             |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Agent",
        "id": "http://www.modeling-platform/agent/a1b2c3",
        "name": "AI Agent",
        "summary": "An agent acting on behalf of a user",
        "interfaces": [
            "API",
            "CLI"
        ]
    }

.. _underlyingModel:

underlyingModel
~~~~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#underlyingModel   |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the underlying model used by an agent.                                |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`agent`                                                                     |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`domainModel`                                                               |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Agent",
        "id": "http://www.modeling-platform/agent/a1b2c3",
        "name": "AI Agent",
        "summary": "An agent acting on behalf of a user",
        "underlyingModel": "http://www.modeling-platform/domainmodel/d1e2f3"
    }

.. _adaptability:

adaptability
~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#adaptability      |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the adaptability of an agent.                                         |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`agent`                                                                     |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:boolean                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Agent",
        "id": "http://www.modeling-platform/agent/a1b2c3",
        "name": "AI Agent",
        "summary": "An agent acting on behalf of a user",
        "adaptability": true
    }

.. _mediaTypes:

mediaTypes
~~~~~~~~~~

+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#mediaTypes        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the media types supported by an agent.                                |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`agent`                                                                     |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:string                                                                       |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | True                                                                             |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Agent",
        "id": "http://www.modeling-platform/agent/a1b2c3",
        "name": "AI Agent",
        "summary": "An agent acting on behalf of a user",
        "mediaTypes": [
            "application/json",
            "text/html"
        ]
    }

.. _grants:

grants
~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#grants            |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the grants associated with a domain model.                            |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`domainModel`                                                               |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`grant` |                                                                   |
|                 | `Link <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link>`_             |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | True                                                                             |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "DomainModel",
        "id": "http://www.modeling-platform/domainmodels/a1b2c3",
        "name": "A simple Domain Model",
        "grants": [
            {
                "type": "Grant",
                "id": "http://www.modeling-platform/grants/g4h5i6",
                "actor": "https://modeling-platform/maintainer-user",
                "to": "https://other-platform/modeler-user",
                "target": "http://www.modeling-platform/domainmodels/m1o2d3",
                "role": "write"
            }
        ]
    }

Values
------
Values are predifined 

.. _role:

role
~~~~

.. _visit:

visit
^^^^^

.. _write:

write
^^^^^

.. _maintain:

maintain
^^^^^^^^

.. _admin:

admin
^^^^^

.. code-block:: json-ld
    
   {
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://BESSER-PEARL.github.io/Modelverse/ns/modelfed.jsonld"
    ],
    "type": "Create",
    "id": "http://platformA.com/activities/a4c6t8",
    "actor": "http://platformA.com/user1/",
    "to": [
        "http://platformB.com/user2/",
        "http://platformC.com/user3/"
    ],
    "object": {
        "type": "Class",
        "id": "http://platformA.com/classes/c7l8s9",
        "name": "ProductPassport",
        "attributes": [
          {
            "type": "Property",
            "id": "http://platformA.com/properties/p8b1c1",
            "name": "name",
            "elementType": "str"
          }
        ],
        "methods": []
    },
    "timestamp": "2025-04-01T15:32:45Z"
   }
