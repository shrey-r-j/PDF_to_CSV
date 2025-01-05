import PyPDF2
import pandas as pd
import re
import np
import gui2

import matplotlib.pyplot as pl
# Open the PDF file
path = gui2.my_function
reader = PyPDF2.PdfReader(gui2.selected_file_path)

import os

# # Ask the user for a directory to save the files
# save_dir = input("Please enter the directory where you want to save the CSV files: ")

# # Ensure the directory exists
# if not os.path.exists(save_dir):
#     os.makedirs(save_dir)

save_dir = gui2.selected_folder_path  # Use the folder selected in the GUI

# Ensure the directory exists
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


text = ""
for page_num in range(len(reader.pages)):
    page = reader.pages[page_num] 
    text += page.extract_text()
text_1=''
for k in text:
    if k=='*':
        text_1+=' '
    elif k=='#':
        text_1+=''
    else:
        text_1+=k

# Extract the table using regex
col=re.findall(r'(\w{6}\s*\w{4}\s*\w{3}\s*\w{3}\s*\w{5}\s*\w{2}\s*\w{2}\s*\w{2}\s*\w{3}%\s*\w{3}\s*\w{3}\s*\w{2}\s*\w{2})',text)
mech=re.findall(r'\w{11}\s*M\w{8}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
mech_pr=re.findall(r'\w{11}\s*M\w{8}\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
sme=re.findall(r'SYSTEMS IN MECH. ENGG.\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
sme_pr=re.findall(r'SYSTEMS IN MECH. ENGG.\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
bee=re.findall(r'BASIC ELECTRICAL ENGG.\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
bee_pr=re.findall(r'BASIC ELECTRICAL ENGG.\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
m1=re.findall(r'ENGINEERING MATHEMATICS I\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
m1_tw=re.findall(r'ENGINEERING MATHEMATICS I\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
EP=re.findall(r'ENGINEERING  PHYSICS\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
EP_pr=re.findall(r'ENGINEERING  PHYSICS\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
WS=re.findall(r'WORKSHOP\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
EG=re.findall(r'ENGINEERING GRAPHICS\s*---\s*\d{3}/\d{3}\s*\d{3}/\d{2}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
EG_tw=re.findall(r'ENGINEERING GRAPHICS\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
bxe=re.findall(r'BASIC ELECTRONICS ENGG.\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
bxe_pr=re.findall(r'BASIC ELECTRONICS ENGG.\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
m2=re.findall(r'ENGINEERING MATHEMATICS II\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
m2_tw=re.findall(r'ENGINEERING MATHEMATICS II\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
EC=re.findall(r'ENGINEERING  CHEMISTRY\s*\d{3}/\d{3}\s*[0-9]+/[0-9]+\s*[0-9]+/[0-9]+\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
EC_pr=re.findall(r'ENGINEERING  CHEMISTRY\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
pps=re.findall(r'PROG. & PROBLEM SOLVING\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*---\s*---\s*[0-9|A-Z]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
pps_pr=re.findall(r'PROG. & PROBLEM SOLVING\s*---\s*---\s*---\s*---\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
pbl=re.findall(r'PROJECT BASED LEARNING\s*---\s*---\s*---\s*\d{3}/\d{3}\s*\d{3}/\d{3}\s*---\s*[0-9]+\s*\d{2}\s*\w{1}\s*\d{2}\s*\d{2}',text_1)
names=re.findall(r'NAME\s*:\s*[A-Z]+\s*[A-Z]+\s[A-Z]+|NAME\s*:\s*[A-Z]+\s*[A-Z]+',text_1)
sgpa=re.findall(r'FIRST YEAR SGPA : --|FIRST YEAR SGPA : [0-9]+.[0-9]+',text_1)
seatno=re.findall(r'SEAT NO.: [A-Z|0-9]+',text_1)
z=''
y=''

for i in range(len(pps)):
    if i==0:
        z=z+names[0][8:]+'\n'
    elif i==len(pps)-1:
        z=z+names[i][7:]
    else:
        z=z+names[i][7:]+'\n'
for u in range(len(pps)):
    if u==len(pps)-1:
        y=y+sgpa[u][18:]
    else:
        y=y+sgpa[u][18:]+'\n'
#print(text_1)
ref_names=z.split('\n')                                     #names
sgpa_ref_0=y.split('\n')
sgpa_ref=[s.replace('--','0')for s in sgpa_ref_0]
#sgpa
#print(sgpa_ref)
#print(ref_names)
new_mech=[s.replace('            ',',')for s in mech]
#new_mech1=[s.replace('')]
#print(ref_names)
#print(sgpa_ref)            
new_mech1=[re.sub(r'0  0','0,0',s)for s in new_mech]          

new_mech2=[re.sub(r'0  1','0,1',s)for s in new_mech1] 
new_mech3=[re.sub(r'    -',',-',s)for s in new_mech2]
new_mech4=[re.sub(r'  ,',',',s)for s in new_mech3]
new_mech5=[re.sub(r'    ',',',s)for s in new_mech4]
new_mech6=[re.sub(r'   ',',',s)for s in new_mech5]
new_mech7=[re.sub(r', ',',',s)for s in new_mech6]
mech_final_0=[re.sub(r'  ',',',s)for s in new_mech7] #final mechanics
mech_final_1=[re.sub(r'/030','',s)for s in mech_final_0]
mech_final_2=[re.sub(r'/070','',s)for s in mech_final_1]
mech_final=[re.sub(r'/100','',s)for s in mech_final_2]

new_em_pr=[re.sub(r'              ',',',s)for s in mech_pr] 
new_em_pr1=[re.sub(r'     ',',',s)for s in new_em_pr] 
new_em_pr2=[re.sub(r'    ',',',s)for s in new_em_pr1] 
new_em_pr3=[re.sub(r'   ',',',s)for s in new_em_pr2] 
mech_pr_final=[re.sub(r'  ',',',s)for s in new_em_pr3] #final pr


new_sme=[re.sub(r'           ',',',s)for s in sme]
new_sme1=[re.sub(r'     ',',',s)for s in new_sme] 
new_sme2=[re.sub(r'    ',',',s)for s in new_sme1] 
new_sme3=[re.sub(r'   ',',',s)for s in new_sme2] 
new_sme4=[re.sub(r'  ',',',s)for s in new_sme3] 
sme_final_0=[re.sub(r', ',',',s)for s in new_sme4] 
sme_final_1=[re.sub(r'/030','',s)for s in sme_final_0]
sme_final_2=[re.sub(r'/070','',s)for s in sme_final_1]
sme_final=[re.sub(r'/100','',s)for s in sme_final_2]#final sme


sme_pr1=[re.sub(r'             ',',',s)for s in sme_pr]
sme_pr2=[re.sub(r'     ',',',s)for s in sme_pr1] 
sme_pr3=[re.sub(r'    ',',',s)for s in sme_pr2] 
sme_pr4=[re.sub(r'   ',',',s)for s in sme_pr3] 
sme_pr5=[re.sub(r'  ',',',s)for s in sme_pr4] 
sme_pr_final=[re.sub(r', ',',',s)for s in sme_pr5]   #final sme pr


bee1=[re.sub(r'           ',',',s)for s in bee]
bee2=[re.sub(r'     ',',',s)for s in bee1] 
bee3=[re.sub(r'    ',',',s)for s in bee2] 
bee4=[re.sub(r'   ',',',s)for s in bee3] 
bee5=[re.sub(r'  ',',',s)for s in bee4] 
bee_final_0=[re.sub(r', ',',',s)for s in bee5]
bee_final_1=[re.sub(r'/030','',s)for s in bee_final_0]
bee_final_2=[re.sub(r'/070','',s)for s in bee_final_1]
bee_final=[re.sub(r'/100','',s)for s in bee_final_2]#final bee



bee_pr1=[re.sub(r'             ',',',s)for s in bee_pr]
bee_pr2=[re.sub(r'     ',',',s)for s in bee_pr1] 
bee_pr3=[re.sub(r'    ',',',s)for s in bee_pr2] 
bee_pr4=[re.sub(r'   ',',',s)for s in bee_pr3] 
bee_pr5=[re.sub(r'  ',',',s)for s in bee_pr4] 
bee_pr_final=[re.sub(r', ',',',s)for s in bee_pr5]    #final bee pr


m1_new=[re.sub(r'        ',',',s)for s in m1]
m1_new1=[re.sub(r'     ',',',s)for s in m1_new] 
m1_new2=[re.sub(r'    ',',',s)for s in m1_new1] 
m1_new3=[re.sub(r'   ',',',s)for s in m1_new2] 
m1_new4=[re.sub(r'  ',',',s)for s in m1_new3] 
m1_final_0=[re.sub(r', ',',',s)for s in m1_new4] 
m1_final_1=[re.sub(r'/030','',s)for s in m1_final_0]
m1_final_2=[re.sub(r'/070','',s)for s in m1_final_1]
m1_final=[re.sub(r'/100','',s)for s in m1_final_2]#m1 final


m1_tw_new=[re.sub(r'          ',',',s)for s in m1_tw]
m1_tw_new1=[re.sub(r'     ',',',s)for s in m1_tw_new] 
m1_tw_new2=[re.sub(r'    ',',',s)for s in m1_tw_new1] 
m1_tw_new3=[re.sub(r'   ',',',s)for s in m1_tw_new2] 
m1_tw_new4=[re.sub(r'  ',',',s)for s in m1_tw_new3] 
m1_tw_final=[re.sub(r', ',',',s)for s in m1_tw_new4]     #final m1 tw

EP0=[re.sub(r'ENGINEERING  PHYSICS','ENGINEERING PHYSICS',s)for s in EP]
EP1=[re.sub(r'             ',',',s)for s in EP0]
EP2=[re.sub(r'     ',',',s)for s in EP1] 
EP3=[re.sub(r'    ',',',s)for s in EP2] 
EP4=[re.sub(r'   ',',',s)for s in EP3]  
EP5=[re.sub(r'  ',',',s)for s in EP4] 
EP_final_0=[re.sub(r', ',',',s)for s in EP5] 
EP_final_1=[re.sub(r'/030','',s)for s in EP_final_0]
EP_final_2=[re.sub(r'/070','',s)for s in EP_final_1]
EP_final=[re.sub(r'/100','',s)for s in EP_final_2]#final EP



EP_pr0=[re.sub(r'ENGINEERING  PHYSICS','ENGINEERING PHYSICS',s)for s in EP_pr]
EP_pr1=[re.sub(r'               ',',',s)for s in EP_pr0]
EP_pr2=[re.sub(r'     ',',',s)for s in EP_pr1] 
EP_pr3=[re.sub(r'    ',',',s)for s in EP_pr2] 
EP_pr4=[re.sub(r'   ',',',s)for s in EP_pr3] 
EP_pr5=[re.sub(r'  ',',',s)for s in EP_pr4] 
EP_pr_final=[re.sub(r', ',',',s)for s in EP_pr5]         #final EP pr


WS1=[re.sub(r'                           ',',',s)for s in WS]
WS2=[re.sub(r'     ',',',s)for s in WS1] 
WS3=[re.sub(r'    ',',',s)for s in WS2] 
WS4=[re.sub(r'   ',',',s)for s in WS3] 
WS5=[re.sub(r'  ',',',s)for s in WS4] 
WS_final_0=[re.sub(r', ',',',s)for s in WS5] 
WS_final_1=[re.sub(r'/030','',s)for s in WS_final_0]
WS_final_2=[re.sub(r'/070','',s)for s in WS_final_1]
WS_final=[re.sub(r'/100','',s)for s in WS_final_2]#final WS




EG1=[re.sub(r'               ',',',s)for s in EG]
EG2=[re.sub(r'     ',',',s)for s in EG1] 
EG3=[re.sub(r'    ',',',s)for s in EG2] 
EG4=[re.sub(r'   ',',',s)for s in EG3] 
EG5=[re.sub(r'  ',',',s)for s in EG4] 
EG_final_0=[re.sub(r', ',',',s)for s in EG5] 
EG_final_1=[re.sub(r'/050','',s)for s in EG_final_0]
EG_final=[re.sub(r'/50','',s)for s in EG_final_1]#final EG


EG_tw1=[re.sub(r'               ',',',s)for s in EG_tw]
EG_tw2=[re.sub(r'     ',',',s)for s in EG_tw1] 
EG_tw3=[re.sub(r'    ',',',s)for s in EG_tw2] 
EG_tw4=[re.sub(r'   ',',',s)for s in EG_tw3] 
EG_tw5=[re.sub(r'  ',',',s)for s in EG_tw4] 
EG_tw_final=[re.sub(r', ',',',s)for s in EG_tw5]              #final EG tw



bxe1=[re.sub(r'          ',',',s)for s in bxe]
bxe2=[re.sub(r'     ',',',s)for s in bxe1] 
bxe3=[re.sub(r'    ',',',s)for s in bxe2] 
bxe4=[re.sub(r'   ',',',s)for s in bxe3] 
bxe5=[re.sub(r'  ',',',s)for s in bxe4] 
bxe_final_0=[re.sub(r', ',',',s)for s in bxe5]  
bxe_final_1=[re.sub(r'/030','',s)for s in bxe_final_0]
bxe_final_2=[re.sub(r'/070','',s)for s in bxe_final_1]
bxe_final=[re.sub(r'/100','',s)for s in bxe_final_2]#final BXE 



bxe_pr1=[re.sub(r'            ',',',s)for s in bxe_pr]
bxe_pr2=[re.sub(r'     ',',',s)for s in bxe_pr1] 
bxe_pr3=[re.sub(r'    ',',',s)for s in bxe_pr2] 
bxe_pr4=[re.sub(r'   ',',',s)for s in bxe_pr3] 
bxe_pr5=[re.sub(r'  ',',',s)for s in bxe_pr4] 
bxe_pr_final=[re.sub(r', ',',',s)for s in bxe_pr5]            #final BXE pr



m2_new=[re.sub(r'       ',',',s)for s in m2]
m2_new1=[re.sub(r'     ',',',s)for s in m2_new] 
m2_new2=[re.sub(r'    ',',',s)for s in m2_new1] 
m2_new3=[re.sub(r'   ',',',s)for s in m2_new2] 
m2_new4=[re.sub(r'  ',',',s)for s in m2_new3] 
m2_final_0=[re.sub(r', ',',',s)for s in m2_new4]
m2_final_1=[re.sub(r'/030','',s)for s in m2_final_0]
m2_final_2=[re.sub(r'/070','',s)for s in m2_final_1]
m2_final=[re.sub(r'/100','',s)for s in m2_final_2]#final m2



m2_tw_new=[re.sub(r'         ',',',s)for s in m2_tw]
m2_tw_new1=[re.sub(r'     ',',',s)for s in m2_tw_new] 
m2_tw_new2=[re.sub(r'    ',',',s)for s in m2_tw_new1] 
m2_tw_new3=[re.sub(r'   ',',',s)for s in m2_tw_new2] 
m2_tw_new4=[re.sub(r'  ',',',s)for s in m2_tw_new3] 
m2_tw_final=[re.sub(r', ',',',s)for s in m2_tw_new4]            #final m2 tw


EC0=[re.sub(r'ENGINEERING  CHEMISTRY','ENGINEERING CHEMISTRY',s)for s in EC]
EC1=[re.sub(r'           ',',',s)for s in EC0]
EC2=[re.sub(r'     ',',',s)for s in EC1] 
EC3=[re.sub(r'    ',',',s)for s in EC2] 
EC4=[re.sub(r'   ',',',s)for s in EC3]  
EC5=[re.sub(r'  ',',',s)for s in EC4] 
EC_final_0=[re.sub(r', ',',',s)for s in EC5] 
EC_final_1=[re.sub(r'/030','',s)for s in EC_final_0]
EC_final_2=[re.sub(r'/070','',s)for s in EC_final_1]
EC_final=[re.sub(r'/100','',s)for s in EC_final_2]#final EC




EC_pr0=[re.sub(r'ENGINEERING  CHEMISTRY','ENGINEERING CHEMISTRY',s)for s in EC_pr]
EC_pr1=[re.sub(r'             ',',',s)for s in EC_pr0]
EC_pr2=[re.sub(r'     ',',',s)for s in EC_pr1] 
EC_pr3=[re.sub(r'    ',',',s)for s in EC_pr2] 
EC_pr4=[re.sub(r'   ',',',s)for s in EC_pr3] 
EC_pr5=[re.sub(r'  ',',',s)for s in EC_pr4] 
EC_pr_final=[re.sub(r', ',',',s)for s in EC_pr5]                 #final EC pr



pps1=[re.sub(r'          ',',',s)for s in pps]
pps2=[re.sub(r'     ',',',s)for s in pps1] 
pps3=[re.sub(r'    ',',',s)for s in pps2] 
pps4=[re.sub(r'   ',',',s)for s in pps3] 
pps5=[re.sub(r'  ',',',s)for s in pps4] 
pps_final_0=[re.sub(r', ',',',s)for s in pps5]
pps_final_1=[re.sub(r'/030','',s)for s in pps_final_0]
pps_final_2=[re.sub(r'/070','',s)for s in pps_final_1]
pps_final=[re.sub(r'/100','',s)for s in pps_final_2]#final pps



pps_pr1=[re.sub(r'            ',',',s)for s in pps_pr]
pps_pr2=[re.sub(r'     ',',',s)for s in pps_pr1] 
pps_pr3=[re.sub(r'    ',',',s)for s in pps_pr2] 
pps_pr4=[re.sub(r'   ',',',s)for s in pps_pr3] 
pps_pr5=[re.sub(r'  ',',',s)for s in pps_pr4] 
pps_pr_final=[re.sub(r', ',',',s)for s in pps_pr5]                #final pps pr



pbl1=[re.sub(r'             ',',',s)for s in pbl]
pbl2=[re.sub(r'     ',',',s)for s in pbl1] 
pbl3=[re.sub(r'    ',',',s)for s in pbl2] 
pbl4=[re.sub(r'   ',',',s)for s in pbl3] 
pbl5=[re.sub(r'  ',',',s)for s in pbl4] 
pbl_final_0=[re.sub(r', ',',',s)for s in pbl5] 
pbl_final_1=[re.sub(r'/030','',s)for s in pbl_final_0]
pbl_final_2=[re.sub(r'/070','',s)for s in pbl_final_1]
pbl_final=[re.sub(r'/100','',s)for s in pbl_final_2]#PBL final


h=['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']
rows=EC_final
df=pd.DataFrame(rows,columns=["Row"])
df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=df["Row"].str.split(',',expand=True)
df=df.drop("Row",axis=1)
#print(df.iloc[:])
#print(ref_names)
sno=[re.sub(r'SEAT NO.: ','',s)for s in seatno] 


#Chem df
chem_rows=EC_final
chem_df=pd.DataFrame(chem_rows,columns=["Row"])
chem_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=chem_df["Row"].str.split(',',expand=True)
chem_df=chem_df.drop("Row",axis=1)
chem_df['SGPA']=sgpa_ref
chem_df['NAME']=ref_names
chem_df['SEAT NO']=sno
chem_df['ISE'] = chem_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
chem_df['ESE'] = chem_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
chem_df.replace('FF', np.nan, inplace=True)
chem_df['Tot%'] = chem_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
chem_df['SGPA'] = chem_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)
#chem_df['SEAT NO']=sno
#print(df.iloc[:])
#print(ref_names)

#chem_df.to_csv('D:\\fe\\pbl\\mks\\chem.csv')

#Chem pr
chem_pr_rows=EC_pr_final
chem_pr_df=pd.DataFrame(chem_pr_rows,columns=["Row"])
chem_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=chem_pr_df["Row"].str.split(',',expand=True)
chem_pr_df=chem_pr_df.drop("Row",axis=1)
chem_pr_df['SGPA']=sgpa_ref
chem_pr_df['NAME']=ref_names
chem_pr_df['SEAT NO']=sno

#chem_pr_df.to_csv('D:\\fe\\pbl\\mks\\chem_pr.csv')

#Mechanics pr df
mech_pr_rows=mech_pr_final
mech_pr_df=pd.DataFrame(mech_pr_rows,columns=["Row"])
mech_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=mech_pr_df["Row"].str.split(',',expand=True)
mech_pr_df=mech_pr_df.drop("Row",axis=1)
mech_pr_df['SGPA']=sgpa_ref
mech_pr_df['NAME']=ref_names
mech_pr_df['SEAT NO']=sno

#mech_pr_df.to_csv('D:\\fe\\pbl\\mks\\mech_pr.csv')

#mechanics
mech_rows=mech_final
mech_df=pd.DataFrame(mech_rows,columns=["Row"])
mech_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=mech_df["Row"].str.split(',',expand=True)
mech_df=mech_df.drop("Row",axis=1)
mech_df['SGPA']=sgpa_ref
mech_df['NAME']=ref_names
mech_df['SEAT NO']=sno
mech_df['ISE'] = mech_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
mech_df['ESE'] = mech_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
mech_df.replace('FF', np.nan, inplace=True)
mech_df['Tot%'] = mech_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
mech_df['SGPA'] = mech_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#mech_df.to_csv('D:\\fe\\pbl\\mks\\mech.csv')

#eg
eg_rows=EG_final
eg_df=pd.DataFrame(eg_rows,columns=["Row"])
eg_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=eg_df["Row"].str.split(',',expand=True)
eg_df=eg_df.drop("Row",axis=1)
eg_df['SGPA']=sgpa_ref
eg_df['NAME']=ref_names
eg_df['SEAT NO']=sno
eg_df['ESE'] = eg_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
eg_df.replace('FF', np.nan, inplace=True)
eg_df['Tot%'] = eg_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
eg_df['SGPA'] = eg_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#eg_df.to_csv('D:\\fe\\pbl\\mks\\eg.csv')


#eg tw
eg_tw_rows=EG_tw_final
eg_tw_df=pd.DataFrame(eg_tw_rows,columns=["Row"])
eg_tw_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=eg_tw_df["Row"].str.split(',',expand=True)
eg_tw_df=eg_tw_df.drop("Row",axis=1)
eg_tw_df['SGPA']=sgpa_ref
eg_tw_df['NAME']=ref_names
eg_tw_df['SEAT NO']=sno

#eg_tw_df.to_csv('D:\\fe\\pbl\\mks\\eg_tw.csv')

#m1
m1_rows=m1_final
m1_df=pd.DataFrame(m1_rows,columns=["Row"])
m1_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=m1_df["Row"].str.split(',',expand=True)
m1_df=m1_df.drop("Row",axis=1)
m1_df['SGPA']=sgpa_ref
m1_df['NAME']=ref_names
m1_df['SEAT NO']=sno
m1_df['ISE'] = m1_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
m1_df['ESE'] = m1_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
m1_df.replace('FF', np.nan, inplace=True)
m1_df['Tot%'] = m1_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
m1_df['SGPA'] = m1_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#m1_df.to_csv('D:\\fe\\pbl\\mks\\m1.csv')

#m1 tw
m1_tw_rows=m1_tw_final
m1_tw_df=pd.DataFrame(m1_tw_rows,columns=["Row"])
m1_tw_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=m1_tw_df["Row"].str.split(',',expand=True)
m1_tw_df=m1_tw_df.drop("Row",axis=1)
m1_tw_df['SGPA']=sgpa_ref
m1_tw_df['NAME']=ref_names
m1_tw_df['SEAT NO']=sno

#m1_tw_df.to_csv('D:\\fe\\pbl\\mks\\m1_tw.csv')

#m2
m2_rows=m2_final
m2_df=pd.DataFrame(m2_rows,columns=["Row"])
m2_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=m2_df["Row"].str.split(',',expand=True)
m2_df=m2_df.drop("Row",axis=1)
m2_df['SGPA']=sgpa_ref
m2_df['NAME']=ref_names
m2_df['SEAT NO']=sno
m2_df['ISE'] = m2_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
m2_df['ESE'] = m2_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
m2_df.replace('FF', np.nan, inplace=True)
m2_df['Tot%'] = m2_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
m2_df['SGPA'] = m2_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#m2_df.to_csv('D:\\fe\\pbl\\mks\\m2.csv')

#m2 tw
m2_tw_rows=m2_tw_final
m2_tw_df=pd.DataFrame(m2_tw_rows,columns=["Row"])
m2_tw_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=m2_tw_df["Row"].str.split(',',expand=True)
m2_tw_df=m2_tw_df.drop("Row",axis=1)
m2_tw_df['SGPA']=sgpa_ref
m2_tw_df['NAME']=ref_names
m2_tw_df['SEAT NO']=sno

#m2_tw_df.to_csv('D:\\fe\\pbl\\mks\\m2_tw.csv')

#pps
pps_rows=pps_final
pps_df=pd.DataFrame(pps_rows,columns=["Row"])
pps_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=pps_df["Row"].str.split(',',expand=True)
pps_df=pps_df.drop("Row",axis=1)
pps_df['SGPA']=sgpa_ref
pps_df['NAME']=ref_names
pps_df['SEAT NO']=sno
pps_df['ISE'] = pps_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
pps_df['ESE'] = pps_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
pps_df.replace('FF', np.nan, inplace=True)
pps_df['Tot%'] = pps_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
pps_df['SGPA'] = pps_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#pps_df.to_csv('D:\\fe\\pbl\\mks\\pps.csv')


#pps pr
pps_pr_rows=pps_pr_final
pps_pr_df=pd.DataFrame(pps_pr_rows,columns=["Row"])
pps_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=pps_pr_df["Row"].str.split(',',expand=True)
pps_pr_df=pps_pr_df.drop("Row",axis=1)
pps_pr_df['SGPA']=sgpa_ref
pps_pr_df['NAME']=ref_names
pps_pr_df['SEAT NO']=sno

#pps_pr_df.to_csv('D:\\fe\\pbl\\mks\\pps_pr.csv')

#sme
sme_rows=sme_final
sme_df=pd.DataFrame(sme_rows,columns=["Row"])
sme_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=sme_df["Row"].str.split(',',expand=True)
sme_df=sme_df.drop("Row",axis=1)
sme_df['SGPA']=sgpa_ref
sme_df['NAME']=ref_names
sme_df['SEAT NO']=sno
sme_df['ISE'] = sme_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
sme_df['ESE'] = sme_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
sme_df.replace('FF', np.nan, inplace=True)
sme_df['Tot%'] = sme_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
sme_df['SGPA'] = sme_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#sme_df.to_csv('D:\\fe\\pbl\\mks\\sme.csv')


#sme pr
sme_pr_rows=sme_pr_final
sme_pr_df=pd.DataFrame(sme_pr_rows,columns=["Row"])
sme_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=sme_pr_df["Row"].str.split(',',expand=True)
sme_pr_df=sme_pr_df.drop("Row",axis=1)
sme_pr_df['SGPA']=sgpa_ref
sme_pr_df['NAME']=ref_names
sme_pr_df['SEAT NO']=sno

#sme_pr_df.to_csv('D:\\fe\\pbl\\mks\\sme_pr.csv')


#pbl
pbl_rows=pbl_final
pbl_df=pd.DataFrame(pbl_rows,columns=["Row"])
pbl_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=pbl_df["Row"].str.split(',',expand=True)
pbl_df=pbl_df.drop("Row",axis=1)
pbl_df['SGPA']=sgpa_ref
pbl_df['NAME']=ref_names
pbl_df['SEAT NO']=sno
pbl_df.replace('FF', np.nan, inplace=True)
pbl_df['Tot%'] = pbl_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
pbl_df['SGPA'] = pbl_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#pbl_df.to_csv('D:\\fe\\pbl\\mks\\pbl.csv')

#bee
bee_rows=bee_final
bee_df=pd.DataFrame(bee_rows,columns=["Row"])
bee_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=bee_df["Row"].str.split(',',expand=True)
bee_df=bee_df.drop("Row",axis=1)
bee_df['SGPA']=sgpa_ref
bee_df['NAME']=ref_names
bee_df['SEAT NO']=sno
bee_df['ISE'] = bee_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
bee_df['ESE'] = bee_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
bee_df.replace('FF', np.nan, inplace=True)
bee_df['Tot%'] = bee_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
bee_df['SGPA'] = bee_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)

#bee_df.to_csv('D:\\fe\\pbl\\mks\\bee.csv')

#bee pr
bee_pr_rows=bee_pr_final
bee_pr_df=pd.DataFrame(bee_pr_rows,columns=["Row"])
bee_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=bee_pr_df["Row"].str.split(',',expand=True)
bee_pr_df=bee_pr_df.drop("Row",axis=1)
bee_pr_df['SGPA']=sgpa_ref
bee_pr_df['NAME']=ref_names
bee_pr_df['SEAT NO']=sno
#bee_pr_df.to_csv('D:\\fe\\pbl\\mks\\bee_pr.csv')


#bxe
bxe_rows=bxe_final
bxe_df=pd.DataFrame(bxe_rows,columns=["Row"])
bxe_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=bxe_df["Row"].str.split(',',expand=True)
bxe_df=bxe_df.drop("Row",axis=1)
bxe_df['SGPA']=sgpa_ref
bxe_df['NAME']=ref_names
bxe_df['SEAT NO']=sno
bxe_df['ISE'] = bxe_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
bxe_df['ESE'] = bxe_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
bxe_df.replace('FF', np.nan, inplace=True)
bxe_df['Tot%'] = bxe_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
bxe_df['SGPA'] = bxe_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)
#bxe_df.to_csv('D:\\fe\\pbl\\mks\\bxe.csv')

#bxe pr
bxe_pr_rows=bxe_pr_final
bxe_pr_df=pd.DataFrame(bxe_pr_rows,columns=["Row"])
bxe_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=bxe_pr_df["Row"].str.split(',',expand=True)
bxe_pr_df=bxe_pr_df.drop("Row",axis=1)
bxe_pr_df['SGPA']=sgpa_ref
bxe_pr_df['NAME']=ref_names
bxe_pr_df['SEAT NO']=sno
#bxe_pr_df.to_csv('D:\\fe\\pbl\\mks\\bxe_pr.csv')

#phy
ep_rows=EP_final
ep_df=pd.DataFrame(ep_rows,columns=["Row"])
ep_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=ep_df["Row"].str.split(',',expand=True)
ep_df=ep_df.drop("Row",axis=1)
ep_df['SGPA']=sgpa_ref
ep_df['NAME']=ref_names
ep_df['SEAT NO']=sno
ep_df['ISE'] = ep_df['ISE'].replace('NaN', pd.NA).fillna(0).astype(int)
ep_df['ESE'] = ep_df['ESE'].replace('NaN', pd.NA).fillna(0).astype(int)
ep_df.replace('FF', np.nan, inplace=True)
ep_df['Tot%'] = ep_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
ep_df['SGPA'] = ep_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)
#ep_df.to_csv('D:\\fe\\pbl\\mks\\ep.csv')

#phy pr
ep_pr_rows=EP_pr_final
ep_pr_df=pd.DataFrame(ep_pr_rows,columns=["Row"])
ep_pr_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=ep_pr_df["Row"].str.split(',',expand=True)
ep_pr_df=ep_pr_df.drop("Row",axis=1)
ep_pr_df['SGPA']=sgpa_ref
ep_pr_df['NAME']=ref_names
ep_pr_df['SEAT NO']=sno
#ep_pr_df.to_csv('D:\\fe\\pbl\\mks\\ep_pr.csv')

#ws
ws_rows=WS_final
ws_df=pd.DataFrame(ws_rows,columns=["Row"])
ws_df[['COURSE NAME','ISE','ESE','TOTAL','TW','PR','OR','Tot%','Crd','Grd','GP','CP']]=ws_df["Row"].str.split(',',expand=True)
ws_df=ws_df.drop("Row",axis=1)
ws_df['SGPA']=sgpa_ref
ws_df['NAME']=ref_names
ws_df['SEAT NO']=sno
ws_df.replace('FF', np.nan, inplace=True)
ws_df['Tot%'] = ws_df['Tot%'].replace('NaN', pd.NA).fillna(0).astype(int)
ws_df['SGPA'] = ws_df['SGPA'].replace('NaN', pd.NA).fillna(0).astype(float)
#ws_df.to_csv('D:\\fe\\pbl\\mks\\ws.csv')


# Save CSV files in the user-provided directory
chem_df.to_csv(os.path.join(save_dir, 'chem.csv'))
chem_pr_df.to_csv(os.path.join(save_dir, 'chem_pr.csv'))
mech_pr_df.to_csv(os.path.join(save_dir, 'mech_pr.csv'))
mech_df.to_csv(os.path.join(save_dir, 'mech.csv'))
eg_df.to_csv(os.path.join(save_dir, 'eg.csv'))
eg_tw_df.to_csv(os.path.join(save_dir, 'eg_tw.csv'))
m1_df.to_csv(os.path.join(save_dir, 'm1.csv'))
m1_tw_df.to_csv(os.path.join(save_dir, 'm1_tw.csv'))
m2_df.to_csv(os.path.join(save_dir, 'm2.csv'))
m2_tw_df.to_csv(os.path.join(save_dir, 'm2_tw.csv'))
pps_df.to_csv(os.path.join(save_dir, 'pps.csv'))
pps_pr_df.to_csv(os.path.join(save_dir, 'pps_pr.csv'))
sme_df.to_csv(os.path.join(save_dir, 'sme.csv'))
sme_pr_df.to_csv(os.path.join(save_dir, 'sme_pr.csv'))
pbl_df.to_csv(os.path.join(save_dir, 'pbl.csv'))
bee_df.to_csv(os.path.join(save_dir, 'bee.csv'))
bee_pr_df.to_csv(os.path.join(save_dir, 'bee_pr.csv'))
bxe_df.to_csv(os.path.join(save_dir, 'bxe.csv'))
bxe_pr_df.to_csv(os.path.join(save_dir, 'bxe_pr.csv'))
ep_df.to_csv(os.path.join(save_dir, 'ep.csv'))
ep_pr_df.to_csv(os.path.join(save_dir, 'ep_pr.csv'))
ws_df.to_csv(os.path.join(save_dir, 'ws.csv'))



def tot_analysis():
    i=len(pps)-1
    max_chem=0
    while i>=0:
        if chem_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(chem_df['Tot%'].values[i])>max_chem:
            max_chem=int(chem_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_ep=0
    while i>=0:
        if ep_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(ep_df['Tot%'].values[i])>max_ep:
            max_ep=int(ep_df['Tot%'].values[i])
        i-=1
        
    i=len(pps)-1
    max_mech=0
    while i>=0:
        if mech_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(mech_df['Tot%'].values[i])>max_mech:
            max_mech=int(mech_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_bee=0
    while i>=0:
        if bee_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(bee_df['Tot%'].values[i])>max_bee:
            max_bee=int(bee_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_pps=0
    while i>=0:
        if pps_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(pps_df['Tot%'].values[i])>max_pps:
            max_pps=int(pps_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_bxe=0
    while i>=0:
        if bxe_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(bxe_df['Tot%'].values[i])>max_bxe:
            max_bxe=int(bxe_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_EG=0
    while i>=0:
        if eg_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(eg_df['Tot%'].values[i])>max_EG:
            max_EG=int(eg_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_sme=0
    while i>=0:
        if sme_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(sme_df['Tot%'].values[i])>max_sme:
            max_sme=int(sme_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_m1=0
    while i>=0:
        if m1_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(m1_df['Tot%'].values[i])>max_m1:
            max_m1=int(m1_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_m2=0
    while i>=0:
        if m2_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(m2_df['Tot%'].values[i])>max_m2:
            max_m2=int(m2_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_ws=0
    while i>=0:
        if ws_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(ws_df['Tot%'].values[i])>max_ws:
            max_ws=int(ws_df['Tot%'].values[i])
        i-=1
    i=len(pps)-1
    max_pbl=0
    while i>=0:
        if pbl_df['Tot%'].values[i]=='FF':
            i-=1
            continue
        elif int(pbl_df['Tot%'].values[i])>max_pbl:
            max_pbl=int(pbl_df['Tot%'].values[i])
        i-=1
    names_max_bee = bee_df[bee_df['Tot%'] == max_bee]['NAME'].values
    names_max_bxe = bxe_df[bxe_df['Tot%'] == max_bxe]['NAME'].values
    names_max_ep = ep_df[ep_df['Tot%'] == max_ep]['NAME'].values
    names_max_chem = chem_df[chem_df['Tot%'] == max_chem]['NAME'].values
    names_max_sme = sme_df[sme_df['Tot%'] == max_sme]['NAME'].values
    names_max_pps = pps_df[pps_df['Tot%'] == max_pps]['NAME'].values
    names_max_m1 = m1_df[m1_df['Tot%'] == max_m1]['NAME'].values
    names_max_m2 = m2_df[m2_df['Tot%'] == max_m2]['NAME'].values
    names_max_mech = mech_df[mech_df['Tot%'] == max_mech]['NAME'].values
    names_max_EG = eg_df[eg_df['Tot%'] == max_EG]['NAME'].values
    names_max_pbl = pbl_df[pbl_df['Tot%'] == max_pbl]['NAME'].values
    names_max_ws = ws_df[ws_df['Tot%'] == max_ws]['NAME'].values
    print('PHYSICS HIGHEST MARKS : ',max_ep)
    print('PHYSICS TOPPERS : ',names_max_ep)
    print('CHEMISTRY HIGHEST MARKS : ',max_chem)
    print('CHEMISTRY TOPPERS : ',names_max_chem)
    print('SME HIGHEST MARKS : ',max_sme)
    print('SME TOPPERS : ',names_max_sme)
    print('PPS HIGHEST MARKS : ',max_pps)
    print('PPS TOPPERS : ',names_max_pps)
    print('BEE HIGHEST MARKS : ',max_bee)
    print('BEE TOPPERS : ',names_max_bee)
    print('BXE HIGHEST MARKS : ',max_bxe)
    print('BXE TOPPERS : ',names_max_bxe)
    print('EM-I HIGHEST MARKS : ',max_m1)
    print('EM-I TOPPERS : ',names_max_m1)
    print('EM-II HIGHEST MARKS : ',max_m2)
    print('EM-II TOPPERS : ',names_max_m2)
    print('MECHANICS HIGHEST MARKS : ',max_mech)
    print('MECHANICS TOPPERS : ',names_max_mech)
    print('ENGINEERING GRAPHICS HIGHEST MARKS : ',max_EG)
    print('ENGINEERING GRAPHICS TOPPERS : ',names_max_EG)
    print('PROJECT BASED LEARNING HIGHEST MARKS : ',max_pbl)
    print('PROJECT BASED LEARNING TOPPERS : ',names_max_pbl)
    print('WORKSHOP HIGHEST MARKS : ',max_ws)
    print('WORKSHOP TOPPERS : ',names_max_ws)
    
tot_analysis()

#print(ws_df)

#graphs

def chem_graph():
    chem_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('Chemistry graph')
    pl.show()
    
def mech_graph():
    mech_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('Mechanics graph')
    pl.show()
    
def ep_graph():
    ep_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('Physics graph')
    pl.show()
    
def bxe_graph():
    bxe_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('BXE graph')
    pl.show()
    
def bee_graph():
    bee_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('BEE graph')
    pl.show()

def m1_graph():
    m1_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('M1 graph')
    pl.show()
    
def m2_graph():
    m2_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('M2 graph')
    pl.show()
    
def sme_graph():
    sme_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('SME graph')
    pl.show()

def pps_graph():
    pps_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('PPS graph')
    pl.show()

def pbl_graph():
    pbl_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('PBL graph')
    pl.show()

def ws_graph():
    ws_df.plot(kind='bar',x='SEAT NO',y=['Tot%'])
    pl.title('WS graph')
    pl.show()


