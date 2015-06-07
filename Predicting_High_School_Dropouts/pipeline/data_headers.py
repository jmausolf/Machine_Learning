
varlist = ['suspensionrate',
'mobilityrateentrantswithdra',
'attendancerate',
'avg_class_size',
'studentinstructionalstaffratio',
'dropoutrate',
'grade12documenteddecisionco',
'grade12documenteddecisionem',
'grade12documenteddecisionmi',
'grad12docdec_col_emp',
'graduationrate',
'studentsmeetinguniversitysyste',
'Est_Households_2012',
'Est_Population_2012',
'Med_Household_Income_2012',
'Mean_Household_Income_2012',
'Pop_Below_Poverty_2012',
'Percent_Below_Poverty_2012',
'Pop_Under18_2012',
'Under18_Below_Poverty_2012',
'Under18_Below_Poverty_Percent_2012',
'Housholds_on_Food_stamps_with_Children_Under18_2012',
'Housholds_Pop_on_Food_Stamps_2012',
'Pop_BlackAA_2012',
'Pop_White_2012',
'Bt_18_24_percent_less_than_High_School_2012',
'Bt_18_24_percent_High_School_2012',
'Bt_18_24_percent_Some_College_or_AA_2012',
'Bt_1824_percent_BA_or_Higher_2012',
'Over_25_percent_less_than_9th_grade_2012',
'Over_25_percent_9th_12th_2012',
'Over_25_percent_High_School_2012',
'Over_25__percent_Some_College_No_Deg_2012',
'Over_25_percent_AA_2012',
'Over_25_percent_Bachelors_2012',
'Over_25_percent_Graduate_or_Professionals_2012']

for var in varlist:
	g6var = "g6_"+var
	g7var = "g7_"+var
	g8var = "g8_"+var
	g9var = "g9_"+var
	g10var = "g10_"+var
	g11var = "g11_"+var
	g12var = "g12_"+var

	#print g6var
	#print g7var
	#print g8var
	#print g9var
	#print g10var
	#print g11var
	#print g12var 

	#print "'"+g6var+"'"+","
	#print "'"+g7var+"'"+","
	#print "'"+g8var+"'"+","
	#print "'"+g9var+"'"+","
	#print "'"+g10var+"'"+","
	#print "'"+g11var+"'"+","
	#print "'"+g12var+"'"+","

	#print "'"+g6var+"'"+",", "'"+g7var+"'"+",",	"'"+g8var+"'"+",", "'"+g9var+"'"+",", "'"+g10var+"'"+",", "'"+g11var+"'"+",", "'"+g12var+"'"+","
	print "'"+g9var+"'"+",", "'"+g10var+"'"+",", "'"+g11var+"'"+",", "'"+g12var+"'"+","


	#print g7var
	#print g8var
	#print g9var
	#print g10var
	#print g11var
	#print g12var 


