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
                  'AQS': {'prefix_prefix': 'AQS',
                          'prefix_reference': 'https://aqs.epa.gov/api/'},
                  'CENSUS': {'prefix_prefix': 'CENSUS',
                             'prefix_reference': 'https://api.census.gov/data/'},
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
                  'GEO': {'prefix_prefix': 'GEO',
                          'prefix_reference': 'http://www.opengis.net/ont/geosparql#'},
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
                  'WGS84': {'prefix_prefix': 'WGS84',
                            'prefix_reference': 'http://www.w3.org/2003/01/geo/wgs84_pos#'},
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

class ExposureRouteEnum(str, Enum):
    """
    Routes of exposure to chemicals or environmental factors
    """
    Oral = "Oral"
    """
    Oral ingestion
    """
    Dermal = "Dermal"
    """
    Dermal contact
    """
    Inhalation = "Inhalation"
    """
    Inhalation
    """
    Injection = "Injection"
    """
    Injection
    """
    Unknown = "Unknown"
    """
    Unknown route
    """


class ExposureMediumEnum(str, Enum):
    """
    Medium through which exposure occurs
    """
    Air = "Air"
    """
    Air
    """
    Water = "Water"
    """
    Water
    """
    Food = "Food"
    """
    Food
    """
    Soil = "Soil"
    """
    Soil
    """
    Dust = "Dust"
    """
    Dust
    """
    ConsumerProduct = "ConsumerProduct"
    """
    Consumer product
    """
    Unknown = "Unknown"
    """
    Unknown medium
    """


class BiologicalOrganizationLevelEnum(str, Enum):
    """
    Levels of biological organization
    """
    Molecular = "Molecular"
    """
    Molecular level
    """
    Cellular = "Cellular"
    """
    Cellular level
    """
    Tissue = "Tissue"
    """
    Tissue level
    """
    Organ = "Organ"
    """
    Organ level
    """
    Organism = "Organism"
    """
    Organism level
    """
    Population = "Population"
    """
    Population level
    """


class StudyTypeEnum(str, Enum):
    """
    Types of research studies
    """
    Cohort = "Cohort"
    """
    Cohort study
    """
    CrossSectional = "CrossSectional"
    """
    Cross-sectional study
    """
    CaseControl = "CaseControl"
    """
    Case-control study
    """
    RandomizedControlledTrial = "RandomizedControlledTrial"
    """
    Randomized controlled trial
    """
    Survey = "Survey"
    """
    Survey
    """
    Gwas = "Gwas"
    """
    Genome-wide association study
    """
    Other = "Other"
    """
    Other study type
    """


class DataSourceEnum(str, Enum):
    """
    Data sources and repositories
    """
    Nhanes = "Nhanes"
    """
    National Health and Nutrition Examination Survey
    """
    Chear = "Chear"
    """
    Children's Health Exposure Analysis Resource
    """
    Hhear = "Hhear"
    """
    Human Health Exposure Analysis Resource
    """
    AopWiki = "AopWiki"
    """
    AOP Wiki
    """
    Ctd = "Ctd"
    """
    Comparative Toxicogenomics Database
    """
    ToxCast = "ToxCast"
    """
    ToxCast
    """
    Tox21 = "Tox21"
    """
    Tox21
    """
    ChemBl = "ChemBl"
    """
    ChEMBL
    """
    CompTox = "CompTox"
    """
    CompTox Dashboard
    """
    GwasCatalog = "GwasCatalog"
    """
    GWAS Catalog
    """
    GeneExpressionAtlas = "GeneExpressionAtlas"
    """
    Gene Expression Atlas
    """
    UsdaPesticide = "UsdaPesticide"
    """
    USDA Pesticide Data Program
    """
    Wweia = "Wweia"
    """
    What We Eat In America
    """
    Aqs = "Aqs"
    """
    EPA Air Quality System
    """
    Acs = "Acs"
    """
    American Community Survey
    """
    Other = "Other"
    """
    Other data source
    """


class SexEnum(str, Enum):
    """
    Biological sex
    """
    Male = "Male"
    """
    Male
    """
    Female = "Female"
    """
    Female
    """
    Unknown = "Unknown"
    """
    Unknown
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological samples
    """
    Blood = "Blood"
    """
    Blood sample
    """
    Urine = "Urine"
    """
    Urine sample
    """
    Serum = "Serum"
    """
    Serum sample
    """
    Plasma = "Plasma"
    """
    Plasma sample
    """
    Tissue = "Tissue"
    """
    Tissue sample
    """
    Saliva = "Saliva"
    """
    Saliva sample
    """
    Hair = "Hair"
    """
    Hair sample
    """
    Nail = "Nail"
    """
    Nail sample
    """
    Other = "Other"
    """
    Other sample type
    """


