##################################
##                              ##
##  MCPS Pipeline               ##
##  Joshua Mausolf              ##
##  Bridgit Donnelly            ##
##  Christine Cook              ##
##                              ##
##################################

import pandas as pd
import numpy as np
import pipeline as ml


def summarize_data(dataset):

    ###############
    ## LOAD DATA ##
    ###############

    print "Loading data..."

    df = ml.read_data(dataset)
    variables = list(df.columns.values)
    #print variables

    ####################################
    ## RUN INITIAL SUMMARY STATISTICS ##
    ####################################
    print "Running summary statistics..."

    ml.summarize_dataset(dataset)
    for v in variables:
        ml.summary_statistics(v, dataset, 5, 10)

    return df

def clean_data(df, cohort):

    print "Cleaning data..."

    ################################
    ## DROP UNNECESSARY VARIABLES ##
    ################################

    print "Dropping unnecessary variables..."

    if cohort == 'cohort1':
        print "for cohort 1..."
        variables_to_drop = ['g6_tardyr','g6_school_name', 'g7_school_name', 'g8_school_name', 'g9_school_name', 'g10_school_name', 'g11_school_name', 'g12_school_name','g6_year', 'g6_gradeexp', 'g6_grade', 'g6_wcode', 'g7_year', 'g7_gradeexp', 'g7_grade', 'g7_wcode', 'g8_year', 'g8_gradeexp', 'g8_grade', 'g8_wcode', 'g9_year', 'g9_gradeexp', 'g9_grade', 'g9_wcode', 'g10_year', 'g10_gradeexp', 'g10_grade', 'g10_wcode', 'g11_year', 'g11_gradeexp', 'g11_grade', 'g11_wcode', 'g12_year', 'g12_gradeexp', 'g12_grade', 'g12_wcode']
        for v in variables_to_drop:
            df.drop(v, axis=1, inplace=True)

    elif cohort == 'cohort2':
        print "for cohort 2..."
        variables_to_drop = ['g6_tardyr','g6_school_name', 'g7_school_name', 'g8_school_name', 'g9_school_name', 'g10_school_name', 'g11_school_name', 'g12_school_name','g6_year', 'g6_grade', 'g6_wcode', 'g7_year', 'g7_grade', 'g7_wcode', 'g8_year', 'g8_grade', 'g8_wcode', 'g9_year', 'g9_grade', 'g9_wcode', 'g10_year', 'g10_grade', 'g10_wcode', 'g11_year', 'g11_grade', 'g11_wcode', 'g12_year', 'g12_grade', 'g12_wcode']
        for v in variables_to_drop:
            df.drop(v, axis=1, inplace=True)

    else:
        pass

    #######################
    ## COMBINE VARIABLES ##
    #######################

    ## Create single column for birth year
    print "Correcting birthdays..."

    df['birthday'] = df['g11_byrmm']
    birthday_cols = ['g12_byrmm', 'g11_byrmm', 'g10_byrmm', 'g9_byrmm', 'g8_byrmm', 'g7_byrmm', 'g6_byrmm']
    for c in birthday_cols:
        ml.replace_with_other_col(df, 'birthday', c)
        df.drop(c, axis=1, inplace=True)
    #print ml.summarize(df['birthday'])

    ## Create single column for gender
    print "Correcting gender..."

    df['gender'] = df['g11_gender']
    gender_cols = ['g12_gender', 'g11_gender', 'g10_gender', 'g9_gender', 'g8_gender', 'g7_gender', 'g6_gender']
    for c in gender_cols:
        ml.replace_with_other_col(df, 'gender', c)
        df.drop(c, axis=1, inplace=True)
    #print df['gender'].value_counts()


    ################
    ## CLEAN DATA ##
    ################

    print "Cleaning data..."
    retained_cols = ['g11_retained', 'g12_retained', 'g9_newmcps', 'g10_newmcps', 'g11_newmcps', 'g12_newmcps', 'g9_newus', 'g10_newus', 'g11_newus', 'g12_newus']
    for col in retained_cols:
        for index, row in df.iterrows():
            if pd.isnull(row[col]):
                df.ix[index, col] = 0
            else:
                df.ix[index, col] = 1
        df[col] = df[col].astype(int)


    ###############################
    ## CREATE MISSING DATA FLAGS ##
    ###############################

    print "Creating missing data flags..."

    ## Create flag if a given student is missing a year's worth of data
    grade_id = ['g6_pid', 'g7_pid', 'g8_pid', 'g9_pid', 'g10_pid', 'g11_pid', 'g12_pid']
    year = 6
    for g in grade_id:
        col_name = 'g' + str(year) + '_missing'
        for index, row in df.iterrows():
            if pd.isnull(row[g]):
                df.ix[index, col_name] = 1
            else:
                df.ix[index, col_name] = 0
        df.drop(g, axis=1, inplace=True)
        year+=1


    ml.print_to_csv(df, 'data/predummy_data.csv')
    #ml.print_to_csv(df, '/mnt/data2/education_data/mcps/DATA_DO_NOT_UPLOAD/predummy_data.csv')