"""

g6_suspensionrate
g6_mobilityrateentrantswithdra
g6_attendancerate
g6_avg_class_size
g6_studentinstructionalstaffratio
g6_dropoutrate
g6_grade12documenteddecisionco
g6_grade12documenteddecisionem
g6_grade12documenteddecisionmi
g6_grad12docdec_col_emp
g6_graduationrate
g6_studentsmeetinguniversitysyste
g6_Est_Households_2012
g6_Est_Population_2012
g6_Med_Household_Income_2012
g6_Mean_Household_Income_2012
g6_Pop_Below_Poverty_2012
g6_Percent_Below_Poverty_2012
g6_Pop_Under18_2012
g6_Under18_Below_Poverty_2012
g6_Under18_Below_Poverty_Percent_2012
g6_Housholds_on_Food_stamps_with_Children_Under18_2012
g6_Housholds_Pop_on_Food_Stamps_2012
g6_Pop_BlackAA_2012
g6_Pop_White_2012
g6_Bt_18_24_percent_less_than_High_School_2012
g6_Bt_18_24_percent_High_School_2012
g6_Bt_18_24_percent_Some_College_or_AA_2012
g6_Bt_1824_percent_BA_or_Higher_2012
g6_Over_25_percent_less_than_9th_grade_2012
g6_Over_25_percent_9th_12th_2012
g6_Over_25_percent_High_School_2012
g6_Over_25__percent_Some_College_No_Deg_2012
g6_Over_25_percent_AA_2012
g6_Over_25_percent_Bachelors_2012
g6_Over_25_percent_Graduate_or_Professionals_2012
g6_school_id

g7_suspensionrate
g7_mobilityrateentrantswithdra
g7_attendancerate
g7_avg_class_size
g7_studentinstructionalstaffratio
g7_dropoutrate
g7_grade12documenteddecisionco
g7_grade12documenteddecisionem
g7_grade12documenteddecisionmi
g7_grad12docdec_col_emp
g7_graduationrate
g7_studentsmeetinguniversitysyste
g7_Est_Households_2012
g7_Est_Population_2012
g7_Med_Household_Income_2012
g7_Mean_Household_Income_2012
g7_Pop_Below_Poverty_2012
g7_Percent_Below_Poverty_2012
g7_Pop_Under18_2012
g7_Under18_Below_Poverty_2012
g7_Under18_Below_Poverty_Percent_2012
g7_Housholds_on_Food_stamps_with_Children_Under18_2012
g7_Housholds_Pop_on_Food_Stamps_2012
g7_Pop_BlackAA_2012
g7_Pop_White_2012
g7_Bt_18_24_percent_less_than_High_School_2012
g7_Bt_18_24_percent_High_School_2012
g7_Bt_18_24_percent_Some_College_or_AA_2012
g7_Bt_1824_percent_BA_or_Higher_2012
g7_Over_25_percent_less_than_9th_grade_2012
g7_Over_25_percent_9th_12th_2012
g7_Over_25_percent_High_School_2012
g7_Over_25__percent_Some_College_No_Deg_2012
g7_Over_25_percent_AA_2012
g7_Over_25_percent_Bachelors_2012
g7_Over_25_percent_Graduate_or_Professionals_2012
g7_school_id

g8_suspensionrate
g8_mobilityrateentrantswithdra
g8_attendancerate
g8_avg_class_size
g8_studentinstructionalstaffratio
g8_dropoutrate
g8_grade12documenteddecisionco
g8_grade12documenteddecisionem
g8_grade12documenteddecisionmi
g8_grad12docdec_col_emp
g8_graduationrate
g8_studentsmeetinguniversitysyste
g8_Est_Households_2012
g8_Est_Population_2012
g8_Med_Household_Income_2012
g8_Mean_Household_Income_2012
g8_Pop_Below_Poverty_2012
g8_Percent_Below_Poverty_2012
g8_Pop_Under18_2012
g8_Under18_Below_Poverty_2012
g8_Under18_Below_Poverty_Percent_2012
g8_Housholds_on_Food_stamps_with_Children_Under18_2012
g8_Housholds_Pop_on_Food_Stamps_2012
g8_Pop_BlackAA_2012
g8_Pop_White_2012
g8_Bt_18_24_percent_less_than_High_School_2012
g8_Bt_18_24_percent_High_School_2012
g8_Bt_18_24_percent_Some_College_or_AA_2012
g8_Bt_1824_percent_BA_or_Higher_2012
g8_Over_25_percent_less_than_9th_grade_2012
g8_Over_25_percent_9th_12th_2012
g8_Over_25_percent_High_School_2012
g8_Over_25__percent_Some_College_No_Deg_2012
g8_Over_25_percent_AA_2012
g8_Over_25_percent_Bachelors_2012
g8_Over_25_percent_Graduate_or_Professionals_2012
g8_school_id


g9_suspensionrate
g9_mobilityrateentrantswithdra
g9_attendancerate
g9_avg_class_size
g9_studentinstructionalstaffratio
g9_dropoutrate
g9_grade12documenteddecisionco
g9_grade12documenteddecisionem
g9_grade12documenteddecisionmi
g9_grad12docdec_col_emp
g9_graduationrate
g9_studentsmeetinguniversitysyste
g9_Est_Households_2012
g9_Est_Population_2012
g9_Med_Household_Income_2012
g9_Mean_Household_Income_2012
g9_Pop_Below_Poverty_2012
g9_Percent_Below_Poverty_2012
g9_Pop_Under18_2012
g9_Under18_Below_Poverty_2012
g9_Under18_Below_Poverty_Percent_2012
g9_Housholds_on_Food_stamps_with_Children_Under18_2012
g9_Housholds_Pop_on_Food_Stamps_2012
g9_Pop_BlackAA_2012
g9_Pop_White_2012
g9_Bt_18_24_percent_less_than_High_School_2012
g9_Bt_18_24_percent_High_School_2012
g9_Bt_18_24_percent_Some_College_or_AA_2012
g9_Bt_1824_percent_BA_or_Higher_2012
g9_Over_25_percent_less_than_9th_grade_2012
g9_Over_25_percent_9th_12th_2012
g9_Over_25_percent_High_School_2012
g9_Over_25__percent_Some_College_No_Deg_2012
g9_Over_25_percent_AA_2012
g9_Over_25_percent_Bachelors_2012
g9_Over_25_percent_Graduate_or_Professionals_2012
g9_school_id


g10_suspensionrate
g10_mobilityrateentrantswithdra
g10_attendancerate
g10_avg_class_size
g10_studentinstructionalstaffratio
g10_dropoutrate
g10_grade12documenteddecisionco
g10_grade12documenteddecisionem
g10_grade12documenteddecisionmi
g10_grad12docdec_col_emp
g10_graduationrate
g10_studentsmeetinguniversitysyste
g10_Est_Households_2012
g10_Est_Population_2012
g10_Med_Household_Income_2012
g10_Mean_Household_Income_2012
g10_Pop_Below_Poverty_2012
g10_Percent_Below_Poverty_2012
g10_Pop_Under18_2012
g10_Under18_Below_Poverty_2012
g10_Under18_Below_Poverty_Percent_2012
g10_Housholds_on_Food_stamps_with_Children_Under18_2012
g10_Housholds_Pop_on_Food_Stamps_2012
g10_Pop_BlackAA_2012
g10_Pop_White_2012
g10_Bt_18_24_percent_less_than_High_School_2012
g10_Bt_18_24_percent_High_School_2012
g10_Bt_18_24_percent_Some_College_or_AA_2012
g10_Bt_1824_percent_BA_or_Higher_2012
g10_Over_25_percent_less_than_9th_grade_2012
g10_Over_25_percent_9th_12th_2012
g10_Over_25_percent_High_School_2012
g10_Over_25__percent_Some_College_No_Deg_2012
g10_Over_25_percent_AA_2012
g10_Over_25_percent_Bachelors_2012
g10_Over_25_percent_Graduate_or_Professionals_2012
g10_school_id



g11_suspensionrate
g11_mobilityrateentrantswithdra
g11_attendancerate
g11_avg_class_size
g11_studentinstructionalstaffratio
g11_dropoutrate
g11_grade12documenteddecisionco
g11_grade12documenteddecisionem
g11_grade12documenteddecisionmi
g11_grad12docdec_col_emp
g11_graduationrate
g11_studentsmeetinguniversitysyste
g11_Est_Households_2012
g11_Est_Population_2012
g11_Med_Household_Income_2012
g11_Mean_Household_Income_2012
g11_Pop_Below_Poverty_2012
g11_Percent_Below_Poverty_2012
g11_Pop_Under18_2012
g11_Under18_Below_Poverty_2012
g11_Under18_Below_Poverty_Percent_2012
g11_Housholds_on_Food_stamps_with_Children_Under18_2012
g11_Housholds_Pop_on_Food_Stamps_2012
g11_Pop_BlackAA_2012
g11_Pop_White_2012
g11_Bt_18_24_percent_less_than_High_School_2012
g11_Bt_18_24_percent_High_School_2012
g11_Bt_18_24_percent_Some_College_or_AA_2012
g11_Bt_1824_percent_BA_or_Higher_2012
g11_Over_25_percent_less_than_9th_grade_2012
g11_Over_25_percent_9th_12th_2012
g11_Over_25_percent_High_School_2012
g11_Over_25__percent_Some_College_No_Deg_2012
g11_Over_25_percent_AA_2012
g11_Over_25_percent_Bachelors_2012
g11_Over_25_percent_Graduate_or_Professionals_2012
g11_school_id


g12_suspensionrate
g12_mobilityrateentrantswithdra
g12_attendancerate
g12_avg_class_size
g12_studentinstructionalstaffratio
g12_dropoutrate
g12_grade12documenteddecisionco
g12_grade12documenteddecisionem
g12_grade12documenteddecisionmi
g12_grad12docdec_col_emp
g12_graduationrate
g12_studentsmeetinguniversitysyste
g12_Est_Households_2012
g12_Est_Population_2012
g12_Med_Household_Income_2012
g12_Mean_Household_Income_2012
g12_Pop_Below_Poverty_2012
g12_Percent_Below_Poverty_2012
g12_Pop_Under18_2012
g12_Under18_Below_Poverty_2012
g12_Under18_Below_Poverty_Percent_2012
g12_Housholds_on_Food_stamps_with_Children_Under18_2012
g12_Housholds_Pop_on_Food_Stamps_2012
g12_Pop_BlackAA_2012
g12_Pop_White_2012
g12_Bt_18_24_percent_less_than_High_School_2012
g12_Bt_18_24_percent_High_School_2012
g12_Bt_18_24_percent_Some_College_or_AA_2012
g12_Bt_1824_percent_BA_or_Higher_2012
g12_Over_25_percent_less_than_9th_grade_2012
g12_Over_25_percent_9th_12th_2012
g12_Over_25_percent_High_School_2012
g12_Over_25__percent_Some_College_No_Deg_2012
g12_Over_25_percent_AA_2012
g12_Over_25_percent_Bachelors_2012
g12_Over_25_percent_Graduate_or_Professionals_2012
g12_school_id


"""


