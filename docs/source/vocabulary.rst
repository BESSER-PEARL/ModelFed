Vocabulary
==========

The Modelverse Vocabulaty extends the `Activity Streams 2.0 <https://www.w3.org/TR/activitystreams-vocabulary/>`_
Vocabulary. Only additional types for federetaion of models are listed here.

The typical ``@context`` for Modelverse objects is as follows:

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
| Properties:  | :ref:`timestamp` | :ref:`types` | :ref:`associations` | :ref:`packages` | :ref:`generalizations`              |
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
| Description: | Represents a model element as part of a domain model.                                                         |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Extends:     | `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_                                      |
+--------------+---------------------------------------------------------------------------------------------------------------+
| Properties:  | :ref:`timestamp`                                                                                              |
|              |                                                                                                               |
|              | Other properties are inherited from `Object <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-object>`_. |
+--------------+---------------------------------------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "ModelElement",
        "id": "http://www.modeling-platform/modelelement/W3E3R4",
        "name": "A simple Model Element"
        "timestamp": "2025-01-20T08:30:00Z"
    }

.. _package:

Package
^^^^^^^
+--------------+------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Package |
+--------------+------------------------------------------------------------------------+
| Description: | Represents a package that groups a set of classes.                     |
+--------------+------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                    |
+--------------+------------------------------------------------------------------------+
| Properties:  | :ref:`classes`                                                         |
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
        "timestamp": "2025-01-20T08:30:00Z",
        "classes": [
            "http://www.modeling-platform/class/C1D2E3"
        ]
    }

.. _type:

Type
^^^^
+--------------+------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Type    |
+--------------+------------------------------------------------------------------------+
| Description: | Represents a type in the model.                                        |
+--------------+------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                    |
+--------------+------------------------------------------------------------------------+
| Properties:  | Inherits all properties from :ref:`modelElement`.                      |
+--------------+------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Type",
        "id": "http://www.modeling-platform/type/t1d2e3",
        "name": "A simple Type",
        "timestamp": "2025-01-20T08:30:00Z"
    }

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
| Properties:  | :ref:`attributes` | :ref:`methods` | :ref:`isAbstract` | :ref:`isReadOnly` |
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
        "timestamp": "2025-01-20T08:30:00Z",
        "attributes": [
            "http://www.modeling-platform/attribute/a1b2c3"
        ],
        "methods": []
    }

.. _dataType:

DataType
^^^^^^^^

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
        "id": "http://www.modeling-platform/enumeration/e1f2g3",
        "name": "A simple Enumeration",
        "timestamp": "2025-01-20T08:30:00Z",
        "literals": [
            "http://www.modeling-platform/enumerationliteral/l1m2n3",
            "http://www.modeling-platform/enumerationliteral/l3m5n7"
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
| Properties:  | :ref`owner`                                                                      |
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
        "id": "http://www.modeling-platform/enumerationliteral/l1m2n3",
        "name": "A simple Enumeration Literal",
        "timestamp": "2025-01-20T08:30:00Z",
        "value": "LiteralValue",
        "owner": "http://www.modeling-platform/enumeration/e1f2g3"
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
        "name": "IntegerType",
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
| Properties:  | :ref:`owner` | :ref:`multiplicity_prop` | :ref:`isComposite` | :ref:`isNavigable` | |
|              | :ref:`isId` | :ref:`isReadOnly`                                                     |
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
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
        "isId": False,
        "multiplicity": "http://www.modeling-platform/multiplicity/m1n2o3"
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
        "id": "http://www.modeling-platform/association/a1b2c3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "ends": [
            "http://www.modeling-platform/property/p1r2y3",
            "http://www.modeling-platform/property/p4r5y6"
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
        "id": "http://www.modeling-platform/binaryassociation/b1c2d3",
        "name": "belongs_to",
        "timestamp": "2025-01-20T08:30:00Z",
        "ends": [
            "http://www.modeling-platform/property/p1f2g3",
            "http://www.modeling-platform/property/p4f5g6"
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
| Properties:  | :ref:`general` | :ref:`specific` | :ref:`isDisjoint` | :ref:`isComplete`         |
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
        "id": "http://www.modeling-platform/generalization/g1h2i3",
        "timestamp": "2025-01-20T08:30:00Z",
        "general": "http://www.modeling-platform/class/c1d2e3",
        "specific": "http://www.modeling-platform/class/c4d5e6",
        "isDisjoint": True,
        "isComplete": True
    }

.. _multiplicity_obj:

Multiplicity
^^^^^^^^^^^^
+--------------+----------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Multiplicity      |
+--------------+----------------------------------------------------------------------------------+
| Description: | Represents the multiplicity of a property.                                       |
+--------------+----------------------------------------------------------------------------------+
| Extends:     | :ref:`modelElement`                                                              |
+--------------+----------------------------------------------------------------------------------+
| Properties:  | :ref:`minMultiplicity` | :ref:`maxMultiplicity`                                  |
|              |                                                                                  |
|              | Other properties are inherited from :ref:`modelElement`.                         |
+--------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Multiplicity",
        "id": "http://www.modeling-platform/multiplicity/m1n2o3",
        "timestamp": "2025-01-20T08:30:00Z",
        "minMultiplicity": 0,
        "maxMultiplicity": 1
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
        "timestamp": "2025-01-20T08:30:00Z",
        "typeElement": "http://www.modeling-platform/type/t1d2e3",
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
        "id": "http://www.modeling-platform/method/m1n2o3",
        "name": "Example Method",
        "timestamp": "2025-01-20T08:30:00Z",
        "owner": "http://www.modeling-platform/class/c1d2e3",
        "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
        "isAbstract": False,
        "parameters": [
            "http://www.modeling-platform/parameter/p1q2r3"
        ],
        "code": "return 42"
    }

Activities
~~~~~~~~~~
Modelverse define some additional activities that inherit from the 
`Activity <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-activity>`_ type.

Reclassify
^^^^^^
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

Agent
^^^^^
+--------------+--------------------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Agent                 |
+--------------+--------------------------------------------------------------------------------------+
| Description: | Represents an agent that acts on behalf of a user or system.                         |
+--------------+--------------------------------------------------------------------------------------+
| Extends:     | `Application <https://www.w3.org/TR/activitystreams-vocabulary/#dfn-application>`_   |
+--------------+--------------------------------------------------------------------------------------+
| Properties:  | :ref:`interfaces` | :ref:`underlyingModel` | :ref:`_daptability` | :ref:`mediaTypes` |
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
        "id": "http://www.modeling-platform/agent/a1b2c3",
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
        "id": "http://www.modeling-platform/domainmodel/grant/a1b2c3",
        "actor": "https://modeling-platform/maintainer-user",
        "to": "https://other-platform/modeler-user",,
        "target": "http://www.modeling-platform/domainmodel/m1o2d3",
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
| Properties:  | :ref:`grant`                                                                    |
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
        "grant": "http://www.modeling-platform/domainmodel/grant/a1b2c3"
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
| Description:    | Represents the object creation datetime.                                 |
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
        "id": "http://www.modeling-platform/class/c1d2e3",
        "name": "A simple Class",
        "timestamp": "2025-01-20T08:30:00Z",
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
        "id": "http://www.modeling-platform/method/m1e2t3",
        "name": "average",
        "timestamp": "2025-01-20T08:30:00Z",
        "owner": "http://www.modeling-platform/class/c1l2a3"
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
        "id": "http://www.modeling-platform/class/c1d2e3",
        "name": "Library",
        "timestamp": "2025-01-20T08:30:00Z",
        "attributes": [
            "http://www.modeling-platform/attribute/a1b2c3",
            {
                "type": "Property",
                "id": "http://www.modeling-platform/property/p1d2e3",
                "name": "location",
                "timestamp": "2025-01-20T08:30:00Z",
                "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
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
            "http://www.modeling-platform/enumerationliteral/l1m2n3",
            {
                "type": "EnumerationLiteral",
                "id": "http://www.modeling-platform/enumerationliteral/l3m5n7",
                "name": "temperature",
                "timestamp": "2025-01-20T08:30:00Z",
                "owner": "http://www.modeling-platform/enumeration/e1f2g3"
            }
        ]
    }


