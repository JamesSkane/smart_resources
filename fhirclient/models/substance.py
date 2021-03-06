#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Substance) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """
    
    resource_name = "Substance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Textual description of the substance, comments.
        Type `str`. """
        
        self.ingredient = None
        """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ If this describes a specific package/container of the substance.
        Type `SubstanceInstance` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Substance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("ingredient", "ingredient", SubstanceIngredient, True),
            ("instance", "instance", SubstanceInstance, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class SubstanceIngredient(fhirelement.FHIRElement):
    """ Composition information about the substance.
    
    A substance can be composed of other substances.
    """
    
    resource_name = "SubstanceIngredient"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.quantity = None
        """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.substance = None
        """ A component of the substance.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        super(SubstanceIngredient, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False),
            ("substance", "substance", fhirreference.FHIRReference, False),
        ])
        return js


class SubstanceInstance(fhirelement.FHIRElement):
    """ If this describes a specific package/container of the substance.
    
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    
    resource_name = "SubstanceInstance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.expiry = None
        """ When no longer valid to use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount of substance in the package.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SubstanceInstance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", fhirdate.FHIRDate, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("quantity", "quantity", quantity.Quantity, False),
        ])
        return js