"""
'g6_suspensionrate',
'g7_suspensionrate',
'g8_suspensionrate',
'g9_suspensionrate',
'g10_suspensionrate',
'g11_suspensionrate',
'g12_suspensionrate',
'g6_mobilityrateentrantswithdra',
'g7_mobilityrateentrantswithdra',
'g8_mobilityrateentrantswithdra',
'g9_mobilityrateentrantswithdra',
'g10_mobilityrateentrantswithdra',
'g11_mobilityrateentrantswithdra',
'g12_mobilityrateentrantswithdra',
'g6_attendancerate',
'g7_attendancerate',
'g8_attendancerate',
'g9_attendancerate',
'g10_attendancerate',
'g11_attendancerate',
'g12_attendancerate',
'g6_avg_class_size',
'g7_avg_class_size',
'g8_avg_class_size',
'g9_avg_class_size',
'g10_avg_class_size',
'g11_avg_class_size',
'g12_avg_class_size',
'g6_studentinstructionalstaffratio',
'g7_studentinstructionalstaffratio',
'g8_studentinstructionalstaffratio',
'g9_studentinstructionalstaffratio',
'g10_studentinstructionalstaffratio',
'g11_studentinstructionalstaffratio',
'g12_studentinstructionalstaffratio',
'g6_dropoutrate',
'g7_dropoutrate',
'g8_dropoutrate',
'g9_dropoutrate',
'g10_dropoutrate',
'g11_dropoutrate',
'g12_dropoutrate',
'g6_grade12documenteddecisionco',
'g7_grade12documenteddecisionco',
'g8_grade12documenteddecisionco',
'g9_grade12documenteddecisionco',
'g10_grade12documenteddecisionco',
'g11_grade12documenteddecisionco',
'g12_grade12documenteddecisionco',
'g6_grade12documenteddecisionem',
'g7_grade12documenteddecisionem',
'g8_grade12documenteddecisionem',
'g9_grade12documenteddecisionem',
'g10_grade12documenteddecisionem',
'g11_grade12documenteddecisionem',
'g12_grade12documenteddecisionem',
'g6_grade12documenteddecisionmi',
'g7_grade12documenteddecisionmi',
'g8_grade12documenteddecisionmi',
'g9_grade12documenteddecisionmi',
'g10_grade12documenteddecisionmi',
'g11_grade12documenteddecisionmi',
'g12_grade12documenteddecisionmi',
'g6_grad12docdec_col_emp',
'g7_grad12docdec_col_emp',
'g8_grad12docdec_col_emp',
'g9_grad12docdec_col_emp',
'g10_grad12docdec_col_emp',
'g11_grad12docdec_col_emp',
'g12_grad12docdec_col_emp',
'g6_graduationrate',
'g7_graduationrate',
'g8_graduationrate',
'g9_graduationrate',
'g10_graduationrate',
'g11_graduationrate',
'g12_graduationrate',
'g6_studentsmeetinguniversitysyste',
'g7_studentsmeetinguniversitysyste',
'g8_studentsmeetinguniversitysyste',
'g9_studentsmeetinguniversitysyste',
'g10_studentsmeetinguniversitysyste',
'g11_studentsmeetinguniversitysyste',
'g12_studentsmeetinguniversitysyste',
'g6_Est_Households_2012',
'g7_Est_Households_2012',
'g8_Est_Households_2012',
'g9_Est_Households_2012',
'g10_Est_Households_2012',
'g11_Est_Households_2012',
'g12_Est_Households_2012',
'g6_Est_Population_2012',
'g7_Est_Population_2012',
'g8_Est_Population_2012',
'g9_Est_Population_2012',
'g10_Est_Population_2012',
'g11_Est_Population_2012',
'g12_Est_Population_2012',
'g6_Med_Household_Income_2012',
'g7_Med_Household_Income_2012',
'g8_Med_Household_Income_2012',
'g9_Med_Household_Income_2012',
'g10_Med_Household_Income_2012',
'g11_Med_Household_Income_2012',
'g12_Med_Household_Income_2012',
'g6_Mean_Household_Income_2012',
'g7_Mean_Household_Income_2012',
'g8_Mean_Household_Income_2012',
'g9_Mean_Household_Income_2012',
'g10_Mean_Household_Income_2012',
'g11_Mean_Household_Income_2012',
'g12_Mean_Household_Income_2012',
'g6_Pop_Below_Poverty_2012',
'g7_Pop_Below_Poverty_2012',
'g8_Pop_Below_Poverty_2012',
'g9_Pop_Below_Poverty_2012',
'g10_Pop_Below_Poverty_2012',
'g11_Pop_Below_Poverty_2012',
'g12_Pop_Below_Poverty_2012',
'g6_Percent_Below_Poverty_2012',
'g7_Percent_Below_Poverty_2012',
'g8_Percent_Below_Poverty_2012',
'g9_Percent_Below_Poverty_2012',
'g10_Percent_Below_Poverty_2012',
'g11_Percent_Below_Poverty_2012',
'g12_Percent_Below_Poverty_2012',
'g6_Pop_Under18_2012',
'g7_Pop_Under18_2012',
'g8_Pop_Under18_2012',
'g9_Pop_Under18_2012',
'g10_Pop_Under18_2012',
'g11_Pop_Under18_2012',
'g12_Pop_Under18_2012',
'g6_Under18_Below_Poverty_2012',
'g7_Under18_Below_Poverty_2012',
'g8_Under18_Below_Poverty_2012',
'g9_Under18_Below_Poverty_2012',
'g10_Under18_Below_Poverty_2012',
'g11_Under18_Below_Poverty_2012',
'g12_Under18_Below_Poverty_2012',
'g6_Under18_Below_Poverty_Percent_2012',
'g7_Under18_Below_Poverty_Percent_2012',
'g8_Under18_Below_Poverty_Percent_2012',
'g9_Under18_Below_Poverty_Percent_2012',
'g10_Under18_Below_Poverty_Percent_2012',
'g11_Under18_Below_Poverty_Percent_2012',
'g12_Under18_Below_Poverty_Percent_2012',
'g6_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g7_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g8_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g9_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g10_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g11_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g12_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g6_Housholds_Pop_on_Food_Stamps_2012',
'g7_Housholds_Pop_on_Food_Stamps_2012',
'g8_Housholds_Pop_on_Food_Stamps_2012',
'g9_Housholds_Pop_on_Food_Stamps_2012',
'g10_Housholds_Pop_on_Food_Stamps_2012',
'g11_Housholds_Pop_on_Food_Stamps_2012',
'g12_Housholds_Pop_on_Food_Stamps_2012',
'g6_Pop_BlackAA_2012',
'g7_Pop_BlackAA_2012',
'g8_Pop_BlackAA_2012',
'g9_Pop_BlackAA_2012',
'g10_Pop_BlackAA_2012',
'g11_Pop_BlackAA_2012',
'g12_Pop_BlackAA_2012',
'g6_Pop_White_2012',
'g7_Pop_White_2012',
'g8_Pop_White_2012',
'g9_Pop_White_2012',
'g10_Pop_White_2012',
'g11_Pop_White_2012',
'g12_Pop_White_2012',
'g6_Bt_18_24_percent_less_than_High_School_2012',
'g7_Bt_18_24_percent_less_than_High_School_2012',
'g8_Bt_18_24_percent_less_than_High_School_2012',
'g9_Bt_18_24_percent_less_than_High_School_2012',
'g10_Bt_18_24_percent_less_than_High_School_2012',
'g11_Bt_18_24_percent_less_than_High_School_2012',
'g12_Bt_18_24_percent_less_than_High_School_2012',
'g6_Bt_18_24_percent_High_School_2012',
'g7_Bt_18_24_percent_High_School_2012',
'g8_Bt_18_24_percent_High_School_2012',
'g9_Bt_18_24_percent_High_School_2012',
'g10_Bt_18_24_percent_High_School_2012',
'g11_Bt_18_24_percent_High_School_2012',
'g12_Bt_18_24_percent_High_School_2012',
'g6_Bt_18_24_percent_Some_College_or_AA_2012',
'g7_Bt_18_24_percent_Some_College_or_AA_2012',
'g8_Bt_18_24_percent_Some_College_or_AA_2012',
'g9_Bt_18_24_percent_Some_College_or_AA_2012',
'g10_Bt_18_24_percent_Some_College_or_AA_2012',
'g11_Bt_18_24_percent_Some_College_or_AA_2012',
'g12_Bt_18_24_percent_Some_College_or_AA_2012',
'g6_Bt_1824_percent_BA_or_Higher_2012',
'g7_Bt_1824_percent_BA_or_Higher_2012',
'g8_Bt_1824_percent_BA_or_Higher_2012',
'g9_Bt_1824_percent_BA_or_Higher_2012',
'g10_Bt_1824_percent_BA_or_Higher_2012',
'g11_Bt_1824_percent_BA_or_Higher_2012',
'g12_Bt_1824_percent_BA_or_Higher_2012',
'g6_Over_25_percent_less_than_9th_grade_2012',
'g7_Over_25_percent_less_than_9th_grade_2012',
'g8_Over_25_percent_less_than_9th_grade_2012',
'g9_Over_25_percent_less_than_9th_grade_2012',
'g10_Over_25_percent_less_than_9th_grade_2012',
'g11_Over_25_percent_less_than_9th_grade_2012',
'g12_Over_25_percent_less_than_9th_grade_2012',
'g6_Over_25_percent_9th_12th_2012',
'g7_Over_25_percent_9th_12th_2012',
'g8_Over_25_percent_9th_12th_2012',
'g9_Over_25_percent_9th_12th_2012',
'g10_Over_25_percent_9th_12th_2012',
'g11_Over_25_percent_9th_12th_2012',
'g12_Over_25_percent_9th_12th_2012',
'g6_Over_25_percent_High_School_2012',
'g7_Over_25_percent_High_School_2012',
'g8_Over_25_percent_High_School_2012',
'g9_Over_25_percent_High_School_2012',
'g10_Over_25_percent_High_School_2012',
'g11_Over_25_percent_High_School_2012',
'g12_Over_25_percent_High_School_2012',
'g6_Over_25__percent_Some_College_No_Deg_2012',
'g7_Over_25__percent_Some_College_No_Deg_2012',
'g8_Over_25__percent_Some_College_No_Deg_2012',
'g9_Over_25__percent_Some_College_No_Deg_2012',
'g10_Over_25__percent_Some_College_No_Deg_2012',
'g11_Over_25__percent_Some_College_No_Deg_2012',
'g12_Over_25__percent_Some_College_No_Deg_2012',
'g6_Over_25_percent_AA_2012',
'g7_Over_25_percent_AA_2012',
'g8_Over_25_percent_AA_2012',
'g9_Over_25_percent_AA_2012',
'g10_Over_25_percent_AA_2012',
'g11_Over_25_percent_AA_2012',
'g12_Over_25_percent_AA_2012',
'g6_Over_25_percent_Bachelors_2012',
'g7_Over_25_percent_Bachelors_2012',
'g8_Over_25_percent_Bachelors_2012',
'g9_Over_25_percent_Bachelors_2012',
'g10_Over_25_percent_Bachelors_2012',
'g11_Over_25_percent_Bachelors_2012',
'g12_Over_25_percent_Bachelors_2012',
'g6_Over_25_percent_Graduate_or_Professionals_2012',
'g7_Over_25_percent_Graduate_or_Professionals_2012',
'g8_Over_25_percent_Graduate_or_Professionals_2012',
'g9_Over_25_percent_Graduate_or_Professionals_2012',
'g10_Over_25_percent_Graduate_or_Professionals_2012',
'g11_Over_25_percent_Graduate_or_Professionals_2012',
'g12_Over_25_percent_Graduate_or_Professionals_2012'

"""
"""

'g6_suspensionrate', 'g7_suspensionrate', 'g8_suspensionrate', 'g9_suspensionrate', 'g10_suspensionrate', 'g11_suspensionrate', 'g12_suspensionrate',
'g6_mobilityrateentrantswithdra', 'g7_mobilityrateentrantswithdra', 'g8_mobilityrateentrantswithdra', 'g9_mobilityrateentrantswithdra', 'g10_mobilityrateentrantswithdra', 'g11_mobilityrateentrantswithdra', 'g12_mobilityrateentrantswithdra',
'g6_attendancerate', 'g7_attendancerate', 'g8_attendancerate', 'g9_attendancerate', 'g10_attendancerate', 'g11_attendancerate', 'g12_attendancerate',
'g6_avg_class_size', 'g7_avg_class_size', 'g8_avg_class_size', 'g9_avg_class_size', 'g10_avg_class_size', 'g11_avg_class_size', 'g12_avg_class_size',
'g6_studentinstructionalstaffratio', 'g7_studentinstructionalstaffratio', 'g8_studentinstructionalstaffratio', 'g9_studentinstructionalstaffratio', 'g10_studentinstructionalstaffratio', 'g11_studentinstructionalstaffratio', 'g12_studentinstructionalstaffratio',
'g6_dropoutrate', 'g7_dropoutrate', 'g8_dropoutrate', 'g9_dropoutrate', 'g10_dropoutrate', 'g11_dropoutrate', 'g12_dropoutrate',
'g6_grade12documenteddecisionco', 'g7_grade12documenteddecisionco', 'g8_grade12documenteddecisionco', 'g9_grade12documenteddecisionco', 'g10_grade12documenteddecisionco', 'g11_grade12documenteddecisionco', 'g12_grade12documenteddecisionco',
'g6_grade12documenteddecisionem', 'g7_grade12documenteddecisionem', 'g8_grade12documenteddecisionem', 'g9_grade12documenteddecisionem', 'g10_grade12documenteddecisionem', 'g11_grade12documenteddecisionem', 'g12_grade12documenteddecisionem',
'g6_grade12documenteddecisionmi', 'g7_grade12documenteddecisionmi', 'g8_grade12documenteddecisionmi', 'g9_grade12documenteddecisionmi', 'g10_grade12documenteddecisionmi', 'g11_grade12documenteddecisionmi', 'g12_grade12documenteddecisionmi',
'g6_grad12docdec_col_emp', 'g7_grad12docdec_col_emp', 'g8_grad12docdec_col_emp', 'g9_grad12docdec_col_emp', 'g10_grad12docdec_col_emp', 'g11_grad12docdec_col_emp', 'g12_grad12docdec_col_emp',
'g6_graduationrate', 'g7_graduationrate', 'g8_graduationrate', 'g9_graduationrate', 'g10_graduationrate', 'g11_graduationrate', 'g12_graduationrate',
'g6_studentsmeetinguniversitysyste', 'g7_studentsmeetinguniversitysyste', 'g8_studentsmeetinguniversitysyste', 'g9_studentsmeetinguniversitysyste', 'g10_studentsmeetinguniversitysyste', 'g11_studentsmeetinguniversitysyste', 'g12_studentsmeetinguniversitysyste',
'g6_Est_Households_2012', 'g7_Est_Households_2012', 'g8_Est_Households_2012', 'g9_Est_Households_2012', 'g10_Est_Households_2012', 'g11_Est_Households_2012', 'g12_Est_Households_2012',
'g6_Est_Population_2012', 'g7_Est_Population_2012', 'g8_Est_Population_2012', 'g9_Est_Population_2012', 'g10_Est_Population_2012', 'g11_Est_Population_2012', 'g12_Est_Population_2012',
'g6_Med_Household_Income_2012', 'g7_Med_Household_Income_2012', 'g8_Med_Household_Income_2012', 'g9_Med_Household_Income_2012', 'g10_Med_Household_Income_2012', 'g11_Med_Household_Income_2012', 'g12_Med_Household_Income_2012',
'g6_Mean_Household_Income_2012', 'g7_Mean_Household_Income_2012', 'g8_Mean_Household_Income_2012', 'g9_Mean_Household_Income_2012', 'g10_Mean_Household_Income_2012', 'g11_Mean_Household_Income_2012', 'g12_Mean_Household_Income_2012',
'g6_Pop_Below_Poverty_2012', 'g7_Pop_Below_Poverty_2012', 'g8_Pop_Below_Poverty_2012', 'g9_Pop_Below_Poverty_2012', 'g10_Pop_Below_Poverty_2012', 'g11_Pop_Below_Poverty_2012', 'g12_Pop_Below_Poverty_2012',
'g6_Percent_Below_Poverty_2012', 'g7_Percent_Below_Poverty_2012', 'g8_Percent_Below_Poverty_2012', 'g9_Percent_Below_Poverty_2012', 'g10_Percent_Below_Poverty_2012', 'g11_Percent_Below_Poverty_2012', 'g12_Percent_Below_Poverty_2012',
'g6_Pop_Under18_2012', 'g7_Pop_Under18_2012', 'g8_Pop_Under18_2012', 'g9_Pop_Under18_2012', 'g10_Pop_Under18_2012', 'g11_Pop_Under18_2012', 'g12_Pop_Under18_2012',
'g6_Under18_Below_Poverty_2012', 'g7_Under18_Below_Poverty_2012', 'g8_Under18_Below_Poverty_2012', 'g9_Under18_Below_Poverty_2012', 'g10_Under18_Below_Poverty_2012', 'g11_Under18_Below_Poverty_2012', 'g12_Under18_Below_Poverty_2012',
'g6_Under18_Below_Poverty_Percent_2012', 'g7_Under18_Below_Poverty_Percent_2012', 'g8_Under18_Below_Poverty_Percent_2012', 'g9_Under18_Below_Poverty_Percent_2012', 'g10_Under18_Below_Poverty_Percent_2012', 'g11_Under18_Below_Poverty_Percent_2012', 'g12_Under18_Below_Poverty_Percent_2012',
'g6_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g7_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g8_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g9_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g10_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g11_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g12_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g6_Housholds_Pop_on_Food_Stamps_2012', 'g7_Housholds_Pop_on_Food_Stamps_2012', 'g8_Housholds_Pop_on_Food_Stamps_2012', 'g9_Housholds_Pop_on_Food_Stamps_2012', 'g10_Housholds_Pop_on_Food_Stamps_2012', 'g11_Housholds_Pop_on_Food_Stamps_2012', 'g12_Housholds_Pop_on_Food_Stamps_2012',
'g6_Pop_BlackAA_2012', 'g7_Pop_BlackAA_2012', 'g8_Pop_BlackAA_2012', 'g9_Pop_BlackAA_2012', 'g10_Pop_BlackAA_2012', 'g11_Pop_BlackAA_2012', 'g12_Pop_BlackAA_2012',
'g6_Pop_White_2012', 'g7_Pop_White_2012', 'g8_Pop_White_2012', 'g9_Pop_White_2012', 'g10_Pop_White_2012', 'g11_Pop_White_2012', 'g12_Pop_White_2012',
'g6_Bt_18_24_percent_less_than_High_School_2012', 'g7_Bt_18_24_percent_less_than_High_School_2012', 'g8_Bt_18_24_percent_less_than_High_School_2012', 'g9_Bt_18_24_percent_less_than_High_School_2012', 'g10_Bt_18_24_percent_less_than_High_School_2012', 'g11_Bt_18_24_percent_less_than_High_School_2012', 'g12_Bt_18_24_percent_less_than_High_School_2012',
'g6_Bt_18_24_percent_High_School_2012', 'g7_Bt_18_24_percent_High_School_2012', 'g8_Bt_18_24_percent_High_School_2012', 'g9_Bt_18_24_percent_High_School_2012', 'g10_Bt_18_24_percent_High_School_2012', 'g11_Bt_18_24_percent_High_School_2012', 'g12_Bt_18_24_percent_High_School_2012',
'g6_Bt_18_24_percent_Some_College_or_AA_2012', 'g7_Bt_18_24_percent_Some_College_or_AA_2012', 'g8_Bt_18_24_percent_Some_College_or_AA_2012', 'g9_Bt_18_24_percent_Some_College_or_AA_2012', 'g10_Bt_18_24_percent_Some_College_or_AA_2012', 'g11_Bt_18_24_percent_Some_College_or_AA_2012', 'g12_Bt_18_24_percent_Some_College_or_AA_2012',
'g6_Bt_1824_percent_BA_or_Higher_2012', 'g7_Bt_1824_percent_BA_or_Higher_2012', 'g8_Bt_1824_percent_BA_or_Higher_2012', 'g9_Bt_1824_percent_BA_or_Higher_2012', 'g10_Bt_1824_percent_BA_or_Higher_2012', 'g11_Bt_1824_percent_BA_or_Higher_2012', 'g12_Bt_1824_percent_BA_or_Higher_2012',
'g6_Over_25_percent_less_than_9th_grade_2012', 'g7_Over_25_percent_less_than_9th_grade_2012', 'g8_Over_25_percent_less_than_9th_grade_2012', 'g9_Over_25_percent_less_than_9th_grade_2012', 'g10_Over_25_percent_less_than_9th_grade_2012', 'g11_Over_25_percent_less_than_9th_grade_2012', 'g12_Over_25_percent_less_than_9th_grade_2012',
'g6_Over_25_percent_9th_12th_2012', 'g7_Over_25_percent_9th_12th_2012', 'g8_Over_25_percent_9th_12th_2012', 'g9_Over_25_percent_9th_12th_2012', 'g10_Over_25_percent_9th_12th_2012', 'g11_Over_25_percent_9th_12th_2012', 'g12_Over_25_percent_9th_12th_2012',
'g6_Over_25_percent_High_School_2012', 'g7_Over_25_percent_High_School_2012', 'g8_Over_25_percent_High_School_2012', 'g9_Over_25_percent_High_School_2012', 'g10_Over_25_percent_High_School_2012', 'g11_Over_25_percent_High_School_2012', 'g12_Over_25_percent_High_School_2012',
'g6_Over_25__percent_Some_College_No_Deg_2012', 'g7_Over_25__percent_Some_College_No_Deg_2012', 'g8_Over_25__percent_Some_College_No_Deg_2012', 'g9_Over_25__percent_Some_College_No_Deg_2012', 'g10_Over_25__percent_Some_College_No_Deg_2012', 'g11_Over_25__percent_Some_College_No_Deg_2012', 'g12_Over_25__percent_Some_College_No_Deg_2012',
'g6_Over_25_percent_AA_2012', 'g7_Over_25_percent_AA_2012', 'g8_Over_25_percent_AA_2012', 'g9_Over_25_percent_AA_2012', 'g10_Over_25_percent_AA_2012', 'g11_Over_25_percent_AA_2012', 'g12_Over_25_percent_AA_2012',
'g6_Over_25_percent_Bachelors_2012', 'g7_Over_25_percent_Bachelors_2012', 'g8_Over_25_percent_Bachelors_2012', 'g9_Over_25_percent_Bachelors_2012', 'g10_Over_25_percent_Bachelors_2012', 'g11_Over_25_percent_Bachelors_2012', 'g12_Over_25_percent_Bachelors_2012',
'g6_Over_25_percent_Graduate_or_Professionals_2012', 'g7_Over_25_percent_Graduate_or_Professionals_2012', 'g8_Over_25_percent_Graduate_or_Professionals_2012', 'g9_Over_25_percent_Graduate_or_Professionals_2012', 'g10_Over_25_percent_Graduate_or_Professionals_2012', 'g11_Over_25_percent_Graduate_or_Professionals_2012', 'g12_Over_25_percent_Graduate_or_Professionals_2012'
"""