.. _minMultiplicity:

minMultiplicity
~~~~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#minMultiplicity   |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the minimum multiplicity.                                             |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`multiplicity_obj`                                                          |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:integer                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Multiplicity",
        "id": "http://www.modeling-platform/multiplicity/m1n2o3",
        "timestamp": "2025-01-20T08:30:00Z",
        "minMultiplicity": 0
        "maxMultiplicity": 1
    }

.. _maxMultiplicity:

maxMultiplicity
~~~~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#maxMultiplicity   |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the maximum multiplicity. Use 9999 for unlimited.                     |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`multiplicity_obj`                                                          |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | xsd:integer                                                                      |
+-----------------+----------------------------------------------------------------------------------+
| Allow multiple: | False                                                                            |
+-----------------+----------------------------------------------------------------------------------+

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Multiplicity",
        "id": "http://www.modeling-platform/multiplicity/m1n2o3",
        "timestamp": "2025-01-20T08:30:00Z",
        "maxMultiplicity": 0
        "maxMultiplicity": 9999
    }

.. _multiplicity_prop:

multiplicity
~~~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#multiplicity      |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Represents the multiplicity of a property.                                       |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`property`                                                                  |
+-----------------+----------------------------------------------------------------------------------+
| Range:          | :ref:`multiplicity_obj`                                                          |
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
        "id": "http://www.modeling-platform/property/p1d2e3",
        "name": "title",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
        "multiplicity": "http://www.modeling-platform/multiplicity/m1n2o3"
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
        "id": "http://www.modeling-platform/property/p1d2e3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/class/t1d2e3",
        "isComposite": True,
        "multiplicity": "http://www.modeling-platform/multiplicity/m1n2o3"
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
        "id": "http://www.modeling-platform/property/p1d2e3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/class/t1d2e3",
        "isComposite": True,
        "isNavigable": True,
        "multiplicity": "http://www.modeling-platform/multiplicity/m1n2o3"
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