def deal_with_dummies(dataset):
    
    df = ml.read_data(dataset)

    ###################################
    ## CREATE DUMMY VARIABLE COLUMNS ##
    ###################################
    print "Creating dummy variables..."

    string_cols = list(df.select_dtypes(include=['object']))
    print string_cols

    df = ml.get_dummys(df, string_cols, dummy_na=True)
    for col in string_cols:
        print col
        df.drop(col, axis=1, inplace=True)

    ## Save clean version
    ml.print_to_csv(df, 'data/clean_data.csv')
    #ml.print_to_csv(df, '/mnt/data2/education_data/mcps/DATA_DO_NOT_UPLOAD/clean_data.csv')


def impute_data(dataset, cohort):

    df = ml.read_data(dataset)

    ##########################
    ## IMPUTE ACADEMIC DATA ##
    ##########################

    print "Impute missing academic information..."

    ## Fill missing school data -- use mean imputation for now
    school_vars = ['g6_school_id', 'g7_school_id', 'g8_school_id', 'g9_school_id', 'g10_school_id', 'g11_school_id', 'g12_school_id']
    ml.replace_with_mean(df, school_vars)

    ## Fill missing grade and test score information -- use mean imputation for now
    grades_tests = ['g6_q1mpa', 'g6_q2mpa', 'g6_q3mpa', 'g6_q4mpa', 'g6_g6mapr','g7_q1mpa', 'g7_q2mpa', 'g7_q3mpa', 'g7_q4mpa', 'g7_g7mapr', 'g8_q1mpa', 'g8_q2mpa', 'g8_q3mpa', 'g8_q4mpa', 'g8_g8mapr', 'g9_q1mpa', 'g9_q2mpa', 'g9_q3mpa', 'g9_q4mpa', 'g9_g8mapr', 'g10_q1mpa', 'g10_q2mpa', 'g10_q3mpa', 'g10_q4mpa', 'g10_psatv', 'g10_psatm', 'g11_q1mpa', 'g11_q2mpa', 'g11_q3mpa', 'g11_q4mpa', 'g11_psatv', 'g11_psatm', 'g12_q1mpa', 'g12_q2mpa', 'g12_q3mpa', 'g12_q4mpa', 'g12_psatv', 'g12_psatm']
    ml.replace_with_mean(df, grades_tests)

    ## Fill in missing id with dummy
    ml.replace_with_value(df, 'id', 0)

    ## Fill missing MSAM data
    g6_msam = ['g6_g6msam_Advanced','g6_g6msam_Basic','g6_g6msam_Proficient']
    ml.replace_dummy_null_mean(df, 'g6_g6msam_nan', g6_msam)

    if cohort == 'cohort1':
        g7_msam = ['g7_g7msam_Advanced','g7_g7msam_Basic','g7_g7msam_Proficient']
        ml.replace_dummy_null_mean(df, 'g7_g7msam_nan', g7_msam)
    elif cohort == 'cohort2':
        g7_msam = ['g7_g7msam_ ','g7_g7msam_1','g7_g7msam_2', 'g7_g7msam_3']
        ml.replace_dummy_null_mean(df, 'g7_g7msam_nan', g7_msam)

    g8_msam = ['g8_g8msam_Advanced','g8_g8msam_Basic','g8_g8msam_Proficient']
    ml.replace_dummy_null_mean(df, 'g8_g8msam_nan', g8_msam)

    g9_msam = ['g9_g8msam_Advanced','g9_g8msam_Basic','g9_g8msam_Proficient']
    ml.replace_dummy_null_mean(df,'g9_g8msam_nan', g9_msam)

    
    ############################
    ## IMPUTE BEHAVIORAL DATA ##
    ############################

    print "Impute missing behavioral data..."

    ## Fill missing behavioral data -- use mean imputation for now
    behavioral_cols = ['g6_absrate', 'g6_nsusp','g7_absrate', 'g7_tardyr', 'g7_nsusp', 'g8_absrate', 'g8_tardyr', 'g8_nsusp', 'g9_absrate', 'g9_nsusp', 'g10_absrate', 'g10_nsusp', 'g11_absrate', 'g11_nsusp','g12_absrate', 'g12_nsusp']
    ml.replace_with_mean(df, behavioral_cols)

    ## Fill in missing birthday data
    #ml.replace_with_mean(df, 'birthday')

    ############################
    ## IMPUTE ENROLLMENT DATA ##
    ############################

    print "Imputing missing enrollment data..."

    ## Fill missing enrollment data
    print "Fixing mobility columns..."
    mobility_cols = ['g10_retained', 'g6_mobility', 'g7_mobility', 'g8_mobility', 'g9_mobility', 'g9_retained','g10_mobility', 'g11_mobility', 'g12_mobility', 'birthday']
    # Includes g10_retained because it's coded as 0/1 already
    ml.replace_with_mean(df, mobility_cols)


    #########################
    ## IMPUTE DROPOUT DATA ##
    #########################

    print "Impute missing droput information..."

    ## Fill missing dropout information with 0
    dropout_vars = ['g6_dropout', 'g7_dropout', 'g8_dropout', 'g9_dropout', 'g10_dropout', 'g11_dropout', 'g12_dropout', 'dropout']
    ml.replace_with_value(df, dropout_vars, [0,0,0,0,0,0,0,0])

    #variables = list(df.columns.values)
    #print variables



    ############################
    # IMPUTE NEIGHBORHOOD DATA #
    ############################

    print "Imputing missing school neighborhood data..."

    ## Fill missing school neighborhood data
    print "Fixing neighborhood columns..."
    """
    neighborhood_cols = ['suspensionrate',  'mobilityrateentrantswithdra',  'attendancerate',   'avg_class_size',   'studentinstructionalstaffratio',   'dropoutrate',  'grade12documenteddecisionco',  'grade12documenteddecisionem',  'grade12documenteddecisionmi',  'grad12docdec_col_emp', 'graduationrate',   'studentsmeetinguniversitysyste',   'Est_Households_2012',  'Est_Population_2012',  'Med_Household_Income_2012',    'Mean_Household_Income_2012',   'Pop_Below_Poverty_2012',   'Percent_Below_Poverty_2012',   'Pop_Under18_2012', 'Under18_Below_Poverty_2012',   'Under18_Below_Poverty_Percent_2012',   'Housholds_on_Food_stamps_with_Children_Under18_2012',  'Housholds_Pop_on_Food_Stamps_2012',    'Pop_BlackAA_2012', 'Pop_White_2012',   'Bt_18_24_percent_less_than_High_School_2012',  'Bt_18_24_percent_High_School_2012',    'Bt_18_24_percent_Some_College_or_AA_2012', 'Bt_1824_percent_BA_or_Higher_2012',    'Over_25_percent_less_than_9th_grade_2012', 'Over_25_percent_9th_12th_2012',    'Over_25_percent_High_School_2012', 'Over_25__percent_Some_College_No_Deg_2012',    'Over_25_percent_AA_2012',  'Over_25_percent_Bachelors_2012',   'Over_25_percent_Graduate_or_Professionals_2012']
    """

    neighborhood_cols = ['g9_suspensionrate', 'g10_suspensionrate', 'g11_suspensionrate', 'g12_suspensionrate', 'g9_mobilityrateentrantswithdra', 'g10_mobilityrateentrantswithdra', 'g11_mobilityrateentrantswithdra', 'g12_mobilityrateentrantswithdra', 'g9_attendancerate', 'g10_attendancerate', 'g11_attendancerate', 'g12_attendancerate','g9_avg_class_size', 'g10_avg_class_size', 'g11_avg_class_size', 'g12_avg_class_size','g9_studentinstructionalstaffratio', 'g10_studentinstructionalstaffratio', 'g11_studentinstructionalstaffratio', 'g12_studentinstructionalstaffratio','g9_dropoutrate', 'g10_dropoutrate', 'g11_dropoutrate', 'g12_dropoutrate', 'g9_grade12documenteddecisionco', 'g10_grade12documenteddecisionco', 'g11_grade12documenteddecisionco', 'g12_grade12documenteddecisionco','g9_grade12documenteddecisionem', 'g10_grade12documenteddecisionem', 'g11_grade12documenteddecisionem', 'g12_grade12documenteddecisionem','g9_grade12documenteddecisionmi', 'g10_grade12documenteddecisionmi', 'g11_grade12documenteddecisionmi', 'g12_grade12documenteddecisionmi', 'g9_grad12docdec_col_emp', 'g10_grad12docdec_col_emp', 'g11_grad12docdec_col_emp', 'g12_grad12docdec_col_emp', 'g9_graduationrate', 'g10_graduationrate', 'g11_graduationrate', 'g12_graduationrate','g9_studentsmeetinguniversitysyste', 'g10_studentsmeetinguniversitysyste', 'g11_studentsmeetinguniversitysyste', 'g12_studentsmeetinguniversitysyste', 'g9_Est_Households_2012', 'g10_Est_Households_2012', 'g11_Est_Households_2012', 'g12_Est_Households_2012','g9_Est_Population_2012', 'g10_Est_Population_2012', 'g11_Est_Population_2012', 'g12_Est_Population_2012', 'g9_Med_Household_Income_2012', 'g10_Med_Household_Income_2012', 'g11_Med_Household_Income_2012', 'g12_Med_Household_Income_2012', 'g9_Mean_Household_Income_2012', 'g10_Mean_Household_Income_2012', 'g11_Mean_Household_Income_2012', 'g12_Mean_Household_Income_2012', 'g9_Pop_Below_Poverty_2012', 'g10_Pop_Below_Poverty_2012', 'g11_Pop_Below_Poverty_2012', 'g12_Pop_Below_Poverty_2012', 'g9_Percent_Below_Poverty_2012', 'g10_Percent_Below_Poverty_2012', 'g11_Percent_Below_Poverty_2012', 'g12_Percent_Below_Poverty_2012', 'g9_Pop_Under18_2012', 'g10_Pop_Under18_2012', 'g11_Pop_Under18_2012', 'g12_Pop_Under18_2012', 'g9_Under18_Below_Poverty_2012', 'g10_Under18_Below_Poverty_2012', 'g11_Under18_Below_Poverty_2012', 'g12_Under18_Below_Poverty_2012', 'g9_Under18_Below_Poverty_Percent_2012', 'g10_Under18_Below_Poverty_Percent_2012', 'g11_Under18_Below_Poverty_Percent_2012', 'g12_Under18_Below_Poverty_Percent_2012', 'g9_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g10_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g11_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g12_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g9_Housholds_Pop_on_Food_Stamps_2012', 'g10_Housholds_Pop_on_Food_Stamps_2012', 'g11_Housholds_Pop_on_Food_Stamps_2012', 'g12_Housholds_Pop_on_Food_Stamps_2012', 'g9_Pop_BlackAA_2012', 'g10_Pop_BlackAA_2012', 'g11_Pop_BlackAA_2012', 'g12_Pop_BlackAA_2012', 'g9_Pop_White_2012', 'g10_Pop_White_2012', 'g11_Pop_White_2012', 'g12_Pop_White_2012', 'g9_Bt_18_24_percent_less_than_High_School_2012', 'g10_Bt_18_24_percent_less_than_High_School_2012', 'g11_Bt_18_24_percent_less_than_High_School_2012', 'g12_Bt_18_24_percent_less_than_High_School_2012', 'g9_Bt_18_24_percent_High_School_2012', 'g10_Bt_18_24_percent_High_School_2012', 'g11_Bt_18_24_percent_High_School_2012', 'g12_Bt_18_24_percent_High_School_2012', 'g9_Bt_18_24_percent_Some_College_or_AA_2012', 'g10_Bt_18_24_percent_Some_College_or_AA_2012', 'g11_Bt_18_24_percent_Some_College_or_AA_2012', 'g12_Bt_18_24_percent_Some_College_or_AA_2012', 'g9_Bt_1824_percent_BA_or_Higher_2012', 'g10_Bt_1824_percent_BA_or_Higher_2012', 'g11_Bt_1824_percent_BA_or_Higher_2012', 'g12_Bt_1824_percent_BA_or_Higher_2012', 'g9_Over_25_percent_less_than_9th_grade_2012', 'g10_Over_25_percent_less_than_9th_grade_2012', 'g11_Over_25_percent_less_than_9th_grade_2012', 'g12_Over_25_percent_less_than_9th_grade_2012', 'g9_Over_25_percent_9th_12th_2012', 'g10_Over_25_percent_9th_12th_2012', 'g11_Over_25_percent_9th_12th_2012', 'g12_Over_25_percent_9th_12th_2012', 'g9_Over_25_percent_High_School_2012', 'g10_Over_25_percent_High_School_2012', 'g11_Over_25_percent_High_School_2012', 'g12_Over_25_percent_High_School_2012', 'g9_Over_25__percent_Some_College_No_Deg_2012', 'g10_Over_25__percent_Some_College_No_Deg_2012', 'g11_Over_25__percent_Some_College_No_Deg_2012', 'g12_Over_25__percent_Some_College_No_Deg_2012', 'g9_Over_25_percent_AA_2012', 'g10_Over_25_percent_AA_2012', 'g11_Over_25_percent_AA_2012', 'g12_Over_25_percent_AA_2012', 'g9_Over_25_percent_Bachelors_2012', 'g10_Over_25_percent_Bachelors_2012', 'g11_Over_25_percent_Bachelors_2012', 'g12_Over_25_percent_Bachelors_2012', 'g9_Over_25_percent_Graduate_or_Professionals_2012', 'g10_Over_25_percent_Graduate_or_Professionals_2012', 'g11_Over_25_percent_Graduate_or_Professionals_2012', 'g12_Over_25_percent_Graduate_or_Professionals_2012']
    ml.replace_with_mean(df, neighborhood_cols)


    summary = ml.summarize(df)
    print summary.T
    #ml.print_to_csv(summary.T, 'updated_summary_stats_vertical.csv')

    ml.print_to_csv(df, 'data/imputed_data.csv')
    #ml.print_to_csv(df, '/mnt/data2/education_data/mcps/DATA_DO_NOT_UPLOAD/imputed_data.csv')
    print "Done!"

#-------------------------------------------------------

if __name__ == '__main__':

    dataset = "data/cohort1_all_school.csv"
    #dataset = "data/cohort2_all_school.csv"
    #dataset = "/mnt/data2/education_data/mcps/DATA_DO_NOT_UPLOAD/cohort1_all_school.csv"

    #df = summarize_data(dataset)
    df = ml.read_data(dataset)
    #clean_data(df, 'cohort1')
    #clean_data(df, 'cohort2')

    #non_dummy_data = 'data/predummy_data.csv'
    #non_dummy_data = '/mnt/data2/education_data/mcps/DATA_DO_NOT_UPLOAD/predummy_data.csv'
    #deal_with_dummies(non_dummy_data)

    clean_dataset = 'data/clean_data.csv'
    #clean_dataset = '/mnt/data2/education_data/mcps/DATA_DO_NOT_UPLOAD/clean_data.csv'
    impute_data(clean_dataset, 'cohort1')
    #impute_data(clean_dataset, 'cohort2')