"""
'g9_suspensionrate',
'g9_mobilityrateentrantswithdra',
'g9_attendancerate',
'g9_avg_class_size',
'g9_studentinstructionalstaffratio',
'g9_dropoutrate',
'g9_grade12documenteddecisionco',
'g9_grade12documenteddecisionem',
'g9_grade12documenteddecisionmi',
'g9_grad12docdec_col_emp',
'g9_graduationrate',
'g9_studentsmeetinguniversitysyste',
'g9_Est_Households_2012',
'g9_Est_Population_2012',
'g9_Med_Household_Income_2012',
'g9_Mean_Household_Income_2012',
'g9_Pop_Below_Poverty_2012',
'g9_Percent_Below_Poverty_2012',
'g9_Pop_Under18_2012',
'g9_Under18_Below_Poverty_2012',
'g9_Under18_Below_Poverty_Percent_2012',
'g9_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g9_Housholds_Pop_on_Food_Stamps_2012',
'g9_Pop_BlackAA_2012',
'g9_Pop_White_2012',
'g9_Bt_18_24_percent_less_than_High_School_2012',
'g9_Bt_18_24_percent_High_School_2012',
'g9_Bt_18_24_percent_Some_College_or_AA_2012',
'g9_Bt_1824_percent_BA_or_Higher_2012',
'g9_Over_25_percent_less_than_9th_grade_2012',
'g9_Over_25_percent_9th_12th_2012',
'g9_Over_25_percent_High_School_2012',
'g9_Over_25__percent_Some_College_No_Deg_2012',
'g9_Over_25_percent_AA_2012',
'g9_Over_25_percent_Bachelors_2012',
'g9_Over_25_percent_Graduate_or_Professionals_2012',
'g10_suspensionrate',
'g10_mobilityrateentrantswithdra',
'g10_attendancerate',
'g10_avg_class_size',
'g10_studentinstructionalstaffratio',
'g10_dropoutrate',
'g10_grade12documenteddecisionco',
'g10_grade12documenteddecisionem',
'g10_grade12documenteddecisionmi',
'g10_grad12docdec_col_emp',
'g10_graduationrate',
'g10_studentsmeetinguniversitysyste',
'g10_Est_Households_2012',
'g10_Est_Population_2012',
'g10_Med_Household_Income_2012',
'g10_Mean_Household_Income_2012',
'g10_Pop_Below_Poverty_2012',
'g10_Percent_Below_Poverty_2012',
'g10_Pop_Under18_2012',
'g10_Under18_Below_Poverty_2012',
'g10_Under18_Below_Poverty_Percent_2012',
'g10_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g10_Housholds_Pop_on_Food_Stamps_2012',
'g10_Pop_BlackAA_2012',
'g10_Pop_White_2012',
'g10_Bt_18_24_percent_less_than_High_School_2012',
'g10_Bt_18_24_percent_High_School_2012',
'g10_Bt_18_24_percent_Some_College_or_AA_2012',
'g10_Bt_1824_percent_BA_or_Higher_2012',
'g10_Over_25_percent_less_than_9th_grade_2012',
'g10_Over_25_percent_9th_12th_2012',
'g10_Over_25_percent_High_School_2012',
'g10_Over_25__percent_Some_College_No_Deg_2012',
'g10_Over_25_percent_AA_2012',
'g10_Over_25_percent_Bachelors_2012',
'g10_Over_25_percent_Graduate_or_Professionals_2012',
'g11_suspensionrate',
'g11_mobilityrateentrantswithdra',
'g11_attendancerate',
'g11_avg_class_size',
'g11_studentinstructionalstaffratio',
'g11_dropoutrate',
'g11_grade12documenteddecisionco',
'g11_grade12documenteddecisionem',
'g11_grade12documenteddecisionmi',
'g11_grad12docdec_col_emp',
'g11_graduationrate',
'g11_studentsmeetinguniversitysyste',
'g11_Est_Households_2012',
'g11_Est_Population_2012',
'g11_Med_Household_Income_2012',
'g11_Mean_Household_Income_2012',
'g11_Pop_Below_Poverty_2012',
'g11_Percent_Below_Poverty_2012',
'g11_Pop_Under18_2012',
'g11_Under18_Below_Poverty_2012',
'g11_Under18_Below_Poverty_Percent_2012',
'g11_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g11_Housholds_Pop_on_Food_Stamps_2012',
'g11_Pop_BlackAA_2012',
'g11_Pop_White_2012',
'g11_Bt_18_24_percent_less_than_High_School_2012',
'g11_Bt_18_24_percent_High_School_2012',
'g11_Bt_18_24_percent_Some_College_or_AA_2012',
'g11_Bt_1824_percent_BA_or_Higher_2012',
'g11_Over_25_percent_less_than_9th_grade_2012',
'g11_Over_25_percent_9th_12th_2012',
'g11_Over_25_percent_High_School_2012',
'g11_Over_25__percent_Some_College_No_Deg_2012',
'g11_Over_25_percent_AA_2012',
'g11_Over_25_percent_Bachelors_2012',
'g11_Over_25_percent_Graduate_or_Professionals_2012',
'g12_suspensionrate',
'g12_mobilityrateentrantswithdra',
'g12_attendancerate',
'g12_avg_class_size',
'g12_studentinstructionalstaffratio',
'g12_dropoutrate',
'g12_grade12documenteddecisionco',
'g12_grade12documenteddecisionem',
'g12_grade12documenteddecisionmi',
'g12_grad12docdec_col_emp',
'g12_graduationrate',
'g12_studentsmeetinguniversitysyste',
'g12_Est_Households_2012',
'g12_Est_Population_2012',
'g12_Med_Household_Income_2012',
'g12_Mean_Household_Income_2012',
'g12_Pop_Below_Poverty_2012',
'g12_Percent_Below_Poverty_2012',
'g12_Pop_Under18_2012',
'g12_Under18_Below_Poverty_2012',
'g12_Under18_Below_Poverty_Percent_2012',
'g12_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g12_Housholds_Pop_on_Food_Stamps_2012',
'g12_Pop_BlackAA_2012',
'g12_Pop_White_2012',
'g12_Bt_18_24_percent_less_than_High_School_2012',
'g12_Bt_18_24_percent_High_School_2012',
'g12_Bt_18_24_percent_Some_College_or_AA_2012',
'g12_Bt_1824_percent_BA_or_Higher_2012',
'g12_Over_25_percent_less_than_9th_grade_2012',
'g12_Over_25_percent_9th_12th_2012',
'g12_Over_25_percent_High_School_2012',
'g12_Over_25__percent_Some_College_No_Deg_2012',
'g12_Over_25_percent_AA_2012',
'g12_Over_25_percent_Bachelors_2012',
'g12_Over_25_percent_Graduate_or_Professionals_2012'


"""

