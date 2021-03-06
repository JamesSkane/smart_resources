#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import bundle
from .fhirdate import FHIRDate


class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)
    
    def testBundle1(self):
        inst = self.instantiate_from("bundle-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle1(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)
    
    def implBundle1(self, inst):
        self.assertEqual(inst.base, "http://example.com/base")
        self.assertEqual(inst.entry[0].resource.id, "3123")
        self.assertEqual(inst.entry[0].search.mode, "match")
        self.assertEqual(inst.entry[0].search.score, 1)
        self.assertEqual(inst.entry[1].resource.id, "example")
        self.assertEqual(inst.entry[1].search.mode, "include")
        self.assertEqual(inst.id, "bundle-example")
        self.assertEqual(inst.link[0].relation, "self")
        self.assertEqual(inst.link[0].url, "https://example.com/base/MedicationPrescription?patient=347&_include=MedicationPrescription.medication")
        self.assertEqual(inst.link[1].relation, "next")
        self.assertEqual(inst.link[1].url, "https://example.com/base/MedicationPrescription?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-08-18T01:43:30Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-08-18T01:43:30Z")
        self.assertEqual(inst.total, 3)
        self.assertEqual(inst.type, "searchset")
    
    def testBundle2(self):
        inst = self.instantiate_from("diagnosticreport-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle2(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)
    
    def implBundle2(self, inst):
        self.assertEqual(inst.base, "http://hl7.org/fhir")
        self.assertEqual(inst.entry[0].resource.id, "3")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[1].resource.id, "4")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[2].resource.id, "5")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[3].resource.id, "6")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[4].resource.id, "7")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[5].resource.id, "8")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[6].resource.id, "9")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[7].resource.id, "15")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[8].resource.id, "16")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[9].resource.id, "17")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.id, "72ac8493-52ac-41bd-8d5d-7258c289b5ea")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle3(self):
        inst = self.instantiate_from("diagnosticreport-examples-lab-text.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle3(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)
    
    def implBundle3(self, inst):
        self.assertEqual(inst.base, "http://hl7.org/fhir")
        self.assertEqual(inst.entry[0].resource.id, "103")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[1].resource.id, "104")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[2].resource.id, "105")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[3].resource.id, "106")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[4].resource.id, "107")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[5].resource.id, "108")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[6].resource.id, "109")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[7].resource.id, "110")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[8].resource.id, "111")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.entry[9].resource.id, "112")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.id, "72ac8493-52ac-41bd-8d5d-7258c289b5ea")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle4(self):
        inst = self.instantiate_from("document-example-dischargesummary.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle4(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)
    
    def implBundle4(self, inst):
        self.assertEqual(inst.base, "http://fhir.healthintersections.com.au/open")
        self.assertEqual(inst.entry[0].base, "urn:uuid:")
        self.assertEqual(inst.entry[0].resource.id, "180f219f-97a8-486d-99d9-ed631fe4fc57")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(inst.entry[1].resource.id, "example")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[2].resource.id, "d1")
        self.assertEqual(inst.entry[3].resource.id, "doc-example")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[4].base, "urn:uuid:")
        self.assertEqual(inst.entry[4].resource.id, "d0dd51d3-3ab2-4c84-b697-a630c3e40e7a")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[5].base, "urn:uuid:")
        self.assertEqual(inst.entry[5].resource.id, "541a72a8-df75-4484-ac89-ac4923f03b81")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[6].base, "urn:uuid:")
        self.assertEqual(inst.entry[6].resource.id, "673f8db5-0ffd-4395-9657-6da00420bbc1")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[7].base, "urn:uuid:")
        self.assertEqual(inst.entry[7].resource.id, "124a6916-5d84-4b8c-b250-10cefb8e6e86")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[8].base, "urn:uuid:")
        self.assertEqual(inst.entry[8].resource.id, "68f86194-e6e1-4f65-b64a-5314256f8d7b")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[9].base, "urn:uuid:")
        self.assertEqual(inst.entry[9].resource.id, "47600e0f-b6b5-4308-84b5-5dec157f7637")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.id, "father")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(inst.meta.tag[0].code, "document")
        self.assertEqual(inst.meta.tag[0].system, "http://hl7.org/fhir/tag")
        self.assertEqual(inst.type, "document")
    
    def testBundle5(self):
        inst = self.instantiate_from("observation-example-bloodpressure.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle5(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)
    
    def implBundle5(self, inst):
        self.assertEqual(inst.base, "http://hl7.org/fhir")
        self.assertEqual(inst.entry[0].resource.id, "34252345234")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.entry[1].resource.id, "34252345234-s")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.entry[2].resource.id, "34252345234-d")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.id, "blood-pressure")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-01-30T22:35:23+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-01-30T22:35:23+11:00")
        self.assertEqual(inst.type, "collection")
    
    def testBundle6(self):
        inst = self.instantiate_from("patient-examples-cypress-template.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle6(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)
    
    def implBundle6(self, inst):
        self.assertEqual(inst.base, "http://hl7.org/fhir")
        self.assertEqual(inst.entry[0].resource.id, "71")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[1].resource.id, "72")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[2].resource.id, "73")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[3].resource.id, "74")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[4].resource.id, "75")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[5].resource.id, "76")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[6].resource.id, "77")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[7].resource.id, "78")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[8].resource.id, "79")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.entry[9].resource.id, "80")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-06-03T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-06-03T23:45:32Z")
        self.assertEqual(inst.id, "b0a5e4277-83c4-4adb-87e2-e3efe3369b6f")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle7(self):
        inst = self.instantiate_from("patient-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle7(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)
    
    def implBundle7(self, inst):
        self.assertEqual(inst.base, "http://hl7.org/fhir")
        self.assertEqual(inst.entry[0].resource.id, "1")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[1].resource.id, "2")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[2].resource.id, "3")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[3].resource.id, "4")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[4].resource.id, "5")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[5].resource.id, "6")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[6].resource.id, "7")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[7].resource.id, "8")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[8].resource.id, "9")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[9].resource.id, "10")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.id, "b248b1b2-1686-4b94-9936-37d7a5f94b51")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle8(self):
        inst = self.instantiate_from("practitioner-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle8(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)
    
    def implBundle8(self, inst):
        self.assertEqual(inst.base, "http://hl7.org/fhir")
        self.assertEqual(inst.entry[0].resource.id, "13")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[1].resource.id, "14")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[2].resource.id, "15")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[3].resource.id, "16")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[4].resource.id, "17")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[5].resource.id, "18")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[6].resource.id, "19")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[7].resource.id, "20")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[8].resource.id, "21")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[9].resource.id, "22")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.id, "3ad0687e-f477-468c-afd5-fcc2bf897809")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle9(self):
        inst = self.instantiate_from("questionnaire-sdc-profile-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle9(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)
    
    def implBundle9(self, inst):
        self.assertEqual(inst.base, "http://AHRQ.org/form")
        self.assertEqual(inst.entry[0].resource.extension[0].url, "http://hl7.org/fhir/StructureDefinition/questionnaire-category")
        self.assertEqual(inst.entry[0].resource.extension[0].valueCodeableConcept.coding[0].code, "Acute Care Hospitals")
        self.assertEqual(inst.entry[0].resource.id, "F8-1.2")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2014-05-15T17:25:15Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2014-05-15T17:25:15Z")
        self.assertEqual(inst.entry[1].resource.id, "HERF-1.2")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2014-05-15T17:25:15Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2014-05-15T17:25:15Z")
        self.assertEqual(inst.entry[2].resource.extension[0].url, "http://hl7.org/fhir/StructureDefinition/questionnaire-category")
        self.assertEqual(inst.entry[2].resource.extension[0].valueCodeableConcept.coding[0].code, "CRF")
        self.assertEqual(inst.entry[2].resource.id, "3921052v1.0")
        self.assertEqual(inst.entry[2].resource.language, "en")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2014-05-15T17:25:15Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2014-05-15T17:25:15Z")
        self.assertEqual(inst.entry[3].resource.extension[0].url, "http://hl7.org/fhir/StructureDefinition/questionnaire-category")
        self.assertEqual(inst.entry[3].resource.extension[0].valueCodeableConcept.coding[0].code, "CRF")
        self.assertEqual(inst.entry[3].resource.extension[1].url, "http://hl7.org/fhir/StructureDefinition/questionnaire-category")
        self.assertEqual(inst.entry[3].resource.extension[1].valueCodeableConcept.coding[0].code, "Demographic")
        self.assertEqual(inst.entry[3].resource.id, "2674812v4.0")
        self.assertEqual(inst.entry[3].resource.language, "en")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2014-05-15T17:25:15Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2014-05-15T17:25:15Z")
        self.assertEqual(inst.entry[4].resource.extension[0].url, "http://hl7.org/fhir/StructureDefinition/questionnaire-category")
        self.assertEqual(inst.entry[4].resource.extension[0].valueCodeableConcept.coding[0].code, "CRF")
        self.assertEqual(inst.entry[4].resource.id, "3265657v2.0")
        self.assertEqual(inst.entry[4].resource.language, "en")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2014-05-15T17:25:15Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2014-05-15T17:25:15Z")
        self.assertEqual(inst.id, "sdc")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-05-15T17:25:15Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-05-15T17:25:15Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle10(self):
        inst = self.instantiate_from("xds-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle10(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)
    
    def implBundle10(self, inst):
        self.assertEqual(inst.base, "cid:123@healthintersections.com.au")
        self.assertEqual(inst.entry[0].resource.id, "a1")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[0].transaction.method, "POST")
        self.assertEqual(inst.entry[0].transaction.url, "DocumentReference")
        self.assertEqual(inst.entry[1].resource.id, "a2")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[1].transaction.ifNoneExist, "Patient?identifier=http://acme.org/xds/patients!89765a87b")
        self.assertEqual(inst.entry[1].transaction.method, "POST")
        self.assertEqual(inst.entry[1].transaction.url, "Patient")
        self.assertEqual(inst.entry[2].resource.id, "a3")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[2].transaction.method, "POST")
        self.assertEqual(inst.entry[2].transaction.url, "Practitioner")
        self.assertEqual(inst.entry[3].resource.id, "a4")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[3].transaction.method, "POST")
        self.assertEqual(inst.entry[3].transaction.url, "Practitioner")
        self.assertEqual(inst.entry[4].resource.id, "1e404af3-077f-4bee-b7a6-a9be97e1ce32")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[4].transaction.method, "POST")
        self.assertEqual(inst.entry[4].transaction.url, "Binary")
        self.assertEqual(inst.id, "xds")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.type, "transaction")

