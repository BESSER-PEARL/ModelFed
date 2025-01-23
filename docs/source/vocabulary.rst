Vocabulary
==========

The Modelverse Vocabulaty extends the `Activity Streams 2.0 <https://www.w3.org/TR/activitystreams-vocabulary/>`_
Vocabulary. Only additional types for federetaion of models are listed.

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

.. _domain-model:

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

.. _model-element:

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

Package
^^^^^^^
+--------------+------------------------------------------------------------------------+
| URI:         | https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld#Package |
+--------------+------------------------------------------------------------------------+
| Description: | Represents a package that groups a set of classes.                     |
+--------------+------------------------------------------------------------------------+
| Extends:     | :ref:`model-element`                                                   |
+--------------+------------------------------------------------------------------------+
| Properties:  | :ref:`classes`                                                         |
|              |                                                                        |
|              | Other properties are inherited from :ref:`model-element`.              |
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

Type
^^^^
Description of Type.

Class
^^^^^
Description of Class.

DataType
^^^^^^^^
Description of DataType.

Enumeration
^^^^^^^^^^^
Description of Enumeration.

EnumerationLiteral
^^^^^^^^^^^^^^^^^^
Description of EnumerationLiteral.

PrimitiveDataType
^^^^^^^^^^^^^^^^^
Description of PrimitiveDataType.

TypedElement
^^^^^^^^^^^^
Description of TypedElement.

Property
^^^^^^^^
Description of Property.

Association
^^^^^^^^^^^
Description of Association.

BinaryAssociation
^^^^^^^^^^^^^^^^^
Description of BinaryAssociation.

Multiplicity
^^^^^^^^^^^^
Description of Multiplicity.

Method
^^^^^^
Description of Method.

Parameter
^^^^^^^^^
Description of Parameter.

Properties
----------

.. _timestamp:

timestamp
~~~~~~~~~

.. _visibility:

visibility
~~~~~~~~~~

.. _owner:

owner
~~~~~

.. _literals:

literals
~~~~~~~~

.. _minMultiplicity:

minMultiplicity
~~~~~~~~~~~~~~~

.. _maxMultiplicity:

maxMultiplicity
~~~~~~~~~~~~~~~

.. _multiplicity:

multiplicity
~~~~~~~~~~~~

.. _isComposite:

isComposite
~~~~~~~~~~~

.. _isNavigable:

isNavigable
~~~~~~~~~~~

.. _typeElement:

typeElement
~~~~~~~~~~~

.. _defaultValue:

defaultValue
~~~~~~~~~~~~
Description of defaultValue.

.. _parameters:

parameters
~~~~~~~~~~
Description of parameters.

.. _code:

code
~~~~
Description of code.

.. _methods:

methods
~~~~~~~
Description of methods.

.. _isAbstract:

isAbstract
~~~~~~~~~~
Description of isAbstract.

.. _isReadOnly:

isReadOnly
~~~~~~~~~~
Description of isReadOnly.

.. _ends:

ends
~~~~
Description of ends.

.. _association:

association
~~~~~~~~~~~
Description of association.

.. _general:

general
~~~~~~~
Description of general.

.. _specific:

specific
~~~~~~~~
Description of specific.

.. _generalizations:

generalizations
~~~~~~~~~~~~~~~
Description of generalizations.

.. _isDisjoint:

isDisjoint
~~~~~~~~~~
Description of isDisjoint.

.. _isComplete:

isComplete
~~~~~~~~~~
Description of isComplete.

.. _classes:

classes
~~~~~~~
Description of classes.

.. _types:

types
~~~~~
Description of types.

.. _associations:

associations
~~~~~~~~~~~~
Description of associations.

.. _packages:

packages
~~~~~~~~
Description of packages.

.. _value:

value
~~~~~
Description of value.

