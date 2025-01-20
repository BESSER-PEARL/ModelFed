Vocabulary
==========

The Modelverse Vocabulaty extends the `Activity Streams 2.0 <https://www.w3.org/TR/activitystreams-vocabulary/>`_
and `ForgeFed <https://forgefed.org/spec/#vocab>`_ Vocabularies. Only additional types for federetaion of models 
are presentes below.

The typical ``@context`` for Modelverse objects are as follows:

.. code-block:: json

    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://forgefed.org/ns",
        "https://BESSER-PEARL.github.io/Modelverse/ns"
    ]




Objects for Structural models
-----------------------------

+------------------------+---------------+------------------------------------------------------+
| Object                 | Description   | Example                                              |
+========================+===============+======================================================+
| *DomainModel*          | URI:            | .. code-block:: json-ld                              |
|                        +---------------+                                                      |
|                        | Notes         |     {                                                |
|                        +---------------+         "@context": [                                |
|                        | Extends       |             "https://www.w3.org/ns/activitystreams", |
|                        +---------------+                                                      |
|                        | Properties    |                                                      |
+------------------------+---------------+------------------------------------------------------+
| *ModelElement*         | Cells may span columns.                                              |
+------------------------+---------------+------------------------------------------------------+


DomainModel
~~~~~~~~~~~
Description of DomainModel.

ModelElement
~~~~~~~~~~~~
Description of ModelElement.

Package
~~~~~~~
Description of Package.

Type
~~~~
Description of Type.

Class
~~~~~
Description of Class.

DataType
~~~~~~~~
Description of DataType.

Enumeration
~~~~~~~~~~~
Description of Enumeration.

EnumerationLiteral
~~~~~~~~~~~~~~~~~~
Description of EnumerationLiteral.

PrimitiveDataType
~~~~~~~~~~~~~~~~~
Description of PrimitiveDataType.

TypedElement
~~~~~~~~~~~~
Description of TypedElement.

Property
~~~~~~~~
Description of Property.

Association
~~~~~~~~~~~
Description of Association.

BinaryAssociation
~~~~~~~~~~~~~~~~~
Description of BinaryAssociation.

Multiplicity
~~~~~~~~~~~~
Description of Multiplicity.

Method
~~~~~~
Description of Method.

Parameter
~~~~~~~~~
Description of Parameter.