.. code-block:: json-ld
    
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
        ],
        "type": "Method",
        "id": "http://www.modeling-platform/method/m1d2e3",
        "name": "get_alias",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": {
            "type": "PrimitiveDataType",
            "id": "http://www.modeling-platform/primitivedatatype/t1d2e3",
            "name": "String",
            "timestamp": "2025-01-20T08:30:00Z"
        }
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
        "id": "http://www.modeling-platform/parameter/p1q2r3",
        "name": "age",
        "timestamp": "2025-01-20T08:30:00Z",
        "defaultValue": 20
        "elementType": {
            "type": "PrimitiveDataType",
            "id": "http://www.modeling-platform/primitivedatatype/t1d2e3",
            "name": "Integer"
        }
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
        "id": "http://www.modeling-platform/method/m1n2o3",
        "name": "calculateSum",
        "timestamp": "2025-01-20T08:30:00Z",
        "parameters": [
            {
                "type": "Parameter",
                "id": "http://www.modeling-platform/parameter/p1q2r3",
                "name": "a",
                "timestamp": "2025-01-20T08:30:00Z",
                "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
                "defaultValue": 0
            },
            {
                "type": "Parameter",
                "id": "http://www.modeling-platform/parameter/p4q5r6",
                "name": "b",
                "timestamp": "2025-01-20T08:30:00Z",
                "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
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
        "id": "http://www.modeling-platform/class/c1d2e3",
        "name": "Library",
        "timestamp": "2025-01-20T08:30:00Z",
        "methods": [
            "http://www.modeling-platform/method/m1n2o3",
            {
                "type": "Method",
                "id": "http://www.modeling-platform/method/m4n5o6",
                "name": "getBooks",
                "timestamp": "2025-01-20T08:30:00Z",
                "code": "return books;",
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
        "id": "http://www.modeling-platform/class/c1d2e3",
        "name": "AbstractClass",
        "timestamp": "2025-01-20T08:30:00Z",
        "isAbstract": True
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
        "id": "http://www.modeling-platform/property/p1d2e3",
        "name": "identifier",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
        "isId": True
    }

.. _isReadOnly:

isReadOnly
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isReadOnly        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the property is read-only.                                     |
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
        "id": "http://www.modeling-platform/property/p1d2e3",
        "name": "readOnlyProperty",
        "timestamp": "2025-01-20T08:30:00Z",
        "elementType": "http://www.modeling-platform/primitivedatatype/t1d2e3",
        "isReadOnly": True
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
        "id": "http://www.modeling-platform/association/a1b2c3",
        "name": "has_books",
        "timestamp": "2025-01-20T08:30:00Z",
        "ends": [
            "http://www.modeling-platform/property/p1r2y3",
            "http://www.modeling-platform/property/p4r5y6"
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
        "general": "http://www.modeling-platform/class/c1d2e3",
        "specific": "http://www.modeling-platform/class/c4d5e6"
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
        "id": "http://www.modeling-platform/generalization/g1h2i3",
        "name": "Generalization Example",
        "timestamp": "2025-01-20T08:30:00Z",
        "general": "http://www.modeling-platform/class/c1d2e3",
        "specific": "http://www.modeling-platform/class/c4d5e6"
    }

.. _isDisjoint:

isDisjoint
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isDisjoint        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the generalization is disjoint.                                |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`generalization`                                                            |
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
        "type": "Generalization",
        "id": "http://www.modeling-platform/generalization/g1h2i3",
        "name": "Generalization Example",
        "timestamp": "2025-01-20T08:30:00Z",
        "general": "http://www.modeling-platform/class/c1d2e3",
        "specific": "http://www.modeling-platform/class/c4d5e6",
        "isDisjoint": True
    }

.. _isComplete:

isComplete
~~~~~~~~~~
+-----------------+----------------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#isComplete        |
+-----------------+----------------------------------------------------------------------------------+
| Description:    | Indicates whether the generalization is complete.                                |
+-----------------+----------------------------------------------------------------------------------+
| Domain:         | :ref:`generalization`                                                            |
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
        "type": "Generalization",
        "id": "http://www.modeling-platform/generalization/g1h2i3",
        "name": "Generalization Example",
        "timestamp": "2025-01-20T08:30:00Z",
        "general": "http://www.modeling-platform/class/c1d2e3",
        "specific": "http://www.modeling-platform/class/c4d5e6",
        "isComplete": True,
        "isDisjoint": True
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
        "timestamp": "2025-01-20T08:30:00Z",
        "generalizations": [
            "http://www.modeling-platform/generalization/g1h2i3",
            {
                "type": "Generalization",
                "id": "http://www.modeling-platform/generalization/g4h5i6",
                "timestamp": "2025-01-20T08:30:00Z",
                "general": "http://www.modeling-platform/class/c7d8e9",
                "specific": "http://www.modeling-platform/class/c1d2e3"
            }
        ]
    }

.. _classes:

classes
~~~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#classes    |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the classes contained in a package or in a domain model.       |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`package` | :ref:`domainModel`                                       |
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
        "timestamp": "2025-01-20T08:30:00Z",
        "classes": [
            "http://www.modeling-platform/class/c1d2e3",
            "http://www.modeling-platform/class/c1l3k4",
            "http://www.modeling-platform/class/c1b5n6"
        ]
    }