"""

g9_suspensionrate
g9_mobilityrateentrantswithdra
g9_attendancerate
g9_avg_class_size
g9_studentinstructionalstaffratio
g9_dropoutrate
g9_grade12documenteddecisionco
g9_grade12documenteddecisionem
g9_grade12documenteddecisionmi
g9_grad12docdec_col_emp
g9_graduationrate
g9_studentsmeetinguniversitysyste
g9_Est_Households_2012
g9_Est_Population_2012
g9_Med_Household_Income_2012
g9_Mean_Household_Income_2012
g9_Pop_Below_Poverty_2012
g9_Percent_Below_Poverty_2012
g9_Pop_Under18_2012
g9_Under18_Below_Poverty_2012
g9_Under18_Below_Poverty_Percent_2012
g9_Housholds_on_Food_stamps_with_Children_Under18_2012
g9_Housholds_Pop_on_Food_Stamps_2012
g9_Pop_BlackAA_2012
g9_Pop_White_2012
g9_Bt_18_24_percent_less_than_High_School_2012
g9_Bt_18_24_percent_High_School_2012
g9_Bt_18_24_percent_Some_College_or_AA_2012
g9_Bt_1824_percent_BA_or_Higher_2012
g9_Over_25_percent_less_than_9th_grade_2012
g9_Over_25_percent_9th_12th_2012
g9_Over_25_percent_High_School_2012
g9_Over_25__percent_Some_College_No_Deg_2012
g9_Over_25_percent_AA_2012
g9_Over_25_percent_Bachelors_2012
g9_Over_25_percent_Graduate_or_Professionals_2012
g10_suspensionrate
g10_mobilityrateentrantswithdra
g10_attendancerate
g10_avg_class_size
g10_studentinstructionalstaffratio
g10_dropoutrate
g10_grade12documenteddecisionco
g10_grade12documenteddecisionem
g10_grade12documenteddecisionmi
g10_grad12docdec_col_emp
g10_graduationrate
g10_studentsmeetinguniversitysyste
g10_Est_Households_2012
g10_Est_Population_2012
g10_Med_Household_Income_2012
g10_Mean_Household_Income_2012
g10_Pop_Below_Poverty_2012
g10_Percent_Below_Poverty_2012
g10_Pop_Under18_2012
g10_Under18_Below_Poverty_2012
g10_Under18_Below_Poverty_Percent_2012
g10_Housholds_on_Food_stamps_with_Children_Under18_2012
g10_Housholds_Pop_on_Food_Stamps_2012
g10_Pop_BlackAA_2012
g10_Pop_White_2012
g10_Bt_18_24_percent_less_than_High_School_2012
g10_Bt_18_24_percent_High_School_2012
g10_Bt_18_24_percent_Some_College_or_AA_2012
g10_Bt_1824_percent_BA_or_Higher_2012
g10_Over_25_percent_less_than_9th_grade_2012
g10_Over_25_percent_9th_12th_2012
g10_Over_25_percent_High_School_2012
g10_Over_25__percent_Some_College_No_Deg_2012
g10_Over_25_percent_AA_2012
g10_Over_25_percent_Bachelors_2012
g10_Over_25_percent_Graduate_or_Professionals_2012
g11_suspensionrate
g11_mobilityrateentrantswithdra
g11_attendancerate
g11_avg_class_size
g11_studentinstructionalstaffratio
g11_dropoutrate
g11_grade12documenteddecisionco
g11_grade12documenteddecisionem
g11_grade12documenteddecisionmi
g11_grad12docdec_col_emp
g11_graduationrate
g11_studentsmeetinguniversitysyste
g11_Est_Households_2012
g11_Est_Population_2012
g11_Med_Household_Income_2012
g11_Mean_Household_Income_2012
g11_Pop_Below_Poverty_2012
g11_Percent_Below_Poverty_2012
g11_Pop_Under18_2012
g11_Under18_Below_Poverty_2012
g11_Under18_Below_Poverty_Percent_2012
g11_Housholds_on_Food_stamps_with_Children_Under18_2012
g11_Housholds_Pop_on_Food_Stamps_2012
g11_Pop_BlackAA_2012
g11_Pop_White_2012
g11_Bt_18_24_percent_less_than_High_School_2012
g11_Bt_18_24_percent_High_School_2012
g11_Bt_18_24_percent_Some_College_or_AA_2012
g11_Bt_1824_percent_BA_or_Higher_2012
g11_Over_25_percent_less_than_9th_grade_2012
g11_Over_25_percent_9th_12th_2012
g11_Over_25_percent_High_School_2012
g11_Over_25__percent_Some_College_No_Deg_2012
g11_Over_25_percent_AA_2012
g11_Over_25_percent_Bachelors_2012
g11_Over_25_percent_Graduate_or_Professionals_2012
g12_suspensionrate
g12_mobilityrateentrantswithdra
g12_attendancerate
g12_avg_class_size
g12_studentinstructionalstaffratio
g12_dropoutrate
g12_grade12documenteddecisionco
g12_grade12documenteddecisionem
g12_grade12documenteddecisionmi
g12_grad12docdec_col_emp
g12_graduationrate
g12_studentsmeetinguniversitysyste
g12_Est_Households_2012
g12_Est_Population_2012
g12_Med_Household_Income_2012
g12_Mean_Household_Income_2012
g12_Pop_Below_Poverty_2012
g12_Percent_Below_Poverty_2012
g12_Pop_Under18_2012
g12_Under18_Below_Poverty_2012
g12_Under18_Below_Poverty_Percent_2012
g12_Housholds_on_Food_stamps_with_Children_Under18_2012
g12_Housholds_Pop_on_Food_Stamps_2012
g12_Pop_BlackAA_2012
g12_Pop_White_2012
g12_Bt_18_24_percent_less_than_High_School_2012
g12_Bt_18_24_percent_High_School_2012
g12_Bt_18_24_percent_Some_College_or_AA_2012
g12_Bt_1824_percent_BA_or_Higher_2012
g12_Over_25_percent_less_than_9th_grade_2012
g12_Over_25_percent_9th_12th_2012
g12_Over_25_percent_High_School_2012
g12_Over_25__percent_Some_College_No_Deg_2012
g12_Over_25_percent_AA_2012
g12_Over_25_percent_Bachelors_2012
g12_Over_25_percent_Graduate_or_Professionals_2012

"""

