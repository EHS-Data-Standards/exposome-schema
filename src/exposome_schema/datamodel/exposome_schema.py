# Auto generated from exposome_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-23T14:29:23
# Schema: exposome-schema
#
# id: https://w3id.org/diatomsRcool/exposome-schema
# description: Comprehensive exposome schema for integrating chemical exposures, environmental factors,
#   dietary data, toxicology databases, and health outcomes with support for Adverse Outcome
#   Pathways (AOPs) and multi-granularity measurements
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
AOPWIKI = CurieNamespace('AOPWIKI', 'https://aopwiki.org/aops/')
CARO = CurieNamespace('CARO', 'http://example.org/UNKNOWN/CARO/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CTD_CHEMICAL = CurieNamespace('CTD_CHEMICAL', 'http://ctdbase.org/detail.go?type=chem&acc=')
CTD_GENE = CurieNamespace('CTD_GENE', 'http://ctdbase.org/detail.go?type=gene&acc=')
DTXSID = CurieNamespace('DTXSID', 'https://comptox.epa.gov/dashboard/dsstoxdb/results?search=')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
EXO = CurieNamespace('ExO', 'http://example.org/UNKNOWN/ExO/')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
GWAS = CurieNamespace('GWAS', 'https://www.ebi.ac.uk/gwas/studies/')
GXA = CurieNamespace('GXA', 'https://www.ebi.ac.uk/gxa/experiments/')
HHEAR = CurieNamespace('HHEAR', 'http://hadatac.org/ont/hhear#')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MP = CurieNamespace('MP', 'http://purl.obolibrary.org/obo/MP_')
NCBIGENE = CurieNamespace('NCBIGENE', 'https://www.ncbi.nlm.nih.gov/gene/')
NHANES = CurieNamespace('NHANES', 'https://wwwn.cdc.gov/Nchs/Nhanes/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
USDA_PESTICIDE = CurieNamespace('USDA_PESTICIDE', 'https://www.ams.usda.gov/datasets/pdp/')
XCO = CurieNamespace('XCO', 'http://example.org/UNKNOWN/XCO/')
ZP = CurieNamespace('ZP', 'http://purl.obolibrary.org/obo/ZP_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CHEAR = CurieNamespace('chear', 'http://hadatac.org/ont/chear#')
EXPOSOME_SCHEMA = CurieNamespace('exposome_schema', 'https://w3id.org/diatomsRcool/exposome-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = EXPOSOME_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class StimulusEntityId(NamedThingId):
    pass


class ChemicalEntityId(StimulusEntityId):
    pass


class BehavioralEntityId(StimulusEntityId):
    pass


class DietEntityId(StimulusEntityId):
    pass


class BiologicalResponseId(NamedThingId):
    pass


class HealthOutcomeId(BiologicalResponseId):
    pass


class StudyEntityId(NamedThingId):
    pass


class MeasurementId(NamedThingId):
    pass


class AssociationId(NamedThingId):
    pass


class ExposureId(NamedThingId):
    pass


class ActiveExposureId(ExposureId):
    pass


class PassiveExposureId(ExposureId):
    pass


class ChemicalExposureId(ExposureId):
    pass


class DietaryExposureId(ExposureId):
    pass


class OccupationalExposureId(ExposureId):
    pass


class ExperimentalExposureId(ExposureId):
    pass


class PrenatalExposureId(ExposureId):
    pass


class BehavioralExposureId(ExposureId):
    pass


class SesExposureId(ExposureId):
    pass


class PhenotypeId(HealthOutcomeId):
    pass


class DiseaseId(HealthOutcomeId):
    pass


class AdverseOutcomeId(HealthOutcomeId):
    pass


class MammalianPhenotypeId(PhenotypeId):
    pass


class ZebrafishPhenotypeId(PhenotypeId):
    pass


class HumanPhenotypeId(PhenotypeId):
    pass


class AdverseOutcomePathwayId(NamedThingId):
    pass


class MolecularInitiatingEventId(BiologicalResponseId):
    pass


class KeyEventId(BiologicalResponseId):
    pass


class KeyEventRelationshipId(AssociationId):
    pass


class StudyId(StudyEntityId):
    pass


class CohortId(StudyEntityId):
    pass


class ParticipantId(StudyEntityId):
    pass


class ExposureMeasurementId(MeasurementId):
    pass


class BiomarkerMeasurementId(MeasurementId):
    pass


class PhenotypeMeasurementId(MeasurementId):
    pass


class AggregatedMeasurementId(MeasurementId):
    pass


class GeneId(BiologicalEntityId):
    pass


class ProteinId(BiologicalEntityId):
    pass


class CellId(BiologicalEntityId):
    pass


class AnatomicalEntityId(BiologicalEntityId):
    pass


class OrganismId(BiologicalEntityId):
    pass


class PopulationId(BiologicalEntityId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class GeneticVariantToPhenotypeAssociationId(AssociationId):
    pass


@dataclass(repr=False)
class ExposureEvent(YAMLRoot):
    """
    An event in which a BiologicalEntity is exposed to a StimulusEntity and results in a BiologicalResponse
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposureEvent"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposureEvent

    exposure_stimulus: Union[str, StimulusEntityId] = None
    exposure_outcome: Union[str, BiologicalResponseId] = None
    exposure_receiver: Union[str, BiologicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.exposure_stimulus):
            self.MissingRequiredField("exposure_stimulus")
        if not isinstance(self.exposure_stimulus, StimulusEntityId):
            self.exposure_stimulus = StimulusEntityId(self.exposure_stimulus)

        if self._is_empty(self.exposure_outcome):
            self.MissingRequiredField("exposure_outcome")
        if not isinstance(self.exposure_outcome, BiologicalResponseId):
            self.exposure_outcome = BiologicalResponseId(self.exposure_outcome)

        if self._is_empty(self.exposure_receiver):
            self.MissingRequiredField("exposure_receiver")
        if not isinstance(self.exposure_receiver, BiologicalEntityId):
            self.exposure_receiver = BiologicalEntityId(self.exposure_receiver)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity in the exposome
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[Union[str, list[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, str) else str(v) for v in self.category]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalEntity(NamedThing):
    """
    Biological entities including genes, proteins, cells, and anatomical structures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CARO["0030000"]
    class_class_curie: ClassVar[str] = "CARO:0030000"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalEntityId):
            self.id = BiologicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StimulusEntity(NamedThing):
    """
    Any entity to which a receiver is being exposed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["StimulusEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:StimulusEntity"
    class_name: ClassVar[str] = "StimulusEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.StimulusEntity

    id: Union[str, StimulusEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StimulusEntityId):
            self.id = StimulusEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(StimulusEntity):
    """
    A chemical entity including compounds, drugs, and metabolites
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["24431"]
    class_class_curie: ClassVar[str] = "CHEBI:24431"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    chebi_id: Optional[Union[str, URIorCURIE]] = None
    dtxsid: Optional[str] = None
    chembl_id: Optional[str] = None
    pubchem_cid: Optional[int] = None
    cas_number: Optional[str] = None
    inchi: Optional[str] = None
    smiles: Optional[str] = None
    molecular_formula: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.chebi_id is not None and not isinstance(self.chebi_id, URIorCURIE):
            self.chebi_id = URIorCURIE(self.chebi_id)

        if self.dtxsid is not None and not isinstance(self.dtxsid, str):
            self.dtxsid = str(self.dtxsid)

        if self.chembl_id is not None and not isinstance(self.chembl_id, str):
            self.chembl_id = str(self.chembl_id)

        if self.pubchem_cid is not None and not isinstance(self.pubchem_cid, int):
            self.pubchem_cid = int(self.pubchem_cid)

        if self.cas_number is not None and not isinstance(self.cas_number, str):
            self.cas_number = str(self.cas_number)

        if self.inchi is not None and not isinstance(self.inchi, str):
            self.inchi = str(self.inchi)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.molecular_formula is not None and not isinstance(self.molecular_formula, str):
            self.molecular_formula = str(self.molecular_formula)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BehavioralEntity(StimulusEntity):
    """
    A stimulus entity representing a behavior, activity, or lifestyle factor (e.g. smoking, physical activity, sleep)
    to which an individual may be exposed or that may mediate an exposure
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["BehavioralEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:BehavioralEntity"
    class_name: ClassVar[str] = "BehavioralEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.BehavioralEntity

    id: Union[str, BehavioralEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralEntityId):
            self.id = BehavioralEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DietEntity(StimulusEntity):
    """
    A stimulus entity representing a food, beverage, dietary pattern, or nutritional component consumed by an
    individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["DietEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:DietEntity"
    class_name: ClassVar[str] = "DietEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.DietEntity

    id: Union[str, DietEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DietEntityId):
            self.id = DietEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalResponse(NamedThing):
    """
    A biological response at the molecular, cellular, or tissue level
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["BiologicalResponse"]
    class_class_curie: ClassVar[str] = "exposome_schema:BiologicalResponse"
    class_name: ClassVar[str] = "BiologicalResponse"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.BiologicalResponse

    id: Union[str, BiologicalResponseId] = None

@dataclass(repr=False)
class HealthOutcome(BiologicalResponse):
    """
    A health-related outcome including phenotypes and diseases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["HealthOutcome"]
    class_class_curie: ClassVar[str] = "exposome_schema:HealthOutcome"
    class_name: ClassVar[str] = "HealthOutcome"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.HealthOutcome

    id: Union[str, HealthOutcomeId] = None

@dataclass(repr=False)
class StudyEntity(NamedThing):
    """
    Entities related to studies, cohorts, and participants
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["StudyEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:StudyEntity"
    class_name: ClassVar[str] = "StudyEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.StudyEntity

    id: Union[str, StudyEntityId] = None

@dataclass(repr=False)
class Measurement(NamedThing):
    """
    A measurement or observation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Measurement"]
    class_class_curie: ClassVar[str] = "exposome_schema:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Measurement

    id: Union[str, MeasurementId] = None

@dataclass(repr=False)
class Association(NamedThing):
    """
    A relationship between two entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Association"]
    class_class_curie: ClassVar[str] = "exposome_schema:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Association

    id: Union[str, AssociationId] = None

@dataclass(repr=False)
class Exposure(NamedThing):
    """
    External, non-genetic, and internal stimuli, that can be chemical, physical, biological, and psychosocial in
    nature, that an individual interacts with
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXO["0000002"]
    class_class_curie: ClassVar[str] = "ExO:0000002"
    class_name: ClassVar[str] = "Exposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Exposure

    id: Union[str, ExposureId] = None
    exposure_route: Optional[Union[str, "ExposureRouteEnum"]] = None
    exposure_duration: Optional[str] = None
    exposure_frequency: Optional[Union[str, "ExposureFrequencyEnum"]] = None
    exposure_concentration: Optional[float] = None
    exposure_medium: Optional[Union[str, "ExposureMediumEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.exposure_route is not None and not isinstance(self.exposure_route, ExposureRouteEnum):
            self.exposure_route = ExposureRouteEnum(self.exposure_route)

        if self.exposure_duration is not None and not isinstance(self.exposure_duration, str):
            self.exposure_duration = str(self.exposure_duration)

        if self.exposure_frequency is not None and not isinstance(self.exposure_frequency, ExposureFrequencyEnum):
            self.exposure_frequency = ExposureFrequencyEnum(self.exposure_frequency)

        if self.exposure_concentration is not None and not isinstance(self.exposure_concentration, float):
            self.exposure_concentration = float(self.exposure_concentration)

        if self.exposure_medium is not None and not isinstance(self.exposure_medium, ExposureMediumEnum):
            self.exposure_medium = ExposureMediumEnum(self.exposure_medium)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActiveExposure(Exposure):
    """
    Direct, intentional contact with a stimulus
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ActiveExposure"]
    class_class_curie: ClassVar[str] = "exposome_schema:ActiveExposure"
    class_name: ClassVar[str] = "ActiveExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ActiveExposure

    id: Union[str, ActiveExposureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActiveExposureId):
            self.id = ActiveExposureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PassiveExposure(Exposure):
    """
    Indirect, unintentional, or incidental contact with a stimulus
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["PassiveExposure"]
    class_class_curie: ClassVar[str] = "exposome_schema:PassiveExposure"
    class_name: ClassVar[str] = "PassiveExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.PassiveExposure

    id: Union[str, PassiveExposureId] = None
    environmental_context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PassiveExposureId):
            self.id = PassiveExposureId(self.id)

        if self.environmental_context is not None and not isinstance(self.environmental_context, str):
            self.environmental_context = str(self.environmental_context)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalExposure(Exposure):
    """
    Exposure to a chemical substance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000231"]
    class_class_curie: ClassVar[str] = "ECTO:0000231"
    class_name: ClassVar[str] = "ChemicalExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ChemicalExposure

    id: Union[str, ChemicalExposureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DietaryExposure(Exposure):
    """
    Exposure through dietary consumption
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOODON["00002403"]
    class_class_curie: ClassVar[str] = "FOODON:00002403"
    class_name: ClassVar[str] = "DietaryExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.DietaryExposure

    id: Union[str, DietaryExposureId] = None
    food_item: Optional[str] = None
    serving_size: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DietaryExposureId):
            self.id = DietaryExposureId(self.id)

        if self.food_item is not None and not isinstance(self.food_item, str):
            self.food_item = str(self.food_item)

        if self.serving_size is not None and not isinstance(self.serving_size, str):
            self.serving_size = str(self.serving_size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OccupationalExposure(Exposure):
    """
    Exposure in an occupational setting
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0001591"]
    class_class_curie: ClassVar[str] = "ECTO:0001591"
    class_name: ClassVar[str] = "OccupationalExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.OccupationalExposure

    id: Union[str, OccupationalExposureId] = None
    occupation: Optional[str] = None
    workplace: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OccupationalExposureId):
            self.id = OccupationalExposureId(self.id)

        if self.occupation is not None and not isinstance(self.occupation, str):
            self.occupation = str(self.occupation)

        if self.workplace is not None and not isinstance(self.workplace, str):
            self.workplace = str(self.workplace)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalExposure(Exposure):
    """
    Exposure to a treatment in an empirical experimental setting
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XCO["0000000"]
    class_class_curie: ClassVar[str] = "XCO:0000000"
    class_name: ClassVar[str] = "ExperimentalExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExperimentalExposure

    id: Union[str, ExperimentalExposureId] = None
    treatment: Optional[str] = None
    experimental_subject: Optional[str] = None
    experimental_result: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentalExposureId):
            self.id = ExperimentalExposureId(self.id)

        if self.treatment is not None and not isinstance(self.treatment, str):
            self.treatment = str(self.treatment)

        if self.experimental_subject is not None and not isinstance(self.experimental_subject, str):
            self.experimental_subject = str(self.experimental_subject)

        if self.experimental_result is not None and not isinstance(self.experimental_result, str):
            self.experimental_result = str(self.experimental_result)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrenatalExposure(Exposure):
    """
    Exposure of a mammalian embryo or fetus via the mother
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["PrenatalExposure"]
    class_class_curie: ClassVar[str] = "exposome_schema:PrenatalExposure"
    class_name: ClassVar[str] = "PrenatalExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.PrenatalExposure

    id: Union[str, PrenatalExposureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrenatalExposureId):
            self.id = PrenatalExposureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BehavioralExposure(Exposure):
    """
    Exposure wherein the receiver engages in a behavior that mediates an exposure  or leads to a health outcome
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["BehavioralExposure"]
    class_class_curie: ClassVar[str] = "exposome_schema:BehavioralExposure"
    class_name: ClassVar[str] = "BehavioralExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.BehavioralExposure

    id: Union[str, BehavioralExposureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralExposureId):
            self.id = BehavioralExposureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SesExposure(Exposure):
    """
    Exposure to stimulus related to socioeconomic factors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["SesExposure"]
    class_class_curie: ClassVar[str] = "exposome_schema:SesExposure"
    class_name: ClassVar[str] = "SesExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.SesExposure

    id: Union[str, SesExposureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SesExposureId):
            self.id = SesExposureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(HealthOutcome):
    """
    An observable characteristic or trait
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UPHENO["0001001"]
    class_class_curie: ClassVar[str] = "UPHENO:0001001"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Phenotype

    id: Union[str, PhenotypeId] = None
    upheno_id: Optional[Union[str, URIorCURIE]] = None
    severity: Optional[str] = None
    onset_age: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.upheno_id is not None and not isinstance(self.upheno_id, URIorCURIE):
            self.upheno_id = URIorCURIE(self.upheno_id)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if self.onset_age is not None and not isinstance(self.onset_age, str):
            self.onset_age = str(self.onset_age)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(HealthOutcome):
    """
    A disease or medical condition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONDO["0000001"]
    class_class_curie: ClassVar[str] = "MONDO:0000001"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Disease

    id: Union[str, DiseaseId] = None
    mondo_id: Optional[Union[str, URIorCURIE]] = None
    affected_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self.mondo_id is not None and not isinstance(self.mondo_id, URIorCURIE):
            self.mondo_id = URIorCURIE(self.mondo_id)

        if self.affected_anatomy is not None and not isinstance(self.affected_anatomy, AnatomicalEntityId):
            self.affected_anatomy = AnatomicalEntityId(self.affected_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcome(HealthOutcome):
    """
    An adverse health outcome in the context of an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AdverseOutcome"]
    class_class_curie: ClassVar[str] = "exposome_schema:AdverseOutcome"
    class_name: ClassVar[str] = "AdverseOutcome"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AdverseOutcome

    id: Union[str, AdverseOutcomeId] = None
    outcome_level: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomeId):
            self.id = AdverseOutcomeId(self.id)

        if self.outcome_level is not None and not isinstance(self.outcome_level, BiologicalOrganizationLevelEnum):
            self.outcome_level = BiologicalOrganizationLevelEnum(self.outcome_level)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MammalianPhenotype(Phenotype):
    """
    A phenotype observed in mammalian model organisms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MP["0000001"]
    class_class_curie: ClassVar[str] = "MP:0000001"
    class_name: ClassVar[str] = "MammalianPhenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.MammalianPhenotype

    id: Union[str, MammalianPhenotypeId] = None
    mp_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MammalianPhenotypeId):
            self.id = MammalianPhenotypeId(self.id)

        if self.mp_id is not None and not isinstance(self.mp_id, URIorCURIE):
            self.mp_id = URIorCURIE(self.mp_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ZebrafishPhenotype(Phenotype):
    """
    A phenotype observed in zebrafish
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ZP["0000000"]
    class_class_curie: ClassVar[str] = "ZP:0000000"
    class_name: ClassVar[str] = "ZebrafishPhenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ZebrafishPhenotype

    id: Union[str, ZebrafishPhenotypeId] = None
    zp_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ZebrafishPhenotypeId):
            self.id = ZebrafishPhenotypeId(self.id)

        if self.zp_id is not None and not isinstance(self.zp_id, URIorCURIE):
            self.zp_id = URIorCURIE(self.zp_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanPhenotype(Phenotype):
    """
    A phenotype observed in humans
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = HP["0000001"]
    class_class_curie: ClassVar[str] = "HP:0000001"
    class_name: ClassVar[str] = "HumanPhenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.HumanPhenotype

    id: Union[str, HumanPhenotypeId] = None
    hp_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanPhenotypeId):
            self.id = HumanPhenotypeId(self.id)

        if self.hp_id is not None and not isinstance(self.hp_id, URIorCURIE):
            self.hp_id = URIorCURIE(self.hp_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdverseOutcomePathway(NamedThing):
    """
    A sequence of causally linked events at different levels of biological organization that lead from exposure to
    adverse health outcomes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AdverseOutcomePathway"]
    class_class_curie: ClassVar[str] = "exposome_schema:AdverseOutcomePathway"
    class_name: ClassVar[str] = "AdverseOutcomePathway"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AdverseOutcomePathway

    id: Union[str, AdverseOutcomePathwayId] = None
    aopwiki_id: Optional[str] = None
    molecular_initiating_event: Optional[Union[str, MolecularInitiatingEventId]] = None
    key_events: Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]] = empty_list()
    key_event_relationships: Optional[Union[Union[str, KeyEventRelationshipId], list[Union[str, KeyEventRelationshipId]]]] = empty_list()
    adverse_outcome: Optional[Union[str, AdverseOutcomeId]] = None
    stressors: Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseOutcomePathwayId):
            self.id = AdverseOutcomePathwayId(self.id)

        if self.aopwiki_id is not None and not isinstance(self.aopwiki_id, str):
            self.aopwiki_id = str(self.aopwiki_id)

        if self.molecular_initiating_event is not None and not isinstance(self.molecular_initiating_event, MolecularInitiatingEventId):
            self.molecular_initiating_event = MolecularInitiatingEventId(self.molecular_initiating_event)

        if not isinstance(self.key_events, list):
            self.key_events = [self.key_events] if self.key_events is not None else []
        self.key_events = [v if isinstance(v, KeyEventId) else KeyEventId(v) for v in self.key_events]

        if not isinstance(self.key_event_relationships, list):
            self.key_event_relationships = [self.key_event_relationships] if self.key_event_relationships is not None else []
        self.key_event_relationships = [v if isinstance(v, KeyEventRelationshipId) else KeyEventRelationshipId(v) for v in self.key_event_relationships]

        if self.adverse_outcome is not None and not isinstance(self.adverse_outcome, AdverseOutcomeId):
            self.adverse_outcome = AdverseOutcomeId(self.adverse_outcome)

        if not isinstance(self.stressors, list):
            self.stressors = [self.stressors] if self.stressors is not None else []
        self.stressors = [v if isinstance(v, ChemicalEntityId) else ChemicalEntityId(v) for v in self.stressors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularInitiatingEvent(BiologicalResponse):
    """
    The initial molecular-level perturbation that starts an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["MolecularInitiatingEvent"]
    class_class_curie: ClassVar[str] = "exposome_schema:MolecularInitiatingEvent"
    class_name: ClassVar[str] = "MolecularInitiatingEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.MolecularInitiatingEvent

    id: Union[str, MolecularInitiatingEventId] = None
    biological_process: Optional[str] = None
    biological_object: Optional[str] = None
    biological_action: Optional[str] = None
    occurs_in_cell_type: Optional[Union[str, CellId]] = None
    occurs_in_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularInitiatingEventId):
            self.id = MolecularInitiatingEventId(self.id)

        if self.biological_process is not None and not isinstance(self.biological_process, str):
            self.biological_process = str(self.biological_process)

        if self.biological_object is not None and not isinstance(self.biological_object, str):
            self.biological_object = str(self.biological_object)

        if self.biological_action is not None and not isinstance(self.biological_action, str):
            self.biological_action = str(self.biological_action)

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, CellId):
            self.occurs_in_cell_type = CellId(self.occurs_in_cell_type)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, AnatomicalEntityId):
            self.occurs_in_anatomy = AnatomicalEntityId(self.occurs_in_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEvent(BiologicalResponse):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["KeyEvent"]
    class_class_curie: ClassVar[str] = "exposome_schema:KeyEvent"
    class_name: ClassVar[str] = "KeyEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.KeyEvent

    id: Union[str, KeyEventId] = None
    biological_process: Optional[str] = None
    biological_object: Optional[str] = None
    biological_action: Optional[str] = None
    level_of_biological_organization: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None
    occurs_in_cell_type: Optional[Union[str, CellId]] = None
    occurs_in_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventId):
            self.id = KeyEventId(self.id)

        if self.biological_process is not None and not isinstance(self.biological_process, str):
            self.biological_process = str(self.biological_process)

        if self.biological_object is not None and not isinstance(self.biological_object, str):
            self.biological_object = str(self.biological_object)

        if self.biological_action is not None and not isinstance(self.biological_action, str):
            self.biological_action = str(self.biological_action)

        if self.level_of_biological_organization is not None and not isinstance(self.level_of_biological_organization, BiologicalOrganizationLevelEnum):
            self.level_of_biological_organization = BiologicalOrganizationLevelEnum(self.level_of_biological_organization)

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, CellId):
            self.occurs_in_cell_type = CellId(self.occurs_in_cell_type)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, AnatomicalEntityId):
            self.occurs_in_anatomy = AnatomicalEntityId(self.occurs_in_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEventRelationship(Association):
    """
    A directional relationship between two key events in an AOP
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["KeyEventRelationship"]
    class_class_curie: ClassVar[str] = "exposome_schema:KeyEventRelationship"
    class_name: ClassVar[str] = "KeyEventRelationship"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.KeyEventRelationship

    id: Union[str, KeyEventRelationshipId] = None
    upstream_event: Optional[Union[str, KeyEventId]] = None
    downstream_event: Optional[Union[str, KeyEventId]] = None
    relationship_type: Optional[str] = None
    evidence_support: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeyEventRelationshipId):
            self.id = KeyEventRelationshipId(self.id)

        if self.upstream_event is not None and not isinstance(self.upstream_event, KeyEventId):
            self.upstream_event = KeyEventId(self.upstream_event)

        if self.downstream_event is not None and not isinstance(self.downstream_event, KeyEventId):
            self.downstream_event = KeyEventId(self.downstream_event)

        if self.relationship_type is not None and not isinstance(self.relationship_type, str):
            self.relationship_type = str(self.relationship_type)

        if self.evidence_support is not None and not isinstance(self.evidence_support, str):
            self.evidence_support = str(self.evidence_support)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(StudyEntity):
    """
    A research study or survey
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EFO["0001444"]
    class_class_curie: ClassVar[str] = "EFO:0001444"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Study

    id: Union[str, StudyId] = None
    study_type: Optional[Union[str, "StudyTypeEnum"]] = None
    population: Optional[str] = None
    enrollment_period: Optional[str] = None
    geographic_location: Optional[str] = None
    data_source: Optional[Union[str, "DataSourceEnum"]] = None
    principal_investigator: Optional[str] = None
    publications: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.study_type is not None and not isinstance(self.study_type, StudyTypeEnum):
            self.study_type = StudyTypeEnum(self.study_type)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if self.enrollment_period is not None and not isinstance(self.enrollment_period, str):
            self.enrollment_period = str(self.enrollment_period)

        if self.geographic_location is not None and not isinstance(self.geographic_location, str):
            self.geographic_location = str(self.geographic_location)

        if self.data_source is not None and not isinstance(self.data_source, DataSourceEnum):
            self.data_source = DataSourceEnum(self.data_source)

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, str):
            self.principal_investigator = str(self.principal_investigator)

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, str) else str(v) for v in self.publications]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cohort(StudyEntity):
    """
    A group of individuals in a study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Cohort"]
    class_class_curie: ClassVar[str] = "exposome_schema:Cohort"
    class_name: ClassVar[str] = "Cohort"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Cohort

    id: Union[str, CohortId] = None
    part_of_study: Optional[Union[str, StudyId]] = None
    cohort_size: Optional[int] = None
    inclusion_criteria: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        if self.part_of_study is not None and not isinstance(self.part_of_study, StudyId):
            self.part_of_study = StudyId(self.part_of_study)

        if self.cohort_size is not None and not isinstance(self.cohort_size, int):
            self.cohort_size = int(self.cohort_size)

        if self.inclusion_criteria is not None and not isinstance(self.inclusion_criteria, str):
            self.inclusion_criteria = str(self.inclusion_criteria)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Participant(StudyEntity):
    """
    An individual participant in a study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Participant"]
    class_class_curie: ClassVar[str] = "exposome_schema:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Participant

    id: Union[str, ParticipantId] = None
    part_of_cohort: Optional[Union[str, CohortId]] = None
    participant_id: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    species: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipantId):
            self.id = ParticipantId(self.id)

        if self.part_of_cohort is not None and not isinstance(self.part_of_cohort, CohortId):
            self.part_of_cohort = CohortId(self.part_of_cohort)

        if self.participant_id is not None and not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureMeasurement(Measurement):
    """
    A measurement of exposure to a chemical or environmental factor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposureMeasurement"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposureMeasurement"
    class_name: ClassVar[str] = "ExposureMeasurement"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposureMeasurement

    id: Union[str, ExposureMeasurementId] = None
    measured_entity: Optional[Union[str, NamedThingId]] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_value: Optional[float] = None
    measurement_unit: Optional[str] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    sample_type: Optional[Union[str, "SampleTypeEnum"]] = None
    source_database_record: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureMeasurementId):
            self.id = ExposureMeasurementId(self.id)

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedThingId):
            self.measured_entity = NamedThingId(self.measured_entity)

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_value is not None and not isinstance(self.measurement_value, float):
            self.measurement_value = float(self.measurement_value)

        if self.measurement_unit is not None and not isinstance(self.measurement_unit, str):
            self.measurement_unit = str(self.measurement_unit)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.sample_type is not None and not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.source_database_record is not None and not isinstance(self.source_database_record, str):
            self.source_database_record = str(self.source_database_record)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiomarkerMeasurement(Measurement):
    """
    A measurement of a biological marker
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["BiomarkerMeasurement"]
    class_class_curie: ClassVar[str] = "exposome_schema:BiomarkerMeasurement"
    class_name: ClassVar[str] = "BiomarkerMeasurement"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.BiomarkerMeasurement

    id: Union[str, BiomarkerMeasurementId] = None
    biomarker_type: Optional[str] = None
    measured_entity: Optional[Union[str, NamedThingId]] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_value: Optional[float] = None
    measurement_unit: Optional[str] = None
    measurement_method: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiomarkerMeasurementId):
            self.id = BiomarkerMeasurementId(self.id)

        if self.biomarker_type is not None and not isinstance(self.biomarker_type, str):
            self.biomarker_type = str(self.biomarker_type)

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedThingId):
            self.measured_entity = NamedThingId(self.measured_entity)

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_value is not None and not isinstance(self.measurement_value, float):
            self.measurement_value = float(self.measurement_value)

        if self.measurement_unit is not None and not isinstance(self.measurement_unit, str):
            self.measurement_unit = str(self.measurement_unit)

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeMeasurement(Measurement):
    """
    A measurement of a phenotypic trait
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["PhenotypeMeasurement"]
    class_class_curie: ClassVar[str] = "exposome_schema:PhenotypeMeasurement"
    class_name: ClassVar[str] = "PhenotypeMeasurement"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.PhenotypeMeasurement

    id: Union[str, PhenotypeMeasurementId] = None
    phenotype: Optional[Union[str, PhenotypeId]] = None
    participant: Optional[Union[str, ParticipantId]] = None
    measurement_value: Optional[float] = None
    measurement_unit: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeMeasurementId):
            self.id = PhenotypeMeasurementId(self.id)

        if self.phenotype is not None and not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        if self.participant is not None and not isinstance(self.participant, ParticipantId):
            self.participant = ParticipantId(self.participant)

        if self.measurement_value is not None and not isinstance(self.measurement_value, float):
            self.measurement_value = float(self.measurement_value)

        if self.measurement_unit is not None and not isinstance(self.measurement_unit, str):
            self.measurement_unit = str(self.measurement_unit)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AggregatedMeasurement(Measurement):
    """
    An aggregated or summary measurement across a cohort or population
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AggregatedMeasurement"]
    class_class_curie: ClassVar[str] = "exposome_schema:AggregatedMeasurement"
    class_name: ClassVar[str] = "AggregatedMeasurement"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AggregatedMeasurement

    id: Union[str, AggregatedMeasurementId] = None
    measured_entity: Optional[Union[str, NamedThingId]] = None
    cohort: Optional[Union[str, CohortId]] = None
    summary_statistic: Optional[Union[str, "SummaryStatisticEnum"]] = None
    statistic_value: Optional[float] = None
    sample_size: Optional[int] = None
    stratification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AggregatedMeasurementId):
            self.id = AggregatedMeasurementId(self.id)

        if self.measured_entity is not None and not isinstance(self.measured_entity, NamedThingId):
            self.measured_entity = NamedThingId(self.measured_entity)

        if self.cohort is not None and not isinstance(self.cohort, CohortId):
            self.cohort = CohortId(self.cohort)

        if self.summary_statistic is not None and not isinstance(self.summary_statistic, SummaryStatisticEnum):
            self.summary_statistic = SummaryStatisticEnum(self.summary_statistic)

        if self.statistic_value is not None and not isinstance(self.statistic_value, float):
            self.statistic_value = float(self.statistic_value)

        if self.sample_size is not None and not isinstance(self.sample_size, int):
            self.sample_size = int(self.sample_size)

        if self.stratification is not None and not isinstance(self.stratification, str):
            self.stratification = str(self.stratification)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gene(BiologicalEntity):
    """
    A gene or genetic element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Gene"]
    class_class_curie: ClassVar[str] = "exposome_schema:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Gene

    id: Union[str, GeneId] = None
    ncbigene_id: Optional[str] = None
    symbol: Optional[str] = None
    in_taxon: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self.ncbigene_id is not None and not isinstance(self.ncbigene_id, str):
            self.ncbigene_id = str(self.ncbigene_id)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.in_taxon is not None and not isinstance(self.in_taxon, str):
            self.in_taxon = str(self.in_taxon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protein(BiologicalEntity):
    """
    A protein or polypeptide
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Protein"]
    class_class_curie: ClassVar[str] = "exposome_schema:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Protein

    id: Union[str, ProteinId] = None
    encoded_by_gene: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        if self.encoded_by_gene is not None and not isinstance(self.encoded_by_gene, GeneId):
            self.encoded_by_gene = GeneId(self.encoded_by_gene)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cell(BiologicalEntity):
    """
    A type of cell
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CL["0000000"]
    class_class_curie: ClassVar[str] = "CL:0000000"
    class_name: ClassVar[str] = "Cell"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Cell

    id: Union[str, CellId] = None
    cl_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)

        if self.cl_id is not None and not isinstance(self.cl_id, URIorCURIE):
            self.cl_id = URIorCURIE(self.cl_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical structure or system, part of an organism, made of many cells
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UBERON["0001062"]
    class_class_curie: ClassVar[str] = "UBERON:0001062"
    class_name: ClassVar[str] = "AnatomicalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    uberon_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self.uberon_id is not None and not isinstance(self.uberon_id, URIorCURIE):
            self.uberon_id = URIorCURIE(self.uberon_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organism(BiologicalEntity):
    """
    An individual organism
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Organism"]
    class_class_curie: ClassVar[str] = "exposome_schema:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Organism

    id: Union[str, OrganismId] = None
    species: Optional[str] = None
    taxon_id: Optional[str] = None
    lifestage: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismId):
            self.id = OrganismId(self.id)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.taxon_id is not None and not isinstance(self.taxon_id, str):
            self.taxon_id = str(self.taxon_id)

        if self.lifestage is not None and not isinstance(self.lifestage, str):
            self.lifestage = str(self.lifestage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Population(BiologicalEntity):
    """
    A group of organisms of the same species
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["Population"]
    class_class_curie: ClassVar[str] = "exposome_schema:Population"
    class_name: ClassVar[str] = "Population"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Population

    id: Union[str, PopulationId] = None
    species: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationId):
            self.id = PopulationId(self.id)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureToPhenotypeAssociation(YAMLRoot):
    """
    An association between an exposure and a phenotype
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposureToPhenotypeAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposureToPhenotypeAssociation"
    class_name: ClassVar[str] = "ExposureToPhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposureToPhenotypeAssociation

    exposure: Optional[Union[dict, ExposureEvent]] = None
    phenotype: Optional[Union[str, PhenotypeId]] = None
    receiver: Optional[Union[str, BiologicalEntityId]] = None
    association_type: Optional[str] = None
    evidence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.exposure is not None and not isinstance(self.exposure, ExposureEvent):
            self.exposure = ExposureEvent(**as_dict(self.exposure))

        if self.phenotype is not None and not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        if self.receiver is not None and not isinstance(self.receiver, BiologicalEntityId):
            self.receiver = BiologicalEntityId(self.receiver)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        if self.evidence is not None and not isinstance(self.evidence, str):
            self.evidence = str(self.evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureToDiseaseAssociation(YAMLRoot):
    """
    An association between an exposure and a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposureToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposureToDiseaseAssociation"
    class_name: ClassVar[str] = "ExposureToDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposureToDiseaseAssociation

    exposure: Optional[Union[dict, ExposureEvent]] = None
    disease: Optional[Union[str, DiseaseId]] = None
    receiver: Optional[Union[str, BiologicalEntityId]] = None
    evidence: Optional[str] = None
    association_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.exposure is not None and not isinstance(self.exposure, ExposureEvent):
            self.exposure = ExposureEvent(**as_dict(self.exposure))

        if self.disease is not None and not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        if self.receiver is not None and not isinstance(self.receiver, BiologicalEntityId):
            self.receiver = BiologicalEntityId(self.receiver)

        if self.evidence is not None and not isinstance(self.evidence, str):
            self.evidence = str(self.evidence)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalToGeneAssociation(YAMLRoot):
    """
    An association between a chemical and a gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ChemicalToGeneAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:ChemicalToGeneAssociation"
    class_name: ClassVar[str] = "ChemicalToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ChemicalToGeneAssociation

    chemical: Optional[Union[str, ChemicalEntityId]] = None
    gene: Optional[Union[str, GeneId]] = None
    receiver: Optional[Union[str, BiologicalEntityId]] = None
    interaction_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.chemical is not None and not isinstance(self.chemical, ChemicalEntityId):
            self.chemical = ChemicalEntityId(self.chemical)

        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.receiver is not None and not isinstance(self.receiver, BiologicalEntityId):
            self.receiver = BiologicalEntityId(self.receiver)

        if self.interaction_type is not None and not isinstance(self.interaction_type, str):
            self.interaction_type = str(self.interaction_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneToDiseaseAssociation(Association):
    """
    An association between a gene and a disease
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["GeneToDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:GeneToDiseaseAssociation"
    class_name: ClassVar[str] = "GeneToDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GeneToDiseaseAssociation

    id: Union[str, GeneToDiseaseAssociationId] = None
    gene: Optional[Union[str, GeneId]] = None
    disease: Optional[Union[str, DiseaseId]] = None
    association_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)

        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.disease is not None and not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneticVariantToPhenotypeAssociation(Association):
    """
    An association between a genetic variant and a phenotype (e.g., from GWAS)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["GeneticVariantToPhenotypeAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:GeneticVariantToPhenotypeAssociation"
    class_name: ClassVar[str] = "GeneticVariantToPhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GeneticVariantToPhenotypeAssociation

    id: Union[str, GeneticVariantToPhenotypeAssociationId] = None
    genetic_variant: Optional[str] = None
    phenotype: Optional[Union[str, PhenotypeId]] = None
    p_value: Optional[float] = None
    effect_size: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneticVariantToPhenotypeAssociationId):
            self.id = GeneticVariantToPhenotypeAssociationId(self.id)

        if self.genetic_variant is not None and not isinstance(self.genetic_variant, str):
            self.genetic_variant = str(self.genetic_variant)

        if self.phenotype is not None and not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.effect_size is not None and not isinstance(self.effect_size, float):
            self.effect_size = float(self.effect_size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposomeDatabase(YAMLRoot):
    """
    Container for all exposome data including exposures, chemicals, health outcomes, AOPs, studies, and measurements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposomeDatabase"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposomeDatabase"
    class_name: ClassVar[str] = "ExposomeDatabase"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposomeDatabase

    chemical_entities: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    exposures: Optional[Union[Union[dict, ExposureEvent], list[Union[dict, ExposureEvent]]]] = empty_list()
    health_outcomes: Optional[Union[dict[Union[str, HealthOutcomeId], Union[dict, HealthOutcome]], list[Union[dict, HealthOutcome]]]] = empty_dict()
    adverse_outcome_pathways: Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, AdverseOutcomePathway]], list[Union[dict, AdverseOutcomePathway]]]] = empty_dict()
    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]] = empty_dict()
    cohorts: Optional[Union[dict[Union[str, CohortId], Union[dict, Cohort]], list[Union[dict, Cohort]]]] = empty_dict()
    participants: Optional[Union[dict[Union[str, ParticipantId], Union[dict, Participant]], list[Union[dict, Participant]]]] = empty_dict()
    measurements: Optional[Union[dict[Union[str, MeasurementId], Union[dict, Measurement]], list[Union[dict, Measurement]]]] = empty_dict()
    biological_entities: Optional[Union[dict[Union[str, BiologicalEntityId], Union[dict, BiologicalEntity]], list[Union[dict, BiologicalEntity]]]] = empty_dict()
    database_records: Optional[Union[str, list[str]]] = empty_list()
    associations: Optional[Union[dict[Union[str, AssociationId], Union[dict, Association]], list[Union[dict, Association]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="chemical_entities", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.exposures, list):
            self.exposures = [self.exposures] if self.exposures is not None else []
        self.exposures = [v if isinstance(v, ExposureEvent) else ExposureEvent(**as_dict(v)) for v in self.exposures]

        self._normalize_inlined_as_list(slot_name="health_outcomes", slot_type=HealthOutcome, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adverse_outcome_pathways", slot_type=AdverseOutcomePathway, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cohorts", slot_type=Cohort, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="participants", slot_type=Participant, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="biological_entities", slot_type=BiologicalEntity, key_name="id", keyed=True)

        if not isinstance(self.database_records, list):
            self.database_records = [self.database_records] if self.database_records is not None else []
        self.database_records = [v if isinstance(v, str) else str(v) for v in self.database_records]

        self._normalize_inlined_as_list(slot_name="associations", slot_type=Association, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class ExposureFrequencyEnum(EnumDefinitionImpl):
    """
    Frequency of exposure
    """
    acute = PermissibleValue(
        text="acute",
        description="Single or short-term exposure")
    subacute = PermissibleValue(
        text="subacute",
        description="Repeated exposure over a short period")
    subchronic = PermissibleValue(
        text="subchronic",
        description="Repeated exposure over an intermediate period")
    chronic = PermissibleValue(
        text="chronic",
        description="Long-term or repeated exposure over a long period")
    intermittent = PermissibleValue(
        text="intermittent",
        description="Exposure occurring at irregular intervals")
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown frequency")

    _defn = EnumDefinition(
        name="ExposureFrequencyEnum",
        description="Frequency of exposure",
    )

class ExposureRouteEnum(EnumDefinitionImpl):
    """
    Routes of exposure to chemicals or environmental factors
    """
    oral = PermissibleValue(
        text="oral",
        description="Oral ingestion",
        meaning=ECTO["0000895"])
    dermal = PermissibleValue(
        text="dermal",
        description="Dermal contact",
        meaning=ECTO["0000896"])
    inhalation = PermissibleValue(
        text="inhalation",
        description="Inhalation",
        meaning=ECTO["0000897"])
    injection = PermissibleValue(
        text="injection",
        description="Injection")
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown route")

    _defn = EnumDefinition(
        name="ExposureRouteEnum",
        description="Routes of exposure to chemicals or environmental factors",
    )

class ExposureMediumEnum(EnumDefinitionImpl):
    """
    Medium through which exposure occurs
    """
    air = PermissibleValue(
        text="air",
        description="Air",
        meaning=ENVO["00002005"])
    water = PermissibleValue(
        text="water",
        description="Water",
        meaning=ENVO["00002006"])
    food = PermissibleValue(
        text="food",
        description="Food",
        meaning=FOODON["00002403"])
    soil = PermissibleValue(
        text="soil",
        description="Soil",
        meaning=ENVO["00001998"])
    dust = PermissibleValue(
        text="dust",
        description="Dust")
    consumer_product = PermissibleValue(
        text="consumer_product",
        description="Consumer product")
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown medium")

    _defn = EnumDefinition(
        name="ExposureMediumEnum",
        description="Medium through which exposure occurs",
    )

class BiologicalOrganizationLevelEnum(EnumDefinitionImpl):
    """
    Levels of biological organization
    """
    molecular = PermissibleValue(
        text="molecular",
        description="Molecular level",
        meaning=EFO["0001432"])
    cellular = PermissibleValue(
        text="cellular",
        description="Cellular level",
        meaning=CL["0000000"])
    tissue = PermissibleValue(
        text="tissue",
        description="Tissue level",
        meaning=UBERON["0000479"])
    organ = PermissibleValue(
        text="organ",
        description="Organ level",
        meaning=UBERON["0000062"])
    organism = PermissibleValue(
        text="organism",
        description="Organism level",
        meaning=UBERON["0000468"])
    population = PermissibleValue(
        text="population",
        description="Population level")

    _defn = EnumDefinition(
        name="BiologicalOrganizationLevelEnum",
        description="Levels of biological organization",
    )

class StudyTypeEnum(EnumDefinitionImpl):
    """
    Types of research studies
    """
    cohort = PermissibleValue(
        text="cohort",
        description="Cohort study",
        meaning=EFO["0001444"])
    cross_sectional = PermissibleValue(
        text="cross_sectional",
        description="Cross-sectional study",
        meaning=EFO["0001745"])
    case_control = PermissibleValue(
        text="case_control",
        description="Case-control study",
        meaning=EFO["0001427"])
    randomized_controlled_trial = PermissibleValue(
        text="randomized_controlled_trial",
        description="Randomized controlled trial",
        meaning=EFO["0001427"])
    survey = PermissibleValue(
        text="survey",
        description="Survey")
    gwas = PermissibleValue(
        text="gwas",
        description="Genome-wide association study",
        meaning=EFO["0000508"])
    other = PermissibleValue(
        text="other",
        description="Other study type")

    _defn = EnumDefinition(
        name="StudyTypeEnum",
        description="Types of research studies",
    )

class DataSourceEnum(EnumDefinitionImpl):
    """
    Data sources and repositories
    """
    nhanes = PermissibleValue(
        text="nhanes",
        description="National Health and Nutrition Examination Survey")
    chear = PermissibleValue(
        text="chear",
        description="Children's Health Exposure Analysis Resource")
    hhear = PermissibleValue(
        text="hhear",
        description="Human Health Exposure Analysis Resource")
    aop_wiki = PermissibleValue(
        text="aop_wiki",
        description="AOP Wiki")
    ctd = PermissibleValue(
        text="ctd",
        description="Comparative Toxicogenomics Database")
    tox_cast = PermissibleValue(
        text="tox_cast",
        description="ToxCast")
    tox21 = PermissibleValue(
        text="tox21",
        description="Tox21")
    chem_bl = PermissibleValue(
        text="chem_bl",
        description="ChEMBL")
    comp_tox = PermissibleValue(
        text="comp_tox",
        description="CompTox Dashboard")
    gwas_catalog = PermissibleValue(
        text="gwas_catalog",
        description="GWAS Catalog")
    gene_expression_atlas = PermissibleValue(
        text="gene_expression_atlas",
        description="Gene Expression Atlas")
    usda_pesticide = PermissibleValue(
        text="usda_pesticide",
        description="USDA Pesticide Data Program")
    wweia = PermissibleValue(
        text="wweia",
        description="What We Eat In America")
    other = PermissibleValue(
        text="other",
        description="Other data source")

    _defn = EnumDefinition(
        name="DataSourceEnum",
        description="Data sources and repositories",
    )

class SexEnum(EnumDefinitionImpl):
    """
    Biological sex
    """
    male = PermissibleValue(
        text="male",
        description="Male",
        meaning=PATO["0000384"])
    female = PermissibleValue(
        text="female",
        description="Female",
        meaning=PATO["0000383"])
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown")

    _defn = EnumDefinition(
        name="SexEnum",
        description="Biological sex",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples
    """
    blood = PermissibleValue(
        text="blood",
        description="Blood sample")
    urine = PermissibleValue(
        text="urine",
        description="Urine sample")
    serum = PermissibleValue(
        text="serum",
        description="Serum sample")
    plasma = PermissibleValue(
        text="plasma",
        description="Plasma sample")
    tissue = PermissibleValue(
        text="tissue",
        description="Tissue sample")
    saliva = PermissibleValue(
        text="saliva",
        description="Saliva sample")
    hair = PermissibleValue(
        text="hair",
        description="Hair sample")
    nail = PermissibleValue(
        text="nail",
        description="Nail sample")
    other = PermissibleValue(
        text="other",
        description="Other sample type")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples",
    )

class SummaryStatisticEnum(EnumDefinitionImpl):
    """
    Types of summary statistics
    """
    mean = PermissibleValue(
        text="mean",
        description="Arithmetic mean")
    median = PermissibleValue(
        text="median",
        description="Median")
    mode = PermissibleValue(
        text="mode",
        description="Mode")
    percentile = PermissibleValue(
        text="percentile",
        description="Percentile")
    standard_deviation = PermissibleValue(
        text="standard_deviation",
        description="Standard deviation")
    variance = PermissibleValue(
        text="variance",
        description="Variance")
    range = PermissibleValue(
        text="range",
        description="Range")
    interquartile_range = PermissibleValue(
        text="interquartile_range",
        description="Interquartile range")

    _defn = EnumDefinition(
        name="SummaryStatisticEnum",
        description="Types of summary statistics",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=EXPOSOME_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=EXPOSOME_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=EXPOSOME_SCHEMA.description, domain=None, range=Optional[str])

slots.category = Slot(uri=EXPOSOME_SCHEMA.category, name="category", curie=EXPOSOME_SCHEMA.curie('category'),
                   model_uri=EXPOSOME_SCHEMA.category, domain=None, range=Optional[Union[str, list[str]]])

slots.xref = Slot(uri=EXPOSOME_SCHEMA.xref, name="xref", curie=EXPOSOME_SCHEMA.curie('xref'),
                   model_uri=EXPOSOME_SCHEMA.xref, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.chebi_id = Slot(uri=EXPOSOME_SCHEMA.chebi_id, name="chebi_id", curie=EXPOSOME_SCHEMA.curie('chebi_id'),
                   model_uri=EXPOSOME_SCHEMA.chebi_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^CHEBI:\d+$'))

slots.dtxsid = Slot(uri=EXPOSOME_SCHEMA.dtxsid, name="dtxsid", curie=EXPOSOME_SCHEMA.curie('dtxsid'),
                   model_uri=EXPOSOME_SCHEMA.dtxsid, domain=None, range=Optional[str],
                   pattern=re.compile(r'^DTXSID\d{7,9}$'))

slots.chembl_id = Slot(uri=EXPOSOME_SCHEMA.chembl_id, name="chembl_id", curie=EXPOSOME_SCHEMA.curie('chembl_id'),
                   model_uri=EXPOSOME_SCHEMA.chembl_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CHEMBL\d+$'))

slots.pubchem_cid = Slot(uri=EXPOSOME_SCHEMA.pubchem_cid, name="pubchem_cid", curie=EXPOSOME_SCHEMA.curie('pubchem_cid'),
                   model_uri=EXPOSOME_SCHEMA.pubchem_cid, domain=None, range=Optional[int])

slots.cas_number = Slot(uri=EXPOSOME_SCHEMA.cas_number, name="cas_number", curie=EXPOSOME_SCHEMA.curie('cas_number'),
                   model_uri=EXPOSOME_SCHEMA.cas_number, domain=None, range=Optional[str])

slots.inchi = Slot(uri=EXPOSOME_SCHEMA.inchi, name="inchi", curie=EXPOSOME_SCHEMA.curie('inchi'),
                   model_uri=EXPOSOME_SCHEMA.inchi, domain=None, range=Optional[str])

slots.smiles = Slot(uri=EXPOSOME_SCHEMA.smiles, name="smiles", curie=EXPOSOME_SCHEMA.curie('smiles'),
                   model_uri=EXPOSOME_SCHEMA.smiles, domain=None, range=Optional[str])

slots.molecular_formula = Slot(uri=EXPOSOME_SCHEMA.molecular_formula, name="molecular_formula", curie=EXPOSOME_SCHEMA.curie('molecular_formula'),
                   model_uri=EXPOSOME_SCHEMA.molecular_formula, domain=None, range=Optional[str])

slots.exposure_stimulus = Slot(uri=EXPOSOME_SCHEMA.exposure_stimulus, name="exposure_stimulus", curie=EXPOSOME_SCHEMA.curie('exposure_stimulus'),
                   model_uri=EXPOSOME_SCHEMA.exposure_stimulus, domain=None, range=Union[str, StimulusEntityId])

slots.exposure_route = Slot(uri=EXPOSOME_SCHEMA.exposure_route, name="exposure_route", curie=EXPOSOME_SCHEMA.curie('exposure_route'),
                   model_uri=EXPOSOME_SCHEMA.exposure_route, domain=None, range=Optional[Union[str, "ExposureRouteEnum"]])

slots.exposure_duration = Slot(uri=EXPOSOME_SCHEMA.exposure_duration, name="exposure_duration", curie=EXPOSOME_SCHEMA.curie('exposure_duration'),
                   model_uri=EXPOSOME_SCHEMA.exposure_duration, domain=None, range=Optional[str])

slots.exposure_concentration = Slot(uri=EXPOSOME_SCHEMA.exposure_concentration, name="exposure_concentration", curie=EXPOSOME_SCHEMA.curie('exposure_concentration'),
                   model_uri=EXPOSOME_SCHEMA.exposure_concentration, domain=None, range=Optional[float])

slots.exposure_medium = Slot(uri=EXPOSOME_SCHEMA.exposure_medium, name="exposure_medium", curie=EXPOSOME_SCHEMA.curie('exposure_medium'),
                   model_uri=EXPOSOME_SCHEMA.exposure_medium, domain=None, range=Optional[Union[str, "ExposureMediumEnum"]])

slots.exposure_frequency = Slot(uri=EXPOSOME_SCHEMA.exposure_frequency, name="exposure_frequency", curie=EXPOSOME_SCHEMA.curie('exposure_frequency'),
                   model_uri=EXPOSOME_SCHEMA.exposure_frequency, domain=None, range=Optional[Union[str, "ExposureFrequencyEnum"]])

slots.exposure_outcome = Slot(uri=EXPOSOME_SCHEMA.exposure_outcome, name="exposure_outcome", curie=EXPOSOME_SCHEMA.curie('exposure_outcome'),
                   model_uri=EXPOSOME_SCHEMA.exposure_outcome, domain=None, range=Union[str, BiologicalResponseId])

slots.exposure_receiver = Slot(uri=EXPOSOME_SCHEMA.exposure_receiver, name="exposure_receiver", curie=EXPOSOME_SCHEMA.curie('exposure_receiver'),
                   model_uri=EXPOSOME_SCHEMA.exposure_receiver, domain=None, range=Union[str, BiologicalEntityId])

slots.food_item = Slot(uri=EXPOSOME_SCHEMA.food_item, name="food_item", curie=EXPOSOME_SCHEMA.curie('food_item'),
                   model_uri=EXPOSOME_SCHEMA.food_item, domain=None, range=Optional[str])

slots.serving_size = Slot(uri=EXPOSOME_SCHEMA.serving_size, name="serving_size", curie=EXPOSOME_SCHEMA.curie('serving_size'),
                   model_uri=EXPOSOME_SCHEMA.serving_size, domain=None, range=Optional[str])

slots.environmental_context = Slot(uri=EXPOSOME_SCHEMA.environmental_context, name="environmental_context", curie=EXPOSOME_SCHEMA.curie('environmental_context'),
                   model_uri=EXPOSOME_SCHEMA.environmental_context, domain=None, range=Optional[str])

slots.occupation = Slot(uri=EXPOSOME_SCHEMA.occupation, name="occupation", curie=EXPOSOME_SCHEMA.curie('occupation'),
                   model_uri=EXPOSOME_SCHEMA.occupation, domain=None, range=Optional[str])

slots.workplace = Slot(uri=EXPOSOME_SCHEMA.workplace, name="workplace", curie=EXPOSOME_SCHEMA.curie('workplace'),
                   model_uri=EXPOSOME_SCHEMA.workplace, domain=None, range=Optional[str])

slots.treatment = Slot(uri=EXPOSOME_SCHEMA.treatment, name="treatment", curie=EXPOSOME_SCHEMA.curie('treatment'),
                   model_uri=EXPOSOME_SCHEMA.treatment, domain=None, range=Optional[str])

slots.experimental_subject = Slot(uri=EXPOSOME_SCHEMA.experimental_subject, name="experimental_subject", curie=EXPOSOME_SCHEMA.curie('experimental_subject'),
                   model_uri=EXPOSOME_SCHEMA.experimental_subject, domain=None, range=Optional[str])

slots.experimental_result = Slot(uri=EXPOSOME_SCHEMA.experimental_result, name="experimental_result", curie=EXPOSOME_SCHEMA.curie('experimental_result'),
                   model_uri=EXPOSOME_SCHEMA.experimental_result, domain=None, range=Optional[str])

slots.hp_id = Slot(uri=EXPOSOME_SCHEMA.hp_id, name="hp_id", curie=EXPOSOME_SCHEMA.curie('hp_id'),
                   model_uri=EXPOSOME_SCHEMA.hp_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^HP:\d{7}$'))

slots.upheno_id = Slot(uri=EXPOSOME_SCHEMA.upheno_id, name="upheno_id", curie=EXPOSOME_SCHEMA.curie('upheno_id'),
                   model_uri=EXPOSOME_SCHEMA.upheno_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^UPHENO:\d+$'))

slots.severity = Slot(uri=EXPOSOME_SCHEMA.severity, name="severity", curie=EXPOSOME_SCHEMA.curie('severity'),
                   model_uri=EXPOSOME_SCHEMA.severity, domain=None, range=Optional[str])

slots.onset_age = Slot(uri=EXPOSOME_SCHEMA.onset_age, name="onset_age", curie=EXPOSOME_SCHEMA.curie('onset_age'),
                   model_uri=EXPOSOME_SCHEMA.onset_age, domain=None, range=Optional[str])

slots.mondo_id = Slot(uri=EXPOSOME_SCHEMA.mondo_id, name="mondo_id", curie=EXPOSOME_SCHEMA.curie('mondo_id'),
                   model_uri=EXPOSOME_SCHEMA.mondo_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^MONDO:\d{7}$'))

slots.affected_anatomy = Slot(uri=EXPOSOME_SCHEMA.affected_anatomy, name="affected_anatomy", curie=EXPOSOME_SCHEMA.curie('affected_anatomy'),
                   model_uri=EXPOSOME_SCHEMA.affected_anatomy, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.outcome_level = Slot(uri=EXPOSOME_SCHEMA.outcome_level, name="outcome_level", curie=EXPOSOME_SCHEMA.curie('outcome_level'),
                   model_uri=EXPOSOME_SCHEMA.outcome_level, domain=None, range=Optional[Union[str, "BiologicalOrganizationLevelEnum"]])

slots.mp_id = Slot(uri=EXPOSOME_SCHEMA.mp_id, name="mp_id", curie=EXPOSOME_SCHEMA.curie('mp_id'),
                   model_uri=EXPOSOME_SCHEMA.mp_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^MP:\d{7}$'))

slots.zp_id = Slot(uri=EXPOSOME_SCHEMA.zp_id, name="zp_id", curie=EXPOSOME_SCHEMA.curie('zp_id'),
                   model_uri=EXPOSOME_SCHEMA.zp_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^ZP:\d{7}$'))

slots.aopwiki_id = Slot(uri=EXPOSOME_SCHEMA.aopwiki_id, name="aopwiki_id", curie=EXPOSOME_SCHEMA.curie('aopwiki_id'),
                   model_uri=EXPOSOME_SCHEMA.aopwiki_id, domain=None, range=Optional[str])

slots.molecular_initiating_event = Slot(uri=EXPOSOME_SCHEMA.molecular_initiating_event, name="molecular_initiating_event", curie=EXPOSOME_SCHEMA.curie('molecular_initiating_event'),
                   model_uri=EXPOSOME_SCHEMA.molecular_initiating_event, domain=None, range=Optional[Union[str, MolecularInitiatingEventId]])

slots.key_events = Slot(uri=EXPOSOME_SCHEMA.key_events, name="key_events", curie=EXPOSOME_SCHEMA.curie('key_events'),
                   model_uri=EXPOSOME_SCHEMA.key_events, domain=None, range=Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]])

slots.key_event_relationships = Slot(uri=EXPOSOME_SCHEMA.key_event_relationships, name="key_event_relationships", curie=EXPOSOME_SCHEMA.curie('key_event_relationships'),
                   model_uri=EXPOSOME_SCHEMA.key_event_relationships, domain=None, range=Optional[Union[Union[str, KeyEventRelationshipId], list[Union[str, KeyEventRelationshipId]]]])

slots.adverse_outcome = Slot(uri=EXPOSOME_SCHEMA.adverse_outcome, name="adverse_outcome", curie=EXPOSOME_SCHEMA.curie('adverse_outcome'),
                   model_uri=EXPOSOME_SCHEMA.adverse_outcome, domain=None, range=Optional[Union[str, AdverseOutcomeId]])

slots.stressors = Slot(uri=EXPOSOME_SCHEMA.stressors, name="stressors", curie=EXPOSOME_SCHEMA.curie('stressors'),
                   model_uri=EXPOSOME_SCHEMA.stressors, domain=None, range=Optional[Union[Union[str, ChemicalEntityId], list[Union[str, ChemicalEntityId]]]])

slots.biological_process = Slot(uri=EXPOSOME_SCHEMA.biological_process, name="biological_process", curie=EXPOSOME_SCHEMA.curie('biological_process'),
                   model_uri=EXPOSOME_SCHEMA.biological_process, domain=None, range=Optional[str])

slots.biological_object = Slot(uri=EXPOSOME_SCHEMA.biological_object, name="biological_object", curie=EXPOSOME_SCHEMA.curie('biological_object'),
                   model_uri=EXPOSOME_SCHEMA.biological_object, domain=None, range=Optional[str])

slots.biological_action = Slot(uri=EXPOSOME_SCHEMA.biological_action, name="biological_action", curie=EXPOSOME_SCHEMA.curie('biological_action'),
                   model_uri=EXPOSOME_SCHEMA.biological_action, domain=None, range=Optional[str])

slots.occurs_in_cell_type = Slot(uri=CL['0000000'], name="occurs_in_cell_type", curie=CL.curie('0000000'),
                   model_uri=EXPOSOME_SCHEMA.occurs_in_cell_type, domain=None, range=Optional[Union[str, CellId]])

slots.occurs_in_anatomy = Slot(uri=EXPOSOME_SCHEMA.occurs_in_anatomy, name="occurs_in_anatomy", curie=EXPOSOME_SCHEMA.curie('occurs_in_anatomy'),
                   model_uri=EXPOSOME_SCHEMA.occurs_in_anatomy, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.level_of_biological_organization = Slot(uri=EXPOSOME_SCHEMA.level_of_biological_organization, name="level_of_biological_organization", curie=EXPOSOME_SCHEMA.curie('level_of_biological_organization'),
                   model_uri=EXPOSOME_SCHEMA.level_of_biological_organization, domain=None, range=Optional[Union[str, "BiologicalOrganizationLevelEnum"]])

slots.upstream_event = Slot(uri=EXPOSOME_SCHEMA.upstream_event, name="upstream_event", curie=EXPOSOME_SCHEMA.curie('upstream_event'),
                   model_uri=EXPOSOME_SCHEMA.upstream_event, domain=None, range=Optional[Union[str, KeyEventId]])

slots.downstream_event = Slot(uri=EXPOSOME_SCHEMA.downstream_event, name="downstream_event", curie=EXPOSOME_SCHEMA.curie('downstream_event'),
                   model_uri=EXPOSOME_SCHEMA.downstream_event, domain=None, range=Optional[Union[str, KeyEventId]])

slots.relationship_type = Slot(uri=EXPOSOME_SCHEMA.relationship_type, name="relationship_type", curie=EXPOSOME_SCHEMA.curie('relationship_type'),
                   model_uri=EXPOSOME_SCHEMA.relationship_type, domain=None, range=Optional[str])

slots.evidence_support = Slot(uri=EXPOSOME_SCHEMA.evidence_support, name="evidence_support", curie=EXPOSOME_SCHEMA.curie('evidence_support'),
                   model_uri=EXPOSOME_SCHEMA.evidence_support, domain=None, range=Optional[str])

slots.study_type = Slot(uri=EXPOSOME_SCHEMA.study_type, name="study_type", curie=EXPOSOME_SCHEMA.curie('study_type'),
                   model_uri=EXPOSOME_SCHEMA.study_type, domain=None, range=Optional[Union[str, "StudyTypeEnum"]])

slots.population = Slot(uri=EXPOSOME_SCHEMA.population, name="population", curie=EXPOSOME_SCHEMA.curie('population'),
                   model_uri=EXPOSOME_SCHEMA.population, domain=None, range=Optional[str])

slots.enrollment_period = Slot(uri=EXPOSOME_SCHEMA.enrollment_period, name="enrollment_period", curie=EXPOSOME_SCHEMA.curie('enrollment_period'),
                   model_uri=EXPOSOME_SCHEMA.enrollment_period, domain=None, range=Optional[str])

slots.geographic_location = Slot(uri=EXPOSOME_SCHEMA.geographic_location, name="geographic_location", curie=EXPOSOME_SCHEMA.curie('geographic_location'),
                   model_uri=EXPOSOME_SCHEMA.geographic_location, domain=None, range=Optional[str])

slots.data_source = Slot(uri=EXPOSOME_SCHEMA.data_source, name="data_source", curie=EXPOSOME_SCHEMA.curie('data_source'),
                   model_uri=EXPOSOME_SCHEMA.data_source, domain=None, range=Optional[Union[str, "DataSourceEnum"]])

slots.principal_investigator = Slot(uri=EXPOSOME_SCHEMA.principal_investigator, name="principal_investigator", curie=EXPOSOME_SCHEMA.curie('principal_investigator'),
                   model_uri=EXPOSOME_SCHEMA.principal_investigator, domain=None, range=Optional[str])

slots.publications = Slot(uri=EXPOSOME_SCHEMA.publications, name="publications", curie=EXPOSOME_SCHEMA.curie('publications'),
                   model_uri=EXPOSOME_SCHEMA.publications, domain=None, range=Optional[Union[str, list[str]]])

slots.part_of_study = Slot(uri=EXPOSOME_SCHEMA.part_of_study, name="part_of_study", curie=EXPOSOME_SCHEMA.curie('part_of_study'),
                   model_uri=EXPOSOME_SCHEMA.part_of_study, domain=None, range=Optional[Union[str, StudyId]])

slots.cohort_size = Slot(uri=EXPOSOME_SCHEMA.cohort_size, name="cohort_size", curie=EXPOSOME_SCHEMA.curie('cohort_size'),
                   model_uri=EXPOSOME_SCHEMA.cohort_size, domain=None, range=Optional[int])

slots.inclusion_criteria = Slot(uri=EXPOSOME_SCHEMA.inclusion_criteria, name="inclusion_criteria", curie=EXPOSOME_SCHEMA.curie('inclusion_criteria'),
                   model_uri=EXPOSOME_SCHEMA.inclusion_criteria, domain=None, range=Optional[str])

slots.part_of_cohort = Slot(uri=BIOLINK.member_of, name="part_of_cohort", curie=BIOLINK.curie('member_of'),
                   model_uri=EXPOSOME_SCHEMA.part_of_cohort, domain=None, range=Optional[Union[str, CohortId]])

slots.participant_id = Slot(uri=EXPOSOME_SCHEMA.participant_id, name="participant_id", curie=EXPOSOME_SCHEMA.curie('participant_id'),
                   model_uri=EXPOSOME_SCHEMA.participant_id, domain=None, range=Optional[str])

slots.age = Slot(uri=EXPOSOME_SCHEMA.age, name="age", curie=EXPOSOME_SCHEMA.curie('age'),
                   model_uri=EXPOSOME_SCHEMA.age, domain=None, range=Optional[int])

slots.sex = Slot(uri=EXPOSOME_SCHEMA.sex, name="sex", curie=EXPOSOME_SCHEMA.curie('sex'),
                   model_uri=EXPOSOME_SCHEMA.sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.species = Slot(uri=EXPOSOME_SCHEMA.species, name="species", curie=EXPOSOME_SCHEMA.curie('species'),
                   model_uri=EXPOSOME_SCHEMA.species, domain=None, range=Optional[str])

slots.measured_entity = Slot(uri=EXPOSOME_SCHEMA.measured_entity, name="measured_entity", curie=EXPOSOME_SCHEMA.curie('measured_entity'),
                   model_uri=EXPOSOME_SCHEMA.measured_entity, domain=None, range=Optional[Union[str, NamedThingId]])

slots.participant = Slot(uri=EXPOSOME_SCHEMA.participant, name="participant", curie=EXPOSOME_SCHEMA.curie('participant'),
                   model_uri=EXPOSOME_SCHEMA.participant, domain=None, range=Optional[Union[str, ParticipantId]])

slots.measurement_value = Slot(uri=EXPOSOME_SCHEMA.measurement_value, name="measurement_value", curie=EXPOSOME_SCHEMA.curie('measurement_value'),
                   model_uri=EXPOSOME_SCHEMA.measurement_value, domain=None, range=Optional[float])

slots.measurement_unit = Slot(uri=EXPOSOME_SCHEMA.measurement_unit, name="measurement_unit", curie=EXPOSOME_SCHEMA.curie('measurement_unit'),
                   model_uri=EXPOSOME_SCHEMA.measurement_unit, domain=None, range=Optional[str])

slots.measurement_method = Slot(uri=EXPOSOME_SCHEMA.measurement_method, name="measurement_method", curie=EXPOSOME_SCHEMA.curie('measurement_method'),
                   model_uri=EXPOSOME_SCHEMA.measurement_method, domain=None, range=Optional[str])

slots.measurement_date = Slot(uri=EXPOSOME_SCHEMA.measurement_date, name="measurement_date", curie=EXPOSOME_SCHEMA.curie('measurement_date'),
                   model_uri=EXPOSOME_SCHEMA.measurement_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.sample_type = Slot(uri=EXPOSOME_SCHEMA.sample_type, name="sample_type", curie=EXPOSOME_SCHEMA.curie('sample_type'),
                   model_uri=EXPOSOME_SCHEMA.sample_type, domain=None, range=Optional[Union[str, "SampleTypeEnum"]])

slots.biomarker_type = Slot(uri=EXPOSOME_SCHEMA.biomarker_type, name="biomarker_type", curie=EXPOSOME_SCHEMA.curie('biomarker_type'),
                   model_uri=EXPOSOME_SCHEMA.biomarker_type, domain=None, range=Optional[str])

slots.phenotype = Slot(uri=EXPOSOME_SCHEMA.phenotype, name="phenotype", curie=EXPOSOME_SCHEMA.curie('phenotype'),
                   model_uri=EXPOSOME_SCHEMA.phenotype, domain=None, range=Optional[Union[str, PhenotypeId]])

slots.cohort = Slot(uri=EXPOSOME_SCHEMA.cohort, name="cohort", curie=EXPOSOME_SCHEMA.curie('cohort'),
                   model_uri=EXPOSOME_SCHEMA.cohort, domain=None, range=Optional[Union[str, CohortId]])

slots.summary_statistic = Slot(uri=EXPOSOME_SCHEMA.summary_statistic, name="summary_statistic", curie=EXPOSOME_SCHEMA.curie('summary_statistic'),
                   model_uri=EXPOSOME_SCHEMA.summary_statistic, domain=None, range=Optional[Union[str, "SummaryStatisticEnum"]])

slots.statistic_value = Slot(uri=EXPOSOME_SCHEMA.statistic_value, name="statistic_value", curie=EXPOSOME_SCHEMA.curie('statistic_value'),
                   model_uri=EXPOSOME_SCHEMA.statistic_value, domain=None, range=Optional[float])

slots.sample_size = Slot(uri=EXPOSOME_SCHEMA.sample_size, name="sample_size", curie=EXPOSOME_SCHEMA.curie('sample_size'),
                   model_uri=EXPOSOME_SCHEMA.sample_size, domain=None, range=Optional[int])

slots.stratification = Slot(uri=EXPOSOME_SCHEMA.stratification, name="stratification", curie=EXPOSOME_SCHEMA.curie('stratification'),
                   model_uri=EXPOSOME_SCHEMA.stratification, domain=None, range=Optional[str])

slots.ncbigene_id = Slot(uri=EXPOSOME_SCHEMA.ncbigene_id, name="ncbigene_id", curie=EXPOSOME_SCHEMA.curie('ncbigene_id'),
                   model_uri=EXPOSOME_SCHEMA.ncbigene_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+$'))

slots.symbol = Slot(uri=EXPOSOME_SCHEMA.symbol, name="symbol", curie=EXPOSOME_SCHEMA.curie('symbol'),
                   model_uri=EXPOSOME_SCHEMA.symbol, domain=None, range=Optional[str])

slots.in_taxon = Slot(uri=EXPOSOME_SCHEMA.in_taxon, name="in_taxon", curie=EXPOSOME_SCHEMA.curie('in_taxon'),
                   model_uri=EXPOSOME_SCHEMA.in_taxon, domain=None, range=Optional[str])

slots.encoded_by_gene = Slot(uri=EXPOSOME_SCHEMA.encoded_by_gene, name="encoded_by_gene", curie=EXPOSOME_SCHEMA.curie('encoded_by_gene'),
                   model_uri=EXPOSOME_SCHEMA.encoded_by_gene, domain=None, range=Optional[Union[str, GeneId]])

slots.cl_id = Slot(uri=EXPOSOME_SCHEMA.cl_id, name="cl_id", curie=EXPOSOME_SCHEMA.curie('cl_id'),
                   model_uri=EXPOSOME_SCHEMA.cl_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^CL:\d{7}$'))

slots.uberon_id = Slot(uri=EXPOSOME_SCHEMA.uberon_id, name="uberon_id", curie=EXPOSOME_SCHEMA.curie('uberon_id'),
                   model_uri=EXPOSOME_SCHEMA.uberon_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^UBERON:\d{7}$'))

slots.taxon_id = Slot(uri=EXPOSOME_SCHEMA.taxon_id, name="taxon_id", curie=EXPOSOME_SCHEMA.curie('taxon_id'),
                   model_uri=EXPOSOME_SCHEMA.taxon_id, domain=None, range=Optional[str])

slots.source_database = Slot(uri=EXPOSOME_SCHEMA.source_database, name="source_database", curie=EXPOSOME_SCHEMA.curie('source_database'),
                   model_uri=EXPOSOME_SCHEMA.source_database, domain=None, range=Optional[str])

slots.source_database_record = Slot(uri=EXPOSOME_SCHEMA.source_database_record, name="source_database_record", curie=EXPOSOME_SCHEMA.curie('source_database_record'),
                   model_uri=EXPOSOME_SCHEMA.source_database_record, domain=None, range=Optional[str])

slots.lifestage = Slot(uri=EXPOSOME_SCHEMA.lifestage, name="lifestage", curie=EXPOSOME_SCHEMA.curie('lifestage'),
                   model_uri=EXPOSOME_SCHEMA.lifestage, domain=None, range=Optional[str])

slots.receiver = Slot(uri=EXPOSOME_SCHEMA.receiver, name="receiver", curie=EXPOSOME_SCHEMA.curie('receiver'),
                   model_uri=EXPOSOME_SCHEMA.receiver, domain=None, range=Optional[Union[str, BiologicalEntityId]])

slots.record_url = Slot(uri=EXPOSOME_SCHEMA.record_url, name="record_url", curie=EXPOSOME_SCHEMA.curie('record_url'),
                   model_uri=EXPOSOME_SCHEMA.record_url, domain=None, range=Optional[Union[str, URI]])

slots.last_updated = Slot(uri=EXPOSOME_SCHEMA.last_updated, name="last_updated", curie=EXPOSOME_SCHEMA.curie('last_updated'),
                   model_uri=EXPOSOME_SCHEMA.last_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.survey_cycle = Slot(uri=EXPOSOME_SCHEMA.survey_cycle, name="survey_cycle", curie=EXPOSOME_SCHEMA.curie('survey_cycle'),
                   model_uri=EXPOSOME_SCHEMA.survey_cycle, domain=None, range=Optional[str])

slots.variable_name = Slot(uri=EXPOSOME_SCHEMA.variable_name, name="variable_name", curie=EXPOSOME_SCHEMA.curie('variable_name'),
                   model_uri=EXPOSOME_SCHEMA.variable_name, domain=None, range=Optional[str])

slots.exposure = Slot(uri=EXPOSOME_SCHEMA.exposure, name="exposure", curie=EXPOSOME_SCHEMA.curie('exposure'),
                   model_uri=EXPOSOME_SCHEMA.exposure, domain=None, range=Optional[Union[dict, ExposureEvent]])

slots.chemical = Slot(uri=EXPOSOME_SCHEMA.chemical, name="chemical", curie=EXPOSOME_SCHEMA.curie('chemical'),
                   model_uri=EXPOSOME_SCHEMA.chemical, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.gene = Slot(uri=EXPOSOME_SCHEMA.gene, name="gene", curie=EXPOSOME_SCHEMA.curie('gene'),
                   model_uri=EXPOSOME_SCHEMA.gene, domain=None, range=Optional[Union[str, GeneId]])

slots.disease = Slot(uri=EXPOSOME_SCHEMA.disease, name="disease", curie=EXPOSOME_SCHEMA.curie('disease'),
                   model_uri=EXPOSOME_SCHEMA.disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.association_type = Slot(uri=EXPOSOME_SCHEMA.association_type, name="association_type", curie=EXPOSOME_SCHEMA.curie('association_type'),
                   model_uri=EXPOSOME_SCHEMA.association_type, domain=None, range=Optional[str])

slots.evidence = Slot(uri=EXPOSOME_SCHEMA.evidence, name="evidence", curie=EXPOSOME_SCHEMA.curie('evidence'),
                   model_uri=EXPOSOME_SCHEMA.evidence, domain=None, range=Optional[str])

slots.interaction_type = Slot(uri=EXPOSOME_SCHEMA.interaction_type, name="interaction_type", curie=EXPOSOME_SCHEMA.curie('interaction_type'),
                   model_uri=EXPOSOME_SCHEMA.interaction_type, domain=None, range=Optional[str])

slots.genetic_variant = Slot(uri=EXPOSOME_SCHEMA.genetic_variant, name="genetic_variant", curie=EXPOSOME_SCHEMA.curie('genetic_variant'),
                   model_uri=EXPOSOME_SCHEMA.genetic_variant, domain=None, range=Optional[str])

slots.p_value = Slot(uri=EXPOSOME_SCHEMA.p_value, name="p_value", curie=EXPOSOME_SCHEMA.curie('p_value'),
                   model_uri=EXPOSOME_SCHEMA.p_value, domain=None, range=Optional[float])

slots.effect_size = Slot(uri=EXPOSOME_SCHEMA.effect_size, name="effect_size", curie=EXPOSOME_SCHEMA.curie('effect_size'),
                   model_uri=EXPOSOME_SCHEMA.effect_size, domain=None, range=Optional[float])

slots.has_exposure = Slot(uri=ECTO['0000006'], name="has_exposure", curie=ECTO.curie('0000006'),
                   model_uri=EXPOSOME_SCHEMA.has_exposure, domain=Participant, range=Optional[Union[Union[dict, ExposureEvent], list[Union[dict, ExposureEvent]]]])

slots.causes_phenotype = Slot(uri=BIOLINK.causes, name="causes_phenotype", curie=BIOLINK.curie('causes'),
                   model_uri=EXPOSOME_SCHEMA.causes_phenotype, domain=ExposureEvent, range=Optional[Union[Union[str, PhenotypeId], list[Union[str, PhenotypeId]]]])

slots.leads_to_molecular_event = Slot(uri=EXPOSOME_SCHEMA.leads_to_molecular_event, name="leads_to_molecular_event", curie=EXPOSOME_SCHEMA.curie('leads_to_molecular_event'),
                   model_uri=EXPOSOME_SCHEMA.leads_to_molecular_event, domain=ExposureEvent, range=Optional[Union[str, MolecularInitiatingEventId]])

slots.triggers_key_event = Slot(uri=EXPOSOME_SCHEMA.triggers_key_event, name="triggers_key_event", curie=EXPOSOME_SCHEMA.curie('triggers_key_event'),
                   model_uri=EXPOSOME_SCHEMA.triggers_key_event, domain=MolecularInitiatingEvent, range=Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]])

slots.measured_in_study = Slot(uri=EXPOSOME_SCHEMA.measured_in_study, name="measured_in_study", curie=EXPOSOME_SCHEMA.curie('measured_in_study'),
                   model_uri=EXPOSOME_SCHEMA.measured_in_study, domain=Measurement, range=Optional[Union[str, StudyId]])

slots.exposomeDatabase__chemical_entities = Slot(uri=EXPOSOME_SCHEMA.chemical_entities, name="exposomeDatabase__chemical_entities", curie=EXPOSOME_SCHEMA.curie('chemical_entities'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__chemical_entities, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.exposomeDatabase__exposures = Slot(uri=EXPOSOME_SCHEMA.exposures, name="exposomeDatabase__exposures", curie=EXPOSOME_SCHEMA.curie('exposures'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__exposures, domain=None, range=Optional[Union[Union[dict, ExposureEvent], list[Union[dict, ExposureEvent]]]])

slots.exposomeDatabase__health_outcomes = Slot(uri=EXPOSOME_SCHEMA.health_outcomes, name="exposomeDatabase__health_outcomes", curie=EXPOSOME_SCHEMA.curie('health_outcomes'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__health_outcomes, domain=None, range=Optional[Union[dict[Union[str, HealthOutcomeId], Union[dict, HealthOutcome]], list[Union[dict, HealthOutcome]]]])

slots.exposomeDatabase__adverse_outcome_pathways = Slot(uri=EXPOSOME_SCHEMA.adverse_outcome_pathways, name="exposomeDatabase__adverse_outcome_pathways", curie=EXPOSOME_SCHEMA.curie('adverse_outcome_pathways'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__adverse_outcome_pathways, domain=None, range=Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, AdverseOutcomePathway]], list[Union[dict, AdverseOutcomePathway]]]])

slots.exposomeDatabase__studies = Slot(uri=EXPOSOME_SCHEMA.studies, name="exposomeDatabase__studies", curie=EXPOSOME_SCHEMA.curie('studies'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__studies, domain=None, range=Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.exposomeDatabase__cohorts = Slot(uri=EXPOSOME_SCHEMA.cohorts, name="exposomeDatabase__cohorts", curie=EXPOSOME_SCHEMA.curie('cohorts'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__cohorts, domain=None, range=Optional[Union[dict[Union[str, CohortId], Union[dict, Cohort]], list[Union[dict, Cohort]]]])

slots.exposomeDatabase__participants = Slot(uri=EXPOSOME_SCHEMA.participants, name="exposomeDatabase__participants", curie=EXPOSOME_SCHEMA.curie('participants'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__participants, domain=None, range=Optional[Union[dict[Union[str, ParticipantId], Union[dict, Participant]], list[Union[dict, Participant]]]])

slots.exposomeDatabase__measurements = Slot(uri=EXPOSOME_SCHEMA.measurements, name="exposomeDatabase__measurements", curie=EXPOSOME_SCHEMA.curie('measurements'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__measurements, domain=None, range=Optional[Union[dict[Union[str, MeasurementId], Union[dict, Measurement]], list[Union[dict, Measurement]]]])

slots.exposomeDatabase__biological_entities = Slot(uri=EXPOSOME_SCHEMA.biological_entities, name="exposomeDatabase__biological_entities", curie=EXPOSOME_SCHEMA.curie('biological_entities'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__biological_entities, domain=None, range=Optional[Union[dict[Union[str, BiologicalEntityId], Union[dict, BiologicalEntity]], list[Union[dict, BiologicalEntity]]]])

slots.exposomeDatabase__database_records = Slot(uri=EXPOSOME_SCHEMA.database_records, name="exposomeDatabase__database_records", curie=EXPOSOME_SCHEMA.curie('database_records'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__database_records, domain=None, range=Optional[Union[str, list[str]]])

slots.exposomeDatabase__associations = Slot(uri=EXPOSOME_SCHEMA.associations, name="exposomeDatabase__associations", curie=EXPOSOME_SCHEMA.curie('associations'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__associations, domain=None, range=Optional[Union[dict[Union[str, AssociationId], Union[dict, Association]], list[Union[dict, Association]]]])
