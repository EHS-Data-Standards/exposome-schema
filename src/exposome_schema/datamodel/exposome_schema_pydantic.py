from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'exposome_schema',
     'default_range': 'string',
     'description': 'Comprehensive exposome schema for integrating chemical '
                    'exposures, environmental factors,\n'
                    'dietary data, toxicology databases, and health outcomes with '
                    'support for Adverse Outcome\n'
                    'Pathways (AOPs) and multi-granularity measurements',
     'id': 'https://w3id.org/diatomsRcool/exposome-schema',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'exposome-schema',
     'prefixes': {'AOPWIKI': {'prefix_prefix': 'AOPWIKI',
                              'prefix_reference': 'https://aopwiki.org/aops/'},
                  'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CHEMBL.COMPOUND': {'prefix_prefix': 'CHEMBL.COMPOUND',
                                      'prefix_reference': 'http://identifiers.org/chembl.compound/'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'CTD.CHEMICAL': {'prefix_prefix': 'CTD.CHEMICAL',
                                   'prefix_reference': 'http://ctdbase.org/detail.go?type=chem&acc='},
                  'CTD.GENE': {'prefix_prefix': 'CTD.GENE',
                               'prefix_reference': 'http://ctdbase.org/detail.go?type=gene&acc='},
                  'DTXSID': {'prefix_prefix': 'DTXSID',
                             'prefix_reference': 'https://comptox.epa.gov/dashboard/dsstoxdb/results?search='},
                  'ECTO': {'prefix_prefix': 'ECTO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ECTO_'},
                  'EFO': {'prefix_prefix': 'EFO',
                          'prefix_reference': 'http://identifiers.org/efo/'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'FOODON': {'prefix_prefix': 'FOODON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/FOODON_'},
                  'GWAS': {'prefix_prefix': 'GWAS',
                           'prefix_reference': 'https://www.ebi.ac.uk/gwas/studies/'},
                  'GXA': {'prefix_prefix': 'GXA',
                          'prefix_reference': 'https://www.ebi.ac.uk/gxa/experiments/'},
                  'HHEAR': {'prefix_prefix': 'HHEAR',
                            'prefix_reference': 'http://hadatac.org/ont/hhear#'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'MP': {'prefix_prefix': 'MP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/MP_'},
                  'NCBIGENE': {'prefix_prefix': 'NCBIGENE',
                               'prefix_reference': 'https://www.ncbi.nlm.nih.gov/gene/'},
                  'NHANES': {'prefix_prefix': 'NHANES',
                             'prefix_reference': 'https://wwwn.cdc.gov/Nchs/Nhanes/'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PUBCHEM.COMPOUND': {'prefix_prefix': 'PUBCHEM.COMPOUND',
                                       'prefix_reference': 'http://identifiers.org/pubchem.compound/'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UPHENO': {'prefix_prefix': 'UPHENO',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UPHENO_'},
                  'USDA.PESTICIDE': {'prefix_prefix': 'USDA.PESTICIDE',
                                     'prefix_reference': 'https://www.ams.usda.gov/datasets/pdp/'},
                  'ZP': {'prefix_prefix': 'ZP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/ZP_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'chear': {'prefix_prefix': 'chear',
                            'prefix_reference': 'http://hadatac.org/ont/chear#'},
                  'exposome_schema': {'prefix_prefix': 'exposome_schema',
                                      'prefix_reference': 'https://w3id.org/diatomsRcool/exposome-schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://diatomsRcool.github.io/exposome-schema'],
     'source_file': 'src/exposome_schema/schema/exposome_schema.yaml',
     'title': 'exposome-schema'} )

class ExposureFrequencyEnum(str, Enum):
    """
    Frequency of exposure
    """
    acute = "acute"
    """
    Single or short-term exposure
    """
    subacute = "subacute"
    """
    Repeated exposure over a short period
    """
    subchronic = "subchronic"
    """
    Repeated exposure over an intermediate period
    """
    chronic = "chronic"
    """
    Long-term or repeated exposure over a long period
    """
    intermittent = "intermittent"
    """
    Exposure occurring at irregular intervals
    """
    unknown = "unknown"
    """
    Unknown frequency
    """


class ExposureRouteEnum(str, Enum):
    """
    Routes of exposure to chemicals or environmental factors
    """
    oral = "oral"
    """
    Oral ingestion
    """
    dermal = "dermal"
    """
    Dermal contact
    """
    inhalation = "inhalation"
    """
    Inhalation
    """
    injection = "injection"
    """
    Injection
    """
    unknown = "unknown"
    """
    Unknown route
    """


class ExposureMediumEnum(str, Enum):
    """
    Medium through which exposure occurs
    """
    air = "air"
    """
    Air
    """
    water = "water"
    """
    Water
    """
    food = "food"
    """
    Food
    """
    soil = "soil"
    """
    Soil
    """
    dust = "dust"
    """
    Dust
    """
    consumer_product = "consumer_product"
    """
    Consumer product
    """
    unknown = "unknown"
    """
    Unknown medium
    """


class BiologicalOrganizationLevelEnum(str, Enum):
    """
    Levels of biological organization
    """
    molecular = "molecular"
    """
    Molecular level
    """
    cellular = "cellular"
    """
    Cellular level
    """
    tissue = "tissue"
    """
    Tissue level
    """
    organ = "organ"
    """
    Organ level
    """
    organism = "organism"
    """
    Organism level
    """
    population = "population"
    """
    Population level
    """


class StudyTypeEnum(str, Enum):
    """
    Types of research studies
    """
    cohort = "cohort"
    """
    Cohort study
    """
    cross_sectional = "cross_sectional"
    """
    Cross-sectional study
    """
    case_control = "case_control"
    """
    Case-control study
    """
    randomized_controlled_trial = "randomized_controlled_trial"
    """
    Randomized controlled trial
    """
    survey = "survey"
    """
    Survey
    """
    gwas = "gwas"
    """
    Genome-wide association study
    """
    other = "other"
    """
    Other study type
    """


class DataSourceEnum(str, Enum):
    """
    Data sources and repositories
    """
    nhanes = "nhanes"
    """
    National Health and Nutrition Examination Survey
    """
    chear = "chear"
    """
    Children's Health Exposure Analysis Resource
    """
    hhear = "hhear"
    """
    Human Health Exposure Analysis Resource
    """
    aop_wiki = "aop_wiki"
    """
    AOP Wiki
    """
    ctd = "ctd"
    """
    Comparative Toxicogenomics Database
    """
    tox_cast = "tox_cast"
    """
    ToxCast
    """
    tox21 = "tox21"
    """
    Tox21
    """
    chem_bl = "chem_bl"
    """
    ChEMBL
    """
    comp_tox = "comp_tox"
    """
    CompTox Dashboard
    """
    gwas_catalog = "gwas_catalog"
    """
    GWAS Catalog
    """
    gene_expression_atlas = "gene_expression_atlas"
    """
    Gene Expression Atlas
    """
    usda_pesticide = "usda_pesticide"
    """
    USDA Pesticide Data Program
    """
    wweia = "wweia"
    """
    What We Eat In America
    """
    other = "other"
    """
    Other data source
    """


class SexEnum(str, Enum):
    """
    Biological sex
    """
    male = "male"
    """
    Male
    """
    female = "female"
    """
    Female
    """
    unknown = "unknown"
    """
    Unknown
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological samples
    """
    blood = "blood"
    """
    Blood sample
    """
    urine = "urine"
    """
    Urine sample
    """
    serum = "serum"
    """
    Serum sample
    """
    plasma = "plasma"
    """
    Plasma sample
    """
    tissue = "tissue"
    """
    Tissue sample
    """
    saliva = "saliva"
    """
    Saliva sample
    """
    hair = "hair"
    """
    Hair sample
    """
    nail = "nail"
    """
    Nail sample
    """
    other = "other"
    """
    Other sample type
    """


class SummaryStatisticEnum(str, Enum):
    """
    Types of summary statistics
    """
    mean = "mean"
    """
    Arithmetic mean
    """
    median = "median"
    """
    Median
    """
    mode = "mode"
    """
    Mode
    """
    percentile = "percentile"
    """
    Percentile
    """
    standard_deviation = "standard_deviation"
    """
    Standard deviation
    """
    variance = "variance"
    """
    Variance
    """
    range = "range"
    """
    Range
    """
    interquartile_range = "interquartile_range"
    """
    Interquartile range
    """



class ExposureEvent(ConfiguredBaseModel):
    """
    An event in which a BiologicalEntity is exposed to a StimulusEntity and results in a BiologicalResponse
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'must_not_have_id_slot': {'tag': 'must_not_have_id_slot',
                                                   'value': True}},
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_stimulus: str = Field(default=..., description="""The stimulus involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_outcome: str = Field(default=..., description="""The biological response resulting from the exposure event""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_receiver: str = Field(default=..., description="""The organism, cell, tissue, or population being exposed""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })


class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity in the exposome
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiologicalEntity(NamedThing):
    """
    Biological entities including genes, proteins, cells, and anatomical structures
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CARO:0030000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class StimulusEntity(NamedThing):
    """
    Any entity to which a receiver is being exposed
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalEntity(StimulusEntity):
    """
    A chemical entity including compounds, drugs, and metabolites
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEBI:24431',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    chebi_id: Optional[str] = Field(default=None, description="""ChEBI identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    dtxsid: Optional[str] = Field(default=None, description="""EPA CompTox Dashboard identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    chembl_id: Optional[str] = Field(default=None, description="""ChEMBL compound identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    pubchem_cid: Optional[int] = Field(default=None, description="""PubChem Compound identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    cas_number: Optional[str] = Field(default=None, description="""CAS Registry Number""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    inchi: Optional[str] = Field(default=None, description="""InChI chemical identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    smiles: Optional[str] = Field(default=None, description="""SMILES chemical structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    molecular_formula: Optional[str] = Field(default=None, description="""Molecular formula""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('chebi_id')
    def pattern_chebi_id(cls, v):
        pattern=re.compile(r"^CHEBI:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chebi_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chebi_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('dtxsid')
    def pattern_dtxsid(cls, v):
        pattern=re.compile(r"^DTXSID\d{7,9}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid dtxsid format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid dtxsid format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chembl_id')
    def pattern_chembl_id(cls, v):
        pattern=re.compile(r"^CHEMBL\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chembl_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chembl_id format: {v}"
            raise ValueError(err_msg)
        return v


class BehavioralEntity(StimulusEntity):
    """
    A stimulus entity representing a behavior, activity, or lifestyle factor (e.g. smoking, physical activity, sleep) to which an individual may be exposed or that may mediate an exposure
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class DietEntity(StimulusEntity):
    """
    A stimulus entity representing a food, beverage, dietary pattern, or nutritional component consumed by an individual
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiologicalResponse(NamedThing):
    """
    A biological response at the molecular, cellular, or tissue level
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class HealthOutcome(BiologicalResponse):
    """
    A health-related outcome including phenotypes and diseases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class StudyEntity(NamedThing):
    """
    Entities related to studies, cohorts, and participants
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Measurement(NamedThing):
    """
    A measurement or observation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Association(NamedThing):
    """
    A relationship between two entities
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Exposure(NamedThing):
    """
    External, non-genetic, and internal stimuli, that can be chemical, physical,  biological, and psychosocial in nature, that an individual interacts with
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'ExO:0000002',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ActiveExposure(Exposure):
    """
    Direct, intentional contact with a stimulus 
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class PassiveExposure(Exposure):
    """
    Indirect, unintentional, or incidental contact with a stimulus
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    environmental_context: Optional[str] = Field(default=None, description="""Environmental context of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['PassiveExposure']} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalExposure(Exposure):
    """
    Exposure to a chemical substance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000231',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class DietaryExposure(Exposure):
    """
    Exposure through dietary consumption
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'FOODON:00002403',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    food_item: Optional[str] = Field(default=None, description="""Food item consumed""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryExposure']} })
    serving_size: Optional[str] = Field(default=None, description="""Serving size""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryExposure']} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class OccupationalExposure(Exposure):
    """
    Exposure in an occupational setting
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0001591',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    occupation: Optional[str] = Field(default=None, description="""Occupation related to exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['OccupationalExposure']} })
    workplace: Optional[str] = Field(default=None, description="""Workplace where exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['OccupationalExposure']} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExperimentalExposure(Exposure):
    """
    Exposure to a treatment in an empirical experimental setting
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'XCO:0000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    treatment: Optional[str] = Field(default=None, description="""The experimental stimulus or intervention applied to subjects in an experimental exposure setting; instantiates exposure_stimulus""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalExposure'], 'instantiates': ['exposure_stimulus']} })
    experimental_subject: Optional[str] = Field(default=None, description="""The organism, cell, tissue, or population that is the subject of an experimental exposure; instantiates exposure_receiver""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalExposure'], 'instantiates': ['exposure_receiver']} })
    experimental_result: Optional[str] = Field(default=None, description="""The biological response or outcome observed as a result of an experimental exposure; instantiates exposure_outcome""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExperimentalExposure'], 'instantiates': ['exposure_outcome']} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class PrenatalExposure(Exposure):
    """
    Exposure of a mammalian embryo or fetus via the mother
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BehavioralExposure(Exposure):
    """
    Exposure wherein the receiver engages in a behavior that mediates an exposure  or leads to a health outcome
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class SesExposure(Exposure):
    """
    Exposure to stimulus related to socioeconomic factors
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_frequency: Optional[ExposureFrequencyEnum] = Field(default=None, description="""The temporal pattern of exposure, describing how often contact with a stimulus occurs over a defined period""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Phenotype(HealthOutcome):
    """
    An observable characteristic or trait
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'UPHENO:0001001',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[str] = Field(default=None, description="""Severity of phenotype or disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    onset_age: Optional[str] = Field(default=None, description="""Age of onset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('upheno_id')
    def pattern_upheno_id(cls, v):
        pattern=re.compile(r"^UPHENO:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid upheno_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid upheno_id format: {v}"
            raise ValueError(err_msg)
        return v


class Disease(HealthOutcome):
    """
    A disease or medical condition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'MONDO:0000001',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    mondo_id: Optional[str] = Field(default=None, description="""MONDO disease identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    affected_anatomy: Optional[str] = Field(default=None, description="""Anatomical location affected""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('mondo_id')
    def pattern_mondo_id(cls, v):
        pattern=re.compile(r"^MONDO:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid mondo_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid mondo_id format: {v}"
            raise ValueError(err_msg)
        return v


class AdverseOutcome(HealthOutcome):
    """
    An adverse health outcome in the context of an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    outcome_level: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""Level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcome']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class MammalianPhenotype(Phenotype):
    """
    A phenotype observed in mammalian model organisms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'MP:0000001',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    mp_id: Optional[str] = Field(default=None, description="""Mammalian Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['MammalianPhenotype']} })
    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[str] = Field(default=None, description="""Severity of phenotype or disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    onset_age: Optional[str] = Field(default=None, description="""Age of onset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('mp_id')
    def pattern_mp_id(cls, v):
        pattern=re.compile(r"^MP:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid mp_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid mp_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('upheno_id')
    def pattern_upheno_id(cls, v):
        pattern=re.compile(r"^UPHENO:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid upheno_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid upheno_id format: {v}"
            raise ValueError(err_msg)
        return v


class ZebrafishPhenotype(Phenotype):
    """
    A phenotype observed in zebrafish
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ZP:0000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    zp_id: Optional[str] = Field(default=None, description="""Zebrafish Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZebrafishPhenotype']} })
    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[str] = Field(default=None, description="""Severity of phenotype or disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    onset_age: Optional[str] = Field(default=None, description="""Age of onset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('zp_id')
    def pattern_zp_id(cls, v):
        pattern=re.compile(r"^ZP:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid zp_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid zp_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('upheno_id')
    def pattern_upheno_id(cls, v):
        pattern=re.compile(r"^UPHENO:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid upheno_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid upheno_id format: {v}"
            raise ValueError(err_msg)
        return v


class HumanPhenotype(Phenotype):
    """
    A phenotype observed in humans
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'HP:0000001',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    hp_id: Optional[str] = Field(default=None, description="""Human Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanPhenotype']} })
    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    severity: Optional[str] = Field(default=None, description="""Severity of phenotype or disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    onset_age: Optional[str] = Field(default=None, description="""Age of onset""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('hp_id')
    def pattern_hp_id(cls, v):
        pattern=re.compile(r"^HP:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid hp_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid hp_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('upheno_id')
    def pattern_upheno_id(cls, v):
        pattern=re.compile(r"^UPHENO:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid upheno_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid upheno_id format: {v}"
            raise ValueError(err_msg)
        return v


class AdverseOutcomePathway(NamedThing):
    """
    A sequence of causally linked events at different levels of biological organization that lead from exposure to adverse health outcomes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    aopwiki_id: Optional[str] = Field(default=None, description="""AOP Wiki identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    molecular_initiating_event: Optional[str] = Field(default=None, description="""The molecular initiating event of an AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_events: Optional[list[str]] = Field(default=[], description="""Key events in an AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    key_event_relationships: Optional[list[str]] = Field(default=[], description="""Relationships between key events""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    adverse_outcome: Optional[str] = Field(default=None, description="""The adverse outcome of an AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    stressors: Optional[list[str]] = Field(default=[], description="""Chemical stressors that trigger the AOP""", json_schema_extra = { "linkml_meta": {'domain_of': ['AdverseOutcomePathway']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class MolecularInitiatingEvent(BiologicalResponse):
    """
    The initial molecular-level perturbation that starts an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    biological_process: Optional[str] = Field(default=None, description="""Biological process involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_object: Optional[str] = Field(default=None, description="""Biological object involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_action: Optional[str] = Field(default=None, description="""Biological action or change""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""Cell type where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'CL:0000000'} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""Anatomical location where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class KeyEvent(BiologicalResponse):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    biological_process: Optional[str] = Field(default=None, description="""Biological process involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_object: Optional[str] = Field(default=None, description="""Biological object involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_action: Optional[str] = Field(default=None, description="""Biological action or change""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    level_of_biological_organization: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""Level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""Cell type where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'CL:0000000'} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""Anatomical location where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class KeyEventRelationship(Association):
    """
    A directional relationship between two key events in an AOP
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    upstream_event: Optional[str] = Field(default=None, description="""Upstream key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    downstream_event: Optional[str] = Field(default=None, description="""Downstream key event""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    relationship_type: Optional[str] = Field(default=None, description="""Type of relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    evidence_support: Optional[str] = Field(default=None, description="""Evidence supporting the relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEventRelationship']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Study(StudyEntity):
    """
    A research study or survey
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'EFO:0001444',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    study_type: Optional[StudyTypeEnum] = Field(default=None, description="""Type of study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    population: Optional[str] = Field(default=None, description="""Study population description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    enrollment_period: Optional[str] = Field(default=None, description="""Time period of enrollment""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    geographic_location: Optional[str] = Field(default=None, description="""Geographic location of study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    data_source: Optional[DataSourceEnum] = Field(default=None, description="""Source database or repository""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: Optional[str] = Field(default=None, description="""Principal investigator name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publications: Optional[list[str]] = Field(default=[], description="""Related publications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Cohort(StudyEntity):
    """
    A group of individuals in a study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    part_of_study: Optional[str] = Field(default=None, description="""Study that this cohort is part of""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    cohort_size: Optional[int] = Field(default=None, description="""Number of participants in cohort""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    inclusion_criteria: Optional[str] = Field(default=None, description="""Criteria for cohort inclusion""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Participant(StudyEntity):
    """
    An individual participant in a study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    part_of_cohort: Optional[str] = Field(default=None, description="""Cohort that this participant is part of""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant'], 'slot_uri': 'biolink:member_of'} })
    participant_id: Optional[str] = Field(default=None, description="""Participant identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    age: Optional[int] = Field(default=None, description="""Age in years""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    sex: Optional[SexEnum] = Field(default=None, description="""Biological sex""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism', 'Population']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureMeasurement(Measurement):
    """
    A measurement of exposure to a chemical or environmental factor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    measured_entity: Optional[str] = Field(default=None, description="""The entity being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[str] = Field(default=None, description="""The participant being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_value: Optional[float] = Field(default=None, description="""Numeric measurement value""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement', 'BiomarkerMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement']} })
    source_database_record: Optional[str] = Field(default=None, description="""Identifier or record reference in the source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class BiomarkerMeasurement(Measurement):
    """
    A measurement of a biological marker
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    biomarker_type: Optional[str] = Field(default=None, description="""Type of biomarker""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiomarkerMeasurement']} })
    measured_entity: Optional[str] = Field(default=None, description="""The entity being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'AggregatedMeasurement']} })
    participant: Optional[str] = Field(default=None, description="""The participant being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_value: Optional[float] = Field(default=None, description="""Numeric measurement value""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement', 'BiomarkerMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class PhenotypeMeasurement(Measurement):
    """
    A measurement of a phenotypic trait
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    phenotype: Optional[str] = Field(default=None, description="""The phenotype being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    participant: Optional[str] = Field(default=None, description="""The participant being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_value: Optional[float] = Field(default=None, description="""Numeric measurement value""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AggregatedMeasurement(Measurement):
    """
    An aggregated or summary measurement across a cohort or population
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    measured_entity: Optional[str] = Field(default=None, description="""The entity being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'AggregatedMeasurement']} })
    cohort: Optional[str] = Field(default=None, description="""The cohort for aggregated measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    summary_statistic: Optional[SummaryStatisticEnum] = Field(default=None, description="""Type of summary statistic""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    statistic_value: Optional[float] = Field(default=None, description="""Value of the summary statistic""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    sample_size: Optional[int] = Field(default=None, description="""Number of samples""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    stratification: Optional[str] = Field(default=None, description="""Stratification variables""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregatedMeasurement']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Gene(BiologicalEntity):
    """
    A gene or genetic element
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    ncbigene_id: Optional[str] = Field(default=None, description="""NCBI Gene identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    symbol: Optional[str] = Field(default=None, description="""Gene symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    in_taxon: Optional[str] = Field(default=None, description="""Taxonomic group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('ncbigene_id')
    def pattern_ncbigene_id(cls, v):
        pattern=re.compile(r"^\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ncbigene_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ncbigene_id format: {v}"
            raise ValueError(err_msg)
        return v


class Protein(BiologicalEntity):
    """
    A protein or polypeptide
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    encoded_by_gene: Optional[str] = Field(default=None, description="""Gene that encodes this protein""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Cell(BiologicalEntity):
    """
    A type of cell
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CL:0000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    cl_id: Optional[str] = Field(default=None, description="""Cell Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cell']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('cl_id')
    def pattern_cl_id(cls, v):
        pattern=re.compile(r"^CL:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cl_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cl_id format: {v}"
            raise ValueError(err_msg)
        return v


class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical structure or system, part of an organism, made of many cells
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'UBERON:0001062',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    uberon_id: Optional[str] = Field(default=None, description="""UBERON anatomical identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('uberon_id')
    def pattern_uberon_id(cls, v):
        pattern=re.compile(r"^UBERON:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid uberon_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid uberon_id format: {v}"
            raise ValueError(err_msg)
        return v


class Organism(BiologicalEntity):
    """
    An individual organism
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism', 'Population']} })
    taxon_id: Optional[str] = Field(default=None, description="""NCBI Taxonomy identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism']} })
    lifestage: Optional[str] = Field(default=None, description="""Lifestage of the organism (e.g. embryo, larva, adult)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Population(BiologicalEntity):
    """
    A group of organisms of the same species
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism', 'Population']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureToPhenotypeAssociation(ConfiguredBaseModel):
    """
    An association between an exposure and a phenotype
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema',
         'implements': ['ExposureEvent']})

    exposure: Optional[ExposureEvent] = Field(default=None, description="""Exposure in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation']} })
    phenotype: Optional[str] = Field(default=None, description="""The phenotype being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    receiver: Optional[str] = Field(default=None, description="""The organism, cell, tissue, or population being exposed in an association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation',
                       'ChemicalToGeneAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation',
                       'GeneToDiseaseAssociation']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence for association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation']} })


class ExposureToDiseaseAssociation(ConfiguredBaseModel):
    """
    An association between an exposure and a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema',
         'implements': ['ExposureEvent']})

    exposure: Optional[ExposureEvent] = Field(default=None, description="""Exposure in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation']} })
    disease: Optional[str] = Field(default=None, description="""Disease in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToDiseaseAssociation', 'GeneToDiseaseAssociation']} })
    receiver: Optional[str] = Field(default=None, description="""The organism, cell, tissue, or population being exposed in an association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation',
                       'ChemicalToGeneAssociation']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence for association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation',
                       'GeneToDiseaseAssociation']} })


class ChemicalToGeneAssociation(ConfiguredBaseModel):
    """
    An association between a chemical and a gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema',
         'implements': ['ExposureEvent']})

    chemical: Optional[str] = Field(default=None, description="""Chemical in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    gene: Optional[str] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    receiver: Optional[str] = Field(default=None, description="""The organism, cell, tissue, or population being exposed in an association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation',
                       'ChemicalToGeneAssociation']} })
    interaction_type: Optional[str] = Field(default=None, description="""Type of interaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })


class GeneToDiseaseAssociation(Association):
    """
    An association between a gene and a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    gene: Optional[str] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    disease: Optional[str] = Field(default=None, description="""Disease in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToDiseaseAssociation', 'GeneToDiseaseAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation',
                       'ExposureToDiseaseAssociation',
                       'GeneToDiseaseAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneticVariantToPhenotypeAssociation(Association):
    """
    An association between a genetic variant and a phenotype (e.g., from GWAS)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    genetic_variant: Optional[str] = Field(default=None, description="""Genetic variant identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticVariantToPhenotypeAssociation']} })
    phenotype: Optional[str] = Field(default=None, description="""The phenotype being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    p_value: Optional[float] = Field(default=None, description="""Statistical p-value""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticVariantToPhenotypeAssociation']} })
    effect_size: Optional[float] = Field(default=None, description="""Effect size of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneticVariantToPhenotypeAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposomeDatabase(ConfiguredBaseModel):
    """
    Container for all exposome data including exposures, chemicals, health outcomes, AOPs, studies, and measurements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema',
         'tree_root': True})

    chemical_entities: Optional[list[ChemicalEntity]] = Field(default=[], description="""Collection of chemical entities including compounds, drugs, and metabolites""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    exposures: Optional[list[ExposureEvent]] = Field(default=[], description="""Collection of exposure events (chemical, dietary, environmental, occupational)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    health_outcomes: Optional[list[HealthOutcome]] = Field(default=[], description="""Collection of health outcomes including phenotypes and diseases""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    adverse_outcome_pathways: Optional[list[AdverseOutcomePathway]] = Field(default=[], description="""Collection of Adverse Outcome Pathways linking exposures to health outcomes""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    studies: Optional[list[Study]] = Field(default=[], description="""Collection of research studies and surveys""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    cohorts: Optional[list[Cohort]] = Field(default=[], description="""Collection of study cohorts""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    participants: Optional[list[Participant]] = Field(default=[], description="""Collection of study participants""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    measurements: Optional[list[Measurement]] = Field(default=[], description="""Collection of measurements and observations""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    biological_entities: Optional[list[BiologicalEntity]] = Field(default=[], description="""Collection of biological entities (genes, proteins, cells, anatomical structures)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    database_records: Optional[list[str]] = Field(default=[], description="""Collection of records from external databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    associations: Optional[list[Association]] = Field(default=[], description="""Collection of associations between entities""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ExposureEvent.model_rebuild()
NamedThing.model_rebuild()
BiologicalEntity.model_rebuild()
StimulusEntity.model_rebuild()
ChemicalEntity.model_rebuild()
BehavioralEntity.model_rebuild()
DietEntity.model_rebuild()
BiologicalResponse.model_rebuild()
HealthOutcome.model_rebuild()
StudyEntity.model_rebuild()
Measurement.model_rebuild()
Association.model_rebuild()
Exposure.model_rebuild()
ActiveExposure.model_rebuild()
PassiveExposure.model_rebuild()
ChemicalExposure.model_rebuild()
DietaryExposure.model_rebuild()
OccupationalExposure.model_rebuild()
ExperimentalExposure.model_rebuild()
PrenatalExposure.model_rebuild()
BehavioralExposure.model_rebuild()
SesExposure.model_rebuild()
Phenotype.model_rebuild()
Disease.model_rebuild()
AdverseOutcome.model_rebuild()
MammalianPhenotype.model_rebuild()
ZebrafishPhenotype.model_rebuild()
HumanPhenotype.model_rebuild()
AdverseOutcomePathway.model_rebuild()
MolecularInitiatingEvent.model_rebuild()
KeyEvent.model_rebuild()
KeyEventRelationship.model_rebuild()
Study.model_rebuild()
Cohort.model_rebuild()
Participant.model_rebuild()
ExposureMeasurement.model_rebuild()
BiomarkerMeasurement.model_rebuild()
PhenotypeMeasurement.model_rebuild()
AggregatedMeasurement.model_rebuild()
Gene.model_rebuild()
Protein.model_rebuild()
Cell.model_rebuild()
AnatomicalEntity.model_rebuild()
Organism.model_rebuild()
Population.model_rebuild()
ExposureToPhenotypeAssociation.model_rebuild()
ExposureToDiseaseAssociation.model_rebuild()
ChemicalToGeneAssociation.model_rebuild()
GeneToDiseaseAssociation.model_rebuild()
GeneticVariantToPhenotypeAssociation.model_rebuild()
ExposomeDatabase.model_rebuild()
