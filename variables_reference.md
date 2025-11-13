# NHANES 2017–2018 Variable Reference

This document provides definitions and descriptions for the variables used in the **AI-based Personalized Nutrition Analysis** project.  
All variables are sourced from publicly available NHANES 2017–2018 datasets released by the U.S. Centers for Disease Control and Prevention (CDC), National Center for Health Statistics (NCHS).

---

## 📦 General Dataset Information

**Data Source:**  
[National Health and Nutrition Examination Survey (NHANES) 2017–2018](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017)

**Files Used:**
- `DR1TOT_J.XPT` — Dietary Interview – Total Nutrient Intakes, Day 1  
- `BMX_J.XPT` — Body Measures  
- `GLU_J.XPT` — Laboratory: Fasting Glucose  
- `DEMO_J.XPT` — Demographics

**Merged Key:**  
`SEQN` — Respondent sequence number (unique participant ID)

---

## 🧩 Variables Used in the Project

| Variable Code | Dataset | Description | Units / Type |
|----------------|----------|--------------|---------------|
| **SEQN** | All | Respondent Sequence Number – unique ID for each participant | Integer |
| **RIDAGEYR** | DEMO_J | Age in years at screening | Years |
| **RIAGENDR** | DEMO_J | Gender: 1 = Male, 2 = Female | Categorical |
| **DR1TKCAL** | DR1TOT_J | Total energy intake from food (Day 1) | kcal |
| **DR1TPROT** | DR1TOT_J | Protein intake (Day 1) | grams |
| **DR1TCARB** | DR1TOT_J | Carbohydrate intake (Day 1) | grams |
| **DR1TTFAT** | DR1TOT_J | Total fat intake (Day 1) | grams |
| **DR1TSFAT** | DR1TOT_J | Saturated fat intake (Day 1) | grams |
| **DR1TMFAT** | DR1TOT_J | Monounsaturated fat intake (Day 1) | grams |
| **DR1TPFAT** | DR1TOT_J | Polyunsaturated fat intake (Day 1) | grams |
| **DR1TFIBE** | DR1TOT_J | Total dietary fiber intake (Day 1) | grams |
| **DR1TSUGR** | DR1TOT_J | Total sugar intake (Day 1) | grams |
| **BMXBMI** | BMX_J | Body Mass Index (weight/height²) | kg/m² |
| **BMXWT** | BMX_J | Weight | kg |
| **BMXHT** | BMX_J | Height | cm |
| **BMXWAIST** | BMX_J | Waist circumference | cm |
| **LBXGLU** | GLU_J | Fasting plasma glucose | mg/dL |
| **LBDGLUSI** | GLU_J | Converted fasting glucose (SI units) | mmol/L |
| **LBXIN** | INS_J | Fasting insulin (if available) | µU/mL |
| **LBDINSI** | INS_J | Converted fasting insulin (SI units) | pmol/L |
| **RIDRETH3** | DEMO_J | Race/Hispanic origin | 1–7 categorical |
| **INDFMPIR** | DEMO_J | Family income-to-poverty ratio | Ratio |
| **WTMEC2YR** | DEMO_J | Full-sample 2-year MEC exam weight | Sampling weight |

---

## 🧠 Variables Used in the Core Analysis Script

For the current project (`phase1_diet_ml.py`), the following subset is used:

| Variable | Description | Role |
|-----------|--------------|------|
| `DR1TPROT` | Protein intake (grams) | Predictor |
| `DR1TCARB` | Carbohydrate intake (grams) | Predictor |
| `DR1TTFAT` | Total fat intake (grams) | Predictor |
| `BMXBMI` | Body Mass Index (kg/m²) | Predictor |
| `LBXGLU` | Fasting plasma glucose (mg/dL) | Outcome (target) |
| `RIDAGEYR` | Age (years) | Covariate |
| `RIAGENDR` | Gender | Covariate |

---

## 🔗 References

1. Centers for Disease Control and Prevention (CDC). National Health and Nutrition Examination Survey (NHANES) Data Documentation, Codebook, and Frequencies (2017–2018).  
   [https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017)

2. NHANES Dietary Data – [DR1TOT_J Documentation (PDF)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR1TOT_J.htm)  
3. NHANES Examination Data – [BMX_J Documentation (PDF)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.htm)  
4. NHANES Laboratory Data – [GLU_J Documentation (PDF)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/GLU_J.htm)  
5. NHANES Demographics – [DEMO_J Documentation (PDF)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm)

---

## 🧾 Notes for Users

- All data used here are **publicly available** and **de-identified**, consistent with CDC usage policy.  
- When publishing or presenting analyses, always cite NHANES appropriately.  
- For weighted analysis (population-level inference), refer to CDC guidance on complex survey weights.

---

*Prepared by:* **Fawad Taj, Ph.D.**  
*Project:* *AI-Based Personalized Nutrition Analysis*  
*Date:* {{Insert current date}}
