#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import coding
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import identifier


class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
    
    A value set specifies a set of codes drawn from one or more code systems.
    """
    
    resource_name = "ValueSet"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.compose = None
        """ When value set includes codes from elsewhere.
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ValueSetContact` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or Publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.define = None
        """ When value set defines its own codes.
        Type `ValueSetDefine` (represented as `dict` in JSON). """
        
        self.description = None
        """ Human language description of the value set.
        Type `str`. """
        
        self.expansion = None
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.extensible = None
        """ Whether this is intended to be used with an extensible binding.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the value set (v2 / CDA).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.immutable = None
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        
        self.lockedDate = None
        """ Fixed date for all referenced code systems and value sets.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ Informal name for this value set.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None
        """ Globally unique logical id for  value set.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the value set.
        Type `str`. """
        
        super(ValueSet, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("compose", "compose", ValueSetCompose, False),
            ("contact", "contact", ValueSetContact, True),
            ("copyright", "copyright", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("define", "define", ValueSetDefine, False),
            ("description", "description", str, False),
            ("expansion", "expansion", ValueSetExpansion, False),
            ("experimental", "experimental", bool, False),
            ("extensible", "extensible", bool, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("immutable", "immutable", bool, False),
            ("lockedDate", "lockedDate", fhirdate.FHIRDate, False),
            ("name", "name", str, False),
            ("publisher", "publisher", str, False),
            ("requirements", "requirements", str, False),
            ("status", "status", str, False),
            ("url", "url", str, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True),
            ("version", "version", str, False),
        ])
        return js


class ValueSetCompose(fhirelement.FHIRElement):
    """ When value set includes codes from elsewhere.
    """
    
    resource_name = "ValueSetCompose"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.exclude = None
        """ Explicitly exclude codes.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.importFrom = None
        """ Import the contents of another value set.
        List of `str` items. """
        
        self.include = None
        """ Include one or more codes from a code system.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ValueSetComposeInclude, True),
            ("importFrom", "import", str, True),
            ("include", "include", ValueSetComposeInclude, True),
        ])
        return js


class ValueSetComposeInclude(fhirelement.FHIRElement):
    """ Include one or more codes from a code system.
    """
    
    resource_name = "ValueSetComposeInclude"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        self.system = None
        """ The system the codes come from.
        Type `str`. """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        
        super(ValueSetComposeInclude, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("concept", "concept", ValueSetComposeIncludeConcept, True),
            ("filter", "filter", ValueSetComposeIncludeFilter, True),
            ("system", "system", str, False),
            ("version", "version", str, False),
        ])
        return js


class ValueSetComposeIncludeConcept(fhirelement.FHIRElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    resource_name = "ValueSetComposeIncludeConcept"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code or expression from system.
        Type `str`. """
        
        self.designation = None
        """ Additional representations for this valueset.
        List of `ValueSetDefineConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ Test to display for this code for this value set.
        Type `str`. """
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("designation", "designation", ValueSetDefineConceptDesignation, True),
            ("display", "display", str, False),
        ])
        return js


class ValueSetComposeIncludeFilter(fhirelement.FHIRElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """
    
    resource_name = "ValueSetComposeIncludeFilter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.op = None
        """ = | is-a | is-not-a | regex | in | not-in.
        Type `str`. """
        
        self.property = None
        """ A property defined by the code system.
        Type `str`. """
        
        self.value = None
        """ Code from the system, or regex criteria.
        Type `str`. """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("op", "op", str, False),
            ("property", "property", str, False),
            ("value", "value", str, False),
        ])
        return js


class ValueSetContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ValueSetContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ValueSetContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class ValueSetDefine(fhirelement.FHIRElement):
    """ When value set defines its own codes.
    
    A definition of an code system, inlined into the value set.
    """
    
    resource_name = "ValueSetDefine"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.caseSensitive = None
        """ If code comparison is case sensitive.
        Type `bool`. """
        
        self.concept = None
        """ Concepts in the code system.
        List of `ValueSetDefineConcept` items (represented as `dict` in JSON). """
        
        self.system = None
        """ URI to identify the code system.
        Type `str`. """
        
        self.version = None
        """ Version of this system.
        Type `str`. """
        
        super(ValueSetDefine, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetDefine, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False),
            ("concept", "concept", ValueSetDefineConcept, True),
            ("system", "system", str, False),
            ("version", "version", str, False),
        ])
        return js


