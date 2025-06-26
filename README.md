# Lung Cancer Data Filtering from MIMIC-IV
This repository contains scripts and documentation for extracting lung cancer-related patient records from the MIMIC-IV dataset. The filtering process involves:

Selecting patients diagnosed with lung cancer using ICD-10 codes relevant to primary and secondary malignant neoplasms of the lung and trachea.

Retrieving subject IDs from diagnosis tables (diagnoses_icd.csv) that match these lung cancer ICD codes.

Filtering other related tables (e.g., admissions, labs, vitals) using the extracted subject IDs to collect comprehensive clinical data for those patients.

This preprocessed dataset can be used for downstream tasks such as cancer prognosis modeling, survival prediction, or clinical pattern analysis.

Note: MIMIC-IV access and credential setup are required to use this dataset. All preprocessing is done in compliance with the PhysioNet data usage guidelines.

