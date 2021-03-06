#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import timing


class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
    
    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    
    resource_name = "DeviceMetric"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.calibration = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        
        self.category = None
        """ measurement | setting | calculation | unspecified.
        Type `str`. """
        
        self.color = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """
        
        self.identifier = None
        """ Unique identifier of this DeviceMetric.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measurementPeriod = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.operationalStatus = None
        """ on | off | standby.
        Type `str`. """
        
        self.parent = None
        """ Describes the link to the parent DeviceComponent.
        Type `FHIRReference` referencing `DeviceComponent` (represented as `dict` in JSON). """
        
        self.source = None
        """ Describes the link to the source Device.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Unit of metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceMetric, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, True),
            ("category", "category", str, False),
            ("color", "color", str, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("measurementPeriod", "measurementPeriod", timing.Timing, False),
            ("operationalStatus", "operationalStatus", str, False),
            ("parent", "parent", fhirreference.FHIRReference, False),
            ("source", "source", fhirreference.FHIRReference, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False),
        ])
        return js


class DeviceMetricCalibration(fhirelement.FHIRElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    
    resource_name = "DeviceMetricCalibration"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.state = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """
        
        self.time = None
        """ Describes the time last calibration has been performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.type = None
        """ unspecified | offset | gain | two-point.
        Type `str`. """
        
        super(DeviceMetricCalibration, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, False),
            ("time", "time", fhirdate.FHIRDate, False),
            ("type", "type", str, False),
        ])
        return js