class ValueSetDefineConcept(fhirelement.FHIRElement):
    """ Concepts in the code system.
    """
    
    resource_name = "ValueSetDefineConcept"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abstract = None
        """ If this code is not for use as a real concept.
        Type `bool`. """
        
        self.code = None
        """ Code that identifies concept.
        Type `str`. """
        
        self.concept = None
        """ Child Concepts (is-a / contains).
        List of `ValueSetDefineConcept` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Formal Definition.
        Type `str`. """
        
        self.designation = None
        """ Additional representations for the concept.
        List of `ValueSetDefineConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ Text to Display to the user.
        Type `str`. """
        
        super(ValueSetDefineConcept, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetDefineConcept, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False),
            ("code", "code", str, False),
            ("concept", "concept", ValueSetDefineConcept, True),
            ("definition", "definition", str, False),
            ("designation", "designation", ValueSetDefineConceptDesignation, True),
            ("display", "display", str, False),
        ])
        return js


class ValueSetDefineConceptDesignation(fhirelement.FHIRElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialised purposes, used for particular purposes, etc.
    """
    
    resource_name = "ValueSetDefineConceptDesignation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.language = None
        """ Language of the designation.
        Type `str`. """
        
        self.use = None
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The text value for this designation.
        Type `str`. """
        
        super(ValueSetDefineConceptDesignation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetDefineConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False),
            ("use", "use", coding.Coding, False),
            ("value", "value", str, False),
        ])
        return js


class ValueSetExpansion(fhirelement.FHIRElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    resource_name = "ValueSetExpansion"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contains = None
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Uniquely identifies this expansion.
        Type `str`. """
        
        self.parameter = None
        """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        
        self.timestamp = None
        """ Time valueset expansion happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ValueSetExpansion, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("contains", "contains", ValueSetExpansionContains, True),
            ("identifier", "identifier", str, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False),
        ])
        return js


class ValueSetExpansionContains(fhirelement.FHIRElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    resource_name = "ValueSetExpansionContains"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abstract = None
        """ If user cannot select this entry.
        Type `bool`. """
        
        self.code = None
        """ Code - if blank, this is not a choosable code.
        Type `str`. """
        
        self.contains = None
        """ Codes contained in this concept.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.display = None
        """ User display for the concept.
        Type `str`. """
        
        self.system = None
        """ System value for the code.
        Type `str`. """
        
        self.version = None
        """ Version in which this code / display is defined.
        Type `str`. """
        
        super(ValueSetExpansionContains, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False),
            ("code", "code", str, False),
            ("contains", "contains", ValueSetExpansionContains, True),
            ("display", "display", str, False),
            ("system", "system", str, False),
            ("version", "version", str, False),
        ])
        return js


class ValueSetExpansionParameter(fhirelement.FHIRElement):
    """ Parameter that controlled the expansion process.
    
    A Parameter that controlled the expansion process. These paameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    
    resource_name = "ValueSetExpansionParameter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name as assigned by server.
        Type `str`. """
        
        self.valueBoolean = None
        """ Value of the parameter.
        Type `bool`. """
        
        self.valueCode = None
        """ Value of the parameter.
        Type `str`. """
        
        self.valueDecimal = None
        """ Value of the parameter.
        Type `float`. """
        
        self.valueInteger = None
        """ Value of the parameter.
        Type `int`. """
        
        self.valueString = None
        """ Value of the parameter.
        Type `str`. """
        
        self.valueUri = None
        """ Value of the parameter.
        Type `str`. """
        
        super(ValueSetExpansionParameter, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCode", "valueCode", str, False),
            ("valueDecimal", "valueDecimal", float, False),
            ("valueInteger", "valueInteger", int, False),
            ("valueString", "valueString", str, False),
            ("valueUri", "valueUri", str, False),
        ])
        return js