.. _types:

types
~~~~~
+-----------------+---------------------------------------------------------------------------+
| URI:            | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#types      |
+-----------------+---------------------------------------------------------------------------+
| Description:    | Represents the types contained in a domain model.                         |
+-----------------+---------------------------------------------------------------------------+
| Domain:         | :ref:`domainModel`                                                        |
+-----------------+---------------------------------------------------------------------------+
| Range:          | :ref:`class` | :ref:`enumeration` | :ref:`primitivedatatype`              |
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
        "id": "http://www.modeling-platform/domainmodel/a1b2c3",
        "name": "A simple Domain Model",
        "types": [
            "http://www.modeling-platform/class/t1d2e3",
            "http://www.modeling-platform/enumeration/e1n2m3",
            "http://www.modeling-platform/primitivedatatype/p1d2t3",
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
        "id": "http://www.modeling-platform/domainmodel/a1b2c3",
        "name": "A simple Domain Model",
        "associations": [
            "http://www.modeling-platform/association/a1b2c3",
            {
                "type": "BynaryAssociation",
                "id": "http://www.modeling-platform/association/a4b5c6",
                "name": "Another Association",
                "timestamp": "2025-01-20T08:30:00Z",
                "ends": [
                    "http://www.modeling-platform/property/p1r2y3",
                    "http://www.modeling-platform/property/p4r5y6"
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
        "id": "http://www.modeling-platform/domainmodel/a1b2c3",
        "name": "A simple Domain Model",
        "packages": [
            "http://www.modeling-platform/package/p1d2e3",
            "http://www.modeling-platform/package/p5d6e7",
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
        "adaptability": True
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
