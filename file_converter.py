import pandas as pd
import os as os
df = pd.read_csv(r'jobs.csv')


# for i in range(len(df)):
#     jobTitle = df.loc[i][2]
# #     # Discription = df.loc[i][0]
# #     # minimumQualifications = df.loc[i][1]
# #     job = df.loc[i][3]
#     f_name = jobTitle + ".html"
# #     #f = open(f_name,"a")
# #     # f.write(jobTitle)
# #     #data = df.loc[i]
# #     html = df.to_html(f_name)
#     top = df.head(i+1)
#     bottem = top.tail(1)
#     #bottem.to_html(f_name)



for i in range(len(df)):
    jobTitle = df.loc[i][2]
    Discription = df.loc[i][0]
    minimumQualifications = df.loc[i][1]
    job = df.loc[i][3]
    #name of html file 
    f_name = jobTitle + ".html"
    total_data  ="<b>Job Title:			</b> " + jobTitle + "<br><b> Discription:			</b>" +Discription + "<br> <b>minimumQualifications:		</b> " + minimumQualifications +"<br><b> job:		</b>"+job
    f = open('html_files/'+f_name,"a")
    f.write(total_data)



