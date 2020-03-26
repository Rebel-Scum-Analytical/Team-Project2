-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: sr28
-- Source Schemata: sr28
-- Created: Fri Mar 20 00:01:03 2020
-- Workbench Version: 8.0.19
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema sr28
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `sr28` ;
CREATE SCHEMA IF NOT EXISTS `sr28` ;

-- ----------------------------------------------------------------------------
-- Table sr28.WEIGHT
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`WEIGHT` (
  `NDB_No` VARCHAR(5) NOT NULL,
  `Seq` VARCHAR(2) NOT NULL,
  `Amount` DOUBLE NULL,
  `Msre_Desc` VARCHAR(84) NULL,
  `Gm_Wgt` DOUBLE NULL,
  `Num_Data_Pts` SMALLINT(5) NULL,
  `Std_Dev` DOUBLE NULL,
  PRIMARY KEY (`NDB_No`, `Seq`),
  INDEX `Num_Data_Pts` (`Num_Data_Pts` ASC),
  CONSTRAINT `FOOD_DESWEIGHT`
    FOREIGN KEY (`NDB_No`)
    REFERENCES `sr28`.`FOOD_DES` (`NDB_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- ----------------------------------------------------------------------------
-- Table sr28.LANGDESC
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`LANGDESC` (
  `Factor` VARCHAR(6) NOT NULL,
  `Description` VARCHAR(250) NULL,
  PRIMARY KEY (`Factor`));

-- ----------------------------------------------------------------------------
-- Table sr28.FOOTNOTE
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`FOOTNOTE` (
  `NDB_No` VARCHAR(5) NULL,
  `Footnt_No` VARCHAR(4) NULL,
  `Footnot_Typ` VARCHAR(1) NULL,
  `Nutr_No` VARCHAR(3) NULL,
  `Footnot_Txt` VARCHAR(200) NULL,
  CONSTRAINT `FOOD_DESFOOTNOTE`
    FOREIGN KEY (`NDB_No`)
    REFERENCES `sr28`.`FOOD_DES` (`NDB_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- ----------------------------------------------------------------------------
-- Table sr28.ABBREV
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`ABBREV` (
  `NDB_No` VARCHAR(5) NOT NULL,
  `Shrt_Desc` VARCHAR(60) NULL,
  `Water_g` DOUBLE NULL,
  `Energ_Kcal` INT(10) NULL,
  `Protein_g` DOUBLE NULL,
  `Lipid_Tot_g` DOUBLE NULL,
  `Ash_g` DOUBLE NULL,
  `Carbohydrt_g` DOUBLE NULL,
  `Fiber_TD_g` DOUBLE NULL,
  `Sugar_Tot_g` DOUBLE NULL,
  `Calcium_mg` INT(10) NULL,
  `Iron_mg` DOUBLE NULL,
  `Magnesium_mg` DOUBLE NULL,
  `Phosphorus_mg` INT(10) NULL,
  `Potassium_mg` INT(10) NULL,
  `Sodium_g` INT(10) NULL,
  `Zinc_mg` DOUBLE NULL,
  `Copper_mg` DOUBLE NULL,
  `Manganese_mg` DOUBLE NULL,
  `Selenium_mcg` DOUBLE NULL,
  `Vit_C_mg` DOUBLE NULL,
  `Thiamin_mg` DOUBLE NULL,
  `Riboflavin_mg` DOUBLE NULL,
  `Niacin_mg` DOUBLE NULL,
  `Panto_Acid_mg` DOUBLE NULL,
  `Vit_B6_mg` DOUBLE NULL,
  `Folate_Tot_mcg` DOUBLE NULL,
  `Folic_Acid_mcg` DOUBLE NULL,
  `Food_Folate_mcg` DOUBLE NULL,
  `Folate_DFE_mcg` DOUBLE NULL,
  `Choline_Tot_mg` DOUBLE NULL,
  `Vit_B12_mcg` DOUBLE NULL,
  `Vit_A_IU` INT(10) NULL,
  `Vit_A_RAE` DOUBLE NULL,
  `Retinol_mcg` DOUBLE NULL,
  `Alpha_Carot_mcg` DOUBLE NULL,
  `Beta_Carot_mcg` DOUBLE NULL,
  `Beta_Crypt_mcg` DOUBLE NULL,
  `Lycopene_mcg` DOUBLE NULL,
  `Lut+Zea_mcg` DOUBLE NULL,
  `Vit_E_mg` DOUBLE NULL,
  `Vit_D_mcg` DOUBLE NULL,
  `Vit_D_IU` DOUBLE NULL,
  `Vit_K_mcg` DOUBLE NULL,
  `FA_Sat_g` DOUBLE NULL,
  `FA_Mono_g` DOUBLE NULL,
  `FA_Poly_g` DOUBLE NULL,
  `Cholestrl_g` INT(10) NULL,
  `GmWt_1` DOUBLE NULL,
  `GmWt_Desc1` VARCHAR(120) NULL,
  `GmWt_2` DOUBLE NULL,
  `GmWt_Desc2` VARCHAR(120) NULL,
  `Refuse_Pct` INT(10) NULL,
  PRIMARY KEY (`NDB_No`));

-- ----------------------------------------------------------------------------
-- Table sr28.DATSRCLN
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`DATSRCLN` (
  `NDB_No` VARCHAR(5) NOT NULL,
  `Nutr_No` VARCHAR(3) NOT NULL,
  `DataSrc_ID` VARCHAR(6) NOT NULL,
  INDEX `DataSrc_ID` (`DataSrc_ID` ASC),
  INDEX `DATSRCLNNDB_No` (`NDB_No` ASC),
  PRIMARY KEY (`NDB_No`, `Nutr_No`, `DataSrc_ID`),
  CONSTRAINT `NUT_DATADATSRCLN`
    FOREIGN KEY (`NDB_No` , `Nutr_No`)
    REFERENCES `sr28`.`NUT_DATA` (`NDB_No` , `Nutr_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- ----------------------------------------------------------------------------
-- Table sr28.FD_GROUP
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`FD_GROUP` (
  `FdGrp_CD` VARCHAR(4) NOT NULL,
  `FdGrp_Desc` VARCHAR(60) NULL,
  PRIMARY KEY (`FdGrp_CD`));

-- ----------------------------------------------------------------------------
-- Table sr28.NUT_DATA
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`NUT_DATA` (
  `NDB_No` VARCHAR(5) NOT NULL,
  `Nutr_No` VARCHAR(3) NOT NULL,
  `Nutr_Val` DOUBLE NULL,
  `Num_Data_Pts` INT(10) NULL,
  `Std_Error` DOUBLE NULL,
  `Src_Cd` VARCHAR(2) NULL,
  `Deriv_Cd` VARCHAR(4) NULL,
  `Ref_NDB_No` VARCHAR(5) NULL,
  `Add_Nutr_Mark` VARCHAR(1) NULL,
  `Num_Studies` SMALLINT(5) NULL,
  `Min` DOUBLE NULL,
  `Max` DOUBLE NULL,
  `DF` DOUBLE NULL,
  `Low_EB` DOUBLE NULL,
  `Up_EB` DOUBLE NULL,
  `Stat_Cmt` VARCHAR(10) NULL,
  `AddMod_Date` VARCHAR(10) NULL,
  INDEX `Num_Data_Pts` (`Num_Data_Pts` ASC),
  INDEX `Num_Studies` (`Num_Studies` ASC),
  PRIMARY KEY (`NDB_No`, `Nutr_No`),
  CONSTRAINT `NUTR_DEFNUT_DATA`
    FOREIGN KEY (`Nutr_No`)
    REFERENCES `sr28`.`NUTR_DEF` (`Nutr_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `DERIV_CDNUT_DATA`
    FOREIGN KEY (`Deriv_Cd`)
    REFERENCES `sr28`.`DERIV_CD` (`Deriv_CD`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `FOOTNOTENUT_DATA`
    FOREIGN KEY (`NDB_No`)
    REFERENCES `sr28`.`FOOTNOTE` (`NDB_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `SRC_CDNUT_DATA`
    FOREIGN KEY (`Src_Cd`)
    REFERENCES `sr28`.`SRC_CD` (`Src_Cd`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- ----------------------------------------------------------------------------
-- Table sr28.FOOD_DES
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`FOOD_DES` (
  `NDB_No` VARCHAR(5) NOT NULL,
  `FdGrp_Cd` VARCHAR(4) NULL,
  `Long_Desc` VARCHAR(200) NULL,
  `Shrt_Desc` VARCHAR(60) NULL,
  `ComName` VARCHAR(100) NULL,
  `ManufacName` VARCHAR(65) NULL,
  `Survey` VARCHAR(1) NULL,
  `Ref_Desc` VARCHAR(135) NULL,
  `Refuse` SMALLINT(5) NULL,
  `SciName` VARCHAR(65) NULL,
  `N_Factor` DOUBLE NULL,
  `Pro_Factor` DOUBLE NULL,
  `Fat_Factor` DOUBLE NULL,
  `CHO_Factor` DOUBLE NULL,
  PRIMARY KEY (`NDB_No`),
  CONSTRAINT `FD_GROUPFOOD_DES`
    FOREIGN KEY (`FdGrp_Cd`)
    REFERENCES `sr28`.`FD_GROUP` (`FdGrp_CD`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `ABBREVFOOD_DES`
    FOREIGN KEY (`NDB_No`)
    REFERENCES `sr28`.`ABBREV` (`NDB_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- ----------------------------------------------------------------------------
-- Table sr28.DERIV_CD
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`DERIV_CD` (
  `Deriv_CD` VARCHAR(4) NOT NULL,
  `Deriv_Desc` VARCHAR(120) NULL,
  PRIMARY KEY (`Deriv_CD`));

-- ----------------------------------------------------------------------------
-- Table sr28.NUTR_DEF
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`NUTR_DEF` (
  `Nutr_No` VARCHAR(3) NOT NULL,
  `Units` VARCHAR(7) NULL,
  `Tagname` VARCHAR(20) NULL,
  `NutrDesc` VARCHAR(60) NULL,
  `Num_Dec` VARCHAR(1) NULL,
  `SR_Order` DOUBLE NULL,
  PRIMARY KEY (`Nutr_No`),
  INDEX `Num_Dec` (`Num_Dec` ASC));

-- ----------------------------------------------------------------------------
-- Table sr28.DATA_SRC
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`DATA_SRC` (
  `DataSrc_ID` VARCHAR(6) NULL,
  `Authors` VARCHAR(255) NULL,
  `Title` VARCHAR(255) NULL,
  `Year` VARCHAR(4) NULL,
  `Journal` VARCHAR(135) NULL,
  `Vol_City` VARCHAR(16) NULL,
  `Issue_State` VARCHAR(5) NULL,
  `Start_Page` VARCHAR(5) NULL,
  `End_Page` VARCHAR(5) NULL,
  CONSTRAINT `DATSRCLNDATA_SRC`
    FOREIGN KEY (`DataSrc_ID`)
    REFERENCES `sr28`.`DATSRCLN` (`DataSrc_ID`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);

-- ----------------------------------------------------------------------------
-- Table sr28.SRC_CD
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`SRC_CD` (
  `Src_Cd` VARCHAR(2) NOT NULL,
  `SrcCd_Desc` VARCHAR(60) NULL,
  PRIMARY KEY (`Src_Cd`));

-- ----------------------------------------------------------------------------
-- Table sr28.LANGUAL
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `sr28`.`LANGUAL` (
  `NDB_No` VARCHAR(5) NOT NULL,
  `Factor` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`NDB_No`, `Factor`),
  CONSTRAINT `FOOD_DESLANGUAL`
    FOREIGN KEY (`NDB_No`)
    REFERENCES `sr28`.`FOOD_DES` (`NDB_No`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `{E3679419-C67B-41FC-9EA5-30E55DA9B9AA}`
    FOREIGN KEY (`Factor`)
    REFERENCES `sr28`.`LANGDESC` (`Factor`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
SET FOREIGN_KEY_CHECKS = 1;