## 9th - 12th grade code labels imput

"""

'g9_suspensionrate', 'g10_suspensionrate', 'g11_suspensionrate', 'g12_suspensionrate',
'g9_mobilityrateentrantswithdra', 'g10_mobilityrateentrantswithdra', 'g11_mobilityrateentrantswithdra', 'g12_mobilityrateentrantswithdra',
'g9_attendancerate', 'g10_attendancerate', 'g11_attendancerate', 'g12_attendancerate',
'g9_avg_class_size', 'g10_avg_class_size', 'g11_avg_class_size', 'g12_avg_class_size',
'g9_studentinstructionalstaffratio', 'g10_studentinstructionalstaffratio', 'g11_studentinstructionalstaffratio', 'g12_studentinstructionalstaffratio',
'g9_dropoutrate', 'g10_dropoutrate', 'g11_dropoutrate', 'g12_dropoutrate',
'g9_grade12documenteddecisionco', 'g10_grade12documenteddecisionco', 'g11_grade12documenteddecisionco', 'g12_grade12documenteddecisionco',
'g9_grade12documenteddecisionem', 'g10_grade12documenteddecisionem', 'g11_grade12documenteddecisionem', 'g12_grade12documenteddecisionem',
'g9_grade12documenteddecisionmi', 'g10_grade12documenteddecisionmi', 'g11_grade12documenteddecisionmi', 'g12_grade12documenteddecisionmi',
'g9_grad12docdec_col_emp', 'g10_grad12docdec_col_emp', 'g11_grad12docdec_col_emp', 'g12_grad12docdec_col_emp',
'g9_graduationrate', 'g10_graduationrate', 'g11_graduationrate', 'g12_graduationrate',
'g9_studentsmeetinguniversitysyste', 'g10_studentsmeetinguniversitysyste', 'g11_studentsmeetinguniversitysyste', 'g12_studentsmeetinguniversitysyste',
'g9_Est_Households_2012', 'g10_Est_Households_2012', 'g11_Est_Households_2012', 'g12_Est_Households_2012',
'g9_Est_Population_2012', 'g10_Est_Population_2012', 'g11_Est_Population_2012', 'g12_Est_Population_2012',
'g9_Med_Household_Income_2012', 'g10_Med_Household_Income_2012', 'g11_Med_Household_Income_2012', 'g12_Med_Household_Income_2012',
'g9_Mean_Household_Income_2012', 'g10_Mean_Household_Income_2012', 'g11_Mean_Household_Income_2012', 'g12_Mean_Household_Income_2012',
'g9_Pop_Below_Poverty_2012', 'g10_Pop_Below_Poverty_2012', 'g11_Pop_Below_Poverty_2012', 'g12_Pop_Below_Poverty_2012',
'g9_Percent_Below_Poverty_2012', 'g10_Percent_Below_Poverty_2012', 'g11_Percent_Below_Poverty_2012', 'g12_Percent_Below_Poverty_2012',
'g9_Pop_Under18_2012', 'g10_Pop_Under18_2012', 'g11_Pop_Under18_2012', 'g12_Pop_Under18_2012',
'g9_Under18_Below_Poverty_2012', 'g10_Under18_Below_Poverty_2012', 'g11_Under18_Below_Poverty_2012', 'g12_Under18_Below_Poverty_2012',
'g9_Under18_Below_Poverty_Percent_2012', 'g10_Under18_Below_Poverty_Percent_2012', 'g11_Under18_Below_Poverty_Percent_2012', 'g12_Under18_Below_Poverty_Percent_2012',
'g9_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g10_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g11_Housholds_on_Food_stamps_with_Children_Under18_2012', 'g12_Housholds_on_Food_stamps_with_Children_Under18_2012',
'g9_Housholds_Pop_on_Food_Stamps_2012', 'g10_Housholds_Pop_on_Food_Stamps_2012', 'g11_Housholds_Pop_on_Food_Stamps_2012', 'g12_Housholds_Pop_on_Food_Stamps_2012',
'g9_Pop_BlackAA_2012', 'g10_Pop_BlackAA_2012', 'g11_Pop_BlackAA_2012', 'g12_Pop_BlackAA_2012',
'g9_Pop_White_2012', 'g10_Pop_White_2012', 'g11_Pop_White_2012', 'g12_Pop_White_2012',
'g9_Bt_18_24_percent_less_than_High_School_2012', 'g10_Bt_18_24_percent_less_than_High_School_2012', 'g11_Bt_18_24_percent_less_than_High_School_2012', 'g12_Bt_18_24_percent_less_than_High_School_2012',
'g9_Bt_18_24_percent_High_School_2012', 'g10_Bt_18_24_percent_High_School_2012', 'g11_Bt_18_24_percent_High_School_2012', 'g12_Bt_18_24_percent_High_School_2012',
'g9_Bt_18_24_percent_Some_College_or_AA_2012', 'g10_Bt_18_24_percent_Some_College_or_AA_2012', 'g11_Bt_18_24_percent_Some_College_or_AA_2012', 'g12_Bt_18_24_percent_Some_College_or_AA_2012',
'g9_Bt_1824_percent_BA_or_Higher_2012', 'g10_Bt_1824_percent_BA_or_Higher_2012', 'g11_Bt_1824_percent_BA_or_Higher_2012', 'g12_Bt_1824_percent_BA_or_Higher_2012',
'g9_Over_25_percent_less_than_9th_grade_2012', 'g10_Over_25_percent_less_than_9th_grade_2012', 'g11_Over_25_percent_less_than_9th_grade_2012', 'g12_Over_25_percent_less_than_9th_grade_2012',
'g9_Over_25_percent_9th_12th_2012', 'g10_Over_25_percent_9th_12th_2012', 'g11_Over_25_percent_9th_12th_2012', 'g12_Over_25_percent_9th_12th_2012',
'g9_Over_25_percent_High_School_2012', 'g10_Over_25_percent_High_School_2012', 'g11_Over_25_percent_High_School_2012', 'g12_Over_25_percent_High_School_2012',
'g9_Over_25__percent_Some_College_No_Deg_2012', 'g10_Over_25__percent_Some_College_No_Deg_2012', 'g11_Over_25__percent_Some_College_No_Deg_2012', 'g12_Over_25__percent_Some_College_No_Deg_2012',
'g9_Over_25_percent_AA_2012', 'g10_Over_25_percent_AA_2012', 'g11_Over_25_percent_AA_2012', 'g12_Over_25_percent_AA_2012',
'g9_Over_25_percent_Bachelors_2012', 'g10_Over_25_percent_Bachelors_2012', 'g11_Over_25_percent_Bachelors_2012', 'g12_Over_25_percent_Bachelors_2012',
'g9_Over_25_percent_Graduate_or_Professionals_2012', 'g10_Over_25_percent_Graduate_or_Professionals_2012', 'g11_Over_25_percent_Graduate_or_Professionals_2012', 'g12_Over_25_percent_Graduate_or_Professionals_2012',

"""