class SummaryStatisticEnum(str, Enum):
    """
    Types of summary statistics
    """
    Mean = "Mean"
    """
    Arithmetic mean
    """
    Median = "Median"
    """
    Median
    """
    Mode = "Mode"
    """
    Mode
    """
    Percentile = "Percentile"
    """
    Percentile
    """
    StandardDeviation = "StandardDeviation"
    """
    Standard deviation
    """
    Variance = "Variance"
    """
    Variance
    """
    Range = "Range"
    """
    Range
    """
    InterquartileRange = "InterquartileRange"
    """
    Interquartile range
    """


class GeographicLevelEnum(str, Enum):
    """
    Levels of geographic aggregation
    """
    Global = "Global"
    """
    Global level
    """
    Country = "Country"
    """
    Country level
    """
    State = "State"
    """
    State or province level
    """
    County = "County"
    """
    County level
    """
    City = "City"
    """
    City or municipality level
    """
    Neighborhood = "Neighborhood"
    """
    Neighborhood level
    """
    PostalCode = "PostalCode"
    """
    Postal code or ZIP code level
    """
    Custom = "Custom"
    """
    Custom geographic boundary
    """


class CensusGeographicLevelEnum(str, Enum):
    """
    US Census geographic hierarchy levels
    """
    Nation = "Nation"
    """
    National level
    """
    State = "State"
    """
    State level
    """
    County = "County"
    """
    County level
    """
    Tract = "Tract"
    """
    Census tract level
    """
    BlockGroup = "BlockGroup"
    """
    Block group level
    """
    Block = "Block"
    """
    Census block level (not available in ACS)
    """
    Place = "Place"
    """
    Incorporated place (city/town)
    """
    MetropolitanStatisticalArea = "MetropolitanStatisticalArea"
    """
    Metropolitan Statistical Area (MSA)
    """
    CongressionalDistrict = "CongressionalDistrict"
    """
    Congressional district
    """
    ZctaZipCode = "ZctaZipCode"
    """
    ZIP Code Tabulation Area (ZCTA)
    """


class TemporalResolutionEnum(str, Enum):
    """
    Temporal resolution of data
    """
    Instantaneous = "Instantaneous"
    """
    Single point in time
    """
    Hourly = "Hourly"
    """
    Hourly aggregation
    """
    Daily = "Daily"
    """
    Daily aggregation
    """
    Weekly = "Weekly"
    """
    Weekly aggregation
    """
    Monthly = "Monthly"
    """
    Monthly aggregation
    """
    Quarterly = "Quarterly"
    """
    Quarterly aggregation
    """
    Annual = "Annual"
    """
    Annual aggregation
    """
    Decadal = "Decadal"
    """
    Decadal aggregation
    """
    Custom = "Custom"
    """
    Custom temporal resolution
    """


class MonitoringSiteTypeEnum(str, Enum):
    """
    Types of environmental monitoring sites
    """
    Urban = "Urban"
    """
    Urban monitoring site
    """
    Suburban = "Suburban"
    """
    Suburban monitoring site
    """
    Rural = "Rural"
    """
    Rural monitoring site
    """
    NearRoad = "NearRoad"
    """
    Near-road monitoring site
    """
    Industrial = "Industrial"
    """
    Industrial area monitoring site
    """
    Background = "Background"
    """
    Background monitoring site
    """
    Mobile = "Mobile"
    """
    Mobile monitoring site
    """
    Other = "Other"
    """
    Other site type
    """


