# Auto generated from exposome_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-24T13:42:22
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

from linkml_runtime.linkml_model.types import Date, Datetime, Float, Integer, String, Time, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Namespaces
AOPWIKI = CurieNamespace('AOPWIKI', 'https://aopwiki.org/aops/')
AQS = CurieNamespace('AQS', 'https://aqs.epa.gov/api/')
CENSUS = CurieNamespace('CENSUS', 'https://api.census.gov/data/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CTD_CHEMICAL = CurieNamespace('CTD_CHEMICAL', 'http://ctdbase.org/detail.go?type=chem&acc=')
CTD_GENE = CurieNamespace('CTD_GENE', 'http://ctdbase.org/detail.go?type=gene&acc=')
DTXSID = CurieNamespace('DTXSID', 'https://comptox.epa.gov/dashboard/dsstoxdb/results?search=')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
GEO = CurieNamespace('GEO', 'http://www.opengis.net/ont/geosparql#')
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
WGS84 = CurieNamespace('WGS84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
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


class ChemicalEntityId(NamedThingId):
    pass


class ExposureEventId(NamedThingId):
    pass


class BiologicalResponseId(NamedThingId):
    pass


class HealthOutcomeId(NamedThingId):
    pass


class StudyEntityId(NamedThingId):
    pass


class MeasurementId(NamedThingId):
    pass


class AssociationId(NamedThingId):
    pass


class ChemicalExposureId(ExposureEventId):
    pass


class DietaryExposureId(ExposureEventId):
    pass


class EnvironmentalExposureId(ExposureEventId):
    pass


class OccupationalExposureId(ExposureEventId):
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


class CellTypeId(BiologicalEntityId):
    pass


class AnatomicalEntityId(BiologicalEntityId):
    pass


class OrganismId(BiologicalEntityId):
    pass


class GeoLocationId(NamedThingId):
    pass


class H3SpatialIndexId(NamedThingId):
    pass


class GeographicEntityId(NamedThingId):
    pass


class CensusGeographyId(GeographicEntityId):
    pass


class SpatiotemporalIndexId(NamedThingId):
    pass


class TemporalEntityId(NamedThingId):
    pass


class AQSMonitoringSiteId(NamedThingId):
    pass


class AQSMeasurementId(MeasurementId):
    pass


class AirQualityParameterId(NamedThingId):
    pass


class ACSEstimateId(MeasurementId):
    pass


class ACSVariableId(NamedThingId):
    pass


class DemographicDataId(NamedThingId):
    pass


class GeolocatedDatasetId(NamedThingId):
    pass


class DatabaseRecordId(NamedThingId):
    pass


class NHANESRecordId(DatabaseRecordId):
    pass


class CTDRecordId(DatabaseRecordId):
    pass


class ChEMBLRecordId(DatabaseRecordId):
    pass


class GWASRecordId(DatabaseRecordId):
    pass


class AOPWikiRecordId(DatabaseRecordId):
    pass


class ToxCastRecordId(DatabaseRecordId):
    pass


class CompToxRecordId(DatabaseRecordId):
    pass


class GeneExpressionAtlasRecordId(DatabaseRecordId):
    pass


class USDARecordId(DatabaseRecordId):
    pass


class ExposureToPhenotypeAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class GeneticVariantToPhenotypeAssociationId(AssociationId):
    pass


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

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["BiologicalEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None

@dataclass(repr=False)
class ChemicalEntity(NamedThing):
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
class ExposureEvent(NamedThing):
    """
    An event in which an organism is exposed to a chemical or environmental factor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposureEvent"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposureEvent

    id: Union[str, ExposureEventId] = None
    exposed_to_chemical: Optional[Union[str, ChemicalEntityId]] = None
    exposure_route: Optional[Union[str, "ExposureRouteEnum"]] = None
    exposure_duration: Optional[str] = None
    exposure_concentration: Optional[float] = None
    exposure_medium: Optional[Union[str, "ExposureMediumEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.exposed_to_chemical is not None and not isinstance(self.exposed_to_chemical, ChemicalEntityId):
            self.exposed_to_chemical = ChemicalEntityId(self.exposed_to_chemical)

        if self.exposure_route is not None and not isinstance(self.exposure_route, ExposureRouteEnum):
            self.exposure_route = ExposureRouteEnum(self.exposure_route)

        if self.exposure_duration is not None and not isinstance(self.exposure_duration, str):
            self.exposure_duration = str(self.exposure_duration)

        if self.exposure_concentration is not None and not isinstance(self.exposure_concentration, float):
            self.exposure_concentration = float(self.exposure_concentration)

        if self.exposure_medium is not None and not isinstance(self.exposure_medium, ExposureMediumEnum):
            self.exposure_medium = ExposureMediumEnum(self.exposure_medium)

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
class HealthOutcome(NamedThing):
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
class ChemicalExposure(ExposureEvent):
    """
    Exposure to a chemical substance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000006"]
    class_class_curie: ClassVar[str] = "ECTO:0000006"
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
class DietaryExposure(ExposureEvent):
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
class EnvironmentalExposure(ExposureEvent):
    """
    Exposure to environmental factors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000001"]
    class_class_curie: ClassVar[str] = "ECTO:0000001"
    class_name: ClassVar[str] = "EnvironmentalExposure"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    environmental_context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.environmental_context is not None and not isinstance(self.environmental_context, str):
            self.environmental_context = str(self.environmental_context)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OccupationalExposure(ExposureEvent):
    """
    Exposure in an occupational setting
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["0000002"]
    class_class_curie: ClassVar[str] = "ECTO:0000002"
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
class Phenotype(HealthOutcome):
    """
    An observable characteristic or trait
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = HP["0000118"]
    class_class_curie: ClassVar[str] = "HP:0000118"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.Phenotype

    id: Union[str, PhenotypeId] = None
    hp_id: Optional[Union[str, URIorCURIE]] = None
    upheno_id: Optional[Union[str, URIorCURIE]] = None
    phenotype_category: Optional[str] = None
    severity: Optional[str] = None
    onset_age: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.hp_id is not None and not isinstance(self.hp_id, URIorCURIE):
            self.hp_id = URIorCURIE(self.hp_id)

        if self.upheno_id is not None and not isinstance(self.upheno_id, URIorCURIE):
            self.upheno_id = URIorCURIE(self.upheno_id)

        if self.phenotype_category is not None and not isinstance(self.phenotype_category, str):
            self.phenotype_category = str(self.phenotype_category)

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
    disease_category: Optional[str] = None
    affected_anatomy: Optional[Union[str, AnatomicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self.mondo_id is not None and not isinstance(self.mondo_id, URIorCURIE):
            self.mondo_id = URIorCURIE(self.mondo_id)

        if self.disease_category is not None and not isinstance(self.disease_category, str):
            self.disease_category = str(self.disease_category)

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

    class_class_uri: ClassVar[URIRef] = ECTO["3000000"]
    class_class_curie: ClassVar[str] = "ECTO:3000000"
    class_name: ClassVar[str] = "MolecularInitiatingEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.MolecularInitiatingEvent

    id: Union[str, MolecularInitiatingEventId] = None
    biological_process: Optional[str] = None
    biological_object: Optional[str] = None
    biological_action: Optional[str] = None
    occurs_in_cell_type: Optional[Union[str, CellTypeId]] = None
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

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, CellTypeId):
            self.occurs_in_cell_type = CellTypeId(self.occurs_in_cell_type)

        if self.occurs_in_anatomy is not None and not isinstance(self.occurs_in_anatomy, AnatomicalEntityId):
            self.occurs_in_anatomy = AnatomicalEntityId(self.occurs_in_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyEvent(BiologicalResponse):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ECTO["1000000"]
    class_class_curie: ClassVar[str] = "ECTO:1000000"
    class_name: ClassVar[str] = "KeyEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.KeyEvent

    id: Union[str, KeyEventId] = None
    biological_process: Optional[str] = None
    biological_object: Optional[str] = None
    biological_action: Optional[str] = None
    level_of_biological_organization: Optional[Union[str, "BiologicalOrganizationLevelEnum"]] = None
    occurs_in_cell_type: Optional[Union[str, CellTypeId]] = None
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

        if self.occurs_in_cell_type is not None and not isinstance(self.occurs_in_cell_type, CellTypeId):
            self.occurs_in_cell_type = CellTypeId(self.occurs_in_cell_type)

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
    source_database_record: Optional[Union[str, DatabaseRecordId]] = None

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

        if self.source_database_record is not None and not isinstance(self.source_database_record, DatabaseRecordId):
            self.source_database_record = DatabaseRecordId(self.source_database_record)

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
class CellType(BiologicalEntity):
    """
    A type of cell
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CL["0000000"]
    class_class_curie: ClassVar[str] = "CL:0000000"
    class_name: ClassVar[str] = "CellType"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.CellType

    id: Union[str, CellTypeId] = None
    cl_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeId):
            self.id = CellTypeId(self.id)

        if self.cl_id is not None and not isinstance(self.cl_id, URIorCURIE):
            self.cl_id = URIorCURIE(self.cl_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical structure or system
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

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismId):
            self.id = OrganismId(self.id)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.taxon_id is not None and not isinstance(self.taxon_id, str):
            self.taxon_id = str(self.taxon_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoLocation(NamedThing):
    """
    A geographic location specified by coordinates and H3 hexagonal index
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WGS84["SpatialThing"]
    class_class_curie: ClassVar[str] = "WGS84:SpatialThing"
    class_name: ClassVar[str] = "GeoLocation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GeoLocation

    id: Union[str, GeoLocationId] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    elevation: Optional[float] = None
    h3_index: Optional[str] = None
    h3_resolution: Optional[int] = None
    coordinate_uncertainty: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeoLocationId):
            self.id = GeoLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.elevation is not None and not isinstance(self.elevation, float):
            self.elevation = float(self.elevation)

        if self.h3_index is not None and not isinstance(self.h3_index, str):
            self.h3_index = str(self.h3_index)

        if self.h3_resolution is not None and not isinstance(self.h3_resolution, int):
            self.h3_resolution = int(self.h3_resolution)

        if self.coordinate_uncertainty is not None and not isinstance(self.coordinate_uncertainty, float):
            self.coordinate_uncertainty = float(self.coordinate_uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class H3SpatialIndex(NamedThing):
    """
    An H3 hexagonal grid cell used for spatiotemporal indexing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["H3SpatialIndex"]
    class_class_curie: ClassVar[str] = "exposome_schema:H3SpatialIndex"
    class_name: ClassVar[str] = "H3SpatialIndex"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.H3SpatialIndex

    id: Union[str, H3SpatialIndexId] = None
    h3_index: Optional[str] = None
    h3_resolution: Optional[int] = None
    center_latitude: Optional[float] = None
    center_longitude: Optional[float] = None
    parent_h3_index: Optional[str] = None
    child_h3_indices: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, H3SpatialIndexId):
            self.id = H3SpatialIndexId(self.id)

        if self.h3_index is not None and not isinstance(self.h3_index, str):
            self.h3_index = str(self.h3_index)

        if self.h3_resolution is not None and not isinstance(self.h3_resolution, int):
            self.h3_resolution = int(self.h3_resolution)

        if self.center_latitude is not None and not isinstance(self.center_latitude, float):
            self.center_latitude = float(self.center_latitude)

        if self.center_longitude is not None and not isinstance(self.center_longitude, float):
            self.center_longitude = float(self.center_longitude)

        if self.parent_h3_index is not None and not isinstance(self.parent_h3_index, str):
            self.parent_h3_index = str(self.parent_h3_index)

        if not isinstance(self.child_h3_indices, list):
            self.child_h3_indices = [self.child_h3_indices] if self.child_h3_indices is not None else []
        self.child_h3_indices = [v if isinstance(v, str) else str(v) for v in self.child_h3_indices]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeographicEntity(NamedThing):
    """
    A geographic region or administrative area
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["GeographicEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:GeographicEntity"
    class_name: ClassVar[str] = "GeographicEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GeographicEntity

    id: Union[str, GeographicEntityId] = None
    geo_location: Optional[Union[str, GeoLocationId]] = None
    geographic_level: Optional[Union[str, "GeographicLevelEnum"]] = None
    geographic_identifier: Optional[str] = None
    boundary_polygon: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicEntityId):
            self.id = GeographicEntityId(self.id)

        if self.geo_location is not None and not isinstance(self.geo_location, GeoLocationId):
            self.geo_location = GeoLocationId(self.geo_location)

        if self.geographic_level is not None and not isinstance(self.geographic_level, GeographicLevelEnum):
            self.geographic_level = GeographicLevelEnum(self.geographic_level)

        if self.geographic_identifier is not None and not isinstance(self.geographic_identifier, str):
            self.geographic_identifier = str(self.geographic_identifier)

        if self.boundary_polygon is not None and not isinstance(self.boundary_polygon, str):
            self.boundary_polygon = str(self.boundary_polygon)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CensusGeography(GeographicEntity):
    """
    Census-defined geographic areas including block groups, tracts, and counties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["CensusGeography"]
    class_class_curie: ClassVar[str] = "exposome_schema:CensusGeography"
    class_name: ClassVar[str] = "CensusGeography"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.CensusGeography

    id: Union[str, CensusGeographyId] = None
    census_geographic_level: Optional[Union[str, "CensusGeographicLevelEnum"]] = None
    geoid: Optional[str] = None
    state_fips: Optional[str] = None
    county_fips: Optional[str] = None
    tract_code: Optional[str] = None
    block_group_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CensusGeographyId):
            self.id = CensusGeographyId(self.id)

        if self.census_geographic_level is not None and not isinstance(self.census_geographic_level, CensusGeographicLevelEnum):
            self.census_geographic_level = CensusGeographicLevelEnum(self.census_geographic_level)

        if self.geoid is not None and not isinstance(self.geoid, str):
            self.geoid = str(self.geoid)

        if self.state_fips is not None and not isinstance(self.state_fips, str):
            self.state_fips = str(self.state_fips)

        if self.county_fips is not None and not isinstance(self.county_fips, str):
            self.county_fips = str(self.county_fips)

        if self.tract_code is not None and not isinstance(self.tract_code, str):
            self.tract_code = str(self.tract_code)

        if self.block_group_code is not None and not isinstance(self.block_group_code, str):
            self.block_group_code = str(self.block_group_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpatiotemporalIndex(NamedThing):
    """
    A spatiotemporal index combining H3 spatial indexing with temporal information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["SpatiotemporalIndex"]
    class_class_curie: ClassVar[str] = "exposome_schema:SpatiotemporalIndex"
    class_name: ClassVar[str] = "SpatiotemporalIndex"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.SpatiotemporalIndex

    id: Union[str, SpatiotemporalIndexId] = None
    h3_spatial_index: Optional[Union[str, H3SpatialIndexId]] = None
    time_point: Optional[Union[str, XSDDateTime]] = None
    time_range_start: Optional[Union[str, XSDDateTime]] = None
    time_range_end: Optional[Union[str, XSDDateTime]] = None
    temporal_resolution: Optional[Union[str, "TemporalResolutionEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpatiotemporalIndexId):
            self.id = SpatiotemporalIndexId(self.id)

        if self.h3_spatial_index is not None and not isinstance(self.h3_spatial_index, H3SpatialIndexId):
            self.h3_spatial_index = H3SpatialIndexId(self.h3_spatial_index)

        if self.time_point is not None and not isinstance(self.time_point, XSDDateTime):
            self.time_point = XSDDateTime(self.time_point)

        if self.time_range_start is not None and not isinstance(self.time_range_start, XSDDateTime):
            self.time_range_start = XSDDateTime(self.time_range_start)

        if self.time_range_end is not None and not isinstance(self.time_range_end, XSDDateTime):
            self.time_range_end = XSDDateTime(self.time_range_end)

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, TemporalResolutionEnum):
            self.temporal_resolution = TemporalResolutionEnum(self.temporal_resolution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemporalEntity(NamedThing):
    """
    An entity with temporal extent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["TemporalEntity"]
    class_class_curie: ClassVar[str] = "exposome_schema:TemporalEntity"
    class_name: ClassVar[str] = "TemporalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.TemporalEntity

    id: Union[str, TemporalEntityId] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    temporal_resolution: Optional[Union[str, "TemporalResolutionEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, TemporalResolutionEnum):
            self.temporal_resolution = TemporalResolutionEnum(self.temporal_resolution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AQSMonitoringSite(NamedThing):
    """
    An EPA Air Quality System monitoring site
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AQSMonitoringSite"]
    class_class_curie: ClassVar[str] = "exposome_schema:AQSMonitoringSite"
    class_name: ClassVar[str] = "AQSMonitoringSite"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AQSMonitoringSite

    id: Union[str, AQSMonitoringSiteId] = None
    site_id: Optional[str] = None
    site_name: Optional[str] = None
    geo_location: Optional[Union[str, GeoLocationId]] = None
    h3_index: Optional[str] = None
    site_type: Optional[Union[str, "MonitoringSiteTypeEnum"]] = None
    monitoring_agency: Optional[str] = None
    establishment_date: Optional[Union[str, XSDDate]] = None
    closure_date: Optional[Union[str, XSDDate]] = None
    monitor_parameters: Optional[Union[Union[str, AirQualityParameterId], list[Union[str, AirQualityParameterId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AQSMonitoringSiteId):
            self.id = AQSMonitoringSiteId(self.id)

        if self.site_id is not None and not isinstance(self.site_id, str):
            self.site_id = str(self.site_id)

        if self.site_name is not None and not isinstance(self.site_name, str):
            self.site_name = str(self.site_name)

        if self.geo_location is not None and not isinstance(self.geo_location, GeoLocationId):
            self.geo_location = GeoLocationId(self.geo_location)

        if self.h3_index is not None and not isinstance(self.h3_index, str):
            self.h3_index = str(self.h3_index)

        if self.site_type is not None and not isinstance(self.site_type, MonitoringSiteTypeEnum):
            self.site_type = MonitoringSiteTypeEnum(self.site_type)

        if self.monitoring_agency is not None and not isinstance(self.monitoring_agency, str):
            self.monitoring_agency = str(self.monitoring_agency)

        if self.establishment_date is not None and not isinstance(self.establishment_date, XSDDate):
            self.establishment_date = XSDDate(self.establishment_date)

        if self.closure_date is not None and not isinstance(self.closure_date, XSDDate):
            self.closure_date = XSDDate(self.closure_date)

        if not isinstance(self.monitor_parameters, list):
            self.monitor_parameters = [self.monitor_parameters] if self.monitor_parameters is not None else []
        self.monitor_parameters = [v if isinstance(v, AirQualityParameterId) else AirQualityParameterId(v) for v in self.monitor_parameters]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AQSMeasurement(Measurement):
    """
    An air quality measurement from the EPA AQS monitoring network
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AQSMeasurement"]
    class_class_curie: ClassVar[str] = "exposome_schema:AQSMeasurement"
    class_name: ClassVar[str] = "AQSMeasurement"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AQSMeasurement

    id: Union[str, AQSMeasurementId] = None
    monitoring_site: Optional[Union[str, AQSMonitoringSiteId]] = None
    parameter_code: Optional[str] = None
    parameter_name: Optional[str] = None
    measurement_value: Optional[float] = None
    measurement_unit: Optional[str] = None
    measurement_date: Optional[Union[str, XSDDate]] = None
    measurement_time: Optional[Union[str, XSDTime]] = None
    sample_duration: Optional[str] = None
    detection_limit: Optional[float] = None
    uncertainty: Optional[float] = None
    quality_indicator: Optional[str] = None
    spatiotemporal_index: Optional[Union[str, SpatiotemporalIndexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AQSMeasurementId):
            self.id = AQSMeasurementId(self.id)

        if self.monitoring_site is not None and not isinstance(self.monitoring_site, AQSMonitoringSiteId):
            self.monitoring_site = AQSMonitoringSiteId(self.monitoring_site)

        if self.parameter_code is not None and not isinstance(self.parameter_code, str):
            self.parameter_code = str(self.parameter_code)

        if self.parameter_name is not None and not isinstance(self.parameter_name, str):
            self.parameter_name = str(self.parameter_name)

        if self.measurement_value is not None and not isinstance(self.measurement_value, float):
            self.measurement_value = float(self.measurement_value)

        if self.measurement_unit is not None and not isinstance(self.measurement_unit, str):
            self.measurement_unit = str(self.measurement_unit)

        if self.measurement_date is not None and not isinstance(self.measurement_date, XSDDate):
            self.measurement_date = XSDDate(self.measurement_date)

        if self.measurement_time is not None and not isinstance(self.measurement_time, XSDTime):
            self.measurement_time = XSDTime(self.measurement_time)

        if self.sample_duration is not None and not isinstance(self.sample_duration, str):
            self.sample_duration = str(self.sample_duration)

        if self.detection_limit is not None and not isinstance(self.detection_limit, float):
            self.detection_limit = float(self.detection_limit)

        if self.uncertainty is not None and not isinstance(self.uncertainty, float):
            self.uncertainty = float(self.uncertainty)

        if self.quality_indicator is not None and not isinstance(self.quality_indicator, str):
            self.quality_indicator = str(self.quality_indicator)

        if self.spatiotemporal_index is not None and not isinstance(self.spatiotemporal_index, SpatiotemporalIndexId):
            self.spatiotemporal_index = SpatiotemporalIndexId(self.spatiotemporal_index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AirQualityParameter(NamedThing):
    """
    An air quality parameter measured by monitoring networks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AirQualityParameter"]
    class_class_curie: ClassVar[str] = "exposome_schema:AirQualityParameter"
    class_name: ClassVar[str] = "AirQualityParameter"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AirQualityParameter

    id: Union[str, AirQualityParameterId] = None
    parameter_code: Optional[str] = None
    parameter_name: Optional[str] = None
    cas_number: Optional[str] = None
    measurement_scale: Optional[str] = None
    standard_units: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AirQualityParameterId):
            self.id = AirQualityParameterId(self.id)

        if self.parameter_code is not None and not isinstance(self.parameter_code, str):
            self.parameter_code = str(self.parameter_code)

        if self.parameter_name is not None and not isinstance(self.parameter_name, str):
            self.parameter_name = str(self.parameter_name)

        if self.cas_number is not None and not isinstance(self.cas_number, str):
            self.cas_number = str(self.cas_number)

        if self.measurement_scale is not None and not isinstance(self.measurement_scale, str):
            self.measurement_scale = str(self.measurement_scale)

        if self.standard_units is not None and not isinstance(self.standard_units, str):
            self.standard_units = str(self.standard_units)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ACSEstimate(Measurement):
    """
    A demographic or socioeconomic estimate from the American Community Survey
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ACSEstimate"]
    class_class_curie: ClassVar[str] = "exposome_schema:ACSEstimate"
    class_name: ClassVar[str] = "ACSEstimate"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ACSEstimate

    id: Union[str, ACSEstimateId] = None
    census_geography: Optional[Union[str, CensusGeographyId]] = None
    variable_code: Optional[str] = None
    variable_name: Optional[str] = None
    estimate_value: Optional[float] = None
    margin_of_error: Optional[float] = None
    survey_year: Optional[int] = None
    survey_period: Optional[str] = None
    spatiotemporal_index: Optional[Union[str, SpatiotemporalIndexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ACSEstimateId):
            self.id = ACSEstimateId(self.id)

        if self.census_geography is not None and not isinstance(self.census_geography, CensusGeographyId):
            self.census_geography = CensusGeographyId(self.census_geography)

        if self.variable_code is not None and not isinstance(self.variable_code, str):
            self.variable_code = str(self.variable_code)

        if self.variable_name is not None and not isinstance(self.variable_name, str):
            self.variable_name = str(self.variable_name)

        if self.estimate_value is not None and not isinstance(self.estimate_value, float):
            self.estimate_value = float(self.estimate_value)

        if self.margin_of_error is not None and not isinstance(self.margin_of_error, float):
            self.margin_of_error = float(self.margin_of_error)

        if self.survey_year is not None and not isinstance(self.survey_year, int):
            self.survey_year = int(self.survey_year)

        if self.survey_period is not None and not isinstance(self.survey_period, str):
            self.survey_period = str(self.survey_period)

        if self.spatiotemporal_index is not None and not isinstance(self.spatiotemporal_index, SpatiotemporalIndexId):
            self.spatiotemporal_index = SpatiotemporalIndexId(self.spatiotemporal_index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ACSVariable(NamedThing):
    """
    A variable measured in the American Community Survey
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ACSVariable"]
    class_class_curie: ClassVar[str] = "exposome_schema:ACSVariable"
    class_name: ClassVar[str] = "ACSVariable"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ACSVariable

    id: Union[str, ACSVariableId] = None
    variable_code: Optional[str] = None
    variable_name: Optional[str] = None
    variable_category: Optional[Union[str, "ACSVariableCategoryEnum"]] = None
    universe: Optional[str] = None
    data_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ACSVariableId):
            self.id = ACSVariableId(self.id)

        if self.variable_code is not None and not isinstance(self.variable_code, str):
            self.variable_code = str(self.variable_code)

        if self.variable_name is not None and not isinstance(self.variable_name, str):
            self.variable_name = str(self.variable_name)

        if self.variable_category is not None and not isinstance(self.variable_category, ACSVariableCategoryEnum):
            self.variable_category = ACSVariableCategoryEnum(self.variable_category)

        if self.universe is not None and not isinstance(self.universe, str):
            self.universe = str(self.universe)

        if self.data_type is not None and not isinstance(self.data_type, str):
            self.data_type = str(self.data_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DemographicData(NamedThing):
    """
    Demographic information for a geographic area
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["DemographicData"]
    class_class_curie: ClassVar[str] = "exposome_schema:DemographicData"
    class_name: ClassVar[str] = "DemographicData"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.DemographicData

    id: Union[str, DemographicDataId] = None
    census_geography: Optional[Union[str, CensusGeographyId]] = None
    total_population: Optional[int] = None
    population_density: Optional[float] = None
    median_age: Optional[float] = None
    median_household_income: Optional[float] = None
    spatiotemporal_index: Optional[Union[str, SpatiotemporalIndexId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DemographicDataId):
            self.id = DemographicDataId(self.id)

        if self.census_geography is not None and not isinstance(self.census_geography, CensusGeographyId):
            self.census_geography = CensusGeographyId(self.census_geography)

        if self.total_population is not None and not isinstance(self.total_population, int):
            self.total_population = int(self.total_population)

        if self.population_density is not None and not isinstance(self.population_density, float):
            self.population_density = float(self.population_density)

        if self.median_age is not None and not isinstance(self.median_age, float):
            self.median_age = float(self.median_age)

        if self.median_household_income is not None and not isinstance(self.median_household_income, float):
            self.median_household_income = float(self.median_household_income)

        if self.spatiotemporal_index is not None and not isinstance(self.spatiotemporal_index, SpatiotemporalIndexId):
            self.spatiotemporal_index = SpatiotemporalIndexId(self.spatiotemporal_index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeolocatedDataset(NamedThing):
    """
    A dataset with geographic and temporal indexing using H3
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["GeolocatedDataset"]
    class_class_curie: ClassVar[str] = "exposome_schema:GeolocatedDataset"
    class_name: ClassVar[str] = "GeolocatedDataset"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GeolocatedDataset

    id: Union[str, GeolocatedDatasetId] = None
    dataset_name: Optional[str] = None
    dataset_type: Optional[str] = None
    coverage_area: Optional[str] = None
    temporal_coverage_start: Optional[Union[str, XSDDate]] = None
    temporal_coverage_end: Optional[Union[str, XSDDate]] = None
    h3_resolution_levels: Optional[Union[int, list[int]]] = empty_list()
    data_source: Optional[Union[str, "DataSourceEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeolocatedDatasetId):
            self.id = GeolocatedDatasetId(self.id)

        if self.dataset_name is not None and not isinstance(self.dataset_name, str):
            self.dataset_name = str(self.dataset_name)

        if self.dataset_type is not None and not isinstance(self.dataset_type, str):
            self.dataset_type = str(self.dataset_type)

        if self.coverage_area is not None and not isinstance(self.coverage_area, str):
            self.coverage_area = str(self.coverage_area)

        if self.temporal_coverage_start is not None and not isinstance(self.temporal_coverage_start, XSDDate):
            self.temporal_coverage_start = XSDDate(self.temporal_coverage_start)

        if self.temporal_coverage_end is not None and not isinstance(self.temporal_coverage_end, XSDDate):
            self.temporal_coverage_end = XSDDate(self.temporal_coverage_end)

        if not isinstance(self.h3_resolution_levels, list):
            self.h3_resolution_levels = [self.h3_resolution_levels] if self.h3_resolution_levels is not None else []
        self.h3_resolution_levels = [v if isinstance(v, int) else int(v) for v in self.h3_resolution_levels]

        if self.data_source is not None and not isinstance(self.data_source, DataSourceEnum):
            self.data_source = DataSourceEnum(self.data_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatabaseRecord(NamedThing):
    """
    A record from an external database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["DatabaseRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:DatabaseRecord"
    class_name: ClassVar[str] = "DatabaseRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.DatabaseRecord

    id: Union[str, DatabaseRecordId] = None
    source_database: Optional[str] = None
    record_url: Optional[Union[str, URI]] = None
    last_updated: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.source_database is not None and not isinstance(self.source_database, str):
            self.source_database = str(self.source_database)

        if self.record_url is not None and not isinstance(self.record_url, URI):
            self.record_url = URI(self.record_url)

        if self.last_updated is not None and not isinstance(self.last_updated, XSDDate):
            self.last_updated = XSDDate(self.last_updated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NHANESRecord(DatabaseRecord):
    """
    A record from the National Health and Nutrition Examination Survey
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["NHANESRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:NHANESRecord"
    class_name: ClassVar[str] = "NHANESRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.NHANESRecord

    id: Union[str, NHANESRecordId] = None
    survey_cycle: Optional[str] = None
    variable_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NHANESRecordId):
            self.id = NHANESRecordId(self.id)

        if self.survey_cycle is not None and not isinstance(self.survey_cycle, str):
            self.survey_cycle = str(self.survey_cycle)

        if self.variable_name is not None and not isinstance(self.variable_name, str):
            self.variable_name = str(self.variable_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CTDRecord(DatabaseRecord):
    """
    A record from the Comparative Toxicogenomics Database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["CTDRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:CTDRecord"
    class_name: ClassVar[str] = "CTDRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.CTDRecord

    id: Union[str, CTDRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CTDRecordId):
            self.id = CTDRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChEMBLRecord(DatabaseRecord):
    """
    A record from ChEMBL chemical database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ChEMBLRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:ChEMBLRecord"
    class_name: ClassVar[str] = "ChEMBLRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ChEMBLRecord

    id: Union[str, ChEMBLRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChEMBLRecordId):
            self.id = ChEMBLRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GWASRecord(DatabaseRecord):
    """
    A record from the GWAS Catalog
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["GWASRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:GWASRecord"
    class_name: ClassVar[str] = "GWASRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GWASRecord

    id: Union[str, GWASRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GWASRecordId):
            self.id = GWASRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AOPWikiRecord(DatabaseRecord):
    """
    A record from the AOP Wiki
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["AOPWikiRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:AOPWikiRecord"
    class_name: ClassVar[str] = "AOPWikiRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.AOPWikiRecord

    id: Union[str, AOPWikiRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AOPWikiRecordId):
            self.id = AOPWikiRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToxCastRecord(DatabaseRecord):
    """
    A record from the ToxCast database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ToxCastRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:ToxCastRecord"
    class_name: ClassVar[str] = "ToxCastRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ToxCastRecord

    id: Union[str, ToxCastRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToxCastRecordId):
            self.id = ToxCastRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompToxRecord(DatabaseRecord):
    """
    A record from the EPA CompTox Chemicals Dashboard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["CompToxRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:CompToxRecord"
    class_name: ClassVar[str] = "CompToxRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.CompToxRecord

    id: Union[str, CompToxRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompToxRecordId):
            self.id = CompToxRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionAtlasRecord(DatabaseRecord):
    """
    A record from the Gene Expression Atlas
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["GeneExpressionAtlasRecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:GeneExpressionAtlasRecord"
    class_name: ClassVar[str] = "GeneExpressionAtlasRecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.GeneExpressionAtlasRecord

    id: Union[str, GeneExpressionAtlasRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneExpressionAtlasRecordId):
            self.id = GeneExpressionAtlasRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class USDARecord(DatabaseRecord):
    """
    A record from USDA Pesticide Data Program
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["USDARecord"]
    class_class_curie: ClassVar[str] = "exposome_schema:USDARecord"
    class_name: ClassVar[str] = "USDARecord"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.USDARecord

    id: Union[str, USDARecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, USDARecordId):
            self.id = USDARecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureToPhenotypeAssociation(Association):
    """
    An association between an exposure and a phenotype
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ExposureToPhenotypeAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:ExposureToPhenotypeAssociation"
    class_name: ClassVar[str] = "ExposureToPhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ExposureToPhenotypeAssociation

    id: Union[str, ExposureToPhenotypeAssociationId] = None
    exposure: Optional[Union[str, ExposureEventId]] = None
    phenotype: Optional[Union[str, PhenotypeId]] = None
    association_type: Optional[str] = None
    evidence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureToPhenotypeAssociationId):
            self.id = ExposureToPhenotypeAssociationId(self.id)

        if self.exposure is not None and not isinstance(self.exposure, ExposureEventId):
            self.exposure = ExposureEventId(self.exposure)

        if self.phenotype is not None and not isinstance(self.phenotype, PhenotypeId):
            self.phenotype = PhenotypeId(self.phenotype)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        if self.evidence is not None and not isinstance(self.evidence, str):
            self.evidence = str(self.evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalToGeneAssociation(Association):
    """
    An association between a chemical and a gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA["ChemicalToGeneAssociation"]
    class_class_curie: ClassVar[str] = "exposome_schema:ChemicalToGeneAssociation"
    class_name: ClassVar[str] = "ChemicalToGeneAssociation"
    class_model_uri: ClassVar[URIRef] = EXPOSOME_SCHEMA.ChemicalToGeneAssociation

    id: Union[str, ChemicalToGeneAssociationId] = None
    chemical: Optional[Union[str, ChemicalEntityId]] = None
    gene: Optional[Union[str, GeneId]] = None
    interaction_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)

        if self.chemical is not None and not isinstance(self.chemical, ChemicalEntityId):
            self.chemical = ChemicalEntityId(self.chemical)

        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

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
    exposures: Optional[Union[dict[Union[str, ExposureEventId], Union[dict, ExposureEvent]], list[Union[dict, ExposureEvent]]]] = empty_dict()
    health_outcomes: Optional[Union[dict[Union[str, HealthOutcomeId], Union[dict, HealthOutcome]], list[Union[dict, HealthOutcome]]]] = empty_dict()
    adverse_outcome_pathways: Optional[Union[dict[Union[str, AdverseOutcomePathwayId], Union[dict, AdverseOutcomePathway]], list[Union[dict, AdverseOutcomePathway]]]] = empty_dict()
    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]] = empty_dict()
    cohorts: Optional[Union[dict[Union[str, CohortId], Union[dict, Cohort]], list[Union[dict, Cohort]]]] = empty_dict()
    participants: Optional[Union[dict[Union[str, ParticipantId], Union[dict, Participant]], list[Union[dict, Participant]]]] = empty_dict()
    measurements: Optional[Union[dict[Union[str, MeasurementId], Union[dict, Measurement]], list[Union[dict, Measurement]]]] = empty_dict()
    biological_entities: Optional[Union[dict[Union[str, BiologicalEntityId], Union[dict, BiologicalEntity]], list[Union[dict, BiologicalEntity]]]] = empty_dict()
    database_records: Optional[Union[dict[Union[str, DatabaseRecordId], Union[dict, DatabaseRecord]], list[Union[dict, DatabaseRecord]]]] = empty_dict()
    associations: Optional[Union[dict[Union[str, AssociationId], Union[dict, Association]], list[Union[dict, Association]]]] = empty_dict()
    geo_locations: Optional[Union[dict[Union[str, GeoLocationId], Union[dict, GeoLocation]], list[Union[dict, GeoLocation]]]] = empty_dict()
    h3_spatial_indices: Optional[Union[dict[Union[str, H3SpatialIndexId], Union[dict, H3SpatialIndex]], list[Union[dict, H3SpatialIndex]]]] = empty_dict()
    geographic_entities: Optional[Union[dict[Union[str, GeographicEntityId], Union[dict, GeographicEntity]], list[Union[dict, GeographicEntity]]]] = empty_dict()
    spatiotemporal_indices: Optional[Union[dict[Union[str, SpatiotemporalIndexId], Union[dict, SpatiotemporalIndex]], list[Union[dict, SpatiotemporalIndex]]]] = empty_dict()
    aqs_monitoring_sites: Optional[Union[dict[Union[str, AQSMonitoringSiteId], Union[dict, AQSMonitoringSite]], list[Union[dict, AQSMonitoringSite]]]] = empty_dict()
    aqs_measurements: Optional[Union[dict[Union[str, AQSMeasurementId], Union[dict, AQSMeasurement]], list[Union[dict, AQSMeasurement]]]] = empty_dict()
    acs_estimates: Optional[Union[dict[Union[str, ACSEstimateId], Union[dict, ACSEstimate]], list[Union[dict, ACSEstimate]]]] = empty_dict()
    demographic_data: Optional[Union[dict[Union[str, DemographicDataId], Union[dict, DemographicData]], list[Union[dict, DemographicData]]]] = empty_dict()
    geolocated_datasets: Optional[Union[dict[Union[str, GeolocatedDatasetId], Union[dict, GeolocatedDataset]], list[Union[dict, GeolocatedDataset]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="chemical_entities", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="exposures", slot_type=ExposureEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="health_outcomes", slot_type=HealthOutcome, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="adverse_outcome_pathways", slot_type=AdverseOutcomePathway, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cohorts", slot_type=Cohort, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="participants", slot_type=Participant, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="biological_entities", slot_type=BiologicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="database_records", slot_type=DatabaseRecord, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="associations", slot_type=Association, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="geo_locations", slot_type=GeoLocation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="h3_spatial_indices", slot_type=H3SpatialIndex, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="geographic_entities", slot_type=GeographicEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="spatiotemporal_indices", slot_type=SpatiotemporalIndex, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aqs_monitoring_sites", slot_type=AQSMonitoringSite, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aqs_measurements", slot_type=AQSMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="acs_estimates", slot_type=ACSEstimate, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="demographic_data", slot_type=DemographicData, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="geolocated_datasets", slot_type=GeolocatedDataset, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class ExposureRouteEnum(EnumDefinitionImpl):
    """
    Routes of exposure to chemicals or environmental factors
    """
    Oral = PermissibleValue(
        text="Oral",
        description="Oral ingestion",
        meaning=ECTO["0000895"])
    Dermal = PermissibleValue(
        text="Dermal",
        description="Dermal contact",
        meaning=ECTO["0000896"])
    Inhalation = PermissibleValue(
        text="Inhalation",
        description="Inhalation",
        meaning=ECTO["0000897"])
    Injection = PermissibleValue(
        text="Injection",
        description="Injection")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown route")

    _defn = EnumDefinition(
        name="ExposureRouteEnum",
        description="Routes of exposure to chemicals or environmental factors",
    )

class ExposureMediumEnum(EnumDefinitionImpl):
    """
    Medium through which exposure occurs
    """
    Air = PermissibleValue(
        text="Air",
        description="Air",
        meaning=ENVO["00002005"])
    Water = PermissibleValue(
        text="Water",
        description="Water",
        meaning=ENVO["00002006"])
    Food = PermissibleValue(
        text="Food",
        description="Food",
        meaning=FOODON["00002403"])
    Soil = PermissibleValue(
        text="Soil",
        description="Soil",
        meaning=ENVO["00001998"])
    Dust = PermissibleValue(
        text="Dust",
        description="Dust")
    ConsumerProduct = PermissibleValue(
        text="ConsumerProduct",
        description="Consumer product")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown medium")

    _defn = EnumDefinition(
        name="ExposureMediumEnum",
        description="Medium through which exposure occurs",
    )

class BiologicalOrganizationLevelEnum(EnumDefinitionImpl):
    """
    Levels of biological organization
    """
    Molecular = PermissibleValue(
        text="Molecular",
        description="Molecular level",
        meaning=EFO["0001432"])
    Cellular = PermissibleValue(
        text="Cellular",
        description="Cellular level",
        meaning=CL["0000000"])
    Tissue = PermissibleValue(
        text="Tissue",
        description="Tissue level",
        meaning=UBERON["0000479"])
    Organ = PermissibleValue(
        text="Organ",
        description="Organ level",
        meaning=UBERON["0000062"])
    Organism = PermissibleValue(
        text="Organism",
        description="Organism level",
        meaning=UBERON["0000468"])
    Population = PermissibleValue(
        text="Population",
        description="Population level")

    _defn = EnumDefinition(
        name="BiologicalOrganizationLevelEnum",
        description="Levels of biological organization",
    )

class StudyTypeEnum(EnumDefinitionImpl):
    """
    Types of research studies
    """
    Cohort = PermissibleValue(
        text="Cohort",
        description="Cohort study",
        meaning=EFO["0001444"])
    CrossSectional = PermissibleValue(
        text="CrossSectional",
        description="Cross-sectional study",
        meaning=EFO["0001745"])
    CaseControl = PermissibleValue(
        text="CaseControl",
        description="Case-control study",
        meaning=EFO["0001427"])
    RandomizedControlledTrial = PermissibleValue(
        text="RandomizedControlledTrial",
        description="Randomized controlled trial",
        meaning=EFO["0001427"])
    Survey = PermissibleValue(
        text="Survey",
        description="Survey")
    Gwas = PermissibleValue(
        text="Gwas",
        description="Genome-wide association study",
        meaning=EFO["0000508"])
    Other = PermissibleValue(
        text="Other",
        description="Other study type")

    _defn = EnumDefinition(
        name="StudyTypeEnum",
        description="Types of research studies",
    )

class DataSourceEnum(EnumDefinitionImpl):
    """
    Data sources and repositories
    """
    Nhanes = PermissibleValue(
        text="Nhanes",
        description="National Health and Nutrition Examination Survey")
    Chear = PermissibleValue(
        text="Chear",
        description="Children's Health Exposure Analysis Resource")
    Hhear = PermissibleValue(
        text="Hhear",
        description="Human Health Exposure Analysis Resource")
    AopWiki = PermissibleValue(
        text="AopWiki",
        description="AOP Wiki")
    Ctd = PermissibleValue(
        text="Ctd",
        description="Comparative Toxicogenomics Database")
    ToxCast = PermissibleValue(
        text="ToxCast",
        description="ToxCast")
    Tox21 = PermissibleValue(
        text="Tox21",
        description="Tox21")
    ChemBl = PermissibleValue(
        text="ChemBl",
        description="ChEMBL")
    CompTox = PermissibleValue(
        text="CompTox",
        description="CompTox Dashboard")
    GwasCatalog = PermissibleValue(
        text="GwasCatalog",
        description="GWAS Catalog")
    GeneExpressionAtlas = PermissibleValue(
        text="GeneExpressionAtlas",
        description="Gene Expression Atlas")
    UsdaPesticide = PermissibleValue(
        text="UsdaPesticide",
        description="USDA Pesticide Data Program")
    Wweia = PermissibleValue(
        text="Wweia",
        description="What We Eat In America")
    Aqs = PermissibleValue(
        text="Aqs",
        description="EPA Air Quality System")
    Acs = PermissibleValue(
        text="Acs",
        description="American Community Survey")
    Other = PermissibleValue(
        text="Other",
        description="Other data source")

    _defn = EnumDefinition(
        name="DataSourceEnum",
        description="Data sources and repositories",
    )

class SexEnum(EnumDefinitionImpl):
    """
    Biological sex
    """
    Male = PermissibleValue(
        text="Male",
        description="Male",
        meaning=PATO["0000384"])
    Female = PermissibleValue(
        text="Female",
        description="Female",
        meaning=PATO["0000383"])
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown")

    _defn = EnumDefinition(
        name="SexEnum",
        description="Biological sex",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples
    """
    Blood = PermissibleValue(
        text="Blood",
        description="Blood sample")
    Urine = PermissibleValue(
        text="Urine",
        description="Urine sample")
    Serum = PermissibleValue(
        text="Serum",
        description="Serum sample")
    Plasma = PermissibleValue(
        text="Plasma",
        description="Plasma sample")
    Tissue = PermissibleValue(
        text="Tissue",
        description="Tissue sample")
    Saliva = PermissibleValue(
        text="Saliva",
        description="Saliva sample")
    Hair = PermissibleValue(
        text="Hair",
        description="Hair sample")
    Nail = PermissibleValue(
        text="Nail",
        description="Nail sample")
    Other = PermissibleValue(
        text="Other",
        description="Other sample type")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples",
    )

class SummaryStatisticEnum(EnumDefinitionImpl):
    """
    Types of summary statistics
    """
    Mean = PermissibleValue(
        text="Mean",
        description="Arithmetic mean")
    Median = PermissibleValue(
        text="Median",
        description="Median")
    Mode = PermissibleValue(
        text="Mode",
        description="Mode")
    Percentile = PermissibleValue(
        text="Percentile",
        description="Percentile")
    StandardDeviation = PermissibleValue(
        text="StandardDeviation",
        description="Standard deviation")
    Variance = PermissibleValue(
        text="Variance",
        description="Variance")
    Range = PermissibleValue(
        text="Range",
        description="Range")
    InterquartileRange = PermissibleValue(
        text="InterquartileRange",
        description="Interquartile range")

    _defn = EnumDefinition(
        name="SummaryStatisticEnum",
        description="Types of summary statistics",
    )

class GeographicLevelEnum(EnumDefinitionImpl):
    """
    Levels of geographic aggregation
    """
    Global = PermissibleValue(
        text="Global",
        description="Global level")
    Country = PermissibleValue(
        text="Country",
        description="Country level")
    State = PermissibleValue(
        text="State",
        description="State or province level")
    County = PermissibleValue(
        text="County",
        description="County level")
    City = PermissibleValue(
        text="City",
        description="City or municipality level")
    Neighborhood = PermissibleValue(
        text="Neighborhood",
        description="Neighborhood level")
    PostalCode = PermissibleValue(
        text="PostalCode",
        description="Postal code or ZIP code level")
    Custom = PermissibleValue(
        text="Custom",
        description="Custom geographic boundary")

    _defn = EnumDefinition(
        name="GeographicLevelEnum",
        description="Levels of geographic aggregation",
    )

class CensusGeographicLevelEnum(EnumDefinitionImpl):
    """
    US Census geographic hierarchy levels
    """
    Nation = PermissibleValue(
        text="Nation",
        description="National level")
    State = PermissibleValue(
        text="State",
        description="State level")
    County = PermissibleValue(
        text="County",
        description="County level")
    Tract = PermissibleValue(
        text="Tract",
        description="Census tract level")
    BlockGroup = PermissibleValue(
        text="BlockGroup",
        description="Block group level")
    Block = PermissibleValue(
        text="Block",
        description="Census block level (not available in ACS)")
    Place = PermissibleValue(
        text="Place",
        description="Incorporated place (city/town)")
    MetropolitanStatisticalArea = PermissibleValue(
        text="MetropolitanStatisticalArea",
        description="Metropolitan Statistical Area (MSA)")
    CongressionalDistrict = PermissibleValue(
        text="CongressionalDistrict",
        description="Congressional district")
    ZctaZipCode = PermissibleValue(
        text="ZctaZipCode",
        description="ZIP Code Tabulation Area (ZCTA)")

    _defn = EnumDefinition(
        name="CensusGeographicLevelEnum",
        description="US Census geographic hierarchy levels",
    )

class TemporalResolutionEnum(EnumDefinitionImpl):
    """
    Temporal resolution of data
    """
    Instantaneous = PermissibleValue(
        text="Instantaneous",
        description="Single point in time")
    Hourly = PermissibleValue(
        text="Hourly",
        description="Hourly aggregation")
    Daily = PermissibleValue(
        text="Daily",
        description="Daily aggregation")
    Weekly = PermissibleValue(
        text="Weekly",
        description="Weekly aggregation")
    Monthly = PermissibleValue(
        text="Monthly",
        description="Monthly aggregation")
    Quarterly = PermissibleValue(
        text="Quarterly",
        description="Quarterly aggregation")
    Annual = PermissibleValue(
        text="Annual",
        description="Annual aggregation")
    Decadal = PermissibleValue(
        text="Decadal",
        description="Decadal aggregation")
    Custom = PermissibleValue(
        text="Custom",
        description="Custom temporal resolution")

    _defn = EnumDefinition(
        name="TemporalResolutionEnum",
        description="Temporal resolution of data",
    )

class MonitoringSiteTypeEnum(EnumDefinitionImpl):
    """
    Types of environmental monitoring sites
    """
    Urban = PermissibleValue(
        text="Urban",
        description="Urban monitoring site")
    Suburban = PermissibleValue(
        text="Suburban",
        description="Suburban monitoring site")
    Rural = PermissibleValue(
        text="Rural",
        description="Rural monitoring site")
    NearRoad = PermissibleValue(
        text="NearRoad",
        description="Near-road monitoring site")
    Industrial = PermissibleValue(
        text="Industrial",
        description="Industrial area monitoring site")
    Background = PermissibleValue(
        text="Background",
        description="Background monitoring site")
    Mobile = PermissibleValue(
        text="Mobile",
        description="Mobile monitoring site")
    Other = PermissibleValue(
        text="Other",
        description="Other site type")

    _defn = EnumDefinition(
        name="MonitoringSiteTypeEnum",
        description="Types of environmental monitoring sites",
    )

class ACSVariableCategoryEnum(EnumDefinitionImpl):
    """
    Categories of American Community Survey variables
    """
    Age = PermissibleValue(
        text="Age",
        description="Age and sex")
    Race = PermissibleValue(
        text="Race",
        description="Race and ethnicity")
    Household = PermissibleValue(
        text="Household",
        description="Household composition")
    Housing = PermissibleValue(
        text="Housing",
        description="Housing characteristics")
    Income = PermissibleValue(
        text="Income",
        description="Income and earnings")
    Employment = PermissibleValue(
        text="Employment",
        description="Employment and occupation")
    Education = PermissibleValue(
        text="Education",
        description="Educational attainment")
    Poverty = PermissibleValue(
        text="Poverty",
        description="Poverty status")
    Transportation = PermissibleValue(
        text="Transportation",
        description="Transportation and commuting")
    Health = PermissibleValue(
        text="Health",
        description="Health insurance coverage")
    Veterans = PermissibleValue(
        text="Veterans",
        description="Veteran status")
    Disability = PermissibleValue(
        text="Disability",
        description="Disability status")
    Language = PermissibleValue(
        text="Language",
        description="Language spoken at home")
    Immigration = PermissibleValue(
        text="Immigration",
        description="Citizenship and immigration")
    Ancestry = PermissibleValue(
        text="Ancestry",
        description="Ancestry and origin")
    Other = PermissibleValue(
        text="Other",
        description="Other variable category")

    _defn = EnumDefinition(
        name="ACSVariableCategoryEnum",
        description="Categories of American Community Survey variables",
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

slots.exposed_to_chemical = Slot(uri=CHEBI['24431'], name="exposed_to_chemical", curie=CHEBI.curie('24431'),
                   model_uri=EXPOSOME_SCHEMA.exposed_to_chemical, domain=None, range=Optional[Union[str, ChemicalEntityId]])

slots.exposure_route = Slot(uri=EXPOSOME_SCHEMA.exposure_route, name="exposure_route", curie=EXPOSOME_SCHEMA.curie('exposure_route'),
                   model_uri=EXPOSOME_SCHEMA.exposure_route, domain=None, range=Optional[Union[str, "ExposureRouteEnum"]])

slots.exposure_duration = Slot(uri=EXPOSOME_SCHEMA.exposure_duration, name="exposure_duration", curie=EXPOSOME_SCHEMA.curie('exposure_duration'),
                   model_uri=EXPOSOME_SCHEMA.exposure_duration, domain=None, range=Optional[str])

slots.exposure_concentration = Slot(uri=EXPOSOME_SCHEMA.exposure_concentration, name="exposure_concentration", curie=EXPOSOME_SCHEMA.curie('exposure_concentration'),
                   model_uri=EXPOSOME_SCHEMA.exposure_concentration, domain=None, range=Optional[float])

slots.exposure_medium = Slot(uri=EXPOSOME_SCHEMA.exposure_medium, name="exposure_medium", curie=EXPOSOME_SCHEMA.curie('exposure_medium'),
                   model_uri=EXPOSOME_SCHEMA.exposure_medium, domain=None, range=Optional[Union[str, "ExposureMediumEnum"]])

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

slots.hp_id = Slot(uri=EXPOSOME_SCHEMA.hp_id, name="hp_id", curie=EXPOSOME_SCHEMA.curie('hp_id'),
                   model_uri=EXPOSOME_SCHEMA.hp_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^HP:\d{7}$'))

slots.upheno_id = Slot(uri=EXPOSOME_SCHEMA.upheno_id, name="upheno_id", curie=EXPOSOME_SCHEMA.curie('upheno_id'),
                   model_uri=EXPOSOME_SCHEMA.upheno_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^UPHENO:\d+$'))

slots.phenotype_category = Slot(uri=EXPOSOME_SCHEMA.phenotype_category, name="phenotype_category", curie=EXPOSOME_SCHEMA.curie('phenotype_category'),
                   model_uri=EXPOSOME_SCHEMA.phenotype_category, domain=None, range=Optional[str])

slots.severity = Slot(uri=EXPOSOME_SCHEMA.severity, name="severity", curie=EXPOSOME_SCHEMA.curie('severity'),
                   model_uri=EXPOSOME_SCHEMA.severity, domain=None, range=Optional[str])

slots.onset_age = Slot(uri=EXPOSOME_SCHEMA.onset_age, name="onset_age", curie=EXPOSOME_SCHEMA.curie('onset_age'),
                   model_uri=EXPOSOME_SCHEMA.onset_age, domain=None, range=Optional[str])

slots.mondo_id = Slot(uri=EXPOSOME_SCHEMA.mondo_id, name="mondo_id", curie=EXPOSOME_SCHEMA.curie('mondo_id'),
                   model_uri=EXPOSOME_SCHEMA.mondo_id, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^MONDO:\d{7}$'))

slots.disease_category = Slot(uri=EXPOSOME_SCHEMA.disease_category, name="disease_category", curie=EXPOSOME_SCHEMA.curie('disease_category'),
                   model_uri=EXPOSOME_SCHEMA.disease_category, domain=None, range=Optional[str])

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
                   model_uri=EXPOSOME_SCHEMA.occurs_in_cell_type, domain=None, range=Optional[Union[str, CellTypeId]])

slots.occurs_in_anatomy = Slot(uri=UBERON['0001062'], name="occurs_in_anatomy", curie=UBERON.curie('0001062'),
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

slots.source_database_record = Slot(uri=EXPOSOME_SCHEMA.source_database_record, name="source_database_record", curie=EXPOSOME_SCHEMA.curie('source_database_record'),
                   model_uri=EXPOSOME_SCHEMA.source_database_record, domain=None, range=Optional[Union[str, DatabaseRecordId]])

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

slots.record_url = Slot(uri=EXPOSOME_SCHEMA.record_url, name="record_url", curie=EXPOSOME_SCHEMA.curie('record_url'),
                   model_uri=EXPOSOME_SCHEMA.record_url, domain=None, range=Optional[Union[str, URI]])

slots.last_updated = Slot(uri=EXPOSOME_SCHEMA.last_updated, name="last_updated", curie=EXPOSOME_SCHEMA.curie('last_updated'),
                   model_uri=EXPOSOME_SCHEMA.last_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.survey_cycle = Slot(uri=EXPOSOME_SCHEMA.survey_cycle, name="survey_cycle", curie=EXPOSOME_SCHEMA.curie('survey_cycle'),
                   model_uri=EXPOSOME_SCHEMA.survey_cycle, domain=None, range=Optional[str])

slots.variable_name = Slot(uri=EXPOSOME_SCHEMA.variable_name, name="variable_name", curie=EXPOSOME_SCHEMA.curie('variable_name'),
                   model_uri=EXPOSOME_SCHEMA.variable_name, domain=None, range=Optional[str])

slots.exposure = Slot(uri=EXPOSOME_SCHEMA.exposure, name="exposure", curie=EXPOSOME_SCHEMA.curie('exposure'),
                   model_uri=EXPOSOME_SCHEMA.exposure, domain=None, range=Optional[Union[str, ExposureEventId]])

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
                   model_uri=EXPOSOME_SCHEMA.has_exposure, domain=Participant, range=Optional[Union[Union[str, ExposureEventId], list[Union[str, ExposureEventId]]]])

slots.causes_phenotype = Slot(uri=BIOLINK.causes, name="causes_phenotype", curie=BIOLINK.curie('causes'),
                   model_uri=EXPOSOME_SCHEMA.causes_phenotype, domain=ExposureEvent, range=Optional[Union[Union[str, PhenotypeId], list[Union[str, PhenotypeId]]]])

slots.leads_to_molecular_event = Slot(uri=EXPOSOME_SCHEMA.leads_to_molecular_event, name="leads_to_molecular_event", curie=EXPOSOME_SCHEMA.curie('leads_to_molecular_event'),
                   model_uri=EXPOSOME_SCHEMA.leads_to_molecular_event, domain=ExposureEvent, range=Optional[Union[str, MolecularInitiatingEventId]])

slots.triggers_key_event = Slot(uri=EXPOSOME_SCHEMA.triggers_key_event, name="triggers_key_event", curie=EXPOSOME_SCHEMA.curie('triggers_key_event'),
                   model_uri=EXPOSOME_SCHEMA.triggers_key_event, domain=MolecularInitiatingEvent, range=Optional[Union[Union[str, KeyEventId], list[Union[str, KeyEventId]]]])

slots.measured_in_study = Slot(uri=EXPOSOME_SCHEMA.measured_in_study, name="measured_in_study", curie=EXPOSOME_SCHEMA.curie('measured_in_study'),
                   model_uri=EXPOSOME_SCHEMA.measured_in_study, domain=Measurement, range=Optional[Union[str, StudyId]])

slots.latitude = Slot(uri=WGS84.lat, name="latitude", curie=WGS84.curie('lat'),
                   model_uri=EXPOSOME_SCHEMA.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=WGS84.long, name="longitude", curie=WGS84.curie('long'),
                   model_uri=EXPOSOME_SCHEMA.longitude, domain=None, range=Optional[float])

slots.elevation = Slot(uri=EXPOSOME_SCHEMA.elevation, name="elevation", curie=EXPOSOME_SCHEMA.curie('elevation'),
                   model_uri=EXPOSOME_SCHEMA.elevation, domain=None, range=Optional[float])

slots.h3_index = Slot(uri=EXPOSOME_SCHEMA.h3_index, name="h3_index", curie=EXPOSOME_SCHEMA.curie('h3_index'),
                   model_uri=EXPOSOME_SCHEMA.h3_index, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9a-f]{15}$'))

slots.h3_resolution = Slot(uri=EXPOSOME_SCHEMA.h3_resolution, name="h3_resolution", curie=EXPOSOME_SCHEMA.curie('h3_resolution'),
                   model_uri=EXPOSOME_SCHEMA.h3_resolution, domain=None, range=Optional[int])

slots.coordinate_uncertainty = Slot(uri=EXPOSOME_SCHEMA.coordinate_uncertainty, name="coordinate_uncertainty", curie=EXPOSOME_SCHEMA.curie('coordinate_uncertainty'),
                   model_uri=EXPOSOME_SCHEMA.coordinate_uncertainty, domain=None, range=Optional[float])

slots.center_latitude = Slot(uri=EXPOSOME_SCHEMA.center_latitude, name="center_latitude", curie=EXPOSOME_SCHEMA.curie('center_latitude'),
                   model_uri=EXPOSOME_SCHEMA.center_latitude, domain=None, range=Optional[float])

slots.center_longitude = Slot(uri=EXPOSOME_SCHEMA.center_longitude, name="center_longitude", curie=EXPOSOME_SCHEMA.curie('center_longitude'),
                   model_uri=EXPOSOME_SCHEMA.center_longitude, domain=None, range=Optional[float])

slots.parent_h3_index = Slot(uri=EXPOSOME_SCHEMA.parent_h3_index, name="parent_h3_index", curie=EXPOSOME_SCHEMA.curie('parent_h3_index'),
                   model_uri=EXPOSOME_SCHEMA.parent_h3_index, domain=None, range=Optional[str])

slots.child_h3_indices = Slot(uri=EXPOSOME_SCHEMA.child_h3_indices, name="child_h3_indices", curie=EXPOSOME_SCHEMA.curie('child_h3_indices'),
                   model_uri=EXPOSOME_SCHEMA.child_h3_indices, domain=None, range=Optional[Union[str, list[str]]])

slots.geo_location = Slot(uri=EXPOSOME_SCHEMA.geo_location, name="geo_location", curie=EXPOSOME_SCHEMA.curie('geo_location'),
                   model_uri=EXPOSOME_SCHEMA.geo_location, domain=None, range=Optional[Union[str, GeoLocationId]])

slots.geographic_level = Slot(uri=EXPOSOME_SCHEMA.geographic_level, name="geographic_level", curie=EXPOSOME_SCHEMA.curie('geographic_level'),
                   model_uri=EXPOSOME_SCHEMA.geographic_level, domain=None, range=Optional[Union[str, "GeographicLevelEnum"]])

slots.geographic_identifier = Slot(uri=EXPOSOME_SCHEMA.geographic_identifier, name="geographic_identifier", curie=EXPOSOME_SCHEMA.curie('geographic_identifier'),
                   model_uri=EXPOSOME_SCHEMA.geographic_identifier, domain=None, range=Optional[str])

slots.boundary_polygon = Slot(uri=EXPOSOME_SCHEMA.boundary_polygon, name="boundary_polygon", curie=EXPOSOME_SCHEMA.curie('boundary_polygon'),
                   model_uri=EXPOSOME_SCHEMA.boundary_polygon, domain=None, range=Optional[str])

slots.census_geographic_level = Slot(uri=EXPOSOME_SCHEMA.census_geographic_level, name="census_geographic_level", curie=EXPOSOME_SCHEMA.curie('census_geographic_level'),
                   model_uri=EXPOSOME_SCHEMA.census_geographic_level, domain=None, range=Optional[Union[str, "CensusGeographicLevelEnum"]])

slots.geoid = Slot(uri=EXPOSOME_SCHEMA.geoid, name="geoid", curie=EXPOSOME_SCHEMA.curie('geoid'),
                   model_uri=EXPOSOME_SCHEMA.geoid, domain=None, range=Optional[str])

slots.state_fips = Slot(uri=EXPOSOME_SCHEMA.state_fips, name="state_fips", curie=EXPOSOME_SCHEMA.curie('state_fips'),
                   model_uri=EXPOSOME_SCHEMA.state_fips, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{2}$'))

slots.county_fips = Slot(uri=EXPOSOME_SCHEMA.county_fips, name="county_fips", curie=EXPOSOME_SCHEMA.curie('county_fips'),
                   model_uri=EXPOSOME_SCHEMA.county_fips, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{3}$'))

slots.tract_code = Slot(uri=EXPOSOME_SCHEMA.tract_code, name="tract_code", curie=EXPOSOME_SCHEMA.curie('tract_code'),
                   model_uri=EXPOSOME_SCHEMA.tract_code, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d{6}$'))

slots.block_group_code = Slot(uri=EXPOSOME_SCHEMA.block_group_code, name="block_group_code", curie=EXPOSOME_SCHEMA.curie('block_group_code'),
                   model_uri=EXPOSOME_SCHEMA.block_group_code, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d$'))

slots.start_date = Slot(uri=EXPOSOME_SCHEMA.start_date, name="start_date", curie=EXPOSOME_SCHEMA.curie('start_date'),
                   model_uri=EXPOSOME_SCHEMA.start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.end_date = Slot(uri=EXPOSOME_SCHEMA.end_date, name="end_date", curie=EXPOSOME_SCHEMA.curie('end_date'),
                   model_uri=EXPOSOME_SCHEMA.end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.temporal_resolution = Slot(uri=EXPOSOME_SCHEMA.temporal_resolution, name="temporal_resolution", curie=EXPOSOME_SCHEMA.curie('temporal_resolution'),
                   model_uri=EXPOSOME_SCHEMA.temporal_resolution, domain=None, range=Optional[Union[str, "TemporalResolutionEnum"]])

slots.time_point = Slot(uri=EXPOSOME_SCHEMA.time_point, name="time_point", curie=EXPOSOME_SCHEMA.curie('time_point'),
                   model_uri=EXPOSOME_SCHEMA.time_point, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.time_range_start = Slot(uri=EXPOSOME_SCHEMA.time_range_start, name="time_range_start", curie=EXPOSOME_SCHEMA.curie('time_range_start'),
                   model_uri=EXPOSOME_SCHEMA.time_range_start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.time_range_end = Slot(uri=EXPOSOME_SCHEMA.time_range_end, name="time_range_end", curie=EXPOSOME_SCHEMA.curie('time_range_end'),
                   model_uri=EXPOSOME_SCHEMA.time_range_end, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.h3_spatial_index = Slot(uri=EXPOSOME_SCHEMA.h3_spatial_index, name="h3_spatial_index", curie=EXPOSOME_SCHEMA.curie('h3_spatial_index'),
                   model_uri=EXPOSOME_SCHEMA.h3_spatial_index, domain=None, range=Optional[Union[str, H3SpatialIndexId]])

slots.spatiotemporal_index = Slot(uri=EXPOSOME_SCHEMA.spatiotemporal_index, name="spatiotemporal_index", curie=EXPOSOME_SCHEMA.curie('spatiotemporal_index'),
                   model_uri=EXPOSOME_SCHEMA.spatiotemporal_index, domain=None, range=Optional[Union[str, SpatiotemporalIndexId]])

slots.site_id = Slot(uri=EXPOSOME_SCHEMA.site_id, name="site_id", curie=EXPOSOME_SCHEMA.curie('site_id'),
                   model_uri=EXPOSOME_SCHEMA.site_id, domain=None, range=Optional[str])

slots.site_name = Slot(uri=EXPOSOME_SCHEMA.site_name, name="site_name", curie=EXPOSOME_SCHEMA.curie('site_name'),
                   model_uri=EXPOSOME_SCHEMA.site_name, domain=None, range=Optional[str])

slots.site_type = Slot(uri=EXPOSOME_SCHEMA.site_type, name="site_type", curie=EXPOSOME_SCHEMA.curie('site_type'),
                   model_uri=EXPOSOME_SCHEMA.site_type, domain=None, range=Optional[Union[str, "MonitoringSiteTypeEnum"]])

slots.monitoring_agency = Slot(uri=EXPOSOME_SCHEMA.monitoring_agency, name="monitoring_agency", curie=EXPOSOME_SCHEMA.curie('monitoring_agency'),
                   model_uri=EXPOSOME_SCHEMA.monitoring_agency, domain=None, range=Optional[str])

slots.monitoring_site = Slot(uri=EXPOSOME_SCHEMA.monitoring_site, name="monitoring_site", curie=EXPOSOME_SCHEMA.curie('monitoring_site'),
                   model_uri=EXPOSOME_SCHEMA.monitoring_site, domain=None, range=Optional[Union[str, AQSMonitoringSiteId]])

slots.establishment_date = Slot(uri=EXPOSOME_SCHEMA.establishment_date, name="establishment_date", curie=EXPOSOME_SCHEMA.curie('establishment_date'),
                   model_uri=EXPOSOME_SCHEMA.establishment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.closure_date = Slot(uri=EXPOSOME_SCHEMA.closure_date, name="closure_date", curie=EXPOSOME_SCHEMA.curie('closure_date'),
                   model_uri=EXPOSOME_SCHEMA.closure_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.monitor_parameters = Slot(uri=EXPOSOME_SCHEMA.monitor_parameters, name="monitor_parameters", curie=EXPOSOME_SCHEMA.curie('monitor_parameters'),
                   model_uri=EXPOSOME_SCHEMA.monitor_parameters, domain=None, range=Optional[Union[Union[str, AirQualityParameterId], list[Union[str, AirQualityParameterId]]]])

slots.parameter_code = Slot(uri=EXPOSOME_SCHEMA.parameter_code, name="parameter_code", curie=EXPOSOME_SCHEMA.curie('parameter_code'),
                   model_uri=EXPOSOME_SCHEMA.parameter_code, domain=None, range=Optional[str])

slots.parameter_name = Slot(uri=EXPOSOME_SCHEMA.parameter_name, name="parameter_name", curie=EXPOSOME_SCHEMA.curie('parameter_name'),
                   model_uri=EXPOSOME_SCHEMA.parameter_name, domain=None, range=Optional[str])

slots.measurement_time = Slot(uri=EXPOSOME_SCHEMA.measurement_time, name="measurement_time", curie=EXPOSOME_SCHEMA.curie('measurement_time'),
                   model_uri=EXPOSOME_SCHEMA.measurement_time, domain=None, range=Optional[Union[str, XSDTime]])

slots.sample_duration = Slot(uri=EXPOSOME_SCHEMA.sample_duration, name="sample_duration", curie=EXPOSOME_SCHEMA.curie('sample_duration'),
                   model_uri=EXPOSOME_SCHEMA.sample_duration, domain=None, range=Optional[str])

slots.detection_limit = Slot(uri=EXPOSOME_SCHEMA.detection_limit, name="detection_limit", curie=EXPOSOME_SCHEMA.curie('detection_limit'),
                   model_uri=EXPOSOME_SCHEMA.detection_limit, domain=None, range=Optional[float])

slots.uncertainty = Slot(uri=EXPOSOME_SCHEMA.uncertainty, name="uncertainty", curie=EXPOSOME_SCHEMA.curie('uncertainty'),
                   model_uri=EXPOSOME_SCHEMA.uncertainty, domain=None, range=Optional[float])

slots.quality_indicator = Slot(uri=EXPOSOME_SCHEMA.quality_indicator, name="quality_indicator", curie=EXPOSOME_SCHEMA.curie('quality_indicator'),
                   model_uri=EXPOSOME_SCHEMA.quality_indicator, domain=None, range=Optional[str])

slots.measurement_scale = Slot(uri=EXPOSOME_SCHEMA.measurement_scale, name="measurement_scale", curie=EXPOSOME_SCHEMA.curie('measurement_scale'),
                   model_uri=EXPOSOME_SCHEMA.measurement_scale, domain=None, range=Optional[str])

slots.standard_units = Slot(uri=EXPOSOME_SCHEMA.standard_units, name="standard_units", curie=EXPOSOME_SCHEMA.curie('standard_units'),
                   model_uri=EXPOSOME_SCHEMA.standard_units, domain=None, range=Optional[str])

slots.census_geography = Slot(uri=EXPOSOME_SCHEMA.census_geography, name="census_geography", curie=EXPOSOME_SCHEMA.curie('census_geography'),
                   model_uri=EXPOSOME_SCHEMA.census_geography, domain=None, range=Optional[Union[str, CensusGeographyId]])

slots.variable_code = Slot(uri=EXPOSOME_SCHEMA.variable_code, name="variable_code", curie=EXPOSOME_SCHEMA.curie('variable_code'),
                   model_uri=EXPOSOME_SCHEMA.variable_code, domain=None, range=Optional[str])

slots.variable_category = Slot(uri=EXPOSOME_SCHEMA.variable_category, name="variable_category", curie=EXPOSOME_SCHEMA.curie('variable_category'),
                   model_uri=EXPOSOME_SCHEMA.variable_category, domain=None, range=Optional[Union[str, "ACSVariableCategoryEnum"]])

slots.estimate_value = Slot(uri=EXPOSOME_SCHEMA.estimate_value, name="estimate_value", curie=EXPOSOME_SCHEMA.curie('estimate_value'),
                   model_uri=EXPOSOME_SCHEMA.estimate_value, domain=None, range=Optional[float])

slots.margin_of_error = Slot(uri=EXPOSOME_SCHEMA.margin_of_error, name="margin_of_error", curie=EXPOSOME_SCHEMA.curie('margin_of_error'),
                   model_uri=EXPOSOME_SCHEMA.margin_of_error, domain=None, range=Optional[float])

slots.survey_year = Slot(uri=EXPOSOME_SCHEMA.survey_year, name="survey_year", curie=EXPOSOME_SCHEMA.curie('survey_year'),
                   model_uri=EXPOSOME_SCHEMA.survey_year, domain=None, range=Optional[int])

slots.survey_period = Slot(uri=EXPOSOME_SCHEMA.survey_period, name="survey_period", curie=EXPOSOME_SCHEMA.curie('survey_period'),
                   model_uri=EXPOSOME_SCHEMA.survey_period, domain=None, range=Optional[str])

slots.universe = Slot(uri=EXPOSOME_SCHEMA.universe, name="universe", curie=EXPOSOME_SCHEMA.curie('universe'),
                   model_uri=EXPOSOME_SCHEMA.universe, domain=None, range=Optional[str])

slots.data_type = Slot(uri=EXPOSOME_SCHEMA.data_type, name="data_type", curie=EXPOSOME_SCHEMA.curie('data_type'),
                   model_uri=EXPOSOME_SCHEMA.data_type, domain=None, range=Optional[str])

slots.total_population = Slot(uri=EXPOSOME_SCHEMA.total_population, name="total_population", curie=EXPOSOME_SCHEMA.curie('total_population'),
                   model_uri=EXPOSOME_SCHEMA.total_population, domain=None, range=Optional[int])

slots.population_density = Slot(uri=EXPOSOME_SCHEMA.population_density, name="population_density", curie=EXPOSOME_SCHEMA.curie('population_density'),
                   model_uri=EXPOSOME_SCHEMA.population_density, domain=None, range=Optional[float])

slots.median_age = Slot(uri=EXPOSOME_SCHEMA.median_age, name="median_age", curie=EXPOSOME_SCHEMA.curie('median_age'),
                   model_uri=EXPOSOME_SCHEMA.median_age, domain=None, range=Optional[float])

slots.median_household_income = Slot(uri=EXPOSOME_SCHEMA.median_household_income, name="median_household_income", curie=EXPOSOME_SCHEMA.curie('median_household_income'),
                   model_uri=EXPOSOME_SCHEMA.median_household_income, domain=None, range=Optional[float])

slots.dataset_name = Slot(uri=EXPOSOME_SCHEMA.dataset_name, name="dataset_name", curie=EXPOSOME_SCHEMA.curie('dataset_name'),
                   model_uri=EXPOSOME_SCHEMA.dataset_name, domain=None, range=Optional[str])

slots.dataset_type = Slot(uri=EXPOSOME_SCHEMA.dataset_type, name="dataset_type", curie=EXPOSOME_SCHEMA.curie('dataset_type'),
                   model_uri=EXPOSOME_SCHEMA.dataset_type, domain=None, range=Optional[str])

slots.coverage_area = Slot(uri=EXPOSOME_SCHEMA.coverage_area, name="coverage_area", curie=EXPOSOME_SCHEMA.curie('coverage_area'),
                   model_uri=EXPOSOME_SCHEMA.coverage_area, domain=None, range=Optional[str])

slots.temporal_coverage_start = Slot(uri=EXPOSOME_SCHEMA.temporal_coverage_start, name="temporal_coverage_start", curie=EXPOSOME_SCHEMA.curie('temporal_coverage_start'),
                   model_uri=EXPOSOME_SCHEMA.temporal_coverage_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.temporal_coverage_end = Slot(uri=EXPOSOME_SCHEMA.temporal_coverage_end, name="temporal_coverage_end", curie=EXPOSOME_SCHEMA.curie('temporal_coverage_end'),
                   model_uri=EXPOSOME_SCHEMA.temporal_coverage_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.h3_resolution_levels = Slot(uri=EXPOSOME_SCHEMA.h3_resolution_levels, name="h3_resolution_levels", curie=EXPOSOME_SCHEMA.curie('h3_resolution_levels'),
                   model_uri=EXPOSOME_SCHEMA.h3_resolution_levels, domain=None, range=Optional[Union[int, list[int]]])

slots.exposomeDatabase__chemical_entities = Slot(uri=EXPOSOME_SCHEMA.chemical_entities, name="exposomeDatabase__chemical_entities", curie=EXPOSOME_SCHEMA.curie('chemical_entities'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__chemical_entities, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.exposomeDatabase__exposures = Slot(uri=EXPOSOME_SCHEMA.exposures, name="exposomeDatabase__exposures", curie=EXPOSOME_SCHEMA.curie('exposures'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__exposures, domain=None, range=Optional[Union[dict[Union[str, ExposureEventId], Union[dict, ExposureEvent]], list[Union[dict, ExposureEvent]]]])

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
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__database_records, domain=None, range=Optional[Union[dict[Union[str, DatabaseRecordId], Union[dict, DatabaseRecord]], list[Union[dict, DatabaseRecord]]]])

slots.exposomeDatabase__associations = Slot(uri=EXPOSOME_SCHEMA.associations, name="exposomeDatabase__associations", curie=EXPOSOME_SCHEMA.curie('associations'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__associations, domain=None, range=Optional[Union[dict[Union[str, AssociationId], Union[dict, Association]], list[Union[dict, Association]]]])

slots.exposomeDatabase__geo_locations = Slot(uri=EXPOSOME_SCHEMA.geo_locations, name="exposomeDatabase__geo_locations", curie=EXPOSOME_SCHEMA.curie('geo_locations'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__geo_locations, domain=None, range=Optional[Union[dict[Union[str, GeoLocationId], Union[dict, GeoLocation]], list[Union[dict, GeoLocation]]]])

slots.exposomeDatabase__h3_spatial_indices = Slot(uri=EXPOSOME_SCHEMA.h3_spatial_indices, name="exposomeDatabase__h3_spatial_indices", curie=EXPOSOME_SCHEMA.curie('h3_spatial_indices'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__h3_spatial_indices, domain=None, range=Optional[Union[dict[Union[str, H3SpatialIndexId], Union[dict, H3SpatialIndex]], list[Union[dict, H3SpatialIndex]]]])

slots.exposomeDatabase__geographic_entities = Slot(uri=EXPOSOME_SCHEMA.geographic_entities, name="exposomeDatabase__geographic_entities", curie=EXPOSOME_SCHEMA.curie('geographic_entities'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__geographic_entities, domain=None, range=Optional[Union[dict[Union[str, GeographicEntityId], Union[dict, GeographicEntity]], list[Union[dict, GeographicEntity]]]])

slots.exposomeDatabase__spatiotemporal_indices = Slot(uri=EXPOSOME_SCHEMA.spatiotemporal_indices, name="exposomeDatabase__spatiotemporal_indices", curie=EXPOSOME_SCHEMA.curie('spatiotemporal_indices'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__spatiotemporal_indices, domain=None, range=Optional[Union[dict[Union[str, SpatiotemporalIndexId], Union[dict, SpatiotemporalIndex]], list[Union[dict, SpatiotemporalIndex]]]])

slots.exposomeDatabase__aqs_monitoring_sites = Slot(uri=EXPOSOME_SCHEMA.aqs_monitoring_sites, name="exposomeDatabase__aqs_monitoring_sites", curie=EXPOSOME_SCHEMA.curie('aqs_monitoring_sites'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__aqs_monitoring_sites, domain=None, range=Optional[Union[dict[Union[str, AQSMonitoringSiteId], Union[dict, AQSMonitoringSite]], list[Union[dict, AQSMonitoringSite]]]])

slots.exposomeDatabase__aqs_measurements = Slot(uri=EXPOSOME_SCHEMA.aqs_measurements, name="exposomeDatabase__aqs_measurements", curie=EXPOSOME_SCHEMA.curie('aqs_measurements'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__aqs_measurements, domain=None, range=Optional[Union[dict[Union[str, AQSMeasurementId], Union[dict, AQSMeasurement]], list[Union[dict, AQSMeasurement]]]])

slots.exposomeDatabase__acs_estimates = Slot(uri=EXPOSOME_SCHEMA.acs_estimates, name="exposomeDatabase__acs_estimates", curie=EXPOSOME_SCHEMA.curie('acs_estimates'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__acs_estimates, domain=None, range=Optional[Union[dict[Union[str, ACSEstimateId], Union[dict, ACSEstimate]], list[Union[dict, ACSEstimate]]]])

slots.exposomeDatabase__demographic_data = Slot(uri=EXPOSOME_SCHEMA.demographic_data, name="exposomeDatabase__demographic_data", curie=EXPOSOME_SCHEMA.curie('demographic_data'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__demographic_data, domain=None, range=Optional[Union[dict[Union[str, DemographicDataId], Union[dict, DemographicData]], list[Union[dict, DemographicData]]]])

slots.exposomeDatabase__geolocated_datasets = Slot(uri=EXPOSOME_SCHEMA.geolocated_datasets, name="exposomeDatabase__geolocated_datasets", curie=EXPOSOME_SCHEMA.curie('geolocated_datasets'),
                   model_uri=EXPOSOME_SCHEMA.exposomeDatabase__geolocated_datasets, domain=None, range=Optional[Union[dict[Union[str, GeolocatedDatasetId], Union[dict, GeolocatedDataset]], list[Union[dict, GeolocatedDataset]]]])