class ACSVariableCategoryEnum(str, Enum):
    """
    Categories of American Community Survey variables
    """
    Age = "Age"
    """
    Age and sex
    """
    Race = "Race"
    """
    Race and ethnicity
    """
    Household = "Household"
    """
    Household composition
    """
    Housing = "Housing"
    """
    Housing characteristics
    """
    Income = "Income"
    """
    Income and earnings
    """
    Employment = "Employment"
    """
    Employment and occupation
    """
    Education = "Education"
    """
    Educational attainment
    """
    Poverty = "Poverty"
    """
    Poverty status
    """
    Transportation = "Transportation"
    """
    Transportation and commuting
    """
    Health = "Health"
    """
    Health insurance coverage
    """
    Veterans = "Veterans"
    """
    Veteran status
    """
    Disability = "Disability"
    """
    Disability status
    """
    Language = "Language"
    """
    Language spoken at home
    """
    Immigration = "Immigration"
    """
    Citizenship and immigration
    """
    Ancestry = "Ancestry"
    """
    Ancestry and origin
    """
    Other = "Other"
    """
    Other variable category
    """



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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalEntity(NamedThing):
    """
    A chemical entity including compounds, drugs, and metabolites
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEBI:24431',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    chebi_id: Optional[str] = Field(default=None, description="""ChEBI identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    dtxsid: Optional[str] = Field(default=None, description="""EPA CompTox Dashboard identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    chembl_id: Optional[str] = Field(default=None, description="""ChEMBL compound identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    pubchem_cid: Optional[int] = Field(default=None, description="""PubChem Compound identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity']} })
    cas_number: Optional[str] = Field(default=None, description="""CAS Registry Number""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity', 'AirQualityParameter']} })
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


class ExposureEvent(NamedThing):
    """
    An event in which an organism is exposed to a chemical or environmental factor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
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


class HealthOutcome(NamedThing):
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


class ChemicalExposure(ExposureEvent):
    """
    Exposure to a chemical substance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000006',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class DietaryExposure(ExposureEvent):
    """
    Exposure through dietary consumption
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'FOODON:00002403',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    food_item: Optional[str] = Field(default=None, description="""Food item consumed""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryExposure']} })
    serving_size: Optional[str] = Field(default=None, description="""Serving size""", json_schema_extra = { "linkml_meta": {'domain_of': ['DietaryExposure']} })
    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class EnvironmentalExposure(ExposureEvent):
    """
    Exposure to environmental factors
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000001',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    environmental_context: Optional[str] = Field(default=None, description="""Environmental context of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnvironmentalExposure']} })
    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class OccupationalExposure(ExposureEvent):
    """
    Exposure in an occupational setting
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:0000002',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    occupation: Optional[str] = Field(default=None, description="""Occupation related to exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['OccupationalExposure']} })
    workplace: Optional[str] = Field(default=None, description="""Workplace where exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['OccupationalExposure']} })
    exposed_to_chemical: Optional[str] = Field(default=None, description="""The chemical entity involved in the exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent'], 'slot_uri': 'CHEBI:24431'} })
    exposure_route: Optional[ExposureRouteEnum] = Field(default=None, description="""Route of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_duration: Optional[str] = Field(default=None, description="""Duration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_concentration: Optional[float] = Field(default=None, description="""Concentration of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    exposure_medium: Optional[ExposureMediumEnum] = Field(default=None, description="""Medium through which exposure occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureEvent']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class Phenotype(HealthOutcome):
    """
    An observable characteristic or trait
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'HP:0000118',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    hp_id: Optional[str] = Field(default=None, description="""Human Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_category: Optional[str] = Field(default=None, description="""Category of phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
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


class Disease(HealthOutcome):
    """
    A disease or medical condition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'MONDO:0000001',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    mondo_id: Optional[str] = Field(default=None, description="""MONDO disease identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
    disease_category: Optional[str] = Field(default=None, description="""Category of disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })
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
    hp_id: Optional[str] = Field(default=None, description="""Human Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_category: Optional[str] = Field(default=None, description="""Category of phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
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


class ZebrafishPhenotype(Phenotype):
    """
    A phenotype observed in zebrafish
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ZP:0000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    zp_id: Optional[str] = Field(default=None, description="""Zebrafish Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['ZebrafishPhenotype']} })
    hp_id: Optional[str] = Field(default=None, description="""Human Phenotype Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    upheno_id: Optional[str] = Field(default=None, description="""Unified phenotype ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
    phenotype_category: Optional[str] = Field(default=None, description="""Category of phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype']} })
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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:3000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    biological_process: Optional[str] = Field(default=None, description="""Biological process involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_object: Optional[str] = Field(default=None, description="""Biological object involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_action: Optional[str] = Field(default=None, description="""Biological action or change""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""Cell type where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'CL:0000000'} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""Anatomical location where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'UBERON:0001062'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class KeyEvent(BiologicalResponse):
    """
    A measurable change in biological state that is a step in an Adverse Outcome Pathway
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ECTO:1000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    biological_process: Optional[str] = Field(default=None, description="""Biological process involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_object: Optional[str] = Field(default=None, description="""Biological object involved""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    biological_action: Optional[str] = Field(default=None, description="""Biological action or change""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent']} })
    level_of_biological_organization: Optional[BiologicalOrganizationLevelEnum] = Field(default=None, description="""Level of biological organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyEvent']} })
    occurs_in_cell_type: Optional[str] = Field(default=None, description="""Cell type where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'CL:0000000'} })
    occurs_in_anatomy: Optional[str] = Field(default=None, description="""Anatomical location where event occurs""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularInitiatingEvent', 'KeyEvent'],
         'slot_uri': 'UBERON:0001062'} })
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
    data_source: Optional[DataSourceEnum] = Field(default=None, description="""Source database or repository""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'GeolocatedDataset']} })
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
    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism']} })
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
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement', 'BiomarkerMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    sample_type: Optional[SampleTypeEnum] = Field(default=None, description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement']} })
    source_database_record: Optional[str] = Field(default=None, description="""Link to original database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement']} })
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
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_method: Optional[str] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement', 'BiomarkerMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
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
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
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


class CellType(BiologicalEntity):
    """
    A type of cell
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CL:0000000',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    cl_id: Optional[str] = Field(default=None, description="""Cell Ontology identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellType']} })
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
    An anatomical structure or system
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

    species: Optional[str] = Field(default=None, description="""Species name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant', 'Organism']} })
    taxon_id: Optional[str] = Field(default=None, description="""NCBI Taxonomy identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organism']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeoLocation(NamedThing):
    """
    A geographic location specified by coordinates and H3 hexagonal index
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'WGS84:SpatialThing',
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    latitude: Optional[float] = Field(default=None, description="""Latitude in decimal degrees (WGS84)""", ge=-90.0, le=90.0, json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation'], 'slot_uri': 'WGS84:lat'} })
    longitude: Optional[float] = Field(default=None, description="""Longitude in decimal degrees (WGS84)""", ge=-180.0, le=180.0, json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation'], 'slot_uri': 'WGS84:long'} })
    elevation: Optional[float] = Field(default=None, description="""Elevation in meters above sea level""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation']} })
    h3_index: Optional[str] = Field(default=None, description="""H3 hexagonal grid cell index (15 hexadecimal characters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation', 'H3SpatialIndex', 'AQSMonitoringSite']} })
    h3_resolution: Optional[int] = Field(default=None, description="""H3 grid resolution level (0-15, where 0 is coarsest and 15 is finest)""", ge=0, le=15, json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation', 'H3SpatialIndex']} })
    coordinate_uncertainty: Optional[float] = Field(default=None, description="""Uncertainty in coordinates (meters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('h3_index')
    def pattern_h3_index(cls, v):
        pattern=re.compile(r"^[0-9a-f]{15}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid h3_index format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid h3_index format: {v}"
            raise ValueError(err_msg)
        return v


class H3SpatialIndex(NamedThing):
    """
    An H3 hexagonal grid cell used for spatiotemporal indexing
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    h3_index: Optional[str] = Field(default=None, description="""H3 hexagonal grid cell index (15 hexadecimal characters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation', 'H3SpatialIndex', 'AQSMonitoringSite']} })
    h3_resolution: Optional[int] = Field(default=None, description="""H3 grid resolution level (0-15, where 0 is coarsest and 15 is finest)""", ge=0, le=15, json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation', 'H3SpatialIndex']} })
    center_latitude: Optional[float] = Field(default=None, description="""Latitude of H3 cell center""", json_schema_extra = { "linkml_meta": {'domain_of': ['H3SpatialIndex']} })
    center_longitude: Optional[float] = Field(default=None, description="""Longitude of H3 cell center""", json_schema_extra = { "linkml_meta": {'domain_of': ['H3SpatialIndex']} })
    parent_h3_index: Optional[str] = Field(default=None, description="""Parent H3 index at coarser resolution""", json_schema_extra = { "linkml_meta": {'domain_of': ['H3SpatialIndex']} })
    child_h3_indices: Optional[list[str]] = Field(default=[], description="""Child H3 indices at finer resolution""", json_schema_extra = { "linkml_meta": {'domain_of': ['H3SpatialIndex']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('h3_index')
    def pattern_h3_index(cls, v):
        pattern=re.compile(r"^[0-9a-f]{15}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid h3_index format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid h3_index format: {v}"
            raise ValueError(err_msg)
        return v


class GeographicEntity(NamedThing):
    """
    A geographic region or administrative area
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    geo_location: Optional[str] = Field(default=None, description="""Geographic location with coordinates""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity', 'AQSMonitoringSite']} })
    geographic_level: Optional[GeographicLevelEnum] = Field(default=None, description="""Level of geographic aggregation""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity']} })
    geographic_identifier: Optional[str] = Field(default=None, description="""Identifier for geographic entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity']} })
    boundary_polygon: Optional[str] = Field(default=None, description="""GeoJSON or WKT polygon defining geographic boundary""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CensusGeography(GeographicEntity):
    """
    Census-defined geographic areas including block groups, tracts, and counties
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    census_geographic_level: Optional[CensusGeographicLevelEnum] = Field(default=None, description="""Census geographic hierarchy level""", json_schema_extra = { "linkml_meta": {'domain_of': ['CensusGeography']} })
    geoid: Optional[str] = Field(default=None, description="""Geographic identifier used by US Census""", json_schema_extra = { "linkml_meta": {'domain_of': ['CensusGeography']} })
    state_fips: Optional[str] = Field(default=None, description="""State FIPS code (2 digits)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CensusGeography']} })
    county_fips: Optional[str] = Field(default=None, description="""County FIPS code (3 digits)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CensusGeography']} })
    tract_code: Optional[str] = Field(default=None, description="""Census tract code (6 digits)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CensusGeography']} })
    block_group_code: Optional[str] = Field(default=None, description="""Block group code (1 digit)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CensusGeography']} })
    geo_location: Optional[str] = Field(default=None, description="""Geographic location with coordinates""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity', 'AQSMonitoringSite']} })
    geographic_level: Optional[GeographicLevelEnum] = Field(default=None, description="""Level of geographic aggregation""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity']} })
    geographic_identifier: Optional[str] = Field(default=None, description="""Identifier for geographic entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity']} })
    boundary_polygon: Optional[str] = Field(default=None, description="""GeoJSON or WKT polygon defining geographic boundary""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('state_fips')
    def pattern_state_fips(cls, v):
        pattern=re.compile(r"^\d{2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid state_fips format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid state_fips format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('county_fips')
    def pattern_county_fips(cls, v):
        pattern=re.compile(r"^\d{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid county_fips format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid county_fips format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('tract_code')
    def pattern_tract_code(cls, v):
        pattern=re.compile(r"^\d{6}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid tract_code format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid tract_code format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('block_group_code')
    def pattern_block_group_code(cls, v):
        pattern=re.compile(r"^\d$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid block_group_code format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid block_group_code format: {v}"
            raise ValueError(err_msg)
        return v


class SpatiotemporalIndex(NamedThing):
    """
    A spatiotemporal index combining H3 spatial indexing with temporal information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    h3_spatial_index: Optional[str] = Field(default=None, description="""H3 spatial index reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatiotemporalIndex']} })
    time_point: Optional[datetime ] = Field(default=None, description="""Specific point in time""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatiotemporalIndex']} })
    time_range_start: Optional[datetime ] = Field(default=None, description="""Start of time range""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatiotemporalIndex']} })
    time_range_end: Optional[datetime ] = Field(default=None, description="""End of time range""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatiotemporalIndex']} })
    temporal_resolution: Optional[TemporalResolutionEnum] = Field(default=None, description="""Temporal resolution of data""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatiotemporalIndex', 'TemporalEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class TemporalEntity(NamedThing):
    """
    An entity with temporal extent
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    start_date: Optional[date] = Field(default=None, description="""Start date of temporal extent""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalEntity']} })
    end_date: Optional[date] = Field(default=None, description="""End date of temporal extent""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalEntity']} })
    temporal_resolution: Optional[TemporalResolutionEnum] = Field(default=None, description="""Temporal resolution of data""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatiotemporalIndex', 'TemporalEntity']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AQSMonitoringSite(NamedThing):
    """
    An EPA Air Quality System monitoring site
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    site_id: Optional[str] = Field(default=None, description="""AQS site identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    site_name: Optional[str] = Field(default=None, description="""Name of monitoring site""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    geo_location: Optional[str] = Field(default=None, description="""Geographic location with coordinates""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicEntity', 'AQSMonitoringSite']} })
    h3_index: Optional[str] = Field(default=None, description="""H3 hexagonal grid cell index (15 hexadecimal characters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoLocation', 'H3SpatialIndex', 'AQSMonitoringSite']} })
    site_type: Optional[MonitoringSiteTypeEnum] = Field(default=None, description="""Type of monitoring site""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    monitoring_agency: Optional[str] = Field(default=None, description="""Agency operating the monitoring site""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    establishment_date: Optional[date] = Field(default=None, description="""Date site was established""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    closure_date: Optional[date] = Field(default=None, description="""Date site was closed""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    monitor_parameters: Optional[list[str]] = Field(default=[], description="""Parameters monitored at this site""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMonitoringSite']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })

    @field_validator('h3_index')
    def pattern_h3_index(cls, v):
        pattern=re.compile(r"^[0-9a-f]{15}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid h3_index format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid h3_index format: {v}"
            raise ValueError(err_msg)
        return v


class AQSMeasurement(Measurement):
    """
    An air quality measurement from the EPA AQS monitoring network
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    monitoring_site: Optional[str] = Field(default=None, description="""Reference to monitoring site""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement']} })
    parameter_code: Optional[str] = Field(default=None, description="""Parameter code identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'AirQualityParameter']} })
    parameter_name: Optional[str] = Field(default=None, description="""Name of measured parameter""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'AirQualityParameter']} })
    measurement_value: Optional[float] = Field(default=None, description="""Numeric measurement value""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_unit: Optional[str] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_date: Optional[date] = Field(default=None, description="""Date of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureMeasurement',
                       'BiomarkerMeasurement',
                       'PhenotypeMeasurement',
                       'AQSMeasurement']} })
    measurement_time: Optional[str] = Field(default=None, description="""Time of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement']} })
    sample_duration: Optional[str] = Field(default=None, description="""Duration of sample collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement']} })
    detection_limit: Optional[float] = Field(default=None, description="""Minimum detection limit""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement']} })
    uncertainty: Optional[float] = Field(default=None, description="""Measurement uncertainty""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement']} })
    quality_indicator: Optional[str] = Field(default=None, description="""Data quality indicator""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement']} })
    spatiotemporal_index: Optional[str] = Field(default=None, description="""Combined spatial and temporal index""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'ACSEstimate', 'DemographicData']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AirQualityParameter(NamedThing):
    """
    An air quality parameter measured by monitoring networks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    parameter_code: Optional[str] = Field(default=None, description="""Parameter code identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'AirQualityParameter']} })
    parameter_name: Optional[str] = Field(default=None, description="""Name of measured parameter""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'AirQualityParameter']} })
    cas_number: Optional[str] = Field(default=None, description="""CAS Registry Number""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalEntity', 'AirQualityParameter']} })
    measurement_scale: Optional[str] = Field(default=None, description="""Scale of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['AirQualityParameter']} })
    standard_units: Optional[str] = Field(default=None, description="""Standard units for parameter""", json_schema_extra = { "linkml_meta": {'domain_of': ['AirQualityParameter']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ACSEstimate(Measurement):
    """
    A demographic or socioeconomic estimate from the American Community Survey
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    census_geography: Optional[str] = Field(default=None, description="""Census geography reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'DemographicData']} })
    variable_code: Optional[str] = Field(default=None, description="""ACS variable code""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'ACSVariable']} })
    variable_name: Optional[str] = Field(default=None, description="""Variable name in database""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'ACSVariable', 'NHANESRecord']} })
    estimate_value: Optional[float] = Field(default=None, description="""Estimated value from survey""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate']} })
    margin_of_error: Optional[float] = Field(default=None, description="""Margin of error for estimate""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate']} })
    survey_year: Optional[int] = Field(default=None, description="""Year of survey""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate']} })
    survey_period: Optional[str] = Field(default=None, description="""Survey period (1-year, 5-year)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate']} })
    spatiotemporal_index: Optional[str] = Field(default=None, description="""Combined spatial and temporal index""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'ACSEstimate', 'DemographicData']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ACSVariable(NamedThing):
    """
    A variable measured in the American Community Survey
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    variable_code: Optional[str] = Field(default=None, description="""ACS variable code""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'ACSVariable']} })
    variable_name: Optional[str] = Field(default=None, description="""Variable name in database""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'ACSVariable', 'NHANESRecord']} })
    variable_category: Optional[ACSVariableCategoryEnum] = Field(default=None, description="""Category of ACS variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSVariable']} })
    universe: Optional[str] = Field(default=None, description="""Universe or population for variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSVariable']} })
    data_type: Optional[str] = Field(default=None, description="""Data type of variable""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSVariable']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class DemographicData(NamedThing):
    """
    Demographic information for a geographic area
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    census_geography: Optional[str] = Field(default=None, description="""Census geography reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'DemographicData']} })
    total_population: Optional[int] = Field(default=None, description="""Total population count""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemographicData']} })
    population_density: Optional[float] = Field(default=None, description="""Population per square kilometer""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemographicData']} })
    median_age: Optional[float] = Field(default=None, description="""Median age in years""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemographicData']} })
    median_household_income: Optional[float] = Field(default=None, description="""Median household income in USD""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemographicData']} })
    spatiotemporal_index: Optional[str] = Field(default=None, description="""Combined spatial and temporal index""", json_schema_extra = { "linkml_meta": {'domain_of': ['AQSMeasurement', 'ACSEstimate', 'DemographicData']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeolocatedDataset(NamedThing):
    """
    A dataset with geographic and temporal indexing using H3
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    dataset_name: Optional[str] = Field(default=None, description="""Name of geolocated dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeolocatedDataset']} })
    dataset_type: Optional[str] = Field(default=None, description="""Type of dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeolocatedDataset']} })
    coverage_area: Optional[str] = Field(default=None, description="""Geographic coverage area description""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeolocatedDataset']} })
    temporal_coverage_start: Optional[date] = Field(default=None, description="""Start of temporal coverage""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeolocatedDataset']} })
    temporal_coverage_end: Optional[date] = Field(default=None, description="""End of temporal coverage""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeolocatedDataset']} })
    h3_resolution_levels: Optional[list[int]] = Field(default=[], description="""H3 resolution levels used in dataset""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeolocatedDataset']} })
    data_source: Optional[DataSourceEnum] = Field(default=None, description="""Source database or repository""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'GeolocatedDataset']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class DatabaseRecord(NamedThing):
    """
    A record from an external database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class NHANESRecord(DatabaseRecord):
    """
    A record from the National Health and Nutrition Examination Survey
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    survey_cycle: Optional[str] = Field(default=None, description="""NHANES survey cycle""", json_schema_extra = { "linkml_meta": {'domain_of': ['NHANESRecord']} })
    variable_name: Optional[str] = Field(default=None, description="""Variable name in database""", json_schema_extra = { "linkml_meta": {'domain_of': ['ACSEstimate', 'ACSVariable', 'NHANESRecord']} })
    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CTDRecord(DatabaseRecord):
    """
    A record from the Comparative Toxicogenomics Database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChEMBLRecord(DatabaseRecord):
    """
    A record from ChEMBL chemical database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GWASRecord(DatabaseRecord):
    """
    A record from the GWAS Catalog
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class AOPWikiRecord(DatabaseRecord):
    """
    A record from the AOP Wiki
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ToxCastRecord(DatabaseRecord):
    """
    A record from the ToxCast database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class CompToxRecord(DatabaseRecord):
    """
    A record from the EPA CompTox Chemicals Dashboard
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneExpressionAtlasRecord(DatabaseRecord):
    """
    A record from the Gene Expression Atlas
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class USDARecord(DatabaseRecord):
    """
    A record from USDA Pesticide Data Program
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    source_database: Optional[str] = Field(default=None, description="""Name of source database""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    record_url: Optional[str] = Field(default=None, description="""URL to database record""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    last_updated: Optional[date] = Field(default=None, description="""Date record was last updated""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseRecord']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ExposureToPhenotypeAssociation(Association):
    """
    An association between an exposure and a phenotype
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    exposure: Optional[str] = Field(default=None, description="""Exposure in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation']} })
    phenotype: Optional[str] = Field(default=None, description="""The phenotype being measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeMeasurement',
                       'ExposureToPhenotypeAssociation',
                       'GeneticVariantToPhenotypeAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation', 'GeneToDiseaseAssociation']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence for association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class ChemicalToGeneAssociation(Association):
    """
    An association between a chemical and a gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    chemical: Optional[str] = Field(default=None, description="""Chemical in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    gene: Optional[str] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    interaction_type: Optional[str] = Field(default=None, description="""Type of interaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    category: Optional[list[str]] = Field(default=[], description="""A category or type for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })
    xref: Optional[list[str]] = Field(default=[], description="""External database cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing']} })


class GeneToDiseaseAssociation(Association):
    """
    An association between a gene and a disease
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/diatomsRcool/exposome-schema'})

    gene: Optional[str] = Field(default=None, description="""Gene in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChemicalToGeneAssociation', 'GeneToDiseaseAssociation']} })
    disease: Optional[str] = Field(default=None, description="""Disease in association""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneToDiseaseAssociation']} })
    association_type: Optional[str] = Field(default=None, description="""Type of association""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureToPhenotypeAssociation', 'GeneToDiseaseAssociation']} })
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
    database_records: Optional[list[DatabaseRecord]] = Field(default=[], description="""Collection of records from external databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    associations: Optional[list[Association]] = Field(default=[], description="""Collection of associations between entities""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    geo_locations: Optional[list[GeoLocation]] = Field(default=[], description="""Collection of geographic locations with H3 indexing""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    h3_spatial_indices: Optional[list[H3SpatialIndex]] = Field(default=[], description="""Collection of H3 hexagonal grid cells""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    geographic_entities: Optional[list[GeographicEntity]] = Field(default=[], description="""Collection of geographic regions and administrative areas""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    spatiotemporal_indices: Optional[list[SpatiotemporalIndex]] = Field(default=[], description="""Collection of spatiotemporal indices combining H3 with temporal data""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    aqs_monitoring_sites: Optional[list[AQSMonitoringSite]] = Field(default=[], description="""Collection of EPA AQS air quality monitoring sites""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    aqs_measurements: Optional[list[AQSMeasurement]] = Field(default=[], description="""Collection of air quality measurements from EPA AQS""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    acs_estimates: Optional[list[ACSEstimate]] = Field(default=[], description="""Collection of American Community Survey demographic estimates""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    demographic_data: Optional[list[DemographicData]] = Field(default=[], description="""Collection of demographic data for geographic areas""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })
    geolocated_datasets: Optional[list[GeolocatedDataset]] = Field(default=[], description="""Collection of geolocated datasets with H3 indexing""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposomeDatabase']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
BiologicalEntity.model_rebuild()
ChemicalEntity.model_rebuild()
ExposureEvent.model_rebuild()
BiologicalResponse.model_rebuild()
HealthOutcome.model_rebuild()
StudyEntity.model_rebuild()
Measurement.model_rebuild()
Association.model_rebuild()
ChemicalExposure.model_rebuild()
DietaryExposure.model_rebuild()
EnvironmentalExposure.model_rebuild()
OccupationalExposure.model_rebuild()
Phenotype.model_rebuild()
Disease.model_rebuild()
AdverseOutcome.model_rebuild()
MammalianPhenotype.model_rebuild()
ZebrafishPhenotype.model_rebuild()
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
CellType.model_rebuild()
AnatomicalEntity.model_rebuild()
Organism.model_rebuild()
GeoLocation.model_rebuild()
H3SpatialIndex.model_rebuild()
GeographicEntity.model_rebuild()
CensusGeography.model_rebuild()
SpatiotemporalIndex.model_rebuild()
TemporalEntity.model_rebuild()
AQSMonitoringSite.model_rebuild()
AQSMeasurement.model_rebuild()
AirQualityParameter.model_rebuild()
ACSEstimate.model_rebuild()
ACSVariable.model_rebuild()
DemographicData.model_rebuild()
GeolocatedDataset.model_rebuild()
DatabaseRecord.model_rebuild()
NHANESRecord.model_rebuild()
CTDRecord.model_rebuild()
ChEMBLRecord.model_rebuild()
GWASRecord.model_rebuild()
AOPWikiRecord.model_rebuild()
ToxCastRecord.model_rebuild()
CompToxRecord.model_rebuild()
GeneExpressionAtlasRecord.model_rebuild()
USDARecord.model_rebuild()
ExposureToPhenotypeAssociation.model_rebuild()
ChemicalToGeneAssociation.model_rebuild()
GeneToDiseaseAssociation.model_rebuild()
GeneticVariantToPhenotypeAssociation.model_rebuild()
ExposomeDatabase.model_rebuild()